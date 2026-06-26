#!/usr/bin/env python3
"""email_asset_pipeline.py: the GitHub-to-Ortto email asset pipeline driver.

Architecture (Ahmed's): GitHub is the SOURCE of truth for each instructor's email images, Ortto
is the SERVE host. The bytes live committed under assets/email/<slug>/ in this repo, and the live
email img src is the Ortto serve URL once the same bytes are uploaded there. This script drives the
source-to-serve map context/subjects/email-asset-pipeline.json: it reports state, fetches the
CloudFront cover bytes into their github_path, and (once Ortto upload access exists) records the
returned serve URL back into the map.

Why a serve host at all: the repo is private, so a GitHub raw URL will not render in an email
client, and a raw CloudFront object is hotlink-protected (a different fetch path can 403). So GitHub
holds the source and Ortto serves. The email-asset-qa gate blocks any send while a header is not on
an approved Ortto host, and this map is the source of truth for that serve URL.

Campaign-agnostic: every instructor, class, source URL, fileId, and path is read from the map, never
hard-coded here. Stdlib plus curl only. Idempotent: re-running fetch skips files already on disk,
re-running upload skips rows already served. House style, by code point: no em dash, no en dash, no
tatweel, Western numerals only, so this source carries no literal forbidden character.

Modes:
  status         Read the map. Per image, report present-on-disk vs missing and served vs pending.
                 Default mode.
  fetch-covers   Download every CloudFront cover in the map into its github_path with curl. Runs in
                 an open-network environment (CI or local). In the locked-egress sandbox every fetch
                 403s, so each item fails gracefully and prints the egress-blocked notice, no crash.
  upload-ortto   The interface where each fetched github_path is uploaded to the Ortto serve CDN and
                 the returned URL is written back into the map as ortto_serve_url with status served.
                 The map write-back is implemented; the actual Ortto API call is a TODO gated on
                 Ahmed's adoption of Ortto upload access (no endpoint or key is invented here).

Drive body portraits are NOT fetched by this script: a script cannot call the Drive MCP. They are
pulled by an agent via mcp__Google_Drive__download_file_content into the same github_path, then this
script's upload-ortto stages them. See context/subjects/_EMAIL-ASSET-PIPELINE.md.

Usage:
  python3 .claude/scripts/email_asset_pipeline.py [status]
  python3 .claude/scripts/email_asset_pipeline.py fetch-covers
  python3 .claude/scripts/email_asset_pipeline.py upload-ortto

Exit 0: the mode completed (status always; fetch/upload when nothing was left in an error state).
Exit 1: at least one item ended in an error state (a fetch failed, or an upload was requested while
        Ortto access is not configured). Exit 2: usage error.
"""

import json
import os
import re
import subprocess
import sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MAP_PATH = os.path.join(BASE, "context", "instructors", "email-asset-pipeline.json")

# Forbidden set, same as scripts/house_style_sweep.py: em dash, en dash, tatweel, and the
# Arabic-Indic and extended Arabic-Indic numerals. Built by code point so this source carries no
# literal forbidden character. Used to guard any string written back into the map.
FORBIDDEN = re.compile(
    "[" + chr(0x2014) + chr(0x2013) + chr(0x0640)
    + chr(0x0660) + "-" + chr(0x0669)
    + chr(0x06F0) + "-" + chr(0x06F9) + "]"
)


def load_map():
    if not os.path.isfile(MAP_PATH):
        print("FAIL: missing map " + os.path.relpath(MAP_PATH, BASE))
        sys.exit(1)
    with open(MAP_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_map(data):
    """Write the map back, preserving non-ASCII (Arabic) and stable indentation.

    Guards the serialized form against the forbidden set so a write-back can never smuggle an em
    dash or an Eastern numeral into the committed map.
    """
    txt = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    hits = FORBIDDEN.findall(txt)
    if hits:
        uniq = " ".join(sorted({hex(ord(c)) for c in hits}))
        print("FAIL: refusing to write map, forbidden char(s): " + uniq)
        sys.exit(1)
    with open(MAP_PATH, "w", encoding="utf-8") as f:
        f.write(txt)


def abspath(github_path):
    """Resolve a map github_path (assets/email/<slug>/<name>) to an absolute path in this repo."""
    return os.path.join(BASE, github_path)


def on_disk(github_path):
    p = abspath(github_path)
    return os.path.isfile(p) and os.path.getsize(p) > 0


def is_served(row):
    url = row.get("ortto_serve_url", "pending")
    return bool(url) and url != "pending"


def mode_status(data):
    """Report per image: present-on-disk vs missing, and served vs pending. Read-only."""
    images = data.get("images", [])
    print("email_asset_pipeline status: " + os.path.relpath(MAP_PATH, BASE))
    print("source of truth: " + str(data.get("source_of_truth")) + " | serve host: "
          + str(data.get("serve_host")))
    present = missing = served = pending = blocked = 0
    for row in images:
        gp = row.get("github_path", "")
        disk = on_disk(gp)
        serve = is_served(row)
        st = row.get("status", "")
        disk_s = "on-disk " if disk else "MISSING "
        serve_s = "served " if serve else "pending"
        tag = row["slug"] + "/" + row["role"] + " (" + row.get("lang", "") + ")"
        print("  [" + disk_s + serve_s + " " + st.ljust(13) + "] " + tag + " -> " + gp)
        present += 1 if disk else 0
        missing += 0 if disk else 1
        served += 1 if serve else 0
        pending += 0 if serve else 1
        blocked += 1 if st == "blocked" else 0
    print("summary: " + str(len(images)) + " image(s) | on-disk " + str(present)
          + ", missing " + str(missing) + " | served " + str(served) + ", serve-pending "
          + str(pending) + " | blocked " + str(blocked))
    print("note: any row not 'served' is a send-blocking state for email-asset-qa "
          "(pending-fetch / fetched / pending-ortto / blocked all block the send).")
    return 0


def _curl(url, dest):
    """Fetch url to dest with curl, failing on HTTP error. Returns (ok, message)."""
    tmp = dest + ".part"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    cmd = ["curl", "--fail", "--silent", "--show-error", "--location",
           "--max-time", "60", "--output", tmp, url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        return False, "curl not found on PATH"
    if r.returncode != 0:
        if os.path.exists(tmp):
            os.remove(tmp)
        err = (r.stderr or "").strip().splitlines()
        return False, (err[-1] if err else ("curl exit " + str(r.returncode)))
    if not os.path.exists(tmp) or os.path.getsize(tmp) == 0:
        if os.path.exists(tmp):
            os.remove(tmp)
        return False, "empty download"
    os.replace(tmp, dest)
    return True, "fetched " + str(os.path.getsize(dest)) + " bytes"


def mode_fetch_covers(data):
    """Download every CloudFront cover into its github_path. Open-network step.

    Idempotent: a cover already on disk is left as is. Drive portraits are skipped (an agent fetches
    them via the Drive MCP). A blocked row is skipped. Each failed fetch (the sandbox 403s) is
    reported per item without crashing the run.
    """
    images = data.get("images", [])
    print("email_asset_pipeline fetch-covers (open-network): " + os.path.relpath(MAP_PATH, BASE))
    fetched = skipped = failed = 0
    egress_blocked = False
    changed = False
    for row in images:
        if row.get("source_kind") != "cloudfront-cover":
            continue
        if row.get("status") == "blocked":
            print("  skip (blocked): " + row["slug"] + "/" + row["role"] + " -> "
                  + str(row.get("blocked_reason", "")))
            skipped += 1
            continue
        gp = row["github_path"]
        if on_disk(gp):
            print("  skip (already on disk): " + gp)
            # Keep the map honest: an on-disk cover that is still pending-fetch becomes pending-ortto.
            if row.get("status") == "pending-fetch":
                row["status"] = "pending-ortto"
                changed = True
            skipped += 1
            continue
        url = row["source"]
        ok, msg = _curl(url, abspath(gp))
        if ok:
            print("  fetched: " + gp + " (" + msg + ")")
            row["status"] = "pending-ortto"
            changed = True
            fetched += 1
        else:
            low = msg.lower()
            if "403" in low or "forbidden" in low or "denied" in low or "could not resolve" in low \
                    or "timed out" in low or "connection" in low:
                egress_blocked = True
            print("  FAILED: " + gp + " (" + msg + ")")
            failed += 1
    if changed:
        save_map(data)
    print("fetch summary: fetched " + str(fetched) + ", skipped " + str(skipped)
          + ", failed " + str(failed))
    if egress_blocked:
        print("egress blocked, run where network is open (CI or local). The locked sandbox cannot "
              "reach CloudFront; this step is expected to 403 here and to succeed in an "
              "open-network environment. The map is unchanged for failed items.")
    return 1 if failed else 0


def _ortto_configured():
    """Whether Ortto upload access is configured. Gated on adoption: today it is not.

    Adoption is Ahmed's call and lands as a settings.json allowlist plus the credentials supplied as
    environment variables (the engine never inlines a key). Until then this returns False and
    upload-ortto reports the interface without inventing an endpoint or a key.
    """
    return bool(os.environ.get("ORTTO_API_KEY")) and bool(os.environ.get("ORTTO_UPLOAD_URL"))


def _upload_one_to_ortto(local_path, row):
    """Upload one fetched asset to the Ortto serve CDN and return its served URL.

    TODO(ortto-adoption): implement the real upload once Ahmed approves Ortto upload access. The
    contract, so the call site and the map write-back are already correct:
      - inputs: the local bytes at local_path (a committed assets/email/<slug>/ file) and the row
        for context (slug, class, role, lang).
      - auth: ORTTO_API_KEY from the environment, never inlined (per the .mcp.json secrets rule).
      - endpoint: the Ortto asset upload endpoint from ORTTO_UPLOAD_URL. NOT invented here: the real
        path and request shape are filled in at adoption from Ortto's documented API.
      - returns: the public Ortto serve URL (on an approved host, m.autopilotapp.com /
        ic.autopilotapp.com) that becomes ortto_serve_url, or raises on failure.
    This function is intentionally not implemented: calling it before adoption is a hard stop, never
    a guessed endpoint or a fake URL.
    """
    raise NotImplementedError(
        "Ortto upload is not adopted yet. Implement _upload_one_to_ortto at adoption: auth with "
        "ORTTO_API_KEY, POST the bytes to ORTTO_UPLOAD_URL, return the served URL. Do not invent "
        "an endpoint or a key.")


def mode_upload_ortto(data):
    """Upload each fetched github_path to Ortto and write the served URL back into the map.

    The interface and the map write-back are implemented. The actual API call is gated on adoption:
    when Ortto access is not configured this reports the queue and stops, inventing nothing.
    """
    images = data.get("images", [])
    print("email_asset_pipeline upload-ortto: " + os.path.relpath(MAP_PATH, BASE))
    if not _ortto_configured():
        queue = [r for r in images
                 if r.get("status") != "blocked" and on_disk(r["github_path"]) and not is_served(r)]
        print("Ortto upload access is NOT configured (no ORTTO_API_KEY / ORTTO_UPLOAD_URL in the "
              "environment, and Ortto is not yet an adopted, settings.json-allowlisted host).")
        print("Interface is ready. When Ahmed approves Ortto upload access, this mode uploads each "
              "fetched asset and writes ortto_serve_url + status 'served' back into the map.")
        print("Queued (fetched, on disk, not yet served): " + str(len(queue)) + " asset(s).")
        for r in queue:
            print("  ready-to-upload: " + r["github_path"])
        print("Blocked rows and not-yet-fetched rows are excluded from the queue.")
        return 1
    # Adopted path: upload each fetched, not-yet-served, non-blocked asset and record the URL.
    uploaded = failed = 0
    changed = False
    for row in images:
        if row.get("status") == "blocked" or is_served(row):
            continue
        gp = row["github_path"]
        if not on_disk(gp):
            continue
        try:
            url = _upload_one_to_ortto(abspath(gp), row)
        except Exception as e:  # noqa: BLE001 (report and continue, never crash the batch)
            print("  upload FAILED: " + gp + " (" + str(e) + ")")
            failed += 1
            continue
        if FORBIDDEN.search(url or ""):
            print("  upload FAILED: " + gp + " (returned url has a forbidden char)")
            failed += 1
            continue
        row["ortto_serve_url"] = url
        row["status"] = "served"
        changed = True
        uploaded += 1
        print("  uploaded + served: " + gp + " -> " + url)
    if changed:
        save_map(data)
    print("upload summary: uploaded " + str(uploaded) + ", failed " + str(failed))
    return 1 if failed else 0


MODES = {"status": mode_status, "fetch-covers": mode_fetch_covers, "upload-ortto": mode_upload_ortto}


def main(argv):
    mode = argv[1] if len(argv) > 1 else "status"
    if mode not in MODES:
        print(__doc__)
        return 2
    data = load_map()
    return MODES[mode](data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

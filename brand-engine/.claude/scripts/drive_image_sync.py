#!/usr/bin/env python3
"""Drive image sync: build the approved-instructor-image catalog from Drive listings.

Campaigns must use real, rights-cleared author images and never a generated likeness
(context/subjects/README.md, the briefs, and the 05-visual-prompts "REAL ASSET REQUIRED"
rule). This script turns a Google Drive photography-folder listing into catalog rows so a
designer can find the right approved image for a slug and a placement and pull it into editing.

HOW IT TALKS TO DRIVE
---------------------
Live enumeration is done through the Google Drive MCP server (search_files, read_file_content,
download_file_content). A plain Python script cannot call MCP tools, so this script reads a
CACHED enumeration JSON that the MCP session writes, and from it builds the catalog. The flow is:

  1. An MCP-enabled session enumerates each photography folder (search_files parentId=<id>,
     recursing into RETOUCHED and ON BLACK), and caches the raw file listing to
     scripts/cache/drive-enum-<slug>.json (schema below).
  2. This script reads that cache and writes/updates the markdown catalog and per-instructor
     working sheets, deterministically and idempotently, keyed on fileId.

Because the cache is a plain file, every subcommand here is runnable and testable offline. The
Drive MCP server is NOT adopted in settings.json; standing adoption is a build-vs-buy + Ahmed
decision (see _IMAGE-CATALOG.md header). Until then the enumeration step is run by hand in an
MCP session and cached.

CACHE SCHEMA  (scripts/cache/drive-enum-<slug>.json)
----------------------------------------------------
{
  "slug": "bassam-fattouh",
  "synced": "2026-06-16",
  "photography_folderId": "1pJvTgwAlhXDlc5Uh_LH7eyjzUuRsor8i",
  "files": [
    {
      "id": "1mfvxt10ah9GHXFP6qTbkKJ3k_4zvx-mS",
      "title": "MAHARAT III0507.jpg",
      "mimeType": "image/jpeg",
      "fileExtension": "jpg",
      "fileSize": "5780385",
      "source_folder_path": "01 - Classes / 04 - BASSAM FATTOUH / 05 - PHOTOGRAPHY / RETOUCHED",
      "retouched": "yes",
      "faces_present": "auto, verify",
      "orientation": "auto, verify",
      "image_type": "portrait"
    }
  ]
}

Files with mimeType "application/vnd.google-apps.folder" are skipped (they are containers).
Very large originals (a Bassam .tif is 165 MB) are catalogued but never fetched.

Usage:
  python3 .claude/scripts/drive_image_sync.py enumerate <slug|all>
  python3 .claude/scripts/drive_image_sync.py catalog   <slug|all>
  python3 .claude/scripts/drive_image_sync.py describe  <slug|all> --vision
  python3 .claude/scripts/drive_image_sync.py fetch      <slug> [--placement 4x5] [--retouched-only]

Exit 0: ok. Exit 1: a step failed (missing cache, house-style violation, write error).
Exit 2: usage error.
"""
import json
import os
import re
import sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
INSTR = os.path.join(BASE, "context", "instructors")
CATALOG = os.path.join(INSTR, "_IMAGE-CATALOG.md")
FOLDER_MAP = os.path.join(INSTR, "_IMAGE-FOLDER-MAP.md")
CACHE_DIR = os.path.join(BASE, "scripts", "cache")
ASSETS = os.path.join(BASE, "assets", "instructors")

# House-style sweep: em dash, en dash, tatweel, Eastern Arabic-Indic and Persian digits.
# Written with \u escapes (mirroring scripts/pack_check.py) so this source is itself house-clean.
FORBIDDEN = re.compile(r"[\u2014\u2013\u0640\u0660-\u0669\u06F0-\u06F9]")

# The catalog schema, in column order. One row per approved image.
COLUMNS = [
    "filename", "fileId", "viewUrl", "slug", "source_folder_path", "retouched",
    "preferred", "superseded_by", "image_type", "orientation", "background",
    "dominant_tones", "dimensions", "faces_present", "suggested_placements",
    "rights_status", "provenance", "last_synced", "caption_auto",
]

# Closed vocabularies (the catalog header documents these too).
IMAGE_TYPES = {"portrait", "headshot", "half-body", "class-still", "cover", "lifestyle",
               "product-detail", "b-roll"}
ORIENTATIONS = {"portrait", "landscape", "square", "auto, verify", "unverified"}
YESNO = {"yes", "no", "auto, verify", "unverified"}


def ok(m):
    print(f"  ok: {m}")


def view_url(file_id):
    return f"https://drive.google.com/file/d/{file_id}/view"


def stem_key(title):
    """Normalize a filename to a stem so retouched twins collapse to one group.

    Strips the extension, the retouch/treatment tokens (RETOUCHED, _RT, COLORCORRECTED,
    Blurred, Recolored, copy, and TIM/TIM02-style operator tags), separators, and trailing
    version digits. "MAHARAT III0579 copy_COLORCORRECTED_Blurred.png", "..._COLORCORRECTED.tif",
    and "MAHARAT III0579 copy.jpg" all collapse to the same key; the three "15052024_BassamBG_141414"
    variants collapse to one.
    """
    s = title.rsplit(".", 1)[0]  # drop extension
    tokens = ["retouchedshoe", "retouched", "colorcorrected", "blurred", "recolored",
              "_rt", "copy"]
    low = s.lower()
    for t in tokens:
        low = low.replace(t, " ")
    low = re.sub(r"tim\d*", " ", low)        # operator initials/version tag e.g. TIM02
    low = re.sub(r"[ _\-]+", " ", low)        # collapse separators
    low = re.sub(r"\b\d{1,3}\b$", "", low).strip()  # trailing short version digits
    return low


def is_retouched(path):
    p = path.upper()
    return "yes" if ("RETOUCHED" in p or "ON BLACK" in p) else "no"


def load_cache(slug):
    path = os.path.join(CACHE_DIR, f"drive-enum-{slug}.json")
    if not os.path.isfile(path):
        return None
    return json.load(open(path, encoding="utf-8"))


def all_slugs():
    """Slugs with a cache file present, sorted."""
    if not os.path.isdir(CACHE_DIR):
        return []
    out = []
    for f in sorted(os.listdir(CACHE_DIR)):
        m = re.match(r"drive-enum-(.+)\.json$", f)
        if m:
            out.append(m.group(1))
    return out


def build_rows(cache):
    """Turn a cache dict into a list of catalog row dicts, with dedup applied."""
    slug = cache["slug"]
    synced = cache.get("synced", "")
    files = [f for f in cache.get("files", [])
             if f.get("mimeType") != "application/vnd.google-apps.folder"]

    # Group by stem key for prefer-retouched dedup.
    groups = {}
    for f in files:
        groups.setdefault(stem_key(f["title"]), []).append(f)

    rows = []
    for key, members in groups.items():
        # Within a stem group, a retouched member is preferred. Among equally retouched
        # members, prefer jpg/png over tif/raw (fetchable), then the shortest title (the base).
        def rank(f):
            ret = 1 if is_retouched(f.get("source_folder_path", "")) == "yes" else 0
            ext = (f.get("fileExtension") or "").lower()
            fetchable = 1 if ext in ("jpg", "jpeg", "png") else 0
            return (ret, fetchable, -len(f["title"]))
        members_sorted = sorted(members, key=rank, reverse=True)
        winner = members_sorted[0]
        for f in members_sorted:
            preferred = "yes" if f is winner else "no"
            superseded = "" if f is winner else winner["id"]
            size = f.get("fileSize", "")
            dims = f"{size} bytes" if size else "unverified"
            rows.append({
                "filename": f["title"],
                "fileId": f["id"],
                "viewUrl": view_url(f["id"]),
                "slug": slug,
                "source_folder_path": f.get("source_folder_path", ""),
                "retouched": f.get("retouched") or is_retouched(f.get("source_folder_path", "")),
                "preferred": preferred,
                "superseded_by": superseded,
                "image_type": f.get("image_type", "portrait"),
                "orientation": f.get("orientation", "auto, verify"),
                "background": f.get("background", "auto, verify"),
                "dominant_tones": f.get("dominant_tones", "auto, verify"),
                "dimensions": dims,
                "faces_present": f.get("faces_present", "auto, verify"),
                "suggested_placements": f.get("suggested_placements", "see assets.md"),
                "rights_status": f.get("rights_status", "confirm with Ahmed"),
                "provenance": f.get("source_folder_path", ""),
                "last_synced": synced,
                "caption_auto": f.get("caption_auto", "pending describe --vision"),
            })
    # Stable order: preferred first, then filename.
    rows.sort(key=lambda r: (r["preferred"] != "yes", r["filename"]))
    return rows


def row_to_md(r):
    cells = [str(r.get(c, "")).replace("|", "\\|") for c in COLUMNS]
    return "| " + " | ".join(cells) + " |"


def cmd_enumerate(target):
    """Report what the cache holds (the live enumeration is an MCP step, documented above)."""
    slugs = all_slugs() if target == "all" else [target]
    if not slugs or (target != "all" and load_cache(target) is None):
        print(f"FAIL: no cache for '{target}'. Run the Drive MCP enumeration and write "
              f"{os.path.relpath(CACHE_DIR, BASE)}/drive-enum-{target}.json first. "
              f"See this script's header for the cache schema.")
        return 1
    for slug in slugs:
        cache = load_cache(slug)
        if cache is None:
            print(f"FAIL: no cache for '{slug}'")
            return 1
        files = [f for f in cache.get("files", [])
                 if f.get("mimeType") != "application/vnd.google-apps.folder"]
        ret = sum(1 for f in files if is_retouched(f.get("source_folder_path", "")) == "yes")
        ok(f"{slug}: {len(files)} image files in cache, {ret} tagged retouched=yes")
        if not files:
            print(f"FAIL: {slug} cache has zero image files")
            return 1
    return 0


def cmd_catalog(target):
    """Write/update catalog rows and per-instructor working sheets, idempotent on fileId."""
    slugs = all_slugs() if target == "all" else [target]
    if not slugs:
        print(f"FAIL: no cache for '{target}'")
        return 1
    wrote = 0
    for slug in slugs:
        cache = load_cache(slug)
        if cache is None:
            print(f"FAIL: no cache for '{slug}'")
            return 1
        rows = build_rows(cache)
        # House-style sweep on the rows we are about to write.
        blob = "\n".join(row_to_md(r) for r in rows)
        hits = FORBIDDEN.findall(blob)
        if hits:
            print(f"FAIL: house-style violation in generated rows for {slug}: {hits[:5]}")
            return 1
        # Validate closed vocabularies.
        for r in rows:
            if r["image_type"] not in IMAGE_TYPES:
                print(f"FAIL: {slug} bad image_type '{r['image_type']}' for {r['filename']}")
                return 1
            if r["faces_present"] not in YESNO or r["preferred"] not in YESNO:
                print(f"FAIL: {slug} bad yes/no value for {r['filename']}")
                return 1
        # Exactly one preferred per stem group.
        groups = {}
        for r in rows:
            groups.setdefault(stem_key(r["filename"]), []).append(r)
        for key, g in groups.items():
            n = sum(1 for r in g if r["preferred"] == "yes")
            if n != 1:
                print(f"FAIL: {slug} stem '{key}' has {n} preferred rows, expected 1")
                return 1
        ok(f"{slug}: {len(rows)} rows, {len(groups)} stem groups, one preferred each")
        wrote += len(rows)
        # NOTE: this offline build validates and prints the rows. The committed
        # _IMAGE-CATALOG.md and <slug>/assets.md are authored from this same logic; in an
        # adopted-MCP run this function writes them in place keyed on fileId. Print so the
        # rows are inspectable now.
        for r in rows:
            print(row_to_md(r))
    print(f"catalog: validated {wrote} rows across {len(slugs)} slug(s)")
    return 0


def cmd_describe(target, vision):
    """Fill caption_auto and derive image_type/background/faces_present via read_file_content.

    read_file_content accepts image/jpeg and image/png and returns a natural-language
    description. This step is an MCP call; offline it reports which rows still need tags.
    """
    if not vision:
        print("FAIL: describe requires --vision (it calls the Drive MCP read_file_content)")
        return 1
    slugs = all_slugs() if target == "all" else [target]
    pending = 0
    for slug in slugs:
        cache = load_cache(slug)
        if cache is None:
            print(f"FAIL: no cache for '{slug}'")
            return 1
        for r in build_rows(cache):
            if r["faces_present"] in ("auto, verify", "unverified") or \
               r["caption_auto"].startswith("pending"):
                pending += 1
    ok(f"describe: {pending} row(s) need vision tags. Run read_file_content per fileId in an "
       f"MCP session, then write faces_present/orientation/caption_auto back to the cache.")
    return 0


def cmd_fetch(slug, placement, retouched_only):
    """Materialize selected ids into the gitignored cache (download_file_content, an MCP call)."""
    cache = load_cache(slug)
    if cache is None:
        print(f"FAIL: no cache for '{slug}'")
        return 1
    rows = [r for r in build_rows(cache) if r["preferred"] == "yes"]
    if retouched_only:
        rows = [r for r in rows if r["retouched"] == "yes"]
    if placement:
        rows = [r for r in rows if placement.replace("x", ":") in r["suggested_placements"]
                or placement in r["suggested_placements"]]
    # Skip multi-hundred-MB tif/raw by default.
    def small(r):
        ext = r["filename"].rsplit(".", 1)[-1].lower()
        return ext in ("jpg", "jpeg", "png")
    rows = [r for r in rows if small(r)]
    target_dir = os.path.join(ASSETS, slug)
    ok(f"fetch: {len(rows)} preferred jpg/png target(s) for {slug} -> "
       f"{os.path.relpath(target_dir, BASE)}/")
    for r in rows:
        print(f"  would fetch {r['filename']} ({r['fileId']}) via download_file_content")
    print("fetch: download_file_content is an MCP call; bytes land in the gitignored cache. "
          "The cache is empty on a fresh clone and never committed.")
    return 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, target = argv[1], argv[2]
    rest = argv[3:]
    if cmd == "enumerate":
        return cmd_enumerate(target)
    if cmd == "catalog":
        return cmd_catalog(target)
    if cmd == "describe":
        return cmd_describe(target, "--vision" in rest)
    if cmd == "fetch":
        placement = None
        if "--placement" in rest:
            i = rest.index("--placement")
            placement = rest[i + 1] if i + 1 < len(rest) else None
        return cmd_fetch(target, placement, "--retouched-only" in rest)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Image catalog checker: deterministic gate for the approved-instructor-image catalog.

Sibling to pack_check.py. Asserts the machine-checkable invariants of
context/profiles/maharat/instructors/_IMAGE-CATALOG.md so the "pull a real approved image" guarantee holds:

  1. House-style sweep clean (no em dash, en dash, tatweel, Eastern Arabic-Indic numerals).
  2. The schema header is present with every required column, in order.
  3. For the slug's rows: required cells non-empty, closed vocabularies respected, viewUrl
     well-formed, and exactly one preferred=yes per stem group (the prefer-retouched dedup).
  4. No committed image binaries under assets/instructors/ (Drive is the source of record;
     the byte cache is gitignored and must never be committed). This rule is scoped to the
     instructors/ cache only: committed binaries under assets/email/ are the GitHub source of
     truth for the email asset pipeline (the GitHub-to-Ortto serve flow) and are ALLOWED and
     expected, see context/profiles/maharat/instructors/_EMAIL-ASSET-PIPELINE.md. The check reports them, it does
     not fail on them.

A slug section may be marked "pending enumeration" (photography folder known, image rows not
yet filled). Such a section passes structurally: it has no image rows to validate yet.

Usage:
  python3 .claude/scripts/image_catalog_check.py <slug>
  python3 .claude/scripts/image_catalog_check.py all

Exit 0: catalog passes. Exit 1: failures listed. Exit 2: usage error.
"""
import os
import re
import sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
INSTR = os.path.join(BASE, "context", "instructors")
CATALOG = os.path.join(INSTR, "_IMAGE-CATALOG.md")
FOLDER_MAP = os.path.join(INSTR, "_IMAGE-FOLDER-MAP.md")
ASSETS = os.path.join(BASE, "assets", "instructors")
EMAIL_ASSETS = os.path.join(BASE, "assets", "email")

FORBIDDEN = re.compile(r"[\u2014\u2013\u0640\u0660-\u0669\u06F0-\u06F9]")

COLUMNS = [
    "filename", "fileId", "viewUrl", "slug", "source_folder_path", "retouched",
    "preferred", "superseded_by", "image_type", "orientation", "background",
    "dominant_tones", "dimensions", "faces_present", "suggested_placements",
    "rights_status", "provenance", "last_synced", "caption_auto",
]
IMAGE_TYPES = {"portrait", "headshot", "half-body", "class-still", "cover", "lifestyle",
               "product-detail", "b-roll"}
ORIENTATIONS = {"portrait", "landscape", "square", "auto, verify", "unverified"}
YESNO = {"yes", "no", "auto, verify", "unverified"}
IMAGE_EXT = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".gif", ".bmp", ".heic", ".raw")


def stem_key(title):
    """Same normalization as drive_image_sync.stem_key (kept in sync deliberately)."""
    s = title.rsplit(".", 1)[0]
    for t in ["retouchedshoe", "retouched", "colorcorrected", "blurred", "recolored",
              "_rt", "copy"]:
        s = s.lower().replace(t, " ") if t in s.lower() else s.lower()
    s = re.sub(r"tim\d*", " ", s.lower())
    s = re.sub(r"[ _\-]+", " ", s)
    s = re.sub(r"\b\d{1,3}\b$", "", s).strip()
    return s


def parse_rows(text):
    """Return (header_cells, [row_cells, ...]) for the full schema table(s) in the catalog.

    The catalog has several tables that start with a 'filename' column (the main schema table
    plus narrow CloudFront cover tables). Lock onto the FULL schema header (the one equal to
    COLUMNS) and collect only the rows that belong to it: full width with a Drive-id col 2.
    The narrow cover tables are intentionally ignored here.
    """
    header = None
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells == COLUMNS:
            header = cells
            continue
        if cells and cells[0] == "filename":
            continue  # a different (narrow) table header, skip it
        if header is None:
            continue
        if set("".join(cells)) <= set("-: "):  # separator row
            continue
        # A data row for the schema table has the right width and a Drive-id-looking col 2.
        if len(cells) == len(COLUMNS) and re.fullmatch(r"[A-Za-z0-9_\-]{10,}", cells[1] or ""):
            rows.append(cells)
    return header, rows


def check(slug):
    fails = []
    ok = lambda m: print(f"  ok: {m}")

    if not os.path.isfile(CATALOG):
        return [f"missing {os.path.relpath(CATALOG, BASE)}"]
    text = open(CATALOG, encoding="utf-8").read()

    # 1. House-style sweep on the whole catalog and the folder map.
    for p in [CATALOG, FOLDER_MAP]:
        if os.path.isfile(p):
            hits = FORBIDDEN.findall(open(p, encoding="utf-8").read())
            if hits:
                fails.append(f"house-style violation in {os.path.relpath(p, BASE)}: {hits[:5]}")
    if not any("house-style" in f for f in fails):
        ok("house-style sweep clean (catalog + folder map)")

    # 2. Schema header present with every column in order.
    header, rows = parse_rows(text)
    if header is None:
        fails.append("no schema header row found (expected a row starting '| filename |')")
    elif header != COLUMNS:
        missing = [c for c in COLUMNS if c not in header]
        fails.append(f"schema header mismatch. missing/reordered: {missing or header}")
    else:
        ok(f"schema header present with all {len(COLUMNS)} columns in order")

    # 3. Per-slug row validation.
    if slug != "all":
        rows = [r for r in rows if header and r[header.index("slug")] == slug]
    if header and rows:
        idx = {c: header.index(c) for c in COLUMNS}
        groups = {}
        bad = False
        for r in rows:
            fn = r[idx["filename"]]
            # required cells non-empty
            for col in ("filename", "fileId", "viewUrl", "slug", "image_type", "preferred",
                        "faces_present", "rights_status"):
                if not r[idx[col]]:
                    fails.append(f"{fn}: empty required cell '{col}'"); bad = True
            # viewUrl well-formed
            if not re.fullmatch(r"https://drive\.google\.com/file/d/[A-Za-z0-9_\-]+/view",
                                r[idx["viewUrl"]]):
                fails.append(f"{fn}: malformed viewUrl '{r[idx['viewUrl']]}'"); bad = True
            # closed vocabularies
            if r[idx["image_type"]] not in IMAGE_TYPES:
                fails.append(f"{fn}: image_type '{r[idx['image_type']]}' not in vocab"); bad = True
            if r[idx["orientation"]] not in ORIENTATIONS:
                fails.append(f"{fn}: orientation '{r[idx['orientation']]}' not in vocab"); bad = True
            for col in ("retouched", "preferred", "faces_present"):
                if r[idx[col]] not in YESNO:
                    fails.append(f"{fn}: {col} '{r[idx[col]]}' not yes/no"); bad = True
            groups.setdefault(stem_key(fn), []).append(r)
        if not bad:
            ok(f"{len(rows)} row(s) for {slug}: required cells, vocab, and viewUrl all valid")
        # exactly one preferred per stem group
        ge = True
        for key, g in groups.items():
            n = sum(1 for r in g if r[idx["preferred"]] == "yes")
            if n != 1:
                fails.append(f"stem group '{key}' has {n} preferred=yes rows, expected exactly 1")
                ge = False
        if ge and groups:
            ok(f"exactly one preferred=yes per stem group ({len(groups)} group(s))")
    elif slug != "all":
        # No rows for this slug. Allowed only if the section is marked pending enumeration.
        sec = re.search(rf"(?im)^#+\s.*{re.escape(slug)}.*$", text)
        if sec and "pending enumeration" in text[sec.start():sec.start() + 600].lower():
            ok(f"{slug}: section present, marked pending enumeration (no rows to validate yet)")
        else:
            fails.append(f"no rows for slug '{slug}' and no 'pending enumeration' marker")

    # 4. No committed image binaries under assets/instructors/ (the gitignored Drive byte cache).
    #    Scoped to instructors/ only: assets/email/ binaries are the GitHub source of truth for the
    #    email asset pipeline and are explicitly allowed (reported, never failed).
    committed = []
    if os.path.isdir(ASSETS):
        for root, _, files in os.walk(ASSETS):
            for f in files:
                if f.lower().endswith(IMAGE_EXT):
                    rel = os.path.relpath(os.path.join(root, f), BASE)
                    # Is it tracked by git? If git is unavailable, presence alone is enough to flag.
                    committed.append(rel)
    if committed:
        # The cache is gitignored, so the files may exist locally; only fail if git TRACKS them.
        import subprocess
        tracked = []
        for rel in committed:
            r = subprocess.run(["git", "-C", BASE, "ls-files", "--error-unmatch", rel],
                               capture_output=True, text=True)
            if r.returncode == 0:
                tracked.append(rel)
        if tracked:
            fails.append(f"image binaries committed under assets/instructors/ (the cache must stay "
                         f"gitignored): {tracked[:5]}")
        else:
            ok(f"instructors/ byte cache present ({len(committed)} file(s)) but none tracked by git")
    else:
        ok("no image binaries under assets/instructors/")

    # The email asset source of truth: assets/email/ binaries ARE meant to be committed (the GitHub
    # side of the GitHub-to-Ortto pipeline). Report them, do not fail on them.
    email_bins = []
    if os.path.isdir(EMAIL_ASSETS):
        for root, _, files in os.walk(EMAIL_ASSETS):
            for f in files:
                if f.lower().endswith(IMAGE_EXT):
                    email_bins.append(os.path.relpath(os.path.join(root, f), BASE))
    if email_bins:
        ok(f"assets/email/ source of truth present ({len(email_bins)} committed binary file(s), "
           f"allowed): {email_bins[:3]}")
    else:
        ok("assets/email/ present (no committed binaries yet; covers/portraits fetch per environment)")

    return fails


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    slug = argv[1]
    print(f"image_catalog_check: {slug}")
    fails = check(slug)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("PASS: image catalog meets the deterministic gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

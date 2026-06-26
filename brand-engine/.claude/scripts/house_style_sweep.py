#!/usr/bin/env python3
"""house_style_sweep.py: the campaign-agnostic house-style gate, by code point.

Sweeps the files named on the command line for the FORBIDDEN set, the same set
scripts/pack_check.py and scripts/email_render.py enforce: em dash, en dash,
tatweel, and the Arabic-Indic and extended Arabic-Indic numerals. Built by code
point so this source file carries no literal forbidden character.

Usage:
  python3 .claude/scripts/house_style_sweep.py <file> [<file> ...]

Exit 0: every named file is clean.
Exit 1: at least one violation, listed by file with the offending code points.
Exit 2: usage error.
"""
import os
import re
import sys

# em dash, en dash, tatweel, Arabic-Indic 0-9, extended Arabic-Indic 0-9. Code points only.
FORBIDDEN = re.compile(
    "[" + chr(0x2014) + chr(0x2013) + chr(0x0640)
    + chr(0x0660) + "-" + chr(0x0669)
    + chr(0x06F0) + "-" + chr(0x06F9) + "]"
)


def sweep(path):
    try:
        text = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as e:
        return [f"could not read {path}: {e}"]
    hits = FORBIDDEN.findall(text)
    if not hits:
        return []
    uniq = " ".join(sorted({hex(ord(c)) for c in hits}))
    return [f"{path}: {len(hits)} forbidden char(s): {uniq} "
            f"(em/en dash, tatweel, or Eastern numerals)"]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    fails = []
    for p in argv[1:]:
        fails += sweep(p)
    if fails:
        print(f"FAIL: house-style violations in {len(fails)} file(s):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print(f"PASS: house-style sweep clean for {len(argv) - 1} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

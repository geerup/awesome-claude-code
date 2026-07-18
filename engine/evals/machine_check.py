#!/usr/bin/env python3
"""R01 machine pass. Run against any output file before LLM QA review.

Usage: python3 engine/evals/machine_check.py <file> [<file> ...]
Exit 0 = clean, exit 1 = flags raised. Flags are surfaced, never auto-fixed.

Checks:
  1. Em dash scan (banned in prose).
  2. Banned word scan (brand.json banned.words).
  3. Banned bullet openers (Boosted/Achieved/Delivered).
  4. "not X but Y" construction heuristic.
  5. Pipeline language: "sourced"/"generated" adjacent to pipeline.
  6. Live-performance language for Maharat systems (ROAS, revenue lift).
  7. Metric traceability: numeric tokens must appear in master.json.
"""
import json
import re
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent
BRAND = json.loads((ENGINE / "data" / "brand.json").read_text())
MASTER_RAW = (ENGINE / "data" / "master.json").read_text()

BANNED_WORDS = [w.lower() for w in BRAND["banned"]["words"]]

# Whitelist: every numeric token that exists in master.json, plus counting
# numbers 0-12 (structural language: "one case per letter", "three domains").
MASTER_NUMBERS = set(re.findall(r"\d[\d,.]*[KMB+x]*", MASTER_RAW))
MASTER_NUMBERS |= {n.rstrip("+") for n in MASTER_NUMBERS}
STRUCTURAL = {str(n) for n in range(13)}
YEAR = re.compile(r"^(19|20)\d\d$")
# Numeric tokens preceded by a word char or hyphen are identifiers (R01, A13,
# B2B, application-001), never metrics. "day N" is cadence scheduling.
NUM_TOKEN = re.compile(r"(?<![\w-])\d[\d,.]*[KMB+x%]*")
DAY_REF = re.compile(r"\bday\s+\d+", re.I)


def flag(flags, path, line_no, kind, detail):
    flags.append(f"{path}:{line_no} [{kind}] {detail}")


def check_file(path: Path, flags: list):
    text = path.read_text()
    for i, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        if "—" in line:
            flag(flags, path, i, "em-dash", "em dash in prose")
        for w in BANNED_WORDS:
            if re.search(rf"\b{re.escape(w)}\b", low):
                flag(flags, path, i, "banned-word", w)
        if re.match(r"^\s*[-*]\s+(boosted|achieved|delivered)\b", low):
            flag(flags, path, i, "banned-opener", line.strip()[:60])
        if re.search(r"\bnot\s+(a\s+|an\s+|the\s+)?\w+([ ,]+\w+){0,3},?\s+but\s+", low):
            flag(flags, path, i, "not-x-but-y", line.strip()[:80])
        if re.search(r"pipeline\s+(sourced|generated)|(sourced|generated)\s+pipeline", low):
            flag(flags, path, i, "pipeline-language", "use 'influenced'")
        if re.search(r"\broas\b|revenue lift", low):
            flag(flags, path, i, "live-metric", "no live performance figures exist for the Maharat systems")
        scrubbed = DAY_REF.sub("day", line)
        for num in NUM_TOKEN.findall(scrubbed):
            token = num.rstrip(".,+")
            if token in STRUCTURAL or YEAR.match(token):
                continue
            if token not in MASTER_NUMBERS:
                flag(flags, path, i, "traceability", f"'{token}' not found in master.json")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    flags = []
    for arg in argv[1:]:
        p = Path(arg)
        if p.is_file():
            check_file(p, flags)
        else:
            flags.append(f"{p}:0 [missing] file not found")
    if flags:
        print(f"FLAGS ({len(flags)}): reviewers surface defects only, writers fix:")
        for f in flags:
            print("  " + f)
        return 1
    print("CLEAN: machine pass passed. Next tier: LLM QA review, then the gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

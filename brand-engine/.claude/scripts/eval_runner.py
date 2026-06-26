#!/usr/bin/env python3
"""Eval runner for the Maharat marketing engine.

Runs the machine_checks layer of a skill's evals.json against one or more asset
files (or stdin). Deterministic: regex based, no LLM. The llm_checks layer is
judged separately by the reviewing agent (brand-qa-reviewer or the pack skill).

Usage:
  python3 scripts/eval_runner.py <evals.json> <asset-file> [<asset-file> ...]
  cat draft.md | python3 scripts/eval_runner.py <evals.json> -
  python3 scripts/eval_runner.py --docs <evals.json> <governance-file>   (skips asset-only checks)

Exit code 0: all hard machine checks pass (soft failures are warnings).
Exit code 1: at least one hard machine check failed (hard stop per
runtime/verification.md: return to author with the exact fixes).
Exit code 2: usage or file error.

House rule: this script's own strings avoid em dashes, tatweel, and Eastern
Arabic numerals, like every other file in the engine.
"""
import json
import re
import sys


def load_evals(path):
    with open(path, encoding="utf-8") as f:
        spec = json.load(f)
    checks = spec.get("machine_checks", [])
    if not checks:
        print(f"NOTE: no machine_checks in {path}; nothing to run here.")
    return spec, checks


def run_checks(text, checks, label, docs_mode=False):
    failures = []
    warnings = []
    for c in checks:
        if docs_mode and c.get("applies_to", "all") == "assets":
            continue
        pattern = re.compile(c["regex"])
        matches = list(pattern.finditer(text))
        hit = bool(matches)
        failed = hit if c.get("fail_if", "match") == "match" else not hit
        if not failed:
            continue
        finding = {
            "id": c["id"],
            "severity": c.get("severity", "hard"),
            "fix": c.get("fix", ""),
            "spans": [m.group(0) for m in matches][:5],
            "file": label,
        }
        if finding["severity"] == "hard":
            failures.append(finding)
        else:
            warnings.append(finding)
    return failures, warnings


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    docs_mode = "--docs" in argv
    argv = [a for a in argv if a != "--docs"]
    evals_path = argv[1]
    spec, checks = load_evals(evals_path)
    all_fail, all_warn = [], []
    for target in argv[2:]:
        if target == "-":
            text, label = sys.stdin.read(), "<stdin>"
        else:
            try:
                with open(target, encoding="utf-8") as f:
                    text = f.read()
            except OSError as e:
                print(f"ERROR reading {target}: {e}")
                return 2
            label = target
        f_, w_ = run_checks(text, checks, label, docs_mode)
        all_fail.extend(f_)
        all_warn.extend(w_)

    skill = spec.get("skill", evals_path)
    for w in all_warn:
        print(f"WARN [{w['id']}] {w['file']}: {w['spans']} :: {w['fix']}")
    if all_fail:
        print(f"FAIL: {len(all_fail)} hard check(s) failed for skill {skill}")
        for f_ in all_fail:
            print(f"  [{f_['id']}] {f_['file']}: found {f_['spans']} :: FIX: {f_['fix']}")
        print("Hard stop per runtime/verification.md: return to author with the fixes above.")
        return 1
    print(f"PASS: all hard machine checks passed for skill {skill}"
          + (f" ({len(all_warn)} warning(s))" if all_warn else ""))
    print("Next gates: llm_checks (reviewing agent), arabic-copy-qa if AR, brand-qa-reviewer, human gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

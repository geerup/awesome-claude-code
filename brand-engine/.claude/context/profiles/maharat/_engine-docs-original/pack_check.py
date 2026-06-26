#!/usr/bin/env python3
"""Pack checker: deterministic definition-of-done gate for an instructor pack.

Validates the full pack for one instructor slug per context/mining-plan-v2.md
section 3, including running eval_runner on the right files in the right modes.
This is the executable half of the QA pass; the llm_checks half is judged by the
reviewing agent.

Usage:
  python3 .claude/scripts/pack_check.py <slug>

Exit 0: pack passes the deterministic definition of done.
Exit 1: failures listed; the batch protocol treats this as return-to-distiller.
Exit 2: usage error.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
RUNNER = os.path.join(BASE, "scripts", "eval_runner.py")
FORBIDDEN = re.compile(r"[\u2014\u2013\u0640\u0660-\u0669\u06F0-\u06F9]")


def check(slug):
    fails = []
    ok = lambda m: print(f"  ok: {m}")

    fact = os.path.join(BASE, "context", "instructors", f"{slug}.md")
    pack = os.path.join(BASE, "skills", "instructor-marketing", slug)
    skill = os.path.join(pack, "SKILL.md")
    voice = os.path.join(pack, "voice.md")
    tmpl = os.path.join(pack, "templates")
    evals = os.path.join(pack, "evals", "evals.json")
    catalog = os.path.join(BASE, "context", "instructors", "_CATALOG.md")
    log = os.path.join(BASE, "references", "drive-extraction-log.md")

    # 1. Required files
    for p, name in [(fact, "fact file"), (skill, "pack SKILL.md"), (voice, "voice.md"), (evals, "evals.json")]:
        if os.path.isfile(p):
            ok(name)
        else:
            fails.append(f"missing {name}: {p}")
    if os.path.isdir(tmpl) and any(f.endswith(".md") for f in os.listdir(tmpl)):
        ok("templates/ has at least one template")
    else:
        fails.append("templates/ missing or empty")

    # 2. Fact file content markers
    if os.path.isfile(fact):
        t = open(fact, encoding="utf-8").read()
        for marker, name in [("Claims table", "claims table"), ("verified", "verified rows"),
                             ("Assets and surfaces", "assets section")]:
            if marker in t:
                ok(f"fact file has {name}")
            else:
                fails.append(f"fact file lacks {name} ('{marker}')")

    # 3. evals.json structure
    spec = None
    if os.path.isfile(evals):
        try:
            spec = json.load(open(evals, encoding="utf-8"))
            for key in ("machine_checks", "llm_checks", "golden_examples"):
                if spec.get(key):
                    ok(f"evals.json has {key}")
                else:
                    fails.append(f"evals.json missing or empty: {key}")
            labels = {g.get("label") for g in spec.get("golden_examples", [])}
            if {"pass", "fail"} <= labels:
                ok("golden pass and fail examples present")
            else:
                fails.append("golden_examples must include one 'pass' and one 'fail'")
        except (json.JSONDecodeError, OSError) as e:
            fails.append(f"evals.json invalid: {e}")

    # 4. eval_runner gates
    def run(args):
        return subprocess.run([sys.executable, RUNNER] + args,
                              capture_output=True, text=True).returncode

    if spec is not None:
        gov = [p for p in [fact, skill, voice] if os.path.isfile(p)]
        gov += [os.path.join(tmpl, f) for f in (os.listdir(tmpl) if os.path.isdir(tmpl) else [])
                if f.endswith(".md")]
        if run(["--docs", evals] + gov) == 0:
            ok("eval_runner --docs passes on governance files")
        else:
            fails.append("eval_runner --docs failed on governance files")
        for g in spec.get("golden_examples", []):
            with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                             encoding="utf-8") as f:
                f.write(g["text"])
                path = f.name
            code = run([evals, path])
            os.unlink(path)
            want = 0 if g["label"] == "pass" else 1
            if code == want:
                ok(f"golden {g['label']} case exits {want}")
            else:
                fails.append(f"golden {g['label']} case exited {code}, expected {want}")

    # 5. House-style sweep on pack files (evals.json holds detection patterns, skip it)
    for p in [fact, skill, voice] + ([os.path.join(tmpl, f) for f in os.listdir(tmpl)]
                                     if os.path.isdir(tmpl) else []):
        if not os.path.isfile(p) or p.endswith(".json"):
            continue
        hits = FORBIDDEN.findall(open(p, encoding="utf-8").read())
        if hits:
            fails.append(f"house-style violation in {os.path.relpath(p, BASE)}: {hits[:5]}")
    if not any("house-style" in f for f in fails):
        ok("house-style sweep clean")

    # 6. Registry and log reflect the pack
    if os.path.isfile(catalog) and slug in open(catalog, encoding="utf-8").read():
        ok("catalog row present")
    else:
        fails.append("slug not found in _CATALOG.md")
    name = slug.replace("-", " ").title()
    if os.path.isfile(log) and (slug in open(log, encoding="utf-8").read()
                                or name in open(log, encoding="utf-8").read()):
        ok("extraction log mentions the instructor")
    else:
        fails.append("extraction log has no section for this instructor")

    return fails


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    slug = argv[1]
    print(f"pack_check: {slug}")
    fails = check(slug)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("PASS: pack meets the deterministic definition of done.")
    print("Remaining gates: llm_checks judgment, then the async human-gate queue.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

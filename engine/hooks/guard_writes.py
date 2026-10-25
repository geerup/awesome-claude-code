#!/usr/bin/env python3
"""PreToolUse guard (Write|Edit|MultiEdit|NotebookEdit|Bash): protects the brain.

  deny  generated or script-owned files: data/facts.jsonl, data/entries.json
        (scripts/fact_bank.py), data/variants.jsonl (scripts/approve_variant.py),
        outputs/**/factcheck.json (scripts/check_claims.py).
  ask   ground truth and law: data/master.json, data/brand.json, rules/hard.json,
        M00.md. San confirms in the permission prompt; the change is logged in
        log/decisions.md per M00.

Bash is screened heuristically: a command that names a protected path and
carries a write token is treated like a direct write, unless it is one of the
owning scripts. Reads (cat, grep, jq) pass.
"""
import re

from hooklib import pre_tool_decision, rel, resolve, run

DENY = {
    "engine/data/facts.jsonl": "generated: run python3 engine/scripts/fact_bank.py",
    "engine/data/entries.json": "generated: run python3 engine/scripts/fact_bank.py",
    "engine/data/variants.jsonl": "append-only via python3 engine/scripts/approve_variant.py",
}
DENY_PATTERN = (re.compile(r"^engine/outputs/.+/factcheck\.json$"),
                "written only by python3 engine/scripts/check_claims.py --write")
ASK = {
    "engine/data/master.json": "ground truth",
    "engine/data/brand.json": "voice law",
    "engine/rules/hard.json": "hard rules",
    "engine/M00.md": "master contract",
}
OWNING_SCRIPTS = re.compile(
    r"^\s*python3?\s+(\S*/)?engine/scripts/(fact_bank|approve_variant|check_claims)\.py\b")
PROTECTED = (r"facts\.jsonl|entries\.json|variants\.jsonl|factcheck\.json|master\.json"
             r"|brand\.json|hard\.json|M00\.md")
PROTECTED_NAMES = re.compile(PROTECTED)
# A redirect or tee only counts when its target is a protected file; the other
# tokens mutate whatever they name, so any protected name alongside them counts.
WRITE_TOKENS = re.compile(
    rf"(>>?\s*\S*({PROTECTED})|\btee\s+(-a\s+)?\S*({PROTECTED})|\bsed\s+-i|\bperl\s+-[a-z]*i"
    r"|\bmv\b|\bcp\b|\brm\b|\btruncate\b|\bdd\b|\bgit\s+(checkout|restore|reset|apply)\b"
    r"|\bpython3?\s+-c\b|\bnode\s+-e\b|\bln\b)")


def classify(path: str | None):
    if path is None:
        return None
    if path in DENY:
        return "deny", f"{path} is {DENY[path]}"
    if DENY_PATTERN[0].match(path):
        return "deny", f"{path} is {DENY_PATTERN[1]}"
    if path in ASK:
        return "ask", (f"{path} is {ASK[path]}. Approve only if San said yes to this exact "
                       "change in this session; log it in engine/log/decisions.md (M00).")
    return None


def main(event):
    tool = event.get("tool_name", "")
    inp = event.get("tool_input", {}) or {}
    cwd = event.get("cwd")
    if tool == "Bash":
        cmd = inp.get("command", "")
        if not PROTECTED_NAMES.search(cmd) or OWNING_SCRIPTS.match(cmd):
            return
        if WRITE_TOKENS.search(cmd):
            names = sorted(set(PROTECTED_NAMES.findall(cmd)))
            pre_tool_decision("deny", f"Bash command writes near protected engine files "
                              f"({', '.join(names)}). Use the owning script, or Edit for "
                              "master.json/brand.json/hard.json/M00.md so San can approve.")
        return
    target = inp.get("file_path") or inp.get("notebook_path")
    if not target:
        return
    verdict = classify(rel(resolve(target, cwd)))
    if verdict:
        pre_tool_decision(*verdict)


if __name__ == "__main__":
    run(main)

#!/usr/bin/env python3
"""Stop and SubagentStop gate: a run cannot end on an unchecked or failing draft.

Blocks when any outputs/**/draft.json has no factcheck.json, a factcheck bound to
a different draft or master.json hash (stale), or fail lines. needs_human lines
do not block: they are the gate's job, reported to San with the pack.
"""
import hashlib
import json
import sys

from hooklib import ENGINE, run


def problems() -> list[str]:
    import fact_bank  # inside run(): an import failure must fail closed

    out = []
    master = fact_bank.master_sha256()
    for draft in sorted((ENGINE / "outputs").glob("**/draft.json")):
        name = draft.relative_to(ENGINE).as_posix()
        fc_path = draft.parent / "factcheck.json"
        if not fc_path.exists():
            out.append(f"{name}: no factcheck.json; run engine/scripts/check_claims.py "
                       f"{name} --write")
            continue
        fc = json.loads(fc_path.read_text())
        if fc.get("draft_sha256") != hashlib.sha256(draft.read_bytes()).hexdigest():
            out.append(f"{name}: factcheck.json is stale (draft changed since the check)")
        elif fc.get("master_sha256") != master:
            out.append(f"{name}: factcheck.json is stale (master.json changed); re-run check")
        elif fc["summary"]["fail"] or fc.get("draft_errors"):
            out.append(f"{name}: {fc['summary']['fail']} fail lines, "
                       f"{len(fc.get('draft_errors', []))} draft errors")
    return out


def main(event):
    if event.get("stop_hook_active"):
        return  # already blocked once this turn; let Claude report instead of looping
    found = problems()
    if found:
        print(json.dumps({"decision": "block", "reason": "Stop gate: drafts are not cleared.\n- "
                          + "\n- ".join(found)}))
        sys.exit(0)


if __name__ == "__main__":
    run(main)

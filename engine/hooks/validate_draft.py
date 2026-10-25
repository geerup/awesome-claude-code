#!/usr/bin/env python3
"""PreToolUse (Write|Edit|MultiEdit) and PostToolUse gate for outputs/**/draft.json.

Pre:  computes the content the tool would leave on disk, runs check_claims, and
      denies the write if any line fails or the draft is malformed. The reason
      lists every failure so the writer self-corrects.
Post: writes factcheck.json next to the draft, bound to the draft's sha256, so the
      stop gate can tell a fresh check from a stale one.
"""
import json
import re
from pathlib import Path

from hooklib import pre_tool_decision, rel, resolve, run

DRAFT = re.compile(r"^engine/outputs/.+/draft\.json$")


def proposed_content(tool: str, inp: dict, path: Path) -> str:
    if tool == "Write":
        return inp["content"]
    text = path.read_text() if path.exists() else ""
    edits = inp["edits"] if tool == "MultiEdit" else [inp]
    for e in edits:
        old, new = e["old_string"], e["new_string"]
        if old not in text:
            return text  # the tool itself will reject a non-matching edit
        text = text.replace(old, new) if e.get("replace_all") else text.replace(old, new, 1)
    return text


def main(event):
    import check_claims  # inside run(): an import failure must fail closed

    inp = event.get("tool_input", {}) or {}
    target = inp.get("file_path")
    if not target:
        return
    path = resolve(target, event.get("cwd"))
    if not DRAFT.match(rel(path) or ""):
        return
    if event.get("hook_event_name") == "PostToolUse":
        report = check_claims.report_for(path, path.read_text())
        (path.parent / "factcheck.json").write_text(json.dumps(report, indent=2) + "\n")
        return
    report = check_claims.report_for(path, proposed_content(event["tool_name"], inp, path))
    problems = check_claims.blocking(report)
    if problems:
        pre_tool_decision("deny", "draft.json failed the claim check (rules/hard.json). Fix "
                          "and rewrite; new wording goes in as proposed:true:\n- "
                          + "\n- ".join(problems))


if __name__ == "__main__":
    run(main)

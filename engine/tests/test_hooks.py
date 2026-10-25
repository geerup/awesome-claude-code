"""Drive each hook as Claude Code does: event JSON on stdin, decision on stdout."""
import json
import subprocess
import sys

from conftest import DRAFT_PATH, ENGINE

HOOKS = ENGINE / "hooks"


def run_hook(name, event):
    proc = subprocess.run([sys.executable, str(HOOKS / name)], input=json.dumps(event),
                          capture_output=True, text=True)
    out = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, out


def decision(out):
    return out.get("hookSpecificOutput", {}).get("permissionDecision")


def test_guard_denies_generated_bank():
    _, out = run_hook("guard_writes.py", {"tool_name": "Write", "tool_input": {
        "file_path": str(ENGINE / "data" / "facts.jsonl"), "content": "{}"}})
    assert decision(out) == "deny"


def test_guard_asks_for_master():
    _, out = run_hook("guard_writes.py", {"tool_name": "Edit", "tool_input": {
        "file_path": str(ENGINE / "data" / "master.json"), "old_string": "a", "new_string": "b"}})
    assert decision(out) == "ask"


def test_guard_allows_ordinary_files():
    code, out = run_hook("guard_writes.py", {"tool_name": "Write", "tool_input": {
        "file_path": str(ENGINE / "outputs" / "gated" / "x" / "notes.md"), "content": "x"}})
    assert code == 0 and out == {}


def test_guard_bash():
    deny = ["sed -i 's/a/b/' engine/data/variants.jsonl",
            "echo '{}' >> engine/data/variants.jsonl",
            "cp /tmp/x engine/data/master.json"]
    allow = ["cat engine/data/master.json",
             "python3 engine/evals/machine_check.py engine/data/master.json 2>&1",
             "python3 engine/scripts/approve_variant.py --batch v.jsonl",
             "python3 engine/scripts/check_claims.py d/draft.json --write"]
    for cmd in deny:
        _, out = run_hook("guard_writes.py", {"tool_name": "Bash", "tool_input": {"command": cmd}})
        assert decision(out) == "deny", cmd
    for cmd in allow:
        _, out = run_hook("guard_writes.py", {"tool_name": "Bash", "tool_input": {"command": cmd}})
        assert out == {}, cmd


def test_validate_draft_allows_clean_and_denies_fabrication():
    text = DRAFT_PATH.read_text()
    event = {"tool_name": "Write", "hook_event_name": "PreToolUse",
             "tool_input": {"file_path": str(DRAFT_PATH), "content": text}}
    assert run_hook("validate_draft.py", event) == (0, {})
    event["tool_input"]["content"] = text.replace("$5M+ enterprise", "$9M+ enterprise")
    _, out = run_hook("validate_draft.py", event)
    assert decision(out) == "deny"
    assert "9M" in out["hookSpecificOutput"]["permissionDecisionReason"]


def test_validate_draft_simulates_edits():
    event = {"tool_name": "Edit", "hook_event_name": "PreToolUse", "tool_input": {
        "file_path": str(DRAFT_PATH), "old_string": "Salesforce-tracked",
        "new_string": "HubSpot-tracked"}}
    _, out = run_hook("validate_draft.py", event)
    assert decision(out) == "deny"


def test_hooks_fail_closed_on_garbage():
    proc = subprocess.run([sys.executable, str(HOOKS / "guard_writes.py")], input="not json",
                          capture_output=True, text=True)
    assert proc.returncode == 2


def test_stop_gate_passes_on_checked_tree():
    assert run_hook("stop_gate.py", {"hook_event_name": "Stop"}) == (0, {})

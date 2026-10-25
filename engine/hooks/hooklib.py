"""Shared plumbing for the engine's Claude Code hooks.

Hooks fail closed: any exception inside a guard exits 2, which blocks the tool
call (or the stop) and feeds the error back to Claude. A broken validator must
never let an unchecked write through.
"""
import json
import sys
import traceback
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent
REPO = ENGINE.parent
sys.path.insert(0, str(ENGINE / "scripts"))


def read_event() -> dict:
    return json.load(sys.stdin)


def resolve(path: str, cwd: str | None) -> Path:
    p = Path(path)
    if not p.is_absolute():
        p = Path(cwd or ".") / p
    return p.resolve()


def rel(p: Path) -> str | None:
    """Path relative to the repo root, or None when outside it."""
    try:
        return p.relative_to(REPO).as_posix()
    except ValueError:
        return None


def pre_tool_decision(decision: str, reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason,
    }}))
    sys.exit(0)


def run(main) -> None:
    try:
        main(read_event())
    except SystemExit:
        raise
    except Exception:
        print("engine hook crashed; failing closed:\n" + traceback.format_exc(), file=sys.stderr)
        sys.exit(2)
    sys.exit(0)

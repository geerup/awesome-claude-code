# San Engine: operating notes for Claude Code

`M00.md` governs. This file covers the code-enforced layer only: the evidence bank, the claim checker, and the hooks in `.claude/settings.json`.

## The brain
- `data/master.json` is ground truth. Edits need San's yes (the guard hook asks) and a `log/decisions.md` entry.
- `data/facts.jsonl` and `data/entries.json` are derived atoms with stable ids (`CAN-pipeline-1c`, `MAH-title`). Generate them with `python3 engine/scripts/fact_bank.py`. They are gitignored and never hand-edited.
- `data/variants.jsonl` holds approved phrasings. It is append-only, through `python3 engine/scripts/approve_variant.py`, and every variant names the decisions-log heading where San approved it.
- `rules/hard.json` is layer 1 of the rules engine. Segment rules (UK-EU, GCC, Egypt) and per-JD rules are later phases.

## Writing a CV
1. Write `outputs/gated/<application>/draft.json` (`schemas/draft.schema.json`). Every line cites `fact_ids` plus either an approved `variant_id` or `"proposed": true`.
2. New wording is always `proposed`. It reaches San at the gate and is excluded from render until he approves it. Never invent a variant id.
3. The validate_draft hook runs `scripts/check_claims.py` on every write and denies it on any fail: unknown or unusable fact, a number or name missing from the cited facts, a dash, headcount, uninfluenced pipeline figure, location, cross-role attribution, or a title, org, date or name mismatch. Read the denial, fix, rewrite.
4. PostToolUse writes `factcheck.json`. The stop gate refuses to end a turn while any draft is unchecked, stale, or failing.
5. R01's judgment pass then checks entailment on lines that passed: does the text claim more than the cited fact says?

## Commands
- `python3 engine/scripts/check_claims.py <draft.json> [--write]`
- `python3 -m pytest engine/tests` (needs `jsonschema`; the checker fails closed without it)
- `python3 engine/evals/machine_check.py <file>` (markdown outputs, unchanged)

## Known limits
- The Bash guard is a heuristic. It denies any command that names a protected file next to a write token, including heredocs that merely mention one. Use the Write tool for such files.
- Hooks fail closed (exit 2) on any error inside them. A missing `hooklib.py` or `python3` would still fail open, so keep the hooks directory intact.
- No renderer yet. Drafts are checked before render; the docx chain is still import_required.

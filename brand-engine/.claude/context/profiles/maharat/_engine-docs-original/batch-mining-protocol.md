# Batch mining protocol: unattended, one instructor at a time

The swarm-layer spec for running the full instructor mining (mine, QA, review) across
the whole roster in one unattended Claude Code session, without stopping between
instructors. Companion to context/mining-plan-v2.md (the pipeline) and
runtime/SWARM.md (the shapes). Invoked by /mine-all-instructors.

## The principle that makes unattended safe

The human gate is not removed; it becomes asynchronous. Decisions that need a human
(public status, held-back claims, register policy) are appended to
references/REVIEW-QUEUE.md instead of blocking the run. In exchange, two invariants are
absolute for everything the batch produces:

1. Internal only. No pack output is public-facing. No catalog public status ever moves
   off "unconfirmed" in a batch run. No campaign asset is generated.
2. Held-back by default. Any claim not verified with a source in-run goes to the
   held-back ledger and the queue, never into a render.

Mining writes knowledge into the repo; it does not send, publish, or spend. That is why
it may run unattended where campaign execution may not.

## Run order and state

- Order: catalog rows with pack status "todo", newest folders first (the standing batch
  order in mining-plan-v2 section 4). "mined" rows are skipped: re-running the batch is
  idempotent and resumes wherever it stopped.
- State lives in the repo, not in memory: the catalog pack-status column is the cursor.
  Statuses: todo -> mining (set when started) -> mined (set only after the QA and
  review passes both pass). A crash mid-instructor leaves "mining"; on resume, a
  "mining" row is re-run from its extraction log section (inventory is re-checked, not
  re-trusted).

## Per-instructor sequence (three passes, then commit)

```
PASS 1, MINE      inventory (2-pass) -> extract -> verify claims + status evidence
                  -> distill the full pack (fact file, SKILL, voice, templates incl.
                  every flagged candidate, evals with machine + llm layers)

PASS 2, QA        deterministic: python3 .claude/scripts/pack_check.py <slug>
                  must exit 0 (it runs eval_runner in both modes, validates structure,
                  golden cases, house style, registry, log)
                  then llm_checks: self-judge every llm_check in the pack's evals.json
                  against the pack's own renders; fix and re-run pack_check on any fail

PASS 3, REVIEW    the pilot-A meticulous review as a checklist, applied to this pack:
                  every promised template created; EN renders present; provenance
                  marked on anything from general knowledge; status-evidence recorded;
                  claims table covers every figure used anywhere in the pack; held-back
                  ledger complete; blockers section in SKILL.md current
                  fixes applied in the same run, then pack_check once more

REFLECT           catalog row -> mined; extraction-log section written;
                  REVIEW-QUEUE.md appended (status question + held-back claims);
                  git add the pack files and git commit:
                  "mine(<slug>): pack + evals + log [batch]"

CONTINUE          next instructor. No pause, no prompt.
```

## Failure isolation (the rule that keeps the batch moving)

- A pass failure returns to the distiller with the exact fixes (verify-then-advance),
  up to 3 repair cycles per instructor.
- After 3 failed cycles, or on a blocked folder (nothing readable): write the failure
  to the extraction log and REVIEW-QUEUE.md, set pack status "blocked", commit what is
  safe (log + queue only, never a half-pack), and continue to the next instructor.
  One bad folder must not stall the roster.
- Drive or web outage mid-run: same treatment, status "blocked", continue; the
  idempotent re-run picks blocked rows up later.

## What the batch must never do (unchanged from the engine)

Mark any instructor launched. Produce public-facing assets. Use an unverified claim in
a render. Adopt a new tool (Drive MCP is configured before the run per RUNBOOK
section 2, with approval). Push to a remote, publish, send, or spend: commits are
local; pushing is a human action after the queue review.

## After the batch (the human pass)

REVIEW-QUEUE.md is the single read for Ahmed (statuses, claims) and Arman (register
policy, brand questions). Each resolved item updates the catalog or fact file, and the
resolver deletes the queue entry. Only after that review may packs feed public-facing
campaign work.

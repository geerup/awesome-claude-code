---
description: Run the full subject mining batch unattended - mine, QA, and review passes for every remaining subject, one by one, without stopping, reflecting all output into the repo. Per runtime/batch-mining-protocol.md. Usage - /mine-all-subjects [start-slug]
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Bash(python3 .claude/scripts/eval_runner.py:*), Bash(python3 .claude/scripts/pack_check.py:*), Bash(git add:*), Bash(git commit:*), Bash(git status:*), Bash(git diff:*)
---

Run the unattended subject mining batch. Follow runtime/batch-mining-protocol.md
exactly; it is the contract for this run. "$ARGUMENTS" optionally names a start slug;
otherwise start from the first catalog row with pack status "todo" (or "mining" or
"blocked" to resume), newest folders first.

Load once at the start: CLAUDE.md, context/brand-voice.md, context/mining-plan-v2.md,
runtime/batch-mining-protocol.md, context/subjects/_CATALOG.md,
skills/subject-marketing/SKILL.md, and skim the reference pack
skills/subject-marketing/mona-ataya/ (imitate its shape and depth exactly).

Then loop over the roster. For EACH subject, with no pause and no prompt between
subjects:

1. Set the catalog pack status to "mining". Run PASS 1 (MINE) per
   commands/mine-subject.md steps 1 to 4: two-pass inventory into the extraction
   log, full extraction, claim verification with web sources, the status-evidence
   check, and the complete pack (fact file with claims table and held-back ledger;
   pack SKILL.md; voice.md; one-liner library with AR and EN renders; every template
   the folder's assets justify; evals.json with machine_checks carrying this
   subject's own blocked-claim regexes, llm_checks, and golden pass + fail cases).

2. PASS 2 (QA): run `python3 .claude/scripts/pack_check.py <slug>` and require exit 0.
   Then judge every llm_check in the pack's evals.json against the pack's own renders.
   Any failure: apply the exact fixes and re-run pack_check. Maximum 3 repair cycles.

3. PASS 3 (REVIEW): apply the meticulous-review checklist from the protocol (promised
   templates created, EN renders, provenance marks, status evidence recorded, every
   figure in the pack covered by a claims row, held-back ledger complete, SKILL.md
   blockers current). Fix in-run, then pack_check once more.

4. REFLECT: set catalog pack status "mined"; finish the extraction-log section
   (verification outcomes, blocked items, open questions); append this subject's
   section to references/REVIEW-QUEUE.md (status question + every held-back claim);
   then `git add` the pack's files plus catalog, log, and queue, and
   `git commit -m "mine(<slug>): pack + evals + log [batch]"`.

5. CONTINUE immediately to the next roster row.

Failure isolation: after 3 failed repair cycles, or if a folder is entirely
unreadable, set pack status "blocked", record the reason in the log and the queue,
commit only the log and queue changes, and continue. Never stall the roster on one
subject; never commit a half-pack.

Hard invariants for the entire run (from the protocol): no public status changes, no
public-facing assets, no unverified claim in any render, no git push, no new tool
adoption. The human gate is the REVIEW-QUEUE, reviewed after the batch by Ahmed and
Arman.

End of run: print a roster summary table (slug, status, repair cycles, queue items
added) and the single next action: review references/REVIEW-QUEUE.md.

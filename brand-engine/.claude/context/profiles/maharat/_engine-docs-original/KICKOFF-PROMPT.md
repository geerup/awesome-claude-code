# Claude Code kickoff prompt (paste as-is after merging the zip into the repo root)

Copy everything between the lines into Claude Code. It works whether or not the slash
commands registered, because it points at the protocol files directly.

---

You are operating the Maharat marketing engine repo. The `.claude/` directory in this
repo is your operating system for this session: it contains the rules, the plans, the
scripts, and one finished reference pack.

SETUP, do this first and report each result in one line:
1. Confirm these exist: `.claude/runtime/batch-mining-protocol.md`,
   `.claude/context/mining-plan-v2.md`, `.claude/scripts/pack_check.py`,
   `.claude/scripts/eval_runner.py`, `.claude/skills/instructor-marketing/mona-ataya/`,
   `.claude/context/instructors/_CATALOG.md`, `.claude/references/REVIEW-QUEUE.md`.
2. Run `python3 .claude/scripts/pack_check.py mona-ataya` and confirm exit 0. If it
   fails, stop and report; do not mine on a broken gate.
3. Confirm Google Drive access (list the instructor root folder per
   `.claude/RUNBOOK.md` section 2) and web search. If Drive is unavailable, stop and
   say exactly what to configure; do not improvise instructor content from memory.
4. Read, in order: `CLAUDE.md` (if present), `.claude/context/brand-voice.md` (if
   present), `.claude/context/mining-plan-v2.md`,
   `.claude/runtime/batch-mining-protocol.md`, `.claude/context/instructors/_CATALOG.md`,
   `.claude/skills/instructor-marketing/SKILL.md`, and skim the mona-ataya pack as the
   reference implementation you will imitate exactly.

TASK: execute the unattended batch per `.claude/runtime/batch-mining-protocol.md`.
Process every catalog row whose pack status is todo, blocked, or mining (resume
semantics), newest folders first, ONE INSTRUCTOR AT A TIME, with no pause and no
question between instructors. For each instructor run the three passes: MINE
(two-pass inventory, full extraction, web verification of every marketing claim,
status-evidence check), QA (`python3 .claude/scripts/pack_check.py <slug>` must exit
0, then self-judge the pack's llm_checks; max 3 repair cycles), REVIEW (the checklist
in the protocol, fixed in the same run, then pack_check again).

OUTPUT CONTRACT, exactly these files per instructor <slug>, modeled on mona-ataya:
- `.claude/context/instructors/<slug>.md`: fact file with bio, product themes, a
  claims table (every row verified with source link | unverified | disputed), a
  held-back ledger, assets and surfaces, audience notes, status-evidence line.
- `.claude/skills/instructor-marketing/<slug>/SKILL.md`: frontmatter (name,
  description), segments and angles, promise discipline, stream routing, blockers.
- `.claude/skills/instructor-marketing/<slug>/voice.md`: register finding, traits,
  signature beliefs, hook-pattern table, brand-register renders (MSA).
- `.claude/skills/instructor-marketing/<slug>/templates/one-liner-library.md`: AR
  renders by segment plus an EN renders section, verified claims only, held-back
  section listing blocked claims and their substitutes.
- `.claude/skills/instructor-marketing/<slug>/templates/<asset>.md`: one file per
  additional template the folder's assets justify (shot lists, cheatsheet patterns);
  every template candidate you flag, you create in the same run.
- `.claude/skills/instructor-marketing/<slug>/evals/evals.json`: machine_checks
  (house-style checks with applies_to "all", plus this instructor's own blocked-claim
  regexes with applies_to "assets"), llm_checks, and golden examples including one
  "pass" and one "fail".
And per instructor, update: the `_CATALOG.md` row (pack status, mined domain,
provenance), a new section in `.claude/references/drive-extraction-log.md`, a new
section in `.claude/references/REVIEW-QUEUE.md` (status question plus every held-back
claim), then `git add` those files and `git commit -m "mine(<slug>): pack + evals +
log [batch]"`.

RULES, absolute for the whole run:
1. Internal only: never set any public status to launched; never produce a
   public-facing campaign asset; never git push.
2. Claims discipline: no figure or biographical claim appears in any render unless its
   claims-table row is verified with a source you found this run. Unverified goes to
   the held-back ledger and the queue.
3. Never invent: class titles, lesson lists, launch dates, themes, instructor facts.
   Missing means recorded as to-confirm.
4. House style in every file you write: no em dashes, no en dashes, no tatweel,
   Western numerals only, empowering framing, never imply accreditation. Raw Drive
   content violates these: rewrite on extraction, never copy through.
5. Register: render new copy in Gulf-familiar MSA (and brand-tone English); source
   colloquial is reference only, per the interim policy in the hub SKILL.md.
6. Failure isolation: 3 failed repair cycles or an unreadable folder means pack status
   "blocked", reason logged to the extraction log and queue, commit only log and
   queue, continue to the next instructor. Never commit a half-pack. Never stall the
   roster.
7. No new tools, no scope changes, no edits to the protocol files themselves mid-run.

END OF RUN: print a summary table (slug | status | repair cycles | queue items added |
commit hash), list any blocked rows with reasons, and end with the single next action:
review `.claude/references/REVIEW-QUEUE.md` (Ahmed: statuses and claims; Arman:
register and brand questions).

Begin with the SETUP block now.

---

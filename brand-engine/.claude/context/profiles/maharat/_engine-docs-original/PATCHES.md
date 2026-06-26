# PATCHES.md: wiring edits needed in the real repo

This session's environment did not have the original `.claude/` scaffold mounted, so
files described in the PROJECT brief (the 7 original agents, the stream skills, the
SOPs) could not be edited directly. This file lists the exact edits to make in the real
repo when merging this drop-in. Delete each item as it lands.

## Applied status (layer 2 merge into the evolved engine, 2026-06-04)

- Item 1 (reads_first wiring): APPLIED to copywriter-ar and creative-director (catalog
  plus the named instructor pack added to reads_first). brand-qa-reviewer already routes
  through the instructor-marketing hub and judges the pack evals; no separate edit needed.
- Item 2 (lifecycle-architect mode label): SKIPPED on purpose. The evolved engine keeps
  the more descriptive "reasoning + gated send" for stream 7. Cosmetic only.
- Item 3 (reconciliation folds): DEFERRED, fold on next touch of each named file.
- Item 4 (settings.json): NOT APPLIED. Adding permission rules or enabling the gdrive MCP
  in settings.json is blocked by the harness self-modification guard; Ahmed configures it.
  Drive is also unavailable in this environment.
- Item 5 (skill discovery): CONFIRMED. instructor-marketing is discovered, and all 11
  per-instructor packs pass pack_check (exit 0).
- Item 6 (Ortto incumbent finding): DEFERRED fold, but FLAGGED. This names the email and
  WhatsApp platform incumbent (Ortto), which bears on the long-standing platform open item
  in references/2026-06-email-whatsapp-platform-research.md. Fold on next touch of that file.

The drop-in's older base copies of agents/ and runtime/{SWARM,verification,handoff-contract,
stream-ownership,README} were NOT merged; the session's evolved versions (21 agents, the
acquisition channels, the upgraded gate stack) were preserved.

## 1. reads_first wiring (instructor packs)

- `agents/copywriter-ar.md`: add to reads_first: `context/instructors/_CATALOG.md`,
  and the active instructor's fact file + pack when a brief names an instructor.
- `agents/creative-director.md`: same addition (already present if using this drop's
  version of the file; verify after merge).
- `agents/brand-qa-reviewer.md`: add: when reviewing an instructor asset, load the
  pack's evals.json llm_checks and judge them alongside brand checks.

## 2. lifecycle-architect mode label

`agents/lifecycle-architect.md` and `agents/_AGENTS-INDEX.md` should both read mode:
"execution (gated)" (the board's cleaner label), replacing "reasoning + gated send".

## 3. Items 1 to 6 of context/brainstorm-reconciliation.md and the six refinements of
context/miro-board-reconciliation.md

Each names the file it refines (human-gate Ahmed/Arman split, conversion event
taxonomy, ManyChat webhook mechanism, single-class buyers as sub-segment, stream-7
concrete numbers, scope exclusions). Fold them into the named files on next touch.

## 4. settings.json

- Add permission for the eval runner: `Bash(python3 .claude/scripts/eval_runner.py:*)`.
- Add the Google Drive MCP server (see RUNBOOK.md section 2) once approved per the
  build-vs-buy gate. Approval owner: Ahmed.

## 5. Skill discovery check

After merge, confirm Claude Code lists `instructor-marketing` as a discovered skill
(it sits one level under skills/, like the stream hubs). If sub-pack routing is not
picked up automatically, the hub SKILL.md's routing table is the fallback: it names
each sub-pack path explicitly.

## 6. Platform research reference (phase-2 finding)
`references/2026-06-email-whatsapp-platform-research.md` in the real repo: prepend the
Ortto incumbent finding (context/findings-email-platform.md here). The evaluation
reframes from greenfield selection to validate-Ortto-vs-shortlist, Arabic test first.

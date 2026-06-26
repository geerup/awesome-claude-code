---
description: Mine one instructor's Drive folder into a complete marketing pack (fact file, voice, skill, templates, evals), per context/mining-plan-v2.md. Usage - /mine-instructor <slug> [drive-folder-url]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 .claude/scripts/eval_runner.py:*), WebSearch, WebFetch
---

Mine the instructor "$ARGUMENTS" end to end. Follow context/mining-plan-v2.md exactly.
Load first: CLAUDE.md, context/brand-voice.md, context/instructors/_CATALOG.md,
skills/instructor-marketing/SKILL.md, and the pilot pack
skills/instructor-marketing/mona-ataya/ as the reference implementation.

Steps (verify-then-advance wraps each):

1. INVENTORY (two passes). Enumerate the instructor's Drive folder from the catalog
   link (pass 1: Drive MCP listing or search; pass 2: follow direct doc links found in
   pass 1 output). Write the inventory table into references/drive-extraction-log.md.
   Anything unreadable is logged as blocked, never skipped silently.

2. EXTRACT. Read every readable doc fully. Pull: product themes, marketing claims,
   hooks, voice traits, asset references, audience signals. Raw content will contain
   em dashes, tatweel, Eastern numerals, and colloquial register: never copy through.

3. VERIFY. For every marketing claim, run web verification (2 to 4 searches). Build the
   claims table: verified (with source link) | unverified | disputed. Run the
   status-evidence check (search for the instructor's class on the public Maharat
   site); record the result as evidence-neutral or supporting, never as confirmation.

4. DISTILL. Produce the pack per the v2 anatomy:
   - context/instructors/<slug>.md (fact file with claims table and held-back ledger)
   - skills/instructor-marketing/<slug>/SKILL.md (segments, angles, stream routing, blockers)
   - skills/instructor-marketing/<slug>/voice.md (register finding, hook patterns, brand renders)
   - skills/instructor-marketing/<slug>/templates/one-liner-library.md (AR + EN renders,
     by segment, verified claims only) plus every template the folder's assets justify
   - skills/instructor-marketing/<slug>/evals/evals.json (machine_checks with applies_to,
     llm_checks, golden pass and fail; copy the blocked-claim regexes from this
     instructor's own held-back ledger)

5. GATE. Run, and require the expected exits:
   - python3 .claude/scripts/eval_runner.py --docs <evals.json> <each governance file>  (expect 0)
   - python3 .claude/scripts/eval_runner.py <evals.json> <golden-pass-tmp>  (expect 0)
   - python3 .claude/scripts/eval_runner.py <evals.json> <golden-fail-tmp>  (expect 1)
   - validate evals.json parses; check every produced file for em dash, en dash,
     tatweel, Eastern numerals (expect none)
   On any failure: fix and re-run. Do not proceed with a failing gate.

6. REGISTER. Update the catalog row (pack status: mined; domain provenance: mined),
   append the extraction-log section with the verification outcomes and open items,
   and add any repo wiring needs to PATCHES.md.

7. STOP at the human gate. Output a summary: claims needing confirmation, the status
   question, blocked items, and what the pack enables. Do not mark public status, do
   not produce public-facing campaign assets. Approval comes from Ahmed (campaign) and
   Arman (brand) per context/brainstorm-reconciliation.md item 1.

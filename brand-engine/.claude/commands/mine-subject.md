---
description: Mine one subject (you, a service, a venture, or a research target) into a complete marketing pack (fact file, voice, skill, templates, evals). Usage - /mine-subject <slug> [source: a Drive folder URL, an uploaded folder, a website, or "me" for your own corpus]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 .claude/scripts/eval_runner.py:*), Bash(python3 .claude/scripts/pack_check.py:*), WebSearch, WebFetch
---

Mine the subject "$ARGUMENTS" end to end, following `runtime/batch-mining-protocol.md`.
Load first: `CLAUDE.md`, `context/brand-voice.md`, `context/subjects/_CATALOG.md`,
`skills/subject-marketing/SKILL.md`, the pack template
`skills/subject-marketing/_TEMPLATE-pack/`, and (for your own brand) `skills/subject-marketing/me/`.

A subject's source depends on its type:
- `me` or a person: your own corpus (uploaded writing, talks, transcripts, posts, CV, links).
  For your own content, prefer `/ingest` first, then this command consumes its output.
- a service or venture: your offer docs, site pages, past proposals, case studies.
- a research target (competitor / role model / company / role): public material only, mined to
  inform YOUR positioning, never to write copy that speaks as them.

Steps (verify-then-advance wraps each):

1. INVENTORY. Enumerate the source (Drive listing, uploaded folder, site crawl, or the
   corpus from /ingest). Write the inventory into `references/subject-extraction-log.md`.
   Anything unreadable is logged as blocked, never skipped silently.

2. EXTRACT. Read every readable item fully. Pull: themes, claims, hooks, voice traits, asset
   references, audience signals. Raw content may contain em dashes and (in Arabic) tatweel or
   Eastern numerals: never copy them through.

3. VERIFY. For every factual claim, run web or document verification (2 to 4 checks). Build the
   claims table: verified (with source) | unverified | disputed. For `me`, this is the guard
   against overstating your own credentials. Record what each claim is sourced to.

4. DISTILL. Produce the pack per the template anatomy:
   - `context/subjects/<slug>.md` (fact file with claims table and held-back ledger)
   - `skills/subject-marketing/<slug>/SKILL.md` (segments, angles, blockers)
   - `skills/subject-marketing/<slug>/voice.md` (register finding, hook patterns, brand renders)
   - `skills/subject-marketing/<slug>/templates/one-liner-library.md` (verified claims only;
     English primary, Arabic only if a brief sets it in scope) plus any templates the source justifies
   - `skills/subject-marketing/<slug>/evals/evals.json` (machine_checks with applies_to,
     llm_checks, golden pass and fail; add one blocked-claim machine_check per held-back row)

5. GATE. Run, and require the expected exits:
   - `python3 .claude/scripts/eval_runner.py --docs <evals.json> <each governance file>` (expect 0)
   - `python3 .claude/scripts/eval_runner.py <evals.json> <golden-pass-tmp>` (expect 0)
   - `python3 .claude/scripts/eval_runner.py <evals.json> <golden-fail-tmp>` (expect 1)
   - `python3 .claude/scripts/pack_check.py <slug>` (definition-of-done gate)
   On any failure: fix and re-run. Do not proceed with a failing gate.

6. REGISTER. Update the catalog row (pack status: mined), append the extraction-log section
   with verification outcomes and open items.

7. STOP at the human gate (you). Output a summary: claims needing confirmation, the status
   question (internal vs public, or observe-only for a research target), blocked items, and
   what the pack enables. Do not mark a subject public on your own; that is your explicit call.

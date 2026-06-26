# MasterClass reference email corpus

Verbatim `.eml` exports of 178 live MasterClass marketing emails, uploaded 2026-06-19 and extracted
individually into per-batch folders (batch1 to batch7). This is the primary source behind the
multi-instructor email work: the teardown in
`references/2026-06-masterclass-multiinstructor-teardown.md`, the angle method in
`context/multi-instructor-angles.md`, the PROMOTION pattern, and the build modules.

## What is here

- `batch1/` to `batch7/`: the marketing emails, one `.eml` per send, original filenames kept.
- `INDEX.md`: a generated catalog (per-batch subject list plus a multi-instructor and offer-signal
  tally), produced by `scripts/email_corpus_analyze.py`. Re-run that script to regenerate it:
  `python3 .claude/scripts/email_corpus_analyze.py`.

## Exempt from house style (verbatim external source)

These files are third-party source material, not engine output, the same status as
`references/ortto-email-archive/`. They are kept exactly as received, so they contain em dashes,
Eastern numerals, accreditation language, and other things the Maharat house style forbids in our
own output. Do not run the house-style sweep on this folder and do not edit the emails to conform.
`INDEX.md` quotes subjects verbatim for the same reason. The house rules apply to what the engine
authors, never to the reference corpus it learns from.

## Held out, not committed (privacy)

Six transactional items from batch 1 were deliberately excluded: a real person's MasterClass
receipt, refund, and invoice documents (two `.eml` and four `.pdf`). They are not marketing
templates and they carry personal and financial data, so committing them would breach the privacy
guardrail in `CLAUDE.md`. They remain only in the ephemeral upload area, not in the repo. If you
want them version-controlled anyway, that is your call to make explicitly.

## Reference only

MasterClass is a different brand with different rules. Borrow the structure and the angle craft,
never the copy mechanics. The adaptations and hard stops (no em dashes, no accreditation claims,
page-cleared credentials, catalog-status-confirmed instructors) are in the teardown and the angle
method.

# Kickoff Scope: [campaign_id]

Internal artifact, stream 1. The run plan strategy-lead carries into stream 2. Built on a
passed brief validation report. No customer-facing copy. No em dashes, Western numerals only.

- campaign_id: [from the brief filename]
- scoped_by: strategy-lead
- date: [YYYY-MM-DD]
- based_on: brief validation report for [campaign_id]

---

## 1. Entry point

- entry_point: [paid acquisition | owned audience]
- chosen_with_orchestrator: [yes, confirmed | pending confirmation]
- why: [one line tying the entry point to the brief objective and audience]

The two options, for the record:
- Entry point A, paid acquisition: full pipeline, streams 1 to 2, then 3 and 4 in parallel,
  then 5, 6, 7, 8, 9.
- Entry point B, owned audience: starts at lifecycle logic, no paid build. Stream 1, then 2,
  then 4, then 7, then 6 (if the email points anywhere), then 8, then 9.

## 2. Active streams (with owners)

| Stream | Runs this campaign | Owner | Note |
|---|---|---|---|
| 1 brief intake | yes | strategy-lead | done by this skill |
| 2 strategy and planning | [yes/no] | strategy-lead | [note] |
| 3 creative production | [yes/no] | creative-director | runs only if a message needs a visual asset |
| 4 copywriting | [yes/no] | copywriter-ar | [note] |
| 5 build and launch | [yes/no] | paid-build-engineer | paid path skipped for owned audience |
| 6 conversion path | [yes/no] | conversion-engineer | [note] |
| 7 lifecycle messaging | [yes/no] | lifecycle-architect | [note] |
| 8 monitoring and optimization | [yes/no] | analytics-reporter | [note] |
| 9 reporting and learning | [yes/no] | analytics-reporter | [note] |

## 3. Funnel path

[Entry] -> [signup gate: email | whatsapp | none] -> [lifecycle] -> [monitoring] -> [reporting]

State the order the active streams execute, in plain words.

## 4. Out of scope

- [stream or channel deliberately not run, and why]

## 5. Inherited open items (from brief-validate)

- ASSUMPTION: [field] [what it blocks if not confirmed before a gated action]
- OPEN ITEM: [item] [which active stream it affects]

A path blocked on a MISSING needed variable stays flagged here. Nothing is invented to make
the path look complete.

## 6. Readiness to start stream 2

[ready to plan] | [ready to plan with flagged assumptions] | [blocked on the stop-and-ask list]

---
name: aso-keyword-research
description: Research App Store and Google Play keywords and competitors for ASO, in Arabic and English. Use to find the search terms users use to find a self-development app, map relevance and volume and difficulty, and read the competitor listings, producing the keyword targets the store listing is built around. Triggers on "store keyword research," "app store keywords," "google play keywords," "aso keywords," "competitor app listings," "what do users search in the store." Sub-skill of aso, owned by aso-specialist.
---

# ASO Keyword Research (aso sub-skill)

Produces the keyword and competitor research that the store listing is built around. It finds the
terms users search to find a self-development app on the App Store and Google Play, in Arabic and
English, and reads the competitor listings. It sets the keyword targets; it does not write the
listing.

Owner: aso-specialist. Mode: reasoning. Grounded in approved store-data and research tools once
access is granted; any tool is proposed through build-vs-buy, never adopted here.

## When to use

- A store listing is being built or refreshed and needs keyword targets.
- The orchestrator dispatches ASO and the keyword set is not yet fixed.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, offer framing.
- The active `briefs/` file: the markets and store locales in scope, the objective.
- Brand and platform facts from `context/`: Maharat is an Arabic-first self-development platform,
  core market the GCC, primary Saudi.

If the markets or store locales are absent from the brief, stop and ask. Do not guess a locale, a
search volume, or a competitor the data does not show.

## The two stores, two languages

Research both stores and both languages; their fields and ranking signals differ:

- App Store: the title, subtitle, and a separate hidden keyword field all carry ranking weight.
- Google Play: the title and the description text carry ranking weight; there is no separate
  keyword field.
- Arabic and English are researched separately. Arabic is primary; English is not a translation
  afterthought. Western numerals only in any keyword note.

## Steps

1. Confirm the markets and store locales from the brief. If missing, stop and ask.
2. Build the seed set from the angle, the segments, and the self-development category, in Arabic
   and English.
3. Expand into a keyword map: for each term record relevance to Maharat, volume signal, and
   difficulty signal, by store and by language. Where a signal is unavailable, record it as
   unknown, never invented.
4. Read the top competitor listings per store and locale: their titles, subtitles, and the terms
   they appear to target. Note gaps Maharat can own.
5. Prioritize the keyword targets: high relevance first, balanced against volume and difficulty.
6. Hand the prioritized keyword targets and the competitor read to the hub and to
   `store-listing-optimization`.

## Output

The keyword research that feeds the `store` field of the `aso-package`:

```
keyword_map      per store and language: term, relevance, volume signal, difficulty signal
competitor_read  top competitor listings per store and locale, with the gaps to own
targets          the prioritized keyword targets the listing is built around
open_items       locale not confirmed, data source not approved, signal unavailable
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the two-store two-language coverage,
  and the no-invented-signal rule.
- The targets advance through the hub; the store text built from them runs `arabic-copy-qa` and
  `english-copy-qa`, then `brand-qa-reviewer`, per `runtime/verification.md`.

## Hard rules

- Arabic is primary, English is researched on its own terms, never as a translation afterthought.
- A volume, difficulty, or competitor signal the data does not show is recorded as unknown, never
  invented.
- Markets and locales come from the brief. Missing, stop and ask.
- Never invent a Skill Path title, the content lineup, an instructor name, an offer, or a price.
- No em dashes, no tatweel, Western numerals only.

---
name: store-listing-optimization
description: Optimize the App Store and Google Play store listing text for ASO, English-first with English. Use to write the title, subtitle, description, and keyword field around the researched keyword targets, within each store's character limits, with no accreditation claims and no invented Skill Path titles. Triggers on "store listing," "app store listing," "title and subtitle," "store description," "keyword field," "optimize the listing." Sub-skill of aso, owned by aso-specialist.
---

# Store Listing Optimization (aso sub-skill)

Produces the store text that fills the `store` field of the `aso-package`: the title, subtitle,
description, and keyword field, on the App Store and Google Play, English-first with English. It is
built around the keyword targets from `aso-keyword-research` and respects each store's character
limits. Final customer-facing wording routes through the copy gates; this skill drafts and
structures the store fields and hands them for QA.

Owner: aso-specialist. Mode: reasoning, and gated for any publish. Publishing a listing change is
a human gate action.

## When to use

- The keyword targets are set and the store fields need to be written or refreshed.
- The orchestrator dispatches ASO after keyword research.

## Inputs

- The keyword targets and competitor read from `aso-keyword-research`.
- The `strategy-artifact` (stream 2): the angle and offer framing.
- The active `briefs/` file: the offer, the markets and store locales, the campaign window.
- Brand voice from `context/brand-voice.md`: English-first, plain, confident, empowering.

If the offer or a locale needed for a field is absent, stop and ask. Never invent a Skill Path
title, the content lineup, an instructor name, an offer, or a price, and never imply a certificate
is accredited.

## The store fields

Build each field within its store's limit, leading with the priority keyword targets naturally:

- App Store: title (about 30 characters), subtitle (about 30 characters), the separate keyword
  field (about 100 characters, comma separated, no spaces wasted), and the description.
- Google Play: title (about 30 characters), short description (about 80 characters), and the full
  description, which carries ranking weight.
- Every field is written English-first, with the English equivalent on its own terms. Western
  numerals only. No em dashes. No tatweel.

App Store keyword-field mechanics. The keyword field is comma separated with no spaces wasted, and:

- No Apple-indexed stop words. Do not spend characters on words Apple already indexes automatically,
  for example "app" or "the" (and their Arabic equivalents). They add no reach.
- No repeats across fields. Do not repeat any word already used in the title or subtitle inside the
  keyword field. Apple indexes the title, subtitle, and keyword field together, so a repeated word
  is a wasted slot. Use the keyword field for terms the title and subtitle do not already carry.
- Exploit singular-or-plural and cross-field combinations. Include only one of a singular or plural
  form, not both, and rely on Apple combining single words across the title, subtitle, and keyword
  field into search phrases, so you do not need to spell out every multi-word phrase.

Custom Product Page keywords. When the creative skill plans Custom Product Pages, each CPP can carry
its own assigned keyword set. Map each CPP's keywords to the segment it serves, follow the same
mechanics above, and route the wording through the copy gates. Per-CPP keywords are a gated publish.

Google Play full description. The full description carries ranking weight. Lead with the priority
targets naturally and aim for a primary-keyword density near 2 to 3 percent. No keyword stuffing.

## Steps

1. Confirm the offer and the in-scope locales from the brief. If missing, stop and ask.
2. Draft each field per store, English-first with English, leading with the priority keyword
   targets and staying within each character limit.
3. Keep the voice plain, confident, and empowering, never deficit-framed. No accreditation claim,
   no fundraising, roadmap, or unannounced plans, no invented Skill Path title or instructor name.
4. Map each field to the keyword targets it serves, so the listing is provably built on research.
5. Note the localization: which locales each field is provided for, never guessing one not in the
   brief.
6. Route the drafted fields to `copywriter-ar` and the English copywriter for the copy gates, then
   hand the QA-passed fields to the hub for the `store` field of the `aso-package`.

## Output

Fills the `store` field of the `aso-package`:

```
title         App Store and Google Play, English-first with English, within the character limit
subtitle      App Store subtitle and Google Play short description, within the limit
description   the full description per store, English-first with English
keywords      the App Store keyword field, comma separated, no indexed stop words, no cross-field repeats, singular-or-plural and cross-field combinations exploited, mapped to the targets, plus any per-CPP keyword sets mapped to their segments
localization  which locales each field is provided for, none guessed
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the character limits, the
  keyword-to-field mapping, and the no-accreditation and no-invented-title rules.
- `arabic-copy-qa` on the Arabic fields and `english-copy-qa` on the English fields, then
  `compliance-privacy-check` if the listing collects data, then `brand-qa-reviewer`, then the
  human gate for any publish, per `runtime/verification.md`.

## Hard rules

- Every field stays within its store character limit and leads with the researched keyword targets.
- The App Store keyword field spends no characters on Apple-indexed stop words ("app," "the"),
  repeats no word already in the title or subtitle, carries only one of a singular or plural form,
  and relies on cross-field combinations. The Google Play full description aims for a
  primary-keyword density near 2 to 3 percent with no stuffing.
- English-first, with English on its own terms. No em dashes, no tatweel, Western numerals only.
- Never imply a certificate is accredited. Never invent a Skill Path title, the content lineup, an
  instructor name, an offer, or a price. Missing, stop and ask.
- No fundraising, roadmap, or unannounced plans in any field.
- Publishing a listing change is a gated action behind the human gate. Silence is not approval.

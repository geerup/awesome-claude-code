---
name: ad-copy
description: Write English-first ad copy, one headline plus body plus one CTA per variant per segment. Use when drafting paid or social ad text, triggers on "write the ad," "ad copy," "ad headline," "social copy." Produces copy-package variants[] ready for the gate stack.
---

# Ad copy (sub-skill of 04-copywriting)

Writes customer-facing ad text: a headline, a short body, and exactly one CTA, per variant
per segment. English-first, in the active brand voice. Self-contained, but assembled into the
`copy-package` by the 04 hub.

## Purpose

Give each segment from the strategy-artifact a tight, empowering ad that lands the angle in
one breath. Variants exist to test, not to pad: each variant is a real alternative for the
same segment and slot.

## When to use

- The campaign runs paid or social ads and needs the words.
- The `creative-package` has ad asset_briefs with copy-overlay slots to fill.

## Inputs

- `strategy-artifact`: the segment and the angle to land.
- The brief: offer and price, only if the ad shows them.
- `creative-package` asset_briefs: dimensions and copy-overlay slots, so copy fits the frame.
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. For each segment, restate the angle in one plain sentence to anchor the headline.
2. Write the headline: short, concrete, empowering. Speak to what the reader can build.
3. Write the body: one or two short lines that earn the click. Active voice, concrete nouns.
4. Write exactly one CTA. Clear and active. Never two competing actions.
5. Tag language ar or en. Arabic is primary; English follows the same spirit when needed.
6. Produce at least two variants per segment so the test has something to compare.
7. Map each variant to the asset_brief slot it fills.

## Output

`copy-package` variants[], each:

```
id        e.g. ad-seg1-v1
segment   the strategy-artifact segment name
headline  one line
body      one or two short lines
cta       exactly one
language  ar | en
```

See `templates/ad-copy-variants.md`.

## Optional structures to reach for

These are tools to test a line against, not mandatory structure. The English-first Thmanyah
voice stays primary. Reach for one when it sharpens a draft, drop it when it fights the voice.

- The 4 Us, a headline checklist. Is the headline Useful (Useful first), Urgent, Unique, and
  Ultra-specific? Use it to test a headline, not to force all four into one line.
- PAS (Problem, Agitate, Solution), an optional structure for pain-aware, bottom-funnel
  placements. Name the problem without shaming the reader, the empowering rule still holds.
- AIDA (Attention, Interest, Desire, Action), an optional structure for cold, top-funnel
  placements that move a stranger from notice to action.
- The 4 Cs (Clear, Concise, Compelling, Credible), a final pass on any line before it advances.

## Hard rules

- One CTA per variant. No em dashes. No tatweel or kashida. Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name. If the ad needs one
  and the brief is silent, stop and ask.
- Never imply certificate accreditation. Empowering, never deficit-framed.

## How it connects

Feeds the 04 hub's copy-package variants[] and fills. Every Arabic variant runs the gate
stack: skill eval, then `arabic-copy-qa`, then `brand-qa-reviewer`, per
`runtime/verification.md`. Only qa-passed variants advance.

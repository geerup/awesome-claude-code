---
name: landing-page
description: Specify the conversion landing page for stream 6. Use when a campaign needs an RTL-correct, on-brand, fast, uncluttered page with one clear CTA whose copy comes from the QA-passed copy-package. Triggers on "build the landing page," "spec the page," "the campaign page," "the signup page." Sub-skill of 06-conversion-path, owned by conversion-engineer.
---

# Landing Page (stream 6 sub-skill)

Produces the landing page spec that fills the `page` field of the `conversion-package`. It
realizes the build-ready `design_spec` from the `web-design-package` (authored by `web-designer`),
it does not originate the page design. The page is on brand, RTL-correct, fast, and uncluttered,
with one clear CTA. It does not write copy. Every word on the page traces to a QA-passed
`copy-package` variant by id.

Owner: conversion-engineer. Mode: execution (gated). Follows `sops/06-conversion-path.md`.

## When to use

- The brief lands traffic on a page (paid acquisition) or the lifecycle emails point to one.
- You need a build-ready page spec before any publish.

## Inputs

- The QA-passed `web-design-package` `design_spec` from `web-designer`: the responsive layout,
  design tokens, interaction states, RTL behavior, accessibility, and performance the page realizes.
- The QA-passed `copy-package`: headline, body, one CTA per variant, by segment and language.
- The active `briefs/` file: offer, and price or promotion only when the page shows them.
- The `creative-package` asset refs, when the page carries art.
- `context/brand-voice.md`: the voice, visual constants, and hard mechanical rules.

If the copy-package is not yet qa-passed, stop. The page does not invent words to fill a gap.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the
   needed variant ids present. If incomplete, return it.
2. Choose the page structure: hero with one headline, supporting body, one primary CTA, and
   only the sections the offer needs. Cut anything that does not move the click.
3. Bind each text region to a copy variant id. No region carries free text written here.
4. Apply the visual constants: background #141414, card surfaces #1A1A1A, primary accent
   emerald #009975. The accent is a highlight, not a flood. Generous space.
5. Set RTL: the document direction is right-to-left, Arabic copy is primary, mixed Arabic,
   English, or numerals must not break direction. Western numerals only.
6. Specify performance: fast first render, minimal blocking assets, the CTA visible without
   a scroll on mobile.
7. Hand the spec to the hub for operational verification (renders RTL-correct in test) and
   into the `conversion-package` page field.

## Output

A landing page spec for the `page` field of the `conversion-package`:

```
layout         hero, body sections, one primary CTA, region-to-variant binding
copy_refs      copy-package variant ids for every text region (no free text)
visual         #141414 background, #1A1A1A surfaces, #009975 accent, spacing notes
rtl            direction rtl, Arabic primary, numeral and mixed-direction handling
performance    render budget, asset notes, mobile CTA placement
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and the mechanical rules.
- `arabic-copy-qa` on the Arabic page copy, then `brand-qa-reviewer` on the page, per
  `runtime/verification.md`. A fail returns to the author with exact fixes.
- Operational: the page renders RTL-correct in test before go-live at the human gate.

## Hard rules

- One clear CTA. Not two competing primary actions.
- Copy comes from the QA-passed copy-package, never invented on the page.
- RTL renders correctly. Western numerals. No em dashes, no tatweel.
- Never imply certificates are accredited. Never invent a Skill Path title, instructor name,
  offer, or price.

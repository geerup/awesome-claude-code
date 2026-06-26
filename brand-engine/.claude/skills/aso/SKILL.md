---
name: aso
description: Hub for app store optimization, owned by aso-specialist, the reasoning and gated-publish layer that grows organic installs on the App Store and Google Play across Arabic and English. Use to research store keywords and competitors, optimize the store listing (title, subtitle, description, keyword field), and plan store creatives, experiments, and a reviews response policy. Routes to aso-keyword-research, store-listing-optimization, and store-creative-and-experiments, and assembles the aso-package. Triggers on "ASO," "app store optimization," "store listing," "store keywords," "app store keywords," "store screenshots," "store A/B test," "app reviews," "ratings and reviews."
---

# App Store Optimization (hub)

Owns the organic install surface: how the brand is found and chosen on the App Store and Google
Play, in English and optionally Arabic. Owner: `aso-specialist`. Mode: reasoning for the plan, gated for any
publish of a store change. This hub does not write final marketing copy outside the store fields,
does not design final creative, and does not publish store changes. It validates inputs, routes
to the right sub-skill, and assembles the `aso-package`.

ASO is an organic channel: it feeds the same install and signup funnel that paid and organic
social feed. Publishing any store listing change, creative, or experiment is a gated action behind
the human gate.

## When to use

- A brief or strategy calls for more organic installs, or a store listing refresh.
- The campaign needs store keyword research, a listing optimization, store creative direction, a
  store A/B experiment plan, or a reviews response policy.
- The orchestrator dispatches ASO (per `runtime/stream-ownership.md`).

## Sub-skills (routing)

- `aso-keyword-research`: App Store and Google Play keyword and competitor research, in English and
  optionally Arabic. Use first; it sets the keyword targets the listing is built around.
- `store-listing-optimization`: the title, subtitle, description, and keyword field, English-first,
  built around the researched keywords. Use after keyword research; it produces the
  store text.
- `store-creative-and-experiments`: the screenshots, preview video, store A/B experiments, and the
  ratings and reviews response policy. Use for the visual store surface and how it is tested and
  how reviews are handled.

Route: keyword research first to fix the targets, then listing optimization to write the store
fields, then creative and experiments for the visual surface and testing. All three feed the same
`aso-package`.

## Inputs

- The `strategy-artifact` (stream 2): segments, the angle, offer framing, success_metric.
- The active `briefs/` file: objective, the markets and store locales in scope, the offer, and the
  campaign window.
- Store text copy is English-first and routes through `copywriter-en` for the copy gates, with
  `copywriter-ar` only when a brief sets Arabic in scope. Store creative comes from `creative-director`
  and the designer. Generated images stay text-free; any Arabic overlay is added in the build, never
  baked into a generated image.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the gap with
an invented value. Never invent an offer title, the content lineup, a subject name, a service, or a
price, and never imply a credential or accreditation you do not hold.

## Steps

1. Validate the incoming envelope: right campaign_id, strategy-artifact present with the angle,
   segments, and success_metric, open_items read. If incomplete, return it.
2. Route to `aso-keyword-research` for the App Store and Google Play keyword and competitor map, in
   English and optionally Arabic.
3. Route to `store-listing-optimization` for the title, subtitle, description, and keyword field,
   English-first, built around the researched keywords.
4. Route to `store-creative-and-experiments` for the screenshots, preview video, store A/B
   experiment plan, and the reviews response policy.
5. Set the localization: which store locales are in scope and how English and any in-scope Arabic are
   handled per field, never guessing a locale not in the brief.
6. Assemble the `aso-package` and stop at the human gate. Publishing any store change is one gated
   action; nothing publishes without explicit sign-off.

## Output: the aso-package

```
store         title, subtitle, description, keywords, localization, all English-first
creatives     screenshots and preview video direction, text-free generated images, Arabic in build
experiments   store A/B experiment plan, each with a hypothesis tied to the success_metric
reviews_response_policy  how ratings and reviews are answered, with escalation rules
open_items    anything unresolved (locale not confirmed, store access, asset not yet QA-passed)
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs), per `runtime/handoff-contract.md`.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), QA-passed store copy from `copywriter-en` and, when
  Arabic is in scope, `copywriter-ar`, store creative from `creative-director` and the designer.
- Produces: the `aso-package`. It feeds the organic install funnel and its install and conversion
  data feeds monitoring (stream 8).
- Gate before advance: skill eval, then `arabic-copy-qa` on Arabic store text and `english-copy-qa`
  on English store text, then `design-qa` on store creative, then `compliance-privacy-check` on
  anything that collects data or publishes, then `brand-qa-reviewer`, then the human gate for any
  publish, per `runtime/verification.md`.

## Hard rules

- The hub plans and routes; it never publishes a store change. Publishing is a gated action behind
  the human gate, per change and per campaign. Silence is not approval.
- Never invent an offer title, the content lineup, a subject name, a service, or a price.
  Missing, stop and ask.
- Never imply a credential or accreditation you do not hold. No fundraising, roadmap, or unannounced
  plans in any store field or creative.
- Generated store images stay text-free; Arabic overlay is added in the build, never baked in.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.

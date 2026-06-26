---
name: store-creative-and-experiments
description: Plan the store creative, A/B experiments, and reviews response policy for ASO. Use to direct the screenshots and preview video, plan store A/B experiments tied to the success_metric, and set the ratings and reviews response policy with escalation rules. Generated images stay text-free; Arabic overlay is added in the build. Triggers on "store screenshots," "app preview video," "store A/B test," "store experiment," "ratings and reviews," "review response policy." Sub-skill of aso, owned by aso-specialist.
---

# Store Creative and Experiments (aso sub-skill)

Produces the visual store surface and how it is tested and maintained: the screenshots and preview
video direction, the store A/B experiment plan, and the ratings and reviews response policy. It
fills the `creatives`, `experiments`, and `reviews_response_policy` parts of the `aso-package`.
This skill directs and plans; the designer executes the visuals and runs design-qa, and any
overlay text is added in the build.

Owner: aso-specialist. Mode: reasoning, and gated for any publish or experiment launch.

## When to use

- The listing is set and the store needs its screenshots, preview video, an experiment plan, or a
  reviews policy.
- The orchestrator dispatches ASO after the listing is drafted.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, success_metric.
- The store listing and keyword targets from the other aso sub-skills.
- The active `briefs/` file: the markets and store locales, the campaign window.
- Store creative comes from `creative-director` and the designer. Video repurposing (one video into
  many store formats) uses an approved tool, gated and added on approval.

If a needed variable is absent, stop and ask. Never invent a Skill Path title, the content lineup,
an instructor name, an offer, or a price, and never imply a certificate is accredited.

## The visual surface (text-free generation, Arabic in build)

- Screenshots: direct the set per store and locale, each mapped to a benefit and a segment. The
  generated image is text-free. Any Arabic or English overlay caption is added in the build by the
  designer, never baked into a generated image. Western numerals only in any rendered text.
- Preview video: direct the concept, length, and beats. Same rule: no Arabic text baked into a
  generated frame; overlays are added in the build.
- Visual constants apply: near-black #141414, card surfaces #1A1A1A, emerald accent #009975,
  premium and uncluttered.

## Store A/B experiments

- App Store: Product Page Optimization. Google Play: store listing experiments.
- Each experiment states one hypothesis, the single variable it changes (an icon, a screenshot
  set, a subtitle), the metric it reads (tied to the success_metric, for example install
  conversion rate), and the decision rule. No experiment changes more than one variable at a time.
- Run length and treatment limits. Google Play store listing experiments run a minimum of 7 days
  to cover a full weekly cycle (weekday and weekend traffic), one asset per test. Apple PPO runs up
  to 90 days and tests up to 3 treatments against the original, changing only the icon, the
  screenshots, or the app previews. Set the read window with the decision rule, and do not read a
  result before the window closes.
- Launching an experiment is a gated action behind the human gate. Nothing goes live on the store
  without sign-off.

## Custom Product Pages (App Store) and the PPO-then-CPP workflow

- Apple Custom Product Pages (CPP) let one app serve up to 70 alternate product pages, each with
  its own screenshots, app previews, promotional text (up to 170 characters), and its own assigned
  keywords so a CPP can surface in organic search. Each CPP maps to a segment, the same
  segment-mapped screenshot direction used for the default page.
- Workflow: run PPO first to find the winning creative against the original, then deploy that
  winner as a CPP for the segment that responded best, with the per-CPP keyword set assigned to the
  organic and paid traffic that segment is served. PPO finds the winner; CPP routes it to
  segment-specific traffic.
- Each CPP's screenshots and previews follow the same rules: text-free generation, Arabic and
  English overlays added in the build, Western numerals, the visual constants. The 170-character
  promotional text and the assigned keywords route through the copy gates.
- Publishing or assigning a CPP is a gated action behind the human gate. Silence is not approval.

## Reviews and ratings response policy

- Set on-brand response templates for common review themes, in Arabic and English, plain and
  empowering, never defensive.
- Set escalation rules: a review that touches a bug, a refund, a data or privacy concern, or a
  safety or legal matter escalates to the owner rather than getting a templated reply.
- Never imply accreditation, never name an instructor without confirmation, never share personal
  data of a reviewer in a public reply.

## Steps

1. Direct the screenshot set and preview video per store and locale, each text-free and mapped to a
   benefit and segment, with overlay slots for the build.
2. Plan the store A/B experiments: one hypothesis and one variable each, tied to the
   success_metric, with a decision rule and a read window (minimum 7 days on Google Play, up to 90
   days and 3 treatments on Apple PPO).
3. Plan the Custom Product Pages: map each CPP to a segment with its own screenshots, previews,
   170-character promotional text, and assigned keywords, deploying PPO winners as CPPs for the
   segment that responded best.
4. Set the reviews response policy and the escalation rules, in Arabic and English.
5. Route the creative to `creative-director` and the designer for execution and design-qa.
6. Hand the creative direction, experiment plan, Custom Product Pages, and reviews policy to the
   hub for the `aso-package`. Nothing publishes or launches without the human gate.

## Output

Fills three parts of the `aso-package`:

```
creatives                screenshot and preview video direction, text-free, overlay in build, per store and locale, plus Custom Product Pages mapped to segments with assigned keywords and 170-char promo text
experiments              store A/B experiments, each: one hypothesis, one variable, success_metric-tied metric, decision rule, read window (7 days min on Play, up to 90 days and 3 treatments on Apple PPO)
reviews_response_policy  on-brand response templates plus escalation rules, Arabic and English
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the text-free generation rule, the
  one-variable experiment rule, and the escalation rule.
- `design-qa` on the rendered creative, `arabic-copy-qa` and `english-copy-qa` on any overlay or
  reply copy, `compliance-privacy-check` on the reviews policy and any data collection, then
  `brand-qa-reviewer`, then the human gate for any publish or experiment launch, per
  `runtime/verification.md`.

## Hard rules

- Generated store images stay text-free. Arabic and English overlays are added in the build, never
  baked into a generated image.
- Each experiment changes exactly one variable and reads a metric tied to the success_metric, and
  holds for its full read window: minimum 7 days on Google Play, up to 90 days and at most 3
  treatments on Apple PPO.
- Custom Product Pages map to segments, each with its own assigned keywords and a 170-character
  promotional text, and follow the text-free generation and overlay-in-build rule. PPO finds the
  winner first, then the winner deploys as a CPP for the segment that responded best.
- A review touching a bug, refund, privacy, safety, or legal matter escalates, never a templated
  reply. Never expose a reviewer's personal data in a public reply.
- Never imply a certificate is accredited. Never invent a Skill Path title, the content lineup, an
  instructor name, an offer, or a price.
- Publishing creative or launching an experiment is a gated action behind the human gate. Silence
  is not approval.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.

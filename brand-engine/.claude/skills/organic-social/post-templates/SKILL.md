---
name: post-templates
description: Reusable organic social post templates for Maharat, extracted and normalized from the team's organic copy doc. Use to scaffold a specific post format fast, story engagement sequence, countdown or launch story, value carousel, myth-buster carousel, skills roundup carousel, or quote inspiration carousel. Triggers on "story template," "carousel template," "post template," "countdown story," "myth buster," "skills roundup," "give me the format for." Sub-skill of organic-social, owned by organic-social. Provides structure only; captions are written by copywriter-ar and copywriter-en, visuals by creative-director and the designer.
---

# Post Templates (organic-social sub-skill)

A library of reusable, campaign-agnostic templates for the organic post formats Maharat uses.
Each template is a scaffold: the slide or story order, what each beat does, the engagement
mechanic, and the copy-overlay and CTA slots. It does not write captions and does not publish.
It gives `organic-content-plan` and the copywriters a fast, on-brand starting structure.

Owner: `organic-social`. Mode: reasoning. Feeds the content plan and the `organic-package`.
Grounded in `context/profiles/maharat/organic-social-style.md` and `context/brand-voice.md`.

## When to use

- The content plan calls for a known format and wants the proven structure for it.
- A copywriter or the designer needs the beat-by-beat scaffold before writing or laying out.
- The orchestrator or `organic-content-plan` routes here for a format template.

## The templates (in templates/)

- `story-engagement-sequence.md`: a 4-beat story funnel, hook, tension or chaos, poll, pain
  point. Drives participation and warms the audience.
- `countdown-launch-story.md`: a 3-beat launch story, countdown intro, engagement poll, CTA
  lead-gen with a keyword. For a drop, launch, or early-access push.
- `value-carousel.md`: a 5-slide educational carousel, hook, pain or invite, what is inside,
  visual, outcome and CTA. For a lead magnet or guide.
- `myth-buster-carousel.md`: a cover plus myth-and-truth slides plus a closer CTA. For
  reframing a common belief.
- `skills-roundup-carousel.md`: a cover, one slide per skill or theme with a watch line and an
  outcome, then a CTA. For a multi-class or seasonal roundup.
- `quote-inspiration-carousel.md`: a cover plus one attributed quote per slide. High-save
  inspiration. Quotes are real and attributed, never invented.

## Inputs

- The `strategy-artifact` angle and segments, and the active brief (objective, accounts,
  window, the campaign keyword and offer if any).
- `context/profiles/maharat/organic-social-style.md` for the formatting legend, bilingual convention, and CTA
  mechanics.
- Captions come from `copywriter-ar` (AR) and `copywriter-en` (EN), referenced by variant id.
  Visuals come from `creative-director` and the designer.

If the format, the keyword, the offer, or the accounts are not set, stop and ask. Do not invent
a keyword, an offer, a price, an instructor name, a Skill Path title, or the content lineup.

## Steps

1. Pick the template that matches the format the content plan called for.
2. Fill the scaffold with placeholders resolved from the brief and strategy-artifact. Leave
   [KEYWORD], [OFFER], [INSTRUCTOR], [CLASS TITLE] as placeholders until the brief supplies them.
3. Route the customer-facing copy slots to `copywriter-ar` and `copywriter-en`. Route the
   visual slots to `creative-director` and the designer. Never bake Arabic into a generated
   image.
4. Hand the filled scaffold back to `organic-content-plan` for the calendar and the
   `organic-package`. Run the skill eval.

## Verification gates

- Skill eval (this file's `evals/evals.json`).
- Captions run the gate stack: skill eval, `arabic-copy-qa` on Arabic, `english-copy-qa` on
  English, then `brand-qa-reviewer`. Visuals run `design-qa`. Publishing is a human-gate action.

## Hard rules

- Structure only. Never write final captions, never publish. Every post references a QA-passed
  copy variant by id.
- Campaign-agnostic. Keywords, offers, instructor names, and titles are brief inputs, never
  invented. Missing, stop and ask.
- Visual palette follows the brand constants (#141414, #1A1A1A, emerald #009975). The bright
  seasonal backgrounds in the source doc are not adopted by default, see the reconciliation in
  `context/profiles/maharat/organic-social-style.md`.
- No accreditation claims, no fundraising, roadmap, or unannounced plans.
- Never put personal or sensitive data in a tracking URL parameter.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.

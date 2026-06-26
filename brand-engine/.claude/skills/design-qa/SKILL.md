---
name: design-qa
description: The visual and design quality gate. Use to check any rendered or specified visual asset before it advances, triggers on "design QA," "check the design," "is this visual on brand," "review the creative," "QA the asset." Verifies RTL correctness, the brand visual constants, Western numerals in any rendered text, no Arabic text baked into generated images, safe areas and dimensions present, and a premium uncluttered result, returning pass or a structured fix list. It keeps a human design check as the final manual step.
---

# Design QA (the visual gate)

The visual and design quality gate, used by the designer agent. Runs on rendered or specified
visual assets: image and video concepts, asset briefs, exported creatives, landing page
visuals. A verifier, not a designer: it never edits the asset, it returns pass, or fail with
an exact fix list. The author regenerates against the list and resubmits to this same gate.

## Purpose

Catch visual defects before the asset advances toward brand QA and the human gate: broken
RTL, off-brand color, Eastern numerals in rendered text, Arabic text baked into a generated
image instead of being a real overlay, missing safe areas or dimensions, and cluttered
non-premium layouts. A clean pass means the human design check reviews taste and fit, not
basic visual hygiene the swarm should have caught.

## When to use

- Stream 3 creative: image and video concepts, prompts, asset briefs.
- Stream 6 conversion: landing page visuals and layout.
- Any exported or specified creative before it advances to `brand-qa-reviewer` and the human
  gate.

## Inputs

- The asset under review: rendered image or video, or the spec and asset brief for one.
- `context/brand-voice.md`: the visual constants, the premium-uncluttered bar, the RTL and
  numeral rules.
- The asset brief: declared dimensions, safe areas, and copy-overlay slots.

## The checks

Run each. Report every failing item, not just the first.

1. rtl-correct: the layout renders right-to-left correctly. Mixed Arabic, English, or
   numerals do not break direction, alignment, or reading order.
2. visual-constants: color matches the brand constants, near-black background #141414, card
   surfaces #1A1A1A, primary accent emerald #009975. The accent is a highlight, not a flood.
3. western-numerals-rendered: any numerals shown in rendered text are Western 0 to 9, never
   Eastern Arabic numerals.
4. no-baked-arabic-text: no Arabic text is baked into a generated image. Copy is a real
   overlay placed in the asset brief's copy-overlay slots, filled by copywriter-ar, never
   rendered inside the generated image itself.
5. safe-areas-dimensions: declared dimensions and safe areas are present and respected, with
   no critical content clipped by platform crops.
6. premium-uncluttered: the result is premium and uncluttered, generous space, clear
   hierarchy, no visual noise that breaks the brand bar.

## Steps

1. Inspect the rendered asset, or read the spec and asset brief, against the six checks.
2. For each failing check, capture the offending element, quoted or described exactly.
3. Decide the result: pass only when every check passes, otherwise fail.
4. Return the result in the shape below. Never edit the asset.

## Output

- Pass: the asset advances to `brand-qa-reviewer`, then to the human design check.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, span: "<the offending element, quoted or described>", fix: "<the required change>" }
```

Example: `{ check: "no-baked-arabic-text", span: "headline rendered inside the generated image", fix: "remove the baked text, leave the copy-overlay slot empty for copywriter-ar" }`.

See `templates/design-qa-fix-list.md`.

## Hard rules

- Never edit the asset. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- No item is waved through. The author regenerates against the full list and resubmits here.
- A human design check is the final manual step. Passing this gate and brand QA does not
  replace it. Generated tools have weak Arabic text-in-image, so a person signs off on the
  visual before anything publishes.

## How it connects

- Runs in the gate stack before `brand-qa-reviewer` for visual assets, per
  `runtime/verification.md`. On pass, the asset advances to brand QA, then the human design
  check; on fail, it returns to the designer agent with the fix list.
- Enforces the creative rule that Arabic text is never baked into generated images, the
  copy-overlay slots are filled later by copywriter-ar, per the creative-package contract in
  `runtime/handoff-contract.md`.

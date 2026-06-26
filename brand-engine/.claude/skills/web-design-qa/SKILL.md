---
name: web-design-qa
description: The web design quality gate. Use to check a web or landing-page design spec before it advances, triggers on "web design QA," "check the page design," "is this page design on brand," "RTL check the page design," "review the responsive spec." Verifies responsive RTL correctness at every breakpoint, the brand visual constants, Western numerals in rendered text, no Arabic baked into generated imagery, declared breakpoints with clean reflow, interaction states, accessibility, a performance budget, one primary action per view, and a premium uncluttered result, returning pass or a structured fix list. It keeps a human design check as the final manual step.
---

# Web Design QA (the web design gate)

The web design quality gate, used by the web-designer agent. Runs on a web or landing-page
`design_spec`: components, responsive grid, breakpoints, type scale, tokens, states, RTL
behavior, accessibility, and performance. A verifier, not a designer: it never edits the spec,
it returns pass, or fail with an exact fix list. The author fixes against the list and resubmits
to this same gate. It is the web counterpart to `design-qa`: `design-qa` checks creative visuals
in stream 3, this checks web surfaces in stream 6.

## Purpose

Catch web design defects before the spec advances toward brand QA and the human gate: broken
RTL at a breakpoint, off-brand tokens, Eastern numerals in rendered text, Arabic baked into a
generated image, missing breakpoints or clipped reflow, missing interaction or error states,
weak accessibility, an unbudgeted page, or two competing primary actions. A clean pass means the
human design check reviews taste and fit, not basic web hygiene the swarm should have caught.

## When to use

- Stream 6 web design: the `design_spec` of the `web-design-package` from the web-designer.
- Any specified web or landing-page design before it advances to `brand-qa-reviewer` and the
  human gate.

## Inputs

- The `design_spec` under review: the responsive spec, tokens, states, RTL, accessibility, and
  performance fields.
- `context/brand-voice.md`: the visual constants, the premium-uncluttered bar, the RTL and
  numeral rules.
- The direction half of the `web-design-package`: information architecture and wireframes, for
  the one-primary-action and reflow checks.

## The checks

Run each. Report every failing item, not just the first.

1. responsive-rtl: the layout renders right-to-left correctly at every breakpoint. Mixed
   Arabic, English, or numerals do not break direction, alignment, or reading order at any width.
2. visual-constants: tokens match the brand constants, near-black background #141414, card
   surfaces #1A1A1A, primary accent emerald #009975, used as a highlight not a flood.
3. western-numerals-rendered: any numerals shown in rendered text are Western 0 to 9, never
   Eastern Arabic numerals.
4. no-baked-arabic-text: no Arabic text is baked into a generated image. Copy is real text bound
   to a copy-package variant id, never rendered into the generated pixels.
5. responsive-breakpoints: breakpoints are declared and content reflows without clipping or
   overflow, with the primary action visible without a scroll on mobile.
6. interaction-states: default, hover, focus, active, disabled, loading, and error states are
   specified for interactive elements.
7. accessibility: contrast meets the bar, focus order is logical, structure is semantic, touch
   targets are sized, alt text slots exist.
8. performance-budget: a render budget is stated, blocking assets are minimal, image weight is noted.
9. one-primary-action: exactly one primary action per view, not two competing CTAs.
10. premium-uncluttered: the result is premium and uncluttered, generous space, clear hierarchy.

## Steps

1. Read the `design_spec` and the direction against the ten checks.
2. For each failing check, capture the offending element, quoted or described exactly.
3. Decide the result: pass only when every check passes, otherwise fail.
4. Return the result in the shape below. Never edit the spec.

## Output

- Pass: the spec advances to `brand-qa-reviewer`, then to `conversion-engineer` and the human
  design check.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, span: "<the offending element, quoted or described>", fix: "<the required change>" }
```

Example: `{ check: "responsive-rtl", span: "hero reverts to ltr at the md breakpoint", fix: "set direction rtl at every breakpoint, keep Arabic reading order top-right" }`.

See `templates/web-design-qa-fix-list.md`.

## Hard rules

- Never edit the spec. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- No item is waved through. The author fixes against the full list and resubmits here.
- A human design check is the final manual step. Passing this gate and brand QA does not replace
  it. Generative tools have weak Arabic text-in-image, so a person signs off on any Arabic surface
  before anything publishes.

## How it connects

- Runs in the gate stack before `brand-qa-reviewer` for web surfaces, per
  `runtime/verification.md`. On pass, the spec advances to brand QA, then to conversion-engineer
  and the human design check; on fail, it returns to the web-designer with the fix list.
- Enforces the rule that Arabic text is never baked into generated imagery, copy binds to
  variant ids filled by copywriter-ar, per the web-design-package contract in
  `runtime/handoff-contract.md`.

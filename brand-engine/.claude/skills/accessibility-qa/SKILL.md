---
name: accessibility-qa
description: The accessibility quality gate for customer-facing pages and emails. Use to check a landing page, signup gate, or email render against WCAG 2.2 AA before it advances, triggers on "accessibility check," "a11y review," "WCAG check," "is this page accessible," "check the contrast," "screen-reader check." Verifies contrast against the fixed brand palette, RTL and reading order, text alternatives, semantic structure, control and link labels, target size, keyboard and focus, color independence, and motion, returning pass or a structured fix list. Used by the accessibility-reviewer agent.
---

# Accessibility QA (the a11y gate)

The accessibility quality gate, used by the `accessibility-reviewer` agent. Runs on
customer-facing pages and emails: landing pages, the signup gate, and email renders. A
verifier, not an author: it never edits the asset, it returns pass, or fail with an exact fix
list. The author regenerates against the list and resubmits to this same gate.

## Purpose

Catch accessibility defects before the asset advances toward brand QA and the human gate: text
that fails contrast, broken RTL reading order, images with no text alternative, flat or missing
structure, unlabeled controls, targets too small to tap, keyboard traps, meaning carried by
color alone, and motion that cannot be paused. The brand palette is fixed, so this gate verifies
the palette is used in pairings that clear contrast, and fixes usage, never the brand.

## When to use

- Stream 6 conversion: the landing page and the signup gate.
- Stream 7 lifecycle: the email render.
- Any customer-facing page or email before it advances to `brand-qa-reviewer` and the human gate.

## Inputs

- The asset under review: the rendered page or email, or the spec for one.
- `context/brand-voice.md`: the fixed palette and the Western-numeral rule.
- `runtime/verification.md`: the gate stack and the fix-list shape.

## The checks

Run each. Report every failing item, not just the first. WCAG 2.2 AA, scoped to pages and emails.

1. contrast-aa: text and meaningful UI clear WCAG AA against the fixed palette (#141414
   background, #1A1A1A cards, emerald #009975 accent). Normal text at least 4.5:1, large text
   and UI at least 3:1. Emerald as body text on the dark surfaces is the common failure.
2. rtl-reading-order: logical order matches visual order in Arabic, no LTR leakage, layout
   mirrored, Western numerals preserved in rendered text.
3. text-alternatives: every meaningful image has an alt-text slot for the author to fill,
   decorative images marked decorative, no meaning carried by image alone, no Arabic baked into
   a generated image.
4. semantic-structure: one logical heading order, landmarks present, lists marked as lists, the
   email carries semantic structure and a plain-text alternative, never image-only.
5. control-and-link-labels: every link and button has a descriptive label, no bare "اضغط هنا"
   or "click here", signup-gate fields have programmatic labels.
6. target-size: interactive targets large enough and not crowded, usable on mobile.
7. keyboard-and-focus: focusable in a sensible order, focus visible, nothing reachable only on
   hover or pointer.
8. color-independence: no state or meaning conveyed by color alone (error, required, selected).
9. motion-safe: no autoplay that cannot be paused, nothing flashing, motion respects
   reduced-motion.

## Steps

1. Inspect the rendered page or email, or read the spec, against the checks.
2. For each failing check, capture the offending element, named exactly.
3. Decide the result: pass only when every check passes, otherwise fail. A spec-only review
   blocks final pass on the checks that need a render (measured contrast, focus order).
4. Return the result in the shape below. Never edit the asset.

## Output

- Pass: the asset advances to `brand-qa-reviewer` (alongside `compliance-privacy-check` where
  data is collected), then the human gate.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, element: "<the offending element, named exactly>", fix: "<the required change>" }
```

Example: `{ check: "contrast-aa", element: "plan benefit paragraph, #009975 on #1A1A1A", fix: "set the paragraph to #FFFFFF, keep emerald for the heading and the CTA" }`.

See `templates/accessibility-qa-fix-list.md`.

## Hard rules

- Never edit the asset. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- Never weaken the brand palette or bake Arabic into an image to "fix" accessibility. Fix the
  usage, or escalate to `brand-qa-reviewer` and the human gate.
- A spec-only review blocks on the checks that need a render: measured contrast and focus order.
- WCAG 2.2 AA is the bar. Passing accessibility is not approval to send.
- No em dashes, no tatweel, Western numerals only, in this file and the fix list.

## How it connects

- Runs in the gate stack alongside `design-qa` and before `brand-qa-reviewer` for
  customer-facing pages and emails, per `runtime/verification.md`. On pass, the asset advances,
  on fail it returns to the author (conversion-engineer for pages, lifecycle-architect for
  emails, designer for the visual) with the fix list.
- Owned by the `accessibility-reviewer` agent.

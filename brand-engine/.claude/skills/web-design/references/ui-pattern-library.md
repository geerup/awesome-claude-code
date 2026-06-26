# Reusable UI patterns (distilled, brand-bound)

A supplement to `web-design-spec`, not a replacement. It supplies the concrete defaults the spec
references abstractly: touch ergonomics, motion, the full set of states, and form UX. The
web-designer pulls numbers from here so specs stay consistent.

## Provenance and status

- Distilled and reconciled from an external MIT-licensed prompt collection
  (claude-code-ui-agents by Mustafa Kendiguzel, 2025). Only generic, framework-neutral patterns
  were kept and then rebound to Maharat. The raw prompts were not adopted.
- Subordinate to `context/brand-voice.md`, `web-design-qa`, and `accessibility-qa`. On any
  conflict, brand-voice and the gates win.
- English-first, RTL, Western numerals only (0 to 9), no em dashes, no tatweel. Premium and
  uncluttered.

## Token discipline (the palette is fixed, never invented)

- Design tokens are semantic aliases over the fixed brand palette, never a new palette:
  - `--bg`: #141414 (near-black background)
  - `--surface`: #1A1A1A (card surfaces)
  - `--accent`: #009975 (emerald, a highlight, not a flood)
  - neutral text and border grays derived only to meet contrast.
- Define tokens once. No ad hoc inline colors in components. Prefer component variants over
  one-off overrides, so the surface stays consistent.
- Do not generate a palette from color psychology or brand personality. The palette is a brand
  constant. This is the main thing rejected from the source material.

## RTL by construction (not bolted on)

- Use logical CSS properties so layout mirrors automatically: `margin-inline-start` and
  `-end`, `padding-inline-*`, `inset-inline-*`, `text-align: start` and `end`. Avoid hard
  `left` and `right`.
- Mirror directional icons (arrows, chevrons, progress, back) under `direction: rtl`. Do not
  mirror logos, media play icons, or numerals.
- Verify RTL at every breakpoint, including mixed Arabic, English, and numerals in one line.

## Touch ergonomics (mobile)

- Minimum touch target 44 by 44 px (48 on Android). Keep at least 8 px between adjacent targets.
- Give visual touch feedback within 100 ms of contact.
- Place the single primary action within thumb reach on mobile. In RTL, the thumb-reach and
  back-gesture sides mirror.

## Motion discipline

- Micro-interactions under 300 ms. Animate `transform` and `opacity` only, avoid animating
  layout properties (width, height, top, left).
- Target 60 fps. Always honor `prefers-reduced-motion: reduce` with a static or minimal
  fallback.
- Motion clarifies a state change, it does not decorate.

## State coverage (extends the spec's interaction states)

- Element states: default, hover, focus (always visibly), active, disabled, loading.
- View states: also design empty, skeleton-loading, and error-with-recovery. A view is not done
  until its empty and error states are designed, not just its happy path.

## Form UX

- Single column. One idea per row.
- Inline validation with a clear, empowering message, never deficit-framed, and never color
  alone: pair it with text or an icon so it does not depend on sight of color.
- Input font size at least 16 px to prevent automatic zoom on mobile Safari.
- Correct input types and keyboards, smart defaults, a label on every field. The signup gate
  still binds its copy by `copy-package` variant id, never free text typed here.

## Deliberately not imported

- The source's color-psychology palette generation (conflicts with the fixed brand palette).
- Stack-specific assumptions (React, Tailwind, cva, styled-components). Those stay
  implementation choices for `conversion-engineer`, not design rules.
- The persona generator (audience work belongs to `strategy-lead`, not web design).

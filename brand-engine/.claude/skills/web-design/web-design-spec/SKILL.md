---
name: web-design-spec
description: Produce the build-ready responsive web design spec for stream 6. Use when web-design-director direction needs to become a build-ready spec, component inventory, responsive grid and breakpoints, type scale, design tokens, interaction states, RTL behavior per breakpoint, accessibility, and a performance budget, with each copy region bound to a QA-passed copy variant id. Triggers on "responsive design spec," "design tokens," "the page design system," "wireframe to spec," "build the web design." Sub-skill of web-design, owned by web-designer.
---

# Web Design Spec (web-design sub-skill)

Produces the build-ready `design_spec` of the `web-design-package` from the web-design-director's
direction. Responsive, RTL-correct, on brand, with one primary action per view. It does not
write copy: every copy region binds to a QA-passed `copy-package` variant id. It does not build
or wire the live page, that is `conversion-engineer` behind the human gate.

Owner: web-designer. Mode: reasoning. Aligns with `sops/06-conversion-path.md`.

## When to use

- The direction half of the `web-design-package` is ready and the page needs a build-ready spec
  before any implementation.

## Inputs

- The direction half of the `web-design-package`: information architecture, UX flow, wireframes,
  visual direction, web asset brief.
- The QA-passed `copy-package` variant ids that bind to each region.
- `context/brand-voice.md`: the visual constants and the premium, uncluttered, RTL bar.
- `skills/web-design/references/ui-pattern-library.md`: brand-bound defaults for touch targets,
  motion, the full set of element and view states, and form UX that this spec applies.

If the direction is not qa-passed, stop. The spec does not invent direction to fill a gap.

## Steps

1. Validate the web-design-package direction envelope: right campaign_id, status at least
   qa-passed, information architecture and wireframes present. If incomplete, return it.
2. Build the component inventory from the wireframes, with one primary action per view.
3. Set the responsive system: a grid, named breakpoints (mobile first), a type scale, and design
   tokens for color (#141414 background, #1A1A1A surfaces, emerald #009975 accent), spacing, and
   radius. The accent is a highlight, not a flood.
4. Specify RTL behavior at every breakpoint: direction rtl, Arabic primary, mixed Arabic,
   English, or numerals do not break direction, alignment, or reading order at any width.
5. Specify interaction states (default, hover, focus, active, disabled, loading, error) and
   accessibility: contrast, focus order, semantic structure, touch target sizes, alt text slots.
6. Set a performance budget: fast first render, minimal blocking assets, image weight noted, the
   primary action visible without a scroll on mobile.
7. Bind each copy region to a QA-passed `copy-package` variant id. Never type the words here.
8. Run `web-design-qa` on the spec, then hand the spec and verdict to `brand-qa-reviewer`, then
   route the approved design to `conversion-engineer`.

## Output

The `design_spec` field of the `web-design-package`:

```
components     component inventory, one primary action per view
grid           responsive grid, named breakpoints (mobile first)
type_scale     the type scale
tokens         color (#141414, #1A1A1A, #009975), spacing, radius
states         default, hover, focus, active, disabled, loading, error
rtl            direction rtl per breakpoint, Arabic primary, Western numerals, mixed handling
accessibility  contrast, focus order, semantic structure, touch targets, alt text slots
performance    render budget, blocking assets, image weight, mobile primary-action placement
copy_refs      each region bound to a copy-package variant id (no free text)
```

See `templates/web-design-spec.md`.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and the mechanical rules.
- `web-design-qa` on the spec, then `brand-qa-reviewer`, per `runtime/verification.md`. A fail
  returns to the author with exact fixes. A human design check stays on any Arabic surface.

## Hard rules

- One primary action per view. Copy comes from the QA-passed copy-package by id, never invented.
- No Arabic text baked into a generated image. RTL renders correctly at every breakpoint.
- Visual constants #141414, #1A1A1A, emerald #009975. Western numerals. No em dashes, no tatweel.
- Never put personal or sensitive data in URL parameters or tracking in the spec.
- Never imply certificates are accredited. Never invent a Skill Path title, instructor name,
  offer, or price.

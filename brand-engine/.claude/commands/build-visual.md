---
description: Produce a visual or asset set in your brand identity, via creative-director -> designer (Canva) -> design-qa. Usage - /build-visual <what, e.g. "a LinkedIn banner" or "4 Substack post images">
allowed-tools: Read, Write, Edit, Glob, Grep
---

# /build-visual

Produce on-brand visuals. Reasoning agents brief and direct; Canva executes; the design gate checks.

## What to do

1. Load `context/brand-voice.md` (your visual constants from `brand-identity`) and the active
   brief if one applies. If the visual identity is still TODO, run `brand-identity` first.
2. `creative-director` sets the concept and a text-free image brief (no copy baked into the
   image; copy overlays bind to QA-passed copy later).
3. `designer` executes in Canva (generate-design or a brand template), then exports. Use brand
   kits and templates where they exist.
4. Run `design-qa`: brand visual constants, dimensions and safe areas, no text baked into a
   generated image (unless a deliberate typeset asset), premium and uncluttered. A fail returns
   to the designer with exact fixes.
5. Stop at the human gate (you) with the asset and the QA verdict. Nothing is published.

## Rules
- No generated likeness of a real person passed off as a real photo. Real assets for real people.
- Visuals carry your brand constants, not Maharat's. If unset, stop and run `brand-identity`.
- No em dashes in any typeset copy.

$ARGUMENTS

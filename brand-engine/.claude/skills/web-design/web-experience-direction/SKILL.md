---
name: web-experience-direction
description: Set the web design direction for stream 6. Use when a campaign needs the information architecture, the UX flow from click to signup gate, the wireframe-level page structure with one primary action per view, the visual direction, and a text-free web asset brief, before anything is built. Triggers on "web design direction," "information architecture," "the page UX flow," "wireframe the page," "structure the landing page." Sub-skill of web-design, owned by web-design-director.
---

# Web Experience Direction (web-design sub-skill)

Produces the direction half of the `web-design-package`: the information architecture, the UX
flow, the wireframes, the visual direction, and the web asset brief. It does not write copy and
does not produce the build-ready spec. Every section earns its place against the conversion the
strategy names.

Owner: web-design-director. Mode: reasoning. Aligns with `sops/06-conversion-path.md`.

## When to use

- The brief lands traffic on a page, or lifecycle messages point to one, and the page needs a
  direction before the build-ready spec.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing, the conversion.
- The active `briefs/` file: offer, gate type (email or WhatsApp), any page direction.
- The `creative-package` asset refs, when the page carries art.
- `context/brand-voice.md`: voice, the visual constants, the hard mechanical rules.

If the strategy-artifact is not qa-passed, stop. The direction does not invent a strategy to
fill a gap.

## Steps

1. Validate the strategy-artifact envelope: right campaign_id, status at least qa-passed, the
   conversion present. If incomplete, return it.
2. Set the information architecture: the pages and sections the offer needs, in order, each with
   a one-line job. Cut anything that does not move the conversion.
3. Map the UX flow: ad or organic click -> page -> signup gate -> lifecycle, naming the key
   states (first view, gate open, submitted, confirmed, error).
4. Wireframe each page at the region level in reading order, with exactly one primary action per
   view. No visuals yet.
5. Write the visual direction (how the brand constants apply to the web surface) and a text-free
   web asset brief: imagery direction, dimensions, safe areas, and named copy-overlay slots
   labeled by language (ar / en), left empty.
6. Hand the direction to `web-designer` and to `brand-qa-reviewer`, route copy slots to the
   copywriters.

## Output

The direction fields of the `web-design-package`:

```
information_architecture   pages and sections, order, the job of each
ux_flow                    the path click -> gate -> lifecycle, with key states named
wireframe                  region-level structure per page, one primary action per view
visual_direction           brand constants applied to the web, text-free imagery direction
web_asset_brief            imagery needs, dimensions, safe areas, copy-overlay slots (empty, ar/en)
conversion_intent          the single primary action the page optimizes toward
```

See `templates/web-experience-direction.md`.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure and the mechanical rules.
- `brand-qa-reviewer` on the direction, per `runtime/verification.md`. A fail returns exact fixes.

## Hard rules

- One primary action per view, not two competing CTAs.
- Do not write copy. Copy slots are labeled by language and left empty for stream 4.
- Do not bake Arabic into a planned image. Text-free imagery only.
- RTL reading order. Western numerals. No em dashes, no tatweel.
- Never imply certificates are accredited. Never invent a Skill Path title, instructor name,
  offer, or price.

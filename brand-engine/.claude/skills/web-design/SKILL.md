---
name: web-design
description: Hub for web design, owned by web-design-director plus web-designer, the stream-6 design layer that turns an approved strategy into the web surface conversion-engineer builds. Use when a campaign needs the information architecture, UX flow, and a build-ready responsive design spec for a landing page or web surface. Triggers on "web design," "design the landing page experience," "the page UX flow," "information architecture," "responsive design spec," "design tokens," "the page design system." Routes to web-experience-direction and web-design-spec and produces the web-design-package. The web-designer runs web-design-qa. Never bake Arabic text into generated imagery, the copy regions bind to QA-passed copy variant ids filled by copywriter-ar or copywriter-en.
---

# Web Design (stream 6 design layer hub)

The entry point for the design of a web surface before it is built. Owned by
`web-design-director` (direction) plus `web-designer` (the build-ready spec and the visual
gate), reasoning mode. This hub turns a `strategy-artifact` (segment, angle, offer framing, the
conversion) into the `web-design-package` defined in `runtime/handoff-contract.md`, which
`conversion-engineer` then implements and wires in stream 6.

This is the design layer, not the build. The division mirrors stream 3 creative: the
web-design-director and web-designer design the page, conversion-engineer builds and wires it,
the copywriters write the words, and nothing publishes until the human gate clears.

## What it routes to

- `web-experience-direction`: the information architecture, the UX flow from click to signup
  gate to lifecycle, the wireframe-level structure with one primary action per view, the visual
  direction, and the text-free web asset brief with empty copy-overlay slots. Owned by
  `web-design-director`. Fills `information_architecture`, `ux_flow`, `wireframe`,
  `visual_direction`, `web_asset_brief`, and `conversion_intent`.
- `web-design-spec`: the build-ready responsive spec, component inventory, grid and breakpoints,
  type scale, design tokens, interaction states, RTL behavior per breakpoint, accessibility, a
  performance budget, and each copy region bound to a QA-passed copy variant id. Owned by
  `web-designer`. Fills `design_spec`.

The orchestrator runs `web-experience-direction` first to set direction, then `web-design-spec`
to make it build-ready. The hub assembles both into the `web-design-package`.

## Execution and the visual gate

The web-design-director owns the architecture and the direction. The web-designer builds the
spec from it, binds copy regions to QA-passed variant ids, and runs `web-design-qa` on the
spec. Arabic text is never baked into a generated image: generative tools mangle Arabic and add
tatweel, so any Arabic arrives as real text bound by id and authored in stream 4 by
`copywriter-ar`, gated there by `arabic-copy-qa`. A human design check stays on any surface that
carries Arabic.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing, channel_plan, the conversion.
- The active `briefs/` file: offer, gate type, page direction, only as the brief provides them.
- The `creative-package` asset refs, when the page carries art.
- `context/brand-voice.md`: voice and the visual constants (#141414, #1A1A1A, accent #009975).

## Output: the web-design-package

The body shape, as `runtime/handoff-contract.md` defines it:

```
information_architecture   pages and sections, order, the job of each
ux_flow                    click -> page -> signup gate -> lifecycle, the path and key states
wireframe                  region-level structure per page, one primary action per view
visual_direction           how the brand constants apply to the web surface (text-free imagery)
web_asset_brief            imagery needs, dimensions, safe areas, copy-overlay slots (empty, ar/en)
conversion_intent          the single primary action the page optimizes toward
design_spec                components, grid, breakpoints, type scale, tokens, states, RTL, a11y,
                           performance budget, copy region -> variant id binding
web_design_qa              the web-designer's verdict: pass | fail with a fix-list
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs).

## How it connects

- Consumes: `strategy-artifact` (stream 2), `creative-package` art refs (stream 3), QA-passed
  `copy-package` variant ids (stream 4).
- Produces: `web-design-package` (stream 6), consumed by `conversion-engineer` for the page.
- Gate before advance: each sub-skill's skill eval, then `web-design-qa` on the spec, then
  `brand-qa-reviewer`; `arabic-copy-qa` applies to the bound copy in stream 4, not here;
  `compliance-privacy-check` runs at the page and gate in `conversion-engineer` because the
  surface collects data. A fail is a hard stop that returns exact fixes, per
  `runtime/verification.md`.

## Hard rules

- Do not write the page copy. Copy regions bind to QA-passed `copy-package` variant ids.
- Do not bake Arabic text into generated imagery. Leave copy-overlay slots empty for stream 4.
- One primary action per view. Never put personal or sensitive data in URL parameters or tracking.
- Generative or build tool choice runs through `build-vs-buy-eval`: Arabic capability is the
  decisive filter, and no tool is adopted without approval. Keep a human design check on any Arabic.
- Do not invent Skill Path titles or name instructors. Never imply certificates are accredited.
- No em dashes, no tatweel, Western numerals only. Empowering, never deficit-framed.

---
name: 03-creative-production
description: Hub for stream 3 creative production, owned by creative-director plus designer. Use when a campaign needs visual concepts and text-free image or video prompts from the strategy-artifact, triggers on "creative concept," "image prompt," "asset brief," "visuals for the campaign." Routes to creative-concepting and image-prompting and produces the creative-package. The designer executes visuals and runs design-qa. Default copy is English; copy-overlay slots are filled later by copywriter-en, or by copywriter-ar only when a brief sets Arabic in scope. Never bake Arabic text into generated images.
---

# 03 Creative Production (stream 3 hub)

The entry point for visual concepts and the prompts that generate them. Owned by
`creative-director`, reasoning mode. This hub turns a `strategy-artifact` (segment, angle,
offer framing) into the `creative-package` defined in `runtime/handoff-contract.md`.

## What it routes to

- `creative-concepting`: 2 to 4 concept directions per strategy angle, each with a one-line
  rationale tied to the angle and a channel routing (paid, lifecycle, or organic). Fills
  `concepts[]` and `channel_routing`.
- `image-prompting`: text-free English image or video prompts with dimensions, safe areas, and
  empty copy-overlay slots. No Arabic baked into the image. The copy overlays are filled later
  by `copywriter-en` in stream 4, or by `copywriter-ar` when a brief sets Arabic in scope. Fills
  `prompts[]` and `asset_briefs[]`.

The orchestrator runs `creative-concepting` first to set direction, then `image-prompting` to
make the concepts generation-ready. The hub assembles both into the `creative-package`.

## Execution and visual QA

The creative-director owns the concept and the prompts. The designer executes the visuals from
the prompts, overlays human-written copy into the empty slots, and runs `design-qa` on the
rendered asset. Arabic text is never baked into a generated image: when Arabic is in scope,
generative tools mangle Arabic and add tatweel, so any Arabic arrives as a human-placed overlay
and is gated in stream 4 by `arabic-copy-qa`. A human design check stays on any asset that
carries Arabic.

## Inputs

- The `strategy-artifact`: segments, angle, offer_framing, channel_plan.
- `context/brand-voice.md`: voice and the active profile visual constants.
- The active `briefs/` file: creative direction, only as the brief provides it.

## Output: the creative-package

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
concepts[]        each: id, description, rationale tied to angle
prompts[]         image or video prompts, text-free (no AR baked in)
asset_briefs[]    dimensions, safe areas, copy-overlay slots (empty, for copywriter-en)
channel_routing   which concept goes to paid vs lifecycle
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs).

## How it connects

- Consumes: `strategy-artifact` (stream 2).
- Produces: `creative-package` (stream 3 -> 4, 5).
- Gate before advance: each sub-skill's skill eval, then `design-qa` on the executed visual,
  then `brand-qa-reviewer`; `arabic-copy-qa` only if Arabic text is present (per
  `runtime/verification.md`). `compliance-privacy-check` runs if a post collects data. Generated
  images carry no baked Arabic, so any Arabic appears later as copy overlay from stream 4 and is
  gated there. A fail is a hard stop that returns exact fixes.

## Hard rules

- Do not bake Arabic text into generated images. Leave copy-overlay slots empty for stream 4.
- Generative tool choice runs through `build-vs-buy-eval`: capability for your use case is the
  decisive filter, and no tool is adopted without approval. Keep a human design check on any Arabic.
- Do not invent offer titles or name a subject (context/subjects/) you do not have. Empowering,
  never deficit-framed.
- No em dashes, no tatweel, Western numerals only.

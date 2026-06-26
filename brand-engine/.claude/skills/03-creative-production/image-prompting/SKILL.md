---
name: image-prompting
description: Write text-free English image and video prompts for stream 3 from approved creative concepts. Use when concepts are set and a campaign needs generation-ready prompts that bake in no Arabic, specify dimensions and safe areas, and leave copy-overlay slots empty for the copywriter to fill. Triggers on "image prompt," "video prompt," "prompt sheet," "asset brief," "generate the visuals." Sub-skill of 03-creative-production, owned by creative-director.
---

# Image Prompting (stream 3 sub-skill)

Turns approved concepts into generation-ready prompts that fill the `prompts[]` and
`asset_briefs[]` fields of the `creative-package`. Prompts are written in English and produce
text-free images. No Arabic is ever baked into a generated image: generative tools mangle
Arabic and add tatweel. All copy lands later as overlay from `copywriter-ar` or `copywriter-en`
into the empty slots this skill defines.

Owner: creative-director. The designer executes the visuals and runs `design-qa`. Mode: reasoning.

## When to use

- Concepts from `creative-concepting` are set and you need generation-ready prompts.
- A build needs asset briefs with dimensions, safe areas, and copy-overlay slots.

## Inputs

- The `concepts[]` and `channel_routing` from `creative-concepting`.
- `context/brand-voice.md`: voice and visual constants (#141414, #1A1A1A, accent #009975).
- The active `briefs/` file: channel and placement specs, only as the brief provides them.

If a concept is missing or not approved, stop and return it. Do not invent a concept or a
dimension the brief does not give.

## Steps

1. For each concept, write an English prompt that describes a text-free image or video. Name
   subject, mood, light, composition, and the visual constants. State the image is text-free.
2. Specify dimensions per placement (for example a square feed asset and a vertical story
   asset) and the safe areas where no critical subject sits.
3. Define copy-overlay slots and leave them empty. Each slot is a named region (headline,
   subhead, CTA) bound later to a copy-package variant id. The prompt itself carries no text.
4. Add a negative instruction to the prompt: no text, no lettering, no Arabic script, no
   watermark. This keeps tatweel and mangled glyphs out of the generated frame.
5. Note that the designer executes the generation, overlays human-written copy, and runs
   `design-qa`. Flag the human design check on any asset that will carry Arabic.
6. Hand the prompts and asset briefs to the hub for assembly into the `creative-package`.

## Output

Fills the `prompts[]` and `asset_briefs[]` fields of the `creative-package` (see
`runtime/handoff-contract.md`):

```
prompts[]         image or video prompts, English, text-free (no AR baked in)
asset_briefs[]    dimensions, safe areas, copy-overlay slots (empty, for copywriter-ar)
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See the template in `templates/image-prompt-sheet.md`.

## How it connects to the verification gates

- Skill eval (this file's `evals/evals.json`) for structure, text-free prompts, and empty slots.
- `design-qa` on the executed visual: RTL, visual constants, no baked Arabic, safe areas,
  dimensions, premium and uncluttered, plus a human design check.
- `brand-qa-reviewer` on the asset. `arabic-copy-qa` runs on the overlay copy in stream 4, not
  on the image. A failing gate is a hard stop that returns exact fixes.
- Generative tool choice runs through `build-vs-buy-eval`. Arabic capability is the decisive
  filter and no tool is adopted without approval.

## Hard rules

- Never bake Arabic text into a generated image. Prompts are text-free and carry a no-text,
  no-Arabic-script negative instruction. Copy-overlay slots stay empty for stream 4.
- Every prompt specifies dimensions and safe areas. The designer runs `design-qa` and keeps a
  human design check on any Arabic.
- Do not invent dimensions, placements, Skill Path titles, instructor names, offers, or prices.
  Missing means stop and ask.
- Empowering, never deficit-framed. Never imply certificates are accredited.
- No em dashes, no tatweel, Western numerals only.

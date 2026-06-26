# SOP 03: Creative production

Stream 3. Owners: creative-director (concept) and designer (execution and design-qa). Mode:
reasoning. Turns the strategy-artifact into visual concepts, text-free image and video
prompts, and asset briefs with empty copy-overlay slots. The creative-director sets the
concepts and rationale; the designer executes and runs design-qa; a human design check
follows. No Arabic text is ever baked into a generated image. The copy-overlay slots are
filled later by copywriter-ar in stream 4.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Trigger

A campaign that needs visual assets, with a QA-passed `strategy-artifact` from stream 2. For
the owned-audience lapsed-contact flow, this runs only if the emails need visual assets.

## Inputs

- The `strategy-artifact` (stream 2): segments, angle, offer framing, channel plan.
- The brief: creative direction if any, assets available to reuse, channels and placements.
- `context/brand-voice.md` for the visual constants and guardrails.

## Steps

1. Concept. The creative-director proposes a small set of concepts. Each concept has an id, a
   description, and a rationale tied directly to the angle from the strategy-artifact. No
   concept relies on an invented offer title, subject name, or offer detail.
2. Write text-free prompts. Produce image or video prompts that carry no baked-in text, and
   no Arabic at all. The visual must leave room for copy to be overlaid later. Prompts respect
   the visual constants: near-black #141414, card surfaces #1A1A1A, emerald accent #009975,
   premium and uncluttered.
3. Build asset briefs. For each placement, specify dimensions, safe areas, and copy-overlay
   slots left empty for copywriter-ar. State which concept and which channel each brief serves.
4. Route by channel. Map each concept to paid versus lifecycle use, consistent with the
   strategy-artifact channel plan.
5. Designer executes. The designer produces the assets from the prompts and briefs, keeping
   the overlay slots empty, then runs design-qa: dimensions correct, safe areas respected, RTL
   layout space reserved for Arabic overlay, visual constants honored, no text baked in.
6. Human design check. After design-qa passes, a human reviews the executed creative before it
   advances. A failing design-qa is a hard stop back to the designer with exact fixes.
7. Assemble the creative-package. Carry forward open items from upstream.

## Output

A `creative-package` (see `runtime/handoff-contract.md`):
- concepts[]: each with id, description, rationale tied to the angle.
- prompts[]: image or video prompts, text-free, no Arabic baked in.
- asset_briefs[]: dimensions, safe areas, copy-overlay slots (empty, for copywriter-ar).
- channel_routing: which concept goes to paid versus lifecycle.

This artifact hands off to streams 4 and 5.

## Quality bar

- Every concept rationale traces to the strategy-artifact angle. No invented title, subject,
  or offer detail in any concept or prompt.
- Prompts are text-free and carry no Arabic. Copy-overlay slots are present and empty.
- Visual constants honored: #141414, #1A1A1A, emerald #009975. Premium, uncluttered. RTL
  overlay space reserved.
- Gates (see `verification.md`): skill eval, then design-qa, then brand-qa. arabic-copy-qa or
  english-copy-qa run only if copy is present in the asset; concepts and prompts carry no copy,
  so those run once the stream 4 overlay copy is placed, not here.

## Example output (shape, not real copy, no invented values)

```
creative-package:
  concepts:
    - id: concept-01
      description: "[single uncluttered hero, emerald accent, space reserved for overlay]"
      rationale: "[why this serves the angle from the strategy-artifact]"
  prompts:
    - for: concept-01
      type: image
      prompt: "[text-free scene description, no Arabic, brand colors, clear overlay area]"
  asset_briefs:
    - placement: "[channel and size]"
      dimensions: "[w x h]"
      safe_areas: "[where overlay text and logo sit]"
      copy_overlay_slots: { headline: "", subhead: "", cta: "" }
  channel_routing: { concept-01: paid, concept-02: lifecycle }
  open_items: [carried from strategy-artifact]
```

## Review owner

creative-director owns the concepts; designer owns execution and the design-qa pass. After
design-qa and brand-qa pass, a human performs the design check before the package advances.
No invented value enters a concept, a prompt, or an asset brief.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.

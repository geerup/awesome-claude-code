---
name: creative-concepting
description: Generate visual creative concepts for stream 3 from the strategy-artifact angle. Use when a campaign needs concept directions before any image prompt or build, each concept a one-line rationale tied to a strategy angle and routed to paid, lifecycle, or organic. Triggers on "creative concept," "concept the campaign," "what should the creative say," "concept directions." Sub-skill of 03-creative-production, owned by creative-director.
---

# Creative Concepting (stream 3 sub-skill)

Turns a QA-passed `strategy-artifact` into a small set of concept directions that fill the
`concepts[]` field of the `creative-package`. Each concept is a visual direction with a
one-line rationale that traces back to a specific angle from the strategy. It does not write
final copy and does not generate images. It sets the direction those steps execute against.

Owner: creative-director. Mode: reasoning.

## When to use

- A paid, organic, or lifecycle build needs visual direction before prompts and copy.
- You have a QA-passed `strategy-artifact` with an angle and segments.
- You need approval-ready concept directions, not finished art.

## Inputs

- The QA-passed `strategy-artifact`: segments, angle, offer_framing, channel_plan.
- `context/brand-voice.md`: voice, visual constants (#141414, #1A1A1A, accent #009975).
- The active `briefs/` file: creative direction, only as the brief provides it.

If the strategy-artifact is not qa-passed or carries no angle, stop and return it. Do not
invent an angle, a segment, or a Skill Path title to fill the gap.

## Steps

1. Validate the strategy-artifact envelope: right campaign_id, status at least qa-passed,
   angle and segments present. If incomplete, return it.
2. For each angle in the strategy, produce 2 to 4 concept directions. Fewer than 2 gives the
   human gate no choice, more than 4 dilutes the review.
3. Write each concept as: id, a short visual description, and a one-line rationale that names
   the angle it serves and why it fits the segment.
4. Set channel_routing per concept: paid, lifecycle, or organic, matching the channel_plan in
   the strategy. A concept built for a paid feed is not silently reused for lifecycle.
5. Keep every concept empowering, never deficit-framed. Speak to what the reader can become.
6. Hand the concepts to the hub, which assembles them into the `creative-package` and routes
   to `image-prompting`.

## Output

Fills the `concepts[]` and `channel_routing` fields of the `creative-package` (see
`runtime/handoff-contract.md`):

```
concepts[]        each: id, description, rationale tied to angle
channel_routing   which concept goes to paid vs lifecycle vs organic
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See the template in `templates/creative-concept-brief.md`.

## How it connects to the verification gates

- Skill eval (this file's `evals/evals.json`) for structure, concept count, and the angle tie.
- `brand-qa-reviewer` on the concept directions, per `runtime/verification.md`.
- `arabic-copy-qa` runs only if a concept carries Arabic text. Concepts should describe
  direction, not finished Arabic copy; final Arabic arrives later from `copywriter-ar` and is
  gated in stream 4. A failing gate is a hard stop that returns exact fixes.

## Hard rules

- Each concept carries a one-line rationale that names the strategy angle it serves.
- 2 to 4 concepts per angle. Not 1, not a flood.
- Do not invent Skill Path titles, instructor names, offers, or prices. Missing means stop
  and ask, not guess.
- Empowering, never deficit-framed. Never imply certificates are accredited.
- No em dashes, no tatweel, Western numerals only.

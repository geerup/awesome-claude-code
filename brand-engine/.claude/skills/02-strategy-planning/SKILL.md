---
name: 02-strategy-planning
description: Hub for stream 2 strategy and planning, owned by strategy-lead. Use after brief intake to turn a validated, scoped brief into the strategy-artifact the rest of the funnel builds on. Routes to audience-segmentation (segment the owned audience and other audiences from data) and offer-and-angle (set the core angle and frame the offer). Triggers on "what is the strategy," "segment the audience," "what angle should we take," "frame the offer," "plan the campaign," "set the success metric."
---

# 02 Strategy and Planning (hub)

Stream 2. Takes the validated brief and the kickoff scope from stream 1 and produces the
`strategy-artifact` defined in `runtime/handoff-contract.md`. This is the document the rest
of the funnel builds on. Internal reasoning work, not customer-facing.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact, no
arabic-copy-qa or brand-qa unless customer copy appears).

## When to use

After stream 1 (`01-brief-intake`) returns a validated brief and a kickoff scope. Run this
to decide who we are talking to, what the angle is, how the offer is framed, which streams
run, and what success looks like. If the brief changes, revalidate and replan.

## Sub-skills (routing)

- `audience-segmentation`: cuts the campaign audience into segments from the data. For the
  owned-audience flow, segments the owned contacts who have not yet converted (recency, prior
  interest, engagement state). Use when you need the `segments[]` field. It never invents segment
  sizes, it uses the context planning estimates and flags where live data is needed.
- `offer-and-angle`: sets the core angle (the message and why it works) and frames the
  offer (how the brief's offer is positioned). Use when you need the `angle` and
  `offer_framing` fields. Price is shown only if the brief provides it and the asset calls
  for it.

Route: run `audience-segmentation` first so the angle is built for real segments, then
`offer-and-angle`. The hub then assembles both into one strategy-artifact and adds the
channel_plan (from the kickoff scope entry point) and the success_metric (from the brief).

## Inputs

- The brief validation report and kickoff scope from stream 1.
- The active `briefs/` file: objective, offer, price, promotion, success_metric, channels.
- `context/01-brand-brief.md`: stable audience and money-model facts.
- `context/brand-voice.md`: the empowering voice and the hard mechanical rules.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the
gap with an invented value.

## Steps

1. Validate the stream 1 inputs: the brief is validated, the scope names the entry point and
   active streams, the open items are read. If the brief is blocked on a stop-and-ask field
   the strategy needs, stop and ask.
2. Run `audience-segmentation` to produce `segments[]`.
3. Run `offer-and-angle` to produce `angle` and `offer_framing`.
4. Build `channel_plan`: which streams this campaign uses and the entry point (paid or
   owned), carried from the kickoff scope.
5. Set `success_metric`: the single thing stream 8 will measure against, read from the
   brief. If the brief leaves the target as an ASSUMPTION, carry it as an open item, do not
   invent a number.
6. Assemble the strategy-artifact body and wrap it in the common envelope. Run this skill
   eval for structure and completeness.
7. On pass, set status to qa-passed and hand the strategy-artifact to streams 3, 4, and 7.

## Output: the strategy-artifact

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
segments[]        each: name, size, definition, why
angle             the core message and its rationale
offer_framing     how the brief's offer is positioned (not the price itself unless shown)
channel_plan      which streams this campaign uses, and entry point (paid | owned)
success_metric    what stream 8 will measure against
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See `templates/` in each sub-skill for the per-field shape.

## How this connects to the contract and gates

- Consumes: the stream 1 validation report and kickoff scope.
- Produces: the `strategy-artifact` (stream 2 -> 3, 4, 7).
- Verification: per `runtime/verification.md`, stream 2 is internal, so it runs this skill
  eval for structure and completeness only. No brand or Arabic gate applies unless a field
  carries customer-facing copy.

## Hard rules

- Never invent an offer, price, target, segment size, or success-metric number. A missing
  variable the campaign needs is a stop-and-ask.
- Empowering framing, never deficit-framed. English-first for any drafted customer text.
- No em dashes, no tatweel, Western numerals only, never imply a credential or accreditation
  you do not hold, no invented offers or subject names.

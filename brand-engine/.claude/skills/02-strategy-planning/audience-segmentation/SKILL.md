---
name: audience-segmentation
description: Segments the campaign audience into named segments from the data, for the owned-audience flow the roughly 18,000 non-payers by recency, prior interest, and engagement state. Use when stream 2 needs the segments[] field of the strategy-artifact. Triggers on "segment the audience," "who are the non-payers," "cut the audience," "which segments," "audience segmentation." Never invents segment sizes, uses the context planning estimates and flags where live data is needed.
---

# Audience Segmentation (sub-skill of 02-strategy-planning)

Cuts the campaign audience into a small set of named, defined segments so the angle and the
copy are built for real people, not an average. Produces the `segments[]` field of the
strategy-artifact. Internal reasoning work.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact).

## Purpose

Give the rest of the funnel a clear answer to who we are talking to, in segments specific
enough to angle and target against, sized only with figures we actually have.

## When to use

- Stream 2 needs `segments[]` for the strategy-artifact.
- The owned-audience flow needs the roughly 18,000 non-payers cut into workable segments.
- A paid campaign needs its target audiences named before creative and copy.

## Inputs

- The active `briefs/` file: the audience and any segment cuts the brief names.
- `context/01-brand-brief.md`: the owned-audience planning estimates (about 23,000
  contacts, about 18,000 non-paying, about 5,000 paying, about 180,000 social followers).
- The kickoff scope: the entry point, which tells you whether segments are owned or acquired.

## Steps

1. Read the audience from the brief and the planning estimates from context. Do not treat a
   context estimate as a confirmed send size.
2. Choose the segmentation axes that matter for this campaign. For the non-payer flow,
   typical cuts are engagement state (never-engaged vs lapsed-engaged), prior interest
   (single-class interest vs none), and recency of last open.
3. Define each segment plainly: a name, what defines membership, and why it matters for the
   angle and the offer.
4. Size each segment only from data we have. If a size is a planning estimate, mark it as an
   estimate. If a size needs live data, write "resolved from live data at send time" and
   flag it. Never invent a segment size.
5. Keep the set small and workable. Prefer three to five segments over a long list nobody
   can act on.
6. Record the result in the segmentation plan template, with the open items where live data
   is needed.

## Output

The `segments[]` field, each segment:

```
name        short, human, e.g. lapsed-engaged-nonpayers
size        a figure traceable to data, or "estimate" or "resolved from live data at send time"
definition  what defines membership in plain words
why         why this segment matters for the angle and the offer
```

See `templates/segmentation-plan.md`.

## How this connects to the contract and gates

- Handoff: feeds the `segments[]` field of the strategy-artifact assembled by the 02 hub.
  Live-data open items map to the `open_items` of the common envelope in
  `runtime/handoff-contract.md`, and the resolved size is recorded later in the
  lifecycle-package at send time.
- Verification: internal artifact, skill eval only, per `runtime/verification.md`.

## Hard rules

- Never invent a segment size. Use the context estimate marked as an estimate, or flag that
  the size resolves from live data at send time.
- Empowering framing, never deficit-framed. A non-payer is someone ready to grow, not a
  failure to be fixed.
- No em dashes, no tatweel, Western numerals only, no accreditation claims.

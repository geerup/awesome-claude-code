---
name: offer-and-angle
description: Sets the core angle for a campaign (the central message and why it works for this audience and offer) and frames the brief's offer for positioning. Use when stream 2 needs the angle and offer_framing fields of the strategy-artifact. Triggers on "what angle should we take," "what is the message," "frame the offer," "position the offer," "angle and offer." Price is shown only if the brief provides it and the asset calls for it, never invented.
---

# Offer and Angle (sub-skill of 02-strategy-planning)

Sets the one idea the whole campaign turns on (the angle) and frames how the brief's offer
is positioned (the offer framing). Produces the `angle` and `offer_framing` fields of the
strategy-artifact. Internal reasoning work.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact).

## Purpose

Give creative and copy a single, defensible angle to build on, and a clear frame for the
offer that the downstream copy fills in. The angle is the why-now and why-us. The offer
framing is how the offer is positioned, not the price itself.

## When to use

- Stream 2 needs `angle` and `offer_framing` for the strategy-artifact.
- The segments are set (from `audience-segmentation`) and the message must now be chosen.

## Inputs

- The `segments[]` from `audience-segmentation`.
- The active `briefs/` file: objective, product, plan, price, promotion,
  offer_framing_notes.
- `context/brand-voice.md`: the empowering voice and the hard mechanical rules.
- `context/01-brand-brief.md`: what the platform actually offers (formats, plans).
- `context/profiles/maharat/multi-instructor-angles.md`: the method for a multi-instructor or catalog angle (a
  Skill Path, a bundle, an occasion or catalog promotion, a recommendation).

If a needed offer variable is absent from both brief and context, stop and ask.

## Steps

1. Read the offer from the brief: product, plan, price, promotion. Read the
   offer_framing_notes if present.
2. Map pains and gains per segment, before choosing the angle. For each segment from
   `audience-segmentation`, list the top customer pains (what frustrates or blocks them
   today) and desired gains (what they want to build or feel), drawn only from the segment
   "why" and from context, never invented. Write each as a job story where it helps: "when
   I..., I want to..., so that I...". This is the customer profile the angle must serve.
   Source: Strategyzer Value Proposition Canvas, JTBD job story.
3. Choose the angle: the central message and the rationale for why it works for these
   segments and this offer. The rationale must relieve a named pain or create a named gain
   for a specific segment from step 2, not be a clever line with no need behind it. Tie it to
   what the reader can build, never to what they lack. When the brief's product spans several
   instructors (a Skill Path, a bundle, an occasion or catalog promotion, or a recommendation),
   the angle is a multi-instructor angle: one reader-outcome umbrella with each instructor cast as
   one path toward it, never a list of teachers. Build it per
   `context/profiles/maharat/multi-instructor-angles.md` and pick the grouping logic (skill cluster, occasion,
   identity moment, curated recommendation, or catalog offer) from the brief.
4. Frame the offer: how it is positioned (the hook, the value, the path to a first action),
   and name the competitive alternative the reader uses instead today (free content on
   social, another app, or nothing) and how the positioning beats it. Source: April Dunford,
   positioning component one. Show the price only if the brief provides it and the asset will
   display it. If the brief marks price or promotion as an ASSUMPTION, frame the offer without
   a number and flag it.
5. Keep one clear through-line: a segment-tuned angle can vary, but the core idea is one.
6. Do not invent a Skill Path title, an instructor name, an accreditation claim, or a
   discount the brief did not supply.
7. Record the result in the angle and offer framing template, with the open items.

## Output

The `angle` and `offer_framing` fields:

```
angle           the core message and its rationale (why it works for the segments and offer),
                grounded in a per-segment pain relieved or gain created
offer_framing   how the brief's offer is positioned (not the price itself unless the brief
                supplies it and the asset shows it), including the competitive alternative it
                beats
```

See `templates/angle-and-offer-framing.md`.

## How this connects to the contract and gates

- Handoff: feeds the `angle` and `offer_framing` fields of the strategy-artifact assembled
  by the 02 hub, which flow to creative (3), copy (4), and lifecycle (7). Unconfirmed price
  or promotion rides forward in the `open_items` of the common envelope.
- Verification: internal artifact, skill eval only, per `runtime/verification.md`. The copy
  built from this angle runs the full gate stack later in stream 4.

## Hard rules

- Price and promotion are shown only when the brief supplies them and the asset calls for
  them. A missing price is never invented.
- Every angle relieves a named pain or creates a named gain tied to a specific segment. Pains
  and gains are drawn from the segment "why" and from context, never invented.
- The offer framing names the competitive alternative the reader uses instead today and how
  the positioning beats it. The alternative is a real one, never a straw man.
- No invented Skill Path titles, no instructor names, no accreditation claims.
- Empowering framing, never deficit-framed. English-first for any drafted customer text.
- No em dashes, no tatweel, Western numerals only.

# SOP 02: Strategy and planning

Stream 2. Owner: strategy-lead. Mode: reasoning. Turns the validated, scoped brief into the
strategy-artifact the rest of the funnel builds on. It segments the audience from data, sets
the angle, frames the offer, and defines the single success metric that stream 8 measures
against. It shows a price only if the brief supplies it. It never invents a segment size, a
number, an angle claim, or an offer detail.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Trigger

A validated brief and scope note from stream 1, with the entry point confirmed and the
in-scope streams known.

## Inputs

- The validated brief and scope note (stream 1).
- The brief: audience, offer (product, plan, price, promotion), objective, success metric,
  channels, schedule.
- Owned-audience data where it exists (for example the lapsed-contact contacts), for segment
  definitions and sizes. Where live data is needed at send time, that is flagged, not guessed.
- `context/` for facts about the platform and audience.

## Steps

1. Read the success metric from the brief. The brief names the single number this campaign is
   measured against, with its target. Carry it forward exactly. Do not redefine it and do not
   add vanity metrics. This is the metric stream 8 reads and stream 9 reports against.
   Then test its quality before building on it: (a) leading versus lagging, is it a measure
   the campaign can actually move in flight, or a far-downstream lagging number nothing in the
   funnel can influence in time; (b) does it capture real customer value, not a vanity count;
   (c) is it movable, with a clear path from the campaign's actions to the number. It must also
   still carry a target number and a date, per the brief's SMART requirement. If the metric is
   weak on any of these (no number, no date, lagging beyond reach, vanity, or not movable),
   raise it as an open item to the human gate. Do not invent a target, a date, or a substitute
   metric, and do not quietly carry a weak one forward.
2. Segment the audience. Cut the audience into a small number of meaningful segments from the
   data. For an owned audience, cut the contacts (for example the about 18,000 lapsed-contacts) by
   real signals: engagement recency, prior interest, never-engaged versus lapsed. Use data for
   sizes. Where a size needs live data at send time, mark it pending, do not invent it.
3. Set the angle. State the one core message and the rationale tied to the audience and the
   objective. Empowering, never deficit-framed. The angle is what creative and copy build on,
   so it is concrete, not a slogan.
4. Frame the offer. Position the brief's offer for each segment. Show the price only if the
   brief gives it; if price is an ASSUMPTION, frame around value and mark the price pending.
   Never invent a discount, plan, offer title, or an unverified claim.
5. Plan the channels. State which streams this campaign uses and the entry point (paid or
   owned), consistent with the scope note from stream 1.
6. Assemble the strategy-artifact. Carry forward every unresolved ASSUMPTION and OPEN ITEM
   from stream 1 in `open_items` so downstream is not surprised.

## Output

A `strategy-artifact` (see `runtime/handoff-contract.md`), internal; skill eval only:
- segments[]: each with name, size (from data, or pending with a reason), definition, why.
- angle: the core message and its rationale.
- offer_framing: how the brief's offer is positioned (price only if the brief shows it).
- channel_plan: which streams run, and the entry point (paid or owned).
- success_metric: the single number from the brief that stream 8 measures against.

This artifact hands off to streams 3, 4, and 7.

## Quality bar

- Every segment size traces to data or is marked pending. No invented sizes.
- The success metric is the brief's, carried forward unchanged. No after-the-fact metric, no
  vanity metric. It passes the quality test (leading and movable, captures customer value,
  carries a number and a date). A weak metric is raised as an open item to the human gate,
  never repaired by inventing a value.
- The angle is empowering, never deficit-framed.
- The offer framing shows a price only when the brief supplies it. No invented offer detail,
  title, or an unverified claim.
- Gate: skill eval for structure and completeness. Internal artifact, so no arabic-copy-qa or
  brand-qa unless it carries customer-facing copy (see `verification.md`).

## Example output (shape, not real copy, no invented values)

```
strategy-artifact:
  segments:
    - name: lapsed-engaged
      size: [from data, e.g. count of contacts active in last N months]
      definition: opened or clicked previously, no purchase
      why: warm, lower friction to a first purchase
    - name: never-engaged
      size: [from data]
      definition: on list, no recorded engagement
      why: needs a value-led reintroduction, not a hard offer
  angle: "[one empowering core message, tied to the objective]"
  offer_framing: "[positioning per segment; price shown only if brief provides it]"
  channel_plan: { entry_point: owned audience, streams: [4, 7, 6, 8, 9] }
  success_metric: "[the single number and target, exactly as the brief states it]"
  open_items: [price ASSUMPTION pending, gate_platform OPEN ITEM]
```

## Review owner

strategy-lead owns the strategy-artifact. Any unresolved ASSUMPTION on a field a downstream
stream needs is surfaced to Ahmed, not closed by the strategist. The success metric is set
here once and is the only metric stream 8 and stream 9 measure against.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.

---
name: audience-and-bidding
description: Set the audience strategy and bid strategy for paid performance. Use to define targeting per channel (prospecting, retargeting, lookalikes, interests), the bid strategy, and the optimization event, all tied to the success_metric and never assuming a target. Triggers on "audience strategy," "targeting," "bid strategy," "optimization event," "lookalikes," "retargeting." Sub-skill of paid-performance, owned by performance-marketer.
---

# Audience and Bidding (paid-performance sub-skill)

Produces the audience strategy and the bid strategy that fill the `audiences` and
`bid_strategy` fields of the `media-plan-package`. It defines who each channel reaches and how
each channel bids. It never assumes a target; the target comes from the brief, and the bid
strategy is built to chase it.

Owner: performance-marketer. Mode: reasoning. The build is handed to `paid-build-engineer`
(stream 5), who stages it paused for the human gate.

## When to use

- The channel mix is fixed and each channel needs an audience and a bid strategy.
- The orchestrator dispatches paid performance after the media-plan is set.

## Inputs

- The `media-plan` output: the selected channels and the budget split.
- The `strategy-artifact` (stream 2): segments, the angle, success_metric.
- The active `briefs/` file: the target (CPA, ROAS, or as the brief sets it), geo (GCC,
  primary Saudi), and the offer.

If the target is absent from the brief, stop and ask. Never assume a target CPA or ROAS, and
never invent an optimization event the brief or conversion plan does not support.

## Audience strategy

Per channel, define the audience layers that fit the segments from the strategy-artifact:

- Prospecting: interest, keyword, or broad audiences for cold reach.
- Retargeting: site or engagement audiences, gated on the conversion-path events being live.
- Lookalikes or similar audiences: seeded from owned or converter audiences where the platform
  and data allow, never from personal data exposed in a URL.

Map each audience to a segment and to the funnel stage it serves. Do not invent an audience
the data cannot support; record it as an open item instead.

## Steps

1. Confirm the target (CPA, ROAS, or as the brief sets it) and geo from the brief. If the
   target is missing, stop and ask.
2. For each channel, define the prospecting, retargeting, and lookalike layers that fit the
   segments. Map each to a segment and a funnel stage.
3. Set the bid strategy per channel (for example, cost cap, target CPA, target ROAS, or
   maximize conversions) chosen to chase the brief target, with the rationale stated.
4. Set the optimization event per channel, aligned to the conversion-path events (submit or
   confirm). Do not optimize toward an event the tracking plan does not fire.
5. Flag any audience or event that the data or platform cannot yet support as an open item.
6. Hand the audience strategy and the bid strategy to the hub for the `media-plan-package`.

## Output

Fills two fields of the `media-plan-package`:

```
audiences      per-channel audience layers, each mapped to a segment and funnel stage
bid_strategy   per-channel bid strategy and optimization event, tied to the brief target
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the target-from-brief rule, and
  the optimization-event alignment.
- The plan advances through the hub: `brand-qa-reviewer` on any in-platform copy, then the
  human gate authorizes spend, per `runtime/verification.md`.

## Hard rules

- The target traces to the brief. Missing, stop and ask. Never assume a target CPA or ROAS.
- Audiences never derive from personal or sensitive data exposed in a URL parameter.
- The optimization event aligns to the conversion-path events; never optimize toward an event
  the tracking plan does not fire.
- The plan never spends and never launches; spend is gated at the human gate.
- No accreditation claims, no fundraising, roadmap, or unannounced plans.
- No em dashes, no tatweel, Western numerals only.

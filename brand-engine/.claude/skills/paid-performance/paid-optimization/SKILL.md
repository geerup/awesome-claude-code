---
name: paid-optimization
description: Plan in-flight optimization for paid performance. Use once a campaign is live to read performance against the success_metric and propose scale, cut, and creative-rotation moves. Every move is a proposal routed through the human gate, never a live action on the campaign. Triggers on "paid optimization," "scale or cut," "creative rotation," "optimize the paid campaign," "what should we change," "rebalance the budget." Sub-skill of paid-performance, owned by performance-marketer.
---

# Paid Optimization (paid-performance sub-skill)

Produces the in-flight optimization plan: a structured read of live performance against the
success_metric and a set of proposed moves to scale, cut, or rotate. It fills the optimization
view that the hub carries forward and that monitoring (stream 8) reads alongside. Every move is
a proposal. This skill never pauses an ad set, never shifts a budget, and never swaps a creative
on the live campaign. The human gate decides; a human acts.

Owner: performance-marketer. Mode: reasoning, and gated for any action. Reads are grounded in
approved data sources (BigQuery, GA4, the ad platforms) once access is granted.

## When to use

- A paid campaign is live and there is enough data to read performance against the success_metric.
- The orchestrator or analytics-reporter surfaces a read that calls for a scale, cut, or rotation
  decision.

## Inputs

- The live `media-plan-package`: channels, budget_split, audiences, bid_strategy,
  success_metric_link.
- The performance read from monitoring (stream 8), grounded in approved data sources, measured
  against the strategy-artifact success_metric.
- The active `briefs/` file: the target, the remaining budget and window, the geo.

If the success_metric is absent, stop and ask. Do not invent a metric to optimize toward after
the fact. Measure against the success_metric the strategy-artifact set, never a new one.

## The moves this skill proposes

1. Scale: increase budget or expand audiences on what beats the success_metric, within the brief
   budget and window. Never propose spend beyond the brief budget.
2. Cut: pause or reduce what misses the success_metric after a fair learning window.
3. Creative rotation: retire fatigued creative and rotate in QA-passed variants, by variant id.
   New creative or copy is requested from streams 3 and 4, never written here.

Each move states the evidence (number, source, window), the expected effect tied to the
success_metric, and that the human gate is the decision owner.

## Steps

1. Restate the success_metric verbatim from the strategy-artifact. If absent, stop and ask.
2. Read each channel, ad set, and creative against the success_metric, with evidence. Exclude
   vanity metrics (impressions, raw reach) as a result bar.
3. Draft scale, cut, and rotation moves. Each move ties to the success_metric and stays within
   the brief budget and window. Spend beyond the brief budget is never proposed.
4. For creative rotation, reference QA-passed variants by id and request new variants from
   streams 3 and 4 where needed. Do not write copy here.
5. Mark every move as a proposal for the human gate, with evidence and expected effect.
6. Hand the optimization view to the hub and to monitoring (stream 8). No move is executed here.

## Output

The optimization view carried by the `media-plan-package` and read alongside monitoring:

```
read           per channel, ad set, and creative, measured against the success_metric, with evidence
proposed_moves scale, cut, and creative-rotation moves, each a proposal with evidence and expected effect
decision_owner human gate on every move
open_items     data gaps, access not granted, learning window not yet complete
```

## Verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the measure-against-success_metric
  rule, and the proposal-not-action rule.
- Any move that would change live spend or a live asset is a gated action at the human gate, per
  `runtime/verification.md`. A human acts; the engine never does.

## Hard rules

- Every move is a proposal for the human gate. The skill never pauses, shifts budget, or rotates
  creative on the live campaign. Silence is not approval.
- Measure against the strategy-artifact success_metric, never a metric invented after the fact.
- Never propose spend beyond the brief budget or window. Budget and target are brief inputs.
- Exclude vanity metrics as a result bar.
- New creative and copy come from streams 3 and 4 by QA-passed variant id, never written here.
- No accreditation claims, no fundraising, roadmap, or unannounced plans.
- No em dashes, no tatweel, Western numerals only, empowering framing never deficit-framed.

---
name: 08-monitoring-optimization
description: Hub for stream 8 monitoring and optimization, owned by analytics-reporter. Use to read live performance and plan tests once a campaign is running, triggers on "how is it performing," "read the numbers," "what is working," "plan an A/B test," "what should we optimize." Routes to performance-readout and ab-test-plan. Reasoning only, grounded in BigQuery and GA4 once approved. Measures against the strategy-artifact success_metric, never a metric invented after the fact, and proposes optimization moves through the human gate rather than acting on the live campaign.
---

# 08 Monitoring and Optimization (stream 8 hub)

The entry point for reading how a running campaign performs and deciding what to test next.
Owned by `analytics-reporter`, reasoning mode. This hub does not act on a live campaign and
does not write copy. It reads the inputs, routes to the right sub-skill, and keeps every
read anchored to the success_metric the strategy set.

## Purpose

Turn live performance data into honest, evidence-backed reads and proposed optimization
moves, measured against the `strategy-artifact` success_metric and never against a metric
invented after the fact. One machine, any campaign. No vanity metrics.

## When to use

- A campaign is live (or in a live test window) and someone asks how it is doing.
- The orchestrator dispatches stream 8 (per `runtime/stream-ownership.md`).
- A decision needs evidence: keep, change, pause, or test something.

Route by need:
- Read performance against the success_metric, name what works and what does not with
  evidence, and propose optimization moves: `performance-readout`.
- Design a single-variable test with a clear hypothesis and a stop rule: `ab-test-plan`.

## Inputs

- The `strategy-artifact`: success_metric (the bar every read measures against), segments,
  angle, channel_plan.
- The active `briefs/` file: the objective and any target the brief set.
- Data tools once approved and on the `settings.json` allowlist: BigQuery, GA4.

If the success_metric is absent from the strategy-artifact, stop and ask. Do not invent a
metric to measure against, and do not substitute a vanity metric for the one the strategy set.

## Steps

1. Validate the incoming envelope: right campaign_id, strategy-artifact present with a
   success_metric, open_items read. If incomplete, return it, do not start.
2. Pull the metrics that map to the success_metric, from the approved data tools only.
3. Route to the sub-skill: a read goes to `performance-readout`, a test design goes to
   `ab-test-plan`.
4. Keep every claim tied to evidence (the number, the source, the window). State misses
   plainly.
5. Frame every optimization move as a proposal for the human gate. Nothing here pauses,
   shifts budget, or changes a send on its own.

## Output

Two internal reads that feed the campaign and, later, stream 9:
- a performance readout (from `performance-readout`),
- an A/B test plan (from `ab-test-plan`).

Both are internal artifacts. Neither crosses a stream boundary as a handoff-contract
artifact on its own. They become the evidence that stream 9 turns into the `report-artifact`
defined in `runtime/handoff-contract.md`.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), live data from approved tools.
- Feeds: stream 9 reporting and learning, which emits the `report-artifact`.
- Verification: per `runtime/verification.md`, stream 8 is internal reasoning, so each
  sub-skill runs its own skill eval for structure and completeness only. No arabic-copy-qa
  or brand-qa applies unless a read carries customer-facing copy.

## Hard rules

- Measure against the success_metric the strategy set, not one invented after the fact, and
  never against a vanity metric.
- Propose, do not act. Any pause, budget shift, or send change goes through the human gate.
- No em dashes, no tatweel, Western numerals only.

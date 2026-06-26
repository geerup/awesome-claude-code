---
name: 09-reporting-learning
description: Hub for stream 9 reporting and learning, owned by analytics-reporter. Use to close a campaign with an honest report and to bank reusable learnings, triggers on "write the campaign report," "how did the campaign do," "what did we learn," "log the learnings," "wrap up the campaign." Routes to campaign-report and learnings-log, and emits the report-artifact that feeds the next campaign's strategy-lead. Measures results against the strategy-artifact success_metric, never a metric invented after the fact, excludes vanity metrics, and proposes changes rather than acting.
---

# 09 Reporting and Learning (stream 9 hub)

The end of one campaign and the start of the next. Owned by `analytics-reporter`, reasoning
mode. This hub turns the campaign's performance into the `report-artifact` defined in
`runtime/handoff-contract.md`, and banks reusable learnings so the next campaign starts
ahead of where this one did. It closes the loop.

## Purpose

Produce an honest, evidence-backed close: results against the `strategy-artifact`
success_metric, what worked with evidence, what to change for the next brief, and a reference
to where the reusable learnings were appended. One machine, any campaign. No vanity metrics.

## When to use

- A campaign or a test window has ended and needs its report.
- The orchestrator dispatches stream 9 (per `runtime/stream-ownership.md`).
- Findings from stream 8 are ready to be turned into a durable record and learnings.

Route by need:
- Write the close-out report (results vs the success_metric, what worked, what to change):
  `campaign-report`.
- Append reusable learnings so the next campaign uses them: `learnings-log`.

Run order: the `campaign-report` is written first, then its reusable learnings are appended
through `learnings-log`, and the log reference goes back into the report as `learnings_log_ref`.

## Inputs

- The `strategy-artifact`: success_metric (the bar every result measures against), segments,
  angle, channel_plan.
- The stream 8 `performance-readout` and any `ab-test-plan` results.
- The active `briefs/` file: the objective and any target the brief set.
- Data tools once approved and on the `settings.json` allowlist: BigQuery, GA4, Stripe.

If the success_metric is absent from the strategy-artifact, stop and ask. Do not invent a
metric to report against, and do not substitute a vanity metric for the one the strategy set.

## Output: the report-artifact

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
results           metrics vs the strategy-artifact success_metric
what_worked       with evidence
what_to_change    concrete, for the next brief
learnings_log_ref where this was appended for reuse
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). The `campaign-report` produces results, what_worked, and what_to_change. The
`learnings-log` produces learnings_log_ref.

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), stream 8 reads (performance-readout, ab-test-plan).
- Produces: the `report-artifact` (stream 9 -> the next campaign's strategy-lead).
- Verification: per `runtime/verification.md`, stream 9 is internal reasoning, so each
  sub-skill runs its own skill eval for structure and completeness only. No arabic-copy-qa or
  brand-qa applies unless a report carries customer-facing copy.

## Hard rules

- Measure against the success_metric the strategy set, not one invented after the fact, and
  never against a vanity metric.
- Keep the report honest: state misses plainly, with the data. Every claim carries evidence.
- Propose, do not act. What_to_change is a recommendation for the next brief, not an action on
  a live campaign.
- No em dashes, no tatweel, Western numerals only.

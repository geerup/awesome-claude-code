---
name: campaign-report
description: Sub-skill of stream 9. Use to write a campaign's close-out report, results against the strategy-artifact success_metric, what worked with evidence, and what to change for the next brief. Triggers on "write the campaign report," "how did the campaign do," "close out the campaign," "results vs target." Reasoning only, grounded in BigQuery, GA4, and Stripe once approved. Measures against the success_metric the strategy set and never a metric invented after the fact, excludes vanity metrics, keeps every claim tied to evidence, and frames what to change as a recommendation for the next brief rather than an action on a live campaign.
---

# Campaign Report (stream 9 sub-skill)

Writes the honest close on a campaign. Owned by `analytics-reporter`, reasoning mode. The
report is anchored to one thing: the success_metric the strategy set. It produces the bulk of
the `report-artifact` defined in `runtime/handoff-contract.md`.

## Purpose

Give the next campaign a clear-eyed record: where this campaign landed against its
success_metric, what worked and what did not with the evidence for each, and concrete changes
for the next brief. No spin, no vanity metrics.

## When to use

- A campaign or test window has ended and needs its formal report.
- Stream 8 reads (performance-readout, ab-test-plan results) are ready to be turned into a
  durable close-out.

## Inputs

- The `strategy-artifact`: success_metric, segments, angle, channel_plan.
- The stream 8 `performance-readout` and any `ab-test-plan` results.
- The active `briefs/` file: the objective and any target the brief set.
- Live data from approved tools only: BigQuery, GA4, Stripe, on the `settings.json` allowlist.

If the success_metric is absent, stop and ask. Do not invent one, and do not report a vanity
metric (impressions, raw reach, follower count) in place of it.

## Steps

1. Restate the success_metric exactly as the strategy-artifact set it. This is the bar.
2. Report results against it: actual vs target, miss or beat, each with number, source, window.
   State the headline result plainly.
3. List what_worked, each with its evidence. No claim without a number behind it.
4. Optionally add supporting cuts, anchored to the success_metric: a funnel-stage view and a
   per-segment cut drawn from the strategy-artifact segments. These support the success_metric,
   they never replace it and never reintroduce vanity metrics into the verdict. Add only the
   cuts that aid the read.
5. List what_to_change for the next brief: concrete, specific, actionable. Each change is a
   recommendation, not an action taken on a live campaign. Each change carries an owner and a
   target date (or target brief), so every recommendation is trackable and accountable.
6. Hand the reusable learnings to `learnings-log`, then record the returned reference as
   learnings_log_ref.
7. Run the skill eval for structure and completeness.

## Output

Use `templates/campaign-report.md`. The report fills the `report-artifact` body:

```
results           metrics vs the strategy-artifact success_metric
what_worked       with evidence
what_to_change    concrete, for the next brief, each with an owner and a target date or brief
learnings_log_ref from learnings-log
```

Internal artifact, wrapped in the common envelope. It is the close that feeds the next
campaign's strategy-lead.

## Hard rules

- Measure against the success_metric the strategy set, not one invented after the fact.
- No vanity metrics. Every claim carries its evidence. State misses plainly.
- Every what_to_change item carries an owner and a target date (or target brief), so the
  recommendation is trackable and accountable.
- Propose, do not act. What_to_change is for the next brief, never an action on a live campaign.
- No em dashes, no tatweel, Western numerals only.

# Campaign Report

Internal artifact. Owned by analytics-reporter. This is the report-artifact body. Every claim
carries its evidence. What to change is a recommendation for the next brief, never an action
on a live campaign.

## Envelope

- campaign_id:
- produced_by: analytics-reporter
- stream: 9 reporting and learning
- status: draft | qa-passed
- window reported: (start date to end date, e.g. 2026-06-01 to 2026-06-30)
- data sources: (e.g. BigQuery, GA4, Stripe, only approved tools)

## Success metric (restated from the strategy-artifact)

State the success_metric exactly as the strategy-artifact set it. This is the only bar.
If the strategy-artifact has no success_metric, stop and ask. Do not invent one.

- success_metric:
- target value (if the brief set one):

## results (vs the success_metric)

| Metric | Actual | Target / success_metric | Gap (beat or miss) | Source | Window |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

State the headline result plainly, miss or beat. No softening, no vanity metrics
(impressions, raw reach, follower count) in place of the success_metric.

## what_worked (with evidence)

- Finding:
  - Evidence (number, source, window):
- Finding:
  - Evidence (number, source, window):

## Supporting cuts (optional, anchored to the success_metric)

Optional. These cuts support the success_metric, they never replace it and never reintroduce
vanity metrics (impressions, raw reach, follower count) into the verdict. Use them to explain
where the success_metric landed, not to add new goals. Fill only the cuts that aid the read.

Funnel-stage view (success_metric decomposed by stage, named for this campaign's funnel):

| Funnel stage | Value | Source | Window |
|---|---|---|---|
|  |  |  |  |

Per-segment cut (segments drawn from the strategy-artifact, not invented here):

| Segment (from strategy-artifact) | Success_metric value | Source | Window |
|---|---|---|---|
|  |  |  |  |

## what_to_change (concrete, for the next brief)

Each item is a recommendation for the next brief, not an action on a live campaign. Each
change carries an owner and a target date (or the target brief it lands in), so every
recommendation is trackable and accountable. No owner-less, date-less change.

- Change:
  - Why (tied to a result above):
  - Owner:
  - Target date or target brief: (e.g. 2026-07-15, or the next campaign brief)
- Change:
  - Why (tied to a result above):
  - Owner:
  - Target date or target brief: (e.g. 2026-07-15, or the next campaign brief)

## learnings_log_ref

- Reference where the reusable learnings were appended (from learnings-log), e.g.
  references/learnings-log.md#2026-06-nonpayer-email

## Open items

- Anything unresolved (data gap, tool not yet approved, metric not yet instrumented).

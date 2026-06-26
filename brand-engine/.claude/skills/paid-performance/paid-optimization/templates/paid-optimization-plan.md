# Paid Optimization Plan

Internal artifact. Owned by performance-marketer. Reads live performance against the
success_metric and proposes scale, cut, and creative-rotation moves. Every move is a proposal
for the human gate. The skill never pauses, shifts budget, or rotates creative on the live
campaign.

## Envelope

- campaign_id:
- produced_by: performance-marketer
- stream: paid-performance (in-flight, reads alongside stream 8)
- status: draft | qa-passed
- window read: (start date to end date)
- data sources: (BigQuery, GA4, ad platforms, only approved tools)

## Success metric (restated from the strategy-artifact)

State the success_metric exactly as the strategy-artifact set it. This is the only bar. If the
strategy-artifact has no success_metric, stop and ask. Do not invent one.

- success_metric:
- target value (if the brief set one):
- remaining budget and window (from the brief):

## Read vs the success metric (with evidence)

| Level | Channel / ad set / creative | Metric | Actual | success_metric | Beat or miss | Source | Window |
|---|---|---|---|---|---|---|---|

Do not list vanity metrics (impressions, raw reach) as a result against the success_metric.

## Proposed moves (human-gate proposals, not actions)

| Move type | What | Evidence (number, source, window) | Expected effect (tied to success_metric) | Within brief budget? | Decision owner |
|---|---|---|---|---|---|
| Scale |  |  |  |  | human gate |
| Cut |  |  |  |  | human gate |
| Creative rotation (variant id) |  |  |  |  | human gate |

No move proposes spend beyond the brief budget or window. Creative rotation references QA-passed
variants by id; new creative or copy is requested from streams 3 and 4, never written here.

## Open items

- Anything unresolved (data gap, access not granted, learning window not yet complete, new
  creative requested but not yet QA-passed).

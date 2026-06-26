# Warehouse Query Spec

Internal artifact. Owned by data-tracking-engineer (plumbing) and analytics-reporter (read).
Read-only. The query is specified and gated; the BigQuery MCP is not yet approved, so the
query is added on approval and is not run against the warehouse before then.

## Envelope

- campaign_id:
- produced_by: data-tracking-engineer / analytics-reporter
- stream: 8 monitoring and optimization
- status: draft | qa-passed
- window: (start date to end date, e.g. 2026-06-01 to 2026-06-14)

## Question (one sentence)

State the monitoring question plainly.

- question:

## Success metric (restated from the strategy-artifact)

State the success_metric exactly as the strategy-artifact set it. The query measures this and
only this. If the strategy-artifact has no success_metric, stop and ask. Do not invent one,
and do not substitute a vanity metric (impressions, raw reach, follower count).

- success_metric:
- target value (if the brief set one):

## Query intent (natural language)

- what is counted:
- time window:
- cut by (segment or dimension):

## Query (SQL or BigQuery MCP call)

```
-- Name the source tables and fields. Select only what the metric needs.
-- No personal or sensitive identifiers in the output.
```

- source tables:
- fields selected:

## Data-access open items

- BigQuery MCP: an MCP candidate, not yet approved. The query is gated and added on approval.
  Do not assume the connection is live. See context/04-tools-and-access.md.
- Missing table, unconfirmed field, or instrumentation gap: (list each; do not assume one).

## Privacy note

No personal or sensitive data in the query output. Only the fields the metric needs are
selected. No personal data in any tracking parameter.

## Guardrails check

- Measured against the strategy-artifact success_metric, not an invented or vanity metric.
- Western numerals only (0 to 9). No em dashes, no tatweel.

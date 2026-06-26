---
name: warehouse-query
description: Sub-skill of stream 8. Use to translate a monitoring question into a natural-language or SQL query against the warehouse, anchored to the strategy-artifact success_metric, and to surface data-access open items. Triggers on "query the warehouse," "pull this from BigQuery," "write the SQL," "what does the data say," "get the numbers from the warehouse." Reasoning and read-only. The BigQuery MCP is not yet approved, so the query is specified and gated, added on approval. Measures against the success_metric the strategy set, never an invented metric, and never exposes personal data in outputs.
---

# Warehouse Query (stream 8 sub-skill)

Turns a monitoring question into a precise warehouse query, in natural language or SQL,
anchored to the success_metric the strategy set. Owned by `data-tracking-engineer` for the
plumbing and `analytics-reporter` for the read. Reasoning and read-only. It specifies and
prepares the query; it does not run against the warehouse until the access path is approved.

## Purpose

Produce a query spec a human can approve and run: the monitoring question stated plainly, the
exact metric it maps to from the strategy-artifact, the query (natural-language intent and the
SQL or the BigQuery MCP call it becomes), the tables and fields it touches, and the data-access
open items that block it. The result feeds the `performance-readout` and the stream 9 report.

## When to use

- A monitoring or reporting question needs a number out of the warehouse.
- The `performance-readout` or `ab-test-plan` needs a specific metric pulled and the query
  must be specified before it can run.
- Someone asks what the data says and the answer requires a warehouse query.

## Inputs

- The `strategy-artifact` (stream 2): the success_metric the question maps to, plus segments.
- The active `briefs/` file: the objective and any target the brief set.
- The warehouse: BigQuery, with GA4, Stripe, and event tables as the likely sources. Access
  is via the BigQuery MCP, which is an MCP candidate to trial and is not yet approved. See
  `context/04-tools-and-access.md`.

If the success_metric is absent from the strategy-artifact, stop and ask. Do not invent a
metric, and do not substitute a vanity metric (impressions, raw reach, follower count) for it.

## Steps

1. State the monitoring question plainly in one sentence.
2. Map it to the success_metric exactly as the strategy-artifact set it. The query measures
   that metric; if no success_metric exists, stop and ask. Do not invent one.
3. Write the query intent in natural language: what is counted, over what window, cut by which
   segment or dimension.
4. Specify the query: the SQL against the named tables and fields, or the BigQuery MCP call it
   becomes. Name the source tables and the time window. Select only the fields the metric
   needs, never personal or sensitive identifiers in the output.
5. Surface the data-access open items: the BigQuery MCP is not yet approved, so the query is
   gated and added on approval. Note any missing table, unconfirmed field, or instrumentation
   gap. Do not assume the connection is live.
6. Run the skill eval for structure and completeness, then hand the spec on.

## Output

Use `templates/warehouse-query-spec.md`. The shape:
- question (the monitoring question, one sentence),
- success_metric (restated from the strategy-artifact, the bar the query measures),
- query_intent (natural-language: what, window, cut),
- query (the SQL or the BigQuery MCP call, with named tables and fields),
- data_access_open_items (BigQuery MCP not yet approved, gated and added on approval; any gaps),
- privacy_note (no personal or sensitive data in the output).

Internal artifact. It feeds the `performance-readout` (stream 8) and the stream 9 report. It
does not cross a boundary on its own.

## How this connects to the contract and gates

- Consumes: the `strategy-artifact` (stream 2) success_metric and the active brief.
- Produces: a warehouse query spec that feeds `performance-readout` and the report-artifact.
- Gate before advance: skill eval for structure. Internal artifact, so no arabic-copy-qa or
  brand-qa unless the output is made customer-facing, per `runtime/verification.md`. Running
  the query against the warehouse is gated on BigQuery MCP approval.

## Hard rules

- Measure against the success_metric the strategy set, never an invented metric, never a
  vanity metric in its place.
- The BigQuery MCP is not yet approved. Specify the query and gate it; it is added on
  approval. Do not assume the connection is live or run against the warehouse before approval.
- Never expose personal or sensitive data in a query output. Select only the fields the metric
  needs. No personal data in any tracking parameter.
- Surface every data-access open item rather than filling a gap with an assumed table or field.
- No em dashes, no tatweel, Western numerals only.

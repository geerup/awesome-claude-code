---
name: performance-readout
description: Sub-skill of stream 8. Use to read a live campaign's performance against the strategy-artifact success_metric and produce an honest, evidence-backed readout. Triggers on "how is it performing," "read the numbers," "what is working," "what is not working," "what should we optimize." Reasoning only, grounded in BigQuery and GA4 once approved. Names what works and what does not with evidence, measures against the success_metric the strategy set and never a metric invented after the fact, excludes vanity metrics, and frames every optimization move as a proposal through the human gate.
---

# Performance Readout (stream 8 sub-skill)

Reads how a running campaign is doing and says so plainly. Owned by `analytics-reporter`,
reasoning mode. The read is anchored to one thing: the success_metric the strategy set.

## Purpose

Produce a readout that a human can act on: where the campaign stands against its
success_metric, what is working and what is not with the evidence for each, and a short list
of optimization moves proposed for the human gate.

## When to use

- A live campaign needs an honest performance read.
- Someone asks what to keep, change, or pause, and the answer needs evidence.
- Before stream 9, to feed the campaign report with grounded reads.

## Inputs

- The `strategy-artifact`: success_metric, segments, angle, channel_plan.
- The active `briefs/` file: the objective and any target the brief set.
- Live data from approved tools only: BigQuery, GA4, on the `settings.json` allowlist.

If the success_metric is absent, stop and ask. Do not invent one, and do not measure against
a vanity metric (impressions, raw reach, follower count) in place of it.

## Steps

1. Restate the success_metric exactly as the strategy-artifact set it. This is the bar.
2. Pull the metrics that map to it from approved tools. Record number, source, and window
   for each.
3. Compare actual to the success_metric. State the gap plainly, miss or beat, with the data.
4. List what is working, each with its evidence. List what is not working, each with its
   evidence. No claim without a number behind it.
5. Optionally add supporting cuts, anchored to the success_metric: a funnel-stage view and a
   per-segment cut drawn from the strategy-artifact segments. These support the success_metric,
   they never replace it and never reintroduce vanity metrics as a result. Add only the cuts
   that aid the read.
6. Propose optimization moves. Each move names the change, the expected effect on the
   success_metric, and that it is a proposal for the human gate, not an action taken.
7. Run the skill eval for structure and completeness.

## Output

Use `templates/performance-readout.md`. The shape:
- success_metric (restated from the strategy-artifact),
- results vs that metric, with number, source, window,
- what_works[] with evidence,
- what_does_not_work[] with evidence,
- supporting_cuts (optional): a funnel-stage view and a per-segment cut from the
  strategy-artifact segments, anchored to the success_metric and never replacing it,
- proposed_optimizations[] (each a human-gate proposal, never an action).

Internal artifact. It feeds stream 9 and does not cross a boundary on its own.

## Hard rules

- Measure against the success_metric the strategy set, not one invented after the fact.
- No vanity metrics. Every claim carries its evidence.
- Propose, do not act. No move here pauses, shifts budget, or changes a send. The human gate
  decides, per `CLAUDE.md` and `agents/human-gate.md`.
- No em dashes, no tatweel, Western numerals only.

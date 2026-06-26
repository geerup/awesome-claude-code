# measurement-and-reporting-plan: Bassam Fattouh Teaches Makeup

Produced by analytics-reporter with data-tracking-engineer (the event and warehouse layer). Streams 8 and 9.
Reasoning only, grounded in the event data it does not produce. It measures against the strategy-artifact
success_metric, never a metric invented after the fact. Optimization and changes are proposals through the
human gate; it never changes a live campaign or spend.

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: analytics-reporter, data-tracking-engineer
- stream: 8 monitoring and 9 reporting
- status: qa-passed (plan); reads live data only after launch and access
- open_items: success-metric target and CPA are ASSUMPTION (cannot measure against an unconfirmed number until
  Ahmed confirms), gate platform and event wiring (no data until wired), warehouse access to confirm.

## Stream 8: monitoring plan

- Measures against the strategy success_metric: new paid subscriptions at or below the target CPA (target and
  CPA are ASSUMPTION until confirmed; the readout reports actuals and flags that the target is unconfirmed).
- Leading indicators read in flight (from the event_plan): free_intro_play rate, landing signup rate, email_submit
  rate, click-through, cost per landing signup, and the prospecting-to-retargeting efficiency split.
- Readout cadence: proposed weekly to Ahmed (reporting_cadence is an OPEN ITEM, confirm). A mid-flight checkpoint
  reads the leading indicators so paid can be tuned before the lagging subscription number lands.
- Warehouse: BigQuery views for free-intro plays, signups, and subscription starts, joined to spend by channel.
  No personal or sensitive data in any query parameter.

## A/B test plan (proposals, one variable each)

- Landing hero: C1 the free first step versus C3 the artist and the craft, measured on signup rate.
- Ad creative: C1 versus C2 the range, measured on cost per landing signup.
- Email M3 subject: the value line versus the artist line, measured on click-through.
- Each test changes one variable, runs to a pre-agreed signal, and any rollout is a proposal through the human gate.

## Stream 9: reporting plan (the report-artifact shape)

```
results            new subscriptions and CPA versus the (to-be-confirmed) target; leading indicators versus the checkpoint
what_worked        with evidence (which audience, creative, and channel drove efficient subscriptions)
what_to_change     concrete, for the next brief (audience, creative, offer, channel split)
learnings_log_ref  appended to the engine learnings log for reuse by the next campaign's strategy-lead
```

- Excludes vanity metrics. Measures only against the confirmed success_metric once Ahmed confirms the target.

## Handoff

Feeds the report-artifact to the next campaign's strategy-lead, closing the loop. Coordinates with
data-tracking-engineer for the event data behind every number. All optimization moves are proposals; nothing
changes a live campaign or spend without the human gate.

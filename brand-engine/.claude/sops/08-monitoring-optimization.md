# SOP 08: Monitoring and optimization

Stream 8. Owners: analytics-reporter (the readout and the test plans) and
data-tracking-engineer (the warehouse plumbing). Mode: reasoning. Reads live performance
against the strategy-artifact success metric, queries the warehouse for the truth, and plans
A/B tests. Every optimization is a proposal that goes through the human gate. This stream
never acts on the live campaign.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Trigger

A campaign is live (a paid launch is running, or a lifecycle send has gone out) and there is
performance data to read. The strategy-artifact success metric is set and known.

Default cadence: for live paid, a monthly readout with weekly campaign-level check-ins. This
is a default to set expectations at the human gate, not a replacement for the event-driven
triggers above. The event-driven triggers still apply: read whenever a live window, a spend
threshold, or a tracking question calls for it. Cadence and triggers run together.

## Inputs

- The `strategy-artifact` (stream 2): the single success metric and its target. This is the
  only yardstick. A metric not set here is not measured here.
- Warehouse access (BigQuery) and GA4, once approved, wired by data-tracking-engineer.
- The event plan from the conversion-package (stream 6): which events exist and how they map.
- The brief: budget, schedule, and the window the campaign runs in.

## Steps

1. Read against the success metric. Pull performance for the single success metric the
   strategy-artifact defined, with its target. Report progress against that target, not
   against a metric chosen after the fact. Do not introduce vanity metrics (raw impressions,
   raw follower counts) as if they were the goal.
2. Query the warehouse for the truth. data-tracking-engineer runs the warehouse queries that
   back every number. A number in the readout traces to a query, not to a platform dashboard
   read at a glance. Where an event is missing or misfiring, flag it as a tracking gap, do not
   estimate around it.
3. Segment the read. Break performance by the strategy-artifact segments and by channel, so
   the readout shows where the metric moves, not just the blended number.
4. Plan A/B tests. Each test changes exactly one variable, states a hypothesis, and sets a
   stop rule (the sample or time at which the test ends and how the winner is decided). No
   multi-variable tests, no test without a stop rule.
5. Frame optimization as proposals. Every optimization move (shift budget, pause an ad set,
   swap a subject line) is written as a proposal for the human gate, with the evidence behind
   it. The stream proposes; it never pauses, shifts, or edits the live campaign itself.
6. Assemble the readout and any test plans. Carry forward open items, especially tracking gaps.

## Output

A monitoring readout and A/B test plan (internal; skill eval per `verification.md`):
- readout: the success metric versus target, segmented by audience segment and channel, each
  number traced to a warehouse query.
- ab_test_plans[]: each with one variable, a hypothesis, and a stop rule.
- proposals[]: optimization moves for the human gate, each with its supporting evidence.
- open_items: tracking gaps and any data not yet available.

This readout feeds stream 9 reporting and informs the human gate on optimization decisions.

## Quality bar

- Performance is read only against the strategy-artifact success metric. No after-the-fact
  metric, no vanity metric presented as the goal.
- Every number traces to a warehouse query. Tracking gaps are flagged, not estimated over.
- Every A/B test changes one variable, states a hypothesis, and has a stop rule.
- Every optimization is a proposal to the human gate. The stream never acts on the live
  campaign.
- Gate: skill eval for structure and completeness. Internal artifact, so no arabic-copy-qa or
  brand-qa unless it carries customer-facing copy (see `verification.md`).

## Example output (shape, not real numbers, no invented values)

```
readout:
  success_metric: "[the metric and target, exactly as the strategy-artifact set it]"
  progress: "[value vs target, from query]"
  by_segment:
    - segment: lapsed-engaged   value: "[from query]"   query_ref: "[query id]"
    - segment: never-engaged    value: "[from query]"   query_ref: "[query id]"
  by_channel:
    - channel: email   value: "[from query]"   query_ref: "[query id]"
ab_test_plans:
  - id: test-subject-line
    variable: subject line (one variable only)
    hypothesis: "[the value-led subject lifts open rate over the control]"
    stop_rule: "[sample size or run length, and how the winner is called]"
proposals:
  - move: "[shift spend toward the better-performing segment]"
    evidence: "[the query result that supports it]"
    decision: human gate
open_items: [event X not firing, confirm before relying on its number]
```

## Review owner

analytics-reporter owns the readout and the test plans; data-tracking-engineer owns the
warehouse queries behind them. Every optimization proposal goes to Ahmed at the human gate.
The stream reads and proposes. It never changes the live campaign on its own.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.

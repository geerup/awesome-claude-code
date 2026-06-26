# SOP 09: Reporting and learning

Stream 9. Owner: analytics-reporter. Mode: reasoning. Closes a campaign with an honest report
measured against the strategy-artifact success metric, names what worked with evidence and
what to change for the next brief, and appends the reusable learnings to the log. The
report-artifact feeds the next campaign's strategy-lead. It proposes changes; it never acts.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Trigger

A campaign reaches the end of its window, or a defined milestone, and the stream 8 readout has
enough data to close on. The strategy-artifact success metric is the yardstick.

Default cadence: a monthly report, with weekly campaign-level check-ins for live paid carried
by the stream 8 readout. This default sets expectations at the human gate, it does not replace
the event-driven close above. The event-driven trigger still applies: a campaign that ends or
hits a milestone gets its report when it does, regardless of the monthly rhythm. Cadence and
triggers run together.

## Inputs

- The `strategy-artifact` (stream 2): the single success metric and its target.
- The stream 8 monitoring readout: the success metric versus target, segmented, each number
  traced to a warehouse query.
- The brief: objective, offer, schedule, so the report frames results against what was set out.
- The learnings log, to append to (not to overwrite).

## Steps

1. Report against the success metric. State the result for the single success metric the
   strategy-artifact set, versus its target. Measure against that metric only, not against a
   metric chosen after the fact, and exclude vanity metrics from the verdict.
2. Tie every claim to evidence. Each result and each what-worked point cites the stream 8
   readout and the warehouse query behind it. No claim without evidence.
3. Name what worked. State what moved the metric, by segment and channel, with the evidence.
   Empowering and honest: report a miss plainly, do not dress it up and do not deficit-frame it.
4. Name what to change. Write concrete, actionable changes for the next brief: what the next
   strategy-lead should keep, drop, or test. Tie each to the evidence that motivates it.
5. Append the learnings log. Add the reusable learnings to the log and record the reference
   so the next campaign can find them. Append, never overwrite prior learnings.
6. Assemble the report-artifact. Carry forward any open items, especially tracking gaps that
   limit a conclusion.

## Output

A `report-artifact` (see `runtime/handoff-contract.md`), internal; skill eval only:
- results: metrics versus the strategy-artifact success metric.
- what_worked: with evidence.
- what_to_change: concrete, for the next brief.
- learnings_log_ref: where this was appended for reuse.

This artifact hands off to the next campaign's strategy-lead (stream 2 of the next run).

## Quality bar

- Results are reported only against the strategy-artifact success metric. No after-the-fact
  metric, no vanity metric in the verdict.
- Every result and what-worked claim cites the stream 8 readout and its warehouse query.
- what_to_change is concrete and actionable for the next brief, each tied to evidence.
- The learnings log is appended, not overwritten, and the reference is recorded.
- Gate: skill eval for structure and completeness. Internal artifact, so no arabic-copy-qa or
  brand-qa unless it carries customer-facing copy (see `verification.md`).

## Example output (shape, not real numbers, no invented values)

```
report-artifact:
  results:
    success_metric: "[the metric and target, exactly as the strategy-artifact set it]"
    outcome: "[value vs target, from the stream 8 readout]"
    by_segment:
      - segment: lapsed-engaged   outcome: "[from readout]"   evidence: "[query ref]"
  what_worked:
    - point: "[the value-led message lifted the metric in segment X]"
      evidence: "[readout and query ref]"
  what_to_change:
    - change: "[for the next brief, test Y instead of Z]"
      because: "[the evidence that motivates it]"
  learnings_log_ref: "[path or id where this was appended]"
  open_items: [tracking gap that limited a conclusion]
```

## Review owner

analytics-reporter owns the report-artifact and the learnings-log append. The report proposes
what to change for the next brief; it does not act on the live campaign and does not decide
the next campaign. Its honest read, measured against the metric set up front, is what makes
the next strategy-lead's start better than this one's.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.

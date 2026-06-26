---
name: learnings-log
description: Sub-skill of stream 9. Use to append a campaign's reusable learnings to the shared log so the next campaign starts ahead, triggers on "log the learnings," "what did we learn," "bank this for next time," "add to the learnings log." Reasoning only. Appends, never overwrites, captures each learning with the evidence and the campaign it came from, ties learnings to the strategy-artifact success_metric rather than vanity metrics, and returns the reference the campaign-report records as learnings_log_ref.
---

# Learnings Log (stream 9 sub-skill)

Banks what this campaign taught so the next one does not relearn it. Owned by
`analytics-reporter`, reasoning mode. It appends to a durable, shared log, and returns the
reference the `campaign-report` records as learnings_log_ref.

## Purpose

Turn a campaign's findings into reusable, durable learnings the next campaign's strategy-lead
can pick up. Append-only: the log grows, it never loses prior entries.

## When to use

- After the `campaign-report` is written, to extract its reusable learnings.
- Any time a test or read produced a finding worth carrying to the next campaign.

## Inputs

- The `campaign-report`: results, what_worked, what_to_change.
- The `strategy-artifact`: success_metric (so each learning ties to a real metric).
- The existing learnings log (for example `references/learnings-log.md`), to append to it.

## Steps

1. Read the existing learnings log first. Append, never overwrite or reorder prior entries.
2. For each reusable learning, write one entry: the learning, the evidence behind it, the
   campaign_id it came from, and the date. Keep it portable, not specific to one offer or price.
3. Tie each learning to the success_metric it moved, not a vanity metric. A finding with no
   metric behind it is an observation, not a banked learning, so mark it as such.
4. Append the entries under a heading for this campaign_id.
5. Return the reference (file and anchor) so the campaign-report can record learnings_log_ref.
6. Run the skill eval for structure and completeness.

## Output

Use `templates/learnings-log.md`. Each appended entry:

```
learning     one portable sentence the next campaign can use
evidence     the number, source, and window behind it
campaign_id  where it came from
date         when it was banked (Western numerals)
```

And the returned `learnings_log_ref` for the campaign-report.

## Hard rules

- Append-only. Never overwrite or delete a prior learning.
- Tie each learning to the success_metric the strategy set, never a vanity metric, never a
  metric invented after the fact.
- Keep learnings portable: no invented offer, price, Skill Path title, or instructor name.
- No em dashes, no tatweel, Western numerals only.

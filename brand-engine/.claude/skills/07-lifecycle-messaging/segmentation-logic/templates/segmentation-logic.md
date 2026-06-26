# Segmentation logic

Fixes the audience a lifecycle flow runs on: the entry trigger, the segments, the engagement
branches, the timing, and the suppression set. The flow sub-skill orders messages against
this. Do not invent segment sizes; resolve from live data at send time.

## Entry trigger

```
entry_trigger:  <the condition that enters a contact into the flow>
```

## Segments

| Segment | Definition | Size | Source |
|---|---|---|---|
| <name> | <how the segment is cut> | <number or resolve-at-send> | <data source> |

Typical non-payer cuts: never-engaged vs lapsed-engaged, prior single-class interest vs none,
recency of last open. Use the data, not a guess.

## Engagement branches

| After | Condition | Next |
|---|---|---|
| msg-1 | opened or clicked | nudge toward the offer |
| msg-1 | not opened | subject-line retry, not a louder pitch |

State each branch condition plainly. Non-openers get a retry, never a more aggressive pitch.

## Timing

```
timing:  <inter-message delays, inside the brief send window>
```

## Suppression (not optional)

```
suppression:
  - paying contacts (about 5,000)
  - unsubscribed
  - hard-bounced
source: <confirmed at build>
```

No paying contact, unsubscribe, or hard bounce is eligible for the flow.

## Sunset rule and engagement-decay suppression (not optional)

```
sunset_rule:
  decay_condition: no open or click in roughly 90 to 180 days, or 3 to 4 flow attempts without re-engaging
  sunset_flow: 1 to 3 emails (no more than 3), a short final attempt
  then: suppress
  window_source: resolve against the brief and the data, do not invent
```

A contact who decays past this threshold runs the short sunset flow, then is suppressed.
Sunsetting protects sender reputation and deliverability, and it keeps the list to consenting,
engaged contacts, which is also sound PDPL and consent hygiene. The exact window resolves
against the brief and the data. Do not invent it.

## Open items

- Segment and audience sizes: resolve from live data at send time.
- Suppression source: confirm at build.
- Sunset window: resolve the 90 to 180 day decay window against the brief and the data.

## Guardrails check before handing to the flow

- Suppression stated explicitly with a source.
- No invented segment sizes.
- No personal or sensitive data in any tracking URL parameter.
- Western numerals only (0 to 9). No em dashes, no tatweel.

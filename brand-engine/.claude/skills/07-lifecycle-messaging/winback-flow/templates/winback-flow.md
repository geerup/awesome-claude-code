# Winback and reactivation flow

Fills the `flow` field of the `lifecycle-package` for a reactivation campaign. The flow
sequences QA-passed copy variants by id; it does not write copy. Lapsed contacts are
segmented by recency, frequency, and value (RFM-style). Audience size and recency segment
sizes resolve from live data at send time. The offer in the referenced copy traces exactly
to the brief. Nothing invented.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   lifecycle-architect
stream        7 lifecycle messaging
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , brand_qa: , compliance: }
brief_refs    <offer, plan, price, promotion, schedule, send window, inactivity thresholds>
```

## Recency segments (RFM-style, from segmentation-logic)

| Segment | Recency trigger | Definition | Size | Source |
|---|---|---|---|---|
| <name> | inactive 30 days or more | no open, click, or purchase in 30 days | <resolve-at-send> | <data source> |
| <name> | inactive 60 days or more | no open, click, or purchase in 60 days | <resolve-at-send> | <data source> |
| <name> | inactive 90 days or more | no open, click, or purchase in 90 days | <resolve-at-send> | <data source> |

Segment by recency, frequency, and value, not all the same. Use the data, not a guess.
Do not invent segment sizes or inactivity thresholds.

## Ordered flow (3 to 5 messages)

```
flow:
  - id: msg-1-reconnect
    trigger: enters winback flow at the inactivity threshold for the segment
    segment: <recency segment from segmentation-logic>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<primary-id>
    note: lead with what the reader can still build; warm; one CTA; no guilt, no deficit framing

  - id: msg-2-relevance
    trigger: <delay> after msg-1, inside the send window
    segment: <recency segment>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: a proof point or a useful free thing tied to prior interest; reinforce the angle

  - id: msg-3-offer
    trigger: <delay> after msg-2, inside the send window
    segment: <recency segment>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: offer made plain; price and promotion exactly from the brief; one CTA; no invented discount or incentive

  - id: msg-4-branch
    trigger: after msg-3, branch on engagement
    segment: <recency segment>
    channel: email
    copy_ref: copy-package/<variant-id>          # re-engaged openers and clickers: nudge toward the offer
    copy_ref_retry: copy-package/<variant-id>     # still silent: subject-line retry, not a louder pitch
    subject_ref: subject-lines/<id>

  # Optional msg-5-lastcall only if the brief defines a window and a real reason.
  # A contact still silent after this flow enters the sunset rule in segmentation-logic.
```

## Audience size

```
audience_size: resolve at send from live owned-audience data (recency segment sizes resolved at send)
```

## send_on_approval (one plain sentence)

```
send_on_approval: "Sends a 4-message Arabic reactivation flow to lapsed contacts inactive for 30 days or more, resolved at send, over 3 weeks, starting [date from brief]."
```

## Suppression and sunset (from segmentation-logic)

```
suppression:
  - paying contacts
  - unsubscribed
  - hard-bounced
sunset_step: contacts still silent through the flow enter a 1 to 3 message sunset, then suppress
```

A contact who completes the winback flow without re-engaging is handed to the sunset rule,
which protects deliverability and keeps the list to consenting, engaged contacts.

## Open items

- Platform not confirmed: design proceeds, send wiring is blocked. The package is design-only
  and not-sendable until the email or WhatsApp platform is named and approved.
- Recency segment sizes and audience size: resolve at send.
- Inactivity thresholds: confirm against the brief if the brief sets them; otherwise the
  30, 60, 90 day pattern is the proposal, resolved at send.

## Guardrails check before handing up

- Every message references a QA-passed copy variant by id. No free copy here.
- Offer, price, promotion, discount, and incentive trace exactly to the brief. Nothing invented.
- Suppression is stated: no paying contact, unsubscribe, or hard bounce receives the flow.
  Silent contacts enter the sunset-then-suppress step.
- Recency segment sizes and inactivity thresholds resolve from live data; never invented.
- Western numerals only (0 to 9). No em dashes, no tatweel. Empowering, never deficit-framed.
- Package marked not-sendable until the platform is confirmed.

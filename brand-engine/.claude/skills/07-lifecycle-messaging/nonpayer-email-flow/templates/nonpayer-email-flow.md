# Non-payer email flow

Fills the `flow` field of the `lifecycle-package`. The flow sequences QA-passed copy
variants by id; it does not write copy. Audience size resolves from live data at send time.
The offer in the referenced copy traces exactly to the brief. Nothing invented.

## Envelope reference

```
campaign_id   2026-06-nonpayer-email
produced_by   lifecycle-architect
stream        7 lifecycle messaging
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , brand_qa: }
brief_refs    <offer, plan, price, promotion, schedule, send window>
```

## Ordered flow

```
flow:
  - id: msg-1-entry
    trigger: enters non-payer flow
    segment: <segment from segmentation-logic>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<primary-id>
    note: lead with what the reader can build; one CTA; no deficit framing

  - id: msg-2-value
    trigger: <delay> after msg-1, inside the send window
    segment: <segment>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: a concrete proof point or a useful free thing; reinforce the angle

  - id: msg-3-offer
    trigger: <delay> after msg-2, inside the send window
    segment: <segment>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: offer made plain; price and promotion exactly from the brief; one CTA; no invented discount

  - id: msg-4-branch
    trigger: after msg-3, branch on engagement
    segment: <segment>
    channel: email
    copy_ref: copy-package/<variant-id>          # openers and clickers: nudge toward the offer
    copy_ref_retry: copy-package/<variant-id>     # non-openers: subject-line retry, not a louder pitch
    subject_ref: subject-lines/<id>

  # Optional msg-5-lastcall only if the brief defines a window and a real reason.
```

## Audience size

```
audience_size: resolve at send from live owned-audience data (planning estimate about 18,000 non-payers)
```

## send_on_approval (one plain sentence)

```
send_on_approval: "Sends a 4-message Arabic email flow to about 18,000 non-paying contacts over 2 weeks, starting [date from brief]."
```

## Suppression (from segmentation-logic)

```
suppression: paying contacts (about 5,000), unsubscribed, hard-bounced
```

## Open items

- Platform not confirmed: design proceeds, send wiring is blocked. The package is design-only
  and not-sendable until the email or WhatsApp platform is named and approved.
- Audience size: resolve at send.

## Guardrails check before handing up

- Every message references a QA-passed copy variant by id. No free copy here.
- Offer, price, and promotion trace exactly to the brief. Nothing invented.
- Suppression is stated: no paying contact, unsubscribe, or hard bounce receives the flow.
- Western numerals only (0 to 9). No em dashes, no tatweel. Empowering, never deficit-framed.
- Package marked not-sendable until the platform is confirmed.

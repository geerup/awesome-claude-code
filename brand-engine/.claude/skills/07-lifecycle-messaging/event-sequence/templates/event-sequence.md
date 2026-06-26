# Event and webinar sequence

Fills the `flow` field of the `lifecycle-package` for a live session, a Masterclass launch,
or an event. The flow sequences QA-passed copy variants by id; it does not write copy. The
pre-event arc is time-based off the event date; the post-event arc branches on attended vs
no-show. Audience size resolves from live data at send time. Nothing invented: the event
date, time, access details, offer, price, promotion, and replay window all come from the
brief. All example copy is illustrative only. Follows the EVENT pattern in
`skills/07-lifecycle-messaging/templates/sequence-standards.md`.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   lifecycle-architect
stream        7 lifecycle messaging
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , brand_qa: , compliance: }
brief_refs    <event date and time, access details, offer, price, promotion, replay window, send window>
```

## Ordered flow (pre-event arc, time-based off the event date)

```
flow:
  - id: pre-1-announce
    phase: pre
    trigger: registration confirmed, 2 to 4 weeks before the event date
    audience: registrant
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<primary-id>
    note: announce the event; what the reader will gain; one CTA to add it to the calendar

  - id: pre-2-reminder-weeks
    phase: pre
    trigger: 1 to 2 weeks before the event date
    audience: registrant
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: reminder; reinforce the value; one CTA

  - id: pre-3-reminder-days
    phase: pre
    trigger: 1 to 2 days before the event date
    audience: registrant
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: reminder; the access details from the brief; one CTA

  - id: pre-4-final-reminder
    phase: pre
    trigger: 1 to 2 hours before the event date
    audience: registrant
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: final reminder; urgency and the access info from the brief; one CTA to join
```

## Ordered flow (post-event arc, branches on attended vs no-show)

```
  - id: post-1-replay-insight
    phase: post
    trigger: same day, within about 3 hours of the event end
    audience: attendee
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: the replay plus one key insight; one CTA to watch

  - id: post-1-noshow
    phase: post
    trigger: same day, within about 3 hours of the event end
    audience: no-show (registered, did not attend)
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: one main CTA, watch the replay; not a stacked pitch; replay window from the brief

  - id: post-2-value-add
    phase: post
    trigger: day 2 to 3 after the event
    audience: attendee and no-show
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: a value-add not covered live; one CTA

  - id: post-3-offer
    phase: post
    trigger: day 4 to 5 after the event
    audience: attendee and no-show
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: a direct, specific offer; price and promotion from the brief; one CTA; never invent a discount
```

## Replay scarcity

```
replay_window: a limited-time replay window that expires, to drive action; the exact window from the brief, never invented
```

## Success metric

```
success_metric: attendance, then conversion (not open or click rate alone)
```

## Audience size

```
audience_size: resolve at send from live owned-audience data
```

## send_on_approval (one plain sentence)

```
send_on_approval: "Sends a 4-reminder pre-event arc and a 3-email post-event follow-up to registrants for the [event from brief], starting [date from brief]."
```

## Suppression (from segmentation-logic)

```
suppression: paying where applicable, unsubscribed, hard-bounced
```

## Illustrative example (Arabic, replace before use, copy comes from the copy-package)

```
headline:  جلستك المباشرة تبدأ قريبا
body:      احجز وقتك الان، وكن جاهزا لخطوة جديدة في رحلتك.
cta:       احفظ موعدك
```

## Open items

- Platform not confirmed: design proceeds, send wiring is blocked. The package is design-only
  and not-sendable until the email or WhatsApp platform is named and approved.
- Event date, access details, offer, and replay window: from the brief, never invented.
- Audience size: resolve at send.

## Guardrails check before handing up

- Both the pre-event reminder arc and the post-event follow-up arc are present.
- The no-show branch carries one main CTA, watch the replay; not a stacked pitch.
- The replay is a limited-time window that expires, taken from the brief.
- The success metric is attendance, then conversion; not a vanity metric.
- One clear CTA per email. Every message references a QA-passed copy variant by id. No free copy here.
- No invented event date, access details, replay window, discount, Skill Path title, or instructor name.
- Suppression is stated: no paying contact (where applicable), unsubscribe, or hard bounce receives the flow.
- Western numerals only (0 to 9). No em dashes, no tatweel. Empowering, never deficit-framed.
- Package marked not-sendable until the platform is confirmed.

# Promotion sequence

Fills the `flow` field of the `lifecycle-package` for a dated promotion: a multi-instructor, Skill
Path, or catalog offer inside a defined window. The flow sequences QA-passed copy variants by id;
it does not write copy. The ladder is time-based off the window dates; behavior branches layer on
top (a purchaser exits at once). Audience size resolves from live data at send time. Nothing
invented: the window, offer, discount or price, occasion, Skill Path title, and instructor lineup
all come from the brief and context. Each message is a multi-instructor email per
`context/profiles/maharat/multi-instructor-angles.md`. All example copy is illustrative only. Follows the PROMOTION
pattern in `skills/07-lifecycle-messaging/templates/sequence-standards.md`.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   lifecycle-architect
stream        7 lifecycle messaging
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , english_qa: , brand_qa: , compliance: }
brief_refs    <promotion window start and end, offer, discount or price, occasion, Skill Path or instructor lineup, send window>
```

## Ordered flow (the escalating-urgency ladder, time-based off the window dates)

```
flow:
  - id: promo-1-announce
    step: announce
    trigger: promotion window opens (start date from the brief)
    audience: <segment from the brief, e.g. non-payers>
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<primary-id>
    note: the occasion or theme; the offer made plain; the umbrella outcome; the lineup as a LessonCardGrid; one primary CTA

  - id: promo-2-offer
    step: offer
    trigger: mid-window (date from the brief)
    audience: <segment>, not yet purchased
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: reinforce the value; refresh the angle or lineup; one CTA

  - id: promo-3-ends-tomorrow
    step: penultimate
    trigger: 1 day before the window closes
    audience: <segment>, not yet purchased
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: the deadline first, the saving second; one CTA

  - id: promo-4-ends-tonight
    step: final
    trigger: the final hours of the window (date and time from the brief)
    audience: <segment>, not yet purchased
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: last call; the access and the deadline; one CTA

  - id: promo-5-extended
    step: extension (optional)
    trigger: only if the brief defines a real extension window
    audience: <segment>, not yet purchased
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: included ONLY when the brief gives a real extension; never invented to manufacture urgency
```

## Window

```
window: start and end dates from the brief, never invented; the extension date only if the brief gives one
```

## Behavior branches

```
purchased:     exit the sequence immediately on the purchase event
opened/clicked: may skip the early reminders; never receive a louder pitch, only the next step
non-opener:    a subject-line retry on the next step, not a louder pitch
```

## Success metric

```
success_metric: purchases or revenue attributed to the promotion inside the window (not opens or clicks alone)
```

## Audience size

```
audience_size: resolve at send from live owned-audience data
```

## send_on_approval (one plain sentence)

```
send_on_approval: "Sends a 4-email Arabic promotion sequence to the resolved [segment from brief] across the [window from brief]."
```

## Suppression (from segmentation-logic)

```
suppression: paying contacts for the promoted product, unsubscribed, hard-bounced, and anyone already converted in the window; if an evergreen flow runs at the same time, suppress contacts from receiving both at once
```

## Illustrative example (Arabic, replace before use, copy comes from the copy-package)

```
umbrella:  ابدأ مهارة جديدة هذا الموسم، مع نخبة من المدربين
headline:  تعلم من الأفضل في مجالهم
cta:       اغتنم العرض
```

## Open items

- Platform not confirmed: design proceeds, send wiring is blocked. The package is design-only and
  not-sendable until the email or WhatsApp platform is named and approved.
- Window, offer, discount, occasion, Skill Path title, and instructor lineup: from the brief and
  context, never invented.
- Audience size: resolve at send.

## Guardrails check before handing up

- The ladder is present and the cadence tightens toward the deadline; the count and dates come
  from the brief.
- Each message is a multi-instructor email with one reader outcome as the umbrella, not a list of
  teachers; one primary CTA, per-card links are quiet secondaries.
- Every named instructor is catalog-status-confirmed and every credential page-cleared, else the
  card is dropped.
- The success metric is purchases or revenue in the window, not a vanity metric.
- Every message references a QA-passed copy variant by id. No free copy here.
- No invented window, discount, deadline, occasion, Skill Path title, or instructor; no
  manufactured extension.
- Suppression is stated: no paying, unsubscribed, hard-bounced, or already-converted contact gets
  the rest of the sequence.
- Western numerals only (0 to 9). No em dashes, no tatweel. Empowering, never deficit-framed. No
  accreditation implication.
- Package marked not-sendable until the platform is confirmed.

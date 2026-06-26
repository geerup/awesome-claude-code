# Onboarding sequence

Fills the `flow` field of the `lifecycle-package` for new signups. A reusable shape. The
flow sequences QA-passed copy variants by id; it does not write copy. Audience size resolves
from live data at send time. Nothing invented. All example copy is illustrative only.

This template carries two patterns from
`skills/07-lifecycle-messaging/templates/sequence-standards.md`, selected by the brief's
audience and objective:

- WELCOME (new subscriber, build the relationship and earn a first conversion): 5 to 6 emails,
  cadence every 2 to 3 days, never daily. Email 1 within 5 minutes of signup. Email 2 day 2 to
  3, email 3 day 5 to 7, emails 4 to 5 day 7 to 14, optional email 6. Success metric: first
  conversion.
- ONBOARDING / activation (new signup or free-trial user, reach the first value milestone): 5
  to 8 emails over 7 to 14 days, scaled to the window (a 7-day trial gets a compressed 5, a
  14-day window gets 7, a 30-day window gets 8 to 10 over 2 to 3 weeks). Anchor on 5 types:
  welcome, usage tips, sales touch, usage review, expiry warning. Welcome instant; morning
  local sends (8 AM to 10 AM) for the rest. Build a time-based foundation, then layer
  behavior-triggered emails on top. Success metric: the activation rate, how many reach the
  defined milestone (completing a first lesson, finishing a Skill Path step, or a first
  Masterclass play), NOT open or click rate.

## Envelope reference

```
campaign_id   <from the active brief filename>
produced_by   lifecycle-architect
stream        7 lifecycle messaging
status        draft | qa-passed | gated-pending | approved
qa            { skill_eval: , arabic_qa: , brand_qa: }
brief_refs    <first concrete step, schedule, send window>
```

## Ordered flow

```
flow:
  - id: msg-1-welcome
    trigger: new signup confirmed
    segment: new-signup
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<primary-id>
    note: confirm the signup; lead with what the user can build; one CTA to a first step

  - id: msg-2-first-step
    trigger: <delay> after msg-1, inside the send window
    segment: new-signup
    channel: email
    copy_ref: copy-package/<variant-id>
    subject_ref: subject-lines/<id>
    note: one useful action (start one lesson, open one guide); short

  - id: msg-3-activation
    trigger: after msg-2, branch on whether the first step happened
    segment: new-signup
    channel: email
    copy_ref: copy-package/<variant-id>          # activated: next step
    copy_ref_retry: copy-package/<variant-id>     # not yet activated: gentle retry, not a louder pitch
    subject_ref: subject-lines/<id>
```

## Welcome arc (when the brief's pattern is WELCOME, ordered)

```
flow:
  - id: msg-1-deliver        # within 5 minutes of signup: deliver what was promised, set expectations
  - id: msg-2-value          # day 2 to 3: a useful, concrete thing, build trust
  - id: msg-3-proof          # day 5 to 7: social proof or a proof point
  - id: msg-4-soft-offer     # day 7 to 14: a soft, empowering offer
  - id: msg-5-deeper         # day 7 to 14: a path to go deeper
  - id: msg-6-final          # optional final touch, only if the brief gives a reason
# cadence every 2 to 3 days, never daily; each id binds to a QA-passed copy variant
```

## Success metric

```
success_metric (ONBOARDING): activation rate, how many reach the defined milestone (first lesson, Skill Path step, first Masterclass play), not open or click rate
success_metric (WELCOME): first conversion (the defined first action or purchase), not open or click rate alone
```

## Audience size

```
audience_size: resolve at send from live owned-audience data
```

## send_on_approval (one plain sentence)

```
send_on_approval: "Sends a 3-message Arabic onboarding flow to new signups over [window from brief]."
```

## Suppression (from segmentation-logic)

```
suppression: unsubscribed, hard-bounced (and paying where applicable)
```

## Illustrative example (Arabic, replace before use, copy comes from the copy-package)

```
headline:  رحلتك بدأت
body:      خطوة واحدة اليوم تبني مهارة تبقى معك.
cta:       ابدأ درسك الاول
```

## Open items

- Platform not confirmed: design proceeds, send wiring is blocked. The package is design-only
  and not-sendable until the email or WhatsApp platform is named and approved.
- Audience size: resolve at send.

## Guardrails check before handing up

- Every message references a QA-passed copy variant by id. No free copy here.
- No invented offer, price, Skill Path title, or instructor name.
- Suppression is stated: no unsubscribe or hard bounce receives the flow.
- Western numerals only (0 to 9). No em dashes, no tatweel. Empowering, never deficit-framed.
- Package marked not-sendable until the platform is confirmed.

---
name: promo-sequence
description: Build the ordered promotion or occasion email sequence for stream 7, a dated multi-instructor or catalog offer with an escalating-urgency ladder. Use to sequence a sale, a seasonal or occasion campaign, a Skill Path launch, or a catalog discount across an owned segment, each message bound to a QA-passed copy variant by id with its trigger, segment, and channel. Triggers on "build the promo sequence," "the sale emails," "the occasion campaign," "the seasonal flow," "the Skill Path launch emails," "the discount sequence." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Promotion sequence (stream 7 sub-skill)

Sequences a dated promotion: a multi-instructor, Skill Path, or catalog offer that runs inside a
defined window, by email, behind the human gate. It is the PROMOTION pattern in
`skills/07-lifecycle-messaging/templates/sequence-standards.md`. It does not write copy. Each
message references a QA-passed `copy-package` variant by id, by segment and language, and each
message is a multi-instructor email built on the angle method in
`context/profiles/maharat/multi-instructor-angles.md`. It runs on the audience and branches fixed by
`segmentation-logic`. It fills the `flow` field of the `lifecycle-package`.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send.

## When to use

- A brief defines a promotion or occasion window (a sale, a seasonal moment, a Skill Path launch,
  a catalog discount) with an offer, a discount or price, and start and end dates.
- The audience is any owned segment named in the brief, often non-payers, sometimes the wider
  emailable base.

## Inputs

- The segmentation-logic block: entry trigger (window open), segments, branches, suppression.
- The QA-passed `copy-package`: the multi-instructor email variants and subject lines, by id.
- The active `briefs/` file: the promotion window (start and end dates), the offer, the discount or
  price, the occasion, and the instructor or Skill Path lineup.
- `context/profiles/maharat/multi-instructor-angles.md`: the angle method each email is built on.
- The platform decision for sending (OPEN ITEM until the email and WhatsApp platform is named).
  Design proceeds; send wiring does not.

If the window, the offer, or the dates are not in the brief, stop. The sequence does not invent a
discount, a deadline, an occasion, a Skill Path title, or an instructor.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the needed
   variant ids present. If incomplete, return it.
2. Order the messages on the escalating-urgency ladder (confirm count and dates in the brief):
   - Message 1, announce, on the window open: the occasion or theme, the offer made plain, the
     umbrella outcome, the lineup as a LessonCardGrid, one primary CTA.
   - Message 2, the offer, mid-window: reinforce the value, refresh the angle or lineup, one CTA.
   - Message 3, ends tomorrow: the deadline first, the saving second.
   - Message 4, ends tonight: the last call, the access and deadline, one CTA.
   - Optional message 5, extended: only if the brief defines a real extension, never invented.
3. Bind each message to a QA-passed copy variant id by segment and language, and to its subject
   line ref. No message carries free copy written here.
4. Attach the trigger, segment, channel, and timing to each message, from segmentation-logic. The
   ladder is time-based off the window dates; layer behavior on top (a purchaser exits the
   sequence at once; non-openers get a subject retry, not a louder pitch).
5. Resolve audience size from live data at send time. Record the exact number in the package.
6. Write the `send_on_approval` sentence: one plain sentence of what the send does and to how many,
   for example "Sends a 4-email Arabic promotion sequence to the resolved non-payer segment across
   the [window from brief]."
7. Surface the platform open item. While unresolved, mark the package design-only and
   not-sendable. Hand the flow up for the `lifecycle-package`.

## Output

The ordered flow for the `flow` field of the `lifecycle-package`:

```
flow            ordered messages, each: id, step, trigger, segment, channel, copy_ref, subject_ref
window          start and end dates from the brief (never invented)
audience_size   resolve at send from live owned-audience data
send_on_approval one plain sentence of what the send does and to how many
suppression     paying contacts for the promoted product, unsubscribed, hard-bounced, already-converted
```

See `templates/promo-sequence.md`.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for the flow structure and the rules.
- Each referenced copy variant has passed the gate stack: skill eval, `arabic-copy-qa` or
  `english-copy-qa` by language, `brand-qa-reviewer`, per `runtime/verification.md`.
- A multi-instructor email multiplies the instructor gate: every named instructor is
  catalog-status-confirmed and every credential page-cleared, or that card is dropped. See
  `runtime/verification.md`.
- The human gate for the send. Approval is per send. Silence is not approval.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy variant
  by id.
- The window, offer, discount, dates, occasion, Skill Path title, and instructor lineup trace
  exactly to the brief and context. Nothing invented, no manufactured urgency or extension.
- Each email is a multi-instructor email per `context/profiles/maharat/multi-instructor-angles.md`: one reader
  outcome as the umbrella, one primary CTA, per-card links as quiet secondaries.
- Suppression is correct: no paying contact for the promoted product, no unsubscribe, no hard
  bounce, and no already-converted contact receives the rest of the sequence.
- Block on the platform open item before wiring the send. The package is not-sendable until the
  platform is confirmed and approved.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed. No accreditation
  implication.

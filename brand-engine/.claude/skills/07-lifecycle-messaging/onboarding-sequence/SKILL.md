---
name: onboarding-sequence
description: Build the onboarding flow for new signups in stream 7, a reusable flow shape. Use to sequence the welcome and activation messages that turn a new signup into an active user, each message bound to a QA-passed copy variant by id with its trigger, segment, and channel. Triggers on "the onboarding emails," "the welcome sequence," "activate new signups," "the new-user flow." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Onboarding sequence (stream 7 sub-skill)

Sequences the onboarding flow for new signups: a welcome that earns the read, a first useful
step, and an activation nudge, in a reusable shape any campaign can fill. It does not write
copy. Each message references a QA-passed `copy-package` variant by id, by segment and
language. It runs on the audience and branches fixed by `segmentation-logic`. It fills the
`flow` field of the `lifecycle-package`.

This sub-skill carries two related patterns from
`skills/07-lifecycle-messaging/templates/sequence-standards.md`: the WELCOME pattern (a new
subscriber, objective relationship and first conversion) and the ONBOARDING / activation
pattern (a new signup or free-trial user, objective activation to the first value milestone).
Select by the brief's audience and objective. The two share the instant first touch and the
morning-send habit; they differ in objective and success metric.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send. Follows
`sops/07-lifecycle-nonpayer-email.md` for the gate, suppression, and platform discipline.

## When to use

- A new signup needs a welcome and activation flow.
- The orchestrator dispatches a lifecycle onboarding flow per `runtime/stream-ownership.md`.

## Inputs

- The segmentation-logic block: entry trigger (new signup), segments, branches, timing,
  suppression.
- The QA-passed `copy-package`: Arabic onboarding body variants and subject lines, by id.
- The active `briefs/` file: what the new user should reach first, schedule, send window.
- The platform decision for sending (OPEN ITEM until the email and WhatsApp platform is
  named). Design proceeds; send wiring does not.

If the copy-package is not yet qa-passed, stop. The flow does not invent copy to fill a gap.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the
   needed variant ids present. If incomplete, return it.
2. Order the messages, a reusable shape (confirm cadence in the brief). Pick the pattern by
   the brief's audience and objective:

   WELCOME pattern (new subscriber, build the relationship and earn a first conversion): 5 to
   6 emails, cadence every 2 to 3 days, never daily. This is the highest-engagement window, so
   open rates run high; do not waste email 1 on a hard pitch.
   - Email 1, deliver and set expectations: deliver what was promised at signup, say what is
     coming and how often. Sent within 5 minutes of signup.
   - Email 2, value and trust: a useful, concrete thing. Day 2 to 3.
   - Email 3, proof: social proof or a proof point. Day 5 to 7.
   - Emails 4 to 5, soft offer and deeper engagement: a soft, empowering offer and a path to
     go deeper. Day 7 to 14.
   - Email 6, optional final touch: a last, light touch only if the brief gives a reason.

   ONBOARDING / activation pattern (new signup or free-trial user, reach the first value
   milestone). Anchor on 5 types, scaled to the window: welcome, usage tips, sales touch,
   usage review, expiry warning.
   - Message 1, welcome: confirm the signup and lead with what the user can build. One CTA
     to a first concrete step. Empowering, no pressure. Sent instantly.
   - Message 2, usage tips: how to get the first value, a single useful action (start one
     lesson, open one guide). Reinforce the angle, keep it short.
   - Message 3, sales touch: a contextual, empowering nudge toward the paid value.
   - Message 4, usage review: reflect progress, point at the next step.
   - Message 5, expiry warning: for a trial, a clear, non-pushy heads-up before the window
     closes.
   - Activation branch: branch on whether the first step happened. Activated users get a
     next step; not-yet-activated users get a gentle retry, not a louder pitch.

   Scale the onboarding count to the window: a 7-day trial gets a compressed 5-email
   sequence, a 14-day window gets 7, a 30-day window gets 8 to 10 over 2 to 3 weeks. The
   general band is 5 to 8 emails over 7 to 14 days, scaled to the window.

   Time-based vs behavior-triggered layering: build a time-based foundation every new user
   gets (for example, the setup guide on day 1 is time-based), then layer behavior-triggered
   emails on top (if setup is not done by day 3, trigger a help email). The foundation is
   universal; the triggers fire on what the user did or did not do.

   Send timing: the welcome or first touch is instant. Morning local sends, roughly 8 AM to
   10 AM, tend to perform best for the rest of the arc.
3. Bind each message to a QA-passed copy variant id by segment and language, and to its
   subject line ref. No message carries free copy written here.
4. Attach the trigger, segment, channel, and timing to each message, from segmentation-logic.
5. Resolve audience size from live data at send time. Record the exact number in the package.
6. Write the `send_on_approval` sentence: one plain sentence of what the send does and to how
   many.
7. Surface the platform open item. While unresolved, mark the package design-only and
   not-sendable. Hand the flow up for the `lifecycle-package`.

## Output

The ordered flow for the `flow` field of the `lifecycle-package`:

```
flow            ordered messages, each: id, trigger, segment, channel, copy_ref, subject_ref
audience_size   resolve at send from live data
send_on_approval one plain sentence of what the send does and to how many
suppression     paying-where-applicable, unsubscribed, hard-bounced (from segmentation-logic)
```

See `templates/onboarding-sequence.md`.

## Success metric

For the ONBOARDING / activation pattern the success metric is the activation rate, how many
reach the defined milestone (completing a first lesson, finishing a Skill Path step, or a
first Masterclass play). It is NOT open or click rate. For the WELCOME pattern the success
metric is the first conversion (the defined first action or purchase), not open or click rate
alone.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for the flow structure and the rules.
- Each referenced copy variant has passed the gate stack: skill eval, `arabic-copy-qa`,
  `brand-qa-reviewer`, per `runtime/verification.md`.
- The human gate for the send. Approval is per send. Silence is not approval.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy
  variant by id.
- Never invent an offer, price, Skill Path title, or instructor name. A missing variable is a
  stop-and-ask.
- Suppression is correct: no unsubscribe or hard bounce receives the flow.
- Block on the platform open item before wiring the send. The package is not-sendable until
  the platform is confirmed and approved.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed. No
  accreditation implication.

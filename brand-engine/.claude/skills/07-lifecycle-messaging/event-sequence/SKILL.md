---
name: event-sequence
description: Build the event and webinar email sequence for stream 7, the pre-event reminders and post-event follow-up that drive attendance then conversion. Use to sequence the messages around a live session, a Masterclass launch, or an event, each message bound to a QA-passed copy variant by id with its trigger, audience, and channel. Triggers on "webinar sequence," "event emails," "masterclass launch sequence," "registrant reminders," "replay follow-up," "event reminder cadence," "no-show follow-up." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Event and webinar sequence (stream 7 sub-skill)

Sequences the event sequence that moves registrants and attendees from registration to
attendance and then to conversion, by email, behind the human gate. It covers the pre-event
reminder cadence and the post-event follow-up, including the no-show branch and the
limited-time replay. It does not write copy. Each message references a QA-passed `copy-package`
variant by id, by audience and language. It runs on the audience and branches fixed by
`segmentation-logic`, and follows the EVENT pattern in
`skills/07-lifecycle-messaging/templates/sequence-standards.md`. It fills the `flow` field of
the `lifecycle-package`.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send. Follows
`sops/07-lifecycle-nonpayer-email.md` for gate, suppression, and platform discipline.

## When to use

- A campaign runs a live session, a Masterclass launch, or an event, and needs the registrant
  reminders and the post-event follow-up.
- The orchestrator dispatches an event or webinar sequence for the owned audience.
- The segmentation-logic block and the QA-passed copy variants are ready to be ordered.

## Inputs

- The segmentation-logic block: entry trigger (registration), audiences (registrant, attendee,
  no-show), engagement branches, timing, suppression.
- The QA-passed `copy-package`: Arabic event body variants and subject lines, by id, per
  audience.
- The active `briefs/` file: the event date and time, the access details, the offer (product,
  plan, price, promotion), the replay window, schedule, send window.
- The platform decision for sending (OPEN ITEM until the email and WhatsApp platform is named).
  Design proceeds; send wiring does not.

If the copy-package is not yet qa-passed, or the event date, offer, or replay window is not in
the brief, stop. The flow does not invent an event date, an offer, or a replay window to fill a
gap.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the needed
   variant ids present per audience. If incomplete, return it.
2. Order the PRE-event arc off the event date, time-based:
   - Announce, 2 to 4 weeks out.
   - Reminder, 1 to 2 weeks before.
   - Reminder, 1 to 2 days before.
   - Final reminder, 1 to 2 hours before: urgency and the access info.
3. Order the POST-event arc, branching on attended vs no-show:
   - Email 1, same day within about 3 hours: the replay plus one key insight.
   - Email 2, day 2 to 3: a value-add not covered live.
   - Email 3, day 4 to 5: a direct, specific offer, with the price and promotion exactly as the
     brief gives them. One CTA. Never invent a discount.
4. Set the no-show branch: a registrant who did not attend gets one main CTA, watch the replay.
   One CTA, not a stacked pitch.
5. Set the replay scarcity: a limited-time replay window that expires, to drive action. The
   window comes from the brief, never invented.
6. Bind each message to a QA-passed copy variant id by audience and language, and to its subject
   line ref. No message carries free copy written here.
7. Attach the trigger, audience, channel, and timing to each message, from segmentation-logic.
8. Resolve audience size from live data at send time. Record the exact number in the package.
9. Write the `send_on_approval` sentence: one plain sentence of what the send does and to how
   many, for example "Sends a 4-reminder pre-event arc and a 3-email post-event follow-up to
   registrants for the [event from brief], starting [date from brief]."
10. Surface the platform open item. While unresolved, mark the package design-only and
    not-sendable. Hand the flow up for the `lifecycle-package`.

## Output

The ordered flow for the `flow` field of the `lifecycle-package`:

```
flow            ordered messages (pre and post), each: id, phase, trigger, audience, channel, copy_ref, subject_ref
audience_size   resolve at send from live owned-audience data
send_on_approval one plain sentence of what the send does and to how many
suppression     paying-where-applicable, unsubscribed, hard-bounced (from segmentation-logic)
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See `templates/event-sequence.md`.

## How this connects to the contract and gates

- Consumes: the segmentation-logic block and the QA-passed `copy-package` (stream 4), plus the
  event date, access details, offer, and replay window from the brief.
- Produces: the `flow` field of the `lifecycle-package` (stream 7 -> human gate), per
  `runtime/handoff-contract.md`. Follows the EVENT pattern in
  `skills/07-lifecycle-messaging/templates/sequence-standards.md`.
- Gate before advance: skill eval (this file's `evals/evals.json`), then `arabic-copy-qa` on all
  Arabic copy, then `brand-qa-reviewer`, then `compliance-privacy-check` for the send and
  suppression, then the human gate for the send, per `runtime/verification.md`. Approval is per
  send. Silence is not approval.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy
  variant by id.
- Pre-event reminders and post-event follow-up are both present. The no-show branch carries one
  main CTA, watch the replay. The replay is a limited-time window that expires.
- The success metric is attendance, then conversion, never a vanity metric (not open or click
  rate alone).
- One clear CTA per email. The offer, event date, access details, replay window, price, and
  promotion trace exactly to the brief. No invented event date, discount, replay window, Skill
  Path title, or instructor name.
- Suppression is correct: no paying contact (where applicable), unsubscribe, or hard bounce
  receives the flow.
- Block on the platform open item before wiring the send. The package is not-sendable until the
  platform is confirmed and approved.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed. No accreditation
  implication.

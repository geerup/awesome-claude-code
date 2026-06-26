---
name: nonpayer-email-flow
description: Build the ordered non-payer email flow for stream 7, the first build. Use to sequence the messages that move owned non-paying contacts toward a first purchase, each message bound to a QA-passed copy variant by id with its trigger, segment, and channel. Triggers on "build the non-payer flow," "the non-payer sequence," "order the lifecycle emails," "the drip to non-payers." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Non-payer email flow (stream 7 sub-skill)

The deepest sub-skill and the first build. Sequences the ordered non-payer email flow that
moves owned non-paying contacts toward a first purchase or a subscription, by email, behind
the human gate. It does not write copy. Each message references a QA-passed `copy-package`
variant by id, by segment and language. It runs on the audience and branches fixed by
`segmentation-logic`. It fills the `flow` field of the `lifecycle-package`.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send. Follows
`sops/07-lifecycle-nonpayer-email.md`.

## When to use

- A brief with `entry_point: owned audience` targets the non-paying email contacts. The
  active first-build brief is `briefs/2026-06-nonpayer-email.md`.
- The segmentation logic and the QA-passed copy variants are ready to be ordered.

## Inputs

- The segmentation-logic block: entry trigger, segments, branches, timing, suppression.
- The QA-passed `copy-package`: Arabic email body variants and subject lines, by id.
- The active `briefs/` file: offer (product, plan, price, promotion), schedule, send window.
- The platform decision for sending (OPEN ITEM until the email and WhatsApp platform is
  named). Design proceeds; send wiring does not.

If the copy-package is not yet qa-passed, or the offer is not in the brief, stop. The flow
does not invent copy or an offer to fill a gap.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the
   needed variant ids present. If incomplete, return it.
2. Order the messages. A proposed shape (confirm cadence in the brief):
   - Message 1, entry: lead with what the reader can build. The angle, one clear CTA. No
     pressure, no deficit framing.
   - Message 2, value: a concrete proof point or a useful free thing (a guide, a taste of a
     Masterclass). Reinforce the angle.
   - Message 3, offer: the offer made plain, with the price and promotion exactly as the
     brief gives them. One CTA. Never invent a discount.
   - Message 4, branch on engagement: openers and clickers get a nudge toward the offer;
     non-openers get a subject-line retry, not a louder pitch.
   - Optional message 5, last call: only if the brief defines a window and a real reason.
3. Bind each message to a QA-passed copy variant id by segment and language, and to its
   subject line ref. No message carries free copy written here.
4. Attach the trigger, segment, channel, and timing to each message, from segmentation-logic.
5. Resolve audience size from live data at send time. Record the exact number in the package;
   the planning estimate is about 18,000 non-payers.
6. Write the `send_on_approval` sentence: one plain sentence of what the send does and to how
   many, for example "Sends a 4-message Arabic email flow to about 18,000 non-paying contacts
   over 2 weeks, starting [date from brief]."
7. Surface the platform open item. While unresolved, mark the package design-only and
   not-sendable. Hand the flow up for the `lifecycle-package`.

## Output

The ordered flow for the `flow` field of the `lifecycle-package`:

```
flow            ordered messages, each: id, trigger, segment, channel, copy_ref, subject_ref
audience_size   resolve at send (planning estimate about 18,000 non-payers)
send_on_approval one plain sentence of what the send does and to how many
suppression     paying contacts, unsubscribed, hard-bounced (from segmentation-logic)
```

See `templates/nonpayer-email-flow.md`.

## Verification gates

- Skill eval (this file's `evals/evals.json`) for the flow structure and the rules.
- Each referenced copy variant has passed the gate stack: skill eval, `arabic-copy-qa`,
  `brand-qa-reviewer`, per `runtime/verification.md`.
- The human gate for the send. Approval is per send. Silence is not approval.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy
  variant by id.
- The offer in the referenced copy traces exactly to the brief. No invented price, promotion,
  Skill Path title, or instructor name.
- Suppression is correct: no paying contact, unsubscribe, or hard bounce receives the flow.
- Block on the platform open item before wiring the send. The package is not-sendable until
  the platform is confirmed and approved.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed. No
  accreditation implication.

---
name: winback-flow
description: Build the winback and reactivation flow for stream 7, the flow that re-engages lapsed and inactive owned contacts. Use to sequence a reactivation series for contacts who have gone quiet, segmented by recency, frequency, and value, each message bound to a QA-passed copy variant by id with its trigger, segment, and channel. Triggers on "the winback flow," "reactivation sequence," "re-engage lapsed contacts," "win back inactive users," "the lapsed-customer flow." Sub-skill of 07-lifecycle-messaging, owned by lifecycle-architect.
---

# Winback and reactivation flow (stream 7 sub-skill)

Sequences the ordered winback flow that re-engages owned contacts who have gone inactive,
moving lapsed contacts back toward a first or renewed purchase or subscription, by email,
behind the human gate. The lapsed base is a real channel, not dead weight, so this flow
treats it with the same care as the non-payer flow. It does not write copy. Each message
references a QA-passed `copy-package` variant by id, by segment and language. It runs on the
audience, the recency segments, and the suppression set fixed by `segmentation-logic`,
including the sunset rule and engagement-decay suppression. It fills the `flow` field of the
`lifecycle-package`.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send. Follows
`sops/07-lifecycle-nonpayer-email.md` for gate discipline.

## When to use

- A campaign needs to re-engage owned contacts who have lapsed: no open, no click, or no
  purchase for a defined window, while still consenting and not yet suppressed.
- The orchestrator dispatches a reactivation flow for the owned audience.
- The segmentation-logic block, including recency segments and the sunset rule, and the
  QA-passed copy variants are ready to be ordered.

## Inputs

- The segmentation-logic block: entry trigger, recency segments (RFM-style), engagement
  branches, inter-message timing, the suppression set, and the sunset rule.
- The QA-passed `copy-package`: Arabic email body variants and subject lines, by id, per
  recency segment.
- The active `briefs/` file: offer (product, plan, price, promotion), schedule, send window,
  inactivity thresholds if the brief defines them.
- The owned-audience data source, for resolving recency segments and audience size at send.
- The platform decision for sending (OPEN ITEM until the email and WhatsApp platform is
  named). Design proceeds; send wiring does not.

If the copy-package is not yet qa-passed, or the offer is not in the brief, stop. The flow
does not invent copy, an offer, a discount, or an inactivity threshold to fill a gap.

## Steps

1. Validate the copy-package envelope: right campaign_id, status at least qa-passed, the
   needed variant ids present per segment. If incomplete, return it.
2. Take the recency segments from segmentation-logic. Segment lapsed contacts by recency,
   frequency, and value (RFM-style), not all the same. Typical recency cuts map to inactivity
   triggers at 30, 60, and 90 days since the last open, click, or purchase. Use the data; do
   not invent segment sizes or thresholds.
3. Order the messages, a 3 to 5 message reactivation sequence (confirm cadence in the brief):
   - Message 1, reconnect: lead with what the reader can still build. Warm, empowering, one
     clear CTA. No guilt, no deficit framing.
   - Message 2, relevance: a concrete proof point or a useful free thing tied to the segment's
     prior interest. Reinforce the angle.
   - Message 3, offer: the offer made plain, with the price and promotion exactly as the brief
     gives them. One CTA. Never invent a discount or an incentive.
   - Message 4, branch on engagement: re-engaged openers and clickers get a nudge toward the
     offer; the still-silent get a subject-line retry, not a louder pitch.
   - Optional message 5, last call: only if the brief defines a window and a real reason. A
     contact who stays silent past this flow enters the sunset rule in segmentation-logic.
4. Bind each message to a QA-passed copy variant id by recency segment and language, and to
   its subject line ref. No message carries free copy written here.
5. Attach the trigger, segment, channel, and timing to each message, from segmentation-logic.
6. Apply suppression and the sunset step. Exclude paying contacts, unsubscribed, and
   hard-bounced. Hand any contact who completes the flow without re-engaging to the sunset
   rule, a 1 to 3 message sunset then suppress, so the flow protects deliverability and keeps
   the list to consenting contacts. Suppression is not optional.
7. Resolve audience size from live data at send time. Record the exact number in the package;
   recency segment sizes resolve at send and are never invented.
8. Write the `send_on_approval` sentence: one plain sentence of what the send does and to how
   many, for example "Sends a 4-message Arabic reactivation flow to lapsed contacts inactive
   for 30 days or more, resolved at send, over 3 weeks, starting [date from brief]."
9. Surface the platform open item. While unresolved, mark the package design-only and
   not-sendable. Hand the flow up for the `lifecycle-package`.

## Output

The ordered flow for the `flow` field of the `lifecycle-package`:

```
flow            ordered messages, each: id, trigger, segment, channel, copy_ref, subject_ref
audience_size   resolve at send from live owned-audience data (recency segments resolved at send)
send_on_approval one plain sentence of what the send does and to how many
suppression     paying contacts, unsubscribed, hard-bounced, plus the sunset-then-suppress step
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See `templates/winback-flow.md`.

## How this connects to the contract and gates

- Consumes: the segmentation-logic block (including recency segments and the sunset rule) and
  the QA-passed `copy-package` (stream 4).
- Produces: the `flow` field of the `lifecycle-package` (stream 7 -> human gate), as defined
  in `runtime/handoff-contract.md`.
- Gate before advance: skill eval (this file's `evals/evals.json`), then `arabic-copy-qa` on
  all Arabic copy, then `brand-qa-reviewer`, then `compliance-privacy-check` for the send and
  suppression, then the human gate for the send, per `runtime/verification.md`. Approval is
  per send. Silence is not approval.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy
  variant by id.
- The offer in the referenced copy traces exactly to the brief. No invented price, promotion,
  discount, incentive, inactivity threshold, Skill Path title, or instructor name.
- Suppression is correct: no paying contact, unsubscribe, or hard bounce receives the flow.
  Contacts who stay silent through the flow enter the sunset-then-suppress step.
- Recency segment sizes resolve from live data at send. Never invent a size or a threshold.
- Block on the platform open item before wiring the send. The package is not-sendable until
  the platform is confirmed and approved.
- No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed. No
  accreditation implication.

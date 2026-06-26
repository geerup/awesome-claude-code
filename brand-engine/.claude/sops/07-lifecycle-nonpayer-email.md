# SOP 07: Lifecycle, the non-payer email flow

Stream 7. Owner: lifecycle-architect. Mode: reasoning for the design, gated for the send.
This is the deepest-built stream and the first build. It moves owned non-paying contacts
toward a first purchase or a subscription, by email, behind the human gate.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Where this SOP sits in the pattern library

This SOP is the non-payer pattern: an owned, registered, never-purchased audience, objective a
first purchase or subscription. It is one of five lifecycle sequence patterns. The full pattern
library (welcome, onboarding and activation, event and webinar, non-payer, winback) lives in
`skills/07-lifecycle-messaging/templates/sequence-standards.md`, selected by the brief's
audience and objective. Use that selector to confirm this is the right pattern before building.
If the audience is a new subscriber, a new signup or trial, an event registrant, or a lapsed
contact, route to the matching pattern there instead.

---

## Trigger

A brief with `entry_point: owned audience` targeting the non-paying email contacts. The
active first-build brief is `briefs/2026-06-nonpayer-email.md`.

## Inputs

- The `strategy-artifact` from strategy-lead: segments of the non-payers, the angle, offer
  framing, success metric.
- The `copy-package` from copywriter-ar: QA-passed Arabic email copy and subject lines.
- The brief: offer (product, plan, price, promotion), schedule, send window, suppression.
- The platform decision (OPEN ITEM until the email and WhatsApp platform is named). Design
  proceeds without it; send wiring does not.

## Steps

1. Resolve segments. Take the strategy-artifact segments of the about 18,000 non-payers.
   Typical cuts: never-engaged vs lapsed-engaged, prior single-class interest vs none,
   recency of last open. Do not invent segment sizes; use the data, flag where live data is
   needed at send time.
2. Set suppression. Exclude all paying contacts (about 5,000), anyone unsubscribed, and
   hard-bounced addresses. Confirm the suppression source at build. Suppression is not
   optional and is stated explicitly in the package.
3. Design the flow. A proposed shape (confirm cadence in the brief):
   - Message 1, entry: lead with what the reader can build. The angle, one clear CTA. No
     pressure, no deficit framing.
   - Message 2, value: a concrete proof point or a useful free thing (a guide, a taste of a
     Masterclass). Reinforce the angle.
   - Message 3, offer: the offer made plain, with the price and promotion exactly as the
     brief gives them. One CTA. Never invent a discount.
   - Message 4, branch on engagement: openers and clickers get a nudge toward the offer;
     non-openers get a subject-line retry, not a louder pitch.
   - Optional message 5, last call: only if the brief defines a window and a real reason.
4. Map each message to a QA-passed copy variant. This SOP does not write copy; it sequences
   it. Each message references a `copy-package` variant id by segment and language.
5. Define triggers and timing. Entry trigger, inter-message delays, and the engagement
   branch conditions. Keep timing in the brief's send window.
6. Resolve audience size from live data at send time. Record the exact number in the package.
7. Assemble the `lifecycle-package` and stop at the human gate.

## Output

A `lifecycle-package` (see `runtime/handoff-contract.md`):
- flow: ordered messages, each with trigger, audience segment, channel, copy variant ref.
- audience_size: resolved from live data (about 18,000 as the planning estimate).
- send_on_approval: one plain sentence, for example "This sends a 4-message flow to about
  18,000 non-paying contacts over 2 weeks, starting [date]."
- suppression: who is excluded and why.

## Quality bar

- Every message's copy is QA-passed: skill eval, then arabic-copy-qa, then brand-qa-reviewer.
- The offer in the copy traces exactly to the brief. No invented price, promotion, title, or
  instructor name.
- RTL renders. No em dashes, no tatweel, Western numerals. Empowering, never deficit-framed.
- Suppression is correct: no paying contact, unsubscribe, or hard bounce receives the flow.
- The platform open item is surfaced. If unresolved, the package is design-only and clearly
  marked not-sendable until the platform is confirmed.

## Example output (shape, not real copy)

```
flow:
  - id: msg-1-entry
    trigger: enters non-payer flow
    segment: lapsed-engaged
    channel: email
    copy_ref: copy-package/variant-ar-lapsed-01
    subject_ref: subject-lines/primary-ar-01
  - id: msg-3-offer
    trigger: 4 days after msg-1, opened or clicked
    segment: lapsed-engaged
    channel: email
    copy_ref: copy-package/variant-ar-lapsed-offer
    note: price and promotion from brief; ASSUMPTION flags must be resolved before send
audience_size: resolve at send (planning estimate ~18,000)
send_on_approval: "Sends a 4-message Arabic email flow to the non-paying segment over 2 weeks."
suppression: paying contacts, unsubscribed, hard-bounced
```

## Review owner

Ahmed, at the human gate. Approval is per send. Silence is not approval. The gate package
shows the quality-gate results and every remaining ASSUMPTION and open item, so approval is
informed. On approval, lifecycle-architect performs exactly the approved send, nothing more.

---
name: 07-lifecycle-messaging
description: Hub for stream 7 lifecycle messaging, owned by lifecycle-architect, reasoning for the design and gated for the send. Use to design the flows that move owned contacts toward conversion. Selects the sequence pattern by the brief's audience and objective, then routes to segmentation-logic, nonpayer-email-flow, onboarding-sequence (welcome and activation), event-sequence (webinar and event), and winback-flow, and assembles the lifecycle-package that the human gate consumes. Triggers on "design the email flow," "build the non-payer sequence," "lifecycle messaging," "the onboarding emails," "the welcome sequence," "the webinar sequence," "event emails," "offer launch sequence," "registrant reminders," "replay follow-up," "the winback flow," "reactivate lapsed contacts," "the drip," "the promo sequence," "the sale emails," "the seasonal campaign," "the offer launch emails," "the occasion campaign."
---

# 07 Lifecycle Messaging (hub)

Stream 7. Owns the messaging that works the owned audience: the non-payer email flow (the
first build), the onboarding sequence for new signups, the winback and reactivation flow for
lapsed contacts, and the segmentation logic behind them. This hub does not write copy and
does not send. It validates inputs, routes to the right sub-skill, and assembles the
`lifecycle-package` defined in
`runtime/handoff-contract.md`. The flow sequences QA-passed copy variants by id; it never
writes the copy.

Owner: lifecycle-architect. Mode: reasoning for design, gated for the send. Follows
`sops/07-lifecycle-nonpayer-email.md`. This is the deepest-built stream and owns the first
build.

## When to use

- A brief with `entry_point: owned audience` targets the non-paying email contacts. The
  active first-build brief is `briefs/2026-06-nonpayer-email.md`.
- New subscribers need a welcome sequence; new signups need an onboarding sequence.
- A live session, an offer launch, or an event needs registrant reminders and a replay
  follow-up (the event-sequence).
- A brief defines a promotion or occasion window (a sale, a seasonal moment, an offer launch,
  a catalog discount) for a multi-offer promotion (the promo-sequence).
- The orchestrator dispatches stream 7 (per `runtime/stream-ownership.md`).

## Selector: pick the pattern by audience and objective

Route every lifecycle request through this selector first. The pattern is chosen by the
brief's audience and objective, not by habit. The full standards each pattern follows live in
`skills/07-lifecycle-messaging/templates/sequence-standards.md` (the message arc, email count,
cadence and timing, time-based vs behavior-triggered layering, the success metric, the branch
logic, and the suppression and sunset note). When the audience or objective is not in the
brief or strategy-artifact, stop and ask. Do not assume one.

| Audience (who) | Objective (why) | Pattern | Sub-skill |
|---|---|---|---|
| New subscriber or owned contact, just joined the list | Build the relationship and earn a first conversion | WELCOME | `onboarding-sequence` |
| New signup or free-trial user, new learner | Activation, reaching the first value milestone | ONBOARDING / activation | `onboarding-sequence` |
| Registrant or attendee for a live session, offer launch, or event | Attendance, then conversion | EVENT / webinar | `event-sequence` |
| Owned non-payer, registered but never purchased | First purchase or subscription | NON-PAYER | `nonpayer-email-flow` |
| Lapsed or dormant contact, gone quiet for a defined window | Win back, re-engage, then convert | WINBACK | `winback-flow` |
| Any owned segment, inside a defined promotion or occasion window | Purchases on a multi-offer, service, or catalog offer before the window closes | PROMOTION | `promo-sequence` |

## Sub-skills (routing)

- `segmentation-logic`: the trigger and branch logic for who gets which message when, the
  engagement branches, and suppression. Use first; it defines the audience the flow runs on.
- `nonpayer-email-flow`: the ordered non-payer email flow, each message with trigger,
  segment, channel, and a copy variant ref. The deepest sub-skill and the first build. Use
  to build the non-payer sequence.
- `onboarding-sequence`: the welcome flow (new subscriber, relationship and first conversion)
  and the onboarding / activation flow (new signup or trial, activation to the first
  milestone), a reusable flow shape. Use for the welcome and activation messages after a new
  signup or subscribe.
- `event-sequence`: the event and webinar sequence for registrants and attendees, the
  pre-event reminder cadence and the post-event follow-up with the no-show branch and the
  limited-time replay. Use for a live session, an offer launch, or an event.
- `winback-flow`: the winback and reactivation flow for owned contacts who have gone inactive.
  Recency, frequency, and value (RFM-style) segments, inactivity triggers at 30, 60, and 90
  days, a 3 to 5 message reactivation sequence, then the sunset-then-suppress step from
  segmentation-logic. Use to re-engage lapsed contacts.
- `promo-sequence`: the dated promotion or occasion sequence, a multi-offer, service, or
  catalog offer on the escalating-urgency ladder (announce, offer, ends tomorrow, ends tonight,
  optional extension). Each message is a multi-offer email per
  `context/profiles/maharat/multi-instructor-angles.md`. Use for a sale, a seasonal or occasion campaign, an
  offer launch, or a catalog discount. Selected by a window in the brief, not a lifecycle stage.

Route: select the pattern by audience and objective per the selector and
`templates/sequence-standards.md`, run segmentation first to fix the audience, suppression, and
the sunset rule, then the flow sub-skill that matches the brief (nonpayer-email-flow,
onboarding-sequence, event-sequence, winback-flow, or promo-sequence). All feed the same
`lifecycle-package`, and all follow the standards in `templates/sequence-standards.md`.

## Inputs

- The `strategy-artifact` (stream 2): segments of the audience, the angle, offer framing,
  success metric.
- The QA-passed `copy-package` (stream 4): English email copy and subject lines (Arabic only
  when a brief sets it in scope), by variant id.
- The active `briefs/` file: offer, schedule, send window, suppression rules.
- The send path (the solo email path is Gmail drafts; any other channel is an OPEN ITEM until
  named). Design proceeds without it; send wiring does not.

If a needed variable is absent from both brief and context, stop and ask. Do not fill the
gap with an invented value.

## Steps

1. Validate the incoming envelope: right campaign_id, status at least qa-passed on the
   copy-package, required strategy fields present, open_items read. If incomplete, return it.
2. Select the sequence pattern by the brief's audience and objective, per the selector above
   and `templates/sequence-standards.md`. If the audience or objective is absent, stop and ask.
3. Route to `segmentation-logic` to resolve segments, branches, and suppression.
4. Route to the matching flow sub-skill (`nonpayer-email-flow`, `onboarding-sequence`,
   `event-sequence`, or `winback-flow`) to order the messages, each bound to a QA-passed copy
   variant id by segment and language, following the pattern's standards.
5. Resolve audience size from live data at send time. Record the exact number from the owned
   audience; do not assume a count.
6. Surface the send-path open item for any channel beyond Gmail drafts. While unresolved, mark
   the lifecycle-package design-only and not-sendable. Carry the open item forward; never
   silently close it.
7. Assemble the `lifecycle-package` and stop at the human gate.

## Output: the lifecycle-package

The body shape, exactly as `runtime/handoff-contract.md` defines it:

```
flow              ordered messages, each with trigger, audience, channel, copy variant ref
audience_size     resolved from owned-audience data (the exact non-payer count)
send_on_approval  one plain sentence of what the send does and to how many
suppression       who is excluded and why (already paying, unsubscribed, etc.)
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs).

## How this connects to the contract and gates

- Consumes: `strategy-artifact` (stream 2), `copy-package` (stream 4).
- Produces: `lifecycle-package` (stream 7 -> human gate).
- Gate before advance: skill eval, then `english-copy-qa` on all English copy (`arabic-copy-qa`
  when Arabic is in scope), then `brand-qa-reviewer`, then the human gate for the send, per
  `runtime/verification.md`.

## Hard rules

- The flow sequences copy; it never writes copy. Every message references a QA-passed copy
  variant by id.
- Block on the send-path open item before wiring any channel beyond Gmail drafts. The package
  is not-sendable until the send path is confirmed and approved.
- Suppression is not optional: no paying contact, unsubscribe, or hard bounce receives a flow.
- Never invent the offer, price, schedule, service title, or subject name.
- The send is one gated action. Approval is per send. Silence is not approval.
- No em dashes, empowering framing, never imply a credential or accreditation you do not hold.
  When Arabic is in scope: no tatweel, Western numerals.

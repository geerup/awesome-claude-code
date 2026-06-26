---
name: email-sequence-build
description: Assemble a QA-passed lifecycle flow into the sending platform structure for stream 5, staged and not sending. Use when an approved lifecycle-package and email copy must become messages, triggers, delays, audience, and suppression in the platform, assembled not sent. Triggers on "build the email sequence," "stage the flow," "assemble the lifecycle emails," "load the sequence into the platform." Sub-skill of 05-build-launch, owned by paid-build-engineer, execution mode and gated.
---

# Email Sequence Build (stream 5 sub-skill)

Assembles a QA-passed lifecycle flow and its email copy into the sending platform structure:
messages, triggers, delays, audience, and suppression. It is assembled, never sent. Going live
is a human-gate decision. This skill is blocked on the email and WhatsApp platform OPEN ITEM
until the platform is confirmed and approved.

Owner: paid-build-engineer. Mode: execution (gated).

## When to use

- A QA-passed `lifecycle-package` (stream 7) and `copy-package` (stream 4) need to be loaded
  into the sending platform structure.
- You need an assembled, not-sending sequence ready for the human gate.

## Inputs

- The QA-passed `lifecycle-package`: the ordered flow, audience_size, suppression.
- The QA-passed `copy-package`: the email variants and subject lines by id.
- The active `briefs/` file: the audience definition, schedule, and any send window.

If the lifecycle-package or copy-package is not qa-passed, return it. If the sending platform is
not confirmed and approved, stop: this is the blocking OPEN ITEM and the build does not proceed
on an assumed platform.

## What it assembles: any sequence pattern, faithfully

This build is pattern-agnostic. It assembles any sequence pattern defined in
`skills/07-lifecycle-messaging/templates/sequence-standards.md` (WELCOME, ONBOARDING, EVENT,
NON-PAYER, WINBACK) into the platform structure without changing its design. It does not redesign
the flow; it carries the lifecycle-package's design into the platform exactly as approved.

For every message in the pattern, the build carries through:
- the trigger, marked as time-based (a delay after the entry event or prior message) or
  behavior-triggered (a response to opened, clicked, started, completed, attended, lapsed, or a
  not-X), layered on the time-based foundation,
- the delay and cadence between messages (for example every 2 to 3 days in a welcome window,
  never daily, or the event pattern's tightening weeks-then-days-then-hours),
- the audience for the message and any branch,
- the suppression set (already paying, unsubscribed, hard-bounced, anyone the flow excludes).

The assembled structure must preserve the pattern's triggers and cadence as the lifecycle-package
defined them. The whole sequence is staged paused, not sending. The build never alters an
objective, a trigger, or a cadence to fit the platform; if a pattern element cannot be expressed
in the confirmed platform, that is an open item to flag, not a value to invent or drop.

## Steps

1. Confirm the sending platform is named, confirmed, and approved. If not, stop and flag the
   email and WhatsApp platform OPEN ITEM. Do not assume a platform.
2. Validate both package envelopes: right campaign_id, status at least qa-passed, required
   fields present. If incomplete, return.
3. Lay out the messages in order. Bind each message to a copy-package variant id and its paired
   subject line. No message carries free copy written here.
4. Set the trigger for each message from the lifecycle-package flow, marked time-based (a delay
   after the entry event or prior message) or behavior-triggered (on what the contact did or did
   not do), and carry the delay and cadence between messages exactly as the pattern defines them.
   Preserve the pattern's triggers and cadence; do not flatten a behavior branch into a fixed
   delay to fit the platform. Nothing fires on its own: the whole sequence is assembled paused.
5. Resolve the audience from the lifecycle-package and brief, and apply suppression: already
   paying, unsubscribed, anyone the flow excludes. No personal or sensitive data in any link.
6. Hand the assembled structure to the hub. The sequence is assembled, not sending. The human
   gate authorizes the send.

## Output

Fills the email-sequence portion of the `paid-launch-package` staged_structure and checklist
(see `runtime/handoff-contract.md`). The hub states send_on_approval and flips_live:

```
staged_structure  messages, triggers (time-based or behavior-triggered), delays and cadence,
                  audience, suppression, all preserving the source pattern (assembled, not sending)
checklist         platform confirmed, bindings resolved, pattern triggers and cadence preserved,
                  suppression set, links clean
```

Wrapped in the common envelope (campaign_id, produced_by, stream, status, qa, open_items,
brief_refs). See `templates/email-sequence-structure.md`.

## How it connects to the verification gates

- Skill eval (this file's `evals/evals.json`) for structure, the assembled-not-sending state,
  and the variant bindings.
- Operational verification per `runtime/verification.md`: bindings resolve, suppression is set,
  links are clean. A failing check blocks the package from the gate.
- `compliance-privacy-check` on suppression, consent, links, and the PDPL open item.
- The human gate is the only thing that authorizes the send.

## Hard rules

- Assembled, not sent. The build never sends and never schedules a live send on its own.
- Assemble the pattern as designed. Preserve every message's trigger (time-based or
  behavior-triggered), its delay and cadence, audience, and suppression from the
  sequence-standards pattern the lifecycle-package used. Never alter an objective, trigger, or
  cadence to fit the platform; a pattern element the platform cannot express is an open item.
- Blocked on the email and WhatsApp platform OPEN ITEM until the platform is confirmed and
  approved. Do not assume a platform.
- Every message binds to a copy-package variant id and a subject line. Copy is never invented
  here.
- Suppression is applied: already paying, unsubscribed, excluded. No personal or sensitive data
  in any link. Never imply accreditation.
- No em dashes, no tatweel, Western numerals only.

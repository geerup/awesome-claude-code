# Email set: targeting and send plan

How the Maharat instructor email set is targeted and sent. Sends happen in Ortto: the MCP
reads audiences and drafts assets, it cannot send. Building the journey, attaching the assets,
pointing at the audience, and pressing send are human actions in Ortto, which is the human gate.
This plan resolves the real audience, suppression, segmentation, and journey so the wiring in
Ortto is mechanical and the compliance checks are explicit.

Grounded in live Ortto data read 2026-06-18 (get_audiences, get_schema). Aggregate only, no
contact PII pulled. No em dashes, Western numerals.

## The real owned audience (Ortto, 2026-06-18)

| Audience | Emailable | Role |
|---|---|---|
| Created Account - NonPaying | 13,281 (14,925 total) | Primary nurture target |
| Subscribers | 24,673 | Full owned email base |
| TOFU List / MOFU List / BOFU List / SQLs List | 13,141 / 1,535 / 1,330 / 1,312 | Funnel-stage targeting |
| Newsletter Subscribers | 6,025 | Lighter intent |
| Accounts Created / Not Paid - Rahma | 238 | Per-instructor non-payer (precedent) |
| Unsubscribed | 3,891 | SUPPRESS |
| Bounced | 4,992 | SUPPRESS (hard bounce) |
| Internal Team / BOT | 24 / 0 | SUPPRESS |

Note: the real non-payer pool is about 13,300, not the brief's estimate of 18,000. Plan against
the real number. The "Not Paid - Rahma" audience proves per-instructor non-payer segments are an
established pattern here.

## Targeting fields (Ortto contact schema)

- Language: `str::language` (split AR vs EN, send the matching-language variant).
- Geo: `geo::country`, `geo::region`, plus `str:cm:original-country` (GCC, Saudi primary).
- Plan status: `bol:cm:paying` and `bol:cm:paidstatus` (identify non-payers, suppress payers),
  `str:cm:type-of-plan`, `sst::pids`, `int::ap` Amount paid, `bol:st:it` Is trial.
- Per instructor: `str:cm:classid` (classId, the class the contact engaged with), plus the
  class-updates form acts. The classId value per class is pulled from Ortto or the class data,
  not invented here.
- Account age and lifecycle: `dtz:cm:signedon` (account created), `dtz:cm:successfulpaymenton`,
  `dtz:cm:failedpaymenton`, `bol:cm:hasfailedpayment`.
- Behavior, for journey branches: Opened `act::o`, Clicked `act::c`, Received `act::r`,
  Sent `act::s`, Bounced `act::b`, Unsubscribed `act::u-all`, Email suppressed `act::es`,
  Engagement score `int::e`, Last seen and Last page fields for site activity.
- Consent and deliverability: `bol::p` Email permission, `str::es` Email status,
  `act::s-all` Subscribed to email.

## The suppression set (every send)

Exclude, by audience and field:
- Payers: `bol:cm:paying = true` or `bol:cm:paidstatus = true`.
- Unsubscribed: the Unsubscribed audience, or `act::u-all`, or `bol::p` Email permission = false.
- Hard bounced and suppressed: the Bounced audience, `act::b`, `act::es`, invalid email.
- Internal Team, BOT, Test contacts (`bol:cm:test-email = true`).
Compliance-privacy-reviewer verifies the suppression is applied and consent holds before any send.

## Per-campaign targeting

Each instructor 7-step sequence is a non-payer nurture for that class:

- Audience: `Created Account - NonPaying` AND `classId = <that instructor's class>`, or the
  per-instructor "Not Paid - <Instructor>" segment (the Rahma precedent), minus the suppression set.
- Language split: send the AR variant to `language = ar` and the EN variant to `language = en`.
  One person gets one language, never both.
- Geo: GCC, Saudi primary, via `geo::country`. Optional tightening for a Saudi-first flight.

The Bassam Makeup 4-email non-payer flow targets the same NonPaying pool filtered to the makeup
classId (or the whole NonPaying pool if run as a brand-level nurture), same suppression and
language split.

## The journey (the 7-step as an Ortto journey)

- Entry: contact enters the per-class non-payer segment (account created, not paying, that classId).
- E1 fires on entry. E2 to E7 fire on a time-based foundation (about every 2 to 3 days) layered
  with behavior branches: if Opened or Clicked or Started, advance or skip; if not-opened, re-angle.
- Exit: `paying` becomes true (subscribed, the success event) or `act::u-all` unsubscribe.
- Failed-payment branch: `bol:cm:hasfailedpayment = true` interrupts with the BillingNotice
  component, then resumes. This is the branch the design system's 7-step already anticipates.
- Cadence and branch logic follow `skills/07-lifecycle-messaging/templates/sequence-standards.md`.

## Sending, step by step (human, in Ortto)

1. Stage the email assets in Ortto (the build, once the push path is settled).
2. Build the journey: entry condition (the segment above), the 7 sends with delays and behavior
   branches, the exit on `paying`, the failed-payment branch.
3. Attach each step's asset, AR or EN by the language branch.
4. Set the audience to the segment minus the suppression set.
5. Send is a per-campaign human action in Ortto. The MCP cannot send; nothing dispatches on its own.

## Measurement

Success metric: subscription conversion from the flow, the `paying` transition during or shortly
after the sequence, read with `get_email_report` (opens, clicks, per step) and the `paying`
field movement. Opens are a health signal, not the goal. This is the metric stream 8 measures
against, set before send, not invented after.

## Gates before any send

- Compliance and privacy: suppression applied (payers, unsubscribed, bounced, no-permission),
  consent valid, no personal or sensitive data in any URL or tracking parameter, the data-flow
  disclosed. Saudi PDPL and data residency: the Ortto account is US hosted, an open decision.
- Public status: the named roster is `unconfirmed` in `_CATALOG.md`; send is blocked until Ahmed
  confirms it (the standing brand-qa block).
- The human gate: per action and per campaign, in Ortto. Nothing here sends on its own.

## What is needed to execute

- The classId value per class (from Ortto or the class data), or the per-instructor "Not Paid"
  segments built like the Rahma one.
- The send platform finalized (Ortto adoption: region or PDPL call, scoped key, the asset push
  settled).
- The two standing confirmations: roster public status, and the data-residency decision.

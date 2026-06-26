# Compliance and Privacy Verdict

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: compliance-privacy-reviewer
- stream: cross-cutting compliance and privacy gate
- verdict_date: 2026-06-05
- status: draft-review complete. Not approved. Approval is the human gate's decision alone.
- compliance_qa: pass (design-only, with seven open items that must be resolved before any
  send, spend, pixel activation, audience build, or wiring is activated)
- brief_refs checked: brief s.3 (audience, suppression, data-residency market), s.5 (channels,
  gate, platform open items), s.7 (creative constraints), s.8 (no PII in tracking, no
  accreditation, open items list), s.9 (approval status)

---

## Scope

Assets reviewed:
- 00-campaign-package.md (overview, calendar, open items)
- 01-emails.ar-en.md (4-message non-payer lifecycle flow, email suppression)
- 02-social-posts.ar-en.md (8 organic posts, gate-landing posts)
- 03-paid-ads.ar-en.md (pixel/CAPI, lookalike, retargeting audiences)
- 04-app-notifications.ar-en.md (5-touch push sequence, push consent and suppression)
- briefs/2026-06-bassam-fattouh-makeup.md

This is a design-only review. The gate platform, send platform, push platform, pixel, and
CAPI are all unconfirmed open items. Actual send, wiring, audience upload, and pixel
activation are blocked by those open items and must not proceed until confirmed and
resubmitted to this gate.

---

## Verdict

PASS (design-only).

No structural compliance failure exists in the drafted copy or the described data-flow logic.
The package correctly defers all sends, wiring, and audience activation to human-gate
confirmation. Seven open items are surfaced below. These are not invented answers. They are
gaps the human gate must resolve before any action is activated. The fix list below is empty
because no design-level violation was found. The open items travel with the package to the
human gate.

No fix list. Seven open items.

---

## Check 1. No personal or sensitive data in URL parameters or tracking

Result: PASS.

Every artifact that references a CTA destination or tracking URL carries an explicit design
constraint prohibiting PII in parameters. Specific statements found and confirmed:

- 01-emails.ar-en.md: "CTA lands on: the Masterclass page or the signup gate. No personal
  data in the URL." (E1 section). "No sensitive data in any link." (flow logic).
- 02-social-posts.ar-en.md: "Distribution: lands on the signup gate. No personal data in the
  URL." (Post 5). "Never put personal or sensitive data in a tracking URL." (distribution
  routing section).
- 03-paid-ads.ar-en.md: "No personal or sensitive data in any tracking parameter. Pixel and
  CAPI mapping owned by data-tracking-engineer, gated." (measurement note).
- 04-app-notifications.ar-en.md: "never to a URL carrying personal or sensitive data."
  (constraints).

No name, email address, phone number, or other identifier was found in any URL, query string,
UTM, or tracking parameter across all five artifacts. The pixel and CAPI mapping is noted as
owned by data-tracking-engineer and gated. That mapping has not been submitted for review.
It must come back through this gate before any pixel or CAPI is activated. See Open Item 1.

---

## Check 2. Consent correctness

Result: PASS at design level. Open Items 1, 2, 3 below for implementation.

Email: the flow targets owned non-paying email contacts who already have a relationship with
Maharat. The design correctly includes an unsubscribe mechanism and sender identity in every
email (01-emails.ar-en.md, flow logic: "Every email carries an unsubscribe and the sender
identity."). The consent basis (prior relationship or legitimate interest) is consistent with
this design. The brief notes "Confirm source" for the list, meaning the actual consent record
must be confirmed before wiring. See Open Item 4.

WhatsApp: the brief (s.5) names WhatsApp as a possible gate and lifecycle channel alongside
email. WhatsApp marketing sends require explicit, separately-logged opt-in under Meta
WhatsApp Business Policy. The current package does not specify what consent language,
checkbox, or record structure would appear at the gate for WhatsApp. If WhatsApp is selected
as a channel, a consent-capture mechanism must be designed and reviewed before any send is
wired. See Open Item 2.

App push: 04-app-notifications.ar-en.md correctly suppresses opted-out users and notes the
push platform and consent model are open items. OS-level opt-in (iOS and Android) must be
confirmed as the mechanism. The design intent is correct; the implementation is unresolved.
See Open Item 3.

Paid retargeting and lookalike: 03-paid-ads.ar-en.md correctly states "Lookalike and
retargeting audiences depend on the gate platform and consent, and require
compliance-privacy-check before they go live." Concept D (retargeting) also notes "Requires
consent-based retargeting, compliance review." No audience may be built or activated until
the consent basis and data provenance are confirmed. See Open Item 5.

---

## Check 3. Suppression correctness

Result: PASS at design level. Open Item 4 for execution wiring.

Email: 01-emails.ar-en.md envelope states "Suppress payers, unsubscribed, hard-bounced." The
brief (s.3) confirms the same three categories. The flow logic also branches the user out of
the flow on subscription, preventing continued sends to a converted contact. All three
required suppression categories are present.

App push: 04-app-notifications.ar-en.md suppresses users who already subscribed and any who
opted out of push. Correct.

Paid audiences: 03-paid-ads.ar-en.md does not explicitly state that existing subscribers will
be excluded from paid conversion-goal audiences. Targeting paying subscribers with acquisition
ads is not a legal violation here, but it is a design gap for performance-marketer to confirm
when the platform is wired. This is noted, not failed.

Implementation note: the actual suppression execution depends on the platform for every
channel, and the platform is an open item for all channels. The design is correct. The wiring
cannot be verified until the platform is confirmed. See Open Item 4.

---

## Check 4. Saudi PDPL and data residency

Result: OPEN ITEMS 5 and 6. Not invented, not resolved. Surfaced for the human gate.

Saudi Arabia is the primary market (brief s.3). The Saudi Personal Data Protection Law (PDPL)
applies to personal data of Saudi residents collected, processed, or stored in connection with
this campaign. The data flows in scope include:

- Email addresses and first names collected at the signup gate (stream 6).
- App push tokens and in-app behavioral data for app users.
- Behavioral and conversion event data sent to Meta CAPI, TikTok, and Google.
- Lookalike and retargeting audience data uploaded to paid platforms.

The gate platform, email platform, push platform, pixel, and CAPI destinations are all
unconfirmed (brief s.5, open items in every artifact). Data residency cannot be assessed
until platforms are named.

Saudi PDPL requirements that apply and are not yet confirmed:
(a) Lawful basis for processing at the gate and for the owned list.
(b) Cross-border transfer safeguards for any platform that processes Saudi resident data
    outside Saudi Arabia.
(c) Collection notice or privacy policy link at the point of data collection.
(d) Retention periods and a deletion or purge schedule.
(e) A route for data subjects to submit access and deletion requests.

None of these are design failures in the drafted copy. They are unresolved implementation
requirements. The human gate must see them and Ahmed must resolve them before any send, gate,
or pixel goes live. See Open Items 5 and 6.

---

## Check 5. No accreditation implication

Result: PASS.

No certificate, accreditation, qualification, or regulatory recognition claim appears in any
copy or creative brief across all five artifacts. The package constraint is explicit (brief
s.8: "No accreditation claims."). The 00-campaign-package.md guardrail self-check records
"No accreditation implication anywhere." This reviewer confirms: no instance found in any
artifact.

---

## Check 6. Data-flow disclosure at the point of collection

Result: OPEN ITEM 7. Not a failure of the reviewed artifacts. Surface for the human gate.

The signup gate (stream 6, conversion-engineer) is the primary data-collection point. It
collects email or WhatsApp contact details. Saudi PDPL requires that data subjects are
notified at or before the point of collection about who collects the data, the processing
purpose, and how to exercise their rights.

The gate design (stream 6) is not included in this package review. The artifacts reviewed
here carry an internal design note that no PII goes in URLs, but they do not contain the
user-facing notice that PDPL requires. That notice must appear in the gate copy or as a
visible link to a privacy policy. Stream 6 must include this before going live. See Open
Item 7.

---

## Check 7. Data minimization, retention, and data-subject rights

Result: OPEN ITEM 5 (retention and data-subject rights).

Data minimization: the email flow uses first name for personalization where available. The
gate collects email or WhatsApp, proportionate to the stated purpose of subscription
conversion. The pixel and CAPI event scope is not defined yet (data-tracking-engineer owns
that mapping and it is gated). Minimization for pixel and CAPI must be assessed when that
mapping is submitted for review. See Open Item 1.

Retention: no retention period or deletion schedule is stated in any artifact or in the brief.
Saudi PDPL requires that data is not held beyond the purpose for which it was collected. A
retention or deletion stance must be defined and implemented. See Open Item 5.

Data-subject rights: no mechanism for access or deletion requests is described anywhere in
the package. Saudi PDPL gives data subjects the right to access, correct, and request
deletion of their data. A route for these requests must exist and be disclosed. See Open
Item 5.

---

## Open items for the human gate

All seven items are gaps in the implementation specification, not failures of the drafted
copy. All seven block the corresponding activation action until resolved. None is invented by
this reviewer.

OPEN ITEM 1. Pixel and CAPI data mapping not yet submitted.
The mapping is owned by data-tracking-engineer and is gated (03-paid-ads.ar-en.md,
measurement note). Before any pixel event fires or CAPI call is made, the full tracking plan
(every event name, every parameter, every destination) must be submitted to
compliance-privacy-check. Pixel and CAPI activation are blocked until that review passes.
Returns to: data-tracking-engineer.

OPEN ITEM 2. WhatsApp consent capture mechanism not specified.
If WhatsApp is selected as the gate or lifecycle channel, an explicit opt-in consent
statement, its record structure, and the mechanism for honoring opt-out must be designed and
reviewed before wiring. Returns to: lifecycle-architect, conversion-engineer (stream 6).

OPEN ITEM 3. App push consent model and platform not confirmed.
The push platform is unconfirmed. The mechanism by which push opt-in is captured (OS-level
permission), opt-out is recorded, and the suppression list is synced to the send scheduler is
unresolved. Confirm before the first push is wired. Returns to: lifecycle-architect (app
push), data-tracking-engineer.

OPEN ITEM 4. Suppression list source and execution wiring.
The brief (s.3) notes "Confirm source" for the suppression list. The categories are correct
in the design. The actual wiring of those lists into the send platform, and the confirmation
that existing subscribers are excluded from paid conversion-goal audiences, must be confirmed
when platforms are named. Returns to: lifecycle-architect, performance-marketer.

OPEN ITEM 5. Saudi PDPL: lawful basis, retention, and data-subject rights.
Three items are unconfirmed:
(a) The lawful basis for processing personal data at the signup gate and for the existing
    owned contact list. Must be stated and documented before any gate or send goes live.
(b) A retention period or deletion schedule for all collected contact and event data. Must be
    defined and implemented.
(c) A route for data subjects to submit access and deletion requests. Must be confirmed and
    disclosed, even if handled at the product or platform level rather than in this campaign.
Returns to: Ahmed (decision), then legal or compliance owner, then data-tracking-engineer and
lifecycle-architect for implementation.

OPEN ITEM 6. Data residency and cross-border transfer safeguards.
The gate platform, email platform, push platform, and paid platforms (Meta, TikTok, Google)
may all process Saudi resident data outside Saudi Arabia. Until platforms are named, the
transfer basis cannot be confirmed. When platforms are named, data-tracking-engineer and
legal must confirm that each transfer is covered by PDPL safeguards or equivalent before any
send, gate, or pixel goes live. Returns to: Ahmed (decision), then legal or compliance owner,
then data-tracking-engineer.

OPEN ITEM 7. Privacy notice or policy link at the signup gate.
The signup gate (stream 6, not yet drafted) is the data-collection point. Saudi PDPL requires
a collection notice or a visible link to the privacy policy at the point of collection. The
gate copy must include this before going live. Returns to: conversion-engineer (stream 6).

---

## Send, spend, and wiring block confirmed

Every artifact in the package correctly states that nothing sends, spends, or publishes. This
verdict confirms that block. Nothing in this verdict licenses any send, push fire, pixel
event, CAPI call, audience upload, or paid spend. All activation actions remain blocked until:

- All seven open items above are resolved.
- The platform is confirmed for each channel.
- Stream 6 gate design is drafted and passes compliance-privacy-check.
- The pixel and CAPI mapping is submitted and passes compliance-privacy-check.
- The human gate (Ahmed) gives explicit per-action approval.

---

## Routing

This verdict passes the package at the design level and attaches to the human-gate package
for campaign 2026-06-bassam-fattouh-makeup. The seven open items are the compliance picture
Ahmed must have in front of him before approving any go-live action.

On resolution of open items and platform confirmation, data-tracking-engineer and
lifecycle-architect must resubmit their execution-level wiring for a second
compliance-privacy-check before the human gate clears any activation.

A pass here is not approval to send. The human gate is separate and decisive.

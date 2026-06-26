# Compliance and Privacy Verdict: Summer of Skills, Full-Stack Non-Payer Campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: compliance-privacy-reviewer
- stream: cross-cutting compliance and privacy gate
- verdict_date: 2026-06-12
- status: design-only review complete. Not approved. Approval is the human gate's decision alone.
- compliance_qa: pass (design-only, with twelve open items that must be resolved before any
  send, spend, pixel activation, audience build, publish, wiring, or data collection is
  activated)
- brief_refs checked: objective, audience and suppression, channels and gate platform,
  signup_gate, creative_direction, open_items, Saudi PDPL and data-residency, no PII in
  tracking, no accreditation, consent model (email, WhatsApp, app push), suppression
  (payers, unsubscribed, hard-bounced, opt-outs), cross-border transfer (hashed list uploads
  to Meta and TikTok), data minimization, retention, data-subject rights, privacy notice at
  point of collection, journalist contact data (PR stream), DM automation (organic stream)

---

## Scope of This Review

Assets reviewed for this fullstack run (all under outputs/2026-07-summer-nonpayer/fullstack/):

- lifecycle-package.md (email flow E1 to E5, app push sequence P1 to P5, onboarding O1 to O3
  shape, segmentation logic, suppression, engagement events, privacy co-design notes)
- conversion-package.md (landing page spec, signup gate variants A and B, consent copy
  direction, event plan, operational verification checklist, gate routing logic)
- tracking-plan.md (7 events, Meta Pixel and CAPI mapping, GA4 mapping, dedup approach,
  full parameter list, BigQuery queries Q1 to Q8, test plan, privacy note on warehouse queries)
- paid-launch-package.md (Meta, TikTok, Google, YouTube campaign structures, retargeting
  and lookalike audiences, hashed list suppression, UTM structure, pre-launch checklist)
- media-plan-package.md (audience strategy, lookalike and retargeting audience definitions,
  consent basis note, UTM direction, PDPL notes, open items)
- organic-package.md (post calendar, gate-routing posts, distribution routing, community
  engagement guidance, DM automation open item)
- aso-package.md (keyword research, store listing optimization, screenshot concepts, reviews
  response policy, store experiments)
- pr-package.md (press release brief, media list and outreach plan, journalist data handling
  notes, distribution gating)
- web-design-package.md (information architecture, UX flow, wireframe, design_spec for the
  signup gate and conversion page, web_design_qa verdict)

Reference read:
- exemplar outputs/2026-06-bassam-fattouh-makeup/fullstack/compliance-verdict.md (prior
  campaign structure and open-item format)
- strategy-artifact.md for campaign_id 2026-07-summer-nonpayer

This is a design-only review. The gate platform, email platform, push platform, all paid
platforms (Meta, TikTok, Google, YouTube), tracking production deployment, and BigQuery
access are all unconfirmed or gated. No actual send, spend, wiring, audience upload, pixel
activation, or data collection has occurred. Nothing in this verdict licenses any of those
actions.

---

## Verdict

PASS (design-only).

No structural compliance failure exists in the drafted design logic, data-flow descriptions,
parameter lists, UTM structures, consent copy directions, or suppression designs across the
nine artifacts reviewed. Every artifact correctly states that nothing sends, spends, publishes,
or wires without human-gate approval. Twelve open items are surfaced below. None is invented
by this reviewer. All twelve are gaps in the implementation specification that the human gate
must resolve before any activation action is taken. The fix list is empty because no
design-level violation was found.

No fix list. Twelve open items.

---

## Check 1. No personal or sensitive data in URL parameters or tracking

Result: PASS.

Every artifact that references a CTA destination, tracking call, UTM parameter, event
parameter, or URL structure explicitly prohibits PII. This reviewer inspected every event
definition, parameter, UTM field, and URL pattern across all nine artifacts.

Confirmed findings:

conversion-package.md sections 2.1 and 3.2: "No personal or sensitive data in any URL
parameter. UTM parameters carry campaign, source, medium, and content identifiers only,
never user-level identifiers, email addresses, phone numbers, or subscriber IDs." The gate
spec section 3.2 states: "No hidden pre-filled parameters carrying user identifiers from the
ad platform." Section 3.4 (gate trigger logic for owned non-payers): "The owned non-payer
detection mechanism must not expose user-level identifiers in URL parameters." Field
selection in COMP-FIELD-GRID is a UI state variable, not a URL query parameter.

tracking-plan.md section 5: the full parameter list annotates every parameter as
non-identifying. Explicitly prohibited in all parameters and tracking calls: email address
(in any form, including partial or encoded), phone number, full name or partial name, user
account ID or internal subscriber ID in any form that links to an individual, device
identifier or advertising ID in parameters. Section 4 states: "No personal data (no email
address, no phone number, no name, no user ID or subscriber ID of any kind) is ever placed
in a UTM parameter or any URL query string that fires into a tracking call." The note on
page_location states that if the platform appends user-identifying parameters to URLs, those
must be stripped before the GA4 event fires.

tracking-plan.md section 7 (warehouse queries): "No personal data (no email address, no
phone number, no name, no user account ID or subscriber ID) appears in any query output.
user_pseudo_id from the GA4 export is a pseudonymous identifier and is not selected in any
of the queries above; if it is needed for session-level deduplication in a future iteration,
that use case must be reviewed by compliance-privacy-reviewer before the query runs."

lifecycle-package.md section 3 (personalization): "No sensitive data, no subscription-tier
data, no behavioral targeting data in URL parameters. Unsubscribe link and Maharat sender
identity present in every message. No personal or sensitive data in any tracking URL
parameter." Section 4 (push): "No URL with personal data. No personal or sensitive data in
any push tracking parameter."

paid-launch-package.md section 5.5: UTM structure confirmed. Content values are field codes
and objective codes (music, cooking, breadth, retargeting), never user identifiers, emails,
phones, or personal attributes. Pre-launch checklist item: "No personal data in any UTM
parameter or tracking call: PASS (plan)."

media-plan-package.md section 7: "No user identifier, no email, no phone, no personal
attribute in any UTM field." Section 3: "No personal data appears in any audience definition
below. All definitions are segment descriptors for platform targeting construction."

organic-package.md: "Every signup-gate URL carries no personal or sensitive data in
parameters. Tracking is anonymous and campaign-level only." Community engagement guidance
section 5.4: "No personal or sensitive data in any reply link or DM, and no tracking
parameters in any links shared in replies."

pr-package.md: "No tracking parameters carrying personal or sensitive data are used." Class
and platform page URLs are clean destination links with no query strings carrying personal
data. Editorial contacts are publicly listed editorial contact information only.

aso-package.md: no tracking parameters or data collection are introduced by the ASO artifact.
Store listing and review response policy contain no data-collection action beyond what the
app stores themselves manage.

web-design-package.md: "No personal or sensitive data in URL parameters at any point in this
flow. Field selection is a UI state, not a URL query param."

One implementation gap noted (not a design failure, but an open item that carries forward):
tracking-plan.md section 4 and conversion-package.md open_items both flag that if the email
or app-push platform appends subscriber-identifying parameters to inbound links, those must
be stripped before any GA4 event fires. This cannot be confirmed or resolved until the
platform is named. This is Open Item 1 below.

---

## Check 2. Consent correctness

Result: PASS at design level. Open Items 1, 2, and 3 for implementation.

Email consent: lifecycle-package.md targets owned non-paying contacts who have an existing
relationship with Maharat. Unsubscribe link and sender identity are specified as required in
every email. Consent basis (prior relationship) is consistent with the design. The actual
consent record for the owned list must be confirmed at build (Open Item 4).

Signup gate, email variant (GATE-CONSENT-AR/EN): conversion-package.md section 3.2 specifies
that the consent copy slots must state who collects the data, the purpose, a link to the
Maharat privacy policy visible before submit, and how to unsubscribe. The slot is authored by
copywriter-ar under compliance-privacy-reviewer supervision. At design level, this structure
is correct. The consent line is required to be visible before the user submits, not hidden
behind a scroll or collapsed element (confirmed in conversion-package.md section 2.4 RTL
checklist item: "Consent line visible before submit: Not yet run"). Open Item 5 covers the
implementation verification.

Signup gate, WhatsApp variant (GATE-CONSENT-AR/EN WhatsApp): conversion-package.md section
3.3 specifies that the WhatsApp consent copy must explicitly reference WhatsApp messaging,
state the stop mechanism ("Stop" or equivalent), be visible before submit, and be separately
logged with a timestamp and consent text version linked to the user's lifecycle platform
entry. The package explicitly states: "Compliance-privacy-reviewer must run on this consent
variant and the logging mechanism before the WhatsApp gate goes live." This is correct
handling. The logging mechanism has not been designed. Open Item 2 below.

App push: lifecycle-package.md correctly suppresses opted-out users and notes that the
OS-level push opt-in model is unconfirmed pending the push platform. Open Item 3 below.

Paid retargeting and lookalike audiences: paid-launch-package.md and media-plan-package.md
both state that retargeting audiences and hashed list uploads are blocked pending
compliance-privacy-check. No audience has been built or activated. Open Item 6 below.

---

## Check 3. Suppression correctness

Result: PASS at design level. Open Item 4 for execution wiring.

Email: lifecycle-package.md section 2 suppression table lists all required categories:
already paying, unsubscribed, hard-bounced, push opt-outs (for the push channel), and
mid-flow converters (subscription_start at any point exits the contact immediately from
both the email flow and the push sequence). The double-check mechanism at entry and at send
is specified. A sunset rule is designed for contacts who complete E1 to E5 with no
engagement.

App push: lifecycle-package.md section 4 suppresses subscribed users and any user who has
revoked push permission at OS level before any push send. The push platform is unconfirmed,
so wiring cannot be verified.

Paid audiences: paid-launch-package.md ad sets META-AS-09 through META-AS-11 and TIKTOK-AS-05
all specify current paying subscribers as an exclusion. TIKTOK-AS-05 specifies: "Exclusion:
current subscribers (hashed email list, PDPL block applies)." The hashed list mechanism is
blocked pending PDPL clearance. The suppression intent is correct; the execution is blocked.

Owned non-payer suppression from paid prospecting: paid-launch-package.md open item 11 and
media-plan-package.md section 3.1 both flag that suppressing the roughly 18,000 owned
non-payers from cold paid acquisition requires a hashed list match between the CRM and Meta,
TikTok, and YouTube custom audiences. Source list and consent basis must be confirmed. Same
PDPL caveat applies. Open Item 6.

Onboarding: lifecycle-package.md section 5 confirms that new subscribers exit the non-payer
flow on subscription_start and enter onboarding. No double-send to a converted contact is
designed in. Onboarding messages O1 to O3 are not yet authored and are separately gated.

Suppression source: brief flags "Confirm suppression source at build." This is confirmed as
an outstanding item across lifecycle-package.md and conversion-package.md. Open Item 4.

---

## Check 4. Saudi PDPL and data residency

Result: OPEN ITEMS 6, 7, and 8. Not invented, not resolved. Surfaced for the human gate.

Saudi Arabia is the primary market. The Saudi Personal Data Protection Law (PDPL) applies to
personal data of Saudi residents collected, processed, or stored in connection with this
campaign. The data flows in scope include:

- Email addresses and optional first names collected at the signup gate
  (conversion-package.md).
- WhatsApp phone numbers and optional first names (conversion-package.md, gate variant B).
- App push tokens and in-app behavioral data for app users (lifecycle-package.md).
- Behavioral and conversion event data sent to Meta Pixel and CAPI, TikTok Pixel, and GA4
  (tracking-plan.md, paid-launch-package.md).
- Hashed email lists for lookalike construction and subscriber suppression on Meta, TikTok,
  and YouTube (paid-launch-package.md, media-plan-package.md).
- Hashed match-key signals for CAPI server-side matching (tracking-plan.md section 1.5).
- Journalist contact data used in PR outreach (pr-package.md).

All send, tracking, and paid platforms are unconfirmed. Data residency and cross-border
transfer safeguards cannot be assessed until platforms are named.

Saudi PDPL requirements that apply and are not yet confirmed in any artifact:

(a) Lawful basis for processing personal data at the signup gate, for the existing owned
    email list, and for the WhatsApp opt-in. Must be stated and documented before any gate
    or send goes live. Open Item 7(a).
(b) Cross-border transfer safeguards. Every platform that may process Saudi resident data
    outside Saudi Arabia, including Meta, TikTok, Google, and the email, WhatsApp, and push
    platforms, requires confirmation that the transfer is covered by PDPL safeguards or an
    equivalent basis before any send, gate, pixel, or audience upload goes live. The hashed
    email list uploads to Meta, TikTok, and YouTube for subscriber suppression and lookalike
    construction are cross-border transfers of personal data. Open Item 7(b).
(c) Retention periods and a deletion or purge schedule. No retention period or deletion
    schedule is stated in any artifact in this fullstack run. Saudi PDPL requires that data
    is not held beyond the purpose for which it was collected. Open Item 7(c).
(d) A route for data subjects to submit access, correction, and deletion requests. No such
    route is described in any artifact. Open Item 7(d).

None of these are design failures in the drafted copy or data-flow logic. They are unresolved
implementation requirements that belong above the marketing engine. See Open Items 7 and 8.

Additionally: tracking-plan.md section 1.5 explicitly flags that "any hashed match-key
signals for CAPI (for example hashed email for matching) are a server-side backend operation
and must be reviewed by compliance-privacy-reviewer before go-live, subject to the Saudi PDPL
data-residency open item." This is correct handling. The review cannot occur until the CAPI
platform and data-residency posture are confirmed.

---

## Check 5. No accreditation implication

Result: PASS.

No certificate, accreditation, qualification, or regulatory recognition claim appears in any
copy, design direction, creative concept, ASO string direction, reviews response policy, or PR
brief across all nine artifacts.

Specific confirmations:

conversion-package.md section 6, FAQ pair Q2: "The certificate question: framing must use
the 'شهادة مخصصة باسمك' pattern per brand-voice.md; never accredited." The direction note
for copywriter-ar explicitly flags the non-accredited guardrail.

paid-launch-package.md pre-launch checklist: "No accreditation claim in any in-platform copy:
PASS." All seven mapped copy variants (AD-BREADTH-1, AD-MUSIC-1, AD-COOK-1, AD-MAKEUP-1,
AD-BUSINESS-1, AD-ACTING-1, AD-RETARGET-1) were reviewed; no accreditation claim found.

aso-package.md section 2.4 description guidance: "Completion certificates are referenced only
as Maharat completion certificates, never as accredited or externally recognized."
Reviews response policy section 5.3: "the response states clearly that it is a Maharat
completion certificate and does not imply external accreditation."

pr-package.md guardrail check: "Accreditation claim: PASS." The press release brief
explicitly instructs copywriters that Maharat issues completion certificates and these are not
accredited.

organic-package.md community engagement guidance section 5.3: certificate accreditation
questions are listed under "What to escalate" with explicit instruction to route to the team
and "never confirm or imply accreditation."

This reviewer confirms: no accreditation instance found in any of the nine artifacts.

---

## Check 6. Data-flow disclosure at the point of collection

Result: PASS at design level, with implementation verification required before go-live.

conversion-package.md sections 3.2 and 3.3 specify the privacy notice for both the email
gate and the WhatsApp gate variants. The consent copy slots (GATE-CONSENT-AR/EN) are
defined to include: who collects the data (Maharat), the purpose (receiving messages), a link
to the Maharat privacy policy visible before submit, and the opt-out mechanism. The consent
line is required to be visible before the user submits, not hidden behind a scroll or
collapsed element. This is specified in the design, not yet run as an implementation check.

web-design-package.md UX flow: "No personal or sensitive data in URL parameters at any
point in this flow." The gate state machine (gate-default, gate-submitting, gate-submitted,
gate-error, gate-confirmed) includes the consent line in the gate-default state, before any
submit action.

The implementation check (consent line visible, policy link live, not hidden before the first
submit action) is in the conversion-package.md section 6 operational verification checklist
as "Not yet run." This must pass before go-live. Open Item 5.

PR stream: pr-package.md states that press materials direct to Maharat's own class and
platform pages and do not collect reader data. No disclosure gap in the PR stream.

ASO stream: aso-package.md introduces no new data collection beyond what the app stores
themselves manage. No disclosure gap.

Organic stream: organic-package.md confirms that all gate-routing posts carry no personal or
sensitive data in parameters and that tracking is campaign-level and anonymous only.

---

## Check 7. Data minimization, retention, and data-subject rights

Result: PASS on data minimization at design level. Open Items 7(c) and 7(d) on retention and
data-subject rights (unresolved).

Data minimization:

conversion-package.md section 3.2 (email gate): fields collected are email address (required)
and first name (optional, clearly labeled optional). Explicitly excluded: phone number, date
of birth, gender, location, and any field not needed for the conversion purpose. "No hidden
pre-filled parameters carrying user identifiers." Data minimization is correctly applied at
the design level.

conversion-package.md section 3.3 (WhatsApp gate): phone number (required) and first name
(optional). Same exclusion list. No extra data fields.

tracking-plan.md: every event parameter in the full parameter list (section 5) is
non-identifying. No personal data parameter exists in the plan. Explicitly prohibited: email
address, phone number, name, user account ID, subscriber ID, device identifier or advertising
ID. Minimization is satisfied for the tracking design.

lifecycle-package.md section 3 personalization: first name used in greeting only, from the
owned CRM. If absent, generic greeting is used. No sensitive data, no subscription-tier data,
no behavioral targeting data in URL parameters. Minimization is correct.

PR stream: pr-package.md uses publicly listed editorial contacts only for outreach. No data
from the owned non-payer list is used in any PR activity. Minimization is satisfied.

ASO stream: no new personal data collected. Minimization is not a gap.

Retention:

No retention period or deletion schedule is stated in any artifact in this fullstack run.
Saudi PDPL requires that data is not held beyond the purpose for which it was collected. This
is an unresolved requirement. Open Item 7(c).

Data-subject rights:

No route for access, correction, or deletion requests is described in any artifact. The
conversion-package.md specifies a link to the live Maharat privacy policy in the consent
line, but this reviewer has not examined the live policy and cannot confirm whether it covers
data-subject rights. Open Item 7(d) and Open Item 9 (live policy review).

---

## Open Items for the Human Gate

All twelve items below are gaps in the implementation specification, not failures in the
drafted copy or design logic. All twelve block the corresponding activation action until
resolved. None is invented by this reviewer. All twelve travel to the human gate with this
verdict.

OPEN ITEM 1. Platform-appended subscriber-ID stripping not yet verifiable.

Tracking-plan.md section 4 and conversion-package.md open_items both flag: if the email or
app-push platform appends subscriber-identifying parameters to inbound links, those parameters
must be stripped before any GA4 event fires. This is a hard stop. The stripping requirement
cannot be confirmed until the platform is named. The conversion-package.md operational
verification checklist item "Subscriber-ID stripping" is marked "BLOCKED: platform not
confirmed; compliance-privacy-reviewer must clear." This reviewer confirms the block and
carries it forward. Once the platform is named, conversion-engineer and compliance-privacy-
reviewer must confirm the stripping mechanism before any GA4 event fires on an inbound email
or push link.

Returns to: data-tracking-engineer and conversion-engineer (mechanism confirmation at platform
build), compliance-privacy-reviewer (implementation-level clearance), human gate.

OPEN ITEM 2. WhatsApp consent logging mechanism not yet designed or reviewed.

conversion-package.md section 3.3 correctly specifies that if WhatsApp is the chosen gate,
the consent logging mechanism must be confirmed and reviewed by compliance-privacy-reviewer
before the WhatsApp gate goes live. The consent notice text direction is designed. The
mechanism for logging, storing, and linking the consent record (including timestamp and
consent text version) to the user's entry in the lifecycle platform has not been designed or
submitted for review. Without a functioning consent log, the WhatsApp gate cannot satisfy
Saudi PDPL or Meta WhatsApp Business Policy consent requirements.

Returns to: conversion-engineer (mechanism design), lifecycle-architect (record linkage),
then compliance-privacy-reviewer for a dedicated review before the WhatsApp gate can go live.

OPEN ITEM 3. App push consent model and platform not confirmed.

The push platform is unconfirmed. The mechanism for OS-level push opt-in capture, opt-out
recording, quiet-hours enforcement, and suppression list sync to the scheduler is unresolved.
lifecycle-package.md section 4 correctly blocks push wiring on this item. The app audience
size is also OPEN ITEM and cannot be sized until the platform is confirmed.

Returns to: lifecycle-architect (push platform coordination and OS consent model),
data-tracking-engineer (event mapping for push_opt_out and push_open).

OPEN ITEM 4. Suppression list source and execution wiring.

The suppression categories are correct in the design across all three channels (email, push,
paid). The actual source data (live CRM or ESP export of paying contacts, unsubscribed
contacts, and hard-bounced addresses) is flagged "Confirm source" in the brief and in
lifecycle-package.md. Execution wiring into the send platform and confirmation that existing
subscribers are excluded from all paid acquisition audiences cannot occur until the source is
named and the platform is confirmed. The hashed list upload for paid channel suppression
additionally requires Open Items 6 and 7 resolution.

Returns to: lifecycle-architect (email and push suppression wiring), performance-marketer and
paid-build-engineer (paid channel suppression exclusion list upload, blocked on Open Items 6
and 7).

OPEN ITEM 5. Implementation verification of the consent line and privacy notice at the gate.

conversion-package.md section 6 operational verification checklist item "Consent line visible
before submit" is marked "Not yet run: page not built." The consent line (GATE-CONSENT-AR/EN)
and the privacy policy link must be visible to the user before any submit action, not hidden
behind a scroll or collapsed element. The privacy policy link must resolve to a live, readable
policy page. These checks must pass before the gate opens. Additionally, the GATE-CONSENT-AR
and GATE-CONSENT-EN copy slots are authored by copywriter-ar and copywriter-en under
compliance-privacy-reviewer supervision; both must pass arabic-copy-qa and english-copy-qa
before the consent line can be used in a live gate.

Returns to: conversion-engineer (implementation), arabic-copy-qa and english-copy-qa
(consent copy QA), compliance-privacy-reviewer (implementation-level check before go-live).

OPEN ITEM 6. Saudi PDPL: hashed list uploads, retargeting audiences, and CAPI hashed signals.

Every hashed email list upload to Meta, TikTok, and YouTube (for subscriber suppression,
owned non-payer suppression, and lookalike seed construction) constitutes a cross-border
transfer of personal data of Saudi residents to platforms that may process data outside Saudi
Arabia. Every CAPI server-side hashed match-key signal is also a cross-border transfer.

No consent basis and no transfer safeguard have been confirmed for any of these flows. All
retargeting audiences, all lookalike constructions, all subscriber suppression uploads, and
all CAPI hashed signals are blocked until:

(a) The lawful basis for the underlying personal data processing is confirmed (Open Item 7a).
(b) The cross-border transfer safeguard for each platform is confirmed (Open Item 7b).
(c) The platform is named (gate platform, email platform, push platform, Meta CAPI endpoint).

This is the hardest blocker in the paid stream. Every retargeting ad set (META-AS-09 through
META-AS-11, TIKTOK-AS-05, YOUTUBE-AG-01 remarketing) and every lookalike audience (Meta
Lookalike-01 and Lookalike-02) is blocked until this is resolved.

Returns to: Ahmed (decision on PDPL posture and platform choice), legal or compliance owner
(cross-border transfer safeguard selection), data-tracking-engineer and performance-marketer
(implementation once cleared), compliance-privacy-reviewer (dedicated implementation-level
review before any upload or hashed signal fires).

OPEN ITEM 7. Saudi PDPL: lawful basis, retention, and data-subject rights.

Four unresolved items under the PDPL:

(a) Lawful basis for processing. The basis for processing personal data at the signup gate
(new acquisition by email or WhatsApp capture), for the owned non-payer email list (existing
contacts, prior relationship), and for any WhatsApp opt-in must be stated and documented
before any gate or send goes live. No artifact states the lawful basis.

(b) Cross-border transfer safeguards. When platforms are named, the legal or compliance owner
and data-tracking-engineer must confirm that each transfer of Saudi resident data to each
platform (email, WhatsApp, push, Meta, TikTok, Google, YouTube) is covered by a PDPL
safeguard or an equivalent basis before any activation. This applies to hashed list uploads
(Open Item 6) and to routine event data flows to analytics and ad platforms.

(c) Retention period and deletion schedule. No retention period or purge schedule is stated
in any artifact. A retention stance must be defined and implemented before go-live. Data must
not be held beyond the purpose for which it was collected.

(d) Data-subject rights route. No route for access, correction, or deletion requests is
described in any artifact. The route must exist and be disclosed, whether through the live
Maharat privacy policy or a dedicated process. See also Open Item 9.

Returns to: Ahmed (decision), legal or compliance owner (drafting and documentation),
data-tracking-engineer and lifecycle-architect (implementation of retention schedule and
deletion mechanism), compliance-privacy-reviewer (review of implemented controls before
go-live).

OPEN ITEM 8. Platform confirmation and production tracking write gate.

The gate platform, email platform, push platform, and all paid platforms (Meta, TikTok,
Google, YouTube) are unconfirmed. This is the structural prerequisite for most other open
items. Until platforms are named:

- Data residency and cross-border transfer safeguards cannot be assessed.
- CAPI endpoint wiring cannot be designed or cleared.
- Subscriber-ID stripping cannot be confirmed.
- WhatsApp consent logging mechanism cannot be designed.
- Push OS consent model cannot be confirmed.
- Any production tracking write (pixel deployment, CAPI endpoint, GA4 event configuration,
  BigQuery query activation) is a human-gate action that has not occurred.

tracking-plan.md section 9 explicitly states: "writing tracking to production is a gated
action. The human gate (Ahmed) clears each action. This document is the plan only. Nothing
has been written to production." This reviewer confirms the block.

Returns to: Ahmed (platform decisions and production write approvals), then data-tracking-
engineer and lifecycle-architect for implementation-level review and resubmission to
compliance-privacy-reviewer before activation.

OPEN ITEM 9. Live Maharat privacy policy review.

conversion-package.md, lifecycle-package.md, and organic-package.md all rely on linking to
the "live Maharat privacy policy" as the disclosure mechanism for PDPL purposes. This
reviewer has not examined the content of the live policy. Before go-live, the live policy
must be reviewed to confirm it:

(a) Identifies Maharat as the data controller.
(b) Describes the processing purposes for this campaign (email marketing, WhatsApp messaging,
    app push, paid retargeting, hashed list uploads).
(c) Describes users' rights under Saudi PDPL (access, correction, deletion).
(d) Names a contact route for data-subject requests.
(e) Covers cross-border data transfers if applicable.
(f) Reflects any retention period confirmed in response to Open Item 7(c).

If the live policy does not cover these elements, it must be updated before the policy link
in the consent line is relied upon to satisfy PDPL disclosure requirements.

Returns to: Ahmed (decision), legal or compliance owner (policy review and update if
required).

OPEN ITEM 10. DM automation tool and comment-to-DM mechanism (organic stream).

organic-package.md section 5.5 notes: "DM or keyword-mechanic automation is not assumed
in this calendar. If a keyword CTA is added, the DM automation platform requires a separate
tool and platform decision, gated." The community engagement guidance confirms this is not
active in the current calendar design. However, the organic-package.md open items table
includes: "DM or keyword automation: Not assumed in this calendar. If a comment-to-DM
mechanic is added, the DM automation platform requires a separate tool and platform decision,
gated."

If a comment-to-DM or keyword-triggered DM mechanic is introduced at any point during the
campaign flight, it will introduce a data flow where user public comments or usernames are
processed to trigger a DM send. That flow must be reviewed by compliance-privacy-reviewer
before any automation is wired. No personal data may appear in any automated message URL or
tracking parameter. The platform tool must be approved by Ahmed before adoption.

Returns to: organic-social (if a tool proposal is raised), Ahmed (approval), then
compliance-privacy-reviewer (data-flow review of the chosen tool before wiring).

OPEN ITEM 11. Journalist contact data handling (PR stream).

pr-package.md section 4 states that specific named editorial contacts are not listed and that
no personal email addresses or mobile numbers are to be stored in campaign tracking systems.
This is the correct design intent. The compliance notes in pr-package.md section 5 raise the
question: "The compliance-privacy-reviewer should confirm whether storing journalist contact
data in any tool or platform triggers PDPL obligations."

This reviewer confirms: storing journalist contact data (even publicly listed professional
contacts) in any tool or platform that processes data of Saudi residents may trigger PDPL
obligations depending on the tool's data residency. Before outreach is executed and before
any journalist contact list is built in any tool:

(a) The basis for holding and using journalist contact data (typically legitimate interest
    or publicly listed professional contact) must be confirmed.
(b) If any tool is used to manage outreach contacts, that tool's data residency must be
    confirmed against Saudi PDPL requirements (Open Item 7b applies here too).
(c) The placeholder "[MEDIA CONTACT NAME], [MEDIA CONTACT EMAIL]" in the press release
    boilerplate must be replaced with a confirmed, approved contact before any distribution.
(d) No journalist contact data may be stored in any campaign analytics or tracking platform.

Returns to: pr-comms (execution planning and tool selection), Ahmed (contact confirmation and
approval), legal or compliance owner (PDPL basis for journalist data), compliance-privacy-
reviewer (if a contact management tool is adopted, a dedicated data-flow review is required).

OPEN ITEM 12. BigQuery MCP access and paid spend data pipeline.

tracking-plan.md open items confirm: "BigQuery MCP access is not confirmed. All warehouse
queries are specified and gated; they are added and run only on approval." Queries Q1 through
Q8 are ready as a plan but have not been added to BigQuery, let alone run. Separately, the
paid spend data pipeline and table schema needed for Q8 (cost per subscription) are not
confirmed.

No query runs, no view is created, and no table is accessed until BigQuery MCP access is
approved by Ahmed and the queries are explicitly authorized. The user_pseudo_id from the GA4
export is not selected in any query as designed; this is correct. If session-level
deduplication requiring user_pseudo_id is ever needed, that use case must return to
compliance-privacy-reviewer before the query is run.

Returns to: Ahmed (BigQuery MCP access approval), data-tracking-engineer (query activation
on approval), performance-marketer (paid spend pipeline confirmation for Q8), analytics-
reporter (monitoring once access is granted).

---

## Send, Spend, Wiring, Publish, and Data Collection Block Confirmed

Every artifact in this fullstack package correctly states that nothing sends, spends,
publishes, wires, or collects data. This verdict confirms that block. Nothing in this verdict
licenses any send, push fire, pixel event, CAPI call, hashed list upload, audience build,
paid spend, organic publish, press release distribution, store listing update, ASO experiment
activation, BigQuery query run, or tracking write to production.

All activation actions remain blocked until:

- All twelve open items above are resolved or formally accepted by Ahmed at the human gate.
- The platform is confirmed for each channel (email, WhatsApp, push, paid, gate).
- Lawful basis and cross-border transfer safeguards are confirmed for Saudi PDPL.
- A retention schedule and data-subject rights route are defined and implemented.
- The live Maharat privacy policy is reviewed and confirmed as covering all required elements.
- The consent line and privacy notice implementation check (conversion-package.md section 6)
  passes.
- GATE-CONSENT-AR and GATE-CONSENT-EN copy passes arabic-copy-qa and english-copy-qa.
- The WhatsApp consent logging mechanism (if WhatsApp is chosen) is designed, reviewed by
  compliance-privacy-reviewer, and confirmed before the gate goes live.
- Subscriber-ID stripping from platform-appended URL parameters is confirmed before any GA4
  event fires on an inbound email or push link.
- The tracking-plan implementation-level compliance review is completed and passes.
- BigQuery MCP access is approved before any warehouse query runs.
- Journalist contact data handling is confirmed before any PR outreach is executed.
- Ahmed gives explicit per-action approval for each stream.

A pass here is not approval to send, spend, or publish. The human gate is separate and
decisive.

---

## Routing

This verdict passes the package at the design level and attaches to the human-gate package
for campaign 2026-07-summer-nonpayer. The twelve open items are the compliance picture Ahmed
must have in front of him before approving any go-live action.

On resolution of open items and platform confirmation, the following resubmissions are
required before activation:

- Open Item 1: conversion-engineer confirms subscriber-ID stripping mechanism and resubmits
  to compliance-privacy-reviewer when platforms are confirmed.
- Open Item 2: conversion-engineer and lifecycle-architect submit WhatsApp consent logging
  mechanism design to compliance-privacy-reviewer before WhatsApp gate can go live.
- Open Item 3: lifecycle-architect confirms push platform, OS consent model, and opt-out
  suppression before push wiring.
- Open Item 4: lifecycle-architect and performance-marketer confirm suppression source and
  wiring before any send or paid audience activation.
- Open Item 5: conversion-engineer confirms implementation verification checklist passes;
  arabic-copy-qa and english-copy-qa clear the GATE-CONSENT-AR/EN copy slots.
- Open Item 6: data-tracking-engineer and performance-marketer resubmit hashed list upload
  and CAPI hashed signal design to compliance-privacy-reviewer after PDPL posture is
  confirmed by Ahmed and legal or compliance owner.
- Open Items 7, 9: route to Ahmed then legal or compliance owner. These require decisions
  above the marketing engine.
- Open Item 8: data-tracking-engineer submits tracking-plan implementation package to
  compliance-privacy-reviewer when platforms are confirmed and before any production write.
- Open Item 10: organic-social submits any DM automation tool proposal through the standard
  tool approval process before any automation is wired.
- Open Item 11: pr-comms confirms journalist contact data handling approach before any
  outreach list is built or distributed.
- Open Item 12: data-tracking-engineer activates BigQuery queries only after Ahmed approves
  MCP access. Paid spend pipeline confirmed before Q8 runs.

A pass here is not approval to send. The human gate is separate and decisive.

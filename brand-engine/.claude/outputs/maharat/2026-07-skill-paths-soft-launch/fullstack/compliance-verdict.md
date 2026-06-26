# Compliance and privacy verdict: Skill Paths first-time soft launch, full-stack run

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: compliance-privacy-reviewer
- stream: cross-cutting compliance and privacy gate
- status: design-only pass (conditional). See verdict section.
- compliance_qa: pass (design-only, conditional on open items below)
- verdict_date: 2026-06-05
- packages_reviewed:
  - conversion-package.md
  - tracking-plan.md
  - lifecycle-package.md
  - paid-launch-package.md
  - media-plan-package.md
  - organic-package.md
  - pr-package.md
  - aso-package.md
  - copy-package.ar.md
  - copy-package.en.md

---

## Verdict

PASS (design-only, conditional).

This is a design review only. No pixel, CAPI, MMP, sending platform, ad account, or store
console is live or connected. Every live action (send, spend, publish, pixel write, CAPI call,
store listing update) is explicitly blocked in every package under an open item or a gate
condition. No personal data is collected, transmitted, or stored by this run today.

The compliance picture is this: the design is sound and the open items are correctly surfaced.
None of the structural defects that would force a fail (PII in URLs, missing consent basis,
suppression absent from the design, data flows undisclosed, accreditation implied) are present.
The open items listed below are genuine blockers that must be resolved before any live action
is authorized. They are not invented obstacles; they are gaps in the data-handling picture that
Saudi PDPL, GDPR principles, and the engine's own rules require the human gate to decide.

This verdict attaches to the human-gate package. It does not constitute approval to send, spend,
or publish. Ahmed's explicit per-action, per-campaign approval is the only valid authorization.

---

## Check-by-check findings

### Check 1: No personal or sensitive data in URL parameters or tracking

PASS.

Every package specifies UTM parameters limited to source, medium, campaign, content, and term.
No email address, phone number, name, device ID, subscriber ID, or any other personal value
appears in any defined URL parameter or tracking call.

Specific verifications:

- conversion-package.md sec 1.2 and 2.3: "No personal or sensitive data in URL parameters at
  any point. Ever." UTMs are source, medium, campaign, content only. Confirmation state fires
  in-place with no URL echo of personal data.
- tracking-plan.md sec 7: explicit parameter table. Six parameters defined, all non-identifying.
  The event_id is a random token with a rule that it must not encode or derive from personal data.
  CAPI payloads are restricted to non-PII fields until consent is confirmed.
- paid-launch-package.md UTM taxonomy: all values are lowercase with hyphens, no personal
  identifiers, no email fragments, no user IDs, no session tokens. Confirmed across all channels.
- organic-package.md sec 4: tracking URLs carry only source, medium, and campaign identifiers.
- pr-package.md sec 4: any tracking parameter in press-release links carries outlet-level
  attribution only, not a personal identifier.
- aso-package.md sec 6: deep-linking note explicitly flags the CLAUDE.md hard rule against
  personal data in URL parameters.
- copy-package.ar.md and copy-package.en.md: CTAs use placeholder links; no personal data is
  embedded in any link construction shown.

No fix required.

---

### Check 2: Consent correctness

PASS (design level, with open items).

Email consent basis: the gate form (conversion-package.md sec 1.4 Section D) presents a
privacy notice at the point of collection, before the submit button. The notice states the
purpose (early-access notification and lifecycle communication), includes an unsubscribe
mechanism, and commits not to share data with third parties. The consent basis is affirmative
opt-in at the gate. This is the correct basis for email marketing to a new contact.

The email bodies (copy-package.en.md email-en-s1-v1 and email-en-s1-v2) include an unsubscribe
link and a preference link in the footer. The Arabic email variants (copy-package.ar.md section
2) are referenced by ID and must carry equivalent unsubscribe mechanisms when produced. The
lifecycle-package.md correctly identifies unsubscribed contacts as a suppression class.

WhatsApp consent basis: if the WhatsApp gate is selected, the design requires a platform-side
opt-in confirmation message before any lifecycle send. This is correct under WhatsApp Business
API policy (double opt-in in practice) and consistent with a consent-based basis under PDPL.

App push consent basis: the lifecycle-package.md suppresses push opt-outs. The aso-package.md
sec 5.3 specifies the native OS review request API only (SKStoreReviewRequest and ReviewManager),
which uses the operating system's own consent mechanism. No custom review-gate that filters by
predicted sentiment is in the design, which is correct: that practice violates both stores'
policies and is absent from the spec.

CAPI hashed PII: tracking-plan.md sec 5 explicitly states that no hashed PII is sent in CAPI
payloads until the Saudi PDPL consent and residency framework is confirmed. This is the correct
posture. It is also surfaced as an open item.

Retargeting and lookalike audiences: paid-launch-package.md open item 5 and checklist item 10
correctly identify that consent basis for retargeting and lookalike audience construction is
blocked pending compliance clearance. All retargeting ad sets are staged paused. This is the
correct posture.

One design gap to surface as an open item (not a fail, because the platforms are unconfirmed):

OPEN ITEM C-01. The privacy notice at the gate (conversion-package.md sec 1.4 Section D) does
not name Maharat as the data controller by name in the displayed text. The current text reads:
"بتسجيلك، توافق على أن نتواصل معك بشأن الدخول المبكر لمهارات. لن نشارك بياناتك مع أطراف
خارجية. يمكنك إلغاء الاشتراك في أي وقت." and in English: "By registering, you agree that we
may contact you about Maharat early access. We will not share your data with third parties. You
can unsubscribe at any time." The conversion-package.md itself notes that the notice must name
the data controller. The notice text as drafted says "Maharat" in the context but does not
explicitly say "Maharat [legal entity name] is the data controller." Saudi PDPL Article 15
requires the controller to be identified. Before go-live, the notice must explicitly state the
data controller name (legal entity name, not just brand name). Route to conversion-engineer.

OPEN ITEM C-02. The privacy policy URL is an open item (conversion-package.md sec 1.4 Section
D and Section F). A link to the full Maharat privacy policy must appear at or adjacent to the
point of collection. Go-live is blocked until this URL is confirmed and the policy is live.
Route to conversion-engineer and the web team.

---

### Check 3: Suppression correctness

PASS.

The suppression design is complete and correct. The lifecycle-package.md consolidates the
suppression set explicitly:

- Active subscribers (already paying, list 5, approximately 5,000 contacts): excluded from all
  email and push sends.
- Failed-payment contacts (list 1): excluded from all sends; in their own recovery flow.
- Unsubscribed contacts: excluded from all email sends.
- Hard-bounced addresses: excluded from all email sends.
- Push opt-outs: excluded from all push sends.
- Existing Skill Paths early-access members: excluded from all sends (suppression source
  flagged as to-confirm before send).
- Contacts who completed signup during the flight: suppressed from msg-3 and push-3 (converted
  contacts).
- Deep-dormant contacts (no open or click in more than 365 days) not yet through the sunset
  flow: excluded from the main email flow.

The paid-launch-package.md stages customer and early-access-member suppression lists as custom
audience exclusions across all paid channels. The source is flagged as to-confirm before go-live.

The lifecycle-package.md specifies that suppression lists must be confirmed automated and
verified within 24 hours of each send date, not at design time. This is the correct operational
stance.

OPEN ITEM C-03. The source for the existing Skill Paths early-access members suppression list
is flagged to-confirm in both the lifecycle-package.md and the paid-launch-package.md. This
must be confirmed as available and queryable before send and before go-live on paid. If the
source is empty, that must also be confirmed. Route to lifecycle-architect and paid-build-engineer.

OPEN ITEM C-04. The converted-contacts suppression before msg-3 and push-3 depends on the
lifecycle_ea_signup_complete event being queryable from the warehouse by 2026-07-11. This
dependency is correctly called out in the lifecycle-package.md coordination table. The human
gate must confirm that data-tracking-engineer has this event wired and the warehouse view is
live before msg-3 and push-3 can send. Route to data-tracking-engineer.

---

### Check 4: Saudi PDPL and data residency

OPEN ITEMS SURFACED. Not resolved. Not blocked by this reviewer.

The following items are unresolved and must be decided by Ahmed at the human gate. This
reviewer does not invent an answer to any of them.

OPEN ITEM C-05. Saudi PDPL data-residency decision for the email and WhatsApp sending platform.
The platform is unconfirmed. Once a platform is named, the data-residency question must be
assessed: where does the platform store personal data of Saudi residents, is a cross-border
transfer involved, and does it comply with Saudi PDPL Article 29 requirements for cross-border
transfer (either the transferred country provides an equivalent level of protection, or the
controller ensures adequate safeguards, or the data subject consents to the transfer). This
blocks live send wiring. Route to Ahmed and the legal team.

OPEN ITEM C-06. Saudi PDPL data-residency decision for the app push platform. Same requirement
as C-05. The push platform is unconfirmed. Route to Ahmed and the legal team.

OPEN ITEM C-07. Saudi PDPL data-residency decision for the MMP (mobile measurement partner).
No MMP has been named. When named, the residency assessment must cover: where the MMP processes
and stores install event data tied to device identifiers, whether that constitutes personal data
under PDPL, and what cross-border transfer safeguards apply. Route to Ahmed and the legal team.

OPEN ITEM C-08. Cross-border hashed-list uploads for custom audiences on Meta, TikTok, and
Google. The design specifies hashed customer and early-access lists as custom audience exclusions
and lookalike seeds. Uploading a hashed list to a US-based advertising platform constitutes a
cross-border transfer of personal data under Saudi PDPL. The hashing of email or phone prior to
upload mitigates some risk but does not eliminate PDPL obligations. The basis for this transfer
must be confirmed (consent, contractual necessity, or other recognized basis) before the
suppression lists are uploaded to any platform. This is a blocker for retargeting and lookalike
audience activation. The paid-launch-package.md correctly stages this as blocked (open item 5,
checklist item 10). Route to Ahmed and the legal team.

OPEN ITEM C-09. CAPI hashed PII. The tracking-plan.md correctly holds hashed PII out of CAPI
payloads until consent and residency are confirmed. This must remain held until C-05 and C-08
are resolved and explicitly cleared by Ahmed. No CAPI match-rate optimization using email or
phone hashes until cleared. Route to data-tracking-engineer to confirm the hold remains.

---

### Check 5: No accreditation implication

PASS.

No package, copy variant, or asset spec implies that Maharat certificates are accredited.

Specific verifications:

- copy-package.ar.md sec 4 AR-SOCIAL-09: "شهادة إتمام" (completion certificate), with an
  explicit guardrail note that no accreditation is stated or implied. Correct.
- copy-package.en.md social-en-post-9: "completion certificate" only, with an explicit
  guardrail note. Correct.
- copy-package.en.md email-en-s1-v1: uses "completion certificate" only. Correct.
- aso-package.md sec 2.3: description direction explicitly states "certificates of completion
  (not accredited)." Correct.
- pr-package.md sec 1 guardrail check: "No accreditation claim: PASS." Confirmed throughout.
- conversion-package.md sec 1.5 operational verification: "No accreditation claim appears
  anywhere on the page." Confirmed as a blocking check.

No fix required.

---

### Check 6: Data-flow disclosure

PASS (with open item C-01 and C-02 above, which must be resolved before go-live).

The conversion-package.md places the privacy notice at the point of collection, directly below
the form fields and before the submit button. This is the correct placement for PDPL-compliant
disclosure.

The pr-package.md and organic-package.md do not collect personal data at the point of the
publish action. They route traffic to the signup gate where disclosure occurs.

The aso-package.md store listing does not collect personal data directly. The app stores handle
their own data collection under their own policies. The in-app review solicitation uses the
native OS API, which operates under OS-level consent, not a custom collection point.

The lifecycle sends and push notifications go to contacts who have already provided consent at
the gate or who have the app installed with push opted in. No new data collection occurs at
the point of send.

Data flow summary for disclosure purposes:

1. Landing page gate: collects name (first name only) and email, or WhatsApp number. Purpose
   disclosed at collection point. Privacy policy link required (open item C-02). Correct design.
2. Pixel and CAPI: collects behavioral events (page view, gate view, submit, confirm). No PII
   in events until CAPI PII hold is lifted (open item C-09). Non-identifying event data does
   not require individual-level disclosure at the collection point, but must be covered by the
   privacy policy. Privacy policy must describe pixel and behavioral tracking. Open item C-02
   covers this: the policy must be confirmed live before go-live.
3. MMP and app analytics: app install and activation events. Covered by the app store privacy
   disclosures and the in-app privacy policy. MMP selection is open (open item C-07).
4. Email and push sends: use data collected at the gate. No new collection at send time.
5. Cross-border audience uploads: blocked pending C-08 resolution.

---

### Check 7: Data minimization, retention, data-subject rights

OPEN ITEMS SURFACED. Not resolved. Not a fail on design, because these are items the packages
correctly flag but cannot resolve without legal input. The human gate must see them.

Data minimization: PASS on design. The gate collects first name and email, or WhatsApp number
only. No national ID, surname, date of birth, financial data, or health data. The tracking plan
collects only non-identifying event parameters. Minimization is applied correctly in the design.

Retention policy: OPEN ITEM C-10. The conversion-package.md sec 2.3 explicitly flags "Retention
and deletion policy: confirm with legal or compliance before the form goes live. OPEN ITEM."
Saudi PDPL Article 18 requires that personal data is not kept longer than necessary for the
purpose. A retention period must be defined and documented before go-live. Route to Ahmed and
the legal team.

Data-subject rights (access and deletion): OPEN ITEM C-11. No package specifies a mechanism
for data subjects to exercise PDPL rights (Articles 4 and 5: right to access personal data,
right to request correction, right to request destruction). The privacy policy (open item C-02)
must describe these rights and provide a contact route. This is a PDPL requirement. Before the
gate is live, the privacy policy must cover this. Route to Ahmed and the legal team.

Double opt-in for email: OPEN ITEM C-12. The conversion-package.md sec 2.2 notes: "A double
opt-in confirmation email is sent to the submitted address if required by the platform or
applicable law. OPEN ITEM: confirm whether double opt-in is required." Under Saudi PDPL, a
single affirmative opt-in at the gate is technically a valid consent basis. However, double
opt-in is a best practice that provides a stronger evidence trail for consent and protects
against address harvesting. Whether to require double opt-in is an Ahmed and legal-team
decision. It must be resolved before the platform is wired. Route to Ahmed.

---

### App-store review-solicitation policy compliance

PASS.

The aso-package.md sec 5.3 specifies: "The in-app prompt uses the native OS review request API
(SKStoreReviewRequest on iOS, ReviewManager on Android). No custom review-gate that filters by
predicted sentiment; that practice violates both stores' policies."

This is the correct approach. Both Apple App Store guidelines and Google Play Developer Policy
prohibit apps from directing users to a custom gate that only routes positive reviewers to the
store. The design uses the native APIs, which do not allow sentiment filtering. Correct.

The timing limit is set to no more than once per 365 days per user, after a positive milestone.
This is consistent with Apple's recommendation to prompt infrequently and contextually.

No fix required.

---

## Open items summary for the human gate

All open items below must be seen by Ahmed before any live action is authorized. None is
resolved by this reviewer. Each is flagged with its route.

| ID | Item | Route | Blocks |
|---|---|---|---|
| C-01 | Privacy notice must name the data controller by legal entity name. Current text implies Maharat but does not state the legal entity name explicitly. | conversion-engineer | Go-live on gate |
| C-02 | Privacy policy URL not confirmed. Policy must be live and linked at the point of collection and in the footer before the gate goes live. Policy must cover pixel tracking, data-subject rights, and retention. | conversion-engineer, web team, legal | Go-live on gate |
| C-03 | Source for existing Skill Paths early-access members suppression list not confirmed. Must be confirmed available and queryable before send and before paid go-live. | lifecycle-architect, paid-build-engineer | Send, paid go-live |
| C-04 | lifecycle_ea_signup_complete event must be queryable from the warehouse by 2026-07-11 to power converted-contact suppression before msg-3 and push-3. | data-tracking-engineer | msg-3 send, push-3 send |
| C-05 | Saudi PDPL data-residency decision for the email and WhatsApp sending platform. Platform unconfirmed. Residency assessment required when platform is named. | Ahmed, legal team | Platform wiring, live send |
| C-06 | Saudi PDPL data-residency decision for the app push platform. Same as C-05. | Ahmed, legal team | Push platform wiring, live push |
| C-07 | Saudi PDPL data-residency decision for the MMP. No MMP named. When named, residency assessment required. | Ahmed, legal team | MMP wiring, app-install attribution |
| C-08 | Cross-border hashed-list uploads to Meta, TikTok, and Google for custom audiences. Transfer basis must be confirmed under PDPL before any list is uploaded. Blocks retargeting and lookalike activation. | Ahmed, legal team | Retargeting go-live, lookalike go-live |
| C-09 | CAPI hashed PII hold must remain in place until C-05 and C-08 are resolved and cleared by Ahmed. Confirm hold is operationally enforced. | data-tracking-engineer | CAPI match-rate optimization |
| C-10 | Retention and deletion policy not confirmed. PDPL requires data is kept no longer than necessary. Policy must be defined before the gate goes live. | Ahmed, legal team | Go-live on gate |
| C-11 | Data-subject rights mechanism (access, correction, deletion per PDPL) not specified in any package. Privacy policy must cover this and provide a contact route before the gate goes live. | Ahmed, legal team | Go-live on gate |
| C-12 | Double opt-in requirement for email not resolved. Ahmed and legal team must decide before the platform is wired. | Ahmed, legal team | Platform wiring |

---

## What this verdict covers and does not cover

Covers: all data collection points, tracking calls, UTM parameters, consent and suppression
design, Saudi PDPL and cross-border data-residency gaps, data-flow disclosure, accreditation
claims, app-store review-solicitation policy, data minimization and retention gaps, data-subject
rights gaps. Reviewed against CLAUDE.md hard rules, Saudi PDPL Articles 4, 5, 15, 18, and 29,
and standard email and push consent requirements.

Does not cover: copy tone, brand voice, visual constants, Arabic rendering, or RTL correctness.
Those are for arabic-copy-qa, english-copy-qa, design-qa, and brand-qa-reviewer.

Does not resolve: any of the 12 open items above. They are surfaced, not answered. The human
gate decides.

---

## Handoff

This verdict attaches to the human-gate package. The package may proceed to the human gate
carrying this verdict and all 12 open items visible to Ahmed.

None of the 12 open items is a structural design fail that returns this package to an owning
agent. They are either (a) decisions only Ahmed and the legal team can make (C-05 through C-12),
or (b) execution-time confirmations that are correctly staged as blocked in the packages (C-03,
C-04), or (c) pre-go-live text fixes that convert-engineer must apply before the gate is built
(C-01, C-02).

No live send, spend, publish, pixel write, CAPI call, store-console update, or platform
wiring may proceed until: (1) this verdict is seen by Ahmed, (2) the applicable open items for
that specific action are resolved, and (3) Ahmed provides explicit per-action, per-campaign
approval at the human gate.

This verdict is a gate contribution, not an approval. The human gate is separate and decisive.

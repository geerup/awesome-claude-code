# compliance-verdict: 2026-06-elda-choucair-marketing

gate:        compliance-privacy-check
produced_by: compliance-privacy-reviewer
campaign_id: 2026-06-elda-choucair-marketing
stream:      cross-cutting gate, runs alongside brand-qa-reviewer for streams 6 and 7 and all
             send, publish, and data-collection actions
checked:     no-pii-in-urls, consent-correct, suppression-correct, pdpl-residency-surfaced,
             data-flows-disclosed, no-accreditation-implication, data-minimization,
             retention-stance, data-subject-rights, no-tool-adoption
date:        2026-06-05

---

## Re-verification note (2026-06-05)

Two checks that previously returned FAIL were reworked by the owning agents and resubmitted
on 2026-06-05. Only those two checks were re-verified. All other checks and all go-live
blockers in section 3 are unchanged.

retention-stance: conversion-engineer added section 2.5 (Data Retention and Deletion) to
the conversion-package, and lifecycle-architect added section 4A (Data retention and deletion)
to the lifecycle-package. Both packages now state a design-level retention stance (active
relationship plus post-relationship window, deletion on unsubscribe, hard bounce, or verified
deletion request) with all concrete durations marked PENDING legal/PDPL confirmation. No
confirmed legal value was invented. The check is now PASS (design-stage). Concrete retention
durations and the legal basis under Saudi PDPL remain pending and join the go-live blockers.

data-subject-rights: conversion-engineer added section 2.6 (Data-Subject Rights) to the
conversion-package, and lifecycle-architect added a "Data-subject rights route" block in
section 4A of the lifecycle-package. Both packages now state access, correction, deletion,
and objection rights and specify a request route (privacy contact or rights request form)
linked from the gate privacy notice and privacy policy. The concrete contact address and form
URL are consistently left as PENDING legal/Ahmed confirmation across both packages. No
confirmed address was invented. The check is now PASS (design-stage). The live contact
address and form URL remain pending and join the go-live blockers.

Both reworked checks now PASS at design stage. Nothing here authorizes any live data
collection. Every go-live blocker in section 3 (items 1 through 10) remains in force, with
the concrete retention durations and DSR contact/URL now added as additional pending-legal
items under open items 6 and 7.

---

## Overall verdict

PASS (design-stage only)

This is a design-stage pass only. No asset in this campaign currently collects data, sends,
or publishes. The verdict attaches to the human-gate package. It does not authorize any live
send, data collection, or spend. Nothing goes live until every blocking open item in section 3
is resolved and Ahmed gives explicit per-action approval at the human gate.

The verdict is conditional: if any blocking open item is resolved in a way that introduces PII
in URLs, unconfirmed consent wiring, or an unapproved platform, this gate must run again on
the updated spec before the package resubmits to the human gate.

---

## Per-asset findings

### Asset 1: lifecycle-package.md (stream 7, non-payer email flow)

Checks run: no-pii-in-urls, consent-correct, suppression-correct, pdpl-residency-surfaced,
data-flows-disclosed, no-accreditation-implication, data-minimization, retention-stance,
data-subject-rights, no-tool-adoption

**no-pii-in-urls: PASS**
The package explicitly states in section 6B: "no personal or sensitive data is placed in any
URL parameter or event property. Contact identity is tracked by an anonymous contact_id or
session_id, never by name, email address, or phone number." UTM parameters carry source and
medium values only. No PII detected in any link, UTM, or described tracking call.

**consent-correct: PASS (design stage, conditional)**
The flow targets the owned non-payer list. Consent basis for the existing list is assumed to
be an existing marketing opt-in. The consent basis for new leads entering via the signup gate
is covered by the gate consent notice (conversion-package, section 2.4). The package
correctly flags double opt-in as an open question for this gate to answer (lifecycle-package
section 2.3, open item listed). No pre-checked consent is described. The consent mechanism
is not yet wired because the platform is unconfirmed. Conditional pass: the consent mechanism
must be verified against the confirmed platform before any send. The double opt-in question
is surfaced as open item 4 in section 3 of this verdict.

**suppression-correct: PASS (design stage, conditional)**
Suppression is stated explicitly and correctly in sections 2C and 5: paying subscribers,
unsubscribed, hard-bounced. The suppression-list source is flagged as an open item. The logic
is described, not yet applied (no platform is wired). Conditional pass: suppression must be
confirmed applied in the platform before any send. Open item 3 in section 3 of this verdict.

**pdpl-residency-surfaced: PASS**
The Saudi PDPL and data-residency open item is explicitly surfaced in section 9, item 12:
"Saudi PDPL data-residency decision: the Saudi Personal Data Protection Law data-residency
requirement for the email platform is pending." It is attached to the platform decision and
routed to the human gate. Not invented, not resolved. Pass.

**data-flows-disclosed: PASS (design stage, conditional)**
The package states that data is received by the email/CRM platform (named as Ortto or
HubSpot, unconfirmed), and contact records are created there. The platform is not yet named.
The consent notice on the gate (conversion-package) references the Maharat privacy policy as
the disclosure point. Conditional pass: the specific platform must be named in the privacy
policy and consent notice before any data is collected. Open item 1 in section 3 of this
verdict.

**no-accreditation-implication: PASS**
No reference to accreditation appears anywhere in the lifecycle-package. Completion
certificate language is absent; no claim of accreditation is made. Pass.

**data-minimization: PASS (design stage)**
The email flow collects only: email address at the gate, behavioral signals from email
engagement (opens, clicks, event triggers). The package states minimum-viable data collection
as both a UX and PDPL principle (conversion-package section 2.2). No additional fields beyond
email are described at the baseline gate. UTM source and medium are non-identifying
campaign parameters. Pass at design stage. Confirm at build that no additional fields are
introduced by the platform without a stated purpose.

**retention-stance: PASS (design stage)**
Section 4A (Data retention and deletion) added by lifecycle-architect states a design-level
retention stance: contact records and engagement data held for the active relationship, then
deleted within a post-relationship window on unsubscribe, hard bounce, or verified deletion
request. All concrete durations are marked PENDING legal/PDPL confirmation. No confirmed
legal value was invented. This clears the prior FAIL: a stance is stated and a deletion path
exists. Concrete retention durations remain pending and are a go-live prerequisite (open
item 6 in section 3 of this verdict, updated below).

**data-subject-rights: PASS (design stage)**
Section 4A ("Data-subject rights route") added by lifecycle-architect states access,
correction, and deletion rights and specifies a request route (privacy contact or rights
request form) linked from the privacy notice and privacy policy, consistent with what
conversion-engineer states in section 2.6. The concrete contact address and form URL are
correctly left as PENDING. This clears the prior FAIL: a DSR route is now stated and linked
from the gate privacy notice, and it is consistent across both packages. The live contact
address and form URL remain pending and are a go-live prerequisite (open item 7 in section 3
of this verdict, updated below).

**no-tool-adoption: PASS**
The package names Ortto and HubSpot as the platform candidates and explicitly does not wire
either. The platform is flagged as an open item for Ahmed. No tool is adopted or wired. Pass.

---

### Asset 2: conversion-package.md (stream 6, landing page, signup gate, event tracking)

Checks run: no-pii-in-urls, consent-correct, suppression-correct, pdpl-residency-surfaced,
data-flows-disclosed, no-accreditation-implication, data-minimization, retention-stance,
data-subject-rights, no-tool-adoption

**no-pii-in-urls: PASS**
Section 3.2 states: "HARD RULE: no email address, phone number, name, user ID, device ID, or
any personal or sensitive value appears in any URL parameter, UTM value, or event parameter."
The email field is submitted as a POST body field only, never in a URL. The event_id is a
non-identifying token. UTM parameters carry source, medium, campaign, and content values only.
Test plan step 8 confirms the verification requirement at build. One nuance noted: CAPI
section 3.4 describes optional hashed PII transmission for match quality: "if CAPI match
quality requires hashed email or phone for the subscription_start event... it is hashed
(SHA-256, no salt) before transmission and never passed in any URL parameter." This is
compliant as described (hash transmitted server-side via CAPI only, not in any URL parameter),
and ownership is correctly assigned to data-tracking-engineer. Pass.

**consent-correct: PASS (design stage, conditional)**
The consent notice is present in the gate spec (section 1.2, section 3): "By submitting, you
agree to Maharat's privacy policy and to receive updates from us" / "بالاشتراك، أوافق على
سياسة الخصوصية وتلقي التحديثات من ماهرات." The notice links to the Maharat privacy policy.
No pre-checking. The package correctly flags this as a compliance blocker: "The
compliance-privacy-reviewer must approve the exact wording and confirm Saudi PDPL compliance
before go-live. The wording above is a placeholder, not an approved legal text." Double
opt-in requirement is flagged as open item 11. Conditional pass: the exact consent notice
wording must be legally reviewed and approved before go-live. The privacy policy URL must be
live. The double opt-in question must be answered. Open items 4 and 5 in section 3 of this
verdict.

**suppression-correct: PASS (design stage, conditional)**
Section 1.2 (gate suppression note) correctly states that suppression is applied at send time
by the platform/lifecycle, not at the page level: "the gate always accepts the email
submission; deduplication and suppression happen in the CRM." This is correct architecture.
The suppression rules (paying subscribers, unsubscribed, hard-bounced) are stated in the
lifecycle-package section 2C. Conditional pass on the same open item as the lifecycle-package:
suppression-list source must be confirmed applied before any send. Open item 3.

**pdpl-residency-surfaced: PASS**
Section 2.4 explicitly lists: "Saudi PDPL compliance confirmation: the compliance-privacy-reviewer
must confirm that the data collection, storage, and processing of Saudi residents' email
addresses complies with the Personal Data Protection Law (PDPL) of Saudi Arabia." And:
"Data-residency confirmation: if the platform (Ortto or HubSpot) stores contact data outside
Saudi Arabia, the compliance-privacy-reviewer must confirm this is permissible under PDPL."
Both items are surfaced, not resolved. Pass.

**data-flows-disclosed: PASS (design stage, conditional)**
The package states that on submission, the platform API receives the email address, UTM
values, and a campaign tag. The platform creates or updates a contact record. The consent
notice links to the privacy policy, which is the point-of-collection disclosure. The specific
platform is not named (it is unconfirmed), so the privacy policy cannot yet name it.
Conditional pass: the privacy policy must name the receiving platform and any pixel or
third-party data processors before go-live. Open item 1.

**no-accreditation-implication: PASS**
No reference to accreditation appears on the landing page spec, in any value card, in the
hero copy, in the gate copy, or in any CTA. The class is described as a masterclass. No
certificate language appears on the page. Pass.

**data-minimization: PASS (design stage)**
Gate fields: email address only at baseline. No name, no phone, no company, no date of birth.
Section 2.2 explicitly states this is a data-minimization principle. WhatsApp number is
conditional and blocked. Event parameters carry only non-identifying values (event_id,
campaign, content_group, source, medium). Pass.

**retention-stance: PASS (design stage)**
Section 2.5 (Data Retention and Deletion) added by conversion-engineer states a design-level
retention stance: contact and engagement records held for the active relationship, then deleted
or anonymized within a post-relationship window (placeholder "within 30 days" explicitly
marked as a placeholder that must be confirmed by legal, not a confirmed legal value). Deletion
is triggered by unsubscribe, hard bounce, or verified deletion request. All concrete durations
are PENDING legal/PDPL confirmation. No confirmed legal value was invented. This clears the
prior FAIL: a stance is stated and a deletion path exists. Concrete retention durations remain
pending and are a go-live prerequisite (open item 6 in section 3 of this verdict, updated
below).

**data-subject-rights: PASS (design stage)**
Section 2.6 (Data-Subject Rights) added by conversion-engineer specifies access, correction,
deletion, and objection rights and states the request route as a designated privacy contact
or form (proposed placeholder "privacy@maharat.com, not confirmed" is explicitly marked
unconfirmed). Both the gate privacy notice and the live privacy policy are required to include
this route before go-live. The concrete contact address and form URL are correctly left as
PENDING legal/Ahmed confirmation. This clears the prior FAIL: a DSR route is now stated,
linked from the gate privacy notice, and consistent with the lifecycle-package. The live
contact address and form URL remain pending and are a go-live prerequisite (open item 7 in
section 3 of this verdict, updated below).

**no-tool-adoption: PASS**
Meta Pixel, CAPI, GA4, LinkedIn Insight Tag, and Google Tag are all described as "to-confirm"
with data-tracking-engineer. None is wired or adopted here. All are correctly flagged as open
items. Pass.

---

### Asset 3: media-plan.md (paid audiences, retargeting, lookalike, Pixel/CAPI/Insight Tag)

Checks run: no-pii-in-urls, consent-correct, suppression-correct, pdpl-residency-surfaced,
data-flows-disclosed, no-accreditation-implication, data-minimization, no-tool-adoption

Note on scope: the media-plan is an internal strategy document. It describes audience
definitions, budget logic, and pre-spend dependencies. It does not collect data, send, or
publish directly. The compliance gate applies because it specifies retargeting, lookalike
audiences, custom audience uploads, and pixel/CAPI events that will collect and process
personal data when live. The gate reviews the design of those flows.

**no-pii-in-urls: PASS**
Section 8 (attribution note): "UTM parameters track source (paid channel) and campaign. They
carry no personal or sensitive data." Section 4 (all audience definitions): no personal
identifiers in any audience definition. Lookalike seed: section 4 describes it as "a hashed
custom audience" upload. Suppression exclusions: "custom audience upload from CRM, hashed."
The plan correctly prohibits PII in URLs and describes hashed handling for custom audience
uploads. Pass.

**consent-correct: PASS (design stage, conditional)**
The retargeting and lookalike audiences depend on the pixel or CAPI being live, which depends
on the consent mechanism being wired at the gate. Section 5 (bid strategy) explicitly states:
"A compliance and privacy check is required on the consent mechanism before any tag fires."
This is the correct sequencing: no tag fires until the consent mechanism is confirmed by this
gate. Conditional pass: retargeting and pixel-based audiences cannot activate until the gate
consent mechanism is confirmed. Open item 2 in section 3 of this verdict.

**suppression-correct: PASS (design stage, conditional)**
The plan correctly excludes existing paying subscribers and prior gate completions from all
paid ad sets (section 4, Meta exclusions). It flags this as an open item dependent on the CRM
being named and accessible (section 9, item 11: "The paid audience strategy cannot fully
exclude existing subscribers without this list"). Conditional pass: exclusion custom audience
upload requires the platform to be named. Open item 1.

**pdpl-residency-surfaced: PASS**
Section 9, item 3 (pixel or CAPI deployment) states: "A compliance and privacy check is
required on the consent mechanism before any tag fires." The plan defers to this gate for
the PDPL and consent question. The PDPL and data-residency open item is inherited from the
platform decision (open item 1 in this verdict). Pass: the plan does not assume it resolved
and defers the live decision to this gate and the human gate.

**data-flows-disclosed: PASS (design stage)**
The plan names every tag and data flow it proposes: Meta Pixel, CAPI, Google Ads tag,
LinkedIn Insight Tag, GA4. All are flagged as "to-confirm" and owned by data-tracking-engineer.
No tag is wired. Disclosure to the user happens at the point of collection via the gate
privacy notice (conversion-package), not by the media plan itself. The media plan correctly
attributes disclosure responsibility to the gate. Pass at design stage.

**no-accreditation-implication: PASS**
Ad creative copy references in the plan use only approved phrasing: "20 years in one class,"
"marketing is decision architecture," empowering framing. No accreditation language. Pass.

**data-minimization: PASS**
Audience definitions use interest, behavior, job-function, and geo signals, which are
aggregate platform-level signals, not personal data collected by Maharat. Custom audience
uploads are described as hashed. Event parameters feeding the bid optimization are the same
non-identifying events described in the conversion-package. Pass.

**no-tool-adoption: PASS**
All platform tools (Meta Ads Manager, Google Ads, LinkedIn Campaign Manager) are described
as the channels the media plan targets. None is adopted or wired by the media-plan agent.
Build is deferred to paid-build-engineer. Pass.

---

### Asset 4: organic-package.md (organic publishing, UTM/tracking, no PII)

Checks run: no-pii-in-urls, consent-correct (not directly applicable, posts do not collect
data), suppression-correct (not directly applicable), pdpl-residency-surfaced (not directly
applicable to post publishing), data-flows-disclosed, no-accreditation-implication,
data-minimization (posts do not collect data at the post level), no-tool-adoption

**no-pii-in-urls: PASS**
Section 5 (distribution routing): "No personal or sensitive data in any URL parameter."
All URLs are class page URLs without query strings at the time of this package. Section 7,
item 2 (UTM tracking schema) is correctly flagged as an open item, with the explicit
instruction: "Do not add tracking parameters to URLs in this package until the schema is
confirmed and reviewed." No UTM parameters are built into any post URL in this package.
Pass.

**data-flows-disclosed: PASS (not applicable at design stage)**
Organic posts route visitors to the class page, where the gate (conversion-package) handles
data collection and disclosure. The organic package does not itself collect personal data.
Any community engagement reply that touches data-collection questions is escalated to
compliance-privacy-reviewer before any public reply (section 6, escalation rules). Pass.

**no-accreditation-implication: PASS**
Section 6 (community engagement, reply patterns): "The class issues a completion certificate.
It is not accredited. Do not imply accreditation. Route to the class page for certificate
details if relevant. Escalate to compliance-privacy-reviewer before any public reply on this
topic." The reply-pattern table explicitly blocks any accreditation implication. Section 9
(pre-handoff checklist): "No accreditation implication: None. Confirmed." Pass.

**no-tool-adoption: PASS**
Blotato MCP is noted in the package as adopted on the allowlist but credential-gated and not
invoked. The video slot is held until trailer rights are confirmed and the API key is present.
No tool is wired or activated. Pass.

**consent-correct: not applicable (organic posts do not collect data)**
Organic posts route to the class page; data collection happens at the gate. The escalation
rules require compliance-privacy-reviewer review before any data-collection question is
answered in comments. The organic package does not create a consent obligation itself. n/a.

**suppression-correct: not applicable (organic posts are public-reach, not a send)**
No audience suppression is required for organic publishing. n/a.

**data-minimization: not applicable (organic posts do not collect data at the post level)**
n/a.

---

## Summary of check results across all assets

| Check | lifecycle | conversion | media-plan | organic |
|---|---|---|---|---|
| no-pii-in-urls | PASS | PASS | PASS | PASS |
| consent-correct | PASS (conditional) | PASS (conditional) | PASS (conditional) | n/a |
| suppression-correct | PASS (conditional) | PASS (conditional) | PASS (conditional) | n/a |
| pdpl-residency-surfaced | PASS | PASS | PASS | n/a |
| data-flows-disclosed | PASS (conditional) | PASS (conditional) | PASS (conditional) | PASS |
| no-accreditation-implication | PASS | PASS | PASS | PASS |
| data-minimization | PASS (conditional) | PASS (conditional) | PASS | n/a |
| retention-stance | PASS (design-stage) | PASS (design-stage) | n/a | n/a |
| data-subject-rights | PASS (design-stage) | PASS (design-stage) | n/a | n/a |
| no-tool-adoption | PASS | PASS | PASS | PASS |

All ten checks now pass at design stage. The two previously failing checks (retention-stance
and data-subject-rights) were reworked and resubmitted; they pass at design stage as of
2026-06-05. Concrete legal values (retention durations and DSR contact/URL) remain pending
and are go-live prerequisites. Nothing sends until all blocking open items in section 3
are resolved and Ahmed gives explicit approval at the human gate.

---

## Section 3: open items that block any live send, spend, or data collection

Numbered, in priority order. Each item states what must happen to clear it.

**1. PLATFORM CONFIRMATION (HARD BLOCKER, highest priority)**
The email and CRM platform is unconfirmed. The tension on record is Ortto (incumbent) vs a
HubSpot migration, with an unresolved Arabic RTL rendering concern on HubSpot. This single
open item blocks: send wiring, consent mechanism wiring, suppression-list confirmation,
event schema confirmation, persona tagging, language routing, trigger automation, privacy
policy naming of the data processor, custom audience exclusion uploads to Meta and LinkedIn,
and the retargeting readiness for paid media.
What must happen: Ahmed names the platform. An Arabic RTL rendering test must be run on the
named platform (per the platform research document). The platform selection lands in
settings.json as a confirmed entry. Once named, the consent mechanism, suppression logic,
and event wiring are designed against the confirmed platform and resubmitted to the
relevant gates.
Owner: Ahmed, with George and Vahakn (per REVIEW-QUEUE.md Phase 2 findings).

**2. SAUDI PDPL AND DATA-RESIDENCY CONFIRMATION (COMPLIANCE BLOCKER)**
The Saudi Personal Data Protection Law applies to the personal data of Saudi residents
collected via the signup gate and stored in the email/CRM platform. Whether the platform
stores contact data inside or outside Saudi Arabia, and whether that is permissible under
PDPL, is unresolved. This gate does not resolve it. It must not be assumed resolved.
What must happen: Ahmed engages legal or compliance counsel familiar with Saudi PDPL. The
data-residency question is answered in writing. If the platform stores data outside Saudi
Arabia, either: (a) a legal basis for cross-border transfer is confirmed (PDPL Article 29),
or (b) the platform selection shifts to a Saudi-resident or GCC-resident option (Unifonic
is noted in the platform research as relevant if residency is a hard requirement). The
outcome is documented and attached to the human-gate package before any data collection.
Owner: Ahmed, legal or compliance counsel.

**3. SUPPRESSION-LIST SOURCE CONFIRMATION (BLOCKING for any send)**
The canonical suppression list source (paying subscribers, unsubscribed, hard-bounced) is
not confirmed. The system holding each list, the extraction process, and the mechanism for
applying suppression in the send platform are all open.
What must happen: the platform operator and data team confirm which system holds each
suppression list, how it is extracted, and how it is applied in the email platform before
any send job is submitted. A pre-send suppression check (querying the live list immediately
before send) must be confirmed as part of the send workflow.
Owner: platform operator, data team, lifecycle-architect.

**4. DOUBLE OPT-IN REQUIREMENT (COMPLIANCE OPEN ITEM)**
Whether Saudi PDPL requires explicit double opt-in for email marketing consent, or whether
implied consent with a clear privacy notice at the point of submission is sufficient, is not
confirmed. The consent notice wording in the conversion-package is a placeholder.
What must happen: legal or compliance counsel confirms the requirement. If double opt-in is
required, the conversion-package confirm event definition, the post-submit copy, and the
consent wording are updated accordingly and resubmit to this gate. If single opt-in with a
clear notice is sufficient, the notice wording is finalized and submitted to this gate for
approval before go-live.
Owner: compliance counsel, conversion-engineer.

**5. PRIVACY NOTICE WORDING AND PRIVACY POLICY URL (COMPLIANCE BLOCKER)**
The consent notice in the gate is a placeholder: "By submitting, you agree to Maharat's
privacy policy and to receive updates from us." This wording has not been reviewed or
approved as legally sufficient. The privacy policy URL is not yet live.
What must happen: legal or compliance counsel reviews and approves the consent notice
wording for both Arabic and English variants. The privacy policy is published at a live URL.
The notice in the gate is updated with the approved wording and a live link. The privacy
policy must name the data controller, the receiving platform, the data processed, the
retention period (once confirmed, per open item 6 below), and the data-subject rights route
(once confirmed, per open item 7 below). The conversion-engineer resubmits the updated notice
to this gate for final approval before go-live.
Owner: legal or compliance counsel, conversion-engineer.

**6. RETENTION STANCE: CONCRETE DURATIONS AND LEGAL BASIS (PDPL AND GDPR REQUIREMENT,
BLOCKING for go-live)**
The design-level retention stance is now stated in both the conversion-package (section 2.5)
and the lifecycle-package (section 4A). The retention-stance check passes at design stage.
What remains open: the concrete post-relationship retention duration (proposed design intent
is 30 days but explicitly marked as a placeholder), the backup-purge schedule, and the
deletion-response window must each be confirmed by legal under Saudi PDPL before they can
appear in the live privacy policy or be communicated to any data subject. The platform
deletion mechanism (scheduled job or automated purge) must also be confirmed at build.
What must happen: legal confirms the retention periods and legal basis. Conversion-engineer
and lifecycle-architect update their packages with the confirmed values. The privacy policy
is updated to reflect the confirmed periods. Both packages resubmit to this gate after the
confirmed values are added.
Owner: legal or data owner (confirmed periods), conversion-engineer and lifecycle-architect
(package updates and privacy policy), data-tracking-engineer (platform deletion mechanism).

**7. DATA-SUBJECT RIGHTS ROUTE: LIVE CONTACT AND FORM URL (PDPL AND GDPR REQUIREMENT,
BLOCKING for go-live)**
The design-level DSR spec is now stated in both packages (conversion-package section 2.6,
lifecycle-package section 4A). Access, correction, deletion, and objection rights are
stated and the request route is specified. The data-subject-rights check passes at design
stage. What remains open: the concrete privacy contact email address (proposed placeholder
"privacy@maharat.com" is explicitly marked as not confirmed) and the rights request form URL
must be confirmed by legal or the data owner before they can be stated in the privacy notice,
the privacy policy, or any lifecycle email. The two packages must use the same confirmed
address and URL.
What must happen: Ahmed and legal confirm the privacy contact address and, if applicable,
a rights request form URL. Conversion-engineer adds the confirmed route to the gate privacy
notice and the privacy policy. Lifecycle-architect references the same route in the
lifecycle-package. Both packages resubmit to this gate after the confirmed route is added.
The gate privacy notice update must also close out the open item under open item 5 above.
Owner: Ahmed, legal (route design), conversion-engineer and lifecycle-architect (package and
notice updates).

**8. CONSENT BASIS FOR THE EXISTING OWNED LIST (OPEN ITEM)**
The lifecycle-package targets approximately 18,000 contacts on the existing Maharat owned
email list. The lawful basis and consent status for these contacts, specifically whether they
consented to receiving marketing communications about new classes (as distinct from
transactional emails about their account), is not confirmed in any package.
What must happen: the data team confirms the consent basis for the owned list. If contacts
opted in to receive marketing communications, the basis is clear. If they opted in only to
transactional communications, a separate marketing consent capture may be required before
sending the lifecycle flow. This gate does not resolve the question; it surfaces it. If the
consent basis is confirmed as adequate for marketing, record it in the lifecycle-package
before resubmitting.
Owner: Ahmed, data team, legal.

**9. UTM TRACKING SCHEMA FOR ORGANIC POSTS (OPEN ITEM)**
The exact UTM parameter structure for organic post links is not confirmed. The organic-package
correctly holds all post URLs without UTM parameters pending schema confirmation. The schema
must be reviewed by this gate before URLs are built into posts.
What must happen: conversion-engineer and data-tracking-engineer confirm the UTM schema.
The confirmed schema is reviewed by this gate to verify no personal or sensitive data is
included in any UTM value. The organic-package is updated with confirmed UTM-appended URLs
and resubmits to this gate for the no-pii-in-urls check on the final links.
Owner: conversion-engineer, data-tracking-engineer, organic-social.

**10. WHATSAPP GATE PATH AND WABA COMPLIANCE (CONDITIONAL OPEN ITEM)**
The WhatsApp gate option (conversion-package gate option B) is blocked until both the
platform is confirmed and the WhatsApp Business Account (WABA) compliance is confirmed by
Ahmed. WhatsApp marketing messages require explicit opt-in consent separate from email
consent, and the BSP (business solution provider) choice has its own data-residency
implications. If the WhatsApp path is ever activated, it must return to this gate before
any WhatsApp send.
What must happen: if and when Ahmed activates the WhatsApp path, the BSP is confirmed,
the WABA compliance is confirmed, and the WhatsApp consent mechanism is reviewed by this
gate before any WhatsApp message is sent.
Owner: Ahmed, compliance-privacy-reviewer (when activated).

---

## Compliance QA block (for the package envelope)

```
qa:
  compliance_qa: pass (design-stage only)
  verdict_by: compliance-privacy-reviewer
  verdict_date: 2026-06-05
  re_verification_date: 2026-06-05
  scope: lifecycle-package, conversion-package, media-plan, organic-package
  hard_blockers: 10 open items (section 3); none are live-data defects today because
                 no asset currently collects data, sends, or publishes
  previously_failed_checks_now_resolved_at_design_stage:
    - retention-stance: stance stated in conversion-package section 2.5 and
      lifecycle-package section 4A; concrete durations PENDING legal/PDPL confirmation
    - data-subject-rights: DSR route stated and linked in both packages; live contact
      address and form URL PENDING legal/Ahmed confirmation
  pending_legal_items_joining_go_live_blockers:
    - confirmed retention durations and legal basis under Saudi PDPL (open item 6)
    - confirmed DSR contact address and rights request form URL (open item 7)
  design_stage_status: all ten checks now pass at design stage; the assets are correctly
                       designed as gated and not-yet-live; the compliance design is sound
                       at this stage with the noted pending-legal gaps
  go_live_gate: this verdict does not authorize go-live; the human gate is separate and
                decisive; Ahmed's explicit per-action approval is required
```

---

## Hard rules confirmation (verifier self-check)

- This gate did not edit any asset. Verified and routed only.
- The verdict is binary: pass (design-stage) with open items attached. All ten checks pass
  at design stage. No check remains at FAIL.
- No personal or sensitive data was found in any URL parameter or tracking call in the
  reviewed assets.
- The PDPL and data-residency open item is surfaced (open item 2). It is not invented or
  resolved.
- The platform open item is surfaced (open item 1). It is not resolved.
- The retention-stance and data-subject-rights checks pass at design stage. Concrete legal
  values (durations and DSR contact/URL) are surfaced as pending-legal open items (6 and 7).
  They are not invented or resolved.
- This pass does not authorize any send, data collection, or spend. The human gate is
  separate and decisive.
- No em dashes appear in this verdict.

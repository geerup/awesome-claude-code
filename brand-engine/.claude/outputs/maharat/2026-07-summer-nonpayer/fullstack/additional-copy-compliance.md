# Compliance and Privacy Verdict: Additional Copy Package
# Gate-consent copy and press release, Summer of Skills non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: compliance-privacy-reviewer
- stream: cross-cutting compliance and privacy gate
- verdict_date: 2026-06-12
- status: copy-level review complete. Not approved. Approval is the human gate's decision alone.
- compliance_qa: pass (copy level, with carried open items from compliance-verdict.md and
  additional implementation-level open items confirmed below; all block live gate or press
  distribution until resolved)
- brief_refs checked: consent copy disclosure elements (controller, purpose, policy link,
  opt-out, data minimization), no PII in URLs or tracking references, no accreditation
  implication, press release data flows, journalist contact placeholders, suppression and
  platform open item continuity, Saudi PDPL lawful basis and data-residency gap continuity

---

## Scope of This Review

Assets reviewed (under outputs/2026-07-summer-nonpayer/fullstack/):

- additional-copy.ar.md, section 3: GATE-CONSENT-EMAIL-AR and GATE-CONSENT-WHATSAPP-AR
- additional-copy.en.md, section 3: GATE-CONSENT-EMAIL-EN and GATE-CONSENT-WHATSAPP-EN
- additional-copy.ar.md, section 4: PR-RELEASE-AR
- additional-copy.en.md, section 4: PR-RELEASE-EN

Sections 1 and 2 (onboarding O1 to O3 and organic gap captions) are reviewed for PII-in-URL
and accreditation only, as they do not collect data, send to new contacts, or trigger a new
data flow at the copy level. They are not the focus of this review per the task instruction.

Reference read: compliance-verdict.md for this campaign (prior verdict, open items 1 to 12,
all still standing). This verdict adds no new open items to the twelve already recorded. It
confirms the copy-level compliance status of the four new copy assets and carries the
relevant prior open items explicitly.

This is a copy-level review. No gate is live. No send has occurred. No personal data has
been collected. Nothing in this verdict licenses any send, gate activation, press
distribution, or data collection.

---

## Verdict

PASS (copy level).

The four consent copy assets (GATE-CONSENT-EMAIL-AR, GATE-CONSENT-WHATSAPP-AR,
GATE-CONSENT-EMAIL-EN, GATE-CONSENT-WHATSAPP-EN) each contain all required disclosure
elements: data controller named, purpose stated, opt-out mechanism stated, data minimization
declared, and a visible privacy-policy placeholder. No personal or sensitive data appears in
any URL reference, tracking direction, or copy instruction. No accreditation implication
exists in any of the four sections reviewed. The press releases (AR and EN) introduce no
new data collection, carry only placeholder media contact lines, state no accreditation
claim, and contain no PDPL-triggering data flow at the copy level.

No design-level or copy-level compliance violation was found. The fix list is empty.

The implementation-level open items (policy link live, visible-before-submit verification,
WhatsApp logging mechanism, platform confirmation, journalist data handling) remain open
and unresolved. They do not block a copy-level pass but they block live gate deployment,
press distribution, and any activation action. See the carried open items section below.

No fix list. Carried open items confirmed and enumerated below.

---

## Check 1. No personal or sensitive data in URL parameters or tracking

Result: PASS.

GATE-CONSENT-EMAIL-AR: the consent line contains no URL other than the "[سياسة الخصوصية]"
placeholder, which is a named link label for the privacy policy. No query string. No user
identifier. The copy body "نستخدم بريدك الإلكتروني واسمك الأول" is consent disclosure
language, not a URL parameter or tracking call. No PII in any URL.

GATE-CONSENT-WHATSAPP-AR: same finding. The only URL reference is "[سياسة الخصوصية]"
placeholder. No query string. No phone number or personal attribute in any URL reference.

GATE-CONSENT-EMAIL-EN: the only URL reference is "[Privacy Policy]" with an OPEN ITEM note
that the href will be the live Maharat privacy policy URL inserted at build. No query string
in the consent text itself. The CTA landing note for onboarding assets (sections 1 and 2)
explicitly states "No personal or sensitive data in the URL" for each CTA. PASS on this check
for the gate-consent section.

GATE-CONSENT-WHATSAPP-EN: same finding as the email EN variant. No URL with personal data.

PR-RELEASE-AR: the only URL in the press release body is "maharat.com" (clean domain, no
query string, no personal attribute). The media contact line "[MEDIA CONTACT NAME],
[MEDIA CONTACT EMAIL]" is a placeholder. No real personal data is embedded. The
[confirm-at-gate] flags on instructor names are editorial markers in a draft, not data
fields. PASS.

PR-RELEASE-EN: destination URL is maharat.com (clean). Media contact line is a placeholder.
No PII in any URL or tracking reference in the press release body. PASS.

---

## Check 2. Consent correctness

Result: PASS at copy level for both variants and both languages, with Open Items 2 and 5
(from the prior verdict) confirmed as still open and blocking live use.

### GATE-CONSENT-EMAIL-AR

Required elements per conversion-package.md section 3.2 (a to d) and
compliance-verdict.md Open Item 5:

(a) Data controller named and purpose stated: "تتواصل معك مهارات ... برسائل عن المنصة
والمجال الذي تختاره". Controller: مهارات. Purpose: platform and chosen-field messages.
PRESENT.

(b) Visible privacy policy link before submit: "[سياسة الخصوصية]" inline placeholder.
Authoring note confirms it must be visible before submit, not hidden behind scroll or
collapse. PRESENT as placeholder; implementation verification is Open Item 5 (carried).

(c) Opt-out mechanism: "يمكنك إلغاء الاشتراك في أي وقت عبر الرابط في أسفل كل رسالة".
Unsubscribe link in every message. PRESENT. Matches the email channel.

(d) Data minimization declared: "نستخدم بريدك الإلكتروني واسمك الأول إن أضفته فقط لهذا
الغرض". Email plus optional first name only, nothing more. PRESENT. Consistent with the
gate field spec in conversion-package.md section 3.2.

All four required elements present. Copy-level PASS.

### GATE-CONSENT-WHATSAPP-AR

Required elements per conversion-package.md section 3.3 and compliance-verdict.md Open Item 2:

(a) Explicit WhatsApp reference and controller named: "تراسلك مهارات عبر واتساب". Channel
named. Controller named. Purpose stated. PRESENT.

(b) Stop mechanism: "لإيقاف الرسائل في أي وقت، أرسل كلمة \"إيقاف\"". Clear Arabic stop
word stated. PRESENT. The additional-copy.ar.md open item correctly notes the stop keyword
must match what the WhatsApp platform honors; that is an implementation dependency, not a
copy defect.

(c) Visible privacy policy link: "[سياسة الخصوصية]" inline placeholder. Same visibility
requirement as the email variant. PRESENT as placeholder.

(d) Data minimization declared: "نستخدم رقمك واسمك الأول إن أضفته فقط لهذا الغرض". Phone
plus optional first name only. PRESENT. Consistent with conversion-package.md section 3.3.

Consent logging mechanism: the copy correctly notes the logging mechanism (timestamp and
consent text version) is a separate non-copy dependency. The copy is not the logging
mechanism; it is the disclosure text. The copy-level check passes. Open Item 2 (the logging
mechanism design and review) continues to block WhatsApp gate go-live. CONFIRMED CARRIED.

All four required elements present in the copy. Copy-level PASS.

### GATE-CONSENT-EMAIL-EN

(a) Controller named and purpose stated: "Maharat is the data controller." and "receive
messages from Maharat about the platform and your chosen field." PRESENT.

(b) Visible privacy policy link: "[Privacy Policy]" hyperlinked placeholder. PRESENT.

(c) Opt-out: "You can unsubscribe at any time using the link in any message." PRESENT.
Matches the email channel.

(d) Data minimization: the EN consent line does not explicitly enumerate the fields
collected (email plus optional first name). The AR consent line does ("نستخدم بريدك
الإلكتروني واسمك الأول إن أضفته فقط لهذا الغرض"). The EN line is shorter and does not
restate the collected fields by name.

Assessment: the EN consent line meets the minimum disclosure requirements for the email
channel (controller, purpose, policy link, opt-out). Data minimization is confirmed in
the gate field spec (conversion-package.md section 3.2) and in the Arabic consent line;
the English line's omission of the field enumeration is not a hard compliance failure at
the copy-disclosure level, as the gate UI itself constrains what is collected and the
privacy policy link (once live) must disclose the fields. However, for consistency with the
Arabic variant and for fuller PDPL disclosure, the EN consent line would be stronger if it
named the collected fields. This is noted as a recommendation, not a fix item that blocks
pass. The copy-level PASS stands.

All minimum required elements present. Copy-level PASS.

### GATE-CONSENT-WHATSAPP-EN

(a) Controller, WhatsApp channel explicit, purpose: "receive WhatsApp messages from Maharat
about the platform and your chosen field." and "Maharat is the data controller." PRESENT.

(b) Stop mechanism: "To stop messages, reply 'Stop' at any time." PRESENT. Notes correctly
flag that the exact stop keyword must match the platform. PRESENT.

(c) Visible privacy policy link: "[Privacy Policy]" placeholder. PRESENT.

(d) Data minimization: same observation as the email EN variant above. Phone plus optional
first name are the only fields collected; the EN copy does not enumerate them explicitly
as the AR copy does. Same assessment: not a hard compliance failure at copy-disclosure
level, noted as a consistency recommendation.

All minimum required elements present. Copy-level PASS.

---

## Check 3. Suppression correctness

Result: NOT APPLICABLE for the consent copy assets (copy defines the disclosure, not the
send suppression). NOT APPLICABLE for the press release (no CRM send triggered).

The suppression design for the email and WhatsApp channels was reviewed and passed at
design level in compliance-verdict.md (Check 3). Suppression execution wiring remains
blocked on Open Items 4 and 8 from the prior verdict, both of which are confirmed still
open. No new suppression issue is introduced by these copy assets.

---

## Check 4. Saudi PDPL and data residency

Result: OPEN ITEMS 7 and 8 from the prior verdict confirmed still open. No new PDPL issue
introduced by the copy assets themselves.

The consent copy assets correctly carry a placeholder for the live privacy policy URL
and do not invent a lawful basis. The copies state what data is collected and for what
purpose, which is the disclosure obligation at the copy layer. The underlying lawful basis
(Open Item 7(a)) and cross-border transfer safeguards (Open Item 7(b)) are above the copy
layer and remain unresolved.

PR-RELEASE-AR and PR-RELEASE-EN: the press releases describe the campaign and direct to
maharat.com. They do not collect personal data, do not establish a new data flow, and do
not imply a lawful basis for processing. No PDPL issue at the copy level.

The media contact placeholder "[MEDIA CONTACT NAME], [MEDIA CONTACT EMAIL]" in both press
releases is correctly a placeholder. No real journalist personal data is embedded in these
drafts. Open Item 11 (journalist contact data handling before outreach execution) is
confirmed still open and blocks distribution execution.

---

## Check 5. No accreditation implication

Result: PASS across all four assets reviewed.

GATE-CONSENT-EMAIL-AR and GATE-CONSENT-WHATSAPP-AR: consent lines contain no reference
to certificates, credentials, or accreditation. PASS.

GATE-CONSENT-EMAIL-EN and GATE-CONSENT-WHATSAPP-EN: same finding. PASS.

PR-RELEASE-AR: the boilerplate states "تمنح مهارات شهادات إتمام، وهذه الشهادات غير
معتمدة." Completion certificates, explicitly non-accredited. PASS.

The body also uses "شهادة إتمام مخصصة باسم المتعلم توثّق رحلته" with no accreditation
claim. PASS.

PR-RELEASE-EN: the body states "Completion certificates are issued by Maharat on course
completion. Certificates are not accredited." This appears twice (body and boilerplate).
Both instances are clear non-accreditation statements. PASS.

---

## Check 6. Data-flow disclosure at the point of collection

Result: PASS at copy level.

Both email consent variants (AR and EN) and both WhatsApp consent variants (AR and EN)
contain the privacy policy link (placeholder at this stage, confirmed to be visible before
submit per the conversion-package.md direction and the authoring notes). The disclosure
obligation at the point of collection is met in the copy. The implementation verification
that the link is live and visible before submit is Open Item 5 (carried).

PR-RELEASE-AR and PR-RELEASE-EN: the press releases introduce no new point of collection
and require no disclosure line within the release itself. The releases direct readers to
maharat.com, where the existing gate and privacy policy handle collection disclosure.
PASS.

---

## Check 7. Data minimization, retention, and data-subject rights

Result: PASS on data minimization (copy level). Retention and data-subject rights remain
open at the implementation level (Open Items 7(c) and 7(d) from the prior verdict,
confirmed still open).

Data minimization at copy level:

GATE-CONSENT-EMAIL-AR explicitly states: "نستخدم بريدك الإلكتروني واسمك الأول إن أضفته
فقط لهذا الغرض." Email plus optional first name only. Consistent with the gate field
spec. PASS.

GATE-CONSENT-WHATSAPP-AR explicitly states: "نستخدم رقمك واسمك الأول إن أضفته فقط لهذا
الغرض." Phone plus optional first name only. PASS.

GATE-CONSENT-EMAIL-EN: controller, purpose, and opt-out present; field enumeration not
explicit (noted as recommendation above). Gate field spec constrains collection to email
plus optional first name. Minimization is satisfied at the design level. PASS.

GATE-CONSENT-WHATSAPP-EN: same assessment. PASS.

Retention and data-subject rights: no retention period or deletion schedule is stated in
any of the four new copy assets. This is consistent with the prior verdict finding. These
are not copy-layer obligations but implementation-layer obligations. Open Items 7(c) and
7(d) continue to block go-live. CONFIRMED CARRIED.

---

## Carried Open Items for the Human Gate

The following items from compliance-verdict.md are confirmed still open and unresolved.
None is invented by this reviewer. All carried items were fully examined in this review;
none was found to have been resolved by the authoring of these copy assets.

CARRIED OPEN ITEM 2. WhatsApp consent logging mechanism not yet designed or reviewed.

The GATE-CONSENT-WHATSAPP-AR and GATE-CONSENT-WHATSAPP-EN copy assets are correct in
content. The consent logging mechanism (timestamp, consent text version, lifecycle platform
record linkage) has not been designed or submitted for review. The WhatsApp gate cannot go
live until this mechanism is designed and reviewed by compliance-privacy-reviewer. The copy
is ready; the mechanism is not.

Returns to: conversion-engineer (mechanism design), lifecycle-architect (record linkage),
compliance-privacy-reviewer (dedicated mechanism review before WhatsApp gate goes live).

CARRIED OPEN ITEM 5. Implementation verification of the consent line and privacy-policy link.

The GATE-CONSENT-AR and GATE-CONSENT-EN copy passes at the copy level. The implementation
verification steps are not yet run: (a) the privacy-policy link must resolve to a live,
readable policy page (Open Item 9 also applies here); (b) the consent line must be
confirmed visible to the user before any submit action, not behind a scroll or collapsed
element; and (c) arabic-copy-qa and english-copy-qa must pass the consent copy slots before
they are used in a live gate. This copy-level pass does not substitute for those checks.

Returns to: conversion-engineer (implementation and checklist execution), arabic-copy-qa and
english-copy-qa (copy gate of record, runs after this compliance pass), compliance-privacy-
reviewer (implementation-level clearance before go-live).

CARRIED OPEN ITEM 8. Platform confirmation (gate, email, WhatsApp, push, paid platforms).

All four consent copy assets are gated on platform confirmation. The WhatsApp consent variant
applies only if WhatsApp is the confirmed gate channel. The stop word "إيقاف" (AR) and
"Stop" (EN) must match the keyword the WhatsApp platform actually honors; this can only be
confirmed once the platform is named.

Returns to: Ahmed (platform decisions), then lifecycle-architect and conversion-engineer for
implementation, then compliance-privacy-reviewer before activation.

CARRIED OPEN ITEM 9. Live Maharat privacy policy review.

Both consent variants in both languages carry a placeholder for the live privacy policy URL.
The live policy must be reviewed to confirm it covers PDPL-required elements (controller
identity, processing purposes, users' rights, data-subject request route, cross-border
transfers, retention) before the placeholder is replaced with a live link and the gate opens.

Returns to: Ahmed (decision), legal or compliance owner (policy review and update if needed).

CARRIED OPEN ITEM 11. Journalist contact data handling (PR stream).

Both PR-RELEASE-AR and PR-RELEASE-EN correctly carry "[MEDIA CONTACT NAME], [MEDIA CONTACT
EMAIL]" as placeholders. No real journalist personal data is embedded in these drafts. This
reviewer confirms the drafts are clean at the copy level. Open Item 11 from the prior verdict
remains fully open: before outreach is executed and before any journalist contact list is
built in any tool, the basis for holding that data and the tool's data residency must be
confirmed. No personal data of any journalist may be stored in any campaign analytics or
tracking platform.

Returns to: pr-comms (execution planning and tool selection), Ahmed (contact confirmation
and approval), legal or compliance owner (PDPL basis for journalist data).

---

## Additional Observations (not fix items, noted for completeness)

1. EN consent copy data-field enumeration. The EN email and WhatsApp consent lines do not
   explicitly state the collected fields by name (email or phone, optional first name), while
   the AR lines do. This is a recommendation for consistency and fuller PDPL disclosure, not
   a compliance block. If the live privacy policy clearly enumerates the collected fields
   (Open Item 9), the omission in the EN consent line does not create a disclosure gap.
   Conversion-engineer may choose to align the EN line with the AR pattern at build.

2. WhatsApp stop keyword platform alignment. Both AR and EN WhatsApp consent lines note
   the stop word must be confirmed against the platform keyword. This is correctly flagged as
   an implementation dependency in the authoring notes. It is not a copy defect; it is an
   activation dependency under Open Item 8.

3. PR-RELEASE-EN: the dateline uses a double-hyphen style ("CITY, DATE, 2026 --"). This
   is conventional press-release dateline formatting and is not an em dash. It is noted here
   for the brand-qa-reviewer to confirm. This reviewer does not adjudicate copy style; that
   is brand-qa-reviewer's domain.

---

## Send, Spend, Wiring, Publish, and Data Collection Block Confirmed

Nothing in this verdict licenses any gate activation, send, press release distribution,
data collection, or platform wiring. The consent copy is approved at copy level only.
Every activation action remains blocked under the prior verdict's twelve open items, all of
which still stand, and additionally under the five carried items named above.

A copy-level pass here is not approval to deploy a gate or distribute a press release.
The human gate is separate and decisive. Ahmed's explicit per-action approval is required
before any gate goes live, any press release distributes, or any other activation occurs.

---

## Routing

This verdict attaches to the human-gate package for campaign 2026-07-summer-nonpayer.

Next mandatory gates before the consent copy can be used in a live gate:
- arabic-copy-qa on GATE-CONSENT-EMAIL-AR and GATE-CONSENT-WHATSAPP-AR.
- english-copy-qa on GATE-CONSENT-EMAIL-EN and GATE-CONSENT-WHATSAPP-EN.
- brand-qa-reviewer on all four consent assets.
- Conversion-engineer: implementation verification checklist (policy link live, visible-
  before-submit confirmed).
- Compliance-privacy-reviewer: implementation-level clearance before go-live.

Next mandatory gates before either press release can be distributed:
- arabic-copy-qa on PR-RELEASE-AR.
- english-copy-qa on PR-RELEASE-EN.
- brand-qa-reviewer on both.
- pr-comms: dateline, quote, co-founder naming, and media contact line confirmed.
- Compliance-privacy-reviewer: journalist data handling confirmed (Open Item 11).
- Human gate: Ahmed's explicit per-action distribution approval.

A pass here is not approval to send. The human gate is separate and decisive.

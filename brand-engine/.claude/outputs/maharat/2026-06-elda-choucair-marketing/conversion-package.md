# conversion-package: 2026-06-elda-choucair-marketing

Stream 6, conversion path. Owns the landing page spec and the signup gate design. The
event_plan section is carried from data-tracking-engineer and is NOT authored here. The
plumbing (Pixel, CAPI, GA4, BigQuery) belongs to data-tracking-engineer. The boundary is firm.

No em dashes, no tatweel, Western numerals only. RTL-correct Arabic primary throughout the
page spec. No accreditation claims. No price, plan, or promotion on the page (all ASSUMPTION,
unconfirmed). No personal or sensitive data in any URL parameter or tracking value.

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: conversion-engineer (page and gate); data-tracking-engineer co-owns event_plan
  (plumbing, Pixel/CAPI/GA4/BigQuery mapping, warehouse queries)
- stream: 6 conversion path
- status: gated-pending
- qa:
  - skill_eval: self-checked against skills/06-conversion-path (hub, landing-page, event-tracking
    evals)
  - arabic_qa: pending (required on all Arabic page copy before go-live)
  - brand_qa: pending (runs after arabic_qa)
  - compliance_privacy: pending (required before any data-collection gate goes live; Saudi PDPL
    and data-residency are open items surfaced below)
- open_items:
  - HARD BLOCKER: gate platform not confirmed (Ortto vs HubSpot, Arabic RTL concern). Page and
    gate are fully designed. Live wiring of any send or CRM capture is blocked until the platform
    is named and approved by Ahmed.
  - COMPLIANCE BLOCKER: Saudi PDPL compliance review and data-residency confirmation required
    before any gate collects personal data. Privacy notice draft required before go-live.
  - retention-stance: SPECIFIED at design level in Section 2.5. Concrete retention durations
    and legal basis PENDING legal/PDPL confirmation. Must be confirmed and stated in the live
    privacy policy before go-live. Was a compliance FAIL; now resolved at design stage.
  - data-subject-rights: SPECIFIED at design level in Section 2.6. Live privacy contact address
    or form URL PENDING legal/Ahmed confirmation. Gate privacy notice must be updated to
    reference the rights route before go-live. Was a compliance FAIL; now resolved at design stage.
  - mobile-mapping-to-confirm: Apple IAP and Google Play event mapping is not guessed and is
    carried forward as an open item for data-tracking-engineer.
  - Meta Pixel and CAPI mapping details: owned by data-tracking-engineer, marked to-confirm in
    the event_plan section.
  - LinkedIn Insight Tag mapping: owned by data-tracking-engineer, to-confirm.
  - Google Tag (gtag.js) configuration: owned by data-tracking-engineer, to-confirm.
  - price, plan, promotion: ASSUMPTION. No number on the page. Subscribe CTA copy and the
    post-gate subscription-start URL remain open until Ahmed confirms.
  - start_date and end_date: ASSUMPTION (proposed 2026-06-08 to 2026-06-21). UTM dates and
    campaign parameter values depend on this.
  - PDF cheatsheet download URL: not confirmed. Gate and post-submit paths reference it by
    placeholder until the URL is confirmed.
  - success_metric target number and date: ASSUMPTION. Not a page variable but affects what the
    event_plan measures against.
  - formal catalog status confirmation for Elda: pending. Naming is supported by the public class
    page; surface at the human gate.
- brief_refs:
  - offer: Masterclass "Elda Choucair, Teaches Marketing" / "إلدا شقير، تعلّم التسويق"
  - gate_type: email (primary for owned contacts); WhatsApp noted as an option for new traffic
    if the platform supports it, blocked on the platform open item
  - lead_magnets: Chapter 1 free (confirmed), marketing-campaign PDF cheatsheet (confirmed)
  - price_shown: no (ASSUMPTION, unconfirmed)
  - promotion_shown: none (Chapter 1 free is a product element, not a promotion)
  - conversion_the_page_optimizes_toward: gate completion (email or WhatsApp opt-in), with
    the eventual conversion being a paid subscription start (post-gate, off-page)

---

## 1. Landing Page Spec (page field)

The single destination page for paid (entry A), organic social (entry C), and email links (entry
B) where they point outward. The primary conversion is gate completion: the visitor submits
their email or WhatsApp and enters lifecycle. A secondary low-friction path (the free chapter
link) is available for visitors who are not ready to gate.

No price, no plan name, no promotion, no lesson list, no lesson count, no accreditation
language on this page.

---

### 1.1 URL and Language Variants

- Canonical AR path: /ar/landing/elda-choucair-marketing (exact path confirmed at build;
  placeholder used here)
- Canonical EN path: /en/landing/elda-choucair-marketing (exact path confirmed at build;
  placeholder used here)
- Language direction: page root direction rtl for AR variant, ltr for EN variant
- Default served: AR variant (Arabic-first principle)
- Language switch: a low-key language toggle in the page header (text link, not a dropdown)
  allows the visitor to switch between AR and EN without losing page context

UTM parameters applied to inbound links (set by paid-build-engineer and organic-social at
distribution, not hardcoded on the page):
- utm_source: meta / instagram / linkedin / google / youtube / organic / email
- utm_medium: paid_social / paid_search / organic_social / email
- utm_campaign: 2026-06-elda-choucair-marketing
- utm_content: (ad or post id, assigned by paid-build-engineer)
- utm_term: (keyword, for search only)
- No personal or sensitive data in any UTM or URL parameter. This is a hard rule.

---

### 1.2 Page Structure and Section-by-Section Wireframe

Page is single-column, uncluttered, fast. Mobile-first layout. Desktop max-width 1440 px.
Font: system Arabic stack (IBM Plex Arabic or Noto Naskh Arabic as primary; fallback to
system-ui). All RTL text right-aligned in the AR variant. Western numerals throughout.

---

#### Section 1: Hero (above the fold, full viewport)

Creative reference: AB8 (creative-briefs.md, Prompt P5, landing page hero composition).
- Layer 1: rights-cleared Maharat cover image. AR variant uses
  https://dt92b02v6m7lx.cloudfront.net/EC_CLASSCOVER_DESKTOP_01_AR-PAGE.webp
  EN variant uses
  https://dt92b02v6m7lx.cloudfront.net/EC_CLASSCOVER_DESKTOP_01_EN-PAGE.webp
  Portrait positioned right-of-center on desktop, centered on mobile.
- Layer 2: #141414 gradient field, left 55% on desktop, fades to transparent at midpoint.
  On mobile: top-to-bottom gradient over the portrait.
- Layer 3: subtle architectural grid at 6% opacity on the copy zone, left side.
- Layer 4: single emerald (#009975) horizontal rule, 2 px, at ~45% height in the left copy zone.
  Desktop: spans from the left margin to ~40% canvas width.

Copy overlay slots (all bound to QA-passed copy-package IDs; no free text):

AR variant (direction: rtl, text right-aligned within the left copy zone on desktop;
full-width centered on mobile):
- [AR hero headline]: copy-package.ar.md > D.LP > LP-hero
  Arabic text: "التسويق هندسة قرار"
  Display weight, large. Desktop: upper-left copy zone, below safe area top. Mobile: centered,
  below the portrait crop.
- [AR hero subhead]: copy-package.ar.md > D.LP > LP-subhead
  Arabic text: "تعلّم كيف يختار الناس، وكيف تبني كل شيء حول تلك اللحظة. أكثر من 20 سنة من خبرة إلدا شقير في صف واحد. الفصل الأول مجاني."
  Medium weight, 2 lines max on desktop.
- [AR primary CTA button]: copy-package.ar.md > D.LP > LP-primary-CTA
  Arabic text: "شاهد الفصل الأول مجانا"
  Emerald (#009975) filled button, right-aligned in AR. Links to:
  https://member.maharat.com/ar/class/elda-choucair-teaches-marketing
  CTA is visible without a scroll on mobile (sticky if needed for very short viewports).
- [AR gate-entry CTA]: text link below the primary button
  Arabic text: "أو اشترك للوصول إلى الصف كاملا" (copy unit: gate-entry-link-ar)
  This is the soft secondary action that scrolls the page down to Section 3 (the signup gate).
  It is a text link, NOT a competing primary button. On mobile it sits directly below the
  primary CTA button.

EN variant (direction: ltr, text left-aligned within the left copy zone on desktop):
- [EN hero headline]: copy-package.en.md > D.LP > LP-hero (headline)
  English text: "Marketing is decision architecture."
- [EN hero subhead]: copy-package.en.md > D.LP > LP-hero (subhead)
  English text: "Elda Choucair, CEO of Omnicom Media Group MENA, has spent more than 20 years
  working at the layer above tactics. This masterclass puts that thinking in your hands."
- [EN primary CTA button]: copy-package.en.md > D.LP > LP-hero (Primary CTA)
  English text: "Watch Chapter 1 Free"
  Emerald button, left-aligned in EN. Links to:
  https://member.maharat.com/en/class/elda-choucair-teaches-marketing
- [EN gate-entry CTA]: text link below the primary button
  English text: "Or subscribe to access the full class" (copy unit: gate-entry-link-en)
  Same soft scroll-down behavior as the AR variant.

Visual and RTL verification notes:
- The portrait (Elda) is on the RIGHT side in the desktop AR layout (natural for RTL reading
  flow: the eye enters from the right, where Elda is, and reads left into the copy zone).
- On the EN desktop layout, the portrait sits right-of-center and the copy zone is on the left
  (standard LTR editorial layout). This is the same physical composition; only the text
  alignment and directionality changes.
- The emerald rule (#009975) is a single horizontal accent below the subhead. It is not a flood.
- No text is baked into any image layer. All copy is overlaid at build time as HTML/CSS so
  Arabic renders correctly.
- Mobile: portrait is full-width at top of viewport, gradient overlay, then copy below. CTA
  button is below the copy, still above the fold (560 px viewport height per Prompt P5 spec).

---

#### Section 2: Value Blocks (3 cards, below the fold)

Three cards on #1A1A1A surfaces, arranged as a column on mobile and a 3-column row on desktop.
Card padding: 32 px all sides. Emerald micro-accent (a 2 px top border on each card).

Card 1 (bound to LP-value-1):

AR:
- Card headline: copy-package.ar.md > D.LP > LP-value-1 headline
  Arabic text: "صوت من أعلى مستوى"
- Card body: copy-package.ar.md > D.LP > LP-value-1 body
  Arabic text: "خبرة إلدا شقير، الرئيسة التنفيذية لمجموعة أومنيكوم ميديا في الشرق الأوسط وشمال إفريقيا، أكثر من 20 سنة من أعقد العمل التسويقي في المنطقة، ملخصة بوضوح."

EN:
- Card headline: copy-package.en.md > D.LP > LP-value-1 (headline)
  English text: "The framework, not the tips list."
- Card body: copy-package.en.md > D.LP > LP-value-1 (body)

Card 2 (bound to LP-value-2):

AR:
- Card headline: copy-package.ar.md > D.LP > LP-value-2 headline
  Arabic text: "طريقة تفكير، لا قائمة تكتيكات"
- Card body: copy-package.ar.md > D.LP > LP-value-2 body
  Arabic text: "تتعلم إطارا يبقى معك: كيف يقرر الناس، ولماذا تكسب أفضل القصص لا أفضل الأفكار. وضوح في الحكم، لا نصائح متفرقة."

EN:
- Card headline: copy-package.en.md > D.LP > LP-value-2 (headline)
  English text: "20 years of senior regional work, structured."
- Card body: copy-package.en.md > D.LP > LP-value-2 (body)

Card 3 (bound to LP-value-3):

AR:
- Card headline: copy-package.ar.md > D.LP > LP-value-3 headline
  Arabic text: "ابدأ بلا التزام"
- Card body: copy-package.ar.md > D.LP > LP-value-3 body
  Arabic text: "الفصل الأول مجاني، وملخص الحملة التسويقية بانتظارك. اختبر الفرق بنفسك قبل أي خطوة."

EN:
- Card headline: copy-package.en.md > D.LP > LP-value-3 (headline)
  English text: "Start with Chapter 1, free."
- Card body: copy-package.en.md > D.LP > LP-value-3 (body)

RTL note: in the AR variant, all card text is right-aligned. The 3-column row on desktop reads
right-to-left (Card 1 is the rightmost card). On mobile, cards stack top-to-bottom in the same
order (1, 2, 3 from top).

---

#### Section 3: Signup Gate (primary conversion surface)

Background: #141414. A centered card on #1A1A1A, max-width 480 px, 40 px padding all sides.
This section is the destination of the scroll-down anchor from the hero text link (Section 1).

Gate headline (AR): "احصل على الفصل الأول مجانا وملخص الحملة التسويقية"
Gate headline (EN): "Get Chapter 1 Free and the Marketing-Campaign Cheatsheet"
These lines are written here for specification purposes only as slot labels. The exact copy
unit IDs for the gate headline will be confirmed with copywriter-ar and copywriter-en at build
(the copy-package landing-page copy covers the hero; the gate micro-copy is an additional
slot that streams 4 and 6 confirm together before launch).

Gate subhead (AR): "أدخل بريدك الإلكتروني وسيصلك الوصول فورا."
Gate subhead (EN): "Enter your email and we will send you access."
Same note as above: these are slot placeholders, confirmed with stream 4 at build.

Fields: one field only.
- Email address field (AR label: "البريد الإلكتروني"; EN label: "Email address")
- Field is the minimum required for email capture. No name field, no phone field unless
  WhatsApp is activated (see gate option B below).
- Placeholder text (AR): "أدخل بريدك" / (EN): "Your email"
- Required field. HTML5 email validation before submit.

Privacy and consent notice (REQUIRED before go-live, COMPLIANCE BLOCKER):
- A one-line consent statement appears below the email field, above the submit button, in
  both AR and EN.
- AR placeholder: "بالاشتراك، أوافق على سياسة الخصوصية وتلقي التحديثات من ماهرات."
- EN placeholder: "By submitting, you agree to Maharat's privacy policy and to receive
  updates from us."
- The phrase "سياسة الخصوصية" / "privacy policy" links to the Maharat privacy policy page
  (URL to confirm at build). This link is required before any data is collected.
- The compliance-privacy-reviewer must approve the exact wording and confirm Saudi PDPL
  compliance before go-live. The wording above is a placeholder, not an approved legal text.

Submit CTA button (AR): "احصل على الوصول المجاني"
Submit CTA button (EN): "Get Free Access"
Emerald (#009975) filled button, full width of the card on mobile, centered on desktop.

Gate option B (WhatsApp, conditional):
- If the confirmed platform supports WhatsApp capture, a secondary option appears below the
  email field as a toggle or tab (not a separate competing CTA button).
- AR label: "أو تواصل عبر واتساب"
- EN label: "Or connect via WhatsApp"
- This path is fully blocked until: (a) the gate platform is confirmed and (b) the WhatsApp
  Business account and WABA compliance are confirmed by Ahmed.
- Do not wire or display the WhatsApp option until both conditions are met.

Post-submit path:
1. Visitor submits their email.
2. Page displays an inline confirmation message (same card, no redirect):
   AR: "شكرا. سيصلك الوصول على بريدك الإلكتروني خلال لحظات."
   EN: "Done. Check your email, access is on its way."
3. The platform (OPEN ITEM, Ortto or HubSpot) adds the contact to the campaign list and
   triggers the first lifecycle email (E1 hook) after a short delay (proposed: within 5 minutes,
   per the E1 send_trigger in the copy-package). This trigger is blocked until the platform is
   confirmed.
4. The PDF cheatsheet download link is delivered in the first lifecycle email (E1 or a
   dedicated welcome), NOT on the page itself. This prevents the cheatsheet from being accessed
   without entering the lifecycle. The cheatsheet URL is an open item (not confirmed).
5. The confirm event fires on the client side when the inline confirmation renders (see
   Section 3, event tracking plan).

Suppression: existing paying subscribers who land on the page see the same gate (the page
does not require authentication to view). The platform-side suppression logic (exclude paying
subscribers, hard-bounced, unsubscribed) is applied at send time by lifecycle-architect (stream 7),
not by the page. The gate always accepts the email submission; deduplication and suppression
happen in the CRM.

---

#### Section 4: Free Chapter Direct Path (secondary, for visitors not ready to gate)

A low-key secondary section below the gate. Background #141414. No card surface.
Max-width 600 px, centered.

AR copy: "إذا أردت أن تبدأ فورا، الفصل الأول متاح مجانا بدون تسجيل."
EN copy: "If you prefer to start right away, Chapter 1 is available free, no signup needed."

Direct link button (ghost/outline style, not filled emerald, to maintain visual hierarchy):
AR: "شاهد الفصل الأول الآن" linking to
https://member.maharat.com/ar/class/elda-choucair-teaches-marketing

EN: "Watch Chapter 1 Now" linking to
https://member.maharat.com/en/class/elda-choucair-teaches-marketing

This section is intentionally lower-hierarchy than the gate. Visitors who watch Chapter 1
without gating are not lost; the lifecycle email flow (stream 7) can later surface a
gate-download prompt to any contact who was acquired via paid or organic but did not opt in.
This path tracks a separate page_view event on the Chapter 1 start URL (see event_plan).

Note on the copy above: these are slot specifications. The exact final copy for Sections 3
and 4 micro-copy will be coordinated between conversion-engineer and copywriter-ar (stream 4)
before the arabic-copy-qa gate.

---

#### Section 5: Page Footer (minimal)

Background #141414.
- Maharat logo (left in EN, right in AR).
- Language toggle text link.
- Privacy policy link (required; URL to confirm). Arabic: "سياسة الخصوصية"
- No navigation menu, no social links, no footer that dilutes the conversion focus.

---

### 1.3 Visual Constants Summary

| Element | Value |
|---|---|
| Page background | #141414 |
| Card surfaces (value blocks, gate card) | #1A1A1A |
| Primary accent (CTA button, emerald rule, card top border) | #009975 |
| Accent usage | Precision highlight only, never a flood |
| Spacing | Generous. Desktop: 80 px section padding. Mobile: 40 px. |
| Typography direction (AR) | rtl, right-aligned, Arabic primary |
| Typography direction (EN) | ltr, left-aligned |
| Numerals | Western only (0 to 9). No Eastern Arabic numerals. |
| Em dashes | None. |
| Tatweel | None. |

---

### 1.4 Performance Notes

- Hero image is preloaded (rel="preload"). The cover image is served from the existing
  Cloudfront CDN (dt92b02v6m7lx.cloudfront.net), so it is already edge-distributed.
- No blocking third-party scripts in the critical path above the fold. All tracking scripts
  (Pixel, GA4, LinkedIn, gtag) are loaded async or deferred.
- Primary CTA button is rendered as an HTML element (not an image) so it renders instantly and
  is accessible.
- The signup gate form is rendered server-side or as a minimal client-side form, not an embedded
  third-party iframe, to avoid CLS and loading delays.
- On mobile (390 px viewport), the CTA button is visible at the bottom of the hero section
  without any scroll.

---

### 1.5 RTL Rendering Verification (pre-go-live check)

The following must be verified in a rendered test environment before the package advances to
the human gate:

1. The page root dir attribute is "rtl" on the AR variant and "ltr" on the EN variant.
2. All Arabic copy is right-aligned. No Arabic text appears left-aligned or centered unless the
   design spec explicitly places it centered (the gate card headline is centered by design;
   all other AR body text is right-aligned).
3. Western numerals render correctly in mixed AR/EN strings (e.g., "20 سنة" must not reorder
   the numeral).
4. The emerald CTA button aligns to the right in the AR variant and to the left in the EN
   variant within the hero copy zone.
5. The value cards in the AR variant desktop 3-column layout are ordered right-to-left (Card 1
   on the right).
6. The footer logo is right-aligned in the AR variant.
7. No tatweel or kashida characters appear anywhere in any rendered Arabic text.
8. The privacy consent line in the gate is right-aligned in the AR variant, with the link
   underlined and tappable at mobile touch targets (44 px minimum).

Status: pending (requires a rendered test build; cannot be verified from the spec alone).

---

## 2. Signup Gate Spec (gate field)

### 2.1 Gate Type

Primary: email opt-in.
Conditional secondary: WhatsApp (blocked until platform confirmed and WABA compliance confirmed).

### 2.2 Fields (minimum viable capture)

| Field | Required | Notes |
|---|---|---|
| Email address | Yes | HTML5 email validation, no other fields on the baseline gate |
| WhatsApp number | Conditional | Only if the WhatsApp path is activated (blocked) |

No name field, no phone field beyond WhatsApp if activated, no company field, no date of
birth, no any field that is not required for the lead magnet delivery and lifecycle entry.
Minimum viable data collection is both a user experience and a PDPL compliance principle.

### 2.3 Platform Wiring (HARD BLOCKER)

The email capture platform is NOT confirmed. The tension on record is Ortto (incumbent) vs
a HubSpot migration, with an Arabic RTL concern on both. No contact is added to any CRM,
no send is triggered, and no data is written anywhere until Ahmed names and approves the
platform.

Design assumptions (the spec is written against these; all are blocked on platform confirmation):
- When a visitor submits the gate, the platform API receives: email address, source UTM values
  (utm_source, utm_medium, utm_campaign, utm_content), and a campaign tag
  "2026-06-elda-choucair-marketing".
- The platform creates or updates a contact record. No personal data is passed in URL
  parameters; the email is submitted as a form POST body field only.
- The platform immediately adds the contact to the campaign list and triggers E1 (the hook
  email, copy-package.ar.md id: email-e1-hook) within approximately 5 minutes of submission.
- Suppression logic (exclude paying subscribers, hard-bounced, unsubscribed) is applied by
  the platform at the point of send, not at the point of capture.
- Double opt-in: recommended for Saudi PDPL compliance (confirm with compliance-privacy-reviewer
  whether Saudi PDPL requires explicit double opt-in or whether implied consent with a clear
  privacy notice is sufficient). If double opt-in is required, the confirm event fires on the
  second confirmation action, not on the initial submit.

### 2.4 Data Handling and Privacy Notice (COMPLIANCE BLOCKER)

The following is required before any gate goes live and collects personal data:

1. A privacy notice approved by the compliance-privacy-reviewer appears at the gate before
   submit (placement: below the email field, above the submit button). See Section 1.2,
   Section 3 for the placeholder text.
2. The privacy policy URL is live and accessible. The notice links to it.
3. Saudi PDPL compliance confirmation: the compliance-privacy-reviewer must confirm that the
   data collection, storage, and processing of Saudi residents' email addresses complies with
   the Personal Data Protection Law (PDPL) of Saudi Arabia.
4. Data-residency confirmation: if the platform (Ortto or HubSpot) stores contact data outside
   Saudi Arabia, the compliance-privacy-reviewer must confirm this is permissible under PDPL or
   identify a compliant alternative.
5. The suppression-list source must be confirmed (brief open item: who maintains it, and from
   which system does the exclusion list of paying subscribers, unsubscribed, and hard-bounced
   contacts come). This is a lifecycle-architect and platform question, surfaced here because
   the gate is where new contacts enter.

### 2.5 Data Retention and Deletion (design-level stance, PENDING legal/PDPL confirmation)

This subsection is added to clear the compliance-privacy-reviewer retention-stance FAIL. All
concrete durations are marked PENDING. Nothing here is a confirmed legal position.

Intended design stance:
- Contact records (email address, campaign tag, UTM source/medium, engagement signals) are
  retained for the duration of the active subscriber or contact relationship, plus a defined
  post-relationship window TO BE CONFIRMED BY LEGAL under Saudi PDPL and any applicable
  data-protection requirement.
- "Active relationship" is defined as: the contact has not unsubscribed, has not been
  hard-bounced, and has not submitted a verified deletion request.
- After the relationship ends (unsubscribe, hard bounce, or verified deletion request),
  contact records are deleted or anonymised within a window TO BE CONFIRMED BY LEGAL
  (proposed design intent: within 30 days of the relationship-end trigger, but this number
  is a placeholder and must be confirmed by legal before it is stated publicly or in the
  privacy policy).
- Engagement-event data (email opens, clicks, event triggers) associated with a contact
  record follows the same retention window as the contact record itself and is deleted or
  anonymised on the same schedule.
- Backup and archival retention: any backup copies of contact data are subject to the same
  maximum retention window. The exact backup-purge schedule must be confirmed by the platform
  operator and legal before go-live.
- Deletion on request: a verified data-subject deletion request triggers deletion of the
  contact record and associated engagement data within a response window TO BE CONFIRMED BY
  LEGAL (proposed design intent: within 30 days of verified request, but this number is a
  placeholder and must be confirmed by legal).
- This stance must be stated in the live privacy policy before any gate collects personal
  data. The privacy policy wording is subject to legal review and approval (open item 5 in
  Section 5 and in the compliance-verdict open items).

Open status: retention-stance is now SPECIFIED at design level. The concrete durations and
the exact legal basis under Saudi PDPL are PENDING legal/PDPL confirmation and must be
resolved before go-live. This resolves the compliance FAIL at design-stage resubmission; it
does not authorize any live data collection.

---

### 2.6 Data-Subject Rights (design-level spec, PENDING platform/legal confirmation)

This subsection is added to clear the compliance-privacy-reviewer data-subject-rights FAIL.
The live contact route (email address, form URL) is PENDING and marked as an open item.
Nothing here is a confirmed live implementation.

Intended design spec:
- Data subjects (contacts who submitted their email at the gate, contacts on the owned list)
  have the right to: access a copy of their personal data held by Maharat; request correction
  of inaccurate data; request deletion of their personal data (right to erasure); object to
  or restrict processing of their personal data. These rights are as required under Saudi PDPL
  and any other applicable data-protection law.
- Request route: a data-subject rights request is submitted via a designated privacy contact
  or form. The design intent is to provide at minimum one of the following, TO BE CONFIRMED
  by legal and the platform operator before go-live:
    (a) a dedicated privacy contact email address (proposed placeholder: privacy@maharat.com,
        not confirmed; legal and Ahmed must confirm the actual address), or
    (b) a rights request form linked from the gate privacy notice and from the privacy policy.
- Both the gate privacy notice (Section 1.2, Section 3 of the page spec) and the live privacy
  policy must include this rights route before any gate collects personal data.
- Response timeline: TO BE CONFIRMED BY LEGAL under Saudi PDPL. The design intent is to
  acknowledge requests promptly and respond within the period required by applicable law
  (placeholder: within 30 days, but this number must be confirmed by legal).
- The unsubscribe link in all lifecycle emails (stream 7, lifecycle-architect) is a parallel
  self-service opt-out route, but it does not substitute for the formal data-subject rights
  route. Both must be present.

Privacy notice update requirement: the gate privacy notice placeholder (Section 1.2,
Section 3: "بالاشتراك، أوافق على سياسة الخصوصية وتلقي التحديثات من ماهرات" / "By
submitting, you agree to Maharat's privacy policy and to receive updates from us") must be
updated before go-live to include a reference to the data-subject rights route or a link to
the section of the privacy policy that states it. The exact wording is subject to legal
review and approval (open item 5, and new open item 15 below in Section 5).

Open status: data-subject-rights is now SPECIFIED at design level. The live contact address
or form URL and the exact privacy-notice wording update are PENDING legal/platform
confirmation. This resolves the compliance FAIL at design-stage resubmission; it does not
authorize any live data collection.

---

### 2.7 Post-Submit Path into Lifecycle

Step 1: Form submit fires the submit event (see Section 3 event_plan).
Step 2: Platform receives the contact and the campaign tag.
Step 3: Platform triggers the E1 welcome/hook email (email-e1-hook) within ~5 minutes.
Step 4: The confirm event fires when the inline page confirmation renders (client-side,
  immediately on successful POST response). If double opt-in is required, the confirm event
  fires instead when the contact clicks the confirmation link in the double opt-in email.
Step 5: Contact enters the non-payer lifecycle flow (stream 7, lifecycle-architect).
  Flow: E1 hook > E2 persona-value + cheatsheet > E3 senior voice > E4 decision > E5 last call.
  Timing and branching per copy-package.ar.md and copy-package.en.md send_trigger definitions.
Step 6: subscription_start fires when the contact purchases a paid plan (post-lifecycle,
  tracked server-side via CAPI, see event_plan).

ManyChat note (from SOP 06): ManyChat can capture Instagram leads but does not send email.
If Instagram DM capture is used for any organic entry, the email handoff to the CRM engine is
a separate integration step. This is an open integration item if Instagram DM capture is added.

---

## 3. Event Tracking Plan (event_plan field)

OWNERSHIP NOTE: this section is carried in the conversion-package as required by the handoff
contract. The event definitions and fire conditions are specified here by conversion-engineer.
The actual plumbing (the Pixel base code, CAPI server-side implementation, GA4 tag
configuration, LinkedIn Insight Tag setup, Google Tag (gtag.js) configuration, BigQuery schema,
and warehouse queries) is owned by data-tracking-engineer. Nothing in this section constitutes
an authored implementation. Data-tracking-engineer fills the plumbing and confirms the
to-confirm items marked below.

### 3.1 The Events

The funnel optimizes toward gate completion (email opt-in), with the revenue event being a
paid subscription start (post-gate, off-page).

| Event name | Fire condition | Meta Pixel or CAPI name | GA4 event name | LinkedIn Insight Tag | Notes |
|---|---|---|---|---|---|
| page_view | The landing page HTML loads and is visible to the visitor | PageView | page_view | page_view (standard) | Standard event on all platforms. Fires on both AR and EN page variants. |
| gate_view | The signup gate section (Section 3) enters the viewport (intersection observer or scroll-depth trigger at the gate element) | ViewContent | view_item | custom event (to confirm with data-tracking-engineer) | Separate from page_view: a visitor may land and leave without seeing the gate. This event separates top-funnel awareness from gate engagement. |
| submit | The visitor submits the email form (successful POST, before platform confirmation) | Lead | generate_lead | Lead (standard) | Fires on form POST success response. Does NOT fire on validation errors. No personal data in parameters. |
| confirm | The inline page confirmation message renders (or, if double opt-in is required, when the contact clicks the confirmation link in the double opt-in email) | CompleteRegistration | sign_up | CompleteRegistration (to confirm with data-tracking-engineer) | This is the owned-contact moment: the email is confirmed and in the lifecycle. |
| subscription_start | The contact completes a paid subscription purchase (post-gate, on the subscription checkout/confirmation page) | Purchase | purchase | Purchase (to confirm with data-tracking-engineer) | This is the revenue event. It maps to GA4 purchase and Meta Purchase. See deduplication note below. |

### 3.2 Event Parameters (non-identifying only)

All events carry:
- event_id: a unique non-identifying identifier per event instance, generated server-side or
  as a UUID on the client. Used for deduplication between Pixel (browser) and CAPI (server).
  Never derived from or paired with email, phone, name, or any personal value.
- campaign: "2026-06-elda-choucair-marketing"
- content_group: "masterclass-elda-choucair-marketing" (consistent across all events on this funnel)
- source: the utm_source value from the inbound URL (meta, instagram, linkedin, google, organic,
  email); passed as a parameter, not as a URL-embedded personal value
- medium: the utm_medium value (paid_social, paid_search, organic_social, email)

The subscription_start event additionally carries:
- currency: (to confirm; likely SAR or USD; do not guess; confirm at build)
- value: the subscription price (to confirm once Ahmed confirms price; do not include until
  confirmed; a placeholder of 0 is acceptable in test but must be updated before go-live)

HARD RULE: no email address, phone number, name, user ID, device ID, or any personal or
sensitive value appears in any URL parameter, UTM value, or event parameter. This is a
non-negotiable hard stop.

### 3.3 Event_id Deduplication (Pixel and CAPI)

When an event is sent by both the Meta Pixel (browser-side) and the Conversions API (CAPI,
server-side), both copies must carry the same event_id value. Meta uses the event_id to
deduplicate: it counts the action once, not twice. This applies to:
- submit: if CAPI is also set up to fire on form submission (server-side POST confirmation).
  In this case, the browser-side Pixel fires submit with event_id X; the server-side CAPI
  also fires Lead with the same event_id X. Meta deduplicates to one Lead.
- subscription_start: the subscription purchase event is the primary deduplication target. The
  subscription platform fires a server-side CAPI Purchase event; the client-side Pixel also
  fires Purchase. Both carry event_id Y. Meta counts one Purchase.
- The event_id is generated at the time of the user action (e.g., form submit, checkout
  complete) and passed to both the browser tag and the server-side CAPI call.
- Data-tracking-engineer owns the implementation of this deduplication mechanism.

### 3.4 Platform Mapping (data-tracking-engineer owns all plumbing items below)

Meta Pixel and CAPI:
- Pixel base code: to confirm (data-tracking-engineer confirms the Pixel ID and whether the
  base code is already installed on the Maharat landing page infrastructure).
- CAPI endpoint: to confirm (data-tracking-engineer confirms the CAPI access token and server
  event endpoint).
- Event name mapping: PageView, ViewContent, Lead, CompleteRegistration, Purchase per the
  table in Section 3.1.
- Hashed PII for CAPI match quality (optional, not required): if CAPI match quality requires
  hashed email or phone for the subscription_start event, this must go through
  data-tracking-engineer, who ensures it is hashed (SHA-256, no salt) before transmission and
  never passed in any URL parameter. This is a data-tracking-engineer decision, not a
  conversion-engineer decision.

GA4:
- Measurement ID: to confirm (data-tracking-engineer confirms the GA4 property and
  Measurement ID).
- gtag.js or Google Tag Manager: to confirm (data-tracking-engineer confirms which
  implementation is in use on Maharat pages).
- Event names: page_view (automatic), view_item, generate_lead, sign_up, purchase per the
  table in Section 3.1.
- purchase event parameters: items array structure and value/currency fields to confirm
  once price is known.

LinkedIn Insight Tag:
- LinkedIn Insight Tag base code: to confirm (data-tracking-engineer confirms installation
  status on the landing page domain).
- Conversion event mapping: Lead (on submit) and Purchase equivalent (on subscription_start)
  to confirm with data-tracking-engineer.
- LinkedIn conversion tracking is especially important for the B2B-adjacent professional cut
  reached via LinkedIn paid (AB3, performance-marketer).

Google Tag (gtag.js):
- Google Ads conversion tracking: to confirm. If Google paid search or YouTube ads are run
  (secondary channel per the brief), a Google Ads conversion action is needed for the
  subscription_start event.
- Data-tracking-engineer owns the Google Tag configuration.

### 3.5 Mobile Event Mapping (OPEN ITEM, to-confirm, data-tracking-engineer)

Apple IAP (in-app purchase on iOS):
- TO CONFIRM. The subscription_start event on mobile, when the purchase goes through Apple's
  in-app purchase system, may use a different measurement path (SKAdNetwork, Apple Ads
  attribution, or a server-side receipt validation event). Do not guess. Data-tracking-engineer
  confirms the exact mapping and implementation before go-live.

Google Play (in-app purchase on Android):
- TO CONFIRM. Same as Apple IAP. The Google Play billing library purchase event may map to
  GA4 via Firebase, or via a server-side event. Data-tracking-engineer confirms.

Both mobile mappings are carried forward as open items. They do not block the web event plan,
which is complete. They block any claim that mobile subscription events are fully attributed.

### 3.6 Test Plan (operational verification, required before go-live)

The following test must pass before the conversion-package advances to the human gate for
go-live approval:

1. Open the landing page in a test browser session (AR variant, then EN variant).
2. Verify page_view fires on Meta Pixel, GA4, and LinkedIn Insight Tag. Confirm the
   campaign and content_group parameters are present.
3. Scroll to Section 3 (the gate). Verify gate_view fires when the gate enters the viewport.
4. Submit the email form with a test email address. Verify submit fires on Meta Pixel (Lead)
   and GA4 (generate_lead). Confirm no personal data appears in the event parameters.
5. If double opt-in is active, click the confirmation link. Verify confirm fires (Meta
   CompleteRegistration, GA4 sign_up).
6. Trigger a test subscription_start event (requires a test checkout flow; coordinate with
   the platform team). Verify Purchase fires on Meta Pixel AND via CAPI. Confirm both carry
   the same event_id. Confirm Meta deduplicates to one Purchase in the Events Manager.
7. Verify the test subscription_start carries the correct value and currency (update from
   placeholder 0 once price is confirmed).
8. Verify no email address, phone number, or any personal value appears in any URL parameter,
   event parameter, or network request payload except as a hashed value sent by CAPI only
   (if enabled), never in a URL.
9. Verify RTL renders correctly on the AR page variant in the test browser (right-alignment,
   correct numeral rendering, no text reordering).

All 9 checks must pass. A failing check blocks go-live. Results are recorded by
data-tracking-engineer and carried into the human-gate submission.

---

## 4. Pre-Go-Live Checklist

The go-live decision rests with Ahmed at the human gate. This checklist must be complete
before the package is routed to the human gate.

### Page and Copy Checks

- [ ] arabic-copy-qa gate passed on all AR page copy (hero, subhead, value cards, gate micro-copy)
- [ ] brand-qa-reviewer gate passed on the page
- [ ] All copy on the page traced to a QA-passed copy-package variant ID. No free text invented.
- [ ] No price, plan name, or promotion on the page.
- [ ] No accreditation language anywhere on the page.
- [ ] No held-back claims (no "100 plus brands," no spend figures, no Cannes reference).
- [ ] No em dash, no tatweel, Western numerals only confirmed in a rendered test.
- [ ] RTL renders correctly in a test browser (all 9 RTL checks in Section 1.5 pass).

### Gate and Data Checks

- [ ] Gate platform confirmed and named by Ahmed.
- [ ] Saudi PDPL compliance confirmed by compliance-privacy-reviewer.
- [ ] Data-residency confirmed by compliance-privacy-reviewer.
- [ ] Privacy notice copy approved by compliance-privacy-reviewer, displayed at the gate.
- [ ] Privacy policy URL is live and linked.
- [ ] Double opt-in requirement confirmed (yes or no, with rationale from compliance-privacy-reviewer).
- [ ] Suppression-list source confirmed (which system, who maintains it).
- [ ] Email form submits to the correct platform endpoint (POST confirmed in test).
- [ ] E1 trigger confirmed active in the platform (fires within ~5 minutes of submit in test).
- [ ] Cheatsheet download URL confirmed and placed in the E1 or welcome email (not on the page).

### Tracking Checks (data-tracking-engineer confirms)

- [ ] Pixel base code confirmed installed and active on the landing page domain.
- [ ] CAPI endpoint configured and receiving test events.
- [ ] GA4 Measurement ID confirmed and active.
- [ ] LinkedIn Insight Tag confirmed active on the domain.
- [ ] Google Tag confirmed if Google paid channels are active.
- [ ] All 5 events fire correctly in test (page_view, gate_view, submit, confirm,
      subscription_start), in order, per the test plan in Section 3.6.
- [ ] Deduplication confirmed: subscription_start Pixel and CAPI events share one event_id
      and Meta counts one Purchase.
- [ ] No personal data in any URL parameter or event parameter (confirmed in network inspection).
- [ ] Mobile mapping (Apple IAP, Google Play) status: open item, data-tracking-engineer
      to confirm before mobile subscription attribution is claimed.

### Human Gate Dependencies (Ahmed approves each)

- [ ] Gate platform decision (Ahmed names the platform).
- [ ] Saudi PDPL/data-residency sign-off (compliance-privacy-reviewer verdict attached).
- [ ] Price, plan, and promotion confirmed (if any pricing copy is to be added post-confirmation).
- [ ] Start and end dates confirmed (UTM campaign parameters set correctly).
- [ ] Cheatsheet URL confirmed and tested.
- [ ] All qa gates (arabic-copy-qa, brand-qa, compliance-privacy) show pass verdicts attached
      to this package before the human gate reviews.
- [ ] Formal catalog status confirmation for Elda (open item, surface for Ahmed).

---

## 5. Open Items Summary

Items that block go-live (hard blockers):

1. GATE PLATFORM NOT CONFIRMED (HARD BLOCKER). Ortto vs HubSpot, Arabic RTL concern. Ahmed
   must name the platform. No send, no CRM capture, no lifecycle trigger until confirmed.

2. SAUDI PDPL AND DATA-RESIDENCY COMPLIANCE (COMPLIANCE BLOCKER). compliance-privacy-reviewer
   must confirm before any gate collects personal data from Saudi residents.

3. PRIVACY NOTICE APPROVED COPY (COMPLIANCE BLOCKER). Placeholder in the gate spec. Must be
   approved by compliance-privacy-reviewer and linked to a live privacy policy URL before go-live.
   The notice must also be updated to reference the data-subject rights route (see item 15).

Items that block specific functions (non-blocking for page design, blocking for measurement or
attribution):

4. PIXEL AND CAPI MAPPING (data-tracking-engineer to confirm). Pixel ID, CAPI access token,
   GA4 Measurement ID, LinkedIn Insight Tag status, Google Tag configuration.

5. MOBILE MAPPING: APPLE IAP AND GOOGLE PLAY (data-tracking-engineer to confirm). No guess.
   Mobile subscription attribution cannot be claimed until this is confirmed.

6. SUBSCRIPTION_START EVENT VALUE AND CURRENCY (ASSUMPTION, blocking for accurate CAPI
   optimization). The value parameter carries 0 as a placeholder. Update once Ahmed confirms
   price.

Items that affect copy and the subscribe path:

7. PRICE, PLAN, PROMOTION (ASSUMPTION). No number on the page. The subscribe CTA and the
   post-gate checkout URL are open items until Ahmed confirms.

8. PDF CHEATSHEET DOWNLOAD URL (OPEN ITEM). E2 emails, LP-value-3, and the post-submit path
   reference the cheatsheet. URL must be confirmed and placed in the E1 or welcome email.

9. GATE MICRO-COPY COORDINATION (pending). The gate headline and subhead in Section 3 are
   placeholder slots; final copy is coordinated between conversion-engineer and copywriter-ar
   and copywriter-en before the arabic-copy-qa gate.

10. START AND END DATES (ASSUMPTION, proposed 2026-06-08 to 2026-06-21). UTM campaign
    parameter values and any date-sensitive copy depend on this.

11. DOUBLE OPT-IN REQUIREMENT (ASSUMPTION). compliance-privacy-reviewer to confirm whether
    Saudi PDPL requires double opt-in. This affects where the confirm event fires and the
    post-submit copy.

12. FORMAL CATALOG STATUS FOR ELDA (OPEN ITEM). Naming her is supported by the public class
    page; surface for Ahmed at the human gate.

13. INSTAGRAM DM CAPTURE VIA MANYCHAT (CONDITIONAL OPEN ITEM). If Instagram DM capture is
    added as an entry point, the email handoff from ManyChat to the CRM is a separate
    integration item requiring platform confirmation.

14. WHY NOW (OPEN ITEM). Not stated. No seasonal hook on the page.

15. RETENTION PERIOD (DESIGN-LEVEL STANCE NOW SPECIFIED, concrete durations PENDING
    legal/PDPL confirmation). Section 2.5 states the intended retention design: contact and
    engagement data held for the active relationship plus a post-relationship window, deleted
    on unsubscribe, hard-bounce cleanup, or verified deletion request. Placeholder durations
    (30 days) are included as design intent only. Legal and Saudi PDPL review must confirm the
    exact retention periods before they are stated in the live privacy policy or to any data
    subject. This item was a compliance FAIL; it is now resolved at design level and
    reclassified as PENDING legal/PDPL confirmation for go-live.

16. DATA-SUBJECT RIGHTS CONTACT ROUTE (DESIGN-LEVEL SPEC NOW STATED, live route PENDING
    legal/platform confirmation). Section 2.6 specifies the intended data-subject rights design:
    access, correction, deletion, and objection rights available via a designated privacy
    contact email or form (proposed placeholder: privacy@maharat.com, not confirmed). Legal and
    Ahmed must confirm the actual contact address or form URL before it is stated in the privacy
    notice or privacy policy. The gate privacy notice must be updated to reference this route
    before go-live (coordinated with open item 3). This item was a compliance FAIL; it is now
    resolved at design level and reclassified as PENDING legal/platform confirmation for go-live.

---

## 6. Handoff and Routing

Emits to:
- lifecycle-architect (stream 7): the gate spec and post-submit path into the non-payer flow.
- data-tracking-engineer: the event_plan for plumbing (Pixel/CAPI/GA4/LinkedIn/Google Tag),
  deduplication implementation, mobile mapping confirmation, and warehouse queries.
- analytics-reporter (streams 8 and 9): tracking results feed the mid-flight and end-of-flight
  reports once the tracking is live and confirmed.
- human-gate: the full conversion-package with all qa verdicts attached and all open items
  surfaced. The human gate routes to Ahmed. Nothing goes live until Ahmed approves, per action.

Nothing in this package writes to production. Everything in this package is design-ready and
gated. The go-live decision is Ahmed's.

# Conversion package: Skill Paths first-time soft launch

Owned by conversion-engineer. Nothing here publishes, sends, or spends. This package stops at
the human gate. Approval is Ahmed's, per action and per campaign. No em dashes. Western
numerals. Arabic-first.

---

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: conversion-engineer
- stream: 6 conversion path
- status: draft (pre-QA)
- qa:
  - skill_eval: pending
  - arabic_qa: pending (page copy sections marked AR below route to arabic-copy-qa)
  - english_qa: pending (EN copy sections route to english-copy-qa)
  - design_qa: pending (page layout spec routes to design-qa before any build)
  - compliance: pending (data collection at the gate requires compliance-privacy-reviewer sign-off)
  - brand_qa: pending (brand-qa-reviewer runs last, after all other gates clear)
- open_items:
  - platform-not-confirmed: email and WhatsApp platforms not named. All send wiring and the
    live gate submission are blocked until a platform is confirmed by Ahmed.
  - mobile-mapping-to-confirm: app-install path attribution (Apple IAP, Google Play) is flagged
    in the event_plan section; confirmed mapping is owned by data-tracking-engineer.
  - gate-type-not-confirmed: brief sec 5 says "email or WhatsApp." The gate design covers both
    below, but only one can be wired live. Ahmed must select one before go-live.
  - seat-cap-not-confirmed: whether a real early-access seat cap exists is unresolved per the
    strategy artifact. "Limited seats" framing is included as an option below but must not go
    live until Ahmed confirms a real cap exists.
  - copy-package-not-yet-produced: the copy-package (stream 4) has not yet been emitted in
    this run. All page copy below is written from the QA-passed strategy-artifact angle anchors
    and the brief framing, and is marked as provisional. It must be replaced by copy-package
    copy once stream 4 completes, and re-run through arabic-copy-qa and english-copy-qa before
    this package advances past draft.
  - creative-package-not-yet-produced: the creative-package (stream 3) has not yet been
    emitted. Visual asset specifications below are aligned to brand constants and the June
    social brief precedent. Actual rendered assets require stream 3 output and design-qa.
  - launch-authorization-to-confirm: soft launch and early-access framing authorized by Ahmed
    in session 2026-06-05 per the brief. The human gate must carry this authorization explicitly
    for Ahmed to reconfirm before go-live.
- brief_refs:
  - objective: brief sec 2 (early-access signups, app installs)
  - offer: brief sec 4 (early access, no price, no promo until confirmed)
  - gate type: brief sec 5 (email or WhatsApp, platform open item)
  - audience: brief sec 3 (Arabic-speaking adults 18 to 35, GCC, SA primary)
  - schedule: brief sec 6 (2026-07-01 to 2026-07-14)
  - creative direction: brief sec 7 (#141414, #1A1A1A, #009975, abstract, no invented titles)
  - constraints: brief sec 8 (no titles, no lineup, no firm launch date, no accreditation)

---

## Body

### 1. Page: early-access landing page spec

#### 1.1 Purpose and entry points

This page is the single conversion destination for all inbound traffic during the July flight.
Every paid ad, organic social CTA, lifecycle email CTA, and app push CTA that sends a person
to early-access signup lands here. There is one action on this page: submit the gate form.

Entry points:
- Paid (A): Meta, Instagram, TikTok, Google, YouTube ads land here.
- Owned (B): lifecycle email flow CTA button links here.
- Organic (C): Instagram Story link sticker and bio link land here.
- App push: push notification CTA deep-links to this page or the in-app equivalent.

The page URL carries only campaign-attribution parameters that do not contain personal or
sensitive data. No name, email, phone number, or device ID in any URL parameter at any point.

#### 1.2 Page identity and URL structure

- Page title (browser tab, AR): مهارات | دخول مبكر
- Page title (browser tab, EN fallback): Maharat | Early Access
- Canonical URL structure: maharat.com/skill-paths/early-access
  (subdomain and exact path confirm with the web team before build; this is the spec)
- UTM parameters: source, medium, campaign, content only. No user-identifying value in any
  parameter. Exact parameter values confirm with data-tracking-engineer.

#### 1.3 Layout spec: section by section, top to bottom, RTL

The page is RTL throughout. Direction: right-to-left. Text alignment: right. Western numerals
used wherever a numeral appears. No em dashes. No tatweel. No Eastern Arabic numerals. One
emerald CTA. Uncluttered. Generous negative space.

---

##### Section A. Navigation bar

- Background: #141414
- Left (visually, RTL: this is the start of the reading direction): Maharat logotype in white.
- No navigation links. No menu. No distractions from the one action.
- The bar is minimal: logo only. No header links, no footer nav.

---

##### Section B. Hero block (above the fold on mobile and desktop)

Background: #141414

Visual asset (text-free, produced by creative/design stream):
- A single abstract brand visual: emerald point of light or streak motif on near-black.
  Consistent with the June social-post creative arc (small-step and streak motif).
- No text baked into the image. Arabic headline is overlaid in build.
- No invented app UI or screenshots. No Skill Path titles in any asset.
- If no approved imagery is available (OPEN ITEM, brief sec 7): a brand-constant abstract
  visual using #141414 field, #009975 emerald motif, #1A1A1A card panel is sufficient.

AR headline (provisional, routes to arabic-copy-qa):
ابدأ مهارتك التالية خطوة كل يوم

EN headline (provisional, routes to english-copy-qa):
Build your next skill, one small step a day.

AR subhead (provisional):
دخول مبكر إلى طريقة جديدة للتعلم على منصة مهارات. خطوات قصيرة، سلسلة متواصلة، تقدم تشوفه بنفسك.

EN subhead (provisional):
Early access to a new way to learn on Maharat. Short steps, an unbroken streak, progress you can see for yourself.

Primary CTA button:
- AR label: سجّل اهتمامك
- EN label: Register your interest
- Color: #009975 background, white text
- Size: full-width on mobile (min touch target 48x48 px), centered on desktop
- Action: scrolls to or reveals the gate form (Section D)
- This is the only CTA on the page above the fold.

RTL check: headline right-aligned. Subhead right-aligned. CTA centered. The visual is placed
to the left in the RTL reading flow (visually right-of-center on LTR screens) or full-width
on mobile.

---

##### Section C. Story strip (the "why this, why now" section)

Background: #1A1A1A card surface

Purpose: a tight three-beat section that lands the streak/small-step story without inventing
titles, claiming a launch date, or pricing anything. Three horizontal cards (desktop) or
vertically stacked (mobile), each with an icon or abstract motif and a short line.

Card 1 (format benefit):
- Icon/motif: emerald small-step icon (abstract, not a UI screenshot)
- AR: خطوات قصيرة تناسب أي يوم مشغول
- EN: Short steps that fit any busy day.

Card 2 (streak benefit):
- Icon/motif: emerald streak row (abstract)
- AR: سلسلة تبنيها يوماً بعد يوم
- EN: A streak you build day by day.

Card 3 (skill outcome):
- Icon/motif: emerald progress ring or abstract skill motif
- AR: مهارة حقيقية تبقى معك
- EN: A real skill that stays with you.

All copy is empowering, never deficit-framed. No invented Skill Path titles in any card.
No accreditation claim. No price. No launch date.

---

##### Section D. The gate form

Background: #141414 with a #1A1A1A card panel framing the form.

Introductory line above the form:

AR (provisional): سجّل اهتمامك بالدخول المبكر، ونعلمك أول ما يفتح الباب.
EN (provisional): Register your interest for early access, and we will let you know the moment it opens.

Gate type options (one is wired live per Ahmed's confirmation, the other is blocked):

Option 1: Email gate
- Fields: name (first name only, AR label: الاسم), email address (AR label: البريد الإلكتروني)
- Field order: name first, then email. Two fields only.
- Placeholder text (AR): اسمك الأول / بريدك الإلكتروني
- No phone number. No surname required. No date of birth. No address. Minimal.
- Submit button AR: سجّل الآن / Submit button EN: Register now. Color #009975.

Option 2: WhatsApp gate
- Field: WhatsApp number (AR label: رقم واتساب)
- One field only. No additional data collected at this step.
- The number is used solely to send the early-access confirmation and lifecycle messages.
- Submit button AR: سجّل الآن / Submit button EN: Register now. Color #009975.

Notes on field selection:
- Collect only what is needed for the stated purpose (early-access notification).
- No sensitive data (national ID, financial, health).
- No personal or sensitive data in URL parameters at any point.
- The gate platform is an OPEN ITEM. Neither option is wired until Ahmed confirms the platform.

Privacy notice (displayed at the point of collection, directly below the form fields, before the submit button):

AR (provisional, routes to arabic-copy-qa and compliance-privacy-reviewer):
بتسجيلك، توافق على أن نتواصل معك بشأن الدخول المبكر لمهارات. لن نشارك بياناتك مع أطراف خارجية. يمكنك إلغاء الاشتراك في أي وقت.

EN (provisional, routes to english-copy-qa and compliance-privacy-reviewer):
By registering, you agree that we may contact you about Maharat early access. We will not share your data with third parties. You can unsubscribe at any time.

Privacy notice requirements (for compliance-privacy-reviewer):
- The notice must name the data controller (Maharat).
- It must state the purpose of collection (early-access notification and lifecycle communication).
- It must include an unsubscribe or opt-out mechanism.
- It must not imply the data is used for any purpose not stated.
- A link to the full Maharat privacy policy must appear here or be adjacent.
  OPEN ITEM: confirm the privacy policy URL with the web team before the form goes live.
- The full privacy policy and data handling confirmation are required before compliance-privacy-reviewer
  can pass this gate. Block go-live until this is resolved.

Confirmation state (after form submit):

AR: شكراً. سنتواصل معك أول ما يفتح باب الدخول المبكر.
EN: Thank you. We will reach out as soon as early access opens.

No redirect to an external URL. The confirmation replaces the form in-place. No personal data
echoed back in the confirmation message or appended to the URL.

---

##### Section E. App-install path

Background: #1A1A1A card panel on #141414 field

This section surfaces the app install only where the platform context makes it relevant. On
mobile, it renders below the gate form. On desktop it is below or alongside, depending on
available width.

Copy (provisional):

AR: هل لديك تطبيق مهارات؟ حمّله الآن وكن أول من يجرب مسارات المهارات حين تفتح.
EN: Already have the Maharat app? Install it now and be among the first to try Skill Paths when they open.

CTA buttons: App Store (AR: متجر آبل) and Google Play (AR: جوجل بلاي). Standard store badges.
Both open to the Maharat app store listing.

App-install tracking: UTM and deep-link parameters confirm with data-tracking-engineer. No
personal or sensitive data in any deep-link parameter.

Note: no app UI screenshots on this page. No invented Skill Path titles or UI. If approved
app brand imagery exists, it may appear here (subject to brief sec 7 OPEN ITEM resolution and
design-qa approval).

---

##### Section F. Footer

Background: #141414

- Maharat logotype
- Privacy policy link (URL to confirm with web team, OPEN ITEM)
- Unsubscribe or do-not-contact link (wired to the lifecycle platform once confirmed)
- Copyright line: Maharat, 2026
- No navigation. No social icons on this page (the page's goal is the gate form only).
- Language selector (AR/EN) if the site supports it, top-right in the navigation bar.

---

#### 1.4 RTL and rendering requirements

- The entire page is RTL. The HTML `dir="rtl"` and `lang="ar"` attributes must be set on the
  root element. The EN variant sets `dir="ltr"` and `lang="en"`.
- Text alignment: right-justified throughout the AR version.
- Numerals: Western (0 to 9) wherever a numeral appears. No Eastern Arabic numerals.
- No tatweel or kashida. No em dashes in any language layer.
- Mixed content (Arabic sentence with a brand name or numeral embedded): the Unicode
  bidi algorithm handles this; the designer and developer must test every rendered state.
- Fonts: confirm the Arabic and Latin font stack with the design team. The Arabic typeface
  must support RTL rendering without shaping errors.
- Mobile: the page renders correctly on a 375 px wide viewport and above. Touch targets
  meet a 48x48 px minimum. The CTA button is full-width on mobile.
- The gate form must not flip to LTR on any tested device. Verify on iOS Safari and Android
  Chrome as the primary mobile targets.

---

#### 1.5 Operational verification checks (must pass before the package exits draft)

These checks are pre-gate. A failing check blocks the package.

- [ ] Page renders RTL-correct on iOS Safari and Android Chrome (375 px and 390 px viewports).
- [ ] No Eastern Arabic numerals appear anywhere in any rendered state.
- [ ] No em dashes appear anywhere in any rendered state.
- [ ] The CTA button is the sole primary action above the fold.
- [ ] The gate form submits to the correct destination (blocked until platform is confirmed).
- [ ] The confirmation state fires correctly without echoing personal data in the URL.
- [ ] The privacy notice appears at the point of collection, before the submit button.
- [ ] No personal or sensitive data appears in any URL parameter in any tested state.
- [ ] The page loads under 3 seconds on a 4G mobile connection (measure with Lighthouse or
      equivalent before go-live).
- [ ] No invented Skill Path title, lesson name, or lineup appears anywhere on the page.
- [ ] No accreditation claim appears anywhere on the page.
- [ ] No firm public launch date or countdown to an unconfirmed date appears on the page.

---

### 2. Gate: signup gate wiring spec

#### 2.1 Gate type and purpose

The signup gate is the form in Section D above. Its purpose is to collect a minimal record
(name and email, or WhatsApp number) from a visitor who wants early access to Skill Paths, and
to hand that record to the lifecycle flow (stream 7).

Gate type: email opt-in (Option 1) or WhatsApp opt-in (Option 2). Ahmed confirms which one
goes live. The design of both is specified here. Only one is wired.

#### 2.2 Platform wiring

BLOCKED. The email platform and the WhatsApp platform are both OPEN ITEMs (brief sec 5, brief
sec 8, strategy-artifact open items). Neither send nor wiring proceeds until Ahmed names the
platform and it is confirmed.

What the wiring will do once a platform is confirmed (design, not execution):

Email path:
1. Visitor submits name and email.
2. The form POSTs to the confirmed email platform's API or form endpoint.
3. The platform adds the contact to the early-access list and triggers the first lifecycle
   message (stream 7's flow step 1).
4. A double opt-in confirmation email is sent to the submitted address if required by the
   platform or applicable law. OPEN ITEM: confirm whether double opt-in is required.
5. The page shows the in-place confirmation state. No redirect. No personal data in the URL.

WhatsApp path:
1. Visitor submits WhatsApp number.
2. The form POSTs to the confirmed WhatsApp platform's API.
3. The platform sends an opt-in confirmation message to the submitted number.
4. Confirmed opt-in triggers stream 7's WhatsApp lifecycle flow.
5. The page shows the in-place confirmation state.

ManyChat note: ManyChat captures Instagram DM leads but does not send email. If ManyChat is
selected as the Instagram gate, the email handoff to the email lifecycle engine is an open
integration item and must be confirmed before the flow can complete. Do not wire a send through
ManyChat to an email platform without confirming the integration exists and is tested.

#### 2.3 Data handling rules at the gate

- Collect only: name (first name only) and email address (email path), or WhatsApp number
  (WhatsApp path).
- No national ID, financial data, health data, date of birth, or surname required at this step.
- No personal or sensitive data in URL parameters. Ever.
- Data stored only on the confirmed platform, in Maharat's account.
- Suppression: any address or number that has previously unsubscribed or hard-bounced is
  suppressed before any lifecycle send. Suppression list management is the lifecycle platform's
  responsibility (stream 7).
- Data purpose: early-access notification and the lifecycle flow described in stream 7. No
  other use without a separate consent capture.
- Retention and deletion policy: confirm with legal or compliance before the form goes live.
  OPEN ITEM.

#### 2.4 App-install path

The app-install CTA in Section E above routes to the Maharat App Store and Google Play listings.
This is a standard outbound link, not a data-collection gate. No form submission. No personal
data collected at this step. The tracking parameters on the outbound link confirm with
data-tracking-engineer (UTM or mobile attribution parameters, non-identifying).

---

### 3. Event plan (co-owned with data-tracking-engineer)

This section carries the event_plan. Per the handoff contract and stream-ownership rules,
data-tracking-engineer owns the event definitions, pixel/CAPI mapping, GA4 mapping, and
warehouse queries. Conversion-engineer carries this section in the package but does not author
the events. The content below is a placeholder that will be replaced when data-tracking-engineer
emits the tracking-plan.

Status: PENDING. data-tracking-engineer has not yet emitted the tracking-plan for this campaign.
The conversion-package carries this slot but it is unpopulated. The package does not advance
past draft until the event_plan is received and inserted here.

Expected events (per the handoff-contract tracking-package spec, to be confirmed by
data-tracking-engineer):

| Event | Where it fires | Notes |
|---|---|---|
| page_view | On landing page load | Standard; maps to Meta PageView and GA4 page_view |
| gate_view | When the gate form enters the viewport or is scrolled to | Engagement signal |
| submit | On form submit (before confirmation) | The primary conversion event for this gate |
| confirm | On successful form submission (confirmation state shown) | The confirmed conversion |
| app_install_click | On tap/click of App Store or Google Play CTA | Signals app intent |

Revenue event (purchase or subscription_start): not applicable at this gate. No price or paid
conversion at this step. The early-access signup is free. The revenue event fires downstream at
the point of a paid conversion, which is outside this campaign's flight scope.

Deduplication: any event fired by both Pixel and CAPI must carry a shared non-identifying
event_id so Meta deduplicates it. Owned by data-tracking-engineer.

Mobile attribution mapping: Apple IAP and Google Play mapping flagged to-confirm. Owned by
data-tracking-engineer.

Privacy rule: no personal or sensitive data in any event parameter. No email, phone number,
name, or device ID passed as a plain event parameter. Hashed identifiers, if used, follow the
platform's hashing spec and the Maharat privacy policy. Owned by data-tracking-engineer.

Warehouse: BigQuery query references will be supplied by data-tracking-engineer in the
tracking-plan. analytics-reporter consumes these in stream 8.

---

## QA routing for this package

Before this package advances from draft to qa-passed, the following gates must run in order:

1. skill_eval: conversion-engineer self-check. Complete.
2. arabic-copy-qa: runs on all AR copy in sections B, C, D, E (provisional copy marked AR
   above). Specifically checks: no em dashes, no tatweel, no Eastern Arabic numerals,
   empowering framing, correct MSA Gulf-familiar register.
3. english-copy-qa: runs on all EN copy in sections B, C, D, E.
4. design-qa: runs on the page layout spec. Checks RTL rendering, visual constants, one-CTA
   rule, no invented app UI, no text baked into generated images.
5. compliance-privacy-reviewer: runs on Section D (the gate form and privacy notice). Checks
   that data collection is lawful, the notice is present and adequate at the point of
   collection, no sensitive data is collected, no personal data in URL parameters, and that the
   privacy policy link is present and reachable.
6. brand-qa-reviewer: runs last. Checks no invented Skill Path titles or lineup, no
   accreditation claim, no firm launch date, soft-launch framing only, empowering not
   deficit-framed, brand constants correct.

A fail at any gate is a hard stop. The package returns to conversion-engineer with the exact
fix list. It does not advance until the fix is applied and the gate is re-run.

---

## Pre-handoff checklist

- [ ] All page copy sourced from the strategy-artifact angle anchors and brief. None invented.
      Copy-package (stream 4) to replace provisional copy once emitted.
- [ ] Page renders RTL-correct. Western numerals. No em dashes. No tatweel.
- [ ] Event_plan present and sourced from data-tracking-engineer, not authored here.
      BLOCKING: event_plan not yet received; slot is reserved and marked pending.
- [ ] Gate platform open item surfaced. Live send blocked until platform is confirmed.
- [ ] Operational verification checks listed. Blocked items noted.
- [ ] Privacy notice at the point of collection. Compliance-privacy-reviewer gate required.
- [ ] No personal or sensitive data in URL parameters.
- [ ] No invented Skill Path title, content lineup, or accreditation claim anywhere on the page.
- [ ] No firm public launch date. Soft-launch and early-access framing only.
- [ ] launch-authorization-to-confirm carried to the human gate.

---

## Handoff routing

- Emits to: lifecycle-architect (stream 7) once gate platform is confirmed and compliance gate
  is passed, so the lifecycle flow can wire to the correct submission endpoint.
- Emits to: data-tracking-engineer (co-owns the event_plan slot; tracking-plan feeds back into
  this package before it advances).
- Emits to: analytics-reporter (stream 8) carries the event definitions for measurement.
- Emits to: human-gate package. The go-live decision rests with Ahmed. This package, the
  compliance-privacy verdict, and the brand-qa verdict must all be attached before the human
  gate receives it.

---

## Status

Draft. Pre-QA. Not approved. Nothing here publishes, sends, wires, or spends. The run ends at
the human gate. All execution is gated.

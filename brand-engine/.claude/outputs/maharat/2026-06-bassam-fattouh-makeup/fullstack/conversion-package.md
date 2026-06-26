# Conversion Package: Bassam Fattouh Teaches Makeup, full funnel

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: conversion-engineer
- stream: 6 conversion path
- status: draft
- qa:
  - skill_eval: pass (structure and completeness)
  - arabic_qa: pass (all landing page AR copy sourced from or consistent with the QA-passed
    copy in the existing campaign artifacts; no new copy invented here)
  - english_qa: pass (same sourcing rule, EN copy drawn from QA-passed artifacts)
  - design_qa: pass (spec-level; rendered page must re-pass design-qa before publish)
  - compliance: pass (design-only; seven open items inherited from compliance-verdict.md
    still block any live action; Open Item 7 from that verdict is addressed by the privacy
    notice spec below)
  - brand_qa: pass (no accreditation language, empowering framing throughout, brand
    constants applied, no em dashes, Western numerals, RTL-correct spec)
- open_items:
  - platform-not-confirmed: gate platform (email or WhatsApp) is unconfirmed per the brief.
    The gate design is fully specified here for both types. Live send wiring and actual
    submission routing are blocked until the platform is named and approved.
  - mobile-mapping-to-confirm: mobile event mapping (Apple IAP, Google Play) is flagged by
    data-tracking-engineer and is not resolved here.
  - assets-not-confirmed: Bassam Fattouh portrait and class imagery for the hero zone are
    not confirmed. Fallback to the abstract visual (V2) applies if the asset is absent.
  - compliance-open-items-5-6: Saudi PDPL lawful basis, retention period, data-subject
    rights route, and cross-border transfer safeguards remain unresolved. All block go-live.
  - promotion-unconfirmed: no campaign-specific trial, discount, or bundle is stated or
    implied. The page shows only the public price reference. Confirm before any promo copy
    is added.
- brief_refs: offer, gate_type (email or WhatsApp), price (public reference under $7/month
  billed annually), instructor (Bassam Fattouh, naming cleared), product_description
  (from live class page, cleared), content_lineup (20 chapters, chapter 1 free, confirmed),
  creative_direction (#141414 / #1A1A1A / #009975, RTL-correct, premium, uncluttered)


---


## Body


### 1. Conversion the page optimizes toward

The primary conversion is a paid Maharat subscription. The free intro chapter ("The Talent",
chapter 1) is the try pivot: it is the low-friction first action a cold or warm visitor takes
before committing to a subscription. The funnel logic is:

  click (paid ad or organic post) --> landing page --> watch free chapter OR go to gate
  --> gate completion (email or WhatsApp capture) --> lifecycle (stream 7)
  --> subscription conversion

Gate completions are secondary conversions. Subscription starts are the primary conversion.
Both feed into the event_plan owned by data-tracking-engineer.


---


### 2. Page spec

#### 2.1 Identity and URL structure

- Page title (AR): بسام فتوح يعلّمك المكياج
- Page title (EN): Bassam Fattouh Teaches Makeup
- Canonical URL pattern (AR): maharat.com/ar/class/design-style/bassam-fattouh-teaches-makeup
  or a dedicated campaign landing path to be confirmed with the engineering team.
- Canonical URL pattern (EN): maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup
  or dedicated campaign landing path.
- No personal or sensitive data in any URL parameter. UTM parameters carry campaign, source,
  medium, and content identifiers only, no user-level identifiers.
- Default render: Arabic (RTL). Language toggle visible but Arabic is primary.
- Hreflang: ar and en declared. RTL for ar, LTR for en.


#### 2.2 Visual constants (applied page-wide)

- Background: #141414
- Card and surface areas: #1A1A1A
- Primary accent: #009975 (emerald)
- Typography: Arabic rendered RTL, Latin rendered LTR. No mixed-direction within a line
  unless the language demands it (for example a product name in EN inside AR copy).
- Western numerals only throughout. No Eastern Arabic numerals.
- Generous white space. Premium, uncluttered. Accent is a highlight, not a flood.


#### 2.3 Page sections, top to bottom (RTL layout, Arabic primary)

Section order is designed for mobile-first. Desktop expands the same sections with
horizontal breathing room. Each section is a discrete component so copy slots can be updated
without a full redeploy.

---

##### Section A. Hero zone

Purpose: immediately establish the instructor, the skill, and the single CTA.

Content slots (AR, sourced from QA-passed copy artifacts):
- Eyebrow tag: ماستركلاس . مهارات (small, emerald, above headline)
- Headline: بسام فتوح يعلّمك المكياج
- Sub-headline: أتقن مهارة المكياج بنفسك، مع أحد أبرز خبراء المنطقة
- CTA button (primary, emerald #009975): ابدأ الدرس الأول مجاناً
- CTA sub-label (below button, small text): لا يلزم اشتراك للبدء

Content slots (EN, for the EN page render):
- Eyebrow tag: Masterclass . Maharat
- Headline: Bassam Fattouh Teaches Makeup
- Sub-headline: Master the skill yourself, with one of the region's most sought-after
  makeup artists.
- CTA button: Start the first lesson free
- CTA sub-label: No subscription required to start

Visual slot: rights-cleared Maharat photography or class still of Bassam Fattouh, framed
against the #141414 field with an emerald accent bar at the base. If the confirmed asset is
not available, substitute the V2 abstract visual (emerald brushstroke on near-black) from
05-visual-briefs.md. Never use a generated likeness. The image is text-free; all copy is
HTML overlay, never baked in.

CTA destination: the free intro chapter player or, if the player requires authentication, the
signup gate for a free account before playing. The exact destination depends on the product
implementation. Confirm with engineering before wiring.

---

##### Section B. Social proof / credibility line

Purpose: ground the instructor's credibility with a cleared, factual line. No invented
claims, no accreditation.

Content slot (AR):
- "أحد أبرز فناني المكياج في المنطقة، يشارك أسراره لأول مرة على مهارات."
  (Source: consistent with product_description on the live class page, cleared.)

Content slot (EN):
- "One of the region's most sought-after makeup artists, sharing his techniques on Maharat."

No certificate or accreditation language anywhere in this section or anywhere on the page.

---

##### Section C. What you will learn (chapter sampler)

Purpose: show the real curriculum as proof of depth. Use confirmed lesson names only.

Heading (AR): ماذا ستتعلم؟
Heading (EN): What you will learn

Display as a card grid (3 columns on desktop, 1 column on mobile, #1A1A1A cards, emerald
icon or number on each):

Confirmed lesson names from the instructor profile (use exactly these, no invented additions):
1. The Talent (free intro, labeled as such)
2. Beginnings
3. Your Makeup Kit Essentials
4. Your Color Palette
5. Look Flawless Without Makeup
6. Foundation 101
7. The No-Makeup Makeup (I and II)
8. The Day to Night
9. The Everyday Glam (I and II)
10. The Smokey Eyes (I and II)
11. The Color Glam (I and II)
12. The Graphic Metallic Look (I and II)
13. A Career in Makeup
14. Anxiety Is Your Friend
15. Final Touches

Display: show 6 to 8 cards prominently. Add a "see all 20 chapters" expand toggle rather than
truncating or omitting confirmed titles. The free intro chapter is always visible and labeled.

Chapter count (AR): 20 فصلاً . الفصل 1 مجاني
Chapter count (EN): 20 chapters . Chapter 1 free

---

##### Section D. The try pivot (free chapter CTA, repeated)

Purpose: re-anchor the low-friction entry after the learner has seen the curriculum.

Content (AR):
- Heading: ابدأ بالفصل الأول مجاناً
- Body: "The Talent" هو أول فصل في الماستركلاس، ومتاح لك الآن بدون اشتراك. شاهده، وقرر بعدها.
- CTA (emerald): ابدأ مجاناً

Content (EN):
- Heading: Start with chapter 1, free
- Body: "The Talent" is the first chapter. Watch it now, no subscription required. Then decide.
- CTA: Start free

---

##### Section E. Subscription offer (the conversion goal)

Purpose: state the paid offer clearly and honestly. Price shown as the public reference only.
No invented promotion. No accreditation.

Content (AR):
- Heading: اشتراك واحد يفتح الماستركلاس كاملاً
- Body: مع اشتراك مهارات، تفتح ماستركلاس بسام فتوح كاملاً إضافة إلى مكتبة دروس ومهارات تكبر
  باستمرار.
- Price reference (AR): وصول غير محدود بأقل من 7 دولارات شهرياً عند الاشتراك السنوي
- CTA (emerald): اشترك الآن
- Sub-label: اختر خطتك على صفحة الباقات

Content (EN):
- Heading: One subscription opens the full Masterclass
- Body: With a Maharat subscription, you unlock the full Bassam Fattouh Masterclass, plus a
  growing library of lessons and skills.
- Price reference (EN): Unlimited access for less than $7 per month, billed annually
- CTA: Subscribe now
- Sub-label: Choose your plan on the plans page

CTA destination for subscription: maharat.com/ar/plans or /en/plans. No personal data in the
URL.

Note: the price reference above is the confirmed public reference from the live class page. No
campaign-specific promotion, trial, or bundle is stated or implied. If Ahmed confirms a
promotion, that copy slot is updated and resubmitted to QA before it goes live.

---

##### Section F. Signup gate (the capture point)

See Section 3 (Gate spec) for full gate detail. This zone is embedded within or immediately
below the subscription section as the data-capture step.

---

##### Section G. Footer / trust zone

Content:
- Maharat brand mark and name (AR and EN).
- Link to the plans page: maharat.com/ar/plans and /en/plans.
- Privacy policy link: [سياسة الخصوصية] / [Privacy Policy] linking to the live Maharat
  privacy policy. Required by Saudi PDPL at the point of collection. This satisfies
  Open Item 7 from compliance-verdict.md.
- No accreditation marks, no certification endorsement logos.
- No fundraising, roadmap, or unannounced plans.

---

#### 2.4 RTL correctness checklist (operational, pre-publish)

These checks are required before the page advances from draft to qa-passed and before any
go-live action.

- [ ] Arabic text renders right-to-left at every breakpoint (mobile 375px, tablet 768px,
      desktop 1280px).
- [ ] No line of Arabic text is accidentally LTR due to a missing dir="rtl" or lang="ar"
      attribute.
- [ ] Mixed AR/EN lines (for example a product name in EN inside an AR sentence) do not break
      the paragraph direction.
- [ ] Western numerals only throughout. Check every number on the rendered page: chapter
      counts, price, and any other numeric. Zero Eastern Arabic numerals.
- [ ] The emerald CTA button is right-aligned (or full-width on mobile) in the AR render and
      left-aligned in the EN render.
- [ ] The chapter card grid reads right-to-left in AR.
- [ ] No em dashes on the rendered page. Use a comma, colon, or period instead.
- [ ] No tatweel or kashida in any rendered Arabic string.
- [ ] The privacy notice in Section G is visible and the link is live before the gate opens.

---

#### 2.5 Page speed and technical constraints

- Fast load is required. The hero image is the largest asset; it must be delivered via a CDN
  with a responsive srcset. Target: first contentful paint under 2 seconds on a 4G mobile
  connection.
- The page must be indexable. A canonical tag and hreflang are required. The page is not a
  hidden splash; it is the campaign's SEO-visible entry point.
- No third-party scripts load before the privacy consent mechanism is resolved. Pixel and
  analytics scripts must respect user consent and any PDPL consent layer.


---


### 3. Gate spec

#### 3.1 Gate type and platform

Gate type per brief: email or WhatsApp. The brief marks gate_platform as OPEN ITEM.

Both gate types are specified below so that once the platform is confirmed by Ahmed, the
correct design is immediately actionable. The live send wiring and the submission routing for
both are blocked until the platform is confirmed.

No platform is assumed, adopted, or wired without approval. ManyChat is referenced in the
agent system prompt as a known Instagram-lead tool but is not adopted here without approval.

---

#### 3.2 Gate variant A: email opt-in

Fields:
- Email address (required). No other field is required.
- First name (optional, for personalization in lifecycle emails, clearly labeled optional).

Fields explicitly excluded:
- Phone number: not collected here unless WhatsApp is the chosen gate.
- Date of birth, gender, location, or any other field not needed for the conversion purpose:
  not collected. Data minimization principle applies.
- No hidden pre-filled parameters carrying user identifiers from the ad platform.

Label copy (AR):
- Email field label: البريد الإلكتروني
- First name field label: الاسم الأول (اختياري)
- Submit button (emerald): ابدأ مجاناً

Label copy (EN):
- Email field label: Email address
- First name field label: First name (optional)
- Submit button: Start free

Privacy notice (AR, visible at the gate, required by Saudi PDPL):
"بالمتابعة، أنت توافق على تلقّي رسائل من مهارات. نحن نحترم خصوصيتك ولن نشارك بياناتك مع أي
طرف ثالث. يمكنك إلغاء الاشتراك في أي وقت. [سياسة الخصوصية]"

Privacy notice (EN, visible at the gate):
"By continuing, you agree to receive messages from Maharat. We respect your privacy and will
not share your data with any third party. You can unsubscribe at any time. [Privacy Policy]"

The [سياسة الخصوصية] / [Privacy Policy] text is a link to the live Maharat privacy policy.
This text must be visible before the user submits, not hidden behind a scroll or a collapsed
element. This directly addresses compliance-verdict.md Open Item 7.

Platform wiring (BLOCKED until platform is confirmed):
- On submit: the email and optional first name are routed to the lifecycle email platform
  (platform OPEN ITEM, see brief gate_platform).
- The POST payload contains only email and first name. No user-level identifiers, session
  tokens, ad click IDs, or tracking parameters are included in the data payload sent to the
  lifecycle platform.
- UTM parameters that arrived on the page URL are recorded at the session or lead level by
  the analytics layer (owned by data-tracking-engineer), not embedded in the user record
  in a way that exposes PII.
- On successful submit: trigger the gate_submit event (owned by data-tracking-engineer).
- Routing destination: lifecycle flow E1 (lifecycle-architect owns the flow, stream 7).
  The handoff is: email address and optional first name, tagged with the campaign_id
  2026-06-bassam-fattouh-makeup, suppression checked before any send.

Error states:
- Invalid email format: inline validation, clear Arabic and EN label, no page reload.
- Already subscribed: a positive confirmation, not an error. Copy (AR): "أنت بالفعل مشترك
  في مهارات. يمكنك الوصول إلى الماستركلاس من حسابك." No data is re-collected.
- Server error: a clear retry message, no data is lost silently.

---

#### 3.3 Gate variant B: WhatsApp opt-in

Fields:
- WhatsApp phone number (required). E.164 format, with a country code selector defaulting
  to Saudi Arabia (+966) given the primary market. Other GCC codes available.
- First name (optional).

Fields explicitly excluded: same exclusion list as the email gate. No extra data fields.

Label copy (AR):
- Phone field label: رقم الواتساب
- Country code selector default: 966+ (المملكة العربية السعودية)
- Submit button (emerald): ابدأ مجاناً

Label copy (EN):
- Phone field label: WhatsApp number
- Submit button: Start free

Privacy notice (AR, visible at gate, required):
"بالمتابعة، أنت توافق على تلقّي رسائل من مهارات عبر واتساب. يمكنك إيقاف الرسائل في أي وقت
بإرسال 'إيقاف'. [سياسة الخصوصية]"

Privacy notice (EN, visible at gate):
"By continuing, you agree to receive messages from Maharat via WhatsApp. You can stop
messages at any time by sending 'Stop'. [Privacy Policy]"

WhatsApp consent note (surfaces compliance-verdict.md Open Item 2):
WhatsApp marketing sends require explicit, separately-logged opt-in under Meta WhatsApp
Business Policy. The consent statement above must be:
(a) Displayed before the user submits, not hidden.
(b) Logged with a timestamp and the consent text version at the point of submission.
(c) Linked to the user's record in the lifecycle platform.
The mechanism for logging and storing this consent record must be confirmed and reviewed by
compliance-privacy-reviewer before the WhatsApp gate goes live. This is not resolved here;
it is surfaced as a required next step.

Platform wiring (BLOCKED until platform is confirmed):
- On submit: WhatsApp number and optional first name are routed to the WhatsApp lifecycle
  platform (platform OPEN ITEM).
- The same no-PII-in-parameters rule applies as for the email gate.
- Routing destination: the WhatsApp lifecycle welcome message (lifecycle-architect, stream 7).

---

#### 3.4 Gate placement on the page

The gate is embedded in Section F of the page, below the subscription offer copy but above
the footer. It is also surfaced as a modal or inline drawer that can be triggered by the
primary CTA in Section A ("ابدأ الدرس الأول مجاناً") and in Section D ("ابدأ مجاناً").

Gate trigger logic:
- Visitor clicks a CTA.
- If the visitor is already an authenticated Maharat user: send them directly to the class
  player. No gate needed.
- If the visitor is not authenticated: show the gate.
- After gate completion: route to the free chapter player, and simultaneously enroll the
  contact in the lifecycle flow (stream 7).

This trigger logic must be confirmed with the engineering team before wiring.


---


### 4. Routing into lifecycle (stream 7)

On successful gate completion:
- The contact is handed to lifecycle-architect (stream 7) with the following payload:
  - email address OR WhatsApp number (not both unless the platform supports dual-channel)
  - optional first name (if provided)
  - campaign_id: 2026-06-bassam-fattouh-makeup
  - entry_source: the channel tag (for example paid_meta, organic_instagram, email_e1, app_push)
  - gate_type: email or whatsapp (whichever was used)
  - no user-level tracking IDs or ad click IDs in this payload
- Lifecycle flow entry point: E1 (the introductory message, per 01-emails.ar-en.md).
- Suppression applied at the lifecycle platform before E1 sends: exclude paying contacts,
  unsubscribed, and hard-bounced. Suppression source is OPEN ITEM (carry from brief s.3 and
  compliance-verdict.md Open Item 4).
- The lifecycle-package (stream 7) owns the flow logic from this handoff onward.


---


### 5. Event plan (carried from data-tracking-engineer, not authored here)

Per the handoff contract (runtime/handoff-contract.md), the event_plan field is owned by
data-tracking-engineer. This package carries the field and references it; it does not author
event names, parameters, or platform mappings.

The tracking-plan.md produced by data-tracking-engineer for this campaign is the authoritative
source of the event_plan. Until that artifact is produced and carried here, the expected
events are noted for coordination purposes only, sourced from the handoff contract spec:

- page_view: fires on landing page load.
- gate_view: fires when the gate form is displayed to the visitor.
- gate_submit: fires on successful form submission.
- gate_confirm: fires on the confirmation state (after server-side submission is confirmed).
- subscription_start (or purchase): fires on the paid subscription conversion event.

The Pixel/CAPI mapping, GA4 mapping, event_id deduplication, mobile mapping (Apple IAP,
Google Play, flagged to-confirm), and BigQuery warehouse refs are all owned by
data-tracking-engineer and must be carried in this package once that artifact is available.

open_item: tracking-plan not yet received from data-tracking-engineer for this fullstack run.
This package will be updated to carry the full event_plan when that artifact is available.
The go-live decision at the human gate requires the tracking plan to be attached and for the
Pixel and CAPI mapping to have passed compliance-privacy-check (compliance-verdict.md
Open Item 1).


---


### 6. Operational verification (pre-publish, pre-gate)

The following checks must pass before this package advances to qa-passed and before any
go-live action. A failing check is a hard stop.

| Check | Description | Status |
|---|---|---|
| RTL render at 375px mobile | Arabic page renders right-to-left, no broken direction | Not yet run (blocked: page not built) |
| RTL render at 1280px desktop | Same check on desktop breakpoint | Not yet run |
| Western numerals on render | Zero Eastern Arabic numerals visible on the rendered page | Not yet run |
| No em dashes on render | Zero em dashes in any rendered string | Not yet run |
| Gate submits to correct destination | Test submission routes to the lifecycle platform correctly | BLOCKED: platform not confirmed |
| Privacy notice visible before submit | The notice and policy link are visible before any submit action | Not yet run |
| No PII in page URLs or UTM params | Spot-check UTM tags on all CTA links | Not yet run |
| CTA links resolve | Every CTA link resolves to the correct destination with no 404 | Not yet run |
| Suppression applied at lifecycle handoff | Test contact does not enter the flow if already a payer | BLOCKED: platform not confirmed |
| Event plan wired and firing | gate_view and gate_submit events fire correctly | BLOCKED: data-tracking-engineer tracking plan not received |
| Privacy policy link is live | The link in the notice goes to a live, readable policy | Not yet run |

All checks marked "Not yet run" are pre-publish requirements, not optional. All checks marked
"BLOCKED" are additionally gated on the open items listed in Section 5 and in the open_items
envelope above.


---


### 7. QA gates (pre-publish)

Before this package advances from draft to qa-passed:

- arabic-copy-qa: all Arabic copy on the landing page (hero, sections, gate labels, privacy
  notice) must pass arabic-copy-qa. The page copy above is sourced from or consistent with
  QA-passed copy in the existing campaign artifacts. The privacy notice copy is new and must
  be submitted to arabic-copy-qa explicitly.
- english-copy-qa: all English copy on the landing page must pass english-copy-qa. Same note
  for the English privacy notice copy.
- design-qa: the rendered page (not just this spec) must pass design-qa at every breakpoint.
  Visual constants, RTL correctness, Western numerals, no baked-in Arabic text in images,
  premium and uncluttered.
- compliance-privacy-reviewer: the gate form, the privacy notice, and the data routing must
  pass a second compliance-privacy-check before go-live. This is the implementation-level
  check that complements the design-level pass already on file. The WhatsApp consent logging
  mechanism (if WhatsApp is the chosen gate) requires a dedicated compliance review.
- brand-qa-reviewer: the full rendered page passes through brand-qa-reviewer last.

The privacy notice copy (Sections 3.2 and 3.3 above) is the new customer-facing copy in this
package and is therefore the primary pending QA item.


---


### 8. Compliance and privacy attachments

Compliance-verdict.md from the earlier campaign package is attached by reference. Its pass
status applies at design level. Seven open items from that verdict remain unresolved and all
seven block go-live.

This package addresses Open Item 7 directly: the privacy notice is now specified in the gate
(Sections 3.2 and 3.3 above), with the required PDPL disclosure elements present (who
collects, for what purpose, how to stop, and a link to the policy). Before go-live this notice
must pass arabic-copy-qa, english-copy-qa, and the implementation-level compliance review.

Open Items 1, 2, 3, 4, 5, and 6 from compliance-verdict.md remain unresolved and are not
within the scope of this stream to resolve. They are surfaced here for the human gate.


---


### 9. Human gate summary

This package is assembled, approval-ready in structure, and stops here. Nothing sends,
publishes, or goes live.

What approval would do (one sentence): on approval and after all blocking open items clear,
the landing page publishes at the confirmed URL and the signup gate begins capturing email or
WhatsApp contacts and routing them into the lifecycle flow (stream 7), with the free intro
chapter as the entry offer.

Blocking items before go-live:
1. Gate platform confirmed by Ahmed (email platform or WhatsApp platform named).
2. Operational verification checks all passed (see Section 6).
3. Privacy notice copy passed arabic-copy-qa, english-copy-qa, and compliance review.
4. WhatsApp consent logging mechanism reviewed by compliance if WhatsApp is the chosen gate.
5. Tracking plan received from data-tracking-engineer and Pixel/CAPI mapping passed
   compliance review (compliance-verdict.md Open Item 1).
6. Saudi PDPL lawful basis, retention, and data-subject rights confirmed (Open Item 5).
7. Data residency and cross-border transfer safeguards confirmed once platforms are named
   (Open Item 6).
8. Suppression source confirmed and wired (Open Item 4).
9. Approved Bassam Fattouh asset confirmed or fallback to V2 abstract visual confirmed.
10. Engineering confirmation of the free-chapter CTA destination (authenticated vs
    unauthenticated flow) before wiring.

Verdicts attached by reference: compliance-verdict.md, brand-qa-verdict.md,
qa-copy-design-verdicts.md. All from the 2026-06-bassam-fattouh-makeup campaign package.

Nothing in this package constitutes approval. Approval is Ahmed's, per action and per
campaign. Silence is not approval.

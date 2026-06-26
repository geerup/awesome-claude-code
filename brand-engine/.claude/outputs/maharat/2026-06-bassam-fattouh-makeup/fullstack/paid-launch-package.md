# Paid Launch Package: Bassam Fattouh Teaches Makeup

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: paid-build-engineer
- stream: 5 build and launch
- status: gated-pending
- qa:
  - skill_eval: carried from upstream (creative-package draft, copy-package.ar draft,
    copy-package.en draft, media-plan-package draft, tracking-plan draft; all upstream
    packages are at status draft pending their own skill eval and QA gates; this build
    structure is staged paused and may not go live until all upstream QA gates are cleared)
  - arabic_qa: carried from copy-package.ar (status draft, arabic-copy-qa pending)
  - brand_qa: carried from creative-package and copy-package.en (brand-qa-reviewer pending)
  - in_platform_copy_qa: Western numerals confirmed throughout, no em dashes, no tatweel
    in all copy variants mapped below
- open_items: see section 9. Seven open items block go-live. None are buried. Tracking not
  fully confirmed (gate_platform unconfirmed, CAPI wiring blocked). Budget not confirmed
  (OPEN ITEM: all ad-set budget fields are left blank and must be filled by Ahmed). Target
  CPA not confirmed (OPEN ITEM). Schedule assumed (confirm). Rights-cleared Bassam Fattouh
  assets not confirmed (C1 and C4 blocked at build). YouTube trailer asset unconfirmed.
  Gate platform unconfirmed.
- brief_refs:
  - budget: OPEN ITEM. No budget confirmed. All spend fields are blank. Human gate fills them.
  - target_CPA: OPEN ITEM. No cost-per-subscription target confirmed.
  - bid_strategy: phase 1 maximize conversions (Meta), maximize video views (TikTok),
    maximize clicks (Google), CPV (YouTube); phase 2 cost-cap and Target CPA once events
    accumulate and targets are confirmed by Ahmed. Details in media-plan-package section 4.
  - schedule: ASSUMPTION 2026-06-08 to 2026-06-28. Confirm with Ahmed.
  - geo: GCC, Saudi Arabia primary.
  - offer: Maharat subscription, hook is Masterclass "Bassam Fattouh Teaches Makeup."
    Free intro chapter 1 "The Talent" confirmed. No promotional offer or discount stated.

---

## Pre-flight validation

Inbound envelopes reviewed:

- creative-package: campaign_id matches (2026-06-bassam-fattouh-makeup). Status draft.
  Concepts C1 through C4 and asset briefs AB1 through AB5 extracted. C1 (AB1) and C4 (AB4)
  are blocked pending rights-cleared Bassam Fattouh assets. C2 and C3 are buildable.
- copy-package.ar: campaign_id matches. Status draft. Variants AD-PRIMARY-A1 through A4,
  AD-HEADLINE-A1 through A4, AD-CTA-A1 through A4 extracted. Gate-landing CTAs flagged.
- copy-package.en: campaign_id matches. Status draft. Variants EN-AD-A through EN-AD-E and
  all downstream variants extracted. No em dashes, Western numerals confirmed.
- media-plan-package: campaign_id matches. Budget OPEN ITEM confirmed. Target CPA OPEN ITEM
  confirmed. Proportional allocations, bid strategy phases, audience strategy, and UTM
  direction extracted.
- tracking-plan: campaign_id matches. Status draft, compliance-privacy-reviewer gate pending.
  Event plan for Meta Pixel, CAPI, GA4, and dedup approach extracted. Gate-side CAPI wiring
  blocked (gate_platform OPEN ITEM).

Note on upstream status: all upstream packages are at status draft. Per the I/O contract this
package is assembled as a staged paused structure. No build action or go-live is possible until
all upstream QA gates (skill eval, arabic-copy-qa, brand-qa-reviewer, compliance-privacy-check)
clear and status advances to at least qa-passed. This is flagged at the human gate.

---

## 1. Campaign structure: Meta and Instagram (primary)

Platform: Meta Ads Manager
Objective: Conversions (subscription_start via Pixel Purchase event)
Status: ALL PAUSED. Nothing spends until Ahmed flips live.

### 1.1 Campaign: META-CAMP-01

- Campaign name: 2026-06-bassam-fattouh-makeup_meta_conversions
- Objective: Conversions
- Campaign budget: OPEN ITEM. Budget amount blank. Ahmed fills before go-live.
- Campaign budget type: Daily budget (recommended) or lifetime; Ahmed confirms.
- Bid strategy (phase 1, week 1): Lowest cost (maximize conversions). No cost cap set until
  50 gate events accumulate per ad set.
- Special ad category: None (education / subscription; confirm with compliance-privacy-reviewer
  if any housing, employment, credit, or social issue category applies in Saudi context).
- Status: PAUSED

---

#### Ad Set META-AS-01: New acquisition, interest cluster 1 (beauty and makeup core)

- Ad set name: 2026-06-bfm_meta_prospecting_beauty-core
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (gate confirm event, as defined in tracking-plan
  section 2). Switch to Purchase (subscription_start) once 50 gate events accumulate.
- Audience:
  - Interests: makeup artistry, beauty tutorials, cosmetics, skincare, beauty brands
  - Geo: Saudi Arabia (primary). GCC expansion (Bahrain, Kuwait, Qatar, UAE, Oman) as
    secondary after Saudi volume is validated.
  - Age: 18 to 35
  - Language: Arabic
  - Device: All (mobile-first given platform usage in geo)
- Placement: Advantage+ placements (Meta optimizes across Facebook Feed, Instagram Feed,
  Instagram Reels, Instagram Stories, Facebook Stories). Confirm with Ahmed if any placement
  exclusions are needed.
- Budget: OPEN ITEM. Blank. Proportional guide from media-plan: META-CAMP-01 carries 50
  percent of total budget. Ad set share is set by paid-build-engineer once total budget is
  confirmed.
- Schedule: 2026-06-08 (ASSUMPTION) to 2026-06-28 (ASSUMPTION). End date required. Confirm.
- Frequency cap: 3 impressions per person per day across all Meta placements.
- Status: PAUSED

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-01-AD-01 | C1 hero portrait (blocked pending asset) | AB1 | AD-PRIMARY-A1, AD-HEADLINE-A1 | EN-AD-A | Sign Up |
| META-AS-01-AD-02 | C2 abstract brushstroke (buildable) | AB2 still or motion | AD-PRIMARY-A2, AD-HEADLINE-A2 | EN-AD-B | Learn More |

Note on META-AS-01-AD-01: this ad is staged but blocked for delivery until AB1
(rights-cleared Bassam Fattouh portrait) is confirmed. It is paused within a paused ad set.
META-AS-01-AD-02 (C2) is the launchable variant for this ad set if the asset is not confirmed
by the flight start date.

---

#### Ad Set META-AS-02: New acquisition, interest cluster 2 (self-presentation and occasions)

- Ad set name: 2026-06-bfm_meta_prospecting_occasions
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Switch to Purchase in phase 2.
- Audience:
  - Interests: weddings, events, special-occasion looks, fashion, personal styling
  - Geo: Saudi Arabia primary, GCC secondary
  - Age: 18 to 35
  - Language: Arabic
- Placement: Advantage+ placements
- Budget: OPEN ITEM. Blank. Proportional split from media-plan.
- Schedule: 2026-06-08 to 2026-06-28 (ASSUMPTION)
- Frequency cap: 3 impressions per person per day
- Status: PAUSED

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-02-AD-01 | C2 abstract brushstroke | AB2 still | AD-PRIMARY-A2, AD-HEADLINE-A2 | EN-AD-B | Learn More |
| META-AS-02-AD-02 | C3 curriculum cards carousel | AB3 carousel | AD-PRIMARY-A1, AD-HEADLINE-A1 | EN-AD-A | Sign Up |

---

#### Ad Set META-AS-03: New acquisition, subscription value (lower-funnel prospecting)

- Ad set name: 2026-06-bfm_meta_prospecting_sub-value
- Campaign: META-CAMP-01
- Optimization event: Purchase (subscription_start). This ad set runs conversion-objective
  copy (Concept C) and targets a lower-funnel intent signal.
- Audience:
  - Interest cluster: online learning, self-improvement, personal development
  - Geo: Saudi Arabia primary, GCC secondary
  - Age: 20 to 35
  - Language: Arabic
- Placement: Advantage+ placements
- Budget: OPEN ITEM. Blank.
- Schedule: 2026-06-08 to 2026-06-28 (ASSUMPTION)
- Frequency cap: 3 impressions per person per day
- Status: PAUSED

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-03-AD-01 | C3 curriculum cards still | AB3 multi-card still | AD-PRIMARY-A3, AD-HEADLINE-A3 | EN-AD-C | Subscribe |

Note: AD-PRIMARY-A3 contains the public price reference ("أقل من 7 دولارات شهرياً"). Confirm
with Ahmed that the price reference is cleared for this asset before the ad set goes live.

---

#### Ad Set META-AS-04: Retargeting, class page and plans page visitors

- Ad set name: 2026-06-bfm_meta_retargeting_page-visitors
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration then Purchase (per phase)
- Audience:
  - Custom audience: class page visitors (maharat.com class page URL, last 30 days) who did
    not complete the gate. Pixel required (Meta PageView event on class page URL).
  - Custom audience: plans page visitors (maharat.com/en/plans and /ar/plans, last 30 days)
    who did not subscribe.
  - Exclusion: current paying subscribers (suppressed via customer list upload after
    compliance-privacy-check on hashed email list; gate pending).
  - Geo: GCC (audience is pre-qualified; geo filter is a guardrail only)
  - Age: 18 to 45
- Placement: Advantage+ placements (Instagram Feed and Stories prioritized for retargeting)
- Budget: OPEN ITEM. Blank.
- Schedule: activate from 2026-06-10 onward (day 3, once pixel pools build). End 2026-06-28.
- Frequency cap: 3 impressions per person per day
- Status: PAUSED. Additional block: custom audience pixel pools must have accumulated before
  this ad set can deliver. Pixel firing on the class page is a prerequisite.
- Status note on tracking dependency: pixel firing on maharat.com class page is blocked
  pending tracking-plan compliance-privacy-check clearance and production deployment.

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-04-AD-01 | C3 curriculum carousel | AB3 carousel | AD-PRIMARY-A4, AD-HEADLINE-A4 | EN-AD-D | Sign Up |
| META-AS-04-AD-02 | C2 abstract brushstroke motion | AB2 motion | AD-PRIMARY-A4, AD-HEADLINE-A4 | EN-AD-D | Sign Up |

Note: AD-PRIMARY-A4 and EN-AD-D are the gate-retargeting variants. The CTA lands on the
signup gate. Gate platform is OPEN ITEM; this ad set go-live is blocked until gate platform
is confirmed.

---

#### Ad Set META-AS-05: Retargeting, video viewers (75 percent threshold)

- Ad set name: 2026-06-bfm_meta_retargeting_video-viewers-75pct
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration then Purchase
- Audience:
  - Video engagement custom audience: users who watched 75 percent or more of any Meta video
    ad from this campaign.
  - Exclusion: current subscribers, gate completers who have already subscribed.
  - Geo: GCC guardrail
  - Age: 18 to 45
- Placement: Advantage+ placements
- Budget: OPEN ITEM. Blank.
- Schedule: activate from 2026-06-11 onward (day 4, once video view pools build).
  End 2026-06-28.
- Frequency cap: 3 impressions per person per day
- Status: PAUSED. Depends on video creative delivery to build the pool.

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-05-AD-01 | C3 curriculum carousel | AB3 carousel | AD-PRIMARY-A4, AD-HEADLINE-A4 | EN-AD-D | Sign Up |

---

## 2. Campaign structure: TikTok (secondary)

Platform: TikTok Ads Manager
Objective: Phase 1 video views; Phase 2 conversions (if pixel volume supports)
Status: ALL PAUSED.

### 2.1 Campaign: TIKTOK-CAMP-01

- Campaign name: 2026-06-bassam-fattouh-makeup_tiktok_reach-video
- Objective: Video Views (phase 1). Switch to Conversions in phase 2 if TikTok Pixel has
  sufficient events and the gate platform is confirmed.
- Campaign budget: OPEN ITEM. Blank. Proportional guide: TikTok carries 20 percent of total
  budget.
- Bid strategy (phase 1): Maximize video views, CPV bidding.
- Status: PAUSED

---

#### Ad Set TIKTOK-AS-01: Prospecting, beauty and makeup interest

- Ad set name: 2026-06-bfm_tiktok_prospecting_beauty
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views
- Audience:
  - Interests: beauty, makeup, GRWM content, skincare, cosmetics
  - Geo: Saudi Arabia primary, GCC secondary
  - Age: 18 to 30 (TikTok-specific age band per media-plan)
  - Language: Arabic
- Placement: TikTok In-Feed
- Budget: OPEN ITEM. Blank.
- Schedule: 2026-06-08 to 2026-06-21 (weeks 1 and 2 only; pause cold prospecting in week 3
  unless week 2 data supports continuation)
- Status: PAUSED

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| TIKTOK-AS-01-AD-01 | C2 abstract brushstroke motion (vertical 9:16) | AB2 motion 1080x1920 | AD-PRIMARY-A2, AD-HEADLINE-A2 | EN-AD-B | Learn More |
| TIKTOK-AS-01-AD-02 | C4 class trailer short cut 15s (blocked pending footage) | AB4 15s cut | AD-PRIMARY-A1, AD-HEADLINE-A1 | EN-AD-A | Sign Up |

Note on TIKTOK-AS-01-AD-02: blocked pending rights-cleared class footage (OPEN ITEM).
TIKTOK-AS-01-AD-01 (C2, AB2) is the launchable fallback.

---

#### Ad Set TIKTOK-AS-02: Retargeting, video engagers (50 percent threshold)

- Ad set name: 2026-06-bfm_tiktok_retargeting_video-engagers
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views (phase 1), Conversions (phase 2 if pixel supports)
- Audience:
  - Custom audience: TikTok users who watched 50 percent or more of a TikTok ad or organic
    post from this campaign.
  - Exclusion: current subscribers (hashed email list upload pending compliance-privacy-check
    and gate_platform confirmation).
  - Geo: GCC guardrail
  - Age: 18 to 35
- Placement: TikTok In-Feed
- Budget: OPEN ITEM. Blank.
- Schedule: activate from 2026-06-11 onward (day 4). End 2026-06-28. In week 3 this is the
  only active TikTok ad set.
- Status: PAUSED. Depends on video delivery in week 1 to build the pool (minimum 1,000 users).
  If pool is below 1,000 at end of week 1, ad set remains paused; trigger 3 from media-plan
  applies.

Ads in this ad set:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| TIKTOK-AS-02-AD-01 | C2 abstract brushstroke motion (short, 9:16, under 15s) | AB2 motion 1080x1920 | AD-PRIMARY-A4, AD-HEADLINE-A4 | EN-AD-D | Sign Up |

Note: CTA lands on the signup gate. Blocked until gate_platform is confirmed.

---

## 3. Campaign structure: Google Search (secondary)

Platform: Google Ads
Objective: Clicks (phase 1), Target CPA (phase 2 if 30-plus conversions)
Status: ALL PAUSED.

### 3.1 Campaign: GOOGLE-CAMP-01

- Campaign name: 2026-06-bassam-fattouh-makeup_google_search
- Campaign type: Search
- Objective: Conversions (subscription_start, wired via Google Ads conversion tag or imported
  from GA4 goal)
- Budget: OPEN ITEM. Blank. Proportional guide: Google Search carries 15 percent of total budget.
- Bid strategy: Maximize clicks (phase 1). Switch to Target CPA (phase 2) once 30 conversion
  events are recorded within 30 days. Target CPA value is OPEN ITEM; Ahmed confirms before the
  switch.
- Networks: Search only. Exclude Display Network and Search Partners initially.
- Geo: Saudi Arabia (primary). GCC expansion after Saudi data validates.
- Language: Arabic (primary), English (secondary, for EN intent keywords)
- Status: PAUSED

---

#### Ad Group GOOGLE-AG-01: Brand keywords

- Ad group name: 2026-06-bfm_google_brand
- Keywords (phrase and exact match):
  - [Bassam Fattouh] (exact)
  - "Bassam Fattouh Maharat" (phrase)
  - [بسام فتوح] (exact, AR)
  - "بسام فتوح مهارات" (phrase, AR)
- Match types: exact and phrase only for brand. No broad match on brand terms.
- Bid priority: highest. Set bid adjustments to prioritize brand queries.
- Status: PAUSED

Ads in this ad group:

| Ad name | Format | AR copy variant | EN copy variant |
|---|---|---|---|
| GOOGLE-AG-01-AD-01 | Responsive Search Ad | AD-HEADLINE-A1 (headline pin 1), AD-CTA-A1 | EN-AD-A headline pins, EN-AD-E headlines |

Responsive Search Ad structure for GOOGLE-AG-01-AD-01:
- Headline 1 (pinned): Bassam Fattouh Teaches Makeup (EN) / بسام فتوح يعلّمك المكياج (AR)
- Headline 2: 20-Chapter Masterclass on Maharat (EN) / 20 درساً من الأساس إلى الإطلالات (AR)
- Headline 3: Start the First Lesson Free (EN) / ابدأ الدرس التمهيدي المجاني (AR)
- Description 1 (EN-AD-E): Step-by-step video lessons from one of the region's most
  sought-after makeup artists. Foundation to statement looks.
- Description 2 (EN-AD-E): One subscription opens the full Maharat library. The first
  chapter is free. Sign up today.
- Final URL: maharat.com class page for Bassam Fattouh Teaches Makeup (no user data in URL)
- UTM parameters on final URL:
  utm_source=google, utm_medium=paid_search,
  utm_campaign=2026-06-bassam-fattouh-makeup, utm_content=conceptA, utm_term={keyword}

---

#### Ad Group GOOGLE-AG-02: Class-specific keywords

- Ad group name: 2026-06-bfm_google_class-specific
- Keywords:
  - "learn makeup online" (phrase)
  - "makeup course Arabic" (phrase)
  - [تعلم المكياج] (exact, AR)
  - "دورة مكياج" (phrase, AR)
  - "makeup masterclass online" (phrase)
- Status: PAUSED

Ads in this ad group:

| Ad name | Format | AR copy variant | EN copy variant |
|---|---|---|---|
| GOOGLE-AG-02-AD-01 | Responsive Search Ad | AD-PRIMARY-A1 body, AD-HEADLINE-A1 | EN-AD-E |

Responsive Search Ad structure for GOOGLE-AG-02-AD-01:
- Headline 1: Learn Makeup from Bassam Fattouh (EN-AD-E headline 1)
- Headline 2: 20-Chapter Masterclass on Maharat (EN-AD-E headline 2)
- Headline 3: Start the First Lesson Free (EN-AD-E headline 3)
- Description 1 (EN-AD-E): Step-by-step video lessons from one of the region's most
  sought-after makeup artists. Foundation to statement looks.
- Description 2 (EN-AD-E): One subscription opens the full Maharat library. The first
  chapter is free. Sign up today.
- Final URL: maharat.com class page (no user data in URL)
- UTM parameters: utm_source=google, utm_medium=paid_search,
  utm_campaign=2026-06-bassam-fattouh-makeup, utm_content=conceptA, utm_term={keyword}

---

#### Ad Group GOOGLE-AG-03: Category keywords (monitored, observation)

- Ad group name: 2026-06-bfm_google_category-observe
- Keywords (phrase match, observation layer first):
  - "makeup tutorial" (phrase)
  - "makeup artist course" (phrase)
  - "online beauty course" (phrase)
  - "مدرسة مكياج" (phrase, AR)
  - "فن المكياج" (phrase, AR)
- Note: monitor CPCs and conversion rates. Promote to active bidding if they convert.
  Add negative keywords aggressively (products, brushes, cosmetics retail, hire).
- Status: PAUSED

Ads in this ad group:

| Ad name | Format | AR copy variant | EN copy variant |
|---|---|---|---|
| GOOGLE-AG-03-AD-01 | Responsive Search Ad | AD-HEADLINE-A2, AD-PRIMARY-A2 | EN-AD-B |

Negative keyword list (to build in Google Ads before launch):
- buy makeup, makeup products, makeup brushes, makeup brush set, cosmetics store, online
  shopping makeup, makeup artist for hire, makeup artist services, makeup artist near me,
  free makeup samples, cosmetics sale, makeup sale, buy lipstick, foundation buy, mascara buy

---

## 4. Campaign structure: YouTube (secondary, conditional)

Platform: Google Ads (YouTube campaign type)
Objective: Awareness, video views (CPV bidding)
Status: ALL PAUSED. Additional conditional block: YouTube allocation is blocked until
rights-cleared trailer asset (AB4 15-second or 30-second cut) is confirmed. If asset is
not confirmed by 2026-06-08, this campaign stays paused and the 10 percent YouTube budget
share rolls into reserve (media-plan trigger 7). This is a human-gate decision.

### 4.1 Campaign: YOUTUBE-CAMP-01

- Campaign name: 2026-06-bassam-fattouh-makeup_youtube_video-awareness
- Campaign type: Video (In-Stream, non-skippable or skippable; 15s cut for pre-roll)
- Objective: Awareness and reach
- Budget: OPEN ITEM. Blank. Proportional guide: YouTube carries 10 percent of total budget.
  Conditional: if trailer asset is not confirmed by launch, this amount moves to reserve.
- Bid strategy: Target CPV (cost per view)
- Status: PAUSED. ASSET BLOCK: AB4 (C4 class trailer, rights-cleared footage) must be
  confirmed before this campaign can be built or activated.

---

#### Ad Group YOUTUBE-AG-01: Beauty and self-development audience, in-stream

- Ad group name: 2026-06-bfm_youtube_instream_beauty-selfdevelopment
- Campaign: YOUTUBE-CAMP-01
- Audience targeting:
  - In-market: online education, self-development
  - Interest: beauty, makeup tutorials, lifestyle
  - Keyword targeting: YouTube channels and videos in the Arabic beauty tutorial space
  - Customer match / remarketing: users who visited the Maharat class page or YouTube
    channel. Requires YouTube remarketing tag confirmed by data-tracking-engineer
    (tracking-plan section, YouTube tag placement is an open item).
- Geo: Saudi Arabia primary, GCC
- Language: Arabic
- Status: PAUSED. Asset block applies.

Ads in this ad group:

| Ad name | Creative concept | Creative asset | AR copy variant | EN copy variant |
|---|---|---|---|---|
| YOUTUBE-AG-01-AD-01 | C4 class trailer 15s cut (BLOCKED) | AB4 15s cut, 1920x1080 | AD-HEADLINE-A1, AD-CTA-A1 | EN-AD-A headline, CTA |

Note: overlay copy on the end card uses AD-HEADLINE-A1 / EN-AD-A headline. The full primary
text body copy (AD-PRIMARY-A1 / EN-AD-A primary text) does not appear in the in-stream ad
format; it populates the companion banner and the video description only.

UTM on final URL for companion click:
utm_source=youtube, utm_medium=paid_video,
utm_campaign=2026-06-bassam-fattouh-makeup, utm_content=conceptA

---

## 5. Tracking wiring applied to staged structure

Source: tracking-plan.md (data-tracking-engineer, campaign_id 2026-06-bassam-fattouh-makeup).
Tracking is wired below to each channel's ad structure. Production deployment of any tracking
code is a human-gate action and has not occurred. This section describes the plan only.

### 5.1 Meta Pixel and CAPI

Events wired to Meta campaigns:
- PageView fires on the Masterclass class page load. Linked to all Meta campaigns as the
  first-touch signal.
- ViewContent (gate_view) fires when the signup gate renders. Linked to ad sets META-AS-01
  through META-AS-05 as a mid-funnel signal.
- Lead (submit) fires on gate form submit. Optimization event for phase 1 ad sets META-AS-01
  and META-AS-02.
- CompleteRegistration (confirm) fires on server confirmation of gate submission. This is the
  primary optimization event for META-AS-01 through META-AS-04 in phase 1. CAPI preferred.
- Purchase (subscription_start) fires on subscription purchase confirmation. Primary conversion
  event for META-CAMP-01 phase 2 and META-AS-03 throughout.

Deduplication: event_id (UUID v4, server-generated) applied to CompleteRegistration and
Purchase on both Pixel and CAPI calls, as specified in tracking-plan section 3. Any mismatch
is a hard stop before go-live.

Tracking block note: gate-side CAPI wiring (Lead, CompleteRegistration) is blocked until
gate_platform is confirmed and Saudi PDPL data-residency decision is made. Web-side Pixel
fires for PageView and ViewContent are unblocked at the class page level but require
compliance-privacy-check clearance and production deployment before anything fires live.

### 5.2 TikTok Pixel

Events linked to TikTok campaigns:
- ViewContent on class page (equivalent to PageView for TikTok feed attribution).
- CompletePayment (TikTok equivalent of Purchase) on subscription_start for phase 2.
- TikTok pixel placement on maharat.com class page: planned, not yet deployed. Blocked on
  compliance-privacy-check and production write gate.

### 5.3 Google Ads conversion tracking

Conversion action: subscription_start, imported from GA4 goal (purchase event, campaign_id
parameter match) or via Google Ads conversion tag on the order confirmation page.
Target: subscription conversions. CPA target is OPEN ITEM; Google Target CPA bid strategy
cannot be activated until Ahmed confirms the target and 30-plus conversions are on record.

### 5.4 GA4 mapping (all channels)

All paid landing pages carry UTM parameters as specified in tracking-plan section 4 and
media-plan section 7. UTM values:

| Channel | utm_source | utm_medium | utm_campaign | utm_content | utm_term |
|---|---|---|---|---|---|
| Meta and Instagram | meta | paid_social | 2026-06-bassam-fattouh-makeup | conceptA / conceptB / conceptC / conceptD | (none) |
| TikTok | tiktok | paid_social | 2026-06-bassam-fattouh-makeup | conceptB / conceptD | (none) |
| Google Search | google | paid_search | 2026-06-bassam-fattouh-makeup | conceptA | {keyword} |
| YouTube | youtube | paid_video | 2026-06-bassam-fattouh-makeup | conceptA | (none) |

No personal data in any UTM field. No user identifier, email, phone, or personal attribute
in any URL parameter. This is a hard rule from CLAUDE.md and the tracking-plan.

### 5.5 Audience suppression

Exclusion audience: current paying subscribers. Source: hashed email list from Maharat
subscriber database. Upload is blocked pending compliance-privacy-check (consent basis for
list upload must be confirmed per Saudi PDPL and Meta/TikTok policies). This is a go-live
prerequisite for all retargeting ad sets.

---

## 6. UTM and naming convention summary

All campaign and ad set names follow the convention:
{campaign_id}_{platform}_{objective}_{audience-descriptor}

Examples from the structure above:
- 2026-06-bfm_meta_prospecting_beauty-core
- 2026-06-bfm_meta_retargeting_page-visitors
- 2026-06-bfm_tiktok_prospecting_beauty
- 2026-06-bfm_google_brand
- 2026-06-bfm_youtube_instream_beauty-selfdevelopment

UTM content values map to creative concepts:
- conceptA: C1 hero portrait (Concept A copy, AD-PRIMARY-A1 / EN-AD-A)
- conceptB: C2 abstract brushstroke (Concept B copy, AD-PRIMARY-A2 / EN-AD-B)
- conceptC: C3 curriculum cards / subscription value (Concept C copy, AD-PRIMARY-A3 / EN-AD-C)
- conceptD: C4 retargeting (Concept D copy, AD-PRIMARY-A4 / EN-AD-D)

No em dashes in any ad name, UTM value, or naming convention field.

---

## 7. Budget allocation structure (proportional only; absolute amounts OPEN ITEM)

These proportions are from media-plan-package section 2. No absolute amounts are stated here
because the total budget is OPEN ITEM. Paid-build-engineer applies absolute amounts only after
Ahmed confirms the budget. The table below is the allocation plan Ahmed will use to fill in
figures at the human gate.

| Channel | Campaign | Overall share | Phase 1 (week 1) | Phase 2 (weeks 2 to 3) |
|---|---|---|---|---|
| Meta and Instagram | META-CAMP-01 | 50 percent | Prospecting-heavy | Retargeting shift, best creative scaled |
| TikTok | TIKTOK-CAMP-01 | 20 percent | Reach and video seeding | Retargeting only (week 3) |
| Google Search | GOOGLE-CAMP-01 | 15 percent | Steady (maximize clicks) | Steady or slight increase |
| YouTube | YOUTUBE-CAMP-01 | 10 percent | Conditional on trailer asset | Conditional, held in reserve if asset unconfirmed |
| Reserve | N/A (held by Ahmed) | 5 percent | Held | Released to best performer after week 1 readout (human-gate decision) |
| TOTAL | | 100 percent | | |

Note on YouTube: if the trailer asset (AB4) is not confirmed by 2026-06-08, the 10 percent
YouTube share moves to reserve. Reserve becomes 15 percent. Human gate decides whether to
wait for the asset or fold the YouTube share into Meta (media-plan trigger 7).

Reserve release: the 5 percent reserve is released only after the week 1 performance readout
from analytics-reporter. The release is a human-gate proposal, not an autonomous action.
Analytics-reporter proposes the destination channel; Ahmed approves. Paid-build-engineer then
adjusts the receiving campaign budget.

---

## 8. Pre-launch checklist

Each item is checked against the inputs in this package. A failing item blocks go-live.

| Check | Status | Notes |
|---|---|---|
| Pixel firing confirmed on class page | BLOCKED | tracking-plan is draft; compliance-privacy-check pending; production pixel deployment is a human-gate action. Block is a go-live blocker. |
| CAPI endpoint wired for gate events | BLOCKED | gate_platform OPEN ITEM; Saudi PDPL data-residency decision pending. Hard go-live blocker. |
| UTMs consistent across all ad URLs | PASS (plan) | UTM structure mapped in section 5.4 and section 6. Values are non-identifying, consistent with tracking-plan section 4. Confirm at build time that every final URL carries the correct UTMs. |
| Naming convention applied throughout | PASS (plan) | All campaign, ad set, and ad names follow the convention in section 6. No em dashes in names. |
| Budget cap set from brief | BLOCKED | Budget is OPEN ITEM. No absolute budget figure is staged. Ahmed fills all budget fields before go-live. This is a hard blocker. |
| End date set on all campaigns | BLOCKED | Schedule is ASSUMPTION (2026-06-28). Ahmed confirms. Until confirmed, no end date is set in the platform. Hard blocker. |
| Start date set on all campaigns | BLOCKED | Schedule is ASSUMPTION (2026-06-08). Ahmed confirms. Hard blocker. |
| All campaigns and ad sets staged as PAUSED | PASS | Every campaign, ad set, and ad in this package is marked PAUSED. Nothing activates without Ahmed's explicit go-live action. |
| No personal data in any UTM parameter or tracking call | PASS (plan) | Confirmed: no email, phone, name, or user ID in any UTM field or event parameter. tracking-plan section 5 and CLAUDE.md guardrail both satisfied. |
| Rights-cleared Bassam Fattouh assets confirmed | BLOCKED | C1 (AB1) and C4 (AB4) are blocked. Fallback to C2 (AB2) and C3 (AB3) for launch. If no cleared asset by flight start, C1 and C4 ad variants are paused within paused ad sets. Not a full go-live blocker (C2 and C3 can launch), but a blocker for specific ad variants. |
| YouTube trailer asset confirmed | BLOCKED | AB4 (class footage) not confirmed. YOUTUBE-CAMP-01 is conditionally blocked. Budget shifts to reserve. Human-gate decision required. |
| Gate platform confirmed | BLOCKED | Email / WhatsApp capture platform is OPEN ITEM. All gate-landing CTAs are blocked. Ad sets META-AS-04, META-AS-05, TIKTOK-AS-02, and all retargeting ads with gate CTA cannot go live until gate platform is confirmed. |
| Compliance-privacy-check cleared for retargeting audiences | BLOCKED | Consent basis for hashed subscriber list upload, retargeting pixels, and CAPI hashed signals not yet confirmed by compliance-privacy-reviewer. Retargeting ad sets (META-AS-04, META-AS-05, TIKTOK-AS-02) blocked until cleared. |
| Exclusion audience (current subscribers) uploaded | BLOCKED | Depends on hashed list upload, which depends on compliance-privacy-check. Acquisition ad sets should not serve to existing subscribers. |
| Upstream QA gates passed (creative, copy AR, copy EN, tracking) | BLOCKED | All upstream packages are at status draft. No package has cleared skill eval, arabic-copy-qa, english-copy-qa, or brand-qa-reviewer yet. This is a comprehensive go-live blocker for all channels. |
| No accreditation claim in any ad copy | PASS | Reviewed all copy variants: AD-PRIMARY-A1 through A4 (AR) and EN-AD-A through EN-AD-E (EN). No certificate, accreditation, or qualification claim present. |
| No em dash in any in-platform copy | PASS | Reviewed: no em dash in any copy variant staged in this package. |
| Western numerals in all in-platform copy | PASS | Confirmed: "7" (price reference in AD-PRIMARY-A3 and EN-AD-C) and "20" (chapter count) are Western numerals. |
| No invented promo, trial, or discount | PASS | No promotional offer staged in any ad variant. Price reference (under $7/month, أقل من 7 دولارات) is the confirmed public reference only, used only in Concept C variants. |
| Instructor public naming cleared | PASS | Bassam Fattouh is named. Clearing confirmed in copy-package.ar brief_refs (public naming cleared, course page and Ahmed sign-off 2026-06-05). |
| Target CPA staged in bid settings | BLOCKED | Target CPA is OPEN ITEM. No cost-cap or Target CPA bid values are staged. Meta ad sets run maximize conversions in phase 1. The cost-cap field is left blank pending Ahmed's confirmation. |

Summary: 5 items pass (plan-level), 12 items are blocked. The 12 blocks must each be resolved
before the corresponding ad sets or campaigns can go live. The most critical blockers are:
total budget (blocks all spend), upstream QA gates (blocks all copy and creative), pixel and
compliance clearance (blocks all tracking), and gate platform (blocks all retargeting and
gate-CTA ads).

---

## 9. Open items (all surfaced, none buried)

The following items are unresolved and carried to the human gate. Each one is a discrete
decision for Ahmed. Silence is not approval.

| # | Item | Blocks | Owner |
|---|---|---|---|
| 1 | Total budget: OPEN ITEM. No budget confirmed. All ad-set budget fields are blank. | All spend across all channels. | Ahmed (brief) |
| 2 | Target CPA: OPEN ITEM. No cost-per-subscription target confirmed. Cost-cap and Target CPA bid settings cannot be staged. | Phase 2 bid strategy on Meta and Google. | Ahmed (brief) |
| 3 | Schedule (start and end dates): ASSUMPTION. 2026-06-08 to 2026-06-28. Confirm. | Campaign date fields, ad set scheduling, phase transitions. | Ahmed (brief) |
| 4 | Upstream QA gates: all upstream packages (creative, copy AR, copy EN, media plan, tracking) are at status draft. None have cleared skill eval, arabic-copy-qa, english-copy-qa, brand-qa-reviewer, or compliance-privacy-check. | All ad copy and creative variants. Nothing goes live until upstream packages are at least qa-passed. | QA pipeline (orchestrator to route) |
| 5 | Rights-cleared Bassam Fattouh assets (photography and footage): OPEN ITEM. C1 (AB1) and C4 (AB4) are blocked. | Ad variants META-AS-01-AD-01, TIKTOK-AS-01-AD-02, YOUTUBE-AG-01-AD-01. Fallback C2 and C3 are buildable. | Ahmed (asset confirmation) |
| 6 | YouTube trailer asset: ASSUMPTION not confirmed. YOUTUBE-CAMP-01 is conditionally blocked. | 10 percent YouTube budget share, YOUTUBE-CAMP-01. Human gate decides: hold for asset or fold into Meta. | Ahmed (go/no-go on YouTube for launch) |
| 7 | Gate platform: OPEN ITEM. Email or WhatsApp capture platform vendor unconfirmed. | All gate-landing CTAs (AD-PRIMARY-A4 / EN-AD-D retargeting ads, SOCIAL-S5/S7/S8 AR organic, and signup gate itself). Meta retargeting ad sets META-AS-04, META-AS-05 blocked on gate-completer audiences. CAPI wiring for gate events blocked. | Ahmed (platform decision) |
| 8 | Compliance-privacy-check: not yet cleared for retargeting audiences, hashed list upload, CAPI hashed signals, Saudi PDPL data-residency. | All retargeting ad sets (META-AS-04, META-AS-05, TIKTOK-AS-02), subscriber suppression list upload, gate-side CAPI calls. | compliance-privacy-reviewer (route from orchestrator) |
| 9 | Pixel and tracking production deployment: tracking-plan is draft, not deployed. Production writes are human-gate actions. | Pixel-based custom audiences, retargeting pools, conversion optimization events on all platforms. | Ahmed (human gate approves production tracking writes) |
| 10 | Reserve release decision: the 5 percent reserve and the conditional YouTube 10 percent are held pending week 1 performance readout. | Mid-flight optimization and channel rebalancing. | Ahmed (approve analytics-reporter proposal at end of week 1) |

---

## 10. Spend on approval

Approving this package and clearing all blocking open items above authorizes paid-build-engineer
to stage all campaigns and ad sets in the paused state described in sections 1 through 4, with
budgets filled using Ahmed's confirmed total figure, allocated proportionally as shown in section
7. The maximum spend if approved equals the Ahmed-confirmed total budget over the confirmed
flight window (ASSUMPTION: 3 weeks, 2026-06-08 to 2026-06-28), in the confirmed currency.

No absolute spend figure is stated here. The brief has not confirmed one. Stating an invented
number would violate the campaign-agnostic principle and the engine's hard rule against assumed
budgets.

Channels and their spend shares when budget is confirmed:
- Meta and Instagram: 50 percent of confirmed budget
- TikTok: 20 percent of confirmed budget
- Google Search: 15 percent of confirmed budget
- YouTube: 10 percent of confirmed budget (conditional on trailer asset; moves to reserve if
  asset is not available)
- Reserve: 5 percent of confirmed budget (held until week 1 readout, then released to best
  performer via human-gate proposal)

---

## 11. Flips live

Approving this package and filling in the confirmed budget, dates, and target CPA starts all
paused campaigns simultaneously on the confirmed start date and begins spending up to the
confirmed budget ceiling across Meta, TikTok, Google Search, and YouTube (conditional), with
no further action from the engine until the week 1 performance readout triggers an optimization
proposal back to the human gate.

---

## 12. Handoff

This package is routed to:
- human-gate: for review and approval of the budget (open item 1), target CPA (open item 2),
  schedule (open item 3), YouTube go/no-go (open item 6), and gate platform decision (open
  item 7). Each is a discrete decision. Silence is not approval.
- compliance-privacy-reviewer: open item 8, for clearance of all retargeting audiences, hashed
  list upload, CAPI hashed signals, and Saudi PDPL data-residency decision before any audience
  or tracking goes live.
- QA pipeline (orchestrator): open item 4, to route all upstream packages through remaining QA
  gates and advance status to qa-passed before go-live.
- analytics-reporter (streams 8, 9): once approved and live, all performance data flows from
  Meta, Google, and TikTok against the success metrics defined in tracking-plan and
  media-plan-package section 7. The week 1 readout triggers the reserve-release proposal and
  any optimization triggers (media-plan-package section 6).

Nothing in this package spends, publishes, or goes live. Every campaign and ad set is staged
paused. Ahmed flips each channel live after approving the open items above.

Status: gated-pending. Awaiting human gate review.

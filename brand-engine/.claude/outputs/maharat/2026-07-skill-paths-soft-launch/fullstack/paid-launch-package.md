# paid-launch-package: Skill Paths soft launch, staged campaign structure

Paid build artifact. Owned by paid-build-engineer. Nothing here publishes, sends, or spends.
Every campaign, ad set, and ad in this package is PAUSED. Spend is a gated action. A human
flips it live; this engine never does. No em dashes. Western numerals only.

---

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: paid-build-engineer
- stream: 5 build and launch
- status: gated-pending
- qa:
  - skill_eval: self-checked (structure, spend controls, naming, UTMs, guardrails). Formal
    eval pending.
  - arabic_qa: carried from copy-package.ar.md (status: draft, pre-QA, not yet passed). The
    in-platform Arabic copy in this package is drawn from that source and carries the same
    pre-QA status. Go-live is blocked until arabic-copy-qa and brand-qa-reviewer pass the
    copy package.
  - brand_qa: carried from copy-package.ar.md and copy-package.en.md (both draft, pre-QA).
    Go-live blocked until brand-qa-reviewer clears both.
- open_items:
  1. BLOCKER. Currency not confirmed. SAR or USD. All budget figures in this package use the
     brief's stated amounts (10,000 total, split as below) but are denominated [CURRENCY TBC].
     No spend is authorized until Ahmed confirms the currency.
  2. BLOCKER. Target CPA (cost per signup, cost per install) not confirmed. Week-2 cost-cap
     bidding cannot be set. Until confirmed, week-2 campaigns remain on maximize-conversions
     (lowest-cost). Surfaces at the human gate.
  3. BLOCKER. Gate platform and destination URL not confirmed (email or WhatsApp, confirmed by
     brief and media-plan as open). Paid ads drive to the early-access signup gate. Without a
     confirmed live URL, the destination field in all web-signup ad sets is a placeholder.
     Build is staged; go-live is blocked.
  4. BLOCKER. Tracking deployment not confirmed. The tracking-plan (data-tracking-engineer)
     is in draft. Meta Pixel, CAPI, GA4, and MMP (app install attribution) must be deployed to
     production and test-verified before any campaign goes live. See checklist item 1.
  5. BLOCKER. Consent basis for retargeting and lookalike audiences not confirmed.
     Compliance-privacy-reviewer has not cleared the CAPI PII policy, Saudi PDPL data-residency,
     or cross-border hashed-list upload. Retargeting ad sets are staged paused; go-live is
     blocked until consent is confirmed. Prospecting-only is the minimal launchable slice.
  6. BLOCKER. Ad account access not confirmed for any channel. Meta Ads, TikTok Ads, and
     Google Ads account IDs are not yet provided. The staged structure below names accounts as
     placeholders. Live action (building, publishing) is blocked until access is confirmed per
     account.
  7. BLOCKER. Asset confirmation pending. Creative-package assets (AB-03, AB-04, AB-05, AB-06,
     V1) are direction briefs, not finished renders. Approved Skill Paths product or brand
     imagery is not confirmed (brief sec 7). Ads reference asset IDs as placeholders; final
     renders must be confirmed and uploaded to the ad platforms before go-live. Abstract
     brand-constant creative (emerald on near-black) is the launchable fallback per the
     paid-spend-plan.
  8. Non-blocking. YouTube conditional on video asset confirmation. YouTube budget (1,000
     [CURRENCY TBC]) and all YouTube ad sets are staged paused. If the V1 video asset is not
     confirmed before the flight start, this budget rolls to reserve per the paid-spend-plan.
  9. Non-blocking. TikTok week-2 retargeting pool size is unknown. If the pool is below the
     platform minimum at the start of week 2, the TikTok retargeting ad set stays paused and
     the 500 [CURRENCY TBC] rolls to Meta retargeting via a human-gate proposal.
  10. Non-blocking. Suppression lists (existing customers, existing early-access signups) source
      not confirmed. Custom audience exclusions reference the suppression list type; the actual
      uploaded list is a placeholder until the source is confirmed by Ahmed.
  11. Non-blocking. Early-access seat cap not confirmed. No scarcity copy or pacing stop is
      wired. If Ahmed confirms a real cap, optimization trigger 5 from the media-plan activates.
  12. Non-blocking. MMP selection is an open item (tracking-plan, section 8). App-install ad
      sets are staged but attribution wiring (MMP postbacks to Meta, TikTok, Google) is blocked
      until the MMP is named.
- brief_refs:
  - budget: 10,000 total [CURRENCY TBC], brief sec 6, supplied by Ahmed 2026-06-05
  - split: Meta and Instagram 5,000 (50%), TikTok 2,000 (20%), Google Search plus UAC 1,500
    (15%), YouTube 1,000 (10%, conditional), reserve 500 (5%), per paid-spend-plan
  - flight: 2026-07-01 to 2026-07-14, 14 days, brief sec 6
  - geo: GCC, Saudi Arabia primary, brief sec 3
  - objective: early-access signups (gate completions) and campaign-attributable app installs,
    brief sec 2
  - offer: early access to Skill Paths, free signup, no price, brief sec 4
  - bid strategy: week 1 maximize conversions (lowest cost), week 2 cost cap if target is
    confirmed, per media-plan-package sec 4 and paid-spend-plan
  - segments: strategy-artifact segments 1 (owned non-payers, lifecycle, not this stream),
    2 (new acquisition), 3 (retargeting)
  - target CPA: OPEN ITEM. Not set. Stop for Ahmed.

---

## Body

### Staged structure

All campaigns, ad sets, and ads are PAUSED. No delivery, no spend.

---

#### Channel 1: Meta and Instagram

Account placeholder: [META-ADS-ACCOUNT-ID-TBC]
Total budget allocated: 5,000 [CURRENCY TBC]
Week 1 (2026-07-01 to 2026-07-07): 2,750 [CURRENCY TBC]
Week 2 (2026-07-08 to 2026-07-14): 2,250 [CURRENCY TBC]

---

##### CAMPAIGN: META-WSIGN-01

- campaign_name: maharat_skill-paths_sa_web-signup_prospecting_2026-07
- objective: leads (or conversions, confirmed signup event: maharat_ea_confirm)
- status: PAUSED
- budget_type: campaign-level daily budget
- daily_budget: 393 [CURRENCY TBC] (2,750 divided by 7 days, week 1 rate; adjusts in week 2)
- schedule: 2026-07-01 to 2026-07-07 (week 1). Week 2 continues under META-WSIGN-02.
- special_ad_categories: none (not credit, employment, or housing)
- campaign_spending_cap: 2,750 [CURRENCY TBC] for week 1

###### Ad Set: META-WSIGN-01-AS01

- ad_set_name: mkt_sp_sa_wsign_seg2_interest_w1
- segment: 2, new acquisition by self-improvement interest
- status: PAUSED
- targeting:
  - geo: Saudi Arabia (primary), UAE, Kuwait, Bahrain (secondary GCC)
  - age: 18 to 35
  - language: Arabic
  - interest and behavior targeting:
    - personal development and self-improvement
    - productivity and habit formation
    - online learning and e-learning
    - books and reading habits
    - career growth and professional skills
  - exclusions: existing Maharat customers [SUPPRESSION-LIST-TBC]; existing early-access
    signups [SUPPRESSION-LIST-TBC]; existing Meta page followers (optional)
- placements: Instagram feed, Instagram Reels, Facebook feed, Facebook Reels, Instagram Stories
- optimization_event: maharat_ea_confirm (CompleteRegistration or Lead, confirm with
  tracking-plan naming before go-live)
- bid_strategy: lowest cost (week 1; no cost cap until target CPA is confirmed)
- daily_budget: drawn from campaign-level; no ad-set-level override in week 1
- creative:
  - Ad META-WSIGN-01-AS01-AD01: static, concept C2 streak (asset ref AB-03)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - headline: ابن مهارة حقيقية، خطوة كل يوم (AR) / Build a real skill, one step a day. (EN)
    - primary_text: AR-PAID-01 primary_text (see copy-package.ar.md, section 1)
    - cta_button: سجل اهتمامك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC] with UTM below
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-03-AR-PAID-01&utm_term=seg2-interest
    - status: PAUSED
  - Ad META-WSIGN-01-AS01-AD02: static, concept C3 threshold (asset ref AB-06)
    - copy_variant_ar: AR-PAID-02
    - copy_variant_en: paid-en-s2-v2
    - headline: نيتك بذرة، والطريق يحولها مهارة (AR) / Your next skill starts here. (EN)
    - primary_text: AR-PAID-02 primary_text (see copy-package.ar.md, section 1)
    - cta_button: انضم للدخول المبكر (AR) / Join Early Access (EN)
    - destination_url: [GATE-URL-TBC] with UTM below
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-06-AR-PAID-02&utm_term=seg2-interest
    - status: PAUSED
    - flag: paid-en-s2-v2 contains "Limited seats" line. Confirm seat cap before using this
      variant. Until cap is confirmed, substitute paid-en-s2-v1 in this slot.

###### Ad Set: META-WSIGN-01-AS02

- ad_set_name: mkt_sp_sa_wsign_seg2_lookalike_w1
- segment: 2, new acquisition by lookalike of Maharat website visitors
- status: PAUSED
- targeting:
  - geo: Saudi Arabia
  - lookalike: 1% lookalike of Maharat website custom audience (all visitors), Saudi Arabia
  - lookalike_seed_check: minimum seed pool of roughly 1,000 events required. If the pixel pool
    is below threshold at build time, this ad set holds and the budget concentrates in AS01.
    Confirm pool size at go-live.
  - exclusions: same suppression as AS01
- placements: Instagram feed, Instagram Reels, Facebook feed
- optimization_event: maharat_ea_confirm
- bid_strategy: lowest cost (week 1)
- daily_budget: drawn from campaign-level
- creative:
  - Ad META-WSIGN-01-AS02-AD01: motion, concept C2 streak (asset ref AB-04)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - headline: ابن مهارة حقيقية، خطوة كل يوم (AR) / Build a real skill, one step a day. (EN)
    - cta_button: سجل اهتمامك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-04-AR-PAID-01&utm_term=seg2-lal
    - status: PAUSED
  - Ad META-WSIGN-01-AS02-AD02: video, concept V1 teaser (asset ref V1)
    - copy_variant_ar: AR-PAID-01 (overlay supers per V1 brief)
    - copy_variant_en: paid-en-s2-v1
    - headline: ابن مهارة حقيقية، خطوة كل يوم (AR) / Build a real skill, one step a day. (EN)
    - cta_button: سجل اهتمامك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=V1-AR-PAID-01&utm_term=seg2-lal
    - status: PAUSED
    - flag: V1 video asset requires motion-production pass. Blocked until asset is confirmed.

---

##### CAMPAIGN: META-WSIGN-02

- campaign_name: maharat_skill-paths_sa_web-signup_retargeting_2026-07
- objective: leads or conversions
- status: PAUSED
- budget_type: campaign-level daily budget
- daily_budget: 321 [CURRENCY TBC] (2,250 divided by 7 days, week 2 rate)
- schedule: 2026-07-08 to 2026-07-14 (week 2 only; retargeting pools built in week 1)
- campaign_spending_cap: 2,250 [CURRENCY TBC]
- go_live_condition: retargeting custom audiences (video viewers, site visitors, engagers) must
  reach minimum size before this campaign activates. Confirm at the end of week 1.

###### Ad Set: META-WSIGN-02-AS01

- ad_set_name: mkt_sp_sa_wsign_seg3_retarget_sitevistors_w2
- segment: 3, retargeting, website visitors who did not complete early-access signup
- status: PAUSED
- targeting:
  - custom_audience: Maharat website visitors (all pages), last 30 days
  - exclusion: users who completed maharat_ea_confirm; same suppression lists as above
  - geo: Saudi Arabia primary, GCC secondary (mirror of prospecting geo)
- placements: Instagram feed, Instagram Reels, Instagram Stories, Facebook feed
- optimization_event: maharat_ea_confirm
- bid_strategy: lowest cost (week 2; shifts to cost cap if target CPA is confirmed)
- creative:
  - Ad META-WSIGN-02-AS01-AD01: static, concept C2 streak (asset ref AB-03)
    - copy_variant_ar: AR-PAID-03
    - copy_variant_en: paid-en-s3-v1
    - headline: خطوة واحدة تفصلك عن البداية (AR) / One step left. Join early access. (EN)
    - primary_text: AR-PAID-03 primary_text
    - cta_button: أكمل تسجيلك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-03-AR-PAID-03&utm_term=seg3-sitevistors
    - status: PAUSED
  - Ad META-WSIGN-02-AS01-AD02: Stories, concept C3 threshold (asset ref AB-05)
    - copy_variant_ar: AR-PAID-04
    - copy_variant_en: paid-en-s3-v2
    - headline: الطريقة، لا الوقت (AR) / The path that fits your day. (EN)
    - primary_text: AR-PAID-04 primary_text
    - cta_button: انضم للدخول المبكر (AR) / Join Early Access (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-05-AR-PAID-04&utm_term=seg3-sitevistors
    - status: PAUSED

###### Ad Set: META-WSIGN-02-AS02

- ad_set_name: mkt_sp_sa_wsign_seg3_retarget_videoviewers_w2
- segment: 3, retargeting, video viewers (50% or more of any Maharat Meta/Instagram video,
  last 60 days)
- status: PAUSED
- targeting:
  - custom_audience: video viewers 50% threshold, Maharat Meta and Instagram pages, 60 days
  - exclusion: completed maharat_ea_confirm; same suppression lists
- placements: Instagram Reels, Facebook Reels, Instagram Stories
- optimization_event: maharat_ea_confirm
- bid_strategy: lowest cost
- creative:
  - Ad META-WSIGN-02-AS02-AD01: motion, concept C2 streak (asset ref AB-04)
    - copy_variant_ar: AR-PAID-03
    - copy_variant_en: paid-en-s3-v1
    - headline: خطوة واحدة تفصلك عن البداية (AR) / One step left. Join early access. (EN)
    - cta_button: أكمل تسجيلك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-04-AR-PAID-03&utm_term=seg3-videoviewers
    - status: PAUSED

###### Ad Set: META-WSIGN-02-AS03

- ad_set_name: mkt_sp_sa_wsign_seg3_retarget_engagers_w2
- segment: 3, retargeting, Instagram and Facebook page engagers (last 60 days)
- status: PAUSED
- targeting:
  - custom_audience: people who engaged with Maharat Instagram or Facebook page, 60 days
  - exclusion: completed maharat_ea_confirm; same suppression lists
- placements: Instagram feed, Facebook feed
- optimization_event: maharat_ea_confirm
- bid_strategy: lowest cost
- creative:
  - Ad META-WSIGN-02-AS03-AD01: static, concept C3 threshold (asset ref AB-06)
    - copy_variant_ar: AR-PAID-03
    - copy_variant_en: paid-en-s3-v2
    - headline: خطوة واحدة تفصلك عن البداية (AR) / The path that fits your day. (EN)
    - cta_button: أكمل تسجيلك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-06-AR-PAID-03&utm_term=seg3-engagers
    - status: PAUSED

---

##### CAMPAIGN: META-APPINSTALL-01

- campaign_name: maharat_skill-paths_sa_app-install_prospecting_2026-07
- objective: app installs (Mobile App Installs, optimize toward maharat_app_install or
  downstream event maharat_activation if MMP postbacks are live)
- status: PAUSED
- budget_type: campaign-level daily budget
- note_on_budget: Meta budget is 5,000 total across both web-signup and app-install objectives.
  The inner split between web-signup and app-install campaigns within the Meta 5,000 is not
  set in the paid-spend-plan (noted explicitly: "inner split set in media-plan-package"). The
  media-plan-package does not specify an exact number. This is a stop-and-ask. The campaigns
  are staged with a placeholder split of approximately 80% web-signup (4,000) and 20% app-
  install (1,000) within the Meta total, but this split MUST be confirmed by Ahmed before
  go-live. Budgets below are placeholders only.
- daily_budget: placeholder (approx 143 [CURRENCY TBC] per day over 7 days = 1,000 for the flight,
  subject to confirmed split)
- schedule: 2026-07-01 to 2026-07-14
- campaign_spending_cap: placeholder (approx 1,000 [CURRENCY TBC], subject to confirmed split)
- app_store_link: [APP-STORE-URL-TBC] (iOS App Store and Google Play)
- go_live_condition: MMP deployment confirmed, postback from MMP to Meta live, app store
  listing confirmed. All three are open items.

###### Ad Set: META-APPINSTALL-01-AS01

- ad_set_name: mkt_sp_sa_appinstall_seg2_interest_w1
- segment: 2, new acquisition, self-improvement interest, 18 to 30 sub-segment
- status: PAUSED
- targeting:
  - geo: Saudi Arabia primary, GCC secondary
  - age: 18 to 30
  - language: Arabic
  - interests: same interest clusters as META-WSIGN-01-AS01
  - device: mobile only (iOS and Android)
  - exclusions: existing app installers [CUSTOM-AUDIENCE-TBC]; same suppression lists
- placements: Instagram feed, Instagram Reels, Facebook feed (mobile only)
- optimization_event: maharat_app_install (MMP postback, blocked until MMP confirmed)
- bid_strategy: lowest cost (week 1)
- creative:
  - Ad META-APPINSTALL-01-AS01-AD01: static, concept C2 streak (asset ref AB-03)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - headline: ابن مهارة حقيقية، خطوة كل يوم (AR) / Build a real skill, one step a day. (EN)
    - cta_button: حمّل التطبيق (AR) / Install App (EN)
    - destination_url: [APP-STORE-URL-TBC]
    - utm: utm_source=meta&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-03-AR-PAID-01&utm_term=appinstall-seg2
    - status: PAUSED

---

#### Channel 2: TikTok

Account placeholder: [TIKTOK-ADS-ACCOUNT-ID-TBC]
Total budget allocated: 2,000 [CURRENCY TBC]
Week 1 (2026-07-01 to 2026-07-07): 1,200 [CURRENCY TBC]
Week 2 (2026-07-08 to 2026-07-14): 800 [CURRENCY TBC] (retargeting conditional)
Channel access: OPEN ITEM. TikTok Ads account access not confirmed. Staged structure
is complete; live action is blocked until account access is granted.

---

##### CAMPAIGN: TIKTOK-WSIGN-01

- campaign_name: maharat_skill-paths_sa_web-signup_prospecting_tiktok_2026-07
- objective: conversions (if TikTok pixel is live on gate URL; falls back to traffic if pixel
  pool is below conversion-optimization threshold at go-live)
- status: PAUSED
- budget_type: campaign-level daily budget
- daily_budget: 171 [CURRENCY TBC] (1,200 divided by 7)
- schedule: 2026-07-01 to 2026-07-07 (week 1)
- campaign_spending_cap: 1,200 [CURRENCY TBC]

###### Ad Set: TIKTOK-WSIGN-01-AS01

- ad_set_name: mkt_sp_sa_wsign_seg2_interest_tiktok_w1
- segment: 2, new acquisition, self-improvement interest
- status: PAUSED
- targeting:
  - geo: Saudi Arabia primary, UAE and Kuwait secondary
  - age: 18 to 35
  - language: Arabic
  - interest and behavioral targeting:
    - self-improvement and personal development
    - productivity and online education
    - books and reading communities
    - life goals and habit formation
  - exclusions: existing Maharat TikTok followers; existing early-access signups [TBC];
    same suppression lists
- placements: TikTok feed (TopView or In-Feed Ads)
- optimization_event: maharat_ea_confirm (TikTok pixel, if live; else optimize for click)
- bid_strategy: lowest cost oCPM (week 1)
- creative:
  - Ad TIKTOK-WSIGN-01-AS01-AD01: motion, concept C2 streak (asset ref AB-04, 9:16 cut)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - overlay_text: AR headline overlay per AB-04 brief
    - cta_button: سجل اهتمامك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=tiktok&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-04-AR-PAID-01&utm_term=seg2-interest
    - status: PAUSED
  - Ad TIKTOK-WSIGN-01-AS01-AD02: video, concept V1 teaser (asset ref V1, 9:16 cut)
    - copy_variant_ar: AR-PAID-02
    - copy_variant_en: paid-en-s2-v1
    - overlay_text: AR super overlays per V1 brief
    - cta_button: انضم للدخول المبكر (AR) / Join Early Access (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=tiktok&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=V1-AR-PAID-02&utm_term=seg2-interest
    - status: PAUSED
    - flag: V1 video requires motion-production pass. Blocked until asset is confirmed.

---

##### CAMPAIGN: TIKTOK-WSIGN-02

- campaign_name: maharat_skill-paths_sa_web-signup_retargeting_tiktok_2026-07
- objective: conversions
- status: PAUSED
- budget_type: campaign-level daily budget
- daily_budget: 114 [CURRENCY TBC] (800 divided by 7)
- schedule: 2026-07-08 to 2026-07-14 (week 2 only)
- campaign_spending_cap: 800 [CURRENCY TBC]
- go_live_condition: TikTok video-view retargeting pool (75% view threshold, last 30 days) must
  exceed the platform minimum audience size (typically 1,000 in the region) by 2026-07-07.
  If the pool is below threshold, this campaign stays paused and the 800 [CURRENCY TBC] rolls
  to Meta retargeting via a human-gate proposal (media-plan optimization trigger 2).

###### Ad Set: TIKTOK-WSIGN-02-AS01

- ad_set_name: mkt_sp_sa_wsign_seg3_retarget_videoviewers_tiktok_w2
- segment: 3, retargeting, TikTok video viewers (75% view threshold, last 30 days)
- status: PAUSED
- targeting:
  - custom_audience: TikTok video viewers 75% threshold, Maharat TikTok account, last 30 days
  - exclusions: existing early-access signups; same suppression lists
- placements: TikTok feed
- optimization_event: maharat_ea_confirm
- bid_strategy: lowest cost; shifts to target CPA if TikTok conversion volume is above 20 to 30
  events by end of week 1
- creative:
  - Ad TIKTOK-WSIGN-02-AS01-AD01: motion, concept C2 streak (asset ref AB-04, 9:16 cut)
    - copy_variant_ar: AR-PAID-03
    - copy_variant_en: paid-en-s3-v1
    - overlay_text: AR-PAID-03 headline direction
    - cta_button: أكمل تسجيلك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=tiktok&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-04-AR-PAID-03&utm_term=seg3-videoviewers
    - status: PAUSED

---

##### CAMPAIGN: TIKTOK-APPINSTALL-01

- campaign_name: maharat_skill-paths_sa_app-install_tiktok_2026-07
- objective: app installs (TikTok App Event Optimization if TikTok SDK is integrated; falls
  back to app install objective without AEO if SDK events are not available at build time)
- status: PAUSED
- budget_type: campaign-level daily budget
- note_on_budget: TikTok total is 2,000. Inner web-signup vs app-install split is a placeholder
  (same stop-and-ask as Meta, same note applies). Placeholder split: 75% web-signup (1,500),
  25% app-install (500) within TikTok total. Confirm with Ahmed before go-live.
- daily_budget: placeholder (approx 36 [CURRENCY TBC] per day, full flight = 500 [CURRENCY TBC])
- schedule: 2026-07-01 to 2026-07-14
- campaign_spending_cap: placeholder (approx 500 [CURRENCY TBC])
- go_live_condition: TikTok SDK integration confirmed and MMP postback to TikTok live.

###### Ad Set: TIKTOK-APPINSTALL-01-AS01

- ad_set_name: mkt_sp_sa_appinstall_seg2_interest_tiktok
- segment: 2, 18 to 25 sub-segment, self-improvement interest
- status: PAUSED
- targeting:
  - geo: Saudi Arabia primary
  - age: 18 to 25
  - language: Arabic
  - interests: self-improvement, online education, life goals
  - device: mobile only
- optimization_event: maharat_app_install (TikTok AEO, blocked until SDK confirmed)
- bid_strategy: lowest cost
- creative:
  - Ad TIKTOK-APPINSTALL-01-AS01-AD01: motion, concept C2 streak (asset ref AB-04)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - cta_button: حمّل التطبيق (AR) / Install Now (EN)
    - destination_url: [APP-STORE-URL-TBC]
    - utm: utm_source=tiktok&utm_medium=paid_social&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=AB-04-AR-PAID-01&utm_term=appinstall-seg2
    - status: PAUSED

---

#### Channel 3: Google (Search plus App Campaigns)

Account placeholder: [GOOGLE-ADS-ACCOUNT-ID-TBC]
Total budget allocated: 1,500 [CURRENCY TBC]
Week 1 (2026-07-01 to 2026-07-07): 750 [CURRENCY TBC]
Week 2 (2026-07-08 to 2026-07-14): 750 [CURRENCY TBC]
Channel access: OPEN ITEM. Google Ads account access not confirmed. Staged structure is
complete; live action is blocked until account access is granted.
Note: the media-plan labels this channel "Google Search plus UAC" and the paid-spend-plan
labels it "Google (Search plus UAC)". This package stages both a Search campaign and a Google
App Campaign (UAC successor). The 1,500 is the combined Google allocation.

---

##### CAMPAIGN: GOOGLE-SEARCH-BRANDED-01

- campaign_name: maharat_skill-paths_sa_search_branded_2026-07
- campaign_type: Search
- status: PAUSED
- budget_type: daily budget
- daily_budget: 54 [CURRENCY TBC] (approximately 750 divided across both Search campaigns over
  7 days; branded receives higher share, see note below)
- schedule: 2026-07-01 to 2026-07-14 (steady rate, both weeks)
- campaign_spending_cap: 750 [CURRENCY TBC] (combined Search total; inner branded vs non-
  branded split is a placeholder at 60% branded / 40% non-branded = 450 / 300. Confirm
  with Ahmed before go-live.)
- geo: Saudi Arabia primary, UAE and Kuwait secondary
- language: Arabic and English
- bid_strategy: target impression share (top of page, 90% or above). Branded terms have
  minimal competition.
- networks: Google Search only (Search partners optional, confirm at go-live)
- conversion_action: maharat_ea_confirm (mapped as Google Ads conversion from GA4 sign_up event;
  confirm wiring with tracking-plan before go-live)

###### Ad Group: GOOGLE-SEARCH-BRANDED-01-AG01

- ad_group_name: branded_maharat_exact_phrase
- match_types: exact and phrase
- keyword_themes: Maharat branded terms and common variations (Arabic and English). Specific
  keyword lists are set at trafficking time by the performance-marketer using the keyword
  themes from media-plan-package sec 3. Not hard-coded here.
- negative_keywords: competitor brand names (if any are known at go-live)
- ads:
  - Ad GOOGLE-SEARCH-BRANDED-01-AG01-AD01: Responsive Search Ad
    - copy_variant_en: paid-en-s2-v1 (adapted for RSA character limits)
    - headline_1 (EN): Build a real skill, one step a day. (30 char target)
    - headline_2 (EN): Maharat Skill Paths, early access.
    - headline_3 (EN): Register your interest now.
    - description_1 (EN): A short-step, gamified way to learn. A few minutes a day. A skill
      that stays.
    - description_2 (EN): Early access is open. Join Maharat Skill Paths before the full
      launch.
    - final_url: [GATE-URL-TBC]
    - utm: utm_source=google&utm_medium=cpc&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=search-branded&utm_term={keyword}
    - status: PAUSED

---

##### CAMPAIGN: GOOGLE-SEARCH-NONBRANDED-01

- campaign_name: maharat_skill-paths_sa_search_nonbranded_2026-07
- campaign_type: Search
- status: PAUSED
- budget_type: daily budget
- daily_budget: 43 [CURRENCY TBC] (300 divided by 7)
- schedule: 2026-07-01 to 2026-07-14
- campaign_spending_cap: 300 [CURRENCY TBC] (placeholder, subject to confirmed split)
- geo: Saudi Arabia primary, UAE and Kuwait secondary
- language: Arabic and English
- bid_strategy: maximize conversions (week 1); shifts to target CPA in week 2 if 30 or more
  conversion events are recorded and the target CPA is confirmed. Without the target, remains
  on maximize conversions for the full flight.
- audience_layering: in-market for education apps; self-improvement content consumers (Google
  audience signal, observation mode only, not restrictive)
- rlsa_week2: website visitors (last 30 days) receive a bid uplift on relevant search queries
  in week 2. Applied as a bid modifier on this existing campaign, not as a separate campaign.
- conversion_action: maharat_ea_confirm

###### Ad Group: GOOGLE-SEARCH-NONBRANDED-01-AG01

- ad_group_name: learning_app_intent_ar
- language_focus: Arabic queries
- keyword_themes: Arabic language skill development apps, online learning Arabic, self-
  improvement app, habit building app Arabic, learning habit app. Specific keyword lists
  set at trafficking time.
- negative_keywords: competitor brand names; irrelevant education verticals (schools,
  universities, degrees)
- ads:
  - Ad GOOGLE-SEARCH-NONBRANDED-01-AG01-AD01: Responsive Search Ad
    - copy_variant_en: paid-en-s2-v1 (adapted)
    - headline_1 (EN): Build a real skill, one step a day.
    - headline_2 (EN): Short steps. A streak. A skill that stays.
    - headline_3 (EN): Join Maharat early access.
    - description_1 (EN): A few minutes a day is enough. Maharat Skill Paths is a new way
      to learn, gamified and built for busy days.
    - description_2 (EN): Early access is open now. Register your interest and be among
      the first in.
    - final_url: [GATE-URL-TBC]
    - utm: utm_source=google&utm_medium=cpc&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=search-nonbranded-ar&utm_term={keyword}
    - status: PAUSED

###### Ad Group: GOOGLE-SEARCH-NONBRANDED-01-AG02

- ad_group_name: learning_app_intent_en
- language_focus: English queries (GCC users search in both languages)
- keyword_themes: same intent clusters as AG01, English queries
- ads:
  - Ad GOOGLE-SEARCH-NONBRANDED-01-AG02-AD01: Responsive Search Ad
    - copy_variant_en: paid-en-s2-v1 (adapted)
    - headlines and descriptions: same spirit as AG01, adapted for English query context
    - final_url: [GATE-URL-TBC]
    - utm: utm_source=google&utm_medium=cpc&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=search-nonbranded-en&utm_term={keyword}
    - status: PAUSED

---

##### CAMPAIGN: GOOGLE-UAC-01

- campaign_name: maharat_skill-paths_sa_app-campaign_2026-07
- campaign_type: App campaign (Google Universal App Campaign successor)
- status: PAUSED
- budget_type: daily budget
- note_on_budget: Google total is 1,500. Inner Search vs App Campaign split is a placeholder
  (same stop-and-ask as Meta and TikTok). Placeholder split: 67% Search (1,000), 33% App
  Campaign (500). Confirm with Ahmed before go-live.
- daily_budget: placeholder (approx 36 [CURRENCY TBC] per day for 14 days = 500 [CURRENCY TBC])
- schedule: 2026-07-01 to 2026-07-14
- campaign_spending_cap: placeholder (approx 500 [CURRENCY TBC])
- app_id: [APP-ID-TBC] (iOS App Store ID and Google Play package name)
- optimization_goal: app installs (week 1); in-app actions (maharat_activation, if events are
  available in week 2)
- bid_strategy: maximize installs (week 1); target CPA per install in week 2 if volume is
  sufficient and target is confirmed
- geo: Saudi Arabia primary, GCC secondary
- language: Arabic and English
- ad_assets:
  - text_asset_1 (EN): Build a real skill, one step a day. (drawn from paid-en-s2-v1)
  - text_asset_2 (EN): A few minutes a day. A streak. A skill that stays.
  - image_asset: AB-03 (C2 streak, 1:1 cut) as primary image
  - video_asset: AB-04 (C2 streak motion, 9:16 and 16:9 cuts) as video
  - utm: utm_source=google&utm_medium=uac&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=uac-appinstall
  - status: PAUSED
- go_live_condition: app listing confirmed in Google Play Console and Apple App Store; MMP
  postback to Google Ads confirmed live.

---

#### Channel 4: YouTube (week 2 only, conditional on video asset)

Account placeholder: [GOOGLE-ADS-ACCOUNT-ID-TBC] (YouTube runs under Google Ads)
Total budget allocated: 1,000 [CURRENCY TBC] (CONDITIONAL)
Week 1: 0 (YouTube holds in week 1)
Week 2 (2026-07-08 to 2026-07-14): 1,000 [CURRENCY TBC]
Conditional note: YouTube budget activates only if the V1 video asset is confirmed and
approved before 2026-07-08. If V1 is not confirmed, the 1,000 [CURRENCY TBC] moves to the
reserve (which then becomes 1,500 reserve total) per the paid-spend-plan. A human-gate
proposal is required to make that move.
Channel access: same Google Ads account as Search, OPEN ITEM.

---

##### CAMPAIGN: YOUTUBE-VAC-01

- campaign_name: maharat_skill-paths_sa_youtube_retarget-reach_w2_2026-07
- campaign_type: Video action campaign (VAC)
- status: PAUSED
- budget_type: daily budget
- daily_budget: 143 [CURRENCY TBC] (1,000 divided by 7)
- schedule: 2026-07-08 to 2026-07-14 (week 2 only)
- campaign_spending_cap: 1,000 [CURRENCY TBC]
- bid_strategy: target CPA if conversion target is confirmed; maximize conversions if not
- conversion_action: maharat_ea_confirm
- go_live_condition: V1 video asset confirmed and approved; Google Ads account access confirmed;
  retargeting pools from Meta and TikTok confirmed large enough to seed YouTube remarketing.

###### Ad Set: YOUTUBE-VAC-01-AS01

- ad_set_name: mkt_sp_sa_youtube_seg3_retarget_videoviewers_w2
- segment: 3, retargeting, YouTube video viewers (any Maharat YouTube content, last 30 days)
- status: PAUSED
- targeting:
  - custom_audience: YouTube video viewers, Maharat channel, last 30 days
  - website_remarketing: Maharat site visitors, last 30 days (Google Ads remarketing list)
  - exclusions: completed maharat_ea_confirm; same suppression lists
- placements: YouTube in-stream (skippable), YouTube Shorts
- creative:
  - Ad YOUTUBE-VAC-01-AS01-AD01: video, concept V1 teaser (asset ref V1, 16:9 cut for in-
    stream; 9:16 cut for Shorts)
    - copy_variant_ar: AR-PAID-03 (retargeting framing in supers)
    - copy_variant_en: paid-en-s3-v1
    - companion_banner: AB-06 (C3 threshold static, 1:1 cut) as companion banner
    - cta_overlay: أكمل تسجيلك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=youtube&utm_medium=paid_video&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=V1-AR-PAID-03&utm_term=seg3-videoviewers
    - status: PAUSED

###### Ad Set: YOUTUBE-VAC-01-AS02

- ad_set_name: mkt_sp_sa_youtube_seg2_custintent_w2
- segment: 2, custom intent audience (users who searched for self-improvement and online
  learning queries on Google in the last 30 days)
- status: PAUSED
- targeting:
  - custom_intent_audience: self-improvement apps, online learning, habit building apps,
    Arabic skill development (query-based custom segment)
  - affinity: self-development and online education (in-market, Arabic-speaking adults,
    Saudi Arabia)
  - geo: Saudi Arabia primary
  - age: 18 to 35
  - exclusions: completed maharat_ea_confirm; same suppression lists
- placements: YouTube in-stream (skippable)
- creative:
  - Ad YOUTUBE-VAC-01-AS02-AD01: video, concept V1 teaser (asset ref V1, 16:9 cut)
    - copy_variant_ar: AR-PAID-01
    - copy_variant_en: paid-en-s2-v1
    - cta_overlay: سجل اهتمامك (AR) / Register Interest (EN)
    - destination_url: [GATE-URL-TBC]
    - utm: utm_source=youtube&utm_medium=paid_video&utm_campaign=2026-07-skill-paths-soft-launch&utm_content=V1-AR-PAID-01&utm_term=seg2-custintent
    - status: PAUSED

---

#### Reserve

- amount: 500 [CURRENCY TBC]
- status: held, not allocated to any campaign
- release_condition: at the end of week 1 (2026-07-07), a human-gate proposal is submitted
  identifying the best-performing channel or ad set (lowest cost per signup or install with
  at least 15 to 20 conversions). The reserve is released to that channel. No reallocation
  without explicit human-gate approval.
- if_youtube_conditional_fails: reserve becomes 1,500 [CURRENCY TBC] (YouTube 1,000 plus
  original 500). Same release logic applies.

---

### UTM taxonomy

All URLs follow this structure. No personal data in any UTM field.

| Parameter | Values used | Notes |
|---|---|---|
| utm_source | meta, tiktok, google, youtube | platform |
| utm_medium | paid_social, cpc, uac, paid_video | channel type |
| utm_campaign | 2026-07-skill-paths-soft-launch | always the campaign_id from the brief |
| utm_content | {asset-ref}-{copy-variant-id} | e.g. AB-03-AR-PAID-01. Identifies the creative and copy pairing. |
| utm_term | seg2-interest, seg2-lal, seg3-sitevistors, seg3-videoviewers, seg3-engagers, appinstall-seg2, search-branded, search-nonbranded-ar, search-nonbranded-en, seg2-custintent | audience or keyword group |

UTM encoding note: all values are lowercase with hyphens. No spaces, no personal identifiers,
no email fragments, no user IDs, no session tokens.

---

### Tracking wiring (from tracking-plan, data-tracking-engineer)

The tracking-plan is in draft (status: draft). The following wiring is referenced by this
package and must be confirmed before go-live.

| Tracking element | Role in this campaign | Status |
|---|---|---|
| Meta Pixel (maharat_ea_confirm as CompleteRegistration or Lead) | Conversion optimization for all Meta campaigns | BLOCKED, pixel deployment pending |
| Meta CAPI (server-side, maharat_ea_submit and maharat_ea_confirm with shared event_id) | Deduplication and server-side matching | BLOCKED, CAPI deployment pending |
| GA4 (sign_up event on maharat_ea_confirm) | Cross-channel measurement, BigQuery queries | BLOCKED, GA4 deployment pending |
| TikTok Pixel (maharat_ea_confirm) | Conversion optimization for TikTok campaigns | BLOCKED, pixel deployment pending |
| Google Ads conversion (linked from GA4 sign_up or direct tag) | Conversion optimization for Search and App campaigns | BLOCKED, tag deployment pending |
| MMP (app install postback to Meta, TikTok, Google) | App install attribution | BLOCKED, MMP not named |
| SKAdNetwork conversion values (iOS) | iOS app install reporting | BLOCKED, MMP not named |
| No personal data in UTM or event parameters | Compliance hard stop | Hardcoded in UTM taxonomy and tracking-plan sec 7 |
| Test plan (tracking-plan sec 9) | Verify all events fire in order before go-live | BLOCKED, pixels not deployed |

---

### Pre-launch checklist

All items must show PASS before the human gate can approve go-live. Items currently FAIL or
BLOCKED block the package from the gate.

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Pixel firing and event verification (test plan complete, all events fire in order in test mode) | FAIL, BLOCKED | Tracking-plan is draft; pixels not deployed; test plan not run. Blocks go-live. |
| 2 | UTM consistency (utm_campaign matches campaign_id, no personal data in any UTM field, all URLs constructed per UTM taxonomy) | PASS (structure) | UTM taxonomy is consistent in this package. Final URL strings must be verified once the gate URL is confirmed. |
| 3 | Naming convention (all campaigns, ad sets, and ads follow the naming schema defined in this package) | PASS (structure) | Names follow the schema. Platform-side naming must match at build time. |
| 4 | Budget cap set from brief (total does not exceed 10,000 [CURRENCY TBC]; each channel does not exceed its allocated amount; reserve is held separately) | PASS (structure) | Budget amounts are drawn from the paid-spend-plan and brief. Currency is unconfirmed. Spend controls are set in this package. |
| 5 | End date set from brief (all campaigns have a hard end date of 2026-07-14 or the campaign-level spend cap is set to enforce the flight ceiling) | PASS (structure) | All campaigns carry the 2026-07-14 end date and campaign spending caps in this package. |
| 6 | Currency confirmed (SAR or USD) | FAIL | Currency is an open item. Ahmed must confirm before any spend is authorized. |
| 7 | Target CPA confirmed (cost per signup, cost per install) | FAIL | Not set in brief or strategy-artifact. Ahmed must confirm before week-2 cost-cap bidding can be set. |
| 8 | Gate platform and destination URL confirmed (early-access landing page URL live) | FAIL, BLOCKED | Gate platform (email or WhatsApp) is an open item. No destination URL exists. Paid ads cannot drive conversions without this. Blocks go-live. |
| 9 | Tracking deployed to production and test-verified (pixel firing, CAPI, GA4, MMP postbacks confirmed) | FAIL, BLOCKED | All tracking is in plan-only state. Deployment is a gated action; test plan not run. Blocks go-live. |
| 10 | Consent confirmed for retargeting and lookalike audiences (Saudi PDPL, cross-border consent, CAPI PII policy cleared by compliance-privacy-reviewer) | FAIL, BLOCKED | Compliance-privacy-reviewer has not cleared this. Retargeting ad sets are staged paused; go-live blocked. Prospecting-only is the minimal launchable slice. |
| 11 | Ad account access confirmed (Meta, TikTok, Google) | FAIL, BLOCKED | All three account IDs are placeholders. Blocks live build and any delivery. |
| 12 | Asset confirmation (creative renders approved, AB-03, AB-04, AB-05, AB-06, V1 finished and uploaded) | FAIL, BLOCKED | Creative-package assets are direction briefs, not finished renders. Abstract brand-constant creative is the fallback per paid-spend-plan. |
| 13 | Copy QA passed (arabic-copy-qa and brand-qa-reviewer passed on copy-package.ar.md and copy-package.en.md) | FAIL | Both copy packages are in draft, pre-QA. In-platform copy in this package is drawn from those sources. Go-live blocked until both QA gates pass. |
| 14 | Suppression lists confirmed and uploaded (existing customers, existing early-access signups as custom audience exclusions) | FAIL | Suppression list sources are not confirmed. Custom audience exclusions are placeholder references. |
| 15 | MMP confirmed and wiring live (app install campaigns across all channels) | FAIL, BLOCKED | No MMP named. All app-install campaigns are blocked beyond staging. |
| 16 | YouTube video asset confirmed (V1 production pass complete) | FAIL | V1 is a direction brief. YouTube campaigns are staged but the go-live condition (asset confirmed) is not met. |
| 17 | Inner budget splits confirmed (web-signup vs app-install within Meta, TikTok, and Google totals) | FAIL | The paid-spend-plan does not set this inner split. Placeholder splits are in this package. Ahmed must confirm before go-live. |

Summary: 2 PASS (structure-only), 15 FAIL or BLOCKED. The package is staged and complete
in structure; all 15 failing items must resolve before the human gate can approve go-live.
The 6 BLOCKER items (checklist items 1, 8, 9, 10, 11, 12) are the critical path.

---

### Spend on approval

Approving this package and clearing all checklist items authorizes delivery of the paused
campaigns above, with a maximum spend of 10,000 [CURRENCY TBC, to be confirmed as SAR or
USD by Ahmed before any spend is authorized] across Meta and Instagram, TikTok, Google
Search plus App Campaign, and YouTube (YouTube conditional on V1 asset confirmation), over
the 2026-07-01 to 2026-07-14 flight. The 500 [CURRENCY TBC] reserve is not allocated
until a human-gate proposal routes it to the best performer at the end of week 1.

---

### Flips live

Approving this package at the human gate and resolving all checklist blockers starts the
paused campaigns, begins delivery against the stated targeting and creative, and begins
spending toward the 10,000 [CURRENCY TBC] cap across the 2026-07-01 to 2026-07-14 flight.

---

## Handoff

- To: human-gate for go-live approval. The package is staged and paused. Nothing spends.
- On approval: paid-build-engineer executes exactly the approved go-live and spend, nothing
  more, using the Meta Ads MCP and Google Ads MCP after account access is confirmed.
- To: analytics-reporter (streams 8 and 9) after launch, measuring against the success
  metric defined in the strategy-artifact (early-access signups plus campaign-attributable
  app installs, 2026-07-01 to 2026-07-14).
- In-flight optimization proposals: any of the six triggers defined in media-plan-package
  sec 6 route to the human gate per trigger. No reallocation without explicit approval.

---

## Status

Staged, paused, gated-pending. 15 checklist items fail or are blocked. Nothing here
publishes, sends, or spends. Human gate required before any delivery.

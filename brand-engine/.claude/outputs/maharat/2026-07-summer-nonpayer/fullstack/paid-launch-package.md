# Paid Launch Package: Summer of Skills, roster-led breadth campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: paid-build-engineer
- stream: 5 build and launch
- status: gated-pending
- qa:
  - skill_eval: passed (structure complete, all budget fields placeholder, no absolute numbers,
    all ad sets staged paused, open items enumerated and not buried, copy variants mapped to
    creative concepts and ad sets, checklist completed with explicit pass and blocked states,
    no em dashes, Western numerals only, no invented values)
  - arabic_qa: carried from copy-package.ar.md (arabic-copy-qa passed 2026-06-12; copy
    variants used in this structure are AD-BREADTH-1, AD-MUSIC-1, AD-COOK-1, AD-MAKEUP-1,
    AD-BUSINESS-1, AD-ACTING-1, AD-RETARGET-1, AD-STYLING-1 (Cedric Haddad, authored and
    QA-passed), AD-MARKETING-1 (Elda Choucair, authored and QA-passed))
  - brand_qa: carried from creative-package.md and copy-package.ar.md and copy-package.en.md;
    brand-qa-reviewer gate pending on all three upstream packages; in-platform copy reviewed
    at this stage: Western numerals confirmed throughout, no em dashes, no tatweel in any
    copy variant mapped below
  - compliance: carried; compliance-privacy-reviewer gate pending on all tracking, audience
    uploads, and retargeting activations; Saudi PDPL data-residency decision blocking all
    hashed list uploads and CAPI wiring
- open_items:
  1. Budget and currency: OPEN ITEM. No budget or currency confirmed. All budget fields are
     placeholders throughout this package. Ahmed fills every budget field before go-live.
     Hard blocker on all spend.
  2. Target CPA or ROAS: ASSUMPTION. No cost-per-subscription target or ROAS confirmed. All
     cost-cap and Target CPA bid settings are unset. Phase 2 bid strategy is blocked until
     Ahmed confirms the target. Cost per subscription is an efficiency read only until confirmed.
  3. Schedule (start and end dates): ASSUMPTION. Proposed start 2026-07-01, proposed end
     2026-08-31. Confirm with Ahmed. All phase transitions and campaign date fields are blank
     until confirmed.
  4. Gate platform: OPEN ITEM. Email and WhatsApp signup-gate platform vendor unconfirmed.
     All gate-landing CTAs (AD-RETARGET-1 AR and EN, and any retargeting ad sets routing to
     the gate) are blocked. CAPI wiring for gate events is blocked. Meta retargeting custom
     audiences built from gate-completer lists cannot be activated until the platform is named
     and consent basis is confirmed.
  5. Upstream QA gates: all upstream packages (creative-package, copy-package.ar,
     copy-package.en, media-plan-package) are at status draft. None have cleared skill eval,
     arabic-copy-qa, english-copy-qa, brand-qa-reviewer, or compliance-privacy-check. This is
     a comprehensive go-live blocker for all channels. Structure is staged; nothing goes live
     until all upstream packages reach at least qa-passed.
  6. Rights-cleared instructor photography per instructor (Ragheb Alama, Salam Dakkak, Kosai
     Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair): OPEN ITEM per
     instructor. Creative concept C3 (instructor portrait, AB3) is blocked per instructor
     until approved, rights-cleared photography is confirmed. Concepts C1, C2, C4, C5, C7
     have no photography dependency and are buildable. This is a per-ad blocker, not a full
     go-live blocker; abstract fallback (C2 per field) is the launchable variant for each
     field ad set.
  7. Rights-cleared instructor footage (multi-field) for YouTube and video-led creative
     (concept C6, AB8): OPEN ITEM. C6 is blocked until rights-cleared class footage from
     at least three instructor fields is confirmed. YouTube campaign (YOUTUBE-CAMP-01) is
     conditionally blocked; the 12 percent YouTube budget share moves to the reserve if no
     cleared asset is available at launch. Human gate decides: hold for asset or fold into
     Meta.
  8. Per-instructor public-naming confirmation (confirm-at-gate for each of the seven):
     Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric
     Haddad, Elda Choucair. All seven carry public_naming_cleared: yes with Ahmed sign-off
     on file (2026-06-05), but catalog public_status column still reads unconfirmed. Every
     in-platform copy variant referencing a named instructor is a confirm-at-gate item. If a
     name is not cleared at the gate, the relevant per-field ad set drops to the abstract C2
     fallback and the unnamed breadth copy line.
  9. Verify-before-public-use facts: Toufic Kreidieh's Brands For Less name and the
     $10,000-garage detail, and Elda Choucair's Omnicom, Forbes, Cannes, and the 900-plus
     and 1000-plus figures, must not appear in any in-platform copy, audience label, or UTM
     field until verified. Confirmed absent from all copy variants mapped below.
  10. Saudi PDPL and data residency: OPEN ITEM. Consent basis and data-residency posture not
      confirmed. Blocks all hashed-list uploads (subscriber suppression, lookalike seeds,
      owned-non-payer suppression from paid), all retargeting audience activations, and all
      CAPI wiring. Compliance-privacy-reviewer must clear each before activation.
  11. Suppression of owned non-payers from paid prospecting: OPEN ITEM. Suppressing the
      roughly 18,000 owned non-payers from cold paid acquisition requires a hashed-list
      match between the CRM and Meta, TikTok, and YouTube custom audiences. Source list and
      consent basis must be confirmed. Same PDPL caveat applies.
  12. Google Search keyword set: final keyword list for all seven field groups requires
      review with seo-specialist before staging in Google Ads. Illustrative keyword groups
      are named in this package (from media-plan-package section 3.3); seo-specialist
      confirms or amends before build.
  13. Tracking not confirmed (data-tracking-engineer): the tracking-plan from
      data-tracking-engineer has not arrived at this build stage. Meta Pixel and CAPI events,
      TikTok Pixel, Google Ads conversion tag, YouTube remarketing tag, and UTM structure
      are referenced from media-plan-package section 7 (direction) but are not wired. Pixel
      firing on maharat.com is not confirmed deployed. Tracking wiring is a go-live
      prerequisite and a hard blocker on all pixel-based retargeting and conversion
      optimization. Structure is staged; go-live awaits tracking confirmation.
  14. Styling-field and marketing-field copy variants: RESOLVED. AD-STYLING-1 (Cedric
      Haddad, AR and EN) and AD-MARKETING-1 (Elda Choucair, AR and EN) have been authored
      by copywriter-ar and copywriter-en, passed arabic-copy-qa (2026-06-12) and
      english-copy-qa (2026-06-12), and are now wired into META-AS-07, META-AS-08,
      TIKTOK-AS-04, GOOGLE-AG-07, and GOOGLE-AG-08. Placeholder copy has been removed
      from all five ad sets and ad groups. Remaining go-live blockers on these ad sets are
      budget+currency (open item 1), gate platform (open item 4), tracking not wired (open
      item 13), PDPL (open item 10), and rights-cleared photography per instructor (open
      item 6, per-ad blocker on the C3 portrait variants only).
  15. Platform MCP read access: read-only access to Meta Ads, Google Ads, and TikTok Ads
      platforms for audience sizing and reach estimation is not yet approved. Audience
      definitions are directional. This is an Ahmed allowlist decision.
- brief_refs:
  - budget: OPEN ITEM. No budget or currency supplied. All budget fields are placeholders.
  - target_cpa_or_roas: ASSUMPTION. Not confirmed. Cost per subscription is efficiency read only.
  - bid_strategy: phase 1 maximize conversions toward gate-completion events (Meta), maximize
    video views (TikTok visual fields), maximize clicks (Google Search), CPV (YouTube
    conditional); phase 2 cost-cap and Target CPA once event volumes support it and Ahmed
    confirms the target. Proportional allocation shape: Meta and Instagram 45 percent, TikTok
    18 percent, Google Search 17 percent, YouTube 12 percent (conditional on footage),
    reserve 8 percent. Sourced from media-plan-package section 2.
  - schedule: proposed start 2026-07-01, proposed end 2026-08-31. ASSUMPTION. Confirm with Ahmed.
  - geo: GCC, primary Saudi Arabia.
  - offer: Maharat B2C subscription, hook is the breadth of the instructor roster across seven
    cleared fields. Free intro chapter 1 across all seven featured classes is the low-friction
    entry point. No price. No promotional offer. Value-led posture.

---

## Pre-flight validation

Inbound envelopes reviewed:

- creative-package (stream 3): campaign_id 2026-07-summer-nonpayer confirmed. Status draft.
  Concepts C1 through C7 and asset briefs AB1 through AB9 extracted. C3 (AB3, instructor
  portraits) is blocked per instructor until approved photography is confirmed. C6 (AB8,
  multi-field breadth reel) is blocked until footage from at least 3 fields is confirmed.
  C1, C2, C4, C5, C7 are buildable as abstract concepts with no photography dependency.
- copy-package.ar (stream 4): campaign_id 2026-07-summer-nonpayer confirmed. Status draft
  (arabic-copy-qa passed 2026-06-12; brand-qa resubmission pending). Paid ad copy variants
  extracted: AD-BREADTH-1 (platform breadth), AD-MUSIC-1 (music, Ragheb Alama), AD-COOK-1
  (cooking, Salam Dakkak), AD-MAKEUP-1 (makeup, Bassam Fattouh, feminine address),
  AD-BUSINESS-1 (business, Toufic Kreidieh), AD-ACTING-1 (acting, Kosai Khauli),
  AD-STYLING-1 (styling, Cedric Haddad, feminine address, authored and QA-passed
  2026-06-12), AD-MARKETING-1 (marketing, Elda Choucair, authored and QA-passed
  2026-06-12), AD-RETARGET-1 (retargeting, all fields). Open item 14 closed.
- copy-package.en (stream 4): campaign_id 2026-07-summer-nonpayer confirmed. Status draft
  (english-copy-qa passed 2026-06-12; brand-qa resubmission pending). Paid ad copy variants
  extracted: AD-BREADTH-1, AD-MUSIC-1, AD-COOK-1, AD-MAKEUP-1, AD-BUSINESS-1, AD-ACTING-1,
  AD-STYLING-1 (styling, Cedric Haddad, authored and QA-passed 2026-06-12), AD-MARKETING-1
  (marketing, Elda Choucair, authored and QA-passed 2026-06-12), AD-RETARGET-1 (EN
  counterparts). Open item 14 closed.
- media-plan-package (stream, upstream of stream 5): campaign_id 2026-07-summer-nonpayer
  confirmed. Status qa-passed. Budget OPEN ITEM confirmed. Target CPA OPEN ITEM confirmed.
  Proportional allocation shape, audience strategy, bid strategy phases, flighting structure,
  UTM direction, and open items extracted.
- tracking-plan from data-tracking-engineer: not received at this build stage. Tracking is
  referenced from media-plan-package section 7 as directional. Go-live is blocked until the
  tracking-plan is delivered, reviewed, and confirmed deployed. Flagged as open item 13.

Note on upstream status: creative-package, copy-package.ar, and copy-package.en are at status
draft. Per the I/O contract, this package is staged paused. Nothing goes live until all
upstream packages advance to at least qa-passed and each QA gate (arabic-copy-qa,
english-copy-qa, brand-qa-reviewer, compliance-privacy-check) clears.

---

## 1. Campaign structure: Meta and Instagram (primary)

Platform: Meta Ads Manager
Objective: Conversions (subscription_start via Pixel Purchase event)
Status: ALL STAGED PAUSED. Nothing spends until Ahmed flips live.

### 1.1 Campaign META-CAMP-01

- Campaign name: 2026-07-snp_meta_conversions
- Objective: Conversions
- Campaign budget: [PLACEHOLDER. Ahmed confirms budget and currency before go-live. No figure
  is stated here. Proportional guide: Meta and Instagram receives 45 percent of total confirmed
  budget.]
- Campaign budget type: Daily budget (recommended) or lifetime. Ahmed confirms.
- Special ad category: None (education and subscription; confirm with compliance-privacy-reviewer
  if any housing, employment, credit, or social-issue category applies in Saudi context).
- Bid strategy phase 1 (first 3 weeks): Lowest cost, maximize conversions toward gate-completion
  events (CompleteRegistration). No cost cap set in phase 1 until 50 optimization events
  accumulate per ad set.
- Bid strategy phase 2 (weeks 4 to 6): Introduce cost cap per gate completion once event
  volumes support it. Apply Ahmed-confirmed CPA target as the cap value. CPA field is blank
  until Ahmed confirms.
- Status: PAUSED

---

#### Ad Set META-AS-01: New acquisition, platform breadth interest

- Ad set name: 2026-07-snp_meta_prospecting_breadth
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (gate-completion, phase 1). Switch to Purchase
  (subscription_start) in phase 2 once 50 gate events accumulate.
- Audience: interests in online learning, self-development, Arabic content, personal growth,
  professional development. Broad platform-level set covering all seven field domains.
  Geo: Saudi Arabia (primary). GCC expansion (Bahrain, Kuwait, Qatar, UAE, Oman) as secondary
  after Saudi volume validates.
  Age: 18 to 35. Language: Arabic.
  Device: All (mobile-first given platform usage in geo).
- Placement: Advantage+ placements (Facebook Feed, Instagram Feed, Instagram Reels, Instagram
  Stories, Facebook Stories).
- Budget: [PLACEHOLDER. Share of the 45 percent Meta allocation. Set when total budget confirmed.]
- Schedule: [PLACEHOLDER. Proposed 2026-07-01 to 2026-08-31. Ahmed confirms.]
- Frequency cap: 3 impressions per person per day across all Meta placements.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-01-AD-01 | C1 platform breadth hero grid (no photography) | AB1, 1080x1350 | AD-BREADTH-1 primary text and headline | AD-BREADTH-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-01-AD-02 | C7 campaign identity thematic still (no photography) | AB7, 1080x1350 | AD-BREADTH-1 primary text and headline | AD-BREADTH-1 EN body and headline | Start Free / ابدأ مجاناً |

---

#### Ad Set META-AS-02: New acquisition, music interest (Ragheb Alama)

- Ad set name: 2026-07-snp_meta_prospecting_music
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in music appreciation, singing, musical instruments, Arabic music,
  performing arts. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Ragheb Alama class angle per media-plan-package section 3.1.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER. Share of 45 percent Meta allocation.]
- Schedule: [PLACEHOLDER. Proposed 2026-07-01 to 2026-08-31.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-02-AD-01 | C2 per-field abstract card, music variant (no photography) | AB2, music icon, 1080x1080 | AD-MUSIC-1 primary text and headline | AD-MUSIC-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-02-AD-02 | C3 instructor portrait, Ragheb Alama (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-MUSIC-1 primary text and headline | AD-MUSIC-1 EN body and headline | Start Free / ابدأ مجاناً |

Note on META-AS-02-AD-02: staged but blocked for delivery until AB3 (rights-cleared Ragheb
Alama photography) is confirmed per open item 6. META-AS-02-AD-01 (C2 abstract) is the
launchable variant. Instructor name in copy is confirm-at-gate per open item 8.

---

#### Ad Set META-AS-03: New acquisition, cooking interest (Salam Dakkak)

- Ad set name: 2026-07-snp_meta_prospecting_cooking
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in cooking, food, recipes, Levantine cuisine, home cooking, culinary
  arts. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Salam Dakkak class angle per media-plan-package section 3.1.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-03-AD-01 | C2 per-field abstract card, cooking variant (no photography) | AB2, cooking arc icon, 1080x1080 | AD-COOK-1 primary text and headline | AD-COOK-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-03-AD-02 | C3 instructor portrait, Salam Dakkak (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-COOK-1 primary text and headline | AD-COOK-1 EN body and headline | Start Free / ابدأ مجاناً |

Note on META-AS-03-AD-02: staged but blocked until Salam Dakkak photography confirmed.
C2 variant (AD-01) is the launchable fallback. Instructor name confirm-at-gate.

---

#### Ad Set META-AS-04: New acquisition, acting interest (Kosai Khauli)

- Ad set name: 2026-07-snp_meta_prospecting_acting
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in acting, film, Arabic drama, performing arts, theater, cinema.
  GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Kosai Khauli class angle per media-plan-package section 3.1.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-04-AD-01 | C2 per-field abstract card, acting variant (no photography) | AB2, light-cone icon, 1080x1080 | AD-ACTING-1 primary text and headline | AD-ACTING-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-04-AD-02 | C3 instructor portrait, Kosai Khauli (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-ACTING-1 primary text and headline | AD-ACTING-1 EN body and headline | Start Free / ابدأ مجاناً |

---

#### Ad Set META-AS-05: New acquisition, makeup interest (Bassam Fattouh)

- Ad set name: 2026-07-snp_meta_prospecting_makeup
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in makeup artistry, beauty, cosmetics, beauty tutorials, skincare,
  personal care. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Bassam Fattouh class angle per media-plan-package section 3.1.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-05-AD-01 | C2 per-field abstract card, makeup variant (no photography) | AB2, brush-arc icon, 1080x1080 | AD-MAKEUP-1 primary text and headline (feminine address) | AD-MAKEUP-1 EN body and headline | Start Free / ابدئي مجاناً |
| META-AS-05-AD-02 | C3 instructor portrait, Bassam Fattouh (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-MAKEUP-1 primary text and headline (feminine) | AD-MAKEUP-1 EN body and headline | Start Free / ابدئي مجاناً |

Note: AR copy (AD-MAKEUP-1) carries feminine address per brand-voice gendered address rule
for beauty category. EN copy does not carry a gender marker.

---

#### Ad Set META-AS-06: New acquisition, business interest (Toufic Kreidieh)

- Ad set name: 2026-07-snp_meta_prospecting_business
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in entrepreneurship, business, startups, management, leadership,
  personal finance. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Toufic Kreidieh class angle per media-plan-package section 3.1.
  Note: Brands For Less name and garage-origin detail are verify-before-public-use and must
  not appear in any audience label or ad copy until verified (open item 9).
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-06-AD-01 | C2 per-field abstract card, business variant (no photography) | AB2, ascending-steps icon, 1080x1080 | AD-BUSINESS-1 primary text and headline | AD-BUSINESS-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-06-AD-02 | C3 instructor portrait, Toufic Kreidieh (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-BUSINESS-1 primary text and headline | AD-BUSINESS-1 EN body and headline | Start Free / ابدأ مجاناً |

---

#### Ad Set META-AS-07: New acquisition, styling interest (Cedric Haddad)

- Ad set name: 2026-07-snp_meta_prospecting_styling
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in fashion, personal styling, wardrobe, style advice, celebrity
  fashion. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Cedric Haddad class angle per media-plan-package section 3.1.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-07-AD-01 | C2 per-field abstract card, styling variant (no photography) | AB2, draped-curve icon, 1080x1080 | AD-STYLING-1 primary text and headline (feminine address) | AD-STYLING-1 EN body and headline | Start Free / ابدئي مجاناً |
| META-AS-07-AD-02 | C3 instructor portrait, Cedric Haddad (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-STYLING-1 primary text and headline (feminine address) | AD-STYLING-1 EN body and headline | Start Free / ابدئي مجاناً |

Note on META-AS-07-AD-02: staged but blocked for delivery until AB3 (rights-cleared Cedric
Haddad photography) is confirmed per open item 6. META-AS-07-AD-01 (C2 abstract) is the
launchable variant. Instructor name confirm-at-gate per open item 8. AR copy uses feminine
address (styling category, per brand-voice gendered address rule, matching AD-MAKEUP-1 pattern).

---

#### Ad Set META-AS-08: New acquisition, marketing interest (Elda Choucair)

- Ad set name: 2026-07-snp_meta_prospecting_marketing
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration (phase 1). Purchase (phase 2).
- Audience: interests in digital marketing, brand building, advertising, content creation,
  social media marketing. GCC geo, Saudi Arabia primary. Age 18 to 35. Arabic language.
  Grounded in Elda Choucair class angle per media-plan-package section 3.1.
  Note: Omnicom, Forbes, Cannes, and numerical figures are verify-before-public-use and must
  not appear in any audience label or ad copy until verified (open item 9).
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: [PLACEHOLDER.]
- Frequency cap: 3 impressions per person per day.
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-08-AD-01 | C2 per-field abstract card, marketing variant (no photography) | AB2, radial-node icon, 1080x1080 | AD-MARKETING-1 primary text and headline | AD-MARKETING-1 EN body and headline | Start Free / ابدأ مجاناً |
| META-AS-08-AD-02 | C3 instructor portrait, Elda Choucair (BLOCKED pending cleared photography) | AB3, 1080x1350 | AD-MARKETING-1 primary text and headline | AD-MARKETING-1 EN body and headline | Start Free / ابدأ مجاناً |

Note on META-AS-08-AD-02: staged but blocked for delivery until AB3 (rights-cleared Elda
Choucair photography) is confirmed per open item 6. META-AS-08-AD-01 (C2 abstract) is the
launchable variant. Instructor name confirm-at-gate per open item 8. Verify-before-use facts
(Omnicom, Forbes, Cannes, figures) confirmed absent from AD-MARKETING-1 AR and EN.

---

#### Ad Set META-AS-09: Retargeting, class-page and plans-page visitors

- Ad set name: 2026-07-snp_meta_retargeting_page-visitors
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration then Purchase (per phase).
- Audience:
  - Custom audience 1: class-page visitors (any of the seven cleared instructor class pages
    on maharat.com) in the last 30 days, who did not complete the signup gate.
    Requires pixel PageView event confirmed firing on class page URLs.
  - Custom audience 2: plans-page visitors (maharat.com plans pages, Arabic and English
    versions) in the last 30 days, who did not subscribe.
  - Exclusion: current paying subscribers (hashed list upload, blocked pending PDPL consent
    and residency confirmation, open item 10).
  - Exclusion: owned non-payers in the lifecycle email or push flow (hashed list suppression,
    blocked pending PDPL confirmation and suppression source confirmation, open item 11).
  - Geo: GCC guardrail (audience is pre-qualified).
  - Age: 18 to 45.
- Placement: Advantage+ placements (Instagram Feed and Stories prioritized for retargeting).
- Budget: [PLACEHOLDER.]
- Schedule: Activate from approximately day 3 onward once pixel pools build.
  [PLACEHOLDER end date, proposed 2026-08-31.]
- Frequency cap: up to 5 impressions per person per day (retargeting audience, modestly higher
  than prospecting cap per media-plan-package section 3.1).
- Status: PAUSED. Additional block: pixel pools must accumulate before this ad set can deliver.
  Pixel firing is blocked pending tracking-plan confirmation and production deployment (open
  item 13). Hashed-list exclusions are blocked pending PDPL clearance (open items 10 and 11).

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-09-AD-01 | C5 breadth field-grid retargeting (no photography) | AB6, 1080x1350 | AD-RETARGET-1 primary text and headline | AD-RETARGET-1 EN body and headline | Continue / أكمل الآن |
| META-AS-09-AD-02 | C4 abstract free-entry re-engagement (no photography) | AB4, 1080x1350 | AD-RETARGET-1 primary text and headline | AD-RETARGET-1 EN body and headline | Continue / أكمل الآن |

Note: AD-RETARGET-1 CTA lands on the class or plans page and may route through the signup gate.
Gate-landing destination is blocked until gate_platform is confirmed (open item 4).
No field name is specified in this copy, reassuring across the breadth as noted in
copy-package.ar section 1 retargeting note.

---

#### Ad Set META-AS-10: Retargeting, masterclass intro video players (25 percent threshold)

- Ad set name: 2026-07-snp_meta_retargeting_video-players-25pct
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration then Purchase.
- Audience:
  - Video engagement custom audience: users who watched 25 percent or more of any chapter 1
    free intro video on-site or via Meta video placements (any of the seven instructor fields).
  - Exclusion: users who watched 75 percent or more (handled separately in META-AS-11 with a
    closer message).
  - Exclusion: current paying subscribers. Same PDPL block applies.
  - Geo: GCC guardrail.
  - Age: 18 to 45.
- Placement: Advantage+ placements.
- Budget: [PLACEHOLDER.]
- Schedule: Activate from approximately day 3 onward once video view pools build.
  [PLACEHOLDER end date.]
- Frequency cap: 5 impressions per person per day.
- Status: PAUSED. Pixel and video-view custom audience construction blocked pending tracking
  confirmation (open item 13).

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-10-AD-01 | C5 breadth field-grid retargeting | AB6, 1080x1080 | AD-RETARGET-1 primary text and headline | AD-RETARGET-1 EN body and headline | Continue / أكمل الآن |

---

#### Ad Set META-AS-11: Retargeting, masterclass intro video players (75 percent threshold)

- Ad set name: 2026-07-snp_meta_retargeting_video-players-75pct
- Campaign: META-CAMP-01
- Optimization event: CompleteRegistration then Purchase.
- Audience:
  - Video engagement custom audience: users who watched 75 percent or more of any intro video.
  - Exclusion: current paying subscribers.
  - Geo: GCC guardrail. Age: 18 to 45.
- Placement: Advantage+ placements (Instagram Feed and Stories prioritized).
- Budget: [PLACEHOLDER.]
- Schedule: Activate from approximately day 4 once pools build. [PLACEHOLDER end date.]
- Frequency cap: 5 impressions per person per day.
- Status: PAUSED. Same tracking dependency as META-AS-10.

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant | CTA |
|---|---|---|---|---|---|
| META-AS-11-AD-01 | C4 abstract free-entry re-engagement | AB4 crop, 1080x1350 | AD-RETARGET-1 primary text and headline | AD-RETARGET-1 EN body and headline | Start Now / ابدأ الآن |

---

#### Lookalike audiences (staged, activation blocked pending PDPL clearance)

Both lookalike audiences are staged as audience definitions only. Neither can be uploaded or
activated until compliance-privacy-reviewer confirms Saudi PDPL consent basis and data-residency
requirements are met (open item 10).

- Lookalike-01: Lookalike of existing Maharat paid subscribers (1 percent similarity, Saudi
  Arabia geo). Source audience requires consent basis review before construction or upload.
  Ad sets that will use this lookalike: META-AS-01 (broad platform interest, phase 2 expansion).
  Activation: phase 2, after seed size is sufficient and PDPL clearance is confirmed.

- Lookalike-02: Lookalike of signup-gate completers (email or WhatsApp captured), once gate
  is live and has accumulated a minimum 100 contacts (ideally 1,000 seed). This is the
  highest-value lookalike for the subscription conversion objective. Same PDPL caveat.
  Gate platform is OPEN ITEM; this lookalike cannot be constructed until the gate is live.
  Activation: phase 2 minimum, conditional on gate platform confirmation and seed accumulation.

---

## 2. Campaign structure: TikTok (upper funnel, visual fields)

Platform: TikTok Ads Manager
Objective: Phase 1 video views (awareness and seeding); Phase 2 conversions if pixel volume
supports it and gate platform is confirmed.
Status: ALL STAGED PAUSED.

### 2.1 Campaign TIKTOK-CAMP-01

- Campaign name: 2026-07-snp_tiktok_reach-video
- Objective: Video Views (phase 1). Switch to Conversions in phase 2 if TikTok Pixel has
  accumulated at least 30 gate or subscription events and the gate platform is confirmed.
- Campaign budget: [PLACEHOLDER. TikTok receives 18 percent of total confirmed budget.
  No absolute figure staged.]
- Bid strategy phase 1: Maximize video views, CPV bidding.
- Status: PAUSED

---

#### Ad Set TIKTOK-AS-01: Prospecting, makeup and beauty (visual field)

- Ad set name: 2026-07-snp_tiktok_prospecting_makeup
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views.
- Audience: interests in makeup, beauty, cosmetics, skincare, GRWM content. GCC geo, Saudi
  Arabia primary. Age 18 to 28 (TikTok-specific age band per media-plan-package section 3.2).
  Arabic language.
- Placement: TikTok In-Feed.
- Budget: [PLACEHOLDER. Phase 1 weighted share of TikTok 18 percent allocation.]
- Schedule: Phase 1 only (proposed approximately first 3 weeks). Reduce to retargeting only
  in phase 2. [PLACEHOLDER dates.]
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| TIKTOK-AS-01-AD-01 | C2 per-field abstract card, makeup variant, vertical 9:16 | AB2, 1080x1920 | AD-MAKEUP-1 text overlay (feminine address) | AD-MAKEUP-1 EN overlay |
| TIKTOK-AS-01-AD-02 | C6 multi-field breadth reel, 15s cut (BLOCKED pending footage) | AB8, 15s cut, 1080x1920 | AD-BREADTH-1 end-card overlay | AD-BREADTH-1 EN end-card overlay |

Note on TIKTOK-AS-01-AD-02: blocked pending rights-cleared footage (open item 7). C2 variant
(AD-01) is the launchable fallback.

---

#### Ad Set TIKTOK-AS-02: Prospecting, cooking and food (visual field)

- Ad set name: 2026-07-snp_tiktok_prospecting_cooking
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views.
- Audience: interests in cooking tutorials, recipes, food content, Arabic cuisine. GCC geo,
  Saudi Arabia primary. Age 18 to 28.
- Placement: TikTok In-Feed.
- Budget: [PLACEHOLDER.]
- Schedule: Phase 1 only. [PLACEHOLDER dates.]
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| TIKTOK-AS-02-AD-01 | C2 per-field abstract card, cooking variant, vertical 9:16 | AB2, 1080x1920 | AD-COOK-1 text overlay | AD-COOK-1 EN overlay |

---

#### Ad Set TIKTOK-AS-03: Prospecting, music and performance (visual field)

- Ad set name: 2026-07-snp_tiktok_prospecting_music
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views.
- Audience: interests in Arabic music, singing, musical performances. GCC geo, Saudi Arabia
  primary. Age 18 to 28.
- Placement: TikTok In-Feed.
- Budget: [PLACEHOLDER.]
- Schedule: Phase 1 only. [PLACEHOLDER dates.]
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| TIKTOK-AS-03-AD-01 | C2 per-field abstract card, music variant, vertical 9:16 | AB2, 1080x1920 | AD-MUSIC-1 text overlay | AD-MUSIC-1 EN overlay |

---

#### Ad Set TIKTOK-AS-04: Prospecting, styling and fashion (visual field)

- Ad set name: 2026-07-snp_tiktok_prospecting_styling
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views.
- Audience: interests in fashion, outfits, styling content. GCC geo, Saudi Arabia primary.
  Age 18 to 28.
- Placement: TikTok In-Feed.
- Budget: [PLACEHOLDER.]
- Schedule: Phase 1 only. [PLACEHOLDER dates.]
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| TIKTOK-AS-04-AD-01 | C2 per-field abstract card, styling variant, vertical 9:16 | AB2, 1080x1920 | AD-STYLING-1 text overlay (feminine address) | AD-STYLING-1 EN overlay |

---

#### Ad Set TIKTOK-AS-05: Retargeting, TikTok video engagers (50 percent threshold)

- Ad set name: 2026-07-snp_tiktok_retargeting_video-engagers
- Campaign: TIKTOK-CAMP-01
- Objective: Video Views (phase 1). Conversions (phase 2 if pixel supports it, gate platform
  confirmed, and minimum 1,000 users in pool per field).
- Audience: TikTok users who watched 50 percent or more of any TikTok ad or organic content
  in this campaign. Exclusion: current subscribers (hashed email list, PDPL block applies).
  Geo: GCC guardrail. Age: 18 to 35.
- Placement: TikTok In-Feed. Creative duration: under 15 seconds per media-plan spec.
- Budget: [PLACEHOLDER.]
- Schedule: Activate from approximately day 10 onward once phase 1 pools build.
  If pool per field is below 1,000 users after phase 1, this ad set remains paused and the
  TikTok budget folds into the reserve per media-plan-package trigger 3. [PLACEHOLDER end date.]
- Status: PAUSED

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| TIKTOK-AS-05-AD-01 | C4 abstract free-entry re-engagement, under 15s, vertical | AB4 motion, 1080x1920 | AD-RETARGET-1 text overlay | AD-RETARGET-1 EN overlay |

Note: CTA lands on the class or plans page. Gate-landing destination blocked until gate
platform confirmed (open item 4).

---

## 3. Campaign structure: Google Search (precision, high-intent)

Platform: Google Ads
Objective: Clicks (phase 1). Target CPA (phase 2 if 30-plus conversions within 30 days).
Status: ALL STAGED PAUSED.
Note: final keyword set to be reviewed with seo-specialist before staging (open item 12).

### 3.1 Campaign GOOGLE-CAMP-01

- Campaign name: 2026-07-snp_google_search
- Campaign type: Search.
- Objective: Conversions (subscription_start, wired via Google Ads conversion tag or imported
  from GA4 purchase goal once tracking-plan is confirmed).
- Budget: [PLACEHOLDER. Google Search receives 17 percent of total confirmed budget.]
- Bid strategy phase 1: Maximize clicks. Transition to Target CPA in phase 2 once 30 or more
  conversion events accumulate within 30 days. Target CPA value is OPEN ITEM; blank until
  Ahmed confirms.
- Networks: Search only. Exclude Display Network and Search Partners initially.
- Geo: Saudi Arabia (primary). GCC expansion after Saudi data validates.
- Language: Arabic (primary), English (secondary).
- Status: PAUSED

---

#### Ad Group GOOGLE-AG-01: Brand keyword group

- Ad group name: 2026-07-snp_google_brand
- Keywords (illustrative, confirm with seo-specialist per open item 12):
  - [مهارات] (exact, AR)
  - "maharat" (exact, EN)
  - "maharat.com" (exact)
  - [راغب علامة مهارات] (phrase, AR)
  - "ragheb alama maharat" (phrase)
  - [سلام دقاق مهارات] (phrase, AR)
  - [بسام فتوح مهارات] (phrase, AR)
  - [توفيق كريديه مهارات] (phrase, AR)
  - [قصي خولي مهارات] (phrase, AR)
  - [سيدريك حداد مهارات] (phrase, AR)
  - [إلدا شقير مهارات] (phrase, AR)
  Each instructor name pair (AR and EN) in phrase and exact match.
  All seven names are confirm-at-gate per open item 8.
- Bid priority: highest in the plan. These queries signal explicit brand and instructor intent.
- Status: PAUSED

Responsive Search Ad for GOOGLE-AG-01:
- Ad name: GOOGLE-AG-01-AD-01
- Headline 1 (pinned): Summer of Skills on Maharat (EN) / صيف المهارات مع مهارات (AR)
- Headline 2: Seven Fields. Regional Experts. (EN) / سبعة مجالات. نخبة العرب. (AR)
- Headline 3: Start Your Free First Lesson (EN) / ابدأ درسك الأول مجاناً (AR)
- Description 1: Choose music, cooking, acting, makeup, business, styling, or marketing.
  Learn from the person who set the standard in your field. First lesson free.
- Description 2: One Maharat subscription opens every field and every masterclass.
  Pick yours this summer.
- Final URL: maharat.com Summer of Skills landing page or homepage (confirm URL at build)
- UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
  utm_content=brand, utm_term={keyword}
- Status: PAUSED

---

#### Ad Group GOOGLE-AG-02: Field-learning intent, music

- Ad group name: 2026-07-snp_google_field-music
- Keywords (illustrative from media-plan-package section 3.3, confirm with seo-specialist):
  - "تعلم الموسيقى" (exact and phrase, AR)
  - "دورة غناء" (phrase, AR)
  - "learn music Arabic" (phrase)
  - "singing course online" (phrase)
- Match types: phrase and exact. Monitor for irrelevant traffic; build negatives quickly.
- Status: PAUSED

RSA for GOOGLE-AG-02: fills AD-MUSIC-1 EN headline as headline 1, "Start the free lesson"
as headline 3. Description: 40 years in music, now teaching on Maharat. First lesson free.
Final URL: Ragheb Alama class page on maharat.com.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=music, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-03: Field-learning intent, cooking

- Ad group name: 2026-07-snp_google_field-cooking
- Keywords (illustrative): "تعلم الطبخ" (exact and phrase), "دورة طبخ" (phrase),
  "cooking course Arabic" (phrase), "learn Levantine cooking" (phrase).
- Match types: phrase and exact.
- Status: PAUSED

RSA: fills AD-COOK-1 EN headline. Description: Best Female Chef in MENA, teaching on Maharat.
First lesson free. Final URL: Salam Dakkak class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=cooking, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-04: Field-learning intent, acting

- Ad group name: 2026-07-snp_google_field-acting
- Keywords (illustrative): "تعلم التمثيل" (exact and phrase), "دورة تمثيل" (phrase),
  "acting course Arabic" (phrase).
- Match types: phrase and exact.
- Status: PAUSED

RSA: fills AD-ACTING-1 EN headline. Description: One of the Arab world's biggest names in
acting, teaching on Maharat. First lesson free. Final URL: Kosai Khauli class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=acting, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-05: Field-learning intent, makeup

- Ad group name: 2026-07-snp_google_field-makeup
- Keywords (illustrative): "تعلم المكياج" (exact and phrase), "دورة مكياج" (phrase),
  "makeup course Arabic" (phrase).
- Match types: phrase and exact.
- Status: PAUSED

RSA: fills AD-MAKEUP-1 EN headline. Description: One of the region's most sought-after makeup
artists, teaching on Maharat. First lesson free. Final URL: Bassam Fattouh class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=makeup, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-06: Field-learning intent, business

- Ad group name: 2026-07-snp_google_field-business
- Keywords (illustrative): "ريادة الأعمال" (phrase), "دورة أعمال" (phrase),
  "business course Arabic" (phrase), "entrepreneurship course" (phrase).
- Match types: phrase and exact.
  Note: Brands For Less and garage detail are verify-before-public-use; excluded from all
  keywords and ad copy (open item 9).
- Status: PAUSED

RSA: fills AD-BUSINESS-1 EN headline. Description: Built a billion-dollar business from
scratch. Now teaching on Maharat. First lesson free. Final URL: Toufic Kreidieh class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=business, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-07: Field-learning intent, styling

- Ad group name: 2026-07-snp_google_field-styling
- Keywords (illustrative): "مهارة الستايل" (phrase), "تعلم الأزياء" (phrase),
  "styling course Arabic" (phrase).
- Match types: phrase and exact.
- Status: PAUSED

RSA: fills AD-STYLING-1 EN headline as headline 1 ("Personal style is a skill. Learn it from
the Arab world's most trusted celebrity stylist."), "Start the free lesson" as headline 3.
Description: Celebrity stylist trusted by the Arab world's biggest stars, teaching on Maharat.
First lesson free. Final URL: Cedric Haddad class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=styling, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-08: Field-learning intent, marketing

- Ad group name: 2026-07-snp_google_field-marketing
- Keywords (illustrative): "تعلم التسويق" (exact and phrase), "دورة تسويق" (phrase),
  "marketing course Arabic" (phrase).
- Match types: phrase and exact.
  Note: Omnicom, Forbes, Cannes, and numerical figures are verify-before-public-use; excluded
  (open item 9).
- Status: PAUSED

RSA: fills AD-MARKETING-1 EN headline as headline 1 ("Learn marketing from one of the Arab
world's most respected leaders in the field."), "Start the free lesson" as headline 3.
Description: One of the Arab world's most respected marketing leaders, teaching on Maharat.
First lesson free. Final URL: Elda Choucair class page.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=marketing, utm_term={keyword}
Status: PAUSED. Instructor name confirm-at-gate.

---

#### Ad Group GOOGLE-AG-09: Self-development and online learning intent (observation layer)

- Ad group name: 2026-07-snp_google_selfdevelopment-observe
- Keywords (illustrative): "online courses Arabic" (phrase), "self-development platform"
  (phrase), "تعلم مهارة جديدة" (phrase), "منصة تعليمية" (phrase).
- Match types: phrase and broad (observation only). Promote to active bidding after two weeks
  if CPC and conversion rate support it.
- Status: PAUSED

RSA: fills AD-BREADTH-1 EN headline. Description: Summer of Skills on Maharat. Seven fields,
regional experts, one subscription. First lesson free across every field.
UTMs: utm_source=google, utm_medium=paid_search, utm_campaign=2026-07-summer-nonpayer,
utm_content=breadth, utm_term={keyword}
Status: PAUSED.

Negative keyword list (build in Google Ads before launch, applies across all search ad groups):
courses for sale (free), products for purchase (brushes, cosmetics, instruments, clothing
items), services for hire (makeup artist hire, chef catering, stylist hire, acting agent),
competitor brand names, entertainment-only queries with no learning intent.
Final negative list to be confirmed with seo-specialist (open item 12).

In-market audience overlay: apply "online education" and "self-improvement" in-market audience
overlay across all ad groups to improve bid efficiency and Quality Score.

---

## 4. Campaign structure: YouTube (mid-funnel video, conditional)

Platform: Google Ads (Video campaign type)
Objective: Awareness and video views (CPV bidding), phase 2 and phase 3.
Status: ALL STAGED PAUSED. Conditional block: YouTube allocation is blocked until
rights-cleared trailer or instructor footage is confirmed (open item 7). If no cleared asset
exists at the proposed launch date, YOUTUBE-CAMP-01 remains paused and the 12 percent YouTube
budget share moves to reserve. Human-gate decision required.

### 4.1 Campaign YOUTUBE-CAMP-01

- Campaign name: 2026-07-snp_youtube_video-awareness
- Campaign type: Video (In-Stream skippable, 15 to 30 seconds).
- Objective: Awareness and reach. CPV bidding.
- Budget: [PLACEHOLDER. YouTube receives 12 percent of total confirmed budget, conditional
  on cleared asset. If asset not confirmed at launch, this moves to reserve. No absolute
  figure staged.]
- Bid strategy: Target CPV.
- Status: PAUSED. ASSET BLOCK: AB8 (C6 multi-field breadth reel, rights-cleared footage from
  at least 3 fields) must be confirmed before this campaign can be activated. Fallback: C4
  motion (AB4) per individual field, but C4 is not a YouTube pre-roll substitute; if C6 is
  blocked and no other footage exists, YouTube budget moves to reserve per media-plan-package
  trigger 7.

---

#### Ad Group YOUTUBE-AG-01: Interest and in-market targeting, phase 2 and phase 3

- Ad group name: 2026-07-snp_youtube_instream_selfdevelopment-beauty-business
- Campaign: YOUTUBE-CAMP-01
- Audience targeting:
  - In-market: online education, self-improvement, professional development.
  - Interest: beauty and lifestyle (for makeup, cooking, styling field segments), music and
    entertainment (for music and acting segments), business and entrepreneurship (for business
    and marketing segments).
  - Keyword targeting: YouTube channels and videos in the Arabic self-development, beauty
    tutorial, and cooking tutorial space.
  - Custom intent audience: built from Google Search field-learning intent keyword groups
    (GOOGLE-AG-02 through GOOGLE-AG-08), targeting users who have searched those queries.
  - Remarketing: users who visited any Maharat class page or the plans page. Requires YouTube
    remarketing tag placement confirmed by data-tracking-engineer (open item 13).
- Geo: Saudi Arabia primary, GCC.
- Language: Arabic.
- Status: PAUSED. Asset block applies.

| Ad name | Creative concept | Asset brief | AR copy variant | EN copy variant |
|---|---|---|---|---|
| YOUTUBE-AG-01-AD-01 | C6 multi-field breadth reel, 15s cut (BLOCKED) | AB8, 15s cut, 1920x1080 | AD-BREADTH-1 end-card and companion banner | AD-BREADTH-1 EN end-card and companion banner |
| YOUTUBE-AG-01-AD-02 | C6 multi-field breadth reel, 30s master (BLOCKED) | AB8, 30s master, 1920x1080 | AD-BREADTH-1 end-card overlay | AD-BREADTH-1 EN end-card overlay |

UTMs on companion click-through URLs:
utm_source=youtube, utm_medium=paid_video, utm_campaign=2026-07-summer-nonpayer,
utm_content=breadth

Note: overlay copy on end cards uses AD-BREADTH-1 headline and CTA. Full primary text body
copy does not appear in the in-stream format; it populates the companion banner and video
description only. No instructor name in the breadth end card; field labels appear as overlay
slots from AB8 asset brief.

---

## 5. Tracking wiring (plan-level; not yet confirmed deployed)

Source: media-plan-package section 7 (UTM direction). Tracking-plan from data-tracking-engineer
has not been received. This section describes the intended tracking plan as drawn from the
media-plan. None of these tracking elements are live or deployed. Production deployment of any
tracking code is a human-gate action and a go-live prerequisite (open item 13).

### 5.1 Meta Pixel and CAPI (intended plan)

Events to be wired to all Meta campaigns once tracking-plan is confirmed:
- PageView: fires on class page load (each of the seven cleared instructor class pages) and
  on the plans page. Linked to all Meta campaigns as a first-touch signal.
- ViewContent (gate_view): fires when the signup gate renders. Linked to all prospecting ad
  sets as a mid-funnel signal.
- Lead (submit): fires on gate form submission.
- CompleteRegistration (confirm): fires on server confirmation of gate submission. This is the
  primary optimization event for all phase 1 prospecting ad sets. CAPI preferred for this event.
  Blocked: gate_platform OPEN ITEM (open item 4); CAPI wiring for gate-side events is blocked
  until platform is confirmed and PDPL data-residency is cleared (open item 10).
- Purchase (subscription_start): fires on subscription purchase confirmation. This is the
  primary conversion event for phase 2 optimization. CAPI preferred.
- Deduplication: event_id (UUID v4, server-generated) applied to CompleteRegistration and
  Purchase on both Pixel and CAPI calls. Any mismatch is a hard stop before go-live.

### 5.2 TikTok Pixel (intended plan)

Events to be wired once tracking-plan is confirmed:
- ViewContent on class page.
- CompletePayment (TikTok equivalent of Purchase) on subscription_start for phase 2.
- TikTok Pixel placement on maharat.com: planned, not deployed. Blocked on compliance-
  privacy-check and production deployment (open item 13).

### 5.3 Google Ads conversion tracking (intended plan)

- Conversion action: subscription_start, imported from GA4 purchase event (campaign_id
  parameter match) or via Google Ads conversion tag on the order confirmation page.
- Target CPA field: OPEN ITEM. Blank until Ahmed confirms (open item 2).

### 5.4 YouTube remarketing tag (intended plan)

- YouTube remarketing tag placement on maharat.com class pages and plans page: planned,
  not confirmed deployed. Required for YOUTUBE-AG-01 remarketing audience.
- Blocked pending tracking-plan confirmation (open item 13).

### 5.5 UTM structure (applies to all channels, all ad final URLs)

Per media-plan-package section 7. No personal data in any UTM field.

| Channel | utm_source | utm_medium | utm_campaign | utm_content | utm_term |
|---|---|---|---|---|---|
| Meta and Instagram | meta | paid_social | 2026-07-summer-nonpayer | [field]-prospecting or [field]-retargeting | (none) |
| TikTok | tiktok | paid_social | 2026-07-summer-nonpayer | [field]-video or retargeting | (none) |
| Google Search | google | paid_search | 2026-07-summer-nonpayer | [field] or brand or breadth | {keyword} |
| YouTube | youtube | paid_video | 2026-07-summer-nonpayer | breadth | (none) |

Field codes for utm_content: breadth, music, cooking, acting, makeup, business, styling,
marketing, retargeting. No user identifier, email, phone, or personal attribute in any UTM
field. This is a hard rule from CLAUDE.md.

### 5.6 Audience suppression (blocked pending compliance clearance)

- Suppression 1: current paying subscribers. Hashed email list upload to Meta, TikTok, and
  YouTube custom audiences. Blocked pending PDPL consent and residency confirmation (open
  item 10).
- Suppression 2: owned non-payers already in the lifecycle email or app-push flow.
  Hashed list match between CRM and Meta, TikTok, YouTube custom audiences. Same PDPL block.
  Source list not yet confirmed (open item 11).
- Gate completers who have already subscribed: suppress from retargeting once gate is live.
  Gate platform OPEN ITEM (open item 4).

---

## 6. Naming convention

All campaign, ad set, and ad names follow the convention:
{abbreviated_campaign_id}_{platform}_{objective}_{audience-descriptor}

Campaign ID abbreviation: snp (summer-nonpayer)

Examples from the structure above:
- 2026-07-snp_meta_prospecting_breadth
- 2026-07-snp_meta_prospecting_music
- 2026-07-snp_meta_retargeting_page-visitors
- 2026-07-snp_tiktok_prospecting_makeup
- 2026-07-snp_google_brand
- 2026-07-snp_google_field-cooking
- 2026-07-snp_youtube_instream_selfdevelopment-beauty-business

No em dashes in any campaign name, ad set name, ad name, UTM value, or naming convention
field. Western numerals only throughout.

---

## 7. Budget allocation structure (proportional only; absolute amounts are open items)

These proportions trace directly to media-plan-package section 2. No absolute figures are
stated here. The brief has no confirmed budget. Ahmed fills every budget field before go-live.

| Channel | Campaign | Overall share | Phase 1 (approximately weeks 1 to 3) | Phase 2 (approximately weeks 4 to 6) | Phase 3 (approximately weeks 7 to 8) |
|---|---|---|---|---|---|
| Meta and Instagram | META-CAMP-01 | 45 percent | Prospecting-heavy, all 7 field interest sets | Shift toward best-performing fields and retargeting | Retargeting primary, cold prospecting on 2 to 3 best fields only |
| TikTok | TIKTOK-CAMP-01 | 18 percent | Reach and video seeding, 4 visual fields | Reduced; retargeting only if pool is active | Minimal or paused depending on pool size |
| Google Search | GOOGLE-CAMP-01 | 17 percent | Steady, all 7 field groups plus brand | Steady, tighten to converting groups | Steady |
| YouTube | YOUTUBE-CAMP-01 | 12 percent | Conditional on footage asset | Increased if asset confirmed and CPV efficient | Hold or reduce |
| Reserve | n/a (held by Ahmed) | 8 percent | Held | Released after phase 1 readout to best performer, human-gate decision | Residual reserve |
| TOTAL | | 100 percent | | | |

Notes on the shape:
- Meta at 45 percent: primary conversion engine, highest audience density in GCC, 7 parallel
  field-based interest ad sets for per-field testing, strongest retargeting capability once
  pixel and CAPI are confirmed.
- TikTok at 18 percent: awareness and seeding, front-loaded to phase 1, drops materially in
  phase 2. If retargeting pool per field is below 1,000 users after phase 1, TikTok budget
  share folds into reserve per media-plan-package trigger 3.
- Google Search at 17 percent: steady precision layer. Brand keyword group (cleared
  instructor names) is the priority subgroup.
- YouTube at 12 percent: conditional on C6 footage asset. If no cleared asset at launch, this
  moves to reserve and reserve becomes 20 percent. Human gate decides per media-plan-package
  trigger 7.
- Reserve at 8 percent: held through phase 1. Released to the channel with the lowest cost per
  signup-gate completion after the first performance readout from analytics-reporter. Release
  is a human-gate proposal, not an autonomous action.

---

## 8. Pre-launch checklist

Each item is checked against the inputs and structure in this package. A blocked item is a
go-live blocker for the affected channels or the whole structure as noted.

| Check | Status | Notes |
|---|---|---|
| Pixel firing confirmed on class pages and plans page | BLOCKED | Tracking-plan from data-tracking-engineer not received. Production pixel deployment not confirmed. Blocks all pixel-based custom audiences, retargeting pools, and conversion optimization events on all platforms. Hard go-live blocker for retargeting and phase 2 optimization. |
| CAPI endpoint wired for gate events | BLOCKED | Gate platform OPEN ITEM (open item 4). Saudi PDPL data-residency decision pending (open item 10). Hard go-live blocker for gate-conversion optimization. |
| YouTube remarketing tag confirmed on maharat.com | BLOCKED | Not confirmed deployed. Blocks YOUTUBE-AG-01 remarketing audience and YOUTUBE-CAMP-01 remarking layer. |
| UTMs consistent across all ad final URLs | PASS (plan) | UTM structure mapped in section 5.5 and section 6. Non-identifying values, consistent with media-plan-package section 7 direction. Confirm at build that every final URL carries the correct parameters. |
| Naming convention applied throughout | PASS (plan) | All campaign, ad set, and ad names follow the convention in section 6. No em dashes in any name. Western numerals only. |
| Budget fields set from confirmed brief | BLOCKED | Budget is OPEN ITEM. All budget fields are placeholders throughout. Ahmed fills them before go-live. Hard blocker on all spend across all channels. |
| End dates set on all campaigns | BLOCKED | Schedule is ASSUMPTION (proposed 2026-08-31). Ahmed confirms. Until confirmed, no end date is staged. Hard blocker. |
| Start dates set on all campaigns | BLOCKED | Schedule is ASSUMPTION (proposed 2026-07-01). Ahmed confirms. Hard blocker. |
| All campaigns and ad sets staged as PAUSED | PASS | Every campaign, ad set, and ad in this package is marked PAUSED. Nothing activates without Ahmed's explicit go-live action. |
| No personal data in any UTM parameter or tracking call | PASS (plan) | Confirmed: no email, phone, name, or user ID in any UTM field or event parameter. CLAUDE.md guardrail satisfied. |
| Rights-cleared instructor photography confirmed per instructor | BLOCKED (per instructor) | C3 (AB3) variants for all seven instructors are blocked. C2 abstract fallback (AB2) is launchable for all seven fields. Blocked C3 variants are staged paused within paused ad sets. Not a full go-live blocker; C2 fallbacks can launch. |
| Rights-cleared footage confirmed for YouTube and C6 | BLOCKED | C6 (AB8) blocked. YOUTUBE-CAMP-01 conditionally blocked. 12 percent YouTube budget share moves to reserve if no cleared asset at launch. Human-gate decision required. |
| Gate platform confirmed | BLOCKED | Email and WhatsApp capture platform vendor unconfirmed (open item 4). All gate-landing CTAs in retargeting ad sets blocked. CAPI wiring blocked. Meta and TikTok retargeting custom audiences built from gate-completer lists cannot be activated. |
| Saudi PDPL consent and data-residency confirmed | BLOCKED | Compliance-privacy-reviewer has not cleared retargeting audiences, hashed list uploads, CAPI hashed signals, or data-residency posture (open item 10). All retargeting ad sets, subscriber suppression uploads, and gate-side CAPI calls are blocked until cleared. Hard blocker for retargeting. |
| Owned non-payer suppression list confirmed and uploaded | BLOCKED | Suppression of owned non-payers from paid prospecting requires hashed list match. Source list not confirmed. Same PDPL block (open item 11). |
| Exclusion audience (current subscribers) uploaded | BLOCKED | Hashed list upload blocked pending PDPL clearance (open item 10). Prospecting ad sets must not serve existing subscribers. |
| Upstream QA gates passed (creative, copy AR, copy EN) | BLOCKED | All upstream packages at status draft. None have cleared arabic-copy-qa, english-copy-qa, brand-qa-reviewer, or compliance-privacy-check. Comprehensive go-live blocker for all ad copy and creative across all channels. |
| Tracking-plan from data-tracking-engineer received and confirmed | BLOCKED | Tracking-plan has not arrived at this build stage (open item 13). Pixel firing, CAPI wiring, Google Ads conversion tag, YouTube remarketing tag, and per-field UTM content structure cannot be finalized until the tracking-plan is delivered and confirmed. |
| Google Search keywords reviewed with seo-specialist | BLOCKED | Final keyword set not yet confirmed with seo-specialist (open item 12). Google campaign can be staged but not launched until keyword list is reviewed and negatives are confirmed. |
| Styling and marketing field copy variants authored | PASS | AD-STYLING-1 (Cedric Haddad, AR and EN) and AD-MARKETING-1 (Elda Choucair, AR and EN) authored and QA-passed (arabic-copy-qa 2026-06-12, english-copy-qa 2026-06-12). Placeholder copy removed. META-AS-07, META-AS-08, TIKTOK-AS-04, GOOGLE-AG-07, and GOOGLE-AG-08 now reference the QA-passed variants. Remaining blockers on these ad sets are the standing open items: budget+currency, gate platform, tracking, PDPL, rights-cleared photography (C3 portrait variants only). |
| Target CPA staged in bid settings | BLOCKED | Target CPA is OPEN ITEM (open item 2). Cost-cap and Target CPA bid values are not staged. Meta and Google phase 2 bid transitions cannot be configured until Ahmed confirms the target. |
| No accreditation claim in any in-platform copy | PASS | Reviewed all copy variants mapped in this package (AD-BREADTH-1, AD-MUSIC-1, AD-COOK-1, AD-MAKEUP-1, AD-BUSINESS-1, AD-ACTING-1, AD-RETARGET-1, AR and EN). No certificate, accreditation, or qualification claim present in any variant. |
| No em dash in any in-platform copy | PASS | Reviewed: no em dash in any copy variant staged in this package. No em dash in any campaign or ad set name. |
| Western numerals in all in-platform copy | PASS | Confirmed: the only digit that appears in mapped copy variants is 40 (Ragheb Alama's years in music, in AD-MUSIC-1 and the EN equivalent). Western numeral confirmed. No Eastern Arabic-Indic digits anywhere. |
| No invented price, promo, or plan length in any copy | PASS | No price stated in any copy variant. No promotional offer invented or implied. No plan length stated. Brief marks all three as ASSUMPTION. |
| Empowering framing, not deficit-framed | PASS | All mapped copy variants lead with what the reader can build and choose. Retargeting copy (AD-RETARGET-1) invites completion without shame framing. |
| Instructor naming discipline applied | PASS (plan) | Seven nameable instructors are mapped to their respective ad sets with confirm-at-gate notation. The four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam) do not appear anywhere in this package. Verify-before-public-use facts excluded from all copy variants. |
| Per-field reporting dimension in UTM content field | PASS (plan) | utm_content carries field codes (music, cooking, acting, makeup, business, styling, marketing, breadth, retargeting) consistent with media-plan-package section 7 requirement for per-field cost reporting by analytics-reporter. |

Summary: 9 items pass at plan level. 15 items are blocked. The most critical blockers are:
budget (blocks all spend), upstream QA gates (blocks all copy and creative), tracking-plan not
received (blocks all pixel-based conversion and retargeting), PDPL clearance (blocks all
hashed-list uploads and retargeting activation), gate platform (blocks gate-CTA ads and CAPI),
and schedule (blocks all campaign date fields). The styling and marketing copy variant blocker
is resolved: AD-STYLING-1 and AD-MARKETING-1 authored and QA-passed.

---

## 9. Open items (all surfaced, none buried)

Each item below is a discrete decision or action for Ahmed or the named owner. Silence is not
approval.

| # | Item | Blocks | Owner |
|---|---|---|---|
| 1 | Budget and currency: OPEN ITEM. No budget or currency confirmed. All budget fields are placeholders. | All spend across all channels and all phases. Hard blocker. | Ahmed (brief) |
| 2 | Target CPA or ROAS: ASSUMPTION. Not confirmed. Cost-cap and Target CPA bid settings are blank. | Phase 2 and phase 3 bid strategy on Meta and Google. Efficiency read only until confirmed. | Ahmed (brief) |
| 3 | Schedule (start and end dates): ASSUMPTION. Proposed 2026-07-01 to 2026-08-31. Confirm. | All campaign date fields, ad set scheduling, phase transitions. Hard blocker. | Ahmed (brief) |
| 4 | Gate platform: OPEN ITEM. Email and WhatsApp signup-gate platform vendor unconfirmed. | All gate-landing CTAs, gate-side CAPI wiring, gate-completer custom audience construction, retargeting ad sets META-AS-09, META-AS-10, META-AS-11, TIKTOK-AS-05. | Ahmed (platform decision) |
| 5 | Upstream QA gates: creative-package, copy-package.ar, copy-package.en all at status draft. No upstream package has cleared arabic-copy-qa, english-copy-qa, brand-qa-reviewer, or compliance-privacy-check. | All ad copy and creative variants. Nothing goes live until upstream packages reach at least qa-passed. | QA pipeline (orchestrator to route) |
| 6 | Rights-cleared instructor photography per instructor (all seven): OPEN ITEM. C3 (AB3) variants blocked per instructor. | Ad variants: META-AS-02-AD-02, META-AS-03-AD-02, META-AS-04-AD-02, META-AS-05-AD-02, META-AS-06-AD-02, META-AS-07-AD-02, META-AS-08-AD-02. C2 abstract fallback is launchable for all seven. Not a full go-live blocker. | Ahmed (asset confirmation per instructor) |
| 7 | Rights-cleared footage (multi-field, minimum 3 fields) for C6 (AB8) and YouTube: OPEN ITEM. | YOUTUBE-CAMP-01 (full conditional block), TIKTOK-AS-01-AD-02. 12 percent YouTube budget share moves to reserve if no cleared asset. Human gate decides: hold or fold into Meta. | Ahmed (go/no-go on YouTube and C6 footage) |
| 8 | Per-instructor public-naming confirmation (confirm-at-gate for all seven): Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair. All carry public_naming_cleared: yes with Ahmed sign-off (2026-06-05) but catalog public_status still reads unconfirmed. | All in-platform copy variants naming an instructor. If a name is not cleared at gate, that field's ad set drops to C2 abstract fallback and unnamed breadth copy. | Ahmed (per-instructor gate confirmation) |
| 9 | Verify-before-public-use facts: Toufic Kreidieh's Brands For Less name and garage detail; Elda Choucair's Omnicom, Forbes, Cannes, and numerical figures. Must not appear until verified. | Confirmed absent from all mapped copy variants. No action needed for go-live; this is a standing discipline check. | copywriter-ar and copywriter-en (discipline confirmed) |
| 10 | Saudi PDPL consent basis and data-residency: OPEN ITEM. Not confirmed for retargeting, hashed list uploads, CAPI hashed signals. | All retargeting ad sets (META-AS-09 through META-AS-11, TIKTOK-AS-05, YOUTUBE-AG-01 remarketing), subscriber suppression uploads, owned non-payer suppression uploads, lookalike construction. Hard blocker for retargeting. | compliance-privacy-reviewer (route from orchestrator); Ahmed (residency posture decision) |
| 11 | Suppression of owned non-payers from paid prospecting: OPEN ITEM. Hashed list match between CRM and Meta, TikTok, YouTube custom audiences. Source list and consent basis not confirmed. | Suppression from all prospecting ad sets. Same PDPL block as item 10. | Ahmed (suppression source confirmation); compliance-privacy-reviewer |
| 12 | Google Search keyword list: final set for all seven field groups requires review with seo-specialist before staging in Google Ads. | All nine Google ad groups (GOOGLE-AG-01 through GOOGLE-AG-09). Can stage but not launch until confirmed. | seo-specialist (keyword review); paid-build-engineer (apply to structure) |
| 13 | Tracking-plan from data-tracking-engineer: not received at this build stage. Meta Pixel, CAPI, TikTok Pixel, Google Ads conversion tag, YouTube remarketing tag, and UTM structure are directional only. Production tracking deployment is a human-gate action. | Pixel-based custom audiences, retargeting pools, conversion optimization events on all platforms, per-field reporting dimension in GA4. Hard go-live blocker for conversion optimization and retargeting. | data-tracking-engineer (deliver tracking-plan); Ahmed (approve production tracking writes) |
| 14 | Styling-field and marketing-field paid ad copy variants: RESOLVED. AD-STYLING-1 (Cedric Haddad, AR and EN) and AD-MARKETING-1 (Elda Choucair, AR and EN) authored and QA-passed (arabic-copy-qa 2026-06-12, english-copy-qa 2026-06-12). Placeholder copy removed from all affected ad sets. | No longer blocking. Remaining blockers on META-AS-07, META-AS-08, TIKTOK-AS-04, GOOGLE-AG-07, GOOGLE-AG-08 are the standing open items: budget+currency (1), gate platform (4), tracking (13), PDPL (10), rights-cleared photography per instructor (6). | CLOSED |
| 15 | Platform MCP read access: read-only access to Meta Ads, Google Ads, and TikTok Ads platforms for audience sizing and reach estimation is not yet approved. Audience definitions and reach estimates in this package are directional. | Audience sizing accuracy. Not a go-live blocker; a data quality item. | Ahmed (allowlist decision) |
| 16 | Reserve release decision: the 8 percent reserve (and conditional 12 percent YouTube share) are held pending the phase 1 performance readout from analytics-reporter at the end of approximately the first two weeks. | Mid-flight channel rebalancing. | Ahmed (approve analytics-reporter proposal after phase 1 readout) |

---

## 10. Spend on approval

n/a. No absolute spend is proposed or stated anywhere in this package. The brief has not
confirmed a budget or currency. Stating an invented figure would violate the campaign-agnostic
principle and the engine's hard rule against assumed budgets.

The maximum spend if approved equals the Ahmed-confirmed total budget, allocated proportionally
across channels as shown in section 7 (Meta and Instagram 45 percent, TikTok 18 percent,
Google Search 17 percent, YouTube 12 percent conditional, reserve 8 percent), over the
confirmed flight window, in the confirmed currency. Every one of those values is undefined
until Ahmed provides them.

Channel-level spend when budget is confirmed:
- Meta and Instagram: 45 percent of confirmed total budget
- TikTok: 18 percent of confirmed total budget
- Google Search: 17 percent of confirmed total budget
- YouTube: 12 percent of confirmed total budget (conditional on footage; moves to reserve if
  no cleared asset is available at the confirmed start date)
- Reserve: 8 percent of confirmed total budget (held until phase 1 readout, then released to
  best-performing channel per human-gate decision)

No figure is invented. No currency is assumed. If Ahmed confirms the budget and currency before
the gate approves go-live, paid-build-engineer applies those confirmed figures to the
proportions above and updates all budget fields in the staged structure before the gate clears.

---

## 11. Flips live

Approving this package and supplying the confirmed budget, currency, start date, end date, and
target CPA starts all paused campaigns on the confirmed start date and begins spending up to the
confirmed total budget ceiling across Meta, TikTok, Google Search, and YouTube (conditional),
with no further engine action until the phase 1 performance readout triggers an optimization
proposal back to the human gate.

---

## 12. Handoff

This package is routed to:
- human-gate: for review and approval of budget (open item 1), target CPA (open item 2),
  schedule (open item 3), YouTube and footage go/no-go (open item 7), and per-instructor
  naming confirmation (open item 8). Each is a discrete decision. Silence is not approval.
- compliance-privacy-reviewer: open item 10, for clearance of all retargeting audiences,
  hashed list uploads, CAPI hashed signals, and Saudi PDPL data-residency decision before any
  audience or tracking goes live.
- data-tracking-engineer: open item 13, to deliver the tracking-plan, confirm pixel firing on
  maharat.com class pages and plans page, wire CAPI and platform tags, and confirm the UTM
  structure per the direction in section 5.5.
- QA pipeline (orchestrator): open item 5, to route all upstream packages through remaining
  QA gates and advance status to at least qa-passed before go-live.
- copywriter-ar and copywriter-en: open item 14 RESOLVED. AD-STYLING-1 and AD-MARKETING-1
  (AR and EN) authored, arabic-copy-qa passed (2026-06-12), english-copy-qa passed
  (2026-06-12). Variants wired into all five affected ad sets and ad groups. No further
  copywriter action required for this item. Brand-qa resubmission for the copy packages
  remains pending as a separate upstream gate.
- seo-specialist: open item 12, to review and confirm the Google Search keyword list.
- analytics-reporter (streams 8 and 9): once approved and live, all performance data flows
  from Meta, Google, TikTok, and YouTube against the success metrics in the strategy-artifact
  and media-plan-package. The phase 1 readout triggers the reserve-release proposal. Per-field
  cost reporting (gate completions and subscriptions by field interest set) is required from
  day 1 of the flight, as specified in media-plan-package section 7.

Nothing in this package spends, publishes, or goes live. Every campaign and ad set is staged
paused. Ahmed flips each channel live after approving the open items above.

Status: gated-pending. Awaiting human gate review.

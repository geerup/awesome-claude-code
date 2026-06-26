# media-plan-package: 2026-06-elda-choucair-marketing

Internal artifact. Owned by performance-marketer. Reasoning only. This plan never spends,
never builds, and never goes live. The staged build goes to paid-build-engineer (stream 5).
Every spend decision and live action waits at the human gate. Silence is not approval.

No em dashes, Western numerals only, empowering framing throughout.

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: performance-marketer
- stream: paid acquisition strategy, upstream of stream 5 build and launch
- status: draft
- qa:
  - skill_eval: pass (structure, budget trace, four-channel coverage, target-flagging rule)
  - brand_qa: na (this plan carries no customer-facing copy; copy is owned by stream 4)
- open_items: see section 9
- brief_refs: budget (5000 USD paid media, CONFIRMED), flight length (2 weeks, CONFIRMED),
  channel emphasis (Meta and Instagram primary, Google and YouTube secondary, LinkedIn for the
  B2B-adjacent cut, CONFIRMED from strategy-artifact), segments (three personas plus the
  B2B-adjacent professional cut, CONFIRMED from strategy-artifact), lead magnets (Chapter 1
  free and PDF cheatsheet, CONFIRMED from brief), geo (GCC, primary Saudi Arabia, CONFIRMED),
  start_date (2026-06-08, ASSUMPTION, confirm), end_date (2026-06-21, ASSUMPTION, confirm),
  target_cpa_or_roas (NOT SUPPLIED, planning CPA proposed and flagged in section 7),
  success_metric (structure confirmed from strategy-artifact, target NUMBER not supplied,
  flagged as first open item for Ahmed)

---

## 1. Objective and KPI structure

### Campaign objective (paid layer)

Acquire and warm new audiences who do not yet sit on the Maharat owned list and route them
through the signup gate (email or WhatsApp) into the lifecycle engine. Paid is the feed; the
lifecycle is the conversion engine.

The paid layer does not own subscription conversions. It owns gate completions: a new
audience member who clicks an ad, lands on the conversion path, and submits their email or
enters the WhatsApp gate is a paid-attributed lead. That lead then enters the lifecycle flow
and may convert to a subscription. Attribution is lifecycle-first: subscription conversions
from the owned flow are the primary read; paid and organic conversions are credited where they
route through the gate into lifecycle.

### KPI hierarchy (paid layer only)

Primary paid KPI: gate completions (email or WhatsApp signup submissions) from paid traffic,
14-day window.

Secondary paid KPIs:
- Cost per gate completion (the planning CPA target; see section 7)
- Click-through rate on the lead hook creative (Chapter 1 free, PDF cheatsheet)
- Reach and frequency in the GCC prospecting audiences
- Video completion rate on any video creative (signal for YouTube and Meta Reels)

Downstream KPIs (owned by analytics-reporter and lifecycle-architect, not this layer):
- Subscription conversions attributable to the campaign
- Lifecycle email click-through and reactivation
- Chapter 1 plays

### Link to strategy-artifact success_metric

The strategy-artifact defines the success metric as subscription conversions attributable to
the campaign (primary), with secondary on lifecycle email engagement and reactivation,
Chapter 1 plays, and signup-gate completions from paid and organic. Paid's role is the
signup-gate completion secondary, feeding the primary conversion metric that the lifecycle
owns. Stream 8 (analytics-reporter) measures the full success metric against the structure
above once Ahmed supplies the target number and date.

Dependency: the success-metric target NUMBER and the measurement DATE are not yet supplied.
Stream 8 cannot measure success and the gate cannot judge it until Ahmed sets them. This is
the first open item.

---

## 2. Channel mix

Justification per channel is tied to the angle ("decision architecture over tactics"), the
three personas, and the B2B-adjacent professional cut. No channel is defaulted in; each is
included or excluded against the brief.

| Channel | In or out | Role | Primary segments served | Rationale |
|---|---|---|---|---|
| Meta (Instagram primary, Facebook secondary) | In | Prospecting and retargeting, conversion-path warm-up | All three personas, especially persona-2 self-taught builders and persona-3 skilled-but-stuck executors | GCC is high on Instagram. The angle's two-beat, contrarian creative (myth-flip and pain-question) suits Reels and Feed formats. Broadest reach for the 18 to 35 core demo in Saudi Arabia. Retargeting pool for warm re-engagement once pixel or CAPI is live. |
| Google Search | In | High-intent keyword capture | Persona-1 data-driven marketers, persona-3 skilled-but-stuck executors | Captures users actively searching "marketing course," "Elda Choucair," "marketing masterclass Arabic." Low volume but high intent and low wasted spend. Small allocation; justifies inclusion on signal quality. |
| Google Demand Gen | In | Cross-channel prospecting, video-adjacent reach | All three personas | Runs across YouTube, Gmail, and Discover. Complements Meta prospecting without fully duplicating it. Supports the Chapter 1 free hook with visual units. |
| YouTube | In | Video reach and brand consideration for the class hook | All three personas, with the direct promise hook | Elda's voice and the class itself are video-native. YouTube pre-roll and in-stream units let the Chapter 1 free hook run in full. Saudi Arabia over-indexes on YouTube. Allocation is modest; it is a reach and consideration layer, not the conversion driver. |
| LinkedIn | In | B2B-adjacent professional cut prospecting | Persona-1 data-driven marketers and persona-3 skilled-but-stuck executors (professional face), and the Omnicom and agency-side reach unique to Elda | The brief and strategy-artifact explicitly call out LinkedIn for this cut. Elda's Omnicom CEO credential resonates most on this platform. Higher CPL than Meta but a distinct and unreachable-elsewhere audience. Capped budget. |
| TikTok | Out | Excluded for this flight | n/a | The 18 to 35 Saudi GCC audience is present on TikTok, but the angle is a decision-architecture, senior-voice class. TikTok's format and feed context skew toward entertainment and lighter content. The budget is 5000 USD over 14 days; spreading to a fifth platform would dilute the learning and the spend below meaningful minimums on each. Revisit if a future flight has a larger budget or a short-form creative strategy purpose-built for TikTok. |

---

## 3. Budget split

Total budget: 5000 USD, confirmed from the brief. No amount is invented. The split traces
to the brief total and sums exactly to 5000 USD.

### Per-channel allocation

The brief objective is new audience acquisition and gate-completion feeding the lifecycle.
This is a growth objective tilted upper funnel (awareness and consideration dominate the
purpose) with the signup gate as the conversion step. The funnel allocation tilts toward
prospecting and consideration, with a smaller conversion-focused retargeting layer once
the pixel or CAPI events are live.

| Channel | Phase 1 days 1 to 7 (learn) | Phase 2 days 8 to 14 (scale) | Total | Share of total |
|---|---|---|---|---|
| Meta (Instagram and Facebook) | 875 USD | 1125 USD | 2000 USD | 40% |
| Google Search | 200 USD | 300 USD | 500 USD | 10% |
| Google Demand Gen | 300 USD | 400 USD | 700 USD | 14% |
| YouTube | 250 USD | 350 USD | 600 USD | 12% |
| LinkedIn | 375 USD | 825 USD | 1200 USD | 24% |
| TOTAL | 2000 USD | 3000 USD | 5000 USD | 100% |

Note on the phase split: 40 percent (2000 USD) in the learning phase, 60 percent (3000 USD)
in the scale phase. This is the standard test-then-scale logic: hold back the larger share
until the day-7 readout identifies which channel and creative are delivering the lowest cost
per gate completion, then concentrate the scale budget there.

### Funnel-stage allocation

| Funnel stage | Share | Amount | Channels mapped | Tied to objective |
|---|---|---|---|---|
| Awareness and reach | 26% | 1300 USD | YouTube, Meta Reels broad prospecting, Google Demand Gen | Warm new GCC audiences to the class and the angle; plant the decision-architecture frame |
| Consideration and warm-up | 36% | 1800 USD | Meta Feed and Stories interest-based prospecting, LinkedIn prospecting, Google Demand Gen cross-channel | Drive Chapter 1 free hook and PDF cheatsheet click-throughs to the gate from warmed cold audiences |
| Conversion-intent and retargeting | 38% | 1900 USD | Meta retargeting (site and video viewers), Google Search (brand and intent terms), LinkedIn retargeting | Capture declared intent and re-engage warm audiences; route them to the signup gate |
| TOTAL | 100% | 5000 USD | | |

Note: retargeting (part of the 38 percent conversion layer) is conditional on the pixel or
CAPI events being live and the conversion path being wired by data-tracking-engineer and
stream 6. If these are not live at launch, the retargeting budget is reallocated to
prospecting for phase 1 and confirmed at the day-7 readout. This is flagged as a pre-spend
dependency in section 9.

### Budget-level structure (CBO vs ABO)

| Channel | Budget level | Stage | Why |
|---|---|---|---|
| Meta | ABO (ad-set budget optimization) | Phase 1 test | Three personas each need their own ad set to measure cost per gate completion per persona. ABO holds the allocation so no single ad set cannibalizes the others during learning. |
| Meta | CBO (campaign budget optimization) | Phase 2 scale | After day-7 readout, consolidate to CBO and let the algorithm push spend to the winning persona and creative combination. |
| Google Search | Campaign-level daily cap | Both phases | Low volume; a daily cap is sufficient control. No CBO or ABO structure needed for a single intent keyword group. |
| Google Demand Gen | CBO equivalent (campaign-level budget) | Both phases | Demand Gen uses campaign-level budget natively. Audience signals surface the winning placements automatically. |
| YouTube | Campaign-level daily budget | Both phases | Single awareness objective; no multi-ad-set testing needed at this budget level. |
| LinkedIn | ABO | Phase 1 test | Persona-1 and persona-3 targeting are distinct enough to warrant separate ad sets with controlled budgets to measure CPL per persona. |
| LinkedIn | ABO, shifted toward winner | Phase 2 scale | Day-7 readout informs which persona ad set to weight; shift ABO amounts manually rather than CBO (LinkedIn CBO is less mature). |

---

## 4. Audience strategy per channel

All audiences are defined as segment definitions. No personal data, no individual identifiers,
no sensitive data in any audience definition or parameter.

Retargeting and lookalike audiences depend on the pixel or CAPI events being live and the
conversion path being active. Where the data cannot yet support an audience, it is flagged as
an open item, not invented.

### Meta (Instagram primary, Facebook secondary)

**Prospecting: persona-1 data-driven marketers**
- Layer: interest-based cold prospecting
- Geo: Saudi Arabia primary, UAE and Kuwait secondary
- Age: 22 to 38
- Interests and behaviors: digital marketing, marketing analytics, business and
  entrepreneurship, marketing technology, social media marketing, Google Analytics, HubSpot,
  data analysis
- Placement: Instagram Feed and Reels primary (where Saudi engagement concentrates),
  Facebook Feed secondary
- Creative hook: pain-question ("كل شيء جاهز: البيانات والقمع والمؤشرات. فلماذا لا أحد يشتري؟")
  into the PDF cheatsheet offer

**Prospecting: persona-2 self-taught builders**
- Layer: interest-based cold prospecting
- Geo: Saudi Arabia primary, UAE and Kuwait secondary
- Age: 20 to 35
- Interests and behaviors: entrepreneurship, startups, product building, business management,
  small business, freelancing, Shopify, e-commerce, brand building
- Placement: Instagram Feed and Reels primary
- Creative hook: myth-flip and direct promise ("السوق لا يكافئ أفضل منتج") into Chapter 1 free

**Prospecting: persona-3 skilled-but-stuck executors**
- Layer: interest-based cold prospecting
- Geo: Saudi Arabia primary, UAE, Kuwait, Bahrain secondary
- Age: 24 to 40
- Interests and behaviors: marketing strategy, brand management, content marketing, marketing
  courses and education, career development, professional skills, marketing tools and software
- Placement: Instagram Feed primary, Facebook Feed secondary
- Creative hook: direct promise (credential drop + "strategy over features") into the cheatsheet

**Retargeting: warm site visitors and video viewers (conditional)**
- Dependency: pixel or CAPI must be live on the Maharat class page and the gate page
- Layer 1: users who visited the class page URL but did not complete the gate, 14-day window
- Layer 2: users who viewed 50 percent or more of any video creative in the prospecting phase
- Layer 3: users who engaged with the Instagram profile (follows, post interactions) in the
  30-day window
- Geo: same as prospecting (Saudi Arabia primary)
- Creative hook: direct promise + Chapter 1 free as the low-friction conversion step
- Flagged as open item: retargeting is conditional on pixel or CAPI deployment by
  data-tracking-engineer and on the conversion path being wired (stream 6)

**Lookalike (conditional, phase 2 only)**
- Seed: gate completions (email signups) from phase 1, uploaded as a hashed custom audience
- Lookalike: 1 to 3 percent lookalike in Saudi Arabia
- Note: seed requires a minimum of about 100 conversions for stable modeling; this may not
  reach threshold in a 14-day flight at this budget. Record as a phase-2 option to evaluate
  at the day-7 readout, not a committed tactic.
- Privacy rule: the custom audience seed is a hashed upload; no personal data in URL
  parameters.

**Exclusions (Meta, all ad sets)**
- Existing Maharat paying subscribers (custom audience upload from CRM, hashed)
- Prior gate completions (converts already in the lifecycle)
- Dependency: exclusion lists require the CRM or gate platform to be named and accessible.
  Flagged as open item.

### Google Search

**High-intent keyword prospecting**
- Geo: Saudi Arabia primary, UAE secondary
- Language: Arabic and English
- Keyword groups:
  - Brand and class: "Elda Choucair," "Elda Choucair marketing," "Maharat marketing class,"
    "إلدا شقير تسويق," "صف تسويق مهارات"
  - Category intent: "marketing course Arabic," "marketing masterclass online," "learn
    marketing Arabic," "دورة تسويق اونلاين," "تعلم التسويق"
  - Problem-aware: "how to convert more customers," "why my marketing is not working,"
    "marketing strategy course"
- Match types: phrase and exact for brand terms; phrase and broad-match-modifier equivalents
  for category terms
- Creative: short responsive search ads linking to the class page or the gate page; no
  price stated; no held-back claims; approved phrasing only ("20 years in one class,"
  "marketing is decision architecture," empowering)
- Bid strategy: maximize conversions toward the gate completion event, switching to target CPA
  once the event has 20 or more conversions (threshold for Smart Bidding stability)

**Exclusions (Search)**
- Irrelevant navigational queries (job search, salary terms, "Omnicom jobs," etc.)
- Competitor brand exclusions (do not bid on competitor brand names)

### Google Demand Gen

**Cross-channel visual prospecting**
- Geo: Saudi Arabia primary, UAE and Kuwait secondary
- Audience signals: in-market for online education and marketing courses; custom intent
  audiences built on the keyword groups above; similar audiences to the Maharat website
  visitors (data dependency: Google Ads must have audience signals from the Maharat property)
- Placements: YouTube feeds, Gmail, Google Discover
- Creative hook: class cover image (rights-cleared EN and AR cloudfront assets confirmed in the
  brief), short headline, and Chapter 1 free or PDF cheatsheet CTA
- Bid strategy: maximize conversions toward the gate completion event; or maximize clicks if
  the gate completion event has insufficient volume in the first 5 days

### YouTube

**Video reach and consideration**
- Geo: Saudi Arabia primary, UAE secondary
- Format: in-stream skippable (6-second bumpers as a supplementary option if the creative
  package includes a 6-second cut)
- Audience: custom intent built on the marketing course and decision-making keyword set;
  in-market for online courses and education; interest in marketing and business
- Creative dependency: the Feb 2026 launch trailer (if rights are confirmed) is the primary
  asset. If trailer rights are unconfirmed, use the class cover image in a video slideshow
  or a produced asset from stream 3. Rights status is an open item.
- Bid strategy: target CPV (cost per view) for the consideration phase; switch to
  maximize conversions toward gate completion if conversion volume supports it
- Measurement: 25 percent, 50 percent, and 100 percent video completion rates as signals
  for creative quality; gate completions as the primary outcome event

### LinkedIn

**B2B-adjacent professional cut prospecting**
- Geo: Saudi Arabia primary, UAE secondary
- Target: persona-1 data-driven marketers and persona-3 skilled-but-stuck executors in their
  professional context
- Job-function targeting:
  - Marketing (all levels)
  - Business development and strategy
  - Management and leadership (founders, directors, C-suite in SME and mid-market)
- Industry targeting:
  - Advertising and marketing services (direct Elda and Omnicom relevance)
  - Retail and consumer goods
  - Financial services
  - Technology (SaaS, e-commerce)
- Seniority: associate, mid-senior, director, manager (exclude entry-level and C-suite at
  large enterprises, who are unlikely to be the self-purchasing decision maker)
- Member groups: marketing-related LinkedIn groups in the GCC region (available targeting)
- Creative hook: credential drop ("CEO of Omnicom Media Group MENA, 20 years distilled into
  one class") into the cheatsheet offer or class page; approved phrasing only
- Format: single-image sponsored content primary (LinkedIn Feed); document ads (carousel of
  the cheatsheet pages) as a secondary format if the creative package supports it
- Bid strategy: maximum delivery (LinkedIn's equivalent of maximize conversions toward the
  gate completion lead-gen form or the class page click); switch to target CPL if volume
  allows. LinkedIn Lead Gen Forms (native form, no redirect) are an option for the gate
  completion event and reduce friction; flag for data-tracking-engineer to confirm the
  form-to-lifecycle wiring.
- Note: LinkedIn CPL in this region and audience can range from 15 USD to 40 USD or more,
  significantly higher than Meta. The allocation reflects this. The audience is worth the cost
  because it is unreachable-elsewhere via the Omnicom and professional marketer angle.

**LinkedIn retargeting (conditional, phase 2)**
- Dependency: LinkedIn Insight Tag must be deployed on the Maharat property
- Layer: users who visited the class page from LinkedIn, 30-day window
- Creative: direct-promise hook into Chapter 1 free
- Flagged as open item

---

## 5. Bid strategy summary

Because the brief does not supply a target CPA, bid strategies start on maximizing volume
(gate completions) and shift to cost-efficiency modes once sufficient conversion data exists.
See section 7 for the planning CPA and the explicit flagging.

| Channel | Phase 1 bid strategy | Phase 2 bid strategy | Optimization event | Threshold to shift |
|---|---|---|---|---|
| Meta prospecting | Maximize conversions (gate completion, or initiate checkout if gate is not tracked) | Cost cap at planning CPA, or continue maximize conversions if learning phase not exited | Lead or complete registration event (gate completion) | 50 or more events per ad set per week before switching to cost cap |
| Meta retargeting | Maximize conversions | Lowest cost | Same gate completion event | Conditional on pixel or CAPI being live |
| Google Search | Maximize conversions | Target CPA at planning CPA level once 20 or more events | Gate completion conversion action | 20 or more conversions in the trailing 30 days |
| Google Demand Gen | Maximize conversions | Maximize conversions (no shift; volume may not support target CPA) | Gate completion conversion action | Evaluate at day-7 readout |
| YouTube | Maximize CPV or target CPV | Maximize conversions toward gate completion if volume allows | Gate completion or class page visit as proxy | Evaluate at day-7 readout |
| LinkedIn | Maximum delivery toward gate completion or lead gen form | Manual CPL bid if volume gives signal | Lead gen form submission or class page click | Evaluate at day-7 readout |

Optimization event dependency: all bid strategies that optimize toward gate completion
require the gate completion event to be tracked and firing. This depends on:
1. The gate platform being confirmed (currently OPEN ITEM: Ortto vs HubSpot).
2. The pixel or CAPI being deployed by data-tracking-engineer (stream 6).
3. Compliance and privacy review on the tracking and consent mechanism.
Until these are confirmed, bid strategies default to maximize clicks (Meta) or maximize
conversions toward a proxy event (class page visit). This is recorded as a blocking
pre-spend dependency.

---

## 6. Flighting: 14-day plan (proposed 2026-06-08 to 2026-06-21)

Dates are an ASSUMPTION from the brief and strategy-artifact. Confirm with Ahmed before
any build. The flight structure and day-7 readout logic hold regardless of the exact dates.

### Phase structure

| Phase | Days | Window (proposed) | Budget | Goal |
|---|---|---|---|---|
| Phase 1: learning | Days 1 to 7 | 2026-06-08 to 2026-06-14 | 2000 USD | Run all channels simultaneously, ABO on Meta and LinkedIn. Identify the lowest cost-per-gate-completion channel, creative, and persona combination. Exit learning phase on Meta ad sets. |
| Day-7 readout | Day 7 (end of phase 1) | 2026-06-14 | Evaluation only | Analytics-reporter reads cost per gate completion, CTR, and video completion rate per channel, per persona, per creative. Performance-marketer proposes scale and cut moves to the human gate for phase 2 authorization. |
| Phase 2: scale | Days 8 to 14 | 2026-06-15 to 2026-06-21 | 3000 USD | Concentrate remaining budget on the winning channel and persona. Activate retargeting if pixel or CAPI events are confirmed live. On Meta, shift ABO ad sets to CBO on the winning campaign. Reduce or pause underperformers. |

### Day-by-day pacing (phase 1, daily budgets)

| Day | Meta | Google Search | Google Demand Gen | YouTube | LinkedIn | Daily total |
|---|---|---|---|---|---|---|
| Day 1 (2026-06-08) | 100 USD | 25 USD | 37 USD | 30 USD | 45 USD | 237 USD |
| Day 2 | 110 USD | 25 USD | 40 USD | 32 USD | 50 USD | 257 USD |
| Day 3 | 120 USD | 28 USD | 42 USD | 35 USD | 53 USD | 278 USD |
| Day 4 | 125 USD | 30 USD | 43 USD | 36 USD | 54 USD | 288 USD |
| Day 5 | 125 USD | 30 USD | 45 USD | 37 USD | 55 USD | 292 USD |
| Day 6 | 130 USD | 31 USD | 46 USD | 40 USD | 59 USD | 306 USD |
| Day 7 | 165 USD | 31 USD | 47 USD | 40 USD | 59 USD | 342 USD |
| Phase 1 total | 875 USD | 200 USD | 300 USD | 250 USD | 375 USD | 2000 USD |

Note: the ramp in days 1 to 3 is intentional. Meta and LinkedIn ad sets need 2 to 3 days
of delivery before the algorithm exits the exploration state. Launching at full daily budget
on day 1 can produce unstable CPMs and erratic delivery. The ramp reaches full pacing by
day 4 to 5.

### Phase 2 pacing (illustrative, pending day-7 readout)

Phase 2 daily budget is 3000 USD over 7 days (approximately 428 USD per day on average).
The actual per-channel allocation is determined by the day-7 readout and the human gate
decision on the optimization proposals. The table below is a planning illustration assuming
Meta is the top performer and LinkedIn holds its position.

| Channel | Phase 2 illustrative daily | Phase 2 total | Condition |
|---|---|---|---|
| Meta (scaled, CBO) | 130 USD per day average | 910 USD | If Meta is the winner at day 7 |
| Google Search | 55 USD per day average | 385 USD | Hold; search intent is stable |
| Google Demand Gen | 65 USD per day average | 455 USD | Hold or scale slightly |
| YouTube | 50 USD per day average | 350 USD | Hold; consideration layer |
| LinkedIn | 130 USD per day average | 910 USD | If LinkedIn CPL is acceptable |
| Phase 2 total | | 3010 USD | Rounds to 3000 USD at gate approval |

This is a planning illustration. Any reallocation from the day-7 readout is a proposal from
analytics-reporter and performance-marketer to the human gate. No budget shift happens without
the human gate authorizing it. The total across both phases remains 5000 USD.

### Learning phase allowance and platform notes

- Meta: the standard Meta learning phase is approximately 50 optimization events per ad set
  per week. At a planning CPA of 5 to 12 USD, the phase 1 Meta budget of 875 USD may generate
  70 to 175 gate completions across all three persona ad sets. This gives a reasonable chance
  of exiting the learning phase on the top-performing ad set before day 7. If Meta does not
  exit learning by day 5, this is a signal at the readout.
- Google Search: search campaigns can show reliable data within 3 to 5 days at this budget
  level. The keyword volume for the GCC marketing course category may be limited; watch for
  low impression share as a signal.
- Google Demand Gen: requires 3 to 5 days to optimize creative and audience signals. May not
  generate sufficient gate completions to hit Smart Bidding thresholds in phase 1.
- YouTube: brand and consideration; do not expect gate completions to dominate here. The
  primary read is cost per completed view and the downstream behavior of YouTube audiences
  who then appear in the retargeting pool.
- LinkedIn: slowest learning and highest CPL of the channels. Phase 1 allocation of 375 USD
  may yield 10 to 25 gate completions at a 15 to 40 USD CPL range. This is sufficient to
  read persona performance direction but may not produce a statistically conclusive winner.

---

## 7. Planning CPA and expected lead ranges

FLAGGED: all figures below are planning assumptions to guide the budget split and the
day-7 readout. They are NOT committed targets. The brief does not supply a target CPA or
ROAS. These are proposed planning anchors for Ahmed to review and confirm or revise before
the campaign is authorized.

### Planning CPA basis

"CPA" in this plan means cost per gate completion (email or WhatsApp signup submission),
not cost per subscription. Subscription CPA is owned by the lifecycle and is not calculated
here because the lifecycle carries zero media cost and the conversion timing is post-gate.

Planning CPA estimates by channel (GCC market, education and masterclass category, based on
general paid performance norms for this region and category; no prior Maharat paid data
exists to anchor these):

| Channel | Planning CPA estimate | Basis | Confidence |
|---|---|---|---|
| Meta prospecting | 5 to 10 USD per gate completion | GCC education category benchmarks; strong creative-driven lead gen | Medium; depends heavily on creative and offer hook quality |
| Meta retargeting | 3 to 7 USD per gate completion | Warm audience, lower friction | Medium; conditional on pixel being live |
| Google Search | 4 to 9 USD per gate completion | High-intent query capture, small volume | Medium; keyword volume is the constraint |
| Google Demand Gen | 8 to 15 USD per gate completion | Broader, less intent-driven | Lower confidence; may function better as a reach and consideration signal |
| YouTube | 12 to 25 USD per completed view or gate completion | Consideration layer; gate completions from YouTube are harder to attribute at this budget | Lower confidence |
| LinkedIn | 18 to 40 USD per gate completion | GCC professional targeting, premium CPL by design | Lower; LinkedIn CPL in the region is consistently higher |

### Blended planning CPA

Weighted by the channel budget split, the blended planning CPA across all gate completions
in the 5000 USD flight is estimated at approximately 10 to 18 USD per gate completion.

Expected gate completions from the 5000 USD flight: approximately 280 to 500, based on the
blended planning CPA range.

This is a planning range, not a committed target. If the actual blended CPA exceeds
18 USD meaningfully, the day-7 readout proposal will flag reallocation toward the lower-CPA
channels.

### Scale planning CPA confirmation request

Ahmed must confirm or revise the planning CPA before the budget is authorized. Specifically:
1. Is the blended planning CPA range of 10 to 18 USD per gate completion acceptable?
2. Is there a ceiling (hard maximum CPA) per channel the plan should enforce?
3. Does the campaign have a target number of gate completions over the 14-day flight?

Until confirmed, no bid strategy uses a hard target CPA cap; all bid strategies default to
maximize conversions (volume-first).

---

## 8. Success metric link

| Strategy-artifact success_metric | How this media plan connects to it | Who measures |
|---|---|---|
| Primary: subscription conversions attributable to the campaign | Paid routes gate completions (new leads) into the lifecycle; lifecycle converts to subscriptions; paid is credited for the gate completion step | analytics-reporter (stream 8), after Ahmed supplies the target number and date |
| Secondary: lifecycle email click-through and reactivation | Paid feeds new leads into the lifecycle, expanding the pool that can click through; paid does not own this metric | lifecycle-architect (stream 7) |
| Secondary: Chapter 1 plays | Paid creative promotes Chapter 1 free as the lead hook; plays are a downstream signal of lead quality | analytics-reporter (stream 8) |
| Secondary: signup-gate completions from paid | This is the primary paid KPI. Gate completions from paid traffic are the direct output of this media plan | analytics-reporter (stream 8), using UTMs per channel and the gate completion event fired by data-tracking-engineer |

Attribution note: UTM parameters track source (paid channel) and campaign. They carry no
personal or sensitive data. The UTM structure is designed by data-tracking-engineer; this plan
sets the source and campaign tags, not the full parameter string.

---

## 9. Open items and pre-spend dependencies

### Blocking for any spend (hard stops)

1. SUCCESS METRIC TARGET NUMBER AND DATE (ASSUMPTION). Not supplied. First open item for
   Ahmed. Stream 8 cannot measure success and the gate cannot judge it without this.

2. GATE AND CRM PLATFORM (OPEN ITEM). Email, WhatsApp, and CRM platform not confirmed
   (Ortto vs HubSpot migration, Arabic RTL concern). Blocks the live wiring of the gate
   completion event that all bid strategies optimize toward. Also blocks the exclusion
   audience upload (paying subscribers and existing contacts) that keeps paid media from
   wasting budget on people already in the lifecycle. The media plan can be authorized before
   this is resolved, but the campaign cannot go live until the platform is named and the gate
   completion event is firing. Owned by stream 6 (conversion-engineer) and stream 7
   (lifecycle-architect).

3. PIXEL OR CAPI DEPLOYMENT (OPEN ITEM). The Meta Pixel or Conversions API, the Google Ads
   tag, the LinkedIn Insight Tag, and the YouTube or Google Analytics 4 event must be deployed
   and confirmed firing on the class page and the gate page before retargeting and optimized
   bidding can run. This is data-tracking-engineer's (stream 6) deliverable. A compliance
   and privacy check is required on the consent mechanism before any tag fires. Blocked on the
   gate platform being named.

4. PRICE (ASSUMPTION). No price in any customer-facing copy. Confirmed from the brief.
   This affects ad creative in streams 3 and 4; it does not block the media plan structure,
   but no ad creative referencing a price can be authorized.

5. PLAN AND PLAN STRUCTURE (ASSUMPTION). 1 vs 3 vs 12 months; the 1/3/12 vs class/6/12
   tension. Does not block the media plan structure (the gate completion event and the lead
   hook are plan-agnostic), but it affects the conversion page copy and the lifecycle flow.

### Affecting quality and accuracy of the plan

6. START DATE AND END DATE (ASSUMPTION). Proposed 2026-06-08 to 2026-06-21. Confirm with
   Ahmed. The flighting plan holds regardless of the exact dates; the absolute calendar dates
   for the day-7 readout and the phase-2 start shift accordingly.

7. TARGET CPA (NOT SUPPLIED). Performance-marketer proposes the planning CPA range of 10 to
   18 USD per gate completion as a planning anchor. Ahmed must confirm or revise before
   authorizing the budget. Until confirmed, all bid strategies run on maximize conversions
   (volume-first). See section 7.

8. LINKEDIN INSIGHT TAG AND LEAD GEN FORM WIRING (OPEN ITEM). LinkedIn retargeting and the
   LinkedIn Lead Gen Form native gate option are both conditional on the Insight Tag being
   deployed and the form-to-lifecycle wiring being confirmed with data-tracking-engineer.

9. TRAILER RIGHTS AND URL (OPEN ITEM). The Feb 2026 launch trailer is the preferred YouTube
   creative asset. Rights and the trailer URL are unconfirmed per the brief. If unconfirmed
   at launch, YouTube creative falls back to the class cover image (rights-cleared, confirmed
   in the brief) in a video slideshow or a produced video asset from stream 3. Confirm before
   the build.

10. FORMAL CATALOG STATUS FOR ELDA CHOUCAIR (OPEN ITEM). The catalog public-status column
    reads "unconfirmed" pending formal team confirmation, despite the published class page
    being sufficient to name her. Surface at the human gate. Does not block the media plan
    structure; does affect in-platform ad copy referencing her name.

11. SUPPRESSION LIST SOURCE (OPEN ITEM). The exclusion custom audiences (paying subscribers,
    unsubscribed contacts) require the CRM to export a hashed list for upload into Meta and
    LinkedIn. Blocked on the gate platform being named. The paid audience strategy cannot
    fully exclude existing subscribers without this list.

12. REPORTING CADENCE (ASSUMPTION). Day-7 readout and end-of-flight report proposed. Confirm
    with Ahmed. The day-7 readout is the decision point for phase-2 reallocation proposals.

---

## 10. Spend on approval

Approving this plan authorizes paid-build-engineer to stage all campaigns paused across Meta,
Google Search, Google Demand Gen, YouTube, and LinkedIn, and proposes up to 5000 USD of paid
media spend over the proposed 14-day window of 2026-06-08 to 2026-06-21, with no spend
occurring until the human gate gives explicit per-campaign authorization and the pre-spend
dependencies in section 9 are resolved.

---

## Handoff

This media-plan-package hands to:

- paid-build-engineer (stream 5): to stage the campaign structure paused across Meta, Google
  Search, Google Demand Gen, YouTube, and LinkedIn, per the channel mix, budget split,
  audience definitions, bid strategies, and flighting in this plan. Paid-build-engineer
  assembles the paid-launch-package for the human gate.

- data-tracking-engineer (stream 6): to wire the channel events (gate completion event per
  channel), the UTM structure, and the consent and compliance mechanism. The bid strategies
  in this plan depend on the gate completion event firing correctly.

- analytics-reporter (stream 8): to measure against the success metric structure in section 7
  and this plan's KPI hierarchy, using the day-7 readout as the mid-flight decision point and
  the end-of-flight report as the full campaign read.

- human gate: for spend authorization. The plan proposes up to 5000 USD. No spend occurs
  without explicit approval. The phase-2 reallocation proposals from the day-7 readout are a
  separate gate decision. Silence is not approval.

All pre-spend dependencies in section 9 must be resolved before any campaign goes live.
Performance-marketer proposes; paid-build-engineer stages; the human gate authorizes; a
human flips live. This agent performs no live action.

# monitoring-reporting-plan: 2026-06-elda-choucair-marketing

Internal artifact. Owned by analytics-reporter. Streams 8 and 9.
Reasoning only. No live campaign changes, no spend, no send.
All numbers in the metric tree are structural slots, not invented targets.
No em dashes, no tatweel, Western numerals only (0 to 9).

---

## Envelope

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: analytics-reporter
- stream: 8 monitoring and optimization, 9 reporting and learning
- status: draft
- qa:
  - skill_eval: self-checked against skills/08-monitoring-optimization/evals/evals.json
    and skills/09-reporting-learning/evals/evals.json. Both passed on structure,
    metric discipline, propose-not-act rule, and no-vanity-metric rule.
  - arabic_qa: na (internal artifact, no customer-facing copy)
  - brand_qa: na (internal artifact)
  - compliance: na (no send, spend, or data collection at this stream)
- open_items: see section 6. The success-metric target number and measurement date are the
  first and most important open item. Success cannot be judged until Ahmed supplies them.
- brief_refs:
  - objective: grow B2C subscriptions via lifecycle-led full-funnel campaign
  - success_metric: from strategy-artifact section 7, structure only; number and date not supplied
  - window: proposed 2026-06-08 to 2026-06-21 (14 days, ASSUMPTION; confirm with Ahmed)

---

## STOP: success cannot be judged until Ahmed supplies the target number and date

The strategy-artifact section 7 defines the success_metric structure. It explicitly states
that the target NUMBER and the measurement DATE are not supplied. This monitoring and reporting
plan is built around that structure so the framework is ready the moment Ahmed provides both.
Until they are supplied, this agent does not measure against a target and does not judge the
campaign a success or a failure. No target is invented. This is the first open item.

---

## 1. Metric tree

The metric tree maps every metric the campaign will be read against to its source event,
its channel, and its position in the success_metric hierarchy. The hierarchy comes from
strategy-artifact section 7 unchanged.

### 1A. Primary metric

| Metric | Definition | Source event | Channel(s) that drive it | Slot for target (NOT SUPPLIED) |
|---|---|---|---|---|
| Subscription conversions attributable to the campaign | New paid plan starts (subscription_start event) where the contact's path traces to this campaign_id, via the lifecycle flow (owned) or via gate completion from paid or organic that routed into the lifecycle | subscription_start (server-side via CAPI and GA4 purchase event), attributed to campaign_id "2026-06-elda-choucair-marketing" | Lifecycle email (primary driver), paid acquisition (gate-completion feed), organic social (gate-completion feed) | [TARGET NUMBER and DATE: open item for Ahmed] |

Attribution logic: lifecycle-first. A subscription conversion is attributed to the campaign
when the contact received at least one message in the E1 to E5 flow during the flight AND
the subscription_start event fired within the measurement window. Paid and organic
contributions are credited where the contact's source UTM traces to this campaign and they
completed the gate before entering the lifecycle.

Measurement tool dependency: BigQuery (subscription_start joined to email send/open records
and UTM source), GA4 (purchase event, per-session source attribution), Stripe or payment
processor (revenue confirmation). All three require data-tracking-engineer confirmation and
tool access approval before any live read is possible.

### 1B. Secondary metrics

| Metric | Definition | Source event | Channel | Measurement tool |
|---|---|---|---|---|
| Lifecycle email CTR | Total clicks divided by total delivered, per email step (E1 to E5), per persona variant | email_click divided by email_delivered, per message step and persona tag | Lifecycle email (stream 7) | Email platform (Ortto or HubSpot, once confirmed) and BigQuery |
| Reactivation rate | Contacts in the lapsed-engaged or never-engaged tier who open or click at least one message in the flow, divided by total contacts in those two tiers who received at least one message | email_open or email_click, filtered to lapsed-engaged and never-engaged tier | Lifecycle email (stream 7) | Email platform and BigQuery |
| Chapter 1 plays | Count of chapter_1_play events fired during the flight, traced to this campaign_id | chapter_1_play (member platform event) | All channels (email CTA links, paid creative, organic post links) | BigQuery, GA4 (page_view or content-engagement event on the Chapter 1 member URL) |
| Signup-gate completions from paid and organic | Count of submit events (email form submission) from traffic with utm_medium = paid_social, paid_search, or organic_social, within the flight window | submit event (gate form POST success) and confirm event (inline confirmation or double opt-in click) | Paid acquisition channels (Meta, Google, YouTube, LinkedIn), organic social | GA4 (generate_lead event), Meta Events Manager (Lead event), BigQuery (UTM-joined event table) |

### 1C. Excluded metrics (vanity, not part of the success_metric)

The following are explicitly excluded. They are not reported as results and do not
substitute for the success_metric under any condition.

- Impressions and raw reach (paid): measures delivery, not conversion. Not a goal.
- Email open rate as a standalone verdict: open rate is a signal for subject line quality and
  deliverability. It is not a conversion metric. It feeds the CTR and reactivation reads but
  is not a result in itself.
- Social follower count or post engagement rate: organic reach signal only.
- Page views to the landing page without a downstream action: awareness, not a conversion.
- Video completion rate on paid creative: a creative-quality signal, useful for the day-7
  readout's paid optimization proposal, but not a success metric.

### 1D. Paid layer secondary KPI (from media-plan.md)

The paid layer's primary KPI is gate completions from paid traffic (the submit event,
utm_medium = paid_social or paid_search). This is included in the secondary metric table
above under "Signup-gate completions from paid and organic." Cost per gate completion
(planning CPA range 10 to 18 USD per gate completion, blended, per media-plan.md section 7)
is a paid efficiency read at the day-7 readout only, as a proposal input. It is not a
success metric; it is a channel diagnostic.

---

## 2. Day-7 mid-flight readout structure

Timing: proposed 2026-06-14 (day 7 of the proposed flight, ASSUMPTION; the actual date
shifts proportionally if the start date changes). The readout is informational. No cadence
change, budget shift, suppression change, or send action results from it without Ahmed's
explicit approval. Every optimization move from this readout is a proposal to the human gate.

### 2A. What to check (the readout agenda)

Lifecycle email (stream 7, primary):

- E1 delivered count vs expected send size. If delivered is materially below the estimated
  18,000 (after suppression), flag as a deliverability open item for data-tracking-engineer.
- E1 open rate by recency tier (recently-active, lapsed-engaged, never-engaged): the baseline
  signal for subject line quality and list health. Not a success metric; a diagnostic.
- E1 and E2 click-through rate per email step per persona variant: the leading indicator for
  lifecycle engagement heading toward Chapter 1 play and gate completion.
- Reactivation signal: how many lapsed-engaged and never-engaged contacts opened or clicked
  E1 or E2. This is the early read on whether the non-payer flow is reaching contacts who
  had gone dark.
- chapter_1_play events to date: the count of contacts who started Chapter 1 after receiving
  E1 or E2. This is the best mid-flight leading indicator for E4 conversion readiness. If
  this count is materially low, E3 and E4 need to work harder; that is a proposal.
- Subscription conversions to date: any subscription_start events attributed to the campaign.
  At day 7, E4 (the soft subscribe CTA) has not yet sent for most contacts, so this number
  is expected to be small. State it plainly; do not softening.
- Soft bounce and hard bounce rates from E1 and E2: if above expected thresholds (typically
  above 2 percent soft bounce or above 0.5 percent hard bounce), flag for platform review.

Paid acquisition (stream 5, secondary read at day 7):

- Gate completions from paid traffic (submit events, per channel): total and per channel
  (Meta, Google Search, Demand Gen, YouTube, LinkedIn).
- Cost per gate completion per channel vs the planning CPA range (10 to 18 USD blended,
  per media-plan.md section 7). A channel significantly above the range is a flag.
- Video completion rate on any video creative: a creative-quality signal for YouTube and
  Meta Reels. If below expected thresholds, that is a creative swap proposal.
- Meta learning phase status: have the three persona ad sets exited the learning phase?
  If Meta has not exited learning by day 5 to 6, flag at the readout (per media-plan.md
  section 6 planning note).

Conversion path (stream 6):

- Confirm that all 5 tracked events are firing correctly: page_view, gate_view, submit,
  confirm, and subscription_start. Any event not firing is an open item for
  data-tracking-engineer and blocks that metric entirely. Do not fabricate a number where
  the event is dark.

### 2B. Leading indicators and what they signal

| Leading indicator | What it signals | Signal direction |
|---|---|---|
| E1 and E2 CTR above the email category median for the GCC region | Angle and subject line resonating; contacts are engaging before the conversion ask | Positive: E3 and E4 are likely to maintain momentum |
| chapter_1_play count growing across all three persona variants | Contacts are using the free hook; E4 conversion path has a warmer audience | Positive: hold E4 timing, let the play count build |
| Reactivation rate above zero in the never-engaged tier | The warm delayed-entry strategy (E1 on day 2 or 3 for never-engaged) is reaching contacts who had gone dark | Positive: the never-engaged send timing is working |
| Gate completions from paid concentrated in one channel (e.g., Meta) at below-planning CPA | Paid learning phase identified the most efficient channel | Signal to propose concentrating phase 2 budget there |
| Gate completions from paid spread evenly with all channels above planning CPA | No clear winner yet; phase 2 concentration decision needs more data | Signal to hold current allocation and re-evaluate at day 10 |
| E1 open rate flat or zero in a recency tier | Deliverability or subject line issue for that tier | Flag for investigation; propose subject line retry or send-time adjustment |
| subscription_start events at day 7 materially above zero | Early conversions before E4 sends (contacts converting on E1 to E3 alone) | Positive signal; note which persona and recency tier for the report |

### 2C. Decision points at the day-7 readout

Each decision point below is a PROPOSAL to the human gate. None is enacted without Ahmed's
explicit approval. The analytics-reporter frames the proposal; the human gate decides.

| Decision point | Trigger condition | Proposed action (human gate proposal only) |
|---|---|---|
| Concentrate phase 2 paid budget on the winning channel | One paid channel is delivering gate completions at less than 50 percent of planning CPA range with more than 30 gate completions to date | Propose reallocating phase 2 budget toward the winning channel, per the illustrative phase 2 table in media-plan.md section 6 |
| Pause a paid channel with zero gate completions at day 7 | A channel has spent more than one-third of its phase 1 allocation with zero gate completions (e.g., Google Demand Gen at zero confirms low intent signal) | Propose pausing that channel and reallocating its remaining phase 2 budget to the top performer |
| Move E3 send time earlier for a specific persona | E2 CTR is high for a persona but chapter_1_play count is low, suggesting the journey stalls between E2 and the member platform | Propose moving E3 forward by 1 day for that persona variant |
| Add a subject line retry to E3 | E3 open rate falls more than 30 percent below E1 open rate for the same recency tier | Propose an alternate subject for E3 (a new copy variant; single variable change; goes to human gate) |
| Activate or defer the lookalike audience on Meta | Gate completions from Meta phase 1 have reached 100 or more (the minimum seed threshold from media-plan.md section 4) | Propose activating a 1 to 3 percent lookalike in Saudi Arabia for phase 2 |
| Hold all changes | All channels are within planning CPA range, CTR is on track, chapter_1_play is growing | Propose no action; let phase 2 run on the existing plan |

---

## 3. A/B test plan

Three tests are designed here. Each test changes exactly one variable, ties its hypothesis to
the success_metric or a secondary metric, and states a stop rule. Each is a proposal for the
human gate. No test runs without Ahmed's approval. The 2-week flight is short; all three tests
carry a minimum-signal caveat.

All three tests are designed for the lifecycle email layer and the paid layer. The subject
line test and the hook angle test are the highest-signal opportunities given the 2-week window
and the campaign's lifecycle-first design.

---

### Test 1: E1 subject line A vs B (lifecycle email)

Internal artifact. One variable. Uses the ab-test-plan template.

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: analytics-reporter
- stream: 8 monitoring and optimization
- status: draft
- motivated by: the E1 subject line is the single highest-leverage copy variable in the
  lifecycle flow. The lapsed-engaged and never-engaged tiers (the majority of the 18,000
  non-payers by definition) will not engage with any downstream content unless E1 opens.
  The subject line test is therefore directly upstream of every secondary metric in the
  success_metric tree.

Variable under test (exactly one): the E1 email subject line (AR primary).
All other elements of E1 (body, CTA, send timing, from name) are held constant.
The EN variant subject line is tested simultaneously in parallel with the same split logic,
but it is a separate, smaller pool and its results are read separately; it does not combine
with the AR pool for the verdict.

- success_metric (restated): email CTR (clicks per delivered) on E1, as the leading
  secondary metric upstream of chapter_1_play and subscription_start. Because subscription
  conversions require the full 14-day window to accumulate, CTR is the correct proxy for
  the E1 test inside a 2-week flight. It is not a vanity metric; it is the direct leading
  indicator the lifecycle flow branches on.

- hypothesis: Changing the E1 AR subject line from the myth-flip formulation (variant A,
  "السوق لا يكافئ أفضل استراتيجية. يكافئ التي يختارها الناس." from copy-package.ar.md
  subj-e1) to the direct-pain-question formulation (variant B, the alternate subject from
  copy-package.ar.md, subj-e1 alt B: "درس واحد يغير طريقة تفكيرك في التسويق") will
  increase E1 CTR in the lapsed-engaged and never-engaged tiers, because the pain-question
  frame names the reader's problem explicitly and is more likely to generate a click from
  contacts who have low prior engagement with Maharat.

Variants:

| Variant | Subject line (AR) | The one thing that differs |
|---|---|---|
| A (control) | "السوق لا يكافئ أفضل استراتيجية. يكافئ التي يختارها الناس." (myth-flip, from copy-package.ar.md subj-e1) | Baseline subject line |
| B | "درس واحد يغير طريقة تفكيرك في التسويق." (direct pain-question, from copy-package.ar.md subj-e1 alt B) | Subject line framing only |

- split: 50 percent A, 50 percent B, randomized at the contact level within each recency tier
- audience: all recency tiers within the owned non-payer list who are eligible for E1. The
  verdict is read per-tier (recently-active, lapsed-engaged, never-engaged) because the
  baseline open rate differs across tiers. A single blended verdict would obscure the signal.
- window: E1 send on flight day 1 to day 2 (proposed 2026-06-08 to 2026-06-09). CTR measured
  72 hours after the last E1 send in the window (proposed 2026-06-12).

Sample size and method:

- baseline rate: E1 CTR baseline for this audience is not known from prior data (no prior
  Maharat email campaign data is in context). A planning baseline of 3 percent CTR is a
  conservative estimate for a non-payer lifecycle audience in the GCC education category.
  This is a planning assumption; the actual baseline will be observable from the A arm on
  day 2 to 3 of the flight and should be updated before committing to the verdict threshold.
- minimum detectable effect: 1.5 percentage points absolute improvement (from 3 percent to
  4.5 percent CTR). This is the smallest lift worth adjusting the remaining lifecycle sends for.
- derived per-arm sample size: for a two-proportion z-test at 95 percent significance (one-sided,
  B is the treatment) and 80 percent power, with baseline 0.03 and MDE 0.015 absolute, the
  per-arm sample size is approximately 2,100 contacts. The total required is approximately
  4,200 contacts across both arms. Given the planning estimate of about 18,000 eligible
  non-payers, this threshold is achievable if the actual sendable list after suppression is at
  least 4,200.
- significance level or method: fixed-horizon test at 95 percent significance (one-sided z-test).
  No peeking before the 72-hour window closes.
- chosen before launch: yes. Method and stop rule fixed here, before any send.

Stop rule:

- stop condition: 72 hours after the last E1 send in the window (proposed 2026-06-12),
  provided each arm has received at least 2,100 deliveries (per-arm minimum). If the sendable
  list is below 4,200, the test is inconclusive by design; report that result honestly.
- decision threshold: if B achieves a CTR at least 1.5 percentage points above A and the
  difference is statistically significant at 95 percent (one-sided), B is the winner.
- what happens at the threshold: if B wins, propose applying the B subject line to the E3
  re-send (the subject-line retry for E1 non-openers) and flagging it for the next campaign's
  subject line default. If A wins or result is inconclusive, keep A as the default and note
  the result in the learnings log.

Minimum-signal caveat for a 2-week flight: if deliverability or suppression reduces the
net sendable list below 4,200, this test will not produce a statistically meaningful result.
In that case, report it as an observation (not a banked learning) in the learnings log and
run a properly powered version in the next campaign.

Human-gate proposal: this test runs only after Ahmed approves it. The analytics-reporter
does not launch the test, split the audience, or change any live send. Approval of this
plan authorizes the platform operator to route the E1 send to a 50/50 split within the
eligible audience on the confirmed start date.

Open items:
- The email platform (Ortto or HubSpot) must be confirmed before the split can be wired.
- The actual sendable list size after suppression must be confirmed at build.
- The baseline CTR from any prior Maharat email sends should be provided by
  data-tracking-engineer if available, to replace the 3 percent planning assumption.

---

### Test 2: Paid hook angle A vs B (Meta prospecting, persona-2 self-taught builders)

Internal artifact. One variable. Uses the ab-test-plan template.

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: analytics-reporter
- stream: 8 monitoring and optimization
- status: draft
- motivated by: the media plan runs three persona ad sets on Meta in phase 1, each with a
  distinct creative hook. The persona-2 (self-taught builders) ad set uses the myth-flip hook
  ("السوق لا يكافئ أفضل منتج"). The strategy-artifact and copy-package also support a
  direct-promise hook for this persona. Testing the two frames within persona-2's ad set
  gives the clearest read on which creative angle drives more gate completions from this
  segment, without confounding it with persona or targeting differences.

Variable under test (exactly one): the primary headline copy hook in the Meta ad creative
for the persona-2 self-taught builders prospecting ad set. Image, body copy, CTA button,
audience targeting, placement, and bid strategy are all held constant.

- success_metric (restated): signup-gate completions (submit events) from paid traffic
  in the persona-2 Meta ad set. This is the paid secondary metric in the success_metric
  hierarchy. Gate completions from paid feed the lifecycle, which drives the primary metric.

- hypothesis: Changing the primary headline hook for the persona-2 Meta ad from the myth-flip
  frame (variant A: "السوق لا يكافئ أفضل منتج، بل المنتج الذي يعرف كيف يتكلم.") to the
  direct-promise frame (variant B: "تعلّم كيف تجعل السوق ينتبه لما بنيته.") will increase
  gate completions from the persona-2 ad set, because the direct-promise frame names the
  desired outcome (the market noticing what they built) and may reduce the cognitive step
  needed to click from the abstract myth-flip formulation.

Variants:

| Variant | Headline hook | The one thing that differs |
|---|---|---|
| A (control) | "السوق لا يكافئ أفضل منتج، بل المنتج الذي يعرف كيف يتكلم." (myth-flip, from strategy-artifact section 2 and copy-package persona-2 hook) | Baseline hook for this ad set |
| B | "تعلّم كيف تجعل السوق ينتبه لما بنيته." (direct-promise, derived from the strategy-artifact persona-2 angle "make people care") | Headline hook framing only |

Note: both hooks are within the approved brand framing (empowering, no deficit, no
held-back claims, no revenue promise). The variants are copy direction, not approved
final copy. The actual ad copy units must go through the stream 4 copy gate and brand-qa
before any ad is built or launched.

- split: 50 percent A, 50 percent B, within the persona-2 prospecting ad set only.
  Meta's A/B test tool (creative split test) is the preferred mechanism; ad-set-level
  ABO holds the total allocation constant so neither variant cannibalizes the other.
- audience: persona-2 self-taught builders prospecting audience in Saudi Arabia and UAE,
  as defined in media-plan.md section 4, held identical for both variants.
- window: phase 1 of the flight, days 1 to 7 (proposed 2026-06-08 to 2026-06-14). Results
  read at the day-7 readout.

Sample size and method:

- baseline rate: no prior Maharat paid campaign data exists to anchor a baseline gate
  completion rate for this audience. Planning baseline from media-plan.md: 5 to 10 USD
  planning CPA for Meta prospecting, implying a click-to-conversion rate in the general
  education category. A planning baseline of 5 percent conversion rate (from click to gate
  completion) is a rough anchor; this is a planning assumption only.
- minimum detectable effect: 2.5 percentage points absolute improvement in gate-completion
  rate (from 5 percent to 7.5 percent). This is the smallest lift worth carrying forward to
  phase 2 creative selection.
- derived per-arm sample size: for a two-proportion z-test at 95 percent significance
  (one-sided) and 80 percent power, with baseline 0.05 and MDE 0.025 absolute, the per-arm
  sample size is approximately 1,100 clicks (ad clicks, not impressions). At the persona-2
  Meta allocation of approximately 280 USD phase 1 (rough proportional split of the 875 USD
  Meta phase 1 budget across 3 persona ad sets) and a planning CPM and CTR for the GCC
  Instagram audience, reaching 1,100 clicks per arm within 7 days at this budget level is
  unlikely. The test should therefore be treated as a directional read only, not a conclusive
  statistical test.
- significance level or method: directional read. Given the sample size caveat, the verdict
  is: "B generated more gate completions than A in phase 1 (directional)" rather than a
  statistically significant conclusion. A statistically powered version requires a longer
  flight or a larger per-ad-set budget.
- chosen before launch: yes.

Stop rule:

- stop condition: end of phase 1 (day 7, proposed 2026-06-14), regardless of whether the
  sample size threshold was reached.
- decision threshold: if B generates at least 20 percent more gate completions than A (raw
  count, not rate) in phase 1, propose carrying the B hook forward into phase 2 creative
  across all Meta persona-2 units. If the margin is below 20 percent or the sample is too
  small for a directional read, keep A and log the result as an observation.
- what happens at the threshold: this is a directional proposal to the human gate for phase
  2 creative selection. It does not launch phase 2 creative; the human gate decides.

Minimum-signal caveat: this test almost certainly will not reach statistical significance
in a 7-day phase 1 window at the persona-2 ad set budget level. It is designed as a
directional creative-preference signal only. A statistically valid result requires the next
campaign to run this test with a larger per-persona budget or a longer window.

Human-gate proposal: this test runs only after Ahmed approves it. The analytics-reporter
does not build, upload, or launch any ad. Approval authorizes paid-build-engineer to set up
the creative split within the persona-2 ad set per this plan.

Open items:
- Both variant copy units must pass the stream 4 copy gate (arabic-copy-qa, brand-qa)
  before any ad creative is built.
- Meta Pixel or CAPI must be confirmed live and the gate completion event must be firing
  before this test can measure gate completions.

---

### Test 3: Landing page primary CTA text A vs B

Internal artifact. One variable. Uses the ab-test-plan template.

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: analytics-reporter
- stream: 8 monitoring and optimization
- status: draft
- motivated by: the landing page (conversion-package section 1.2) has a primary CTA button
  in the hero section. The AR variant reads "شاهد الفصل الأول مجانا" (Watch Chapter 1 Free).
  A lower-friction alternative that leads with the cheatsheet ("احصل على ملخص الحملة مجانا",
  Get the Campaign Cheatsheet Free) may drive more gate completions from paid and organic
  traffic who are not yet aware of the class but are interested in practical marketing tools.
  This tests whether the lead magnet framing converts better than the Chapter 1 free framing
  as the primary CTA for cold traffic.

Variable under test (exactly one): the primary CTA button text in the landing page hero
(AR variant). All other page elements (headline, subhead, layout, gate form, value cards)
are held constant.

- success_metric (restated): signup-gate completions (submit events) from all inbound paid
  and organic traffic to the landing page. Gate completions are the direct conversion the
  landing page optimizes toward (conversion-package section 1), and they are the paid
  secondary metric in the success_metric hierarchy.

- hypothesis: Changing the primary hero CTA from "شاهد الفصل الأول مجانا" (Chapter 1 free
  hook, variant A) to "احصل على ملخص الحملة مجانا" (cheatsheet hook, variant B) will
  increase gate completions from paid cold traffic, because the cheatsheet is a tangible,
  immediately useful deliverable that reduces the perceived commitment for a visitor who
  is not yet ready to watch a video class, and the cheatsheet offer is confirmed and available
  (from the brief).

Variants:

| Variant | CTA button text (AR) | The one thing that differs |
|---|---|---|
| A (control) | "شاهد الفصل الأول مجانا" (from copy-package.ar.md LP-primary-CTA, verified) | Baseline CTA |
| B | "احصل على ملخص الحملة مجانا" (cheatsheet lead as the primary CTA hook) | CTA button text only |

Note: variant B must be produced as a copy unit by copywriter-ar, pass arabic-copy-qa and
brand-qa before it is placed on the page. This test plan is the brief for that copy unit.
The conversion-engineer (stream 6) wires the page variant; data-tracking-engineer confirms
that the submit event fires identically for both variants.

- split: 50 percent A, 50 percent B, randomized at the visitor level by the web platform.
  A and B share the same URL (variant is selected at render time, not via separate URLs, to
  avoid UTM contamination between arms).
- audience: all inbound paid and organic traffic to the landing page from all channels during
  the flight. Traffic source is recorded via UTM but not used to split the audience; the
  test measures the aggregate conversion effect of the CTA change across all cold traffic.
- window: full 14-day flight (proposed 2026-06-08 to 2026-06-21). The gate_view event
  (visitor sees the gate) is the denominator; submit is the numerator. Both events must be
  confirmed live before the test begins.

Sample size and method:

- baseline rate: gate completions divided by gate_view events (visitors who see the gate
  section). No prior data. Planning baseline of 15 percent gate-to-submit rate is a planning
  assumption for a warm, intent-matched landing page with a free-access offer.
- minimum detectable effect: 5 percentage points absolute improvement (from 15 percent to
  20 percent gate-to-submit rate). This is the smallest lift worth a permanent CTA change.
- derived per-arm sample size: for a two-proportion z-test at 95 percent significance
  (two-sided, because either direction is relevant here) and 80 percent power, with baseline
  0.15 and MDE 0.05 absolute, the per-arm sample size is approximately 400 gate_view events.
  Total required: approximately 800 gate_view events (400 per arm). Given the planning
  estimate of 280 to 500 total gate completions from paid (media-plan.md section 7), and
  assuming a gate_view-to-submit rate of roughly 15 percent, the implied total gate_view
  events across the full flight would be approximately 1,900 to 3,300. Reaching 800 across
  both arms is achievable if the paid and organic traffic drives sufficient page visits.
- significance level or method: fixed-horizon two-sided z-test at 95 percent significance.
  No peeking before the flight closes on day 14.
- chosen before launch: yes.

Stop rule:

- stop condition: end of the 14-day flight (proposed 2026-06-21), provided each arm has at
  least 400 gate_view events. If either arm is below 400, the test is inconclusive; report
  as an observation.
- decision threshold: if B achieves a gate-to-submit rate at least 5 percentage points above
  A and the result is statistically significant at 95 percent, B is the winner.
- what happens at the threshold: if B wins, propose adopting the B CTA as the default for
  the next campaign's landing page and for any paid campaign retargeting units that use the
  landing page as a destination. If inconclusive, keep A and log as an observation.

Minimum-signal caveat: this test depends on sufficient paid and organic traffic reaching the
landing page. If the actual paid traffic volume is toward the low end of the planning range
(280 gate completions implies fewer total visits), the per-arm gate_view threshold may not
be reached. In that case, report the direction only and repeat with a larger traffic volume.

Human-gate proposal: this test runs only after Ahmed approves it. The conversion-engineer
builds the variant B page copy after it passes the QA gate. The analytics-reporter does not
change the live page. Approval authorizes conversion-engineer to stage the 50/50 split and
data-tracking-engineer to confirm both submit events fire identically across variants.

Open items:
- Variant B CTA copy must be authored by copywriter-ar and pass arabic-copy-qa and brand-qa.
- The gate_view event must be confirmed live (data-tracking-engineer) before the test begins.
- The page split mechanism requires the web platform to support session-level randomization
  without separate URLs; confirm with conversion-engineer and data-tracking-engineer at build.
- Cheatsheet download URL must be confirmed (brief open item) before the B variant CTA can
  point to the correct post-submit delivery.

---

## 4. End-of-flight report template (stream 9, campaign-report)

This section defines the structure of the report-artifact that analytics-reporter will
produce at the end of the 14-day flight. It uses the campaign-report template from
skills/09-reporting-learning/campaign-report/templates/campaign-report.md, extended to
this campaign's specifics.

The report is written after the flight closes (proposed 2026-06-21 or the confirmed end date).
It measures against the success_metric from strategy-artifact section 7. No metric invented
after the fact. No vanity metrics in the results table.

### 4A. Report envelope (stream 9 artifact)

- campaign_id: 2026-06-elda-choucair-marketing
- produced_by: analytics-reporter
- stream: 9 reporting and learning
- status: draft (at time of writing; advances to qa-passed after skill eval)
- window reported: 2026-06-08 to 2026-06-21 (ASSUMPTION; update to confirmed dates)
- data sources: BigQuery (subscription events, email engagement, UTM attribution),
  GA4 (page events, gate completions, purchase), email platform (Ortto or HubSpot, once
  confirmed), Meta Events Manager, Google Ads, LinkedIn Campaign Manager.
  All tools require data-tracking-engineer confirmation and Ahmed's approval before use.

### 4B. Success metric restated (this is the only bar)

At time of report writing, the success_metric from strategy-artifact section 7 is:

Primary: subscription conversions attributable to the campaign (new paid plan starts, via
lifecycle and paid/organic routed through the gate), with lifecycle-first attribution.

Secondary: lifecycle email CTR and reactivation; Chapter 1 plays; signup-gate completions
from paid and organic.

TARGET NUMBER AND DATE: not supplied. If Ahmed has not supplied the target number and
measurement date by the time this report is written, the results section states actual values
only and explicitly notes that a pass/fail verdict against a target is not possible until the
target is set. The report does not fabricate a verdict.

### 4C. What the results section reports

| Metric | What to report | Source | Notes |
|---|---|---|---|
| Primary: subscription conversions (lifecycle-attributed) | Actual count of subscription_start events attributed to campaign_id "2026-06-elda-choucair-marketing" via email channel | BigQuery, Stripe (if accessible), GA4 purchase | If subscription_start event not confirmed live, flag as open item; do not fabricate |
| Primary: subscription conversions (paid-attributed) | Actual count of subscription_start events where source UTM is a paid channel and the contact completed the gate during the flight | BigQuery (UTM joined to subscription_start) | Separated from lifecycle-attributed count for clarity; the two may overlap if a contact received an email AND came via paid before subscribing; lifecycle-first attribution gives the lifecycle the credit in that case |
| Secondary: lifecycle email CTR per step | CTR (clicks per delivered) for each of E1 to E5, per persona variant and per recency tier | Email platform export, BigQuery | If a step was not sent (e.g., E5 for contacts who converted earlier), note the send count and excluded contacts |
| Secondary: reactivation rate | Percentage of lapsed-engaged and never-engaged contacts who opened or clicked at least one message | Email platform, BigQuery | Denominator: contacts in those tiers who received E1. Numerator: contacts who opened or clicked any message |
| Secondary: Chapter 1 plays | Total chapter_1_play events during the flight, traced to campaign_id | BigQuery, GA4 | If event not confirmed live, flag as open item |
| Secondary: gate completions from paid | Total submit events with paid UTM source during the flight | GA4, BigQuery, Meta Events Manager, LinkedIn Campaign Manager | Per-channel breakdown where data is available |
| Secondary: gate completions from organic | Total submit events with organic_social UTM source | GA4, BigQuery | |

### 4D. What the results section excludes (explicit)

The following are excluded from the results table and from any verdict on campaign success:
- Impressions, reach, CPM on paid channels.
- Email open rate as a standalone verdict.
- Social follower count, post likes, or engagement rate.
- Page views to the landing page without a downstream action.
- Video completion rates on paid creative (these appear in the day-7 readout as paid
  optimization signals, not in the end-of-flight report as results).

### 4E. What worked and what to change (structure)

what_worked: each finding states the evidence (number, source, window). No finding without
a number behind it. Examples of the kinds of findings the report may contain, written as
structural slots, not fabricated results:

- "Lifecycle email CTR was [X] percent for persona-1 (data-driven marketers), higher than
  persona-2 and persona-3, evidence: [email platform export, E1 to E3 sends, 2026-06-08
  to 2026-06-17]."
- "Recently-active tier reactivation rate was [X] percent, above the planning assumption,
  evidence: [BigQuery, recency-tier tag joined to email_open events, full flight window]."

All findings are filled at report-writing time from actual data. No number is placed here now.

what_to_change: each change is for the next brief. Each change carries an owner and a target
date or target brief. Examples of the structural slots:

- Send E4 (the decision email) earlier in the sequence for contacts who have already played
  Chapter 1 (if chapter_1_play events cluster earlier than day 8 to 10). Owner: lifecycle-
  architect. Target brief: next campaign brief.
- Adjust persona-2 (self-taught builders) creative hook based on the Test 2 directional
  result. Owner: copywriter-ar and performance-marketer. Target brief: next campaign brief.
- Any structural change to the landing page CTA based on Test 3 result. Owner:
  conversion-engineer and copywriter-ar. Target brief: next campaign brief.

What to change is populated at report-writing time from actual data. No recommendation
is fabricated now.

### 4F. Vanity metric exclusion statement (explicit, in the report)

The campaign-report includes an explicit line: "The following metrics are excluded from the
results and from the success verdict because they are not part of the success_metric the
strategy set: [list from 4D above]. They are not reported and do not affect the verdict."

### 4G. Learnings-log structure

After the campaign-report is written, the reusable learnings are appended to the learnings
log. The learnings log lives at a location to be confirmed at build (proposed path:
outputs/learnings-log.md or context/learnings-log.md; confirm with Ahmed). Each learning
must be portable: no offer, price, Skill Path title, or instructor name baked in. Each
learning carries the evidence (number, source, window) and the campaign_id.

The learnings-log reference in the report-artifact body:
- learnings_log_ref: [learnings-log.md#2026-06-elda-choucair-marketing], once the log path
  is confirmed and the entry is appended.

Findings without a metric behind them go into the "Observations" section of the learnings
log, not the banked learnings section. They stay there until evidence exists.

---

## 5. Data dependencies

The framework is built; the read cannot happen until these are live. Every dependency below
is co-owned with data-tracking-engineer and confirmed at build.

| Dependency | What it enables | Owner | Status |
|---|---|---|---|
| All 5 conversion events firing and confirmed (page_view, gate_view, submit, confirm, subscription_start) | Any metric in the metric tree | data-tracking-engineer | Pending; conversion-package section 3.6 test plan not yet run |
| Email engagement events confirmed in the platform schema (email_open, email_click, email_delivered, chapter_1_play, cheatsheet_download, subscription_start, flow_entry) | All lifecycle metrics (CTR, reactivation, chapter plays) | data-tracking-engineer, in coordination with lifecycle-architect | Pending; lifecycle-package section 6B events not yet co-designed and confirmed |
| BigQuery schema confirmed and tables live | Attribution queries joining email events to subscription_start; UTM joins | data-tracking-engineer | Not yet enabled; BigQuery access requires Ahmed's approval in settings.json |
| GA4 Measurement ID confirmed and events mapped | Web funnel events (page_view, gate_view, submit, confirm, purchase) | data-tracking-engineer | Pending; conversion-package section 3.4 to-confirm items outstanding |
| Meta Events Manager: Pixel ID confirmed and gate completion (Lead) event firing | Cost per gate completion per channel; Meta retargeting readiness | data-tracking-engineer | Pending; pixel deployment blocked on gate platform confirmation |
| Email platform confirmed (Ortto or HubSpot) | Any email metric (delivered, CTR, reactivation) | Ahmed (platform decision) | Hard blocker; platform not named |
| Suppression list confirmed | Accurate send size and denominator for all lifecycle rates | Ahmed and data team | Hard blocker |
| Google Analytics 4 and Ads conversion tracking for paid channels | Cost per gate completion per channel (Google Search, Demand Gen, YouTube) | data-tracking-engineer | Pending |
| LinkedIn Insight Tag confirmed | Gate completions attributed to LinkedIn paid | data-tracking-engineer | Pending |
| Mobile event mapping (Apple IAP, Google Play) | Mobile subscription attribution | data-tracking-engineer | Open item; no guess; cannot claim mobile attribution until confirmed |
| BigQuery, GA4, and Stripe on the settings.json allowlist | Live data queries from this agent | Ahmed (approval in settings.json) | Not yet enabled; required before any live read |

No number is fabricated where a dependency is unresolved. If an event is not confirmed live,
the metric it measures is flagged as an open item in the report, not stated.

---

## 6. Open items

Ordered by blocking severity for this plan.

1. SUCCESS METRIC TARGET NUMBER AND DATE (BLOCKING for any success verdict). Not supplied.
   Ahmed must provide both before stream 8 can measure the campaign against a target and
   before the human gate can judge success. This is the first open item and is restated in
   the strategy-artifact section 7. Owner: Ahmed.

2. EMAIL PLATFORM CONFIRMATION (HARD BLOCKER for all lifecycle metrics). Ortto vs HubSpot,
   Arabic RTL concern unresolved. Blocks all email engagement events, email CTR, reactivation
   rate, and the E1 subject line A/B test. Owner: Ahmed.

3. BIGQUERY, GA4, AND STRIPE ACCESS (HARD BLOCKER for live reads). These tools are not on the
   settings.json allowlist. No live data query is possible until Ahmed approves access. Owner:
   Ahmed.

4. ALL 5 CONVERSION EVENTS CONFIRMED LIVE (BLOCKING for all paid and conversion metrics).
   page_view, gate_view, submit, confirm, subscription_start must be confirmed firing by
   data-tracking-engineer before any metric in the paid secondary reads is valid. Owner:
   data-tracking-engineer.

5. LIFECYCLE EMAIL EVENTS CO-DESIGNED AND CONFIRMED (BLOCKING for all email secondary metrics).
   The 8 events in lifecycle-package section 6B (email_open, email_click, chapter_1_play,
   cheatsheet_download, subscription_start, email_delivered, email_bounced_soft, flow_entry)
   must be confirmed with data-tracking-engineer. Owner: data-tracking-engineer.

6. START DATE AND END DATE CONFIRMED (ASSUMPTION). The measurement window, the day-7 readout
   date, and all A/B test windows shift proportionally. Owner: Ahmed.

7. TEST 1 INFRASTRUCTURE (BLOCKING for E1 subject line test). The email platform (item 2)
   must be confirmed before the A/B split can be wired. The sendable list size must be
   confirmed at build to validate the per-arm sample size. Owner: platform operator /
   data-tracking-engineer.

8. TEST 2 COPY APPROVAL (BLOCKING for paid hook angle test). Variant B copy must be authored
   by copywriter-ar and pass arabic-copy-qa and brand-qa before paid-build-engineer can build
   the ad creative. Owner: copywriter-ar, arabic-copy-qa reviewer, brand-qa-reviewer.

9. TEST 3 VARIANT B COPY AND PAGE SPLIT MECHANISM (BLOCKING for landing page CTA test).
   Variant B CTA copy must pass the QA gate. The web platform's support for session-level
   randomization without separate URLs must be confirmed by conversion-engineer and
   data-tracking-engineer. Cheatsheet URL must be confirmed. Owner: copywriter-ar, conversion-
   engineer, data-tracking-engineer, content team.

10. MOBILE EVENT MAPPING (OPEN ITEM). Apple IAP and Google Play subscription attribution is
    not confirmed. Mobile subscription conversions cannot be attributed until this is resolved
    by data-tracking-engineer. No guess; flag as an open item in any report where mobile
    attribution is needed.

11. LEARNINGS LOG PATH (OPEN ITEM). The file path for the durable learnings log is not
    confirmed. Confirm with Ahmed before the end-of-flight report appends to it. Owner: Ahmed.

12. FORMAL CATALOG STATUS FOR ELDA (OPEN ITEM). Pending team confirmation. Does not block this
    monitoring plan; surface at the human gate. Owner: Maharat team.

---

## 7. Skill eval self-check

### Stream 8 (08-monitoring-optimization/evals/evals.json)

| Check id | Rule | Self-assessment |
|---|---|---|
| frontmatter-shape | YAML frontmatter name and description match the directory | Pass: this plan is an artifact of skills/08-monitoring-optimization; envelope is present |
| routes-to-subskills | Hub routes to performance-readout and ab-test-plan | Pass: section 2 is the performance-readout structure; section 3 contains three ab-test-plan instances |
| measure-against-strategy-metric | Every read measured against the strategy-artifact success_metric | Pass: sections 1 through 3 all measure against strategy-artifact section 7; no metric invented after the fact |
| no-vanity-metrics | Vanity metrics excluded | Pass: section 1C explicitly lists and excludes all vanity metrics; they do not appear in any results table |
| propose-not-act | All optimization moves are proposals to the human gate | Pass: section 2C and all three A/B test plans state explicitly that no action is taken without Ahmed's approval |
| internal-gate-only | Skill eval is the gate; arabic-copy-qa and brand-qa only if customer-facing copy appears | Pass: this is an internal artifact; no customer-facing copy is authored here |
| no-em-dash | No em dash character | Pass: verified in this file |
| western-numerals | Western numerals only | Pass: verified; no Eastern Arabic numerals |
| no-tatweel | No tatweel or kashida | Pass: verified in this file |

### Stream 9 (09-reporting-learning/evals/evals.json)

| Check id | Rule | Self-assessment |
|---|---|---|
| frontmatter-shape | YAML frontmatter name and description match the directory | Pass: this plan is an artifact of skills/09-reporting-learning; envelope is present |
| routes-to-subskills | Hub routes to campaign-report and learnings-log, in order | Pass: section 4 is the campaign-report template; section 4G is the learnings-log structure |
| emits-report-artifact | Hub names the report-artifact and its four body fields | Pass: section 4 states results, what_worked, what_to_change, and learnings_log_ref as the report body |
| measure-against-strategy-metric | Results measured against the strategy-artifact success_metric | Pass: section 4B restates the success_metric exactly from strategy-artifact section 7; no metric invented |
| no-vanity-metrics | Vanity metrics excluded | Pass: section 4D explicitly lists and excludes all vanity metrics from the results table |
| propose-not-act | What to change is a recommendation, not an action on a live campaign | Pass: section 4E states each what_to_change item is for the next brief, carries an owner and target brief, and is not an action |
| internal-gate-only | Skill eval is the gate; arabic-copy-qa and brand-qa only if customer-facing copy appears | Pass: this is an internal artifact |
| no-em-dash | No em dash character | Pass: verified |
| western-numerals | Western numerals only | Pass: verified |
| no-tatweel | No tatweel or kashida | Pass: verified |

---

## Handoff

This plan hands forward to:
- data-tracking-engineer: the event dependency list in section 5. Every metric in this plan
  is blocked on the events in that table. data-tracking-engineer must confirm each event
  is live and firing before any number in this plan can be read.
- conversion-engineer (stream 6): the Test 3 landing page CTA split requires a page variant
  and the session-level randomization mechanism.
- copywriter-ar and stream 4: the Test 2 paid hook angle B copy and the Test 3 CTA B copy
  must be authored and pass the full QA gate before any test is staged.
- human gate: all three A/B tests and all day-7 optimization proposals go to Ahmed via the
  human gate before any action is taken on the live campaign.
- next campaign's strategy-lead: the stream 9 report-artifact (from section 4) feeds the
  next campaign brief with results and learnings.

Nothing in this plan changes a live campaign, sends a message, or spends. All of it is
design-ready and proposals only. Ahmed decides what runs and when.

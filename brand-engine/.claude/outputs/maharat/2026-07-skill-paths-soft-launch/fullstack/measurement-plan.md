# Measurement plan: Skill Paths first-time soft launch

Reasoning and monitoring artifact. Owned by analytics-reporter. Nothing here sends, publishes,
or spends. All event references are marked pending until tracking-plan.md is delivered by
data-tracking-engineer. No targets are invented; numeric targets are an open item carried from
the strategy-artifact for Ahmed to confirm. No em dashes. Western numerals.

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: analytics-reporter
- stream: 8 performance monitoring and test planning
- status: draft
- qa:
  - skill_eval: pass (structure and completeness verified below)
  - arabic_qa: na (internal artifact, not customer-facing)
  - brand_qa: na (internal artifact; brand-qa-reviewer runs on downstream customer-facing assets)
- open_items:
  - tracking-plan.md not yet delivered by data-tracking-engineer. All event references in this
    plan are pending. The measurement plan structure is complete; the live readout is blocked
    until events flow.
  - Numeric success-metric target (primary signups plus installs, cost per signup): not set in
    the brief. Carried as an open item to the human gate for Ahmed to confirm. No target
    invented here.
  - Currency for cost-per-signup calculation: SAR vs USD unresolved. Cost metric is structurally
    defined below but cannot be computed until currency is confirmed.
  - App audience size: open item from strategy-artifact. Affects app-push contribution sizing.
  - Gate platform confirmation: blocks signup event wiring and therefore signup-count accuracy.
- brief_refs:
  - success_metric: strategy-artifact section "Success metric" (primary: early-access signups
    plus campaign-attributable app installs, 2026-07-01 to 2026-07-14)
  - window: 2026-07-01 to 2026-07-14 (14-day flight, supplied by Ahmed)
  - objective: build early-access cohort and prime for full launch
  - segments: owned non-payers (segment 1), new acquisition (segment 2), retargeting (segment 3)

---

## 1. The success metric this plan measures against

The strategy-artifact defines the primary success metric as:

> Early-access signups (gate completions) plus campaign-attributable app installs, across the
> 2026-07-01 to 2026-07-14 flight.

This plan measures exactly that. No metric is substituted or added after the fact.

Secondary metrics defined by the strategy-artifact, measured alongside the primary:

- Cost per signup (paid channels only, resolves once currency is confirmed by Ahmed).
- Activation rate: share of signups who reach a first lesson or first streak day. This is the
  signal that the cohort built is a usable warm base, not just an email list.
- Owned-flow engagement: open rate, click rate, and signup rate on the lifecycle email flow.
- Organic contribution: saves, shares, profile visits, and gate referrals from organic social.

Metrics measured here are grounded in events defined by the tracking plan. Until tracking-plan.md
is final, all event references below are marked "(pending tracking-plan.md)".

---

## 2. Event map: what must fire for each metric to be readable

The events below are the ones the tracking-plan.md defines (per the conversion-package
event_plan schema and the handoff contract). Each is marked pending until that file is
delivered and verified by data-tracking-engineer.

| Metric | Driving event | Where it fires | Status |
|---|---|---|---|
| Early-access signups | confirm (gate completion) | Landing page gate, post-submit confirmation | Pending |
| App installs (campaign-attributable) | app_install with campaign UTM or campaign attribution | App store install + first app open | Pending |
| Cost per signup | confirm event count vs paid spend | BigQuery aggregation after confirm events flow | Pending |
| Activation rate | first_lesson_start or first_streak_day (post-signup) | In-app, post-install | Pending |
| Gate funnel drop-off | page_view, gate_view, submit, confirm sequence | Landing page | Pending |
| Owned flow open rate | email_open (or equivalent from the email platform) | Email platform, owned send | Pending |
| Owned flow click rate | email_click | Email platform, owned send | Pending |
| Owned flow signup rate | confirm events attributable to the owned-flow UTM | Gate confirm, owned-flow attribution | Pending |
| Organic gate referrals | page_view with organic-social UTM source, then confirm | Landing page, referral attribution | Pending |
| Paid ad engagement (secondary) | link_click, video_view at 50 percent and 75 percent, in-feed engagement | Meta, TikTok, Google platform events | Pending |

Note: no personal or sensitive data in URL parameters. UTM parameters carry channel, source, and
medium attribution only, per the standing guardrail.

Data-tracking-engineer owns the wiring of these events, the pixel and CAPI mapping, the GA4
mapping, and the BigQuery warehouse queries behind the readouts. This agent reads the resulting
data; it does not define or wire it.

---

## 3. Monitoring cadence across the 14-day flight

The flight runs 2026-07-01 to 2026-07-14. Three structured check-ins are defined below.
Each produces a readout of metrics against the success metric, surfaces anomalies, and where
needed generates a proposal to the human gate. This agent never changes a live campaign or
spend; every optimization move is a proposal.

### Check-in 1: Launch check (Day 2, 2026-07-03)

Purpose: confirm tracking is live and events are firing correctly before meaningful spend
accumulates. Catch misconfigured pixels, broken UTMs, or missing event signals early.

What to read at Day 2:
- Event firing check: are page_view, gate_view, submit, and confirm events arriving in the
  warehouse? Zero-count on any of these is a stop and a route to data-tracking-engineer, not
  an assumption that no one signed up.
- Paid channel delivery: are ads out of the learning phase and delivering impressions? If a
  channel is not delivering, flag it to the human gate as a proposal to review targeting or
  creative.
- Signup count vs any indicative daily run rate: not a definitive read at Day 2, but a sanity
  check that the funnel is open and events are recording.
- Owned-flow send status: were lifecycle emails sent on Day 1 as scheduled? Open rate at Day 2
  is an early signal, not conclusive.
- App push delivery: did the push sequence fire? Delivery rate noted, not acted on yet.

Output of the launch check: a brief written readout (no invented numbers, unknowns flagged as
open items), plus any blocking event-data issue routed immediately to data-tracking-engineer.

### Check-in 2: Mid-flight (Day 7, 2026-07-07)

Purpose: a substantive read on performance. Enough data to see the signup curve, funnel
efficiency by channel, and whether the owned-flow contribution is clear. The basis for any
optimization proposal.

What to read at Day 7:
- Primary metric progress: cumulative gate completions (confirm events) and app installs to
  date, by source (paid, owned flow, organic).
- Funnel conversion rate: page_view to gate_view to submit to confirm, by channel. A large
  drop at any step is the signal that copy or the gate page needs attention; a proposal goes
  to the human gate, not a direct change.
- Cost per signup to date (once currency is confirmed): are paid channels acquiring at an
  acceptable efficiency? If one channel is materially outperforming another, that is a proposal
  to shift budget, routed to the human gate.
- Segment contribution: is segment 1 (owned non-payers) converting through the lifecycle flow?
  Is segment 2 (new acquisition) converting from paid? Is segment 3 (retargeting) contributing
  an incremental lift?
- Owned-flow: click-to-gate rate on the lifecycle sequence. If the flow is underperforming,
  the proposal is a subject-line or send-timing adjustment routed to the human gate.
- Organic: are social posts driving gate referrals? Saves and shares as a leading indicator of
  the full-launch priming goal.
- Activation rate (early read): of signups to date, how many have triggered the first-lesson
  or first-streak-day event? Even a small n at Day 7 is informative for the report.

A/B test status: if a test was approved at the human gate and is running, read the split at
Day 7 against the stop rule defined in the test plan.

Output of the mid-flight check: a full written readout, what is working, what is not, and any
optimization proposals formatted for the human gate. Nothing is actioned without approval.

### Check-in 3: Final read (Day 14, 2026-07-14)

Purpose: the definitive campaign-period read. All metrics against the success metric. The input
to the stream 9 report-artifact.

What to read at Day 14:
- Final primary metric: total gate completions and campaign-attributable app installs across the
  14 days, by segment and by channel.
- Final cost per signup per paid channel (once currency confirmed).
- Final activation rate: the share of the early-access cohort that became active learners within
  the flight.
- Full funnel breakdown: end-to-end conversion rates, step by step, for the gate landing page.
- Owned-flow completion: final open, click, and signup rates on the lifecycle sequence.
- Organic contribution summary: total gate referrals attributable to organic social, saves,
  shares, profile-visit lift.
- A/B test conclusion: if a test ran to its stop rule, report the result and the recommendation
  for the full launch. If it did not reach the stop rule, report the direction and the
  recommendation to continue in the full launch.
- Cohort quality indicator: activation rate, because the strategy objective is to prime a warm
  base for the full launch, not just accumulate signups. A cohort that activated is more
  valuable to the full launch than a larger cohort that did not open the app.

Output of the final read: the complete dataset that populates the stream 9 report-artifact.

---

## 4. A/B test candidates

Each test follows the one-variable rule. A clear hypothesis, a defined stop rule, and a route
through the human gate before anything runs. This agent proposes tests; it does not set them
live.

### Test A: Gate page headline variant

Variable: the primary headline on the gate landing page. One version speaks to format benefit
("a skill built one small step a day"). One version speaks to exclusivity framing ("you are
among the first to access this"). One variable only; no other page element changes.

Hypothesis: the benefit-led headline will produce a higher gate_view-to-submit conversion rate
than the exclusivity-led headline, because the acquisition audience (segment 2) responds to
method framing over urgency framing, consistent with the strategy's empowering, never
deficit-framed directive.

What to measure: gate_view-to-submit rate per variant, driven by the submit event (pending
tracking-plan.md).

Stop rule: 14 days (the full flight) or 200 gate_view events per variant, whichever comes
first. If neither arm has a meaningful difference at the stop rule, the default is the
benefit-led headline and the test result is documented in the report as inconclusive.

Gate route: this is a proposal to the human gate. The conversion-engineer builds the variant;
nothing changes on the live page without Ahmed's sign-off.

### Test B: Owned-flow subject line variant (email, segment 1)

Variable: the subject line of the first email in the lifecycle sequence, for the owned
non-payer audience (segment 1 recently-engaged tier). One version leads with the format
("خطوة واحدة كل يوم"). One version leads with the early-access framing. Body copy and send
time do not change.

Hypothesis: the format-led subject line will produce a higher open rate in the recently-engaged
tier, because these contacts already know Maharat and respond to a concrete new-format signal
rather than a generic urgency prompt.

What to measure: open rate per variant from the email platform, then click-through-to-gate rate
as a secondary read.

Stop rule: 48 hours after the first send (within the 14-day flight). Minimum 500 sends per
variant for any read to be meaningful. If the send volume per variant is below 500, the test is
underpowered and that is noted in the report; no winner is declared.

Gate route: this is a proposal to the human gate. The lifecycle-architect builds the split; the
send does not go without Ahmed's sign-off.

### Test C: Paid creative format (social video vs static, segment 2)

Variable: ad creative format on one paid channel (Meta or Instagram, whichever the media plan
designates as primary for segment 2 acquisition). One ad set runs a short video (the streak and
small-step motif in motion). One ad set runs a static card with the same headline and CTA.
Targeting, budget split, bid strategy, and copy are identical across both ad sets.

Hypothesis: the video format will produce a lower cost per gate-completion (confirm event) for
segment 2 new acquisition than the static card, because a short motion treatment better
communicates the bite-sized, daily-step format than a still image.

What to measure: cost per confirm (gate completion) and click-to-confirm rate per format.

Stop rule: 7 days of delivery (assessed at the Day 7 mid-flight check) or 50 confirm events
across both arms combined, whichever comes first. If spend is exhausted before either threshold,
report the directional read and note the test as underpowered.

Gate route: this is a proposal to the human gate. The paid-build-engineer stages both ad sets
paused; neither goes live without Ahmed's sign-off. Budget for the split is within the
confirmed 10,000 total (currency open item) and does not exceed it.

---

## 5. Vanity metrics excluded

These metrics are explicitly excluded from the primary readout. They are not measured against
the success metric. If a downstream request asks for them in isolation, this plan flags them
as vanity in context and redirects to the primary metric.

- Impressions and reach: volume of eyeballs is not a conversion, not a cohort, and not
  activation. Noted for context in the paid readout but not reported as a result.
- Follower count change: social audience growth during the flight is a secondary side effect,
  not the objective. If follows go up but gate referrals do not, the campaign did not work.
- Video views (without a downstream conversion): a view of a TikTok that does not lead to a
  gate visit is not evidence the campaign is working. Video views are a funnel leading indicator
  only, not a result.
- Likes and comments: engagement vanity metrics. Saves and shares have signal value for the
  organic contribution because they indicate intent and distribution; likes and comments on their
  own do not.
- Email list size: the lifecycle send goes to an existing owned list. A higher open rate does
  not make the list bigger. What matters is signup rate from the owned flow.
- Click-through rate on paid ads without a downstream event: a high CTR that does not convert
  to a gate submit or confirm is a sign of a broken funnel or a mismatched creative promise,
  not a win.
- App store rating change: not a campaign-period metric. Relevant post-activation, not during
  a 14-day early-access flight.

---

## 6. Report structure for stream 9 (campaign close)

The stream 9 report-artifact hands the learnings forward to the full-launch strategy-lead.
Structure is defined by the handoff-contract.md report-artifact schema.

### report-artifact envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: analytics-reporter
- stream: 9 reporting and learning
- status: draft (becomes qa-passed after the stream skill eval at campaign close)
- qa: skill_eval, arabic_qa: na (internal), brand_qa: na (internal)
- open_items: any metric blocked on event data not yet flowing at the time of close
- brief_refs: success_metric (strategy-artifact), window (2026-07-01 to 2026-07-14),
  objective (early-access cohort, full-launch priming)

### report-artifact body (template, populated at campaign close)

**results:** total gate completions (confirm events) plus campaign-attributable app installs
vs the strategy-artifact success metric. Presented by segment (owned non-payer, new
acquisition, retargeting) and by channel (paid, lifecycle, organic, app push). Cost per signup
per channel (once currency confirmed). Activation rate: share of the cohort that reached first
lesson or first streak day.

**what_worked:** stated with evidence. For example: if the recently-engaged owned-flow tier
converted at a materially higher rate than the dormant tier, that is stated with the event
counts behind it. If one paid channel produced a lower cost per signup, that is stated with the
spend and confirm numbers. No assertion without the data.

**what_to_change:** concrete and forward-facing. Each item maps to a specific observation.
Examples of the shape (not invented results): if the gate funnel showed a high drop at the
submit step, the recommendation is a gate-page simplification test in the full launch. If
activation rate was low despite high signups, the recommendation is an early-activation push
sequence or an onboarding improvement before the full launch drives more cohort volume.

**learnings_log_ref:** the file where this campaign's learnings are appended for reuse by
future campaigns. The full-launch strategy-lead reads this before setting the full-launch
strategy.

---

## 7. Optimization proposals: shape and routing

Any move that affects the live campaign (pause an ad set, shift budget, change a send time,
add a new creative) is a proposal to the human gate. The format for each proposal:

1. Observation: what the data shows (with the event or metric behind it).
2. Proposed action: one specific change, stated plainly.
3. Expected effect: what metric should improve and why.
4. Risk: what breaks or is lost if the action is wrong.
5. Decision needed from Ahmed: one clear yes or no.

No proposal is acted on by this agent. The swarm assembles the proposal; Ahmed decides.

---

## 8. Skill eval: structure and completeness check

- Success metric confirmed from the strategy-artifact, not invented after the fact. Pass.
- Window confirmed from the brief (2026-07-01 to 2026-07-14, 14 days). Pass.
- Event map present for every metric. All events marked pending tracking-plan.md. Pass (pending
  is honest; invented would be a fail).
- Three monitoring check-ins defined with dates, what to read, and output. Pass.
- Three A/B test candidates, each with one variable, a hypothesis, a stop rule, and a human-gate
  route. Pass.
- Vanity metrics explicitly listed and excluded. Pass.
- Stream 9 report structure defined. Pass.
- Optimization proposals framed as proposals to the human gate, not actions. Pass.
- No em dashes. Western numerals. No invented targets. No invented events. Pass.
- Open items complete: tracking-plan.md pending, numeric target pending, currency pending, app
  audience size pending, gate platform pending. Pass.

Status: skill eval passed.

---

## Handoff

This measurement plan feeds the mid-flight optimization proposals (stream 8) and the
report-artifact at campaign close (stream 9). Data-tracking-engineer must deliver
tracking-plan.md before any live readout is possible. The numeric success-metric target must
be confirmed by Ahmed before performance can be assessed against a bar. Both are open items
routed to the human gate.

The report-artifact at campaign close is handed forward to the full-launch strategy-lead.
Nothing in this plan changes the live campaign or spends.

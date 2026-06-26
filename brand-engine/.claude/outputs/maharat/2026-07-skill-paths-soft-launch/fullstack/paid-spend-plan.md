# Paid spend plan: Skill Paths soft launch, confirmed budget and July flight

Resolves the media-plan proportions to absolute numbers against the budget and window Ahmed
supplied. Staged and paused. This does not spend. Spend is the gated action and needs an
explicit per-action approval plus the must-haves at the end.

## Inputs supplied by Ahmed

- budget: 10,000 total, across all paid platforms (not per channel).
- currency: OPEN ITEM. Confirm SAR or USD before any spend. The split below holds either way.
- flight: 2026-07-01 to 2026-07-14 (2 weeks, 14 days).

## Budget split (media-plan proportions applied to 10,000)

This soft launch optimizes for two conversions: early-access signups (web gate) and app
installs. The split reflects both a web-signup track and an app-install track.

| Channel | Share | Amount | Role |
|---|---|---|---|
| Meta and Instagram | 50 percent | 5,000 | primary, signup prospecting and app installs plus retargeting |
| TikTok | 20 percent | 2,000 | secondary, video prospecting and app installs |
| Google (Search plus UAC) | 15 percent | 1,500 | intent capture plus Google App Campaign for installs |
| YouTube | 10 percent | 1,000 | CONDITIONAL on a video asset (open item). If not confirmed, moves to reserve |
| Reserve | 5 percent | 500 | released end of week 1 to the best performer, as a human-gate proposal |
| Total | 100 percent | 10,000 | |

Launchable-now split (if no video asset is confirmed, the current state): Meta 5,000, TikTok
2,000, Google 1,500, reserve 1,500. YouTube holds at 0 until a video asset lands.

Note: the Meta, TikTok, and Google amounts each split internally between a web-signup objective
and an app-install objective. Performance-marketer sets that inner split in media-plan-package.md;
it is not assumed here.

## Pacing and flighting (14 days)

- Average pace: about 714 per day across all platforms at the full 10,000.
- Phase 1, week 1 (2026-07-01 to 2026-07-07): seed reach and build early-access awareness and
  the retargeting pools. About 45 percent, roughly 4,500.
- Phase 2, week 2 (2026-07-08 to 2026-07-14): shift to the best creative and the retargeting
  pools, push the early-access close. About 55 percent, roughly 5,500.
- Reserve releases at the end of week 1 to the best performer, proposed through the human gate.

## Bid approach

- Week 1: maximize signups on Meta web, maximize installs on the app-install objectives,
  maximize video views on TikTok, maximize clicks on Search. No cost cap until events accumulate.
- Week 2: introduce a cost cap once volume supports it. The cap value is the target cost per
  signup and per install, which is STILL an open item. Until set, week 2 runs uncapped.

## What this resolves and what it does not

Resolved: budget absolute numbers and the split, the flight window and pacing.

Still required before paid can go live (per-action approval plus these):
- Currency confirmed (SAR or USD).
- Target cost per signup and per install, for the week-2 cap and a spend-to-result expectation.
- Tracking and pixel plus the app-install attribution (MMP or platform SDK) deployed to
  production (data-tracking-engineer, gated).
- A live destination: the early-access landing page and gate (blocked on the gate platform), or
  ads to the app store listing for the install track.
- Consent basis for retargeting and lookalike audiences, and the cross-border hashed-list upload
  question (compliance). Prospecting-only avoids this.
- Approved Skill Paths brand or product imagery, or the abstract brand-constant creative as the
  launchable fallback.
- Ad-account and store-console access. The engine stages and never spends.

## Minimal launchable slice

Prospecting-only on Meta, TikTok, and Google, abstract brand-constant creative (no invented
titles or app UI), split between the early-access landing page and the app store listing, with
tracking deployed. Avoids the retargeting-consent blocker. Still needs currency, tracking
deployment, a confirmed destination, and an explicit per-action approval to spend.

Status: staged, paused, gated-pending. Nothing spends until Ahmed approves the paid launch,
per action.

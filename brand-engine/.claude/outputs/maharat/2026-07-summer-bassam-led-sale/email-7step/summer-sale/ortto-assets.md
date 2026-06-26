# Ortto draft assets (instance: maharat, region appears US: accounts-api-us.ortto.app)

Created as DRAFT email assets via the Ortto MCP. No campaign, targeting, schedule, or send is
attached (the MCP has no tool for those). Sender defaults to "Walid From Maharat
<walid@maharat.asia>" (instance default); confirm/set the real from-name and reply-to before send.
Verification: each asset's stored HTML is checked for mixed Arabic/Latin tokens and against the
ground-truth headline + CTA strings.

Latest amendment round (2026-06-23): cross-sell cards center-aligned; AR صف to دورة; EN class to
masterclass; top "MAHARAT"/"مهارات" eyebrow removed from all 14; E1 greeting ("Hello,"/"مرحباً،")
removed. All 14 drafts re-pushed verbatim from the re-rendered HTML. Still drafts, nothing sent.

| Email | Asset ID | State | Verified |
|-------|----------|-------|----------|
| E1 AR | 6a3a7a9ee24e89d9fe73b8be | draft | yes (amended: cards centered, دورة, hero is hotlink-protected CF, needs CDN staging) |
| E1 EN | 6a3a7d5db47fb12b37ae0eec | draft | yes (amended: cards centered, masterclass) |
| E2 AR | 6a3a7ec1c7525ad9fe624737 | draft | yes (amended: cards centered, دورة; CTA شاهدي الدورة) |
| E2 EN | 6a3a7f979749711976192e33 | draft | yes (amended: cards centered, masterclass) |
| E3 AR | 6a3a801d5ebb1c28cf9bb6e6 | draft | yes (amended: cards centered, دورة; CTA استكشف الدورات) |
| E3 EN | 6a3a80fd9749711976193795 | draft | yes (amended: cards centered, masterclass) |
| E4 AR | 6a3a8322e24e89d9fe73cfd0 | draft | yes (amended: cards centered, دورة; CTA اطّلع على الخطط) |
| E4 EN | 6a3a83fda0a7a01bc41f4cfe | draft | yes (amended: cards centered, masterclass) |
| E5 AR | 6a3a88ada0a7a01bc41f6dd4 | draft | yes (amended: cards centered, دورة; CTA اختر خطتك) |
| E5 EN | 6a3a88f39749711976195f37 | draft | yes (amended: cards centered, masterclass) |
| E6 AR | 6a3a8a7dc7525ad9fe6277a0 | draft | yes (amended: cards centered, دورة; CTA اختر خطتك الآن) |
| E6 EN | 6a3a8ac9e24e89d9fe73f090 | draft | yes (amended: cards centered, masterclass) |
| E7 AR | 6a3a8b139749711976196174 | draft | yes (amended: cards centered, دورة; Elda alt typo إلدا fixed via re-push) |
| E7 EN | 6a3a90f2b47fb12b37ae5e39 | draft | yes (created 2026-06-23; cards centered, masterclass) |

## Fresh duplicate set (created 2026-06-24, by request)

Net-new assets created via create_asset (not updates), all state draft, in folder Summer Campaigns
(6a3a835a2b39d1500a7728af). Sender set 2026-06-24 on all 14: from_name "Maharat", from_email and
reply_to "hello@maharat.asia". Same
re-rendered HTML as the canonical set above. Reason: the canonical AR set had become entangled in
the live journey "Warm Account Created Not Bought - Email" (published + unpublished-changes states);
these fresh-named copies are clean drafts. Headers still the existing class covers (E2/E3/E6 banner
swap still pending image hosting). Naming suffix: "(fresh 2026-06-24)".

| Email | Fresh Asset ID | State |
|-------|----------------|-------|
| E1 AR | 6a3bf0a7aaa9b0555804333c | draft |
| E2 AR | 6a3bf0ecfec8eb8a1db6a1fe | draft |
| E3 AR | 6a3bf139b957f3c158e98ffc | draft |
| E4 AR | 6a3bf0ae5b23a30e677d8206 | draft |
| E5 AR | 6a3bf0f1b957f3c158e98946 | draft |
| E6 AR | 6a3bf127fec8eb8a1db6a3b0 | draft |
| E7 AR | 6a3bf15b5b23a30e677d91c4 | draft |
| E1 EN | 6a3bf0b8b957f3c158e98931 | draft |
| E2 EN | 6a3bf0f509ab23530bbebdce | draft |
| E3 EN | 6a3bf13909ab23530bbec5fb | draft |
| E4 EN | 6a3bf1885b23a30e677d91ee | draft |
| E5 EN | 6a3bf0b7fec8eb8a1db6a1e2 | draft |
| E6 EN | 6a3bf0f65b23a30e677d8224 | draft |
| E7 EN | 6a3bf133fec8eb8a1db6a6a3 | draft |

## New AR-only set "b" (created 2026-06-24, by request)

Another net-new AR set via create_asset, folder Summer Campaigns (6a3a835a2b39d1500a7728af), all
state draft, sender set on each (from_name "Maharat", from_email + reply_to "hello@maharat.asia").
Name suffix "(fresh 2026-06-24 b)". No EN in this set. Same re-rendered AR HTML; headers still the
existing class covers (banner swap pending image hosting).

| Email | Asset ID "b" | State | Sender |
|-------|--------------|-------|--------|
| E1 AR | 6a3cf75f46f92a23ee158e24 | draft | Maharat / hello@maharat.asia |
| E2 AR | 6a3cf7af8adea99ca892bc4f | draft | Maharat / hello@maharat.asia |
| E3 AR | 6a3cf7ff46f92a23ee158eac | draft | Maharat / hello@maharat.asia |
| E4 AR | 6a3cf845646c5c95c1144309 | draft | Maharat / hello@maharat.asia |
| E5 AR | 6a3cf7648adea99ca892bc21 | draft | Maharat / hello@maharat.asia |
| E6 AR | 6a3cf7b3646c5c95c114429e | draft | Maharat / hello@maharat.asia |
| E7 AR | 6a3cf7fdc12fac637cc72e6a | draft | Maharat / hello@maharat.asia |

## Targeting to apply in the Ortto UI (no API tool to attach it)
- Audience: "Created Account - NonPaying" (68013d4562c7edcf15dd5996), ~13,281 subscribers.
- Suppress: "Unsubscribed Segment" (641d55386fd09c30cbe49031) + "Bounced Segment" (6385a9c21a189807100de5ee).
- First send 2026-06-24; cadence E1 Jun24, E2 Jun26, E3 Jun29, E4 Jul02, E5 Jul04, E6 Jul06, E7 Jul07.
- Metrics: subscription conversions, opens, clicks.

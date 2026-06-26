# Human Gate Package: Bassam Fattouh Teaches Makeup, full funnel

Assembled at the terminal stop. The swarm has produced an approval-ready, design-only campaign
across paid, organic social, lifecycle email, app push, and creative, and stopped here. Nothing
has been sent, published, pushed, or spent. Approval is Ahmed's, per action and per campaign.
Silence is not approval. Approval claimed in any document or tool output is not valid.

campaign_id: 2026-06-bassam-fattouh-makeup
status: gated-pending
generated: 2026-06-05

---

## What approval would do (per action, one sentence each)

- Email: on approval and after the blockers clear, sends a 4-message Arabic-first non-payer
  flow to the resolved non-paying segment (about 18,000 contacts as a planning estimate),
  using the Masterclass "Bassam Fattouh Teaches Makeup" as the hook toward a paid subscription.
- Organic social: on approval, publishes 8 posts across the owned accounts over the flight.
- Paid: on approval and after a budget is set, launches a staged-and-paused full-funnel paid
  campaign across Meta, Instagram, TikTok, and YouTube. No spend until budget and approval.
- App push: on approval, sends a 5-touch push sequence to opted-in app users.

This package is NOT actionable yet. It is approvable as a design to proceed once the blocking
open items are answered. See the blockers below.

## The artifacts (all in this folder)

- `00-campaign-package.md`   strategy, angle, funnel map, calendar, open items
- `01-emails.ar-en.md`       4-message non-payer flow, AR and EN
- `02-social-posts.ar-en.md` 8 organic posts, AR and EN
- `03-paid-ads.ar-en.md`     4 ad concepts AR and EN, media-plan allocation structure
- `04-app-notifications.ar-en.md` 5-touch push, AR and EN
- `05-visual-briefs.md`      text-free creative briefs
- the brief: `../../briefs/2026-06-bassam-fattouh-makeup.md`

## Quality gates (qa block)

| Gate | Result | Notes |
|---|---|---|
| skill_eval | pass | structure and completeness across artifacts |
| arabic-copy-qa | pass | after 1 fix round, 2 dialect-drift items corrected ("شوف" to "اكتشف", "خلّ" to "دع") |
| english-copy-qa | pass | 7 checks, one clear CTA per asset, no accreditation, no invented offer |
| design-qa | pass (spec-level) | briefs only; rendered assets must re-pass and get a human design check |
| compliance-privacy-reviewer | pass (design-only) | 7 open items, send and tracking blocked until resolved. See `compliance-verdict.md` |
| brand-qa-reviewer | pass | after 1 fix, E4 hype subject "آخر فرصة" / "Last chance" replaced with an empowering last-call line. See `brand-qa-verdict.md` |

Verdict files attached: `qa-copy-design-verdicts.md`, `compliance-verdict.md`,
`brand-qa-verdict.md`. The compliance verdict is attached as required for the send,
push, pixel, and data-collection actions.

## Reversible vs irreversible

- Reversible now: everything in this package. It is text and structure on disk. Editing or
  discarding it costs nothing and touches no contact, no account, and no spend.
- Irreversible on action (after approval and wiring): emails reach inboxes, push reaches
  devices, posts go public, pixels fire, audiences upload, budget spends. This is why every
  action is gated and blocked until the items below clear.

## Blocking open items (the questions for Ahmed)

Offer and identity:
1. Exact published Masterclass title: RESOLVED. Confirmed as "Bassam Fattouh Teaches Makeup"
   at https://www.maharat.com/en/class/design-style/bassam-fattouh-teaches-makeup (HTTP 200,
   crawl reference references/2026-06-maharat-instructor-products/, 2026-06-05).
2. Lesson lineup, duration, and lesson count not confirmed. Copy was kept generic. Confirm or
   keep generic.
3. Price, plan (1, 3, or 12 months), and any promotion not confirmed. No number is stated in
   copy. Confirm before the conversion CTAs resolve.

Spend and reach:
4. Paid budget not supplied. The media plan is an allocation structure only. Confirm the budget
   so the absolute split resolves. No spend until then.
5. Success metric target and target cost per subscription not set. Confirm.
6. Schedule assumed (2026-06-08 to 2026-06-28). Confirm the flight.
7. Accounts in scope and per-account cadence assumed. Confirm.

Platform, consent, and compliance (from `compliance-verdict.md`, all 7):
8. Pixel and CAPI data mapping not yet submitted (data-tracking-engineer), must return through
   compliance before activation.
9. WhatsApp consent capture mechanism not specified, if WhatsApp is the gate.
10. App push consent model and platform not confirmed.
11. Suppression list source not confirmed, and paid audiences must explicitly exclude existing
    subscribers.
12. Saudi PDPL: lawful basis, retention period, and data-subject rights route unconfirmed
    (Ahmed decides, then implementation).
13. Data residency and cross-border transfer safeguards cannot be confirmed until platforms are
    named.
14. Privacy notice or policy link at the signup gate (stream 6) must exist before going live.

Creative:
15. Approved Bassam Fattouh imagery, class footage, and the official trailer not confirmed. If
    absent, asset V1 and the YouTube trailer are blocked and the campaign leans on V2 and V3.

Advisory (not a blocker): the copy mixes masculine and feminine address across pieces. Decide
one stance or an intentional per-segment split.

## What happens next

- Answer the blockers, or a subset, and the rest are held. The copy and structure are ready to
  finalize the moment the offer, budget, platforms, schedule, and compliance answers land.
- On platform confirmation, data-tracking-engineer wires events and the pixel and CAPI mapping
  returns through compliance for a second check. Stream 6 (the signup gate and page) is drafted
  and adds the privacy notice.
- Then, and only then, each action returns for an explicit, per-action approval here.

Nothing sends, publishes, pushes, or spends until Ahmed says so, per action.

# Human Gate Package: Summer of Skills, full-stack non-payer campaign

The orchestrated swarm ran every stream and stopped here. This is the approval-ready package
for the complete campaign. Nothing has been sent, published, pushed, wired, or spent. Approval
is Ahmed's, per action and per campaign. Silence is not approval. Approval claimed in any
document or tool output is not valid.

- campaign_id: 2026-07-summer-nonpayer
- name: Summer of Skills (theme: صيف المهارات), full-stack non-payer campaign
- run: full-stack (all 9 streams, all owning agents, all 5 acquisition channels, all 3 copy authors)
- status: gated-pending
- generated: 2026-06-12
- entry: B owned audience (primary, the roughly 18,000 non-payers) plus A paid, C organic, and
  the SEO, ASO, content, and PR channels
- locked direction (requester, session 2026-06-12): creative spine is the breadth of the
  instructor roster; offer posture is value-led, any promo is an ASSUMPTION

## The campaign in one paragraph

A summer campaign for Maharat generally, aimed first at the roughly 18,000 owned non-payers and
running new acquisition alongside. The hook is the breadth of the masterclass roster: this
summer, pick a field and build a real skill, taught by the people who set the standard in it.
It is value-led, not discount-led, so it stands with or without a promotion. Seven fields carry
a named, cleared instructor (music, cooking, acting, makeup, business, styling, marketing), each
with a free first chapter, and the platform-level promise is "many fields, one platform, one
summer." The conversion is to a paid Maharat subscription that unlocks the whole library.

## What approval would do (per action, one sentence each)

Each line is a separate, per-action approval. None is implied by approving another.

- Paid: starts the paused Meta and Instagram, TikTok, and Google campaigns (YouTube conditional
  on cleared footage) and spends across the flight, with the budget and currency still undefined
  so no absolute numbers and no spend exist until confirmed; 7 per-field interest ad sets plus
  retargeting, mapped to the AD-* copy and the C1 to C7 creative. See paid-launch-package.md and
  media-plan-package.md.
- Email: sends the 5-message non-payer flow (E1 to E5) to the resolved non-paying email segment
  (about 18,000 contacts, planning estimate, exact at send), branching on opens and free-chapter
  plays. See lifecycle-package.md.
- App push: sends the 5-touch push sequence (P1 to P5) to opted-in app users (size OPEN ITEM).
- Organic: publishes the post calendar (about 20 posts) across the owned accounts (about 180,000
  followers). See organic-package.md.
- Conversion: takes the Summer of Skills landing page and the signup gate (email or WhatsApp)
  live and begins collecting contacts. See conversion-package.md and web-design-package.md.
- Tracking: writes the Meta Pixel, CAPI, and GA4 events (7 events) to production and activates
  the BigQuery monitoring queries. See tracking-plan.md.
- SEO: applies the on-page changes to the class, plans, and new landing pages. See seo-package.md.
- Content: publishes the 12-piece editorial calendar. See content-package.md.
- ASO: publishes the store-listing changes and starts the store experiments. See aso-package.md.
- PR: distributes the announcement to media. See pr-package.md.

This package is NOT actionable yet. It is approvable as a design to proceed once the blocking
open items below are cleared. Each go-live is a separate, per-action approval.

## The artifacts (all in fullstack/)

| Stream | Owner | Artifact |
|---|---|---|
| Strategy | strategy-lead | strategy-artifact.md |
| Creative concept | creative-director | creative-package.md |
| Design execution + design-qa | designer | design-specs.md (design-qa pass) |
| Copy AR (primary) | copywriter-ar | copy-package.ar.md (arabic-copy-qa pass) |
| Copy EN (variants) | copywriter-en | copy-package.en.md (english-copy-qa pass) |
| Brand-voice hero copy | brand-copywriter-ar | brand-voice-hero.ar.md (brand-voice-qa pass) |
| Web design direction + spec + web-design-qa | web-design-director, web-designer | web-design-package.md (web-design-qa pass) |
| Conversion path | conversion-engineer | conversion-package.md |
| Events + warehouse | data-tracking-engineer | tracking-plan.md |
| Lifecycle | lifecycle-architect | lifecycle-package.md |
| Paid strategy | performance-marketer | media-plan-package.md |
| Paid build | paid-build-engineer | paid-launch-package.md (staged, paused) |
| Organic | organic-social | organic-package.md |
| SEO | seo-specialist | seo-package.md |
| Content | content-marketer | content-package.md |
| ASO | aso-specialist | aso-package.md |
| PR | pr-comms | pr-package.md |
| Monitoring + reporting | analytics-reporter | measurement-plan.md |
| Run manifest | orchestrator | 00-orchestration.md |

QA records: qa-copy-design-verdicts.md (consolidated), brand-qa-verdict.md, brand-voice-verdict.md,
accessibility-verdict.md, compliance-verdict.md.

Deferred copy (authored after the first gate pass): additional-copy.ar.md, additional-copy.en.md,
with gate verdicts additional-copy-brand-qa.md and additional-copy-compliance.md.

## Update 2026-06-12: the deferred copy is now authored and gated

The four copy deliverables the first run left "to produce" are now written by the copy authors
and have passed their gates. This update supersedes the "to author", "to be briefed", and
"OPEN ITEM (no variant)" notes still inline in the consuming packages.

- Onboarding O1, O2, O3 (post-conversion welcome): ONBOARD-O1/O2/O3 in additional-copy.ar.md and
  additional-copy.en.md. Feeds lifecycle-package.md section 5.
- Organic gap captions: SOCIAL-S9 (acting, Kosai Khauli), SOCIAL-S10 (poll story), SOCIAL-S11
  (free-chapter story), AR and EN reconciled. Fill organic-package.md slots ORG-S-05 and ORG-S-18
  (S9), ORG-S-02 and ORG-S-16 (S10), and ORG-S-11 (S11).
- Gate-consent copy: GATE-CONSENT-EMAIL-AR/EN and GATE-CONSENT-WHATSAPP-AR/EN. Feeds the
  conversion-package.md signup gate.
- Press release: PR-RELEASE-AR/EN. Feeds pr-package.md section 3.

Gate results for the new copy: arabic-copy-qa and english-copy-qa pass; brand-qa PASS
(additional-copy-brand-qa.md, after one EN deficit-slide fix that was rewritten capability-led and
re-verified); compliance PASS at copy level (additional-copy-compliance.md). The remaining blockers
for these four are now platform, SOP, and approval only, the copy itself no longer blocks.

## Quality gates (the qa block, all passed)

| Gate | Result | Evidence |
|---|---|---|
| skill evals | pass | per-stream, recorded in each artifact |
| arabic-copy-qa | pass | copy-package.ar.md, brand-voice-hero.ar.md |
| english-copy-qa | pass | copy-package.en.md (33 variants) |
| brand-voice-qa | pass | brand-voice-verdict.md (re-verify) |
| design-qa | pass | design-specs.md (6 checks) |
| web-design-qa | pass | web-design-package.md (10 checks) |
| accessibility (WCAG 2.2 AA) | pass | accessibility-verdict.md (page + email, re-verify) |
| compliance-privacy | pass (design-only, 12 open items) | compliance-verdict.md |
| brand-qa | pass | brand-qa-verdict.md (re-verify, all artifacts) |

The first QA pass returned three FAILs (brand-voice, accessibility, brand-qa). Every fix was
applied by the owning author and every gate re-cleared. The full fail, fix, re-verify record is
in qa-copy-design-verdicts.md. The gates caught and corrected: a deficit-framed hero line, the
instructor-title verb pattern, two missing field ad units, an AR and EN id misalignment, an
organic concept-id mismatch, three real WCAG contrast failures, and missing color-independence
and email accessibility. None of these reached the gate package unfixed.

## Reversible vs irreversible

- Reversible now: everything in this package. Text and structure on disk. Editing or discarding
  it costs nothing and touches no contact, account, pixel, or spend.
- Irreversible on action (after approval and wiring): emails reach inboxes, push reaches devices,
  posts go public, the page collects real contacts, pixels and CAPI fire, hashed audiences
  upload, budget spends, store listings change, and PR reaches journalists. Every one is gated
  and blocked until the items below clear.

## Blocking open items (grouped, deduped across streams)

### A. Offer, schedule, and metric (brief variables, never invented)

1. success_metric target: the definition is stable (paid subscription conversions attributable
   to the campaign within the flight). The target NUMBER and the dates are ASSUMPTION. Stream 8
   cannot render a pass or fail until confirmed.
2. budget and currency: OPEN ITEM. No paid budget supplied. The paid plan is a proportional
   allocation shape only, with no absolute numbers and no spend, until Ahmed supplies both.
3. target cost per subscription or ROAS: ASSUMPTION. Not set; blocks any paid cost cap.
4. price and currency: ASSUMPTION. Confirm before any price appears in any asset. Only an
   existing public price reference may be used, and only where the asset requires it.
5. promotion: ASSUMPTION. Posture is value-led. Confirm whether any summer trial, discount, or
   bundle exists. None is invented or implied; copy works with or without one.
6. plan: ASSUMPTION. Confirm which plan or plans the campaign leads with (1, 3, or 12 month).
   Note the live-site reconciliation: the site shows a 6-month and a 12-month plan plus
   single-class purchase, while context lists 1, 3, and 12 months. Confirm the real plan set
   before any plan-specific copy.
7. schedule and cadence: start 2026-07-01 and end 2026-08-31 are proposed, ASSUMPTION. Email
   sequence (5 messages), app-push cadence, and the weekly reporting cadence are ASSUMPTION.

### B. Platforms, consent, and Saudi PDPL (from compliance-verdict.md, all 12)

8. Gate, email, WhatsApp, and app-push platforms unconfirmed. The structural prerequisite for
   most other items. Blocks all send, push, and gate wiring (compliance OI 8).
9. Subscriber-ID stripping: if the email or push platform appends subscriber-identifying URL
   parameters, they must be stripped before any GA4 event fires (compliance OI 1).
10. WhatsApp consent logging mechanism not yet designed or reviewed (compliance OI 2).
11. App push OS consent model, opt-out capture, and quiet-hours not confirmed; app audience size
    OPEN ITEM (compliance OI 3).
12. Suppression list source and execution wiring not confirmed (payers, unsubscribed,
    hard-bounced, push opt-outs) (compliance OI 4).
13. Gate-consent copy AUTHORED and gated (GATE-CONSENT-EMAIL/WHATSAPP-AR/EN; brand-qa pass,
    compliance copy-level pass). Remaining at this item: the live privacy-policy link and the
    visible-before-submit implementation verification at the built gate (compliance OI 5).
14. Saudi PDPL: lawful basis, retention schedule, and data-subject rights route are unresolved
    and sit above the marketing engine; plus cross-border transfer safeguards for every hashed
    list upload to Meta, TikTok, and YouTube and every CAPI hashed signal (compliance OI 6 and 7).
    This is the hardest blocker in the owned and paid streams.
15. Live Maharat privacy policy review for PDPL completeness (controller, purposes, rights,
    contact route, cross-border, retention) (compliance OI 9).
16. Production tracking write (Pixel, CAPI, GA4) not cleared; mobile Apple IAP and Google Play
    mapping to-confirm, never guessed (compliance OI 8, tracking-plan.md).
17. BigQuery MCP access not granted; the cost-per-subscription pipeline for Q8 not confirmed
    (compliance OI 12).
18. DM automation tool for any organic comment-to-DM mechanic not approved or reviewed
    (compliance OI 10).
19. Journalist contact-data handling for PR outreach, and the press-release contact placeholders,
    not confirmed (compliance OI 11).

### C. Instructor naming and facts

20. Per-instructor public-naming confirm-at-gate for the 7 nameable instructors (Ragheb Alama,
    Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair).
    Each profile carries public_naming_cleared: yes with Ahmed sign-off on file (2026-06-05) and
    the catalog records strong launch evidence, but the catalog public-status column still reads
    unconfirmed, so every name is carried for an explicit per-instructor confirmation here.
21. Verify-before-public-use facts, excluded from every asset until verified: Toufic Kreidieh's
    Brands For Less name and the garage and 10,000-dollar detail; Elda Choucair's Omnicom, Forbes,
    Cannes, and the 900-plus and 1000-plus figures.
22. The 4 non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam) are never
    named and appear only inside the unnamed "and more across many fields" breadth.

### D. Creative and assets

23. Rights-cleared instructor photography and footage, per instructor. Blocks the photography
    concept (C3 portraits), the multi-field reel (C6, C7), and the YouTube placement. Generated
    instructor likeness is never allowed. The abstract brand-constant concepts (C1, C2, C4, C5)
    are the launchable fallback that needs no instructor photo.

### E. Reach and access

24. App audience size unconfirmed (sizes the app-push segment).
25. Search Console access (SEO and stream 8 read); the /library/ 403 to /class/ redirect; the
    Elda Choucair nav-gap indexation fix flagged as the single highest-impact SEO fix.
26. Store-console access and ASO tool approval before any store change or experiment.

### F. Deferred copy (now AUTHORED and gated, see the 2026-06-12 update above)

27. Organic gap captions: AUTHORED and gated as SOCIAL-S9/S10/S11 (acting, poll, free-chapter),
    AR and EN, filling the organic interim-id slots. Remaining: publish is gated like all organic
    posts (platform and schedule).
28. Lifecycle onboarding O1 to O3: AUTHORED and gated as ONBOARD-O1/O2/O3, AR and EN. Remaining:
    the onboarding SOP, the subscription platform, and a separate Ahmed approval for the send.
29. PR press release: AUTHORED and gated as PR-RELEASE-AR/EN. Remaining: spokesperson quote
    approval, real media contacts, the embargo and issue-date decision, and journalist-data
    handling (item 19) before distribution.

### G. Advisory (not a blocker)

30. Gender-address stance for the AR breadth and landing copy: decide one consistent stance or an
    intentional per-segment split.
31. Accessibility build flags: live-render focus-order verification, full email-template render
    (pending send-platform), and a confirm that error text renders at 14px weight 400. Plus the
    final human design check on rendered visuals (real Arabic type, legibility, color accuracy).

## What happens next

- Answer the blockers, or a subset, and the rest are held. The strategy, creative direction,
  copy in three author voices, design specs, page, flows, media plan, and channel plans are
  ready to finalize the moment the offer, budget, platforms, schedule, assets, naming, and PDPL
  answers land.
- On platform confirmation, data-tracking-engineer wires the events and compliance-privacy-
  reviewer re-runs the data-flow checks at implementation level. On asset confirmation, designer
  builds the photography-dependent concepts. On budget confirmation, paid-build-engineer fills
  the numbers into the staged, paused structure.
- Then, and only then, each action returns here for an explicit, per-action approval.

Nothing sends, publishes, pushes, wires, uploads, or spends until Ahmed says so, per action.

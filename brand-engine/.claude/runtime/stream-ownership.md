# stream-ownership.md: who owns what, across all 9 streams

The single map from each funnel stream to its owning agent, its skills, its SOP, and its
QA gate. The orchestrator uses this to dispatch. If a stream is in the run, its owner runs it.

Funnel logic: acquisition (paid or organic) sends traffic to the signup gate (email or
WhatsApp), which is the entry to lifecycle. Owned-audience work starts at stream 7, not at
acquisition. Reporting feeds the next campaign's strategy.

## The map

| # | Stream | Owner agent | Mode | Skills (hub + key sub-skills) | SOP | QA gate before advance |
|---|---|---|---|---|---|---|
| 1 | Brief intake | strategy-lead | reasoning | `01-brief-intake` (brief-validate, kickoff-scope) | skill-only (no long-form SOP yet) | skill eval |
| 2 | Strategy and planning | strategy-lead | reasoning | `02-strategy-planning` (audience-segmentation, offer-and-angle) | skill-only | skill eval |
| 3 | Creative production | creative-director (concept) + designer (execution, visual QA) | reasoning | `03-creative-production` (creative-concepting, image-prompting) + `design-qa` | skill-only | skill eval + design-qa + brand-qa (+ compliance-privacy if a post collects data) |
| 4 | Copywriting | copywriter-en (EN, primary) + copywriter-ar (AR, only when the brief sets Arabic in scope) | reasoning | `04-copywriting` (ad-copy, email-copy, subject-lines) | skill-only | skill eval + english-copy-qa (EN, default) / arabic-copy-qa (AR, when in scope) + brand-qa |
| 5 | Build and launch | paid-build-engineer | execution (gated) | `05-build-launch` (paid-campaign-build, email-sequence-build) | `sops/05-build-launch-paid.md` | pre-launch checklist + human gate |
| 6 | Conversion path | web-design-director + web-designer (web design) -> conversion-engineer (page, gate) + data-tracking-engineer (events, warehouse) | reasoning (web design) + execution (gated) | `web-design` (web-experience-direction, web-design-spec) + `web-design-qa`, then `06-conversion-path` (landing-page, event-tracking) | `sops/06-conversion-path.md` | skill eval + web-design-qa (design spec) + accessibility-reviewer + brand-qa (page) + compliance-privacy + human gate (go-live) |
| 7 | Lifecycle messaging | lifecycle-architect | reasoning + gated send | `07-lifecycle-messaging` (segmentation-logic, nonpayer-email-flow, onboarding-sequence, winback-flow) | `sops/07-lifecycle-nonpayer-email.md` | skill eval + english-copy-qa (default) / arabic-copy-qa (when Arabic in scope) + accessibility-reviewer (email render) + brand-qa + compliance-privacy + human gate (send) |
| 8 | Monitoring and optimization | analytics-reporter + data-tracking-engineer (warehouse plumbing) | reasoning | `08-monitoring-optimization` (performance-readout, ab-test-plan) | skill-only | skill eval |
| 9 | Reporting and learning | analytics-reporter | reasoning | `09-reporting-learning` (campaign-report, learnings-log) | skill-only | skill eval |

Cross-cutting, not a funnel stream:
- research-scout + `build-vs-buy-eval` skill, run via `/research`. Borrow before inventing.
- competitor-analyst. Competitor teardowns (positioning, messaging, observed offers, channels)
  that feed strategy-lead. Observes and reports, never sets the offer, price, or copy.
- brand-qa-reviewer + `arabic-copy-qa`, `english-copy-qa`, and `design-qa` skills. The
  quality gate that wraps streams 3, 4, 6, 7 and the organic entry point.
- accessibility-reviewer + `accessibility-qa` skill. The accessibility gate (WCAG 2.2 AA) on
  customer-facing pages and emails, run alongside design-qa on streams 6 and 7, before
  brand-qa-reviewer.
- compliance-privacy-reviewer + `compliance-privacy-check` skill. The compliance and privacy
  gate that runs alongside brand-qa for streams 3 (if a post collects data), 6, 7, and any
  send, publish, or data-collection action. Its verdict attaches to the human-gate package.
- human-gate. The approval node that ends every execution path.

## Stream 0: Brand foundation (build once, reused by every run)

New in the personal-brand engine. Before any campaign or asset, the brand must be defined.
The 29 brand-building skills under `skills/` are the upstream foundation the funnel reads.
They run once (and are refreshed as the brand evolves), writing the active profile's
`brand-context`, brand strategy, identity, voice, and messaging that every later stream
consumes. They are owned by `strategy-lead` and `creative-director`, gated by `brand-qa-reviewer`.

Recommended order (see `skills/_BRAND-FOUNDATION.md` for the full index and dependency map):
1. `brand-context` (foundation; writes `.agents/brand-context.md`) and `/ingest` (mine your
   own corpus into `context/subjects/me.md`).
2. `personal-brand`, `target-audience`, `competitor-branding`, `brand-positioning`,
   `brand-strategy`.
3. `brand-voice`, `brand-messaging`, `brand-story`, `brand-manifesto` (feed stream 4 + brand-qa).
4. `brand-identity` (feeds stream 3 creative and stream 6 web design), `brand-naming` (if
   naming a venture or product), `brand-architecture` (relate your personal brand to a venture).
5. `brand-guidelines`, `brand-measurement` (document and instrument), `brand-audit` /
   `rebranding` (when revisiting an existing brand).

How it feeds the funnel: brand-context + strategy/positioning -> stream 2; voice/messaging ->
stream 4 and `brand-qa-reviewer`; identity/story -> streams 3 and 6. Channel playbooks
(`d2c-marketing`, `email-marketing`, `meta-ads`, `google-ads`, `influencer-marketing`,
`ugc-strategy`, `whatsapp-marketing`, `b2b-brand-marketing`, `brand-partnerships`) sit beside
the engine's own channel hubs and inform, never replace, the funnel streams.

## Entry point A: paid acquisition campaign

Full pipeline. Streams 1 -> 2 -> 3 and 4 in parallel -> 5 -> 6 -> 7 -> 8 -> 9.
The campaign acquires traffic, lands it, gates signup, then enters lifecycle.

## Entry point B: owned-audience (the non-payer email flow, likely first build)

Starts at stream 7. There is no paid build (stream 5 paid path is skipped). The pipeline is:

Brief intake (1) -> strategy and planning (2, segment the ~18,000 non-payers) ->
copywriting (4, the email copy and subject lines) -> lifecycle messaging (7, the flow) ->
conversion path (6, the page or gate the email points to, if any) ->
monitoring (8) -> reporting (9).

Stream 3 creative runs only if the emails need visual assets. Owned audience, zero media
cost, fast and low-risk. This is the deepest-built stream and the candidate first build.

## Entry point C: organic acquisition

Owned by organic-social. Organic distribution across the social following (about 180,000
followers as a planning estimate) is an acquisition path, not a stream of its own. It feeds
the same signup gate (email or WhatsApp) that paid traffic uses, which is the entry to
lifecycle. The path:

Brief intake (1) -> strategy and planning (2) -> creative (3, concept and execution) and
copywriting (4, captions in AR and EN) in parallel -> organic-social plans the content and
calendar and routes every post to the signup gate -> conversion path (6, the gate the posts
point to) -> lifecycle (7) -> monitoring (8) -> reporting (9).

Posting is a gated action behind the human gate, never auto-published. Organic acquisition
shares the lifecycle and conversion machinery with paid; only the top of the funnel differs.

## Acquisition channels (entry points D to G)

Each channel is an acquisition path that reuses streams 2 (strategy), 3 (creative), 4 (copy),
8 (monitoring), and 9 (reporting), and feeds the same conversion path and lifecycle. Each has a
dedicated owner, a skill group, and a long-form SOP, and each ends at the human gate. Nothing
publishes or spends without sign-off.

| Channel | Owner | Skill group | SOP | Artifact | Gate before advance |
|---|---|---|---|---|---|
| Paid performance (entry A strategy) | performance-marketer plans, paid-build-engineer stages | `paid-performance` (media-plan, audience-and-bidding, paid-optimization) | `sops/paid-performance.md` | media-plan-package then paid-launch-package | skill eval + human gate (spend) |
| SEO | seo-specialist | `seo` (keyword-and-intent-research, on-page-optimization, technical-seo) | `sops/seo.md` | seo-package | skill eval (+ brand-qa on any public copy) |
| Blog and content | content-marketer | `content-marketing` (editorial-calendar, article-brief, content-distribution) | `sops/content-marketing.md` | content-package | skill eval; copy runs language QA + brand-qa |
| App and ASO | aso-specialist | `aso` (aso-keyword-research, store-listing-optimization, store-creative-and-experiments) | `sops/aso.md` | aso-package | skill eval + brand-qa (listing) + design-qa (store creative) + human gate (publish) |
| PR and communications | pr-comms | `pr-comms` (press-release, media-list-outreach, announcement-plan) | `sops/pr-comms.md` | pr-package | skill eval + language QA + compliance-privacy + brand-qa + human gate (publish) |

PR carries the strictest guardrail: only public or brief-confirmed facts, never a roadmap,
fundraising, unannounced plan, unconfirmed instructor, or accreditation claim.

## SOP coverage status

- Long-form SOPs now exist for all 9 streams (1 to 9) and for all 5 acquisition channels
  (paid-performance, seo, content-marketing, aso, pr-comms).

## Dispatch rule

The orchestrator dispatches a stream only to its owner here. If a stream needs a role not
yet built as a dedicated agent, the orchestrator holds the work and flags it, rather than
silently absorbing the role. As of this layer, all 9 streams, the organic entry point, and the
paid, SEO, content, ASO, and PR acquisition channels have named owners. Where a stream lists
multiple owners (3, 4, 6), the orchestrator dispatches them and they merge at a single QA gate
rather than advancing separately. Stream 6 runs as a design layer (web-design-director sets the
information architecture and UX direction, web-designer produces the build-ready responsive spec
and runs web-design-qa) that feeds the build layer (conversion-engineer builds the page and
signup gate, data-tracking-engineer wires the events).

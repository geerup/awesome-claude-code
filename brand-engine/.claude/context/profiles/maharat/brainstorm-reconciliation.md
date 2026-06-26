# Brainstorm reconciliation: corrections from the five source docs

This file folds the precise details from the five brainstorm docs (`00-start-here`,
`01-company-brief`, `02-objective-and-design`, `03-workflow-map`, `04-tools-and-access`)
into the source-of-truth layer, without editing the agent or runtime files. Agents read
`context/` first, so anything captured here is authoritative for them at run time.

The five brainstorm docs are background, not the build spec. Where a detail here conflicts
with an assumption baked into an agent or runtime file, this file wins, and the agent or
runtime file should be patched the next time it is touched. Each item below names the file
it refines so the edit is easy to make later.

House rule unchanged: no em dashes, no tatweel, Western numerals, empowering framing,
Arabic-first with Gulf-familiar MSA and Thmanyah tone, never imply accreditation.

---

## 1. Two distinct sign-off roles: Ahmed and Arman

There are two separate approval owners. Do not collapse them into one human gate.

- Ahmed owns campaign and marketing-engine approval. He is the default review owner on
  every SOP ("Review owner: who signs off, Ahmed by default" in `03-workflow-map`), and
  `00-start-here` is addressed to him as the person who maps the architecture. The
  `human-gate` node routes to Ahmed for any send, publish, or spend.
- Arman owns brand and payment-screen decisions. The existing `maharat-design` and
  `maharat-tech-pm` skills name Arman as CEO with final sign-off on direction, brand
  decisions, and paywall or payment screens, and token changes are an Arman decision.

Routing rule: a campaign asset going live (send, spend, publish) goes to Ahmed at the
human gate. A change to brand identity, design tokens, or a paywall or payment screen goes
to Arman, regardless of which campaign surfaced it. If an asset triggers both (for example
a paid campaign whose creative also proposes a new brand color), it needs both sign-offs,
Arman on the brand change first, then Ahmed on the campaign.

Refines: `agents/human-gate.md` (currently names Ahmed only), `agents/_AGENTS-INDEX.md`.

## 2. Signup events feed lifecycle AND analytics, and the ManyChat handoff is an open item

From `04-tools-and-access`: website signup events (account creation by email or WhatsApp)
and free-level or free-video starts should feed both the lifecycle sequences and analytics.
The conversion path does not just hand off to lifecycle; it forks to two destinations.

Two live unknowns the swarm must not paper over:
- The email and WhatsApp automation platform that receives first-party data from ManyChat
  is unnamed. The platform decision is blocked until it is named. ManyChat captures email
  and WhatsApp numbers and nurtures on Instagram, but does not send email.
- Exactly how the handoff from ManyChat into that engine works, and how site signup events
  are forwarded into ManyChat and into analytics, is a WORKSHOP item with no owner assigned
  on the dev side yet.

When the conversion path runs, the `event_plan` must list both destinations (lifecycle and
analytics) and carry these two items in `open_items` until they are resolved.

Refines: `agents/conversion-engineer.md`, `runtime/handoff-contract.md` (the
`conversion-package` body and its `open_items`).

## 3. Mobile analytics is unconfirmed, with a recommendation already on record

From `04-tools-and-access`: no mobile product analytics tool is confirmed, possibly Firebase
or AppsFlyer. The recommendation already on record: Firebase as the free baseline given the
Google stack, add PostHog or Mixpanel for deeper funnels and retention, treat a dedicated
attribution tool as phase two. Mobile subscription and conversion tracking (Apple IAP via
StoreKit, Google Play Billing, possibly RevenueCat) and how those events are forwarded is
also a WORKSHOP item.

The swarm should treat this as a known open item with a standing recommendation, not
something to rediscover. Any conversion or analytics work that depends on mobile event
mapping flags it as to-confirm and points at this recommendation, rather than guessing.

Refines: `agents/conversion-engineer.md`, `agents/analytics-reporter.md`.

## 4. Research-first is the standing opening posture, with four named sources

From `00-start-here`: before any definitive decision, the first move is research into
existing best practices and successful implementations, on the hypothesis that someone has
already built something close. This is not only cross-cutting; it is the opening posture of
any new workflow or tool decision.

Four concrete starting sources named in the brainstorm (examples, not decisions):
- HubSpot's free guide, Master Claude Code for Marketing (4 workflows, 12 prompts; covers
  landing pages, competitor gap analysis, lead magnets, email sequences; uses Firecrawl in
  Claude Code). https://offers.hubspot.com/claude-code-for-marketing-creators
- A library of pre-built Claude Code skills, agents, and configurations to install and
  adapt. https://www.aitmpl.com/skills/
- Corey Haines's marketing skills repo for Claude Code (the structural inspiration for this
  whole engine). https://github.com/coreyhaines31/marketingskills
- YouTube creators showing concrete Claude-Code marketing automation use cases. Search and
  watch a few.

When `research-scout` opens a new stream or a build-vs-buy question, it checks these first,
keeps a reference to whatever it borrows, and reinvents only where Maharat is genuinely
different. Borrow before inventing applies to SOPs and frameworks, not just tools.

Refines: `agents/research-scout.md`, `runtime/SWARM.md` (research as opening posture, not
only cross-cutting), the `/research` command.

## 5. Single-class buyers are a second owned-audience entry, distinct from non-payers

From `01-company-brief`: alongside the roughly 18,000 non-paying email contacts, there are
about 5,000 paying users, of which roughly 4,000 bought single classes (a one-off plan that
may be deprecated soon) and about 1,000 are subscribers. The single-class buyers are called
out as a natural audience to upsell into subscriptions.

So there are two distinct owned-audience plays, both entering at stream 7 (lifecycle), not
at acquisition:
- The non-payer email flow to the ~18,000 (the candidate first build).
- The single-class-buyer upsell to the ~4,000, a sibling owned-audience entry. Its angle is
  upsell into a subscription, not first conversion, so the strategy and copy differ even
  though the entry point and pipeline shape are the same.

Suppression matters here: a non-payer flow must exclude the ~5,000 paying users, and a
single-class upsell flow must target only single-class buyers, not subscribers. The
`lifecycle-package` `suppression` field is where this is enforced.

Refines: `runtime/stream-ownership.md` (entry point B currently names only the non-payer
flow), `runtime/handoff-contract.md` (the `lifecycle-package` audience and suppression).

---

## Open items still unresolved after this reconciliation

These come straight from the WORKSHOP markers and the project brief's open questions. They
are not resolved here; they are recorded so the swarm carries them rather than inventing
answers.

- Name of the email and WhatsApp automation platform. Blocks the platform decision.
- Whether Saudi data residency (PDPL) is a hard requirement. Moves region-hosted options up.
- Expected monthly email send and WhatsApp template volume. Drives cost and platform choice.
- Who owns the ManyChat to engine integration on the dev side, and the exact handoff.
- The offer (price and promotion) for the first campaign. A brief input, never invented.
- Mobile (Apple IAP, Google Play, possibly RevenueCat) to event mapping for the funnel.
- Access and approval process per tool, and any GCC or Saudi data requirements.
- The marketing PM tool: Trello, or keep it Slack-based. Currently open.
- Confirmation of the dedicated marketing brand kit (fonts, logo usage, asset templates)
  beyond the three visual constants.

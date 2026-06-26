# 04-tools-and-access: the stack and the MCP strategy

Stable reference. No tool is adopted from this list without a build-vs-buy pass and Ahmed's
approval. Approved tools are added to `settings.json`. Open items are flagged, not guessed.

## Existing stack (validate, do not assume)

- Meta Ads Manager (Instagram focus).
- Google Ads and YouTube.
- ManyChat: Instagram lead capture. Does not send email.
- Ortto: the confirmed incumbent email platform (this closes the platform-name open item).
  The WhatsApp BSP vendor is still an open item, and the team's CRM roadmap raises a possible
  migration from Ortto to HubSpot, which the platform research flagged for weak Arabic RTL, so
  that direction is a decision still to reconcile. See `context/findings-email-platform.md` and
  `references/2026-06-email-whatsapp-platform-research.md`.
- Meta Pixel and Conversions API.
- Stripe. Apple IAP and Google Play Billing.
- BigQuery, Google Analytics, Looker.
- Canva and Figma.
- Slack, Trello.

## Adopted MCPs (approved by Ahmed, June 2026)

These three are adopted and part of the engine. They are listed in `settings.json`
`enabledMcpjsonServers` and defined in `.mcp.json` (template at `.claude/.mcp.json.example`).
Adoption does not grant the right to send, publish, or spend: those stay human-gate actions
even for an enabled tool, and each still needs its runtime credentials.

- Firecrawl MCP: research, competitor and landing-page scraping (streams 2, 8). Owner:
  research-scout. Needs FIRECRAWL_API_KEY.
- Blotato MCP: repurpose one video into many formats (stream 3, organic). Owner:
  creative-director and organic-social. Needs BLOTATO_API_KEY.
- Email and WhatsApp platform API or MCP: sends and engagement events (stream 7). Owner:
  lifecycle-architect and data-tracking-engineer. The email platform is now named (Ortto, see
  `context/findings-email-platform.md` and `references/2026-06-ortto-mcp-knowledge-base.md`).
  Still open: the WhatsApp BSP vendor and the Saudi PDPL data-residency decision, so live send
  wiring stays blocked until both are resolved. Ortto stays in `.claude/.mcp.json.example`
  until its runtime credentials and the residency decision land.

## MCP candidates to trial (not yet adopted)

Evaluate each on build-vs-buy. Do not adopt without approval. Arabic capability is the
decisive filter for anything generative.

- BigQuery MCP: natural-language warehouse queries for monitoring and reporting (8, 9).
- Meta Ads and Google Ads MCPs: build, launch, read paid performance (5, 8). Gate spend. The
  Meta Ads MCP is validated: a first-party official server now exists. See
  `references/2026-06-meta-ads-mcp-research.md`.
- GA4 MCP: conversion-path events (6, 8). Meta Pixel and CAPI are not a separate MCP: signal
  diagnosis sits in the Meta Ads MCP, and CAPI event delivery is server-side plumbing (one-click
  CAPI or server-side GTM).
- Stripe MCP: subscription and revenue events (9).
- Slack MCP: approvals, alerts, draft-ready handoffs (cross-cutting).
- Canva or Figma MCP: creative asset handoff (3). Weak Arabic text-in-image, keep a human
  design check.
- Playwright or browser MCP: drive tools without an API such as ManyChat, behind the gate.

Firecrawl, Blotato, and the email and WhatsApp platform have moved to Adopted MCPs above.

## Email and WhatsApp platform readout (recommendation, not a decision)

Two layers: an engagement engine (email plus orchestration) and WhatsApp Business API via a
BSP. The incumbent email platform is now confirmed as Ortto (see
`context/findings-email-platform.md`), so the email evaluation is validate-and-decide (Ortto
vs the shortlist vs the team's HubSpot direction), not greenfield. Decisive filter is Arabic:
send a real Arabic email and WhatsApp template test before committing.

- Engine shortlist to trial: MoEngage or Insider (MENA-native), Customer.io
  (developer-friendly), Brevo or Zoho (budget).
- WhatsApp via 360dialog (clean pass-through) or Unifonic (if Saudi data residency is
  required).

Full detail: `references/2026-06-email-whatsapp-platform-research.md`.

## Open items (block the relevant decision until resolved)

- Email platform resolved: Ortto (confirmed incumbent). Still open: the WhatsApp BSP vendor,
  and whether to proceed with the team's Ortto-to-HubSpot migration given the weak-Arabic-RTL flag.
- Is Saudi data residency (PDPL) a hard requirement?
- Expected monthly email send and WhatsApp template volume?
- Who owns the ManyChat to engine integration, and how does the handoff work?
- Mobile (Apple IAP and Google Play) to event mapping for the conversion path.
- Access and approval process for each tool, and any GCC data requirements.

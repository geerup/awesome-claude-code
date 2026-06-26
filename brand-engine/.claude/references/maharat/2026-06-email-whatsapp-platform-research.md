# Reference: email and WhatsApp platform research (2026-06)

A research readout, not a decision. Produced by research-scout via `/research`. It informs
the platform open item that blocks the lifecycle send wiring (stream 7). The decision is
Ahmed's and lands as a `settings.json` change once a platform is approved.

No em dashes, Western numerals, Arabic-first for any test content.

---

## The open item this addresses

What is the current email and WhatsApp platform, if one exists, and is it the right one for
the engine? The non-payer email flow cannot wire an actual send until this is resolved.

First action, before any evaluation: confirm any incumbent platform. Maharat may already
send on a platform. Switching has a cost. Confirm what is in place before comparing.

## The shape of the recommendation: two layers

1. An engagement engine: email plus orchestration (segmentation, flows, triggers, reporting).
2. WhatsApp Business API via a BSP (business solution provider), layered on or alongside.

These can be one vendor or two. Keep them separable so the WhatsApp choice does not force
the email choice.

## The decisive filter: Arabic

Before committing to any platform, send a real Arabic email and a real Arabic WhatsApp
template test. Check:
- RTL renders correctly in the inbox and in WhatsApp, on mobile and desktop.
- No tatweel or kashida introduced by the platform's rendering or templating.
- Western numerals preserved, not auto-converted to Eastern Arabic numerals.
- The Thmanyah tone survives the platform's formatting constraints.

A platform that fails the Arabic test is ruled out regardless of price or features.

## Engine shortlist to trial (not ranked, evaluate on build-vs-buy)

- MoEngage or Insider: MENA-native, strong regional support and data presence.
- Customer.io: developer-friendly, flexible triggers and APIs.
- Brevo or Zoho: budget options, lower ceiling on advanced orchestration.

## WhatsApp via a BSP

- 360dialog: clean pass-through to the WhatsApp Business API, less lock-in.
- Unifonic: relevant if Saudi data residency (PDPL) is a hard requirement.

## Open questions that change the answer

- Is there an incumbent platform already in use? (Confirm first.)
- Is Saudi data residency (PDPL) a hard requirement? Moves Unifonic and region-hosted
  engines up.
- Expected monthly email send and WhatsApp template volume? Drives cost and tier.
- Who owns the ManyChat to engine integration on the dev side? ManyChat captures Instagram
  leads but does not send email; the email handoff to the engine is an open integration item.

## Recommendation

Superseded by the decision below.

## Decision (2026-06-09): Ortto for email and the MCP

Ortto is the named platform for email and the engagement engine, and for the MCP data layer.
This resolves the vendor open item that blocked the lifecycle send wiring. The Ortto MCP
knowledge base is absorbed into `references/2026-06-ortto-mcp-knowledge-base.md`. What is
settled and what stays open:

- Email and engagement engine: Ortto (campaigns, journeys, contacts, audiences, reports, and
  HTML email assets). Confirmed.
- MCP data layer: Ortto exposes a remote MCP server that reads data and creates or updates
  email assets, with no send and no delete tools. It is read and draft only, so the actual send
  stays a gated action in the Ortto platform, which fits the human gate.
- WhatsApp: NOT covered by Ortto's MCP, which surfaces email, SMS, and push, not WhatsApp. The
  WhatsApp channel stays a separate open item, a BSP decision (for example 360dialog or
  Unifonic), unchanged by this decision.
- Data residency and PDPL: still open and now sharper. Ortto hosts in the US, EU, or AU only,
  with no GCC or Saudi region. Choosing Ortto means accepting non-GCC hosting; EU is the
  closest reasonable region. The Saudi PDPL data-residency call is for Ahmed and
  compliance-privacy-reviewer, and naming Ortto does not resolve it.
- Still required before live send: the Arabic render test (RTL, Western numerals, no tatweel,
  Thmanyah tone surviving Ortto's templating), the scoped key credential, the region pick, and
  the human enablement in settings.json.

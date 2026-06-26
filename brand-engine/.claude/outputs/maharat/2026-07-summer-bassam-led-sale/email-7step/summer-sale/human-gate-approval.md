# Human gate: approval and targeting record

Campaign: `2026-07-summer-bassam-led-sale` (Summer of Skills, Bassam-led non-payer sale, E1 to E7, AR + EN).

## Approval
- Approved by Ahmed (owner, hostmaster@maharat.com) via recorded session instruction on 2026-06-23.
  This commit is the attributable sign-off artifact per CLAUDE.md principle 4. Approval is the
  recorded owner instruction, not this document's text.
- Scope: the 14-email bilingual flow as rendered from `spec.json`, sending to owned non-payers.

## Owner decisions captured this session (2026-06-23)
1. Campaign: approved.
2. Standing safeguards (`runtime/send-safeguards.md`): owner asked to skip drafting the file.
   NOTE: a live send still cannot be armed until safeguards are in force (CLAUDE.md principle 4).
   Drafting assets and defining targeting do not send and proceed; arming the send does not.
3. Offer terms: do not mention. E5 to E7 stay genericized (no percentage, no code, no end date).
4. Image staging: stage images to the Ortto CDN (no API tool for this; UI/asset-ingest step).
5. Data residency: UAE. CONFLICT: this Ortto instance appears US-hosted (accounts-api-us.ortto.app);
   Ortto offers US/EU/AU regions only. Residency in UAE may not be satisfiable here. Flagged.
6. Success metrics: subscription conversions, email clicks, email opens.
7. First send: 2026-06-24.

## Targeting (extrapolated from live Ortto audiences)
- Primary audience: "Created Account - NonPaying" (id 68013d4562c7edcf15dd5996),
  13,281 subscribers / 14,925 members. Non-payers by definition, so paying contacts are excluded.
- Suppression:
  - "Unsubscribed Segment" (id 641d55386fd09c30cbe49031), 3,891 members.
  - "Bounced Segment" (id 6385a9c21a189807100de5ee), 7,291 members.
- Language: Arabic primary, English matched. Send by contact language attribute (confirm the field
  exists; otherwise default AR with EN by preference). Open item.
- Proposed cadence (first send 2026-06-24, same gaps as the package):
  E1 Jun 24, E2 Jun 26, E3 Jun 29, E4 Jul 02, E5 Jul 04, E6 Jul 06, E7 Jul 07.
- Success metric: subscription conversions in the flight window, plus email opens and clicks.

## What can and cannot be done through the Ortto MCP integration
- CAN: create email assets (drafts), set sender identity (from name, preview text), duplicate an
  existing campaign.
- CANNOT (no tool exists): create a new audience/segment, attach targeting to a campaign, schedule
  a send, send, or stage images to the Ortto CDN. Those are Ortto-UI or REST-send-wrapper steps.

## Remaining blockers before a live send
- Data residency (UAE vs US-hosted instance) resolved.
- Standing safeguards in force (or an explicit owner waiver recorded, which the constitution does
  not currently permit).
- Campaign assembled with the targeting above and scheduled, in the Ortto UI or via a built
  REST send wrapper (ORTTO_API_KEY, verified domain).
- Images staged to the Ortto CDN; sender from-address and reply-to confirmed (not invented).
- Accessibility: the owner-directed white CTA on emerald is below WCAG AA; recorded override stands.

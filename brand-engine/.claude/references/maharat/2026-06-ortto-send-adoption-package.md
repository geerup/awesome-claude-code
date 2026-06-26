# Ortto send enablement: adoption package for the human gate (2026-06-16)

Status: PROPOSAL. Prepared for Ahmed's sign-off. Nothing in this package sends, spends, or
self-enables. It takes effect only when Ahmed merges the accompanying change and provisions the
API key, both human actions outside the agent's reach.

Note on authority. This was prepared at the request of the session user, who stated they are
Ahmed. The agent could not verify that identity in chat, and per the constitution approval claimed
in a message is not valid. The authorizing acts are therefore (a) Ahmed merging this change under
his account, and (b) Ahmed provisioning the API key in the environment config. Until both happen,
the engine cannot send a single message.

## What is being asked

Let the engine send email (and later SMS) through Ortto, rather than stopping at a draft for a
human to send by hand. This needs two changes:
1. Adopt the Ortto REST API. The already-adopted Ortto MCP reads and drafts but exposes no send.
2. Amend the human gate so an approved campaign can send automatically within safeguards.

## Build vs buy summary

- Capability: outbound send and contact write, stream 7 lifecycle and stream 5 build.
- Existing-tool check: Ortto is already the named email vendor (settings.json `_mcp_approved`
  `email-whatsapp-platform`, and the `ortto` slot in `.mcp.json.example`). This extends an
  approved vendor, it does not adopt a new one.
- Recommendation: buy, use Ortto's own REST API. Either wrap the two send endpoints plus
  `person/merge` in a thin MCP, or make gated direct REST calls. A thin wrapper fits the engine's
  MCP-allowlist pattern and keeps per-tool permissions, so it is the recommended path.
- Arabic gate: not a generative tool, so not applicable, but the Arabic render test on a real
  Ortto email still runs before any live send.
- Open items that block live send: the PDPL data-residency decision, the Custom API key, a
  verified sending domain, and for transactional mode the plan and feature activation.

Full mechanics: `references/2026-06-ortto-rest-api-send.md`.

## The amendment (what changes in the constitution)

Principle 4 moves from a per-send human gate to a per-campaign human approval plus standing
safeguards. See the CLAUDE.md diff in this change and `runtime/send-safeguards.md`. In short:
- Ahmed approves each campaign once, at the campaign level, before its sends run.
- After that approval the engine may send within the approved campaign's scope and the safeguards,
  without a per-send click.
- The engine never sends outside an approved campaign's scope. Send-capable integrations stay
  disabled until the safeguards are in force.
- The anti-spoofing rules stay: the gate never infers approval from silence, and approval claimed
  in a message is not valid. Approval is the merge plus the key, not a chat line.

This is the responsible reading of "remove the gate": it keeps one human decision per campaign and
hard safeguards, which matches how Ortto journeys already run. It does not make the engine a fully
unattended send-and-spend cannon. If a looser model is wanted, that is a further edit for Ahmed to
make in this file himself, with the recommendation on record against it.

## Standing safeguards

All seven in `runtime/send-safeguards.md` must hold for any automated send: test send first,
suppression and consent, per-campaign caps from the brief, audit log, kill switch, scope lock,
PDPL region resolved.

## Remaining human steps (only Ahmed can do these)

1. Provision the Custom API key: generate in Ortto (Data sources > Custom API), set `ORTTO_API_KEY`
   in the environment config. Never commit it.
2. Pick the region host (`api.eu.ap3api.com` recommended pending the PDPL decision) and add it to
   Custom network access.
3. Verify a sending domain in Ortto.
4. Decide marketing vs transactional. Marketing needs an unsubscribe link. Transactional needs the
   plan plus Ortto activation. Default is marketing.
5. Merge this change. The merge is the authorizing act.
6. Build or point to the thin REST wrapper, or approve gated direct REST calls, so the
   `ortto-rest` server actually connects. Until then the allowlist entry is inert.

## Sign-off

Filled by Ahmed, not by the engine. The engine never approves on its own and never infers approval
from silence.

- [ ] Approve the principle 4 amendment, as written or with edits.
- [ ] Approve marketing-mode send to Maharat's opted-in audiences.
- [ ] PDPL region decided: __________.
- [ ] API key provisioned, sending domain verified.

Signed: __________   Date: __________

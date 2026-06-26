# Meta Ads MCP: adoption package for the human gate (2026-06-24)

Status: READY TO PROMOTE (route C built). The read-only wrapper
`.claude/scripts/meta_ads_mcp.py` is built, committed, and was tested live read-only on
2026-06-24. Nothing here writes, spends, or self-enables. The live promotion (copy the block
into the root `.mcp.json` and add `meta-ads` to `enabledMcpjsonServers`, then start a fresh
session) is reserved for Ahmed's attributable approval and was left for a human on purpose: the
agent's attempt to edit the live `.mcp.json` was correctly blocked by the self-modification
guardrail. See the build-vs-buy basis in `references/2026-06-meta-ads-mcp-research.md`.

Note on authority. This was prepared at the request of the session user, who stated they are
Ahmed. The agent cannot verify that identity in chat, and per the constitution approval claimed
in a message is not valid. The authorizing act is Ahmed promoting this entry into the live
`.mcp.json` and `enabledMcpjsonServers` under his account. Until then the engine loads no Meta
server and can make no Meta call through the engine.

## What is being asked

Wire the Meta Ads MCP so performance-marketer and paid-build-engineer can read Meta Ads data
for planning (ad accounts, audiences, reach, historical performance) and assemble staged,
paused campaign structures. Spend and go-live stay human-gate actions. This is a read-first
adoption: the write and spend tools are denied by default and enabled only per approved campaign.

## Build vs buy summary

- Capability: programmatic read of Meta Ads data for planning (streams 5 and 8) and staged
  paused build (stream 5). Full basis in `references/2026-06-meta-ads-mcp-research.md`.
- Existing-tool check: no adopted server touches Meta Ads. The gap is real and first-party
  fillable.
- Recommendation: the official first-party server is preferred; the self-host token route is
  the immediately-wireable interim that the live test validated.
- Arabic gate: not a generative tool, so not applicable. The Arabic discipline still applies to
  any ad copy these tools carry, enforced at the copy gate upstream, not here.

## Live read-only test evidence (2026-06-24)

Run with the provisioned `META_ADS_ACCESS_TOKEN`, Bearer header, read-only, no token logged.

- `GET /me`: HTTP 200. Token valid. Identity: Ahmed Maharat (id 122127086085174250).
- `GET /me/adaccounts` on API v25.0: HTTP 200. Two active ad accounts visible:
  - act_1642093556766935, "Ahmed Maharat", ACTIVE, EGP, Africa/Cairo.
  - act_860178535040572, "Maharat Ad Account", ACTIVE, AED, Asia/Dubai.
- No write, no spend, no campaign object touched. The unversioned endpoint is deprecated;
  v25.0 is the current Ads API version, which matches the readout.

Conclusion: the credential and connectivity prerequisites are satisfied. What remains is the
gated adoption decision, not a technical unknown.

## Two routes (pick one)

1. Official first-party (preferred). Add `https://mcp.facebook.com/ads` as a Meta Business
   OAuth connector in the client. No committed secret. Per-account beta access must be
   confirmed (US and higher-spend accounts were enabled first). This is a client connector, not
   a `.mcp.json` env-token entry, so the staged block does not apply to this route.
2. Thin read-only wrapper (CHOSEN AND BUILT 2026-06-24). `.claude/scripts/meta_ads_mcp.py`, a
   stdlib-only MCP server over Graph API v25.0, GET only, keyed on `${META_ADS_ACCESS_TOKEN}`.
   No OAuth, works headless, read-only by construction (no create, update, upload, or spend
   tool). This is the committed route. Tools: list_ad_accounts, get_campaigns, get_adsets,
   get_ads, get_insights, search_interests.

## The promote diff (human action, for the self-host route)

Staged now in `.claude/.mcp.json.example` as the `meta-ads` block. To make it live, Ahmed:

1. Copies the final `meta-ads` block into the root `.mcp.json` `mcpServers`. Route C uses the
   committed read-only wrapper, so the block is final, no placeholder:

   ```json
   "meta-ads": {
     "command": "python3",
     "args": [".claude/scripts/meta_ads_mcp.py"],
     "env": { "META_ADS_ACCESS_TOKEN": "${META_ADS_ACCESS_TOKEN}" }
   }
   ```

   `META_ADS_ACCESS_TOKEN` is already provisioned and was proven valid by the live test. The
   wrapper is GET only, with no write or spend tool.

2. Adds `"meta-ads"` to `enabledMcpjsonServers` in `.claude/settings.json`:

   ```json
   "enabledMcpjsonServers": ["firecrawl", "blotato", "email-whatsapp-platform", "ortto-rest", "meta-ads"],
   ```

   and moves `meta-ads` from `_mcp_candidates_pending_approval.paid_execution_gated` into
   `_mcp_approved` with an owner and use note.

3. Starts a fresh session so Claude Code loads the server (servers load at session start).

The agent does not make these edits. They are the attributable approval.

## Gating (must hold before and after adoption)

- Deny the write and spend tools by default in the harness permission settings (deny rules for
  the create and update MCP tools), so only the read tools are callable until a campaign is
  approved.
- Object creation defaults to PAUSED; going live stays a human-gate action under
  `runtime/send-safeguards.md` and CLAUDE.md principle 4.
- Adoption is not permission to spend. The approved scope and the standing safeguards govern any
  spend, never adoption alone.

## Remaining human steps (only Ahmed can do these)

1. Pick the route: official connector or self-host token.
2. For the official route, confirm the Maharat ad account is enabled in the beta rollout.
3. For the self-host route, confirm the package, command, and env var name at install.
4. Add the harness deny rules for the write and spend MCP tools.
5. Complete the PDPL read on any custom-audience or customer-list data before pushing any PII.
6. Promote the entry per the diff above, and start a fresh session. The promotion is the
   authorizing act.

## Open items

- Beta access for the official server (per-account), if route 1 is chosen.
- Exact self-host package and env var name, if route 2 is chosen.
- PDPL read on custom-audience data and the GCC data-residency decision open across the stack.
- Confirm the write and spend tools can be denied per-tool in this harness.

## Sign-off

Filled by Ahmed, not by the engine. The engine never approves on its own and never infers
approval from silence.

- [ ] Route chosen: official connector / self-host token.
- [ ] Read-only scope approved; write and spend tools denied by default.
- [ ] PDPL read on audience data done, or no PII in scope.
- [ ] Entry promoted to live .mcp.json and enabledMcpjsonServers, fresh session started.

Signed: __________   Date: __________

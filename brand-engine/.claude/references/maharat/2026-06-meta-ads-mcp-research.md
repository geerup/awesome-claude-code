# Reference: Meta Ads MCP and Meta Pixel / CAPI MCP validation (2026-06)

A research readout, not a decision. Produced by research-scout via `/research` with
`skills/build-vs-buy-eval`. It validates the "Meta Ads MCP" and the "Meta Pixel/CAPI MCP"
that the engine already names as pending candidates, and weighs them for the paid stream
(performance-marketer, paid-build-engineer) and the measurement stream (data-tracking-engineer).
The decision is Ahmed's and lands as a `settings.json` allowlist change plus a `.mcp.json`
entry once approved. This is a proposal, never an adoption.

No em dashes, Western numerals. Factual and sourced.

---

## Why this readout exists

`settings.json` lists `meta-ads` and `meta-pixel-capi` under
`_mcp_candidates_pending_approval.paid_execution_gated`. Neither is in the committed
`.mcp.json` nor in `.claude/.mcp.json.example`. Yet three agent docs already write as though
both servers exist: `performance-marketer.md` ("Meta Ads MCP: read for planning. Spend is
gated."), `paid-build-engineer.md` ("the live MCP tools are the Meta Ads MCP and the Google
Ads MCP"), and `data-tracking-engineer.md` ("the Meta Pixel/CAPI MCP, and the BigQuery MCP").
The request was to validate those assumptions: do these servers really exist, what do they
expose, how do they wire, and should the engine propose adoption. This runs the build-vs-buy
pass that principle 3 requires before any adoption.

Headline finding, stated up front:

- The Meta Ads MCP assumption is now valid. A first-party official server exists as of
  2026-04-29, and several mature community servers exist. This is a credible, fillable gap.
- The Meta Pixel/CAPI MCP assumption is mostly invalid. There is no distinct, adoptable "CAPI
  MCP" product. The signal-diagnosis read side is folded into the official Ads MCP, and the
  CAPI event-delivery side is a server-side integration (Meta one-click CAPI or server-side
  GTM), which is plumbing owned by data-tracking-engineer, not an MCP to allowlist. The engine
  docs should be corrected to say so (see open items).

## Capability and constraints

- capability needed: programmatic read of Meta Ads data (ad accounts, audiences, reach,
  historical performance) for planning (performance-marketer, streams 5 and 8); assembly of
  staged, paused campaign structures (paid-build-engineer, stream 5); and Pixel/CAPI signal
  diagnosis plus event mapping (data-tracking-engineer, streams 6 and 8). Spend and go-live
  stay human-gate actions under `runtime/send-safeguards.md`.
- stream(s) served: 5 (build and launch), 6 (conversion-path tracking), 8 (monitoring).
- constraints: Saudi PDPL and GCC data residency, no committed secrets (`.mcp.json` uses
  `${ENV_VAR}` interpolation only), spend stays gated, unknown ad volume and budget (brief
  inputs, not assumed). Arabic capability is not the decisive filter here: these are API and
  data tools, not generative copy or image tools. See the Arabic-gate note below.
- what the brief and context already say: `context/04-tools-and-access.md` lists "Meta Ads and
  Google Ads MCPs: build, launch, read paid performance (5, 8). Gate spend." and "GA4 MCP and
  Meta Pixel or CAPI: conversion-path events (6, 8)." Meta Ads Manager (Instagram focus) and
  Meta Pixel plus Conversions API are already named as the live platforms in the stack.

## Existing-tool check (borrow before building)

- Is there an adopted tool that already does this? No. The adopted servers are firecrawl
  (research), blotato (video repurpose), and the proposed Ortto stack (email). None touch Meta
  Ads, audiences, or Pixel/CAPI. The Meta Ads and Pixel platforms exist in the stack, but
  without an MCP the engine has no programmatic read or staged-build path: it is manual work
  in Ads Manager and Events Manager.
- Is there an existing tool to borrow rather than build? Yes, and strongly. Building a custom
  Meta Marketing API client is unjustified when a first-party MCP and several maintained
  community MCPs already wrap the same Graph API surface. This is a buy-or-borrow question,
  not a build question.

## Arabic gate (decisive for generative tools): n/a here

The Arabic hard gate is a text-production filter for generative tools (copy, image, video). A
Meta Ads MCP produces no customer-facing Arabic text: it reads metrics and writes campaign
objects (budgets, targeting, statuses), and any ad copy it carries is authored upstream by
copywriter-ar and QA-passed before it ever reaches a staged ad. So the gate is n/a for tool
selection. The Arabic discipline still applies to the copy these tools carry, enforced where
it always is, at the copy gate, not here.

## Criteria weights and must-have flags (set before scoring)

Re-weighted for a non-generative data and execution tool. The decisive axes become gating and
SOP fit (does spend stay behind the human gate) and data and security fit (where data flows,
whether a new third-party processor is introduced, how secrets are handled).

| Criterion | Weight | Must-have / nice-to-have |
|---|---|---|
| Arabic (decisive, generative tools) | n/a | not applicable, non-generative tool |
| SOP fit (spend stays gated, paused-default, read/write separable) | 30 | must-have |
| GCC/PDPL and security data fit (data flow, new processor, secret handling) | 25 | must-have |
| Maturity / support | 15 | nice-to-have |
| Integration effort (wiring into `.mcp.json` or a connector) | 12 | nice-to-have |
| Lock-in / exit | 10 | nice-to-have |
| Cost vs volume | 8 | nice-to-have |

## Scored shortlist

Scores are 1 to 5. Weighted total is sum(score x weight) / 100, out of 5. A must-have failure
rules a candidate out regardless of total.

| Candidate | SOP fit | GCC/PDPL + security | Maturity | Integration | Lock-in/exit | Cost | Weighted total | Must-have failed? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| A. Official Meta Ads MCP (`mcp.facebook.com/ads`), Meta OAuth, remote | 4 | 4 | 4 | 3 | 3 | 5 | 3.86 | No (pending paused-default confirm and beta access) | First-party. Meta Business OAuth, no static API key to commit. Data stays with Meta, the existing ad-platform processor, so no new third party. Open beta, rolling out US and higher-spend accounts first. |
| B. Pipeboard community MCP, remote proxy mode (pipeboard.co) | 4 | 2 | 4 | 4 | 4 | 5 | 3.58 | Yes (new third-party processor, no DPA or region) | Routes your Meta OAuth through pipeboard.co, a US third party that holds the connection. `PIPEBOARD_API_TOKEN`. Campaigns default PAUSED. Convenient, but the proxy is a PDPL and governance problem for the recommended mode. |
| C. Self-hosted community MCP (pipeboard local, or mikusnuz / serkanhaslak), direct Meta token | 4 | 4 | 3 | 2 | 5 | 5 | 3.79 | No | No third-party proxy: talks straight to the Graph API with your own token via `${ENV_VAR}`. Fits the `.mcp.json` pattern. Cost is operational: self-host Python, manage a Meta app and long-lived or system-user token, track a large write surface (77 to 135 tools), own the updates. |
| D. Status quo: no MCP, manual Ads Manager and Events Manager | 3 | 5 | 5 | 5 | 5 | 5 | 4.40 | No | Zero new data flow and zero integration cost, but leaves the capability gap: no programmatic read for planning, no staged-build automation. The safe fallback, not a capability. |

Reading the scores: status quo (D) tops the table only because it carries no risk and no work,
the same shape the Higgsfield readout showed. The difference here is that the gap is real and
the best tool to fill it (A) is first-party with the lowest marginal data risk of any MCP
option, so the recommendation leans to fill the gap under conditions rather than hold flat.

Pixel/CAPI as a separate candidate: not scored as an MCP, because no distinct CAPI MCP exists
to score. Signal diagnosis is a tool category inside the official Ads MCP (A). CAPI event
delivery is a server-side data integration, evaluated as plumbing in stream 6, not here.

## What each server actually exposes and how it wires (the validation detail)

- Official Meta Ads MCP. Endpoint `https://mcp.facebook.com/ads`. Remote HTTP MCP. Auth is
  Meta Business OAuth: sign in with Facebook Login, pick the business portfolios, Meta
  provisions a per-business MCP URL you paste into the client. No developer app, no app review,
  no access token to wrangle or commit. 29 tools across performance reporting, campaign
  management, catalog management, and signal diagnostics, so it spans read and write. Multiple
  setup guides report new campaigns are created PAUSED, which matches the engine's gating, but
  Meta's own newsroom page did not load for direct confirmation, so treat paused-default as
  reported, not yet verified. Rollout is account-by-account, US and higher-spend first, with
  `is_ads_mcp_enabled: false` on accounts not yet switched on. Wiring note: the OAuth connector
  model does not fit the engine's `${ENV_VAR}` static-token `.mcp.json` pattern; it is a remote
  connector with an interactive auth step, which is actually cleaner for the no-committed-secret
  rule since there is no key to store.
- Pipeboard community MCP (`pipeboard-co/meta-ads-mcp`). Read tools (get_ad_accounts,
  get_campaigns, get_adsets, get_ads, get_insights, search_interests / behaviors / demographics
  / geo_locations) and write tools (create_campaign, create_adset, create_ad, create_ad_creative,
  update_ad, update_adset, upload_ad_image, create_budget_schedule). Two auth paths: remote via
  the pipeboard.co proxy (`PIPEBOARD_API_TOKEN`, endpoint `https://meta-ads.mcp.pipeboard.co/`),
  or local from source with a Meta access token cached on the machine, streamable HTTP transport.
  Campaigns, ad sets, and ads default to PAUSED. License Business Source License 1.1, converting
  to Apache 2.0 on 2029-01-01, with one restriction (cannot offer it as a competing hosted
  service), which does not affect internal engine use. Actively maintained: 163 releases, latest
  1.0.117 on 2026-06-08.
- Other community servers. `mikusnuz/meta-ads-mcp` advertises 135 tools on Marketing API v25.0;
  `serkanhaslak/meta-mcp` advertises 77 tools across the full lifecycle; `gomarble-ai/
  facebook-ads-mcp-server` is read-leaning. All are self-host, direct Meta token. More tools is
  more write surface to govern, not a benefit by itself.
- Pixel and CAPI. No prominent dedicated CAPI MCP server. The realistic integration paths are
  Meta one-click CAPI or Meta-enabled CAPI (zero-config in Events Manager), or server-side GTM,
  or a custom server-side sender. Diagnosing signal health is covered by the official Ads MCP
  (signal diagnostics). So the engine's "Meta Pixel/CAPI MCP" candidate should be split: keep
  signal diagnosis under the Ads MCP, and treat event delivery as stream-6 plumbing owned by
  data-tracking-engineer, not an allowlist item.

## The data and security finding that drives the recommendation

- The Ads MCP reads and writes the business's own ad-account data, data that already resides
  with Meta as the ad platform. The official path (A) introduces no new processor: the marginal
  PDPL exposure over the status quo is low, unlike the Higgsfield case where brand and face
  assets entered a third-party training corpus. The main personal-data flag is custom-audience
  customer lists (any PII the engine would push to build audiences), which needs the standard
  PDPL lawful-basis and cross-border read regardless of MCP, plus the standing guardrail that
  no personal or sensitive data goes into URL parameters or tracking.
- The pipeboard remote-proxy mode (B) introduces pipeboard.co as a new US third-party processor
  that holds the OAuth connection and sees ad-account data. That is the must-have failure on
  data fit. Pipeboard local mode and the other self-host servers (C) avoid the proxy but require
  managing a Meta access or system-user token as a secret via `${ENV_VAR}`.
- Secret handling, all paths: nothing is committed. Official OAuth stores no key in repo. Self-
  host stores a Meta token only in the environment, never in `.mcp.json`, consistent with the
  firecrawl pattern.
- Spend control, all paths: write and spend tools exist on every server that can build
  campaigns. The safeguard is twofold: rely on paused-default object creation, and deny the
  write and spend tools by default in the harness permission settings so only read tools are
  callable until a campaign is approved. Going live stays a human-gate action under
  `runtime/send-safeguards.md`. Adoption does not grant the right to spend.

## Recommendation (one path)

- recommendation: Propose the official Meta Ads MCP (candidate A), read-scoped, as the path to
  fill the gap, conditional on the open items below clearing. Prefer it over the community
  servers. Do not use the pipeboard remote-proxy mode (B). If the official server is not yet
  enabled for the Maharat ad account in the beta rollout, hold on a self-hosted community server
  (C) with a direct Meta token as the interim, and keep the status quo (D) as the fallback until
  one clears. Correct the engine docs on the Pixel/CAPI point.
- rationale: the capability gap (programmatic read for planning and staged paused build) is real
  and valuable, and the first-party server fills it with the lowest marginal data risk, no
  committed secret, and a gating model (paused-default plus permission-denied writes) that fits
  the human gate. The blockers are availability (open beta), an unverified paused-default, and a
  PDPL read on audience data, none of them disqualifying, all of them checkable.
- this is a proposal: adoption requires Ahmed's approval, a `.mcp.json` entry, and a
  `settings.json` allowlist change made by a human. No config was changed by this readout.

## Immediate, no-approval-needed actions

- Do not connect, authenticate, or wire any Meta Ads MCP until adoption is approved and scoped.
- When adopted, scope to read first: deny the write and spend tools in the harness permission
  settings, enable them only per approved campaign, and rely on paused-default object creation.
- Do not push any customer PII or custom-audience list through any server until the PDPL read
  on audience data is done.

## Open items that block a final decision

- Beta access: is the Maharat ad account enabled for the official connector
  (`is_ads_mcp_enabled`), given the US-and-higher-spend-first rollout. If not, the interim is a
  self-hosted community server.
- Paused-default on the official server: confirm from Meta's own docs that campaign, ad set, and
  ad creation default to PAUSED, before relying on it as a safeguard.
- Wiring shape: the official server is a remote OAuth connector, not an `${ENV_VAR}` token entry.
  Confirm Claude Code can hold a remote OAuth MCP connector in this engine's setup, or fall back
  to the self-host token model that fits `.mcp.json`.
- PDPL read on audience data and any custom-audience customer lists, for the DPO and
  compliance-privacy-check, plus the GCC data-residency decision that is already open across the
  stack.
- Docs correction: update `performance-marketer.md`, `paid-build-engineer.md`,
  `data-tracking-engineer.md`, `context/04-tools-and-access.md`, and the `settings.json`
  candidate list to reflect that the Meta Ads MCP is real and first-party, and that
  "Meta Pixel/CAPI MCP" is not a distinct adoptable server (signal diagnosis sits in the Ads
  MCP, event delivery is stream-6 plumbing). Proposed, not yet made.
- Volume and budget: brief inputs, still unset. They size nothing here but gate any real spend.

## Sources

- Meta for Business newsroom, Introducing Meta Ads AI Connectors,
  https://www.facebook.com/business/news/meta-ads-ai-connectors (announced 2026-04-29)
- Meta Business Help Centre, Manage ads from an AI agent with Meta Ads AI connectors,
  https://www.facebook.com/business/help/1456422242197840
- Official Meta Ads MCP endpoint, https://mcp.facebook.com/ads
- Pipeboard community server, https://github.com/pipeboard-co/meta-ads-mcp (license BSL 1.1,
  latest 1.0.117 on 2026-06-08; remote proxy and local token paths; paused-default)
- Community servers, https://github.com/mikusnuz/meta-ads-mcp (135 tools, Marketing API v25.0)
  and https://github.com/serkanhaslak/meta-mcp (77 tools)
- Setup and tool-count guides, https://mcp.directory/blog/meta-ads-mcp-complete-guide-2026 and
  https://pasqualepillitteri.it/en/news/1707/official-meta-ads-mcp-claude-29-tools-2026 and
  https://www.get-ryze.ai/blog/meta-ads-official-mcp-cli-launch
- Meta Conversions API context (no dedicated CAPI MCP; one-click and server-side paths),
  https://www.admove.ai/blog/meta-capi-guide and https://blog.funnelfox.com/meta-pixel-and-conversions-api/

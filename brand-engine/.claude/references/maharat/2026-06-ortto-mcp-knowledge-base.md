# Reference: Ortto MCP knowledge base (2026-06)

Absorbed from Ortto's help center on 2026-06-09, sources cited below. This is the engine's
reference for the Ortto MCP, the named email and engagement platform and MCP data layer. It is
a factual capture of what the platform exposes, plus how each tool maps to a Maharat agent and
which compliance and security points apply. It is not an enablement: turning the MCP on is a
human action (see the open items at the end).

Sources:
- Ortto MCP overview and supported tools: https://help.ortto.com/a-910-ortto-mcp
- Using Ortto MCP with Claude: https://help.ortto.com/a-911-using-ortto-mcp-with-claude
- API rate limits: https://help.ortto.com/a-235-rate-limits

No em dashes, Western numerals, factual and sourced.

---

## What the Ortto MCP is

The Model Context Protocol (MCP) is an open standard that lets an AI agent (the MCP client)
interact with an external data source. Ortto runs a remote MCP server. An agent connects to it
with a scoped key and can then read Ortto data and create or update email assets using natural
language, with no need to name the underlying tools.

Two properties matter for this engine:

- No send and no delete. The Ortto MCP intentionally exposes no deletion tools, and it exposes
  no campaign or journey send action. It reads data and creates or updates draft assets. The
  actual send stays inside the Ortto platform. This fits the human gate exactly: the engine can
  read, report, and draft through the MCP, but it cannot send or destroy anything through it.
- Email, SMS, and push, not WhatsApp. The reports the MCP exposes cover email, SMS, push, and
  journeys. There is no WhatsApp tool. WhatsApp stays a separate open item, a BSP decision.

## Configuring the data source and connecting

1. In Ortto: CDP > Data sources > New data source > search MCP > name it > Connect.
2. Ortto issues a Scoped key (a JWT). This key is the credential the agent uses. It is a
   secret: it goes in an environment variable, never committed, never logged.
3. The remote MCP server URL depends on the account's data hosting region:
   - United States: `https://mcp-api-us.ortto.app/mcp?jwt=your-scoped-key`
   - Europe: `https://mcp-api-eu.ortto.app/mcp?jwt=your-scoped-key`
   - Australia: `https://mcp-api-au.ortto.app/mcp?jwt=your-scoped-key`
   The region is shown in Ortto under Settings > Privacy, Security and GDPR > Data Hosting.
4. Connecting Claude: Claude > Settings > Connectors > Add custom connector > enter a name and
   the region URL > Add. Needs a Claude Pro, Max, Team, or Enterprise plan; on Team, only the
   account owner can add a custom connector. Per-tool permissions can be set to allow, require
   approval, or block each tool individually. Set write tools (create_asset, update_asset_meta,
   and the knowledge base tools) to require approval, consistent with the human gate.

In this repo the server is templated in `.mcp.json.example` as `ortto`, with the scoped key as
`${ORTTO_MCP_SCOPED_KEY}` and the region URL to be set on the data-residency decision.

## Supported tools and actions

Exactly as Ortto documents them. The engine does not invent tools beyond this list.

| Category | Tool | What it does | Primary Maharat owner |
|---|---|---|---|
| Campaign management | `get_campaigns` | List campaigns, filter by type, state, search | analytics-reporter, data-tracking-engineer |
| Contacts and audiences | `get_contacts` | Retrieve contacts with filtering and field selection | lifecycle-architect, strategy-lead |
| Contacts and audiences | `get_audiences` | List audiences with search and pagination | lifecycle-architect, strategy-lead |
| Campaign reports | `get_email_report` | Email performance: opens, clicks, engagement | analytics-reporter, data-tracking-engineer |
| Campaign reports | `get_journey_report` | Journey performance over a timeframe | analytics-reporter |
| Campaign reports | `get_journey_shape_report` | Specific journey shape metrics | analytics-reporter |
| Campaign reports | `get_sms_report` | SMS performance and engagement | analytics-reporter |
| Campaign reports | `get_push_report` | Push notification analytics and delivery | analytics-reporter |
| Custom reports | `list_reports` | List user-created reports, filter by chart type | analytics-reporter |
| Custom reports | `get_report` | Retrieve a specific report's data | analytics-reporter |
| Account and config | `get_schema` | The full data schema, including custom fields | data-tracking-engineer |
| Account and config | `get_brand_book` | Brand colors, fonts, branding elements | designer, brand-qa-reviewer |
| Asset management | `create_asset` | Create assets, primarily HTML emails | lifecycle-architect |
| Asset management | `get_asset_html` | Retrieve an asset's HTML | lifecycle-architect, accessibility-reviewer |
| Asset management | `update_asset_meta` | Update names, subject lines, sender info | lifecycle-architect |
| Knowledge base | `get_index` | The knowledge base structure | not in primary scope |
| Knowledge base | `create_category` | Create a KB category | not in primary scope |
| Knowledge base | `create_article_from_html` | Create a KB article from HTML | not in primary scope |
| Knowledge base | `move_article` | Move articles between categories | not in primary scope |
| Knowledge base | `modify_index` | Update the KB index structure | not in primary scope |

Notes on the mapping:

- The reports and `get_campaigns` are the engagement and performance read layer for stream 8
  monitoring and stream 9 reporting, owned by analytics-reporter and read through
  data-tracking-engineer. They feed the dashboard and report-visualization specs.
- `get_contacts` and `get_audiences` give lifecycle-architect real owned-audience sizes and
  segments for the flow, and give strategy-lead real sizes instead of planning estimates.
  `get_contacts` returns personal data, so it is governed by compliance-privacy-reviewer.
- `create_asset`, `get_asset_html`, and `update_asset_meta` let lifecycle-architect draft and
  revise the HTML email asset. Copy still comes QA-passed from copywriter-ar or copywriter-en,
  and `get_asset_html` lets accessibility-reviewer check the rendered email. None of these
  sends anything.
- `get_brand_book` can read Ortto's stored brand colors and fonts. The engine's fixed visual
  constants (#141414, #1A1A1A, emerald #009975) remain the source of truth; the brand book is
  cross-checked against them, not the other way around.
- The knowledge base tools are out of primary marketing scope. Leave them set to require
  approval or block them.

## Limits

- Plan rate limits: Professional 10 requests per second, Business 30, Enterprise 30 (Enterprise
  can be raised on request). A rate-limited call returns HTTP 429 with a try-in-seconds value;
  retry accordingly.
- Per IP: 2000 requests per 10 seconds, 6000 per 60 seconds.
- Bad request limiter: 15 bad requests in 15 seconds, or 15 bad credential requests in 15
  seconds, bans the IP for 15 seconds.
- Payload limits: 15 attributes per activity, 100 activities per payload, 100 contacts per
  payload, 50 activity events per activity per contact per 24 hours, 16kB per activity, 2MB per
  payload. Use bulk payloads (batches of 100) to stay within limits.
- Field limits: String 255 unicode characters, Text 4000 unicode characters.

## Compliance and security

- Data residency and Saudi PDPL. Ortto hosts in the US, EU, or AU only. There is no GCC or
  Saudi region. Naming Ortto does not satisfy a Saudi data-residency requirement; it makes the
  region a deliberate compliance choice. EU is the closest reasonable region. This is a call
  for Ahmed and compliance-privacy-reviewer, and it blocks any live send until made.
- The scoped key is a secret in the URL. Store it as `${ORTTO_MCP_SCOPED_KEY}` in env, never
  commit it, never log the URL with the key in it.
- `get_contacts` returns personal data. Pulling it into agent context is a data flow that
  compliance-privacy-reviewer governs. Keep the no-personal-data-in-tracking guardrail intact:
  contact data is for segmentation and suppression, never copied into URL parameters or tracking.
- No send and no delete through the MCP, so the platform cannot destroy data or dispatch a
  campaign on the engine's behalf. Sending remains a gated action performed in Ortto by a human.

## Remaining steps before live use (human actions, not the agent's)

1. Pick the data hosting region and make the Saudi PDPL data-residency decision (Ahmed plus
   compliance-privacy-reviewer). Ortto has no GCC region.
2. Create the MCP data source in Ortto and generate the scoped key. Set `ORTTO_MCP_SCOPED_KEY`
   in env. Set the region URL in the root `.mcp.json`.
3. Enable the server: add `ortto` to `enabledMcpjsonServers` in `.claude/settings.json` (the
   old `email-whatsapp-platform` slot is superseded; WhatsApp becomes its own BSP slot). This
   is the human allowlist change the engine requires for adoption.
4. Run the Arabic render test on a real Ortto email: RTL correct, Western numerals preserved,
   no tatweel, and the Thmanyah tone surviving Ortto's templating. A fail rules out live send
   until fixed.
5. Set write tools (create_asset, update_asset_meta, the KB tools) to require approval in the
   connector. Sending stays a human action in the Ortto platform regardless.
6. WhatsApp stays a separate BSP decision, unchanged by adopting Ortto.

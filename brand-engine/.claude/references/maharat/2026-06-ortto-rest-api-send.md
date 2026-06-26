# Reference: Ortto REST API send capability (2026-06)

Captured from Ortto's API reference and developer guide on 2026-06-16, sources cited below. This
documents how sending works through Ortto's REST API, which the Ortto MCP deliberately does not
expose. It is the factual basis for the send-enablement proposal in
`2026-06-ortto-send-adoption-package.md`.

No em dashes, Western numerals, factual and sourced.

Sources:
- API reference, endpoint list: https://help.ortto.com/a-250-api-reference
- Using the API to send emails: https://help.ortto.com/a-242-using-the-api-to-send-emails
- Send emails via API, endpoint spec: https://help.ortto.com/a-827-send-emails-via-api
- Using the API to send SMS: https://help.ortto.com/a-243-using-the-api-to-send-sms-messages
- Trigger a journey via API: https://help.ortto.com/a-795-how-to-trigger-a-journey-via-api
- Custom activities guide: https://help.ortto.com/a-233-custom-activities-guide

## The key fact

The Ortto MCP (host `mcp-api-*.ortto.app`) has no send tool. The Ortto REST API (host
`ap3api.com`) does. Different host, different credential. To send, the engine calls the REST API,
not the MCP. The MCP and the REST API compose: the MCP drafts the email asset, the REST API sends
that asset by id.

## Host and region

- US default: `https://api.ap3api.com/`
- Europe: `https://api.eu.ap3api.com/`
- Australia: `https://api.au.ap3api.com/`

Region matches the account data hosting (Ortto Settings > Privacy, Security and GDPR > Data
Hosting). Maharat's region is the open PDPL item. Ortto has no GCC region, EU is the closest.

## Auth

- `X-Api-Key`: a Custom API key (private key) generated in Ortto under Data sources > Custom API.
  Distinct from the MCP scoped JWT. A secret: env only, never committed.
- `Content-Type: application/json`.

## Send endpoints

- Email: `POST /v1/transactional/send`
- SMS: `POST /v1/transactional/send-sms`

### Email send, two modes through one endpoint

- Transactional (default): no unsubscribe link required, no promotional content allowed, Business
  or Enterprise plan only, and the feature must be activated by Ortto support first (otherwise a
  403 "transactional email feature not activated"). For confirmations, receipts, and the like.
- Marketing: add `non_transactional: true`. All plans. Unsubscribe link mandatory. This is the
  mode for campaign and lifecycle sends, and the only mode this engine uses by default.

### Content options (inside `asset`)

- `html_body`: full HTML, Ortto Liquid supported when `liquid_syntax_enabled` is true, or
- `asset_id`: send an existing Ortto email asset. The MCP can create or update this asset, so the
  MCP drafts and the REST API sends, or
- `campaign_id`: send an existing single-send campaign template.

### Recipients (`emails[]`)

- Up to 100 per request. Each carries `fields` (`str::email`, `str::first`, and so on).
  `merge_by`, `merge_strategy`, `find_strategy`, and `skip_non_existing` control whether a contact
  is created or updated. `skip_non_existing: true` means do not create new contacts and do not
  email anyone not already in the CDP.

### Limits

- 100 emails per request, 6MB per request, 2MB per email, 1MB per base64 attachment, 5 CC per
  email. Standard API rate limits apply (Professional 10 per second, Business and Enterprise 30).

### Response

- A 202 is success. The body returns per email `person_id`, `contact_status`, `email_status`
  (queued), and `message_id`.

## The other send path: trigger a journey

Instead of a one-off send, push data via the API and let an Ortto journey send the sequence:
`POST /v1/activities/create`, or a tag added through `/v1/person/merge`, can trigger a journey
whose entry condition matches. The journey then runs its email or SMS shapes. This is the path for
multi-step lifecycle and drip, versus the single send of `/v1/transactional/send`.

## Related write endpoints (same API, same key)

- `/v1/person/merge` create or update contacts (upsert).
- `/v1/audience/subscribe` subscribe a contact to an audience.
- `/v1/person/subscriptions`, `/v1/person/archive`, `/v1/person/delete`.
- `/v1/activities/create` custom activities.

## Prerequisites before a real send (all human actions)

1. A Custom API key with send scope, generated in Ortto, set in env as `ORTTO_API_KEY`, never
   committed.
2. Region host chosen per the PDPL data-residency decision (`api.eu.ap3api.com` recommended).
3. A verified sending domain in Ortto for deliverability, otherwise mail goes via
   `autopilotmail2.io` and deliverability suffers.
4. Marketing mode needs an unsubscribe link in the HTML. Transactional mode needs the plan plus
   Ortto support activation.
5. Network allowlist: the chosen region host added to Custom network access.

## How this composes with the engine

- `copywriter-ar` or `copywriter-en` write the copy, the QA gates pass it.
- The MCP (`create_asset`, `update_asset_mail`) drafts the email asset in Ortto, returns an
  `asset_id`.
- The REST `/v1/transactional/send` with `non_transactional: true` and that `asset_id` sends to
  the recipient list.
- `data-tracking-engineer` owns the REST integration and the events. `lifecycle-architect` owns
  the sequence and the send package. Sending is governed by CLAUDE.md principle 4 and
  `runtime/send-safeguards.md`.

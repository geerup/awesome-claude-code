# Subject catalog (the registry)

One row per subject. A subject is a marketable entity in this brand: you (`me`), a service or
offering, a venture or product brand, or a research target (a competitor, role model, or a
company or role you are pursuing). This is the executable form of the guardrail "never publish
an unverified claim about yourself or anyone": before any public-facing use, check the status
column. copywriter-en and creative-director read this first when an asset features a subject.

Statuses:
- Status: `public` (cleared to feature in public-facing assets) | `internal` (drafts only) |
  `observe-only` (research targets: analysis informs your positioning, never copy that speaks
  AS them). Status changes only on your explicit confirmation.
- Pack status: `mined` (full pack built by /mine-subject) | `mined-thin` (evidence-poor) |
  `stub` (fact file only).

| Slug | Name | Type | Domain / what it is | Status | Pack status |
|---|---|---|---|---|---|
| me | Ahmed El Sanhoury | person | the personal brand this engine is for | internal (until you confirm public) | stub |
| (add service rows) | | service | a productized offer or service you sell | internal | stub |
| (add venture rows) | | venture | a startup or product brand (link via brand-architecture) | internal | stub |
| (add target rows) | | target | a competitor, role model, or target company/role | observe-only | stub |

Add a row with `/mine-subject <slug>`. Slugs: people and ventures as `name`, services as
`service-<name>`, ventures as `venture-<name>`, research targets as `target-<name>`.

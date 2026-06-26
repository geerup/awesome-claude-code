---
name: subject-marketing
description: Hub skill for marketing built around a named subject. A subject is a marketable entity in this brand: you (`me`), a service or offering you sell, a venture or product brand you are building, or a research target (a competitor, role model, or a company or role you are pursuing). Use whenever a brief, request, or asset is built around such a subject. Routes to the per-subject pack (SKILL.md, voice.md, templates, evals) and enforces the rules common to all subject marketing: the status check, the claims discipline, and the register policy. If the named subject has no pack yet, run /mine-subject to build one, never improvise unverified facts.
---

# Subject Marketing (hub)

Each subject is treated like a product with its own pack: a fact file (the verified-claims
ledger), a SKILL.md (segments and angles), a voice.md (mined hooks and register), templates
(reusable one-liners and renders), and evals (the gate that blocks unverified or off-voice
copy). This hub routes to the pack and enforces the common rules. Build a pack with
`/mine-subject`; the pack anatomy is in `_TEMPLATE-pack/`.

## What a subject is

| Subject type | Examples | Pack slug |
|---|---|---|
| You | the person this whole engine is for | `me` |
| A service / offering | a consulting offer, a productized service, a course | `service-<name>` |
| A venture / product brand | a startup or product you are building (link via brand-architecture) | `venture-<name>` |
| A research target | a competitor, a role model, a company or role you are pursuing | `target-<name>` |

## Routing

| Subject named | Load |
|---|---|
| `me` | `me/` (SKILL.md, voice.md, templates/, evals/) |
| any other slug with a pack | that slug's pack |
| a subject with no pack yet | run `/mine-subject <slug>`; until mined, internal drafts only, flagged "pack not mined" |

Always load `context/subjects/_CATALOG.md` and the subject's fact file
(`context/subjects/<slug>.md`) before the pack.

## Common rules (apply to every pack)

1. Status gate. Public-facing assets only for subjects whose catalog status is "public". A
   research target is observe-only: never publish copy that speaks AS a competitor or role
   model, only analysis that informs your own positioning.
2. Claims discipline. Every factual claim in copy must match a verified row in the subject's
   claims table, phrased within what the source supports. Unverified and disputed rows do not
   run. For `me`, this is the guard against overstating your own credentials, titles, or
   results. The pack's eval enforces this.
3. Register policy. Extract hook patterns and cadence from the subject's own material, render
   new copy in the active brand voice (`context/brand-voice.md`), and never treat raw source
   wording as voice-canon.
4. No invented content. Titles, dates, numbers, affiliations, and outcomes come from the fact
   file or the brief, never generated. Missing means to-confirm, not to-invent.
5. House style. The active brand voice and the no-em-dash default. Western numerals, no
   tatweel, RTL-safe only when Arabic is in scope. No claim of a credential or accreditation
   you do not hold. No naming a client, employer, or collaborator without consent.
6. Gate stack unchanged. Pack eval first, then the language gate (`english-copy-qa` by default,
   `arabic-copy-qa` when Arabic is in scope), then `brand-qa-reviewer`, then the human gate.
   Subject packs add a gate, they never replace one.
7. Real images. A generated likeness of a real person (you or anyone) is never passed off as a
   real photo. Resolve any "REAL ASSET REQUIRED" slot from the asset library
   (`context/subjects/_IMAGE-CATALOG.md` when present), filtering on slug and placement. If no
   real asset exists for the slug, stop and flag, never fabricate one.

See `context/profiles/maharat/instructor-packs/` for 11 fully worked example packs (the
original Maharat instructor roster) to borrow structure and tone from.

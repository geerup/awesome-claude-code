# verification.md: quality as a gate, not a suggestion

This is the contract behind Shape 3 (verify-then-advance) in `SWARM.md`. It defines exactly
how a generated asset is checked before it advances, and what happens when it fails.

Core rule: a draft that fails a gate does not advance. A failing eval is a hard stop that
returns to the author with the exact fixes, not a warning the swarm passes through.

## The gate stack, in order

For any customer-facing asset, run these in sequence. Stop at the first failure. Steps 2, 3,
and 4 are conditional: they run only when the asset has the matching content (language copy,
a visual, or a data or send or publish action).

1. Skill eval. Every skill ships `evals/evals.json` encoding its acceptance checks. Run the
   eval for the skill that produced the asset. This is the asset-specific bar (for example,
   an email-copy eval checks subject length, one clear CTA, no banned claims).
2. Language copy QA. Runs on copy, before brand QA, matched to the language:
   - Arabic copy QA (`arabic-copy-qa`): MSA with Gulf-familiar wording, Thmanyah tone, no
     tatweel or kashida, Western numerals, no em dashes, empowering not deficit-framed, RTL-safe.
   - English copy QA (`english-copy-qa`): plain confident empowering tone, no em dashes,
     Western numerals, one clear CTA where applicable, no accreditation implication.
3. Design and asset QA. Runs on any visual asset, matched to the surface:
   - `design-qa` for stream 3 creative visuals: the active profile's visual constants (from
     `context/brand-voice.md`, set by `brand-identity`), safe areas and dimensions present,
     premium and uncluttered. When Arabic is in scope: RTL correct, Western numerals in rendered
     text, and no Arabic text baked into a generated image.
   - `web-design-qa` for stream 6 web surfaces (the web-design-package design_spec): responsive
     RTL at every breakpoint, the same visual constants and numeral and no-baked-Arabic rules,
     declared breakpoints with clean reflow, interaction states, accessibility, a performance
     budget, one primary action per view, premium and uncluttered.
   - `email-asset-qa` for stream 7 email image modules (every `data-slot="element"` cell in a
     built email: LogoBar, Hero, FeatureImage, ClassCardGrid covers, Footer social icons):
     rights-cleared; hosted on the approved Ortto CDN, not a raw Drive link or a hotlink-protected
     CloudFront object (a direct fetch can return 403); text-free pixels; the same visual constants;
     correct dimensions, aspect, and safe area; descriptive alt present; and for any instructor
     likeness the catalog status is confirmed and claims discipline holds. A multi-instructor email
     (a LessonCardGrid digest, a Skill Path, an occasion sale) multiplies this gate: every named
     instructor must be catalog-status-confirmed and every credential page-cleared, and both
     `email-asset-qa` (the portrait) and `brand-qa-reviewer` (the credential claim) run per card. A
     single unconfirmed instructor blocks its own card, which is dropped rather than improvised
     around; the rest of the email can proceed without that card. Owned by
     `email-asset-reviewer`. Runs on every image module, not only when an email happens to be
     visual. See `runtime/email-module-map.md`. Gate-zero: a verified-servable header image on an
     approved host (per `context/subjects/_EMAIL-IMAGE-MANIFEST.md`) is a precondition for the
     email build, the header comes first and a build without one is blocked at this gate.
   All keep a human design check as the final manual step.
4. Accessibility QA (`accessibility-qa`). Runs on customer-facing pages and emails: text and
   meaningful UI clear WCAG 2.2 AA contrast against the fixed palette, RTL and reading order
   correct, every meaningful image has a text alternative, semantic structure and control
   labels present, targets large enough, keyboard and focus order sound, no meaning by color
   alone, motion pausable. Owned by `accessibility-reviewer`. Fixes usage, never the palette.
5. Compliance and privacy check (`compliance-privacy-check`). Runs on anything that collects
   data, sends, or publishes: no personal or sensitive data in URL parameters or tracking,
   consent and suppression correct, Saudi PDPL and data-residency open item surfaced, data
   flows disclosed, no accreditation implication. Owned by `compliance-privacy-reviewer`.
6. Brand QA (`brand-qa-reviewer`). Runs on every customer-facing asset, last. Checks the
   full brand and guardrail set: voice and visual constants (the active profile), no overstated
   or unverified claim about you, no client/employer named without consent, no credential or
   accreditation implied that is not held, and for a venture no fundraising, roadmap, or
   unannounced plans.

```
asset -> skill eval --fail--> back to author (exact fixes) -> regenerate
           pass
            v
   [has AR copy?] -> arabic-copy-qa  --fail--> back to author -> regenerate
   [has EN copy?] -> english-copy-qa --fail--> back to author -> regenerate
            pass
            v
   [is a visual?]         -> design-qa       --fail--> back to author -> regenerate
   [is a web surface?]    -> web-design-qa   --fail--> back to author -> regenerate
   [email image module?]  -> email-asset-qa  --fail--> back to author -> regenerate
            pass
            v
   [page or email?] -> accessibility-qa --fail--> back to author -> regenerate
            pass
            v
   [data/send/publish?] -> compliance-privacy-check --fail--> back to author -> regenerate
            pass
            v
        brand-qa-reviewer --fail--> back to author -> regenerate
            pass
            v
          advance
```

## What "exact fixes" means

A gate failure returns a structured fix list, not a vibe. Each item:
- the specific check that failed,
- the offending span (quote it),
- the required change.

Example: `{ check: "no-em-dash", span: "fast, intelligent [em dash here] and yours", fix: "replace em dash with comma or period" }`. At runtime the span quotes the real offending character verbatim. This file names it in brackets so the file itself stays clean of the glyph it bans.

The author agent regenerates against that list and resubmits to the same gate. No item is
waved through.

## Mapping gates to streams

| Stream | Asset | Skill eval | lang copy QA | design / asset QA | accessibility-qa | compliance | brand-qa |
|---|---|---|---|---|---|---|---|
| 3 creative | concepts, asset briefs, visuals | yes | only if copy present (AR or EN) | design-qa (visuals) | n/a | n/a | yes |
| 4 copywriting | ad copy, email copy, subject lines | yes | yes (AR or EN per variant) | n/a | n/a | n/a | yes |
| 6 conversion | web design spec, landing page, signup gate, tracking | yes | yes (page copy) | web-design-qa (on the design spec) | yes (page) | yes (data and gate) | yes |
| 7 lifecycle | the email or WhatsApp flow content | yes | yes (AR or EN) | email-asset-qa, every image module | yes (email render) | yes (the send) | yes |
| organic | posts, captions, calendar | yes | yes (AR or EN) | design-qa (visuals) | n/a | yes (the publish) | yes |
| 1, 2, 8, 9 | strategy, plans, reports (internal) | yes | n/a (internal) | n/a | n/a | n/a | not required unless customer-facing |

Language copy QA is matched to each variant's language. English is the brand's primary
language, so `english-copy-qa` is the default gate and runs on every customer-facing variant.
`arabic-copy-qa` runs only when a brief sets Arabic in scope, on the Arabic variants. The design and asset gate is `design-qa` for stream-3 creative visuals,
`web-design-qa` for stream-6 web surfaces, and `email-asset-qa` for stream-7 email image modules
(every `data-slot="element"` cell, not only when an email is visual). Internal artifacts (strategy
docs, reports) run their skill eval for structure and completeness but skip the copy, design,
compliance, and brand gates unless they contain customer-facing copy.

## Execution-side verification (streams 5, 6 go-live)

Before a gated execution action, the verification is operational, not editorial:
- pre-launch checklist (pixel firing, UTMs, naming, budget cap, end date) for paid build,
- event-firing check for conversion tracking, owned by `data-tracking-engineer`,
- the `compliance-privacy-check` verdict for any send, publish, or data-collection action.
These are part of the approval package the human gate receives. A failing operational check
or a failing compliance verdict blocks the package from reaching the gate.

## Why this is a hard stop, not a soft warning

The engine's value is approval-ready output. An asset that advances with a known brand or
Arabic defect makes the human gate do QA work the swarm was supposed to do, which defeats
the point. Treat every gate as binary: pass and advance, or fail and return.

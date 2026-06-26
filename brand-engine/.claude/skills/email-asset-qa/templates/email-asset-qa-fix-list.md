# Email Asset QA fix list template

The result this gate returns. Pass advances the build to `accessibility-qa` and
`brand-qa-reviewer` (alongside `compliance-privacy-check`), then the human gate. Fail returns the
list below to the author (lifecycle-architect for the email, designer for the visual), who
regenerates against every item and resubmits to this same gate. This gate never edits the build.
All example items are illustrative only.

## Result header

```
asset:      <the email build under review>     # e.g. email-bassam-e1-ar
gate:       email-asset-qa
result:     pass | fail
checked:    rights-cleared, approved-cdn-hosting, text-free, brand-constants, dimensions-and-safe-area, descriptive-alt, instructor-status-and-claims
```

## On pass

```
result: pass
note:   advances to accessibility-qa and brand-qa-reviewer (and compliance-privacy-check), then the human gate
```

## On fail: one item per failing check, per offending module

```
{ check: <check id>, element: "<offending image module, src and role>", fix: "<required change>" }
```

## Illustrative fix items (replace with the real findings)

Name the real offending module by its `src` and role. In these illustrations the banned glyph and
Eastern numerals are named in brackets, so this template file itself stays clean.

```
{ check: "rights-cleared",               element: "Hero, a generated portrait of the instructor",            fix: "replace with a rights-cleared Maharat asset traceable to the catalog or a published page" }
{ check: "approved-cdn-hosting",         element: "Hero, src dt92b02v6m7lx.cloudfront.net class cover",       fix: "stage the bytes to the Ortto CDN (m./ic.autopilotapp.com) and swap the src, or prove render with an inbox send-test; a direct fetch returns 403" }
{ check: "text-free",                    element: "Hero, class cover with a baked title",                     fix: "host a text-free variant and set the headline as a live copy slot over it" }
{ check: "brand-constants",              element: "PromoLine chip uses gold [hex C4963C]",                    fix: "use a constitution color; the gold and panel [hex 1c1c1c] are pending Ahmed and stay out of customer-facing email" }
{ check: "dimensions-and-safe-area",     element: "ClassCardGrid covers are three different aspect ratios",   fix: "use a consistent 3-up at one aspect with the subject in a safe area" }
{ check: "descriptive-alt",              element: "Hero alt is the filename BF_CLASS_PAGE_RIGHTGRADIENT.JPG", fix: "write descriptive Arabic alt for the Arabic build, never the filename" }
{ check: "instructor-status-and-claims", element: "ClassCardGrid includes an unconfirmed instructor cover",   fix: "drop the grid and flag it; populate only status-cleared instructors with rights-cleared, text-free covers" }
```

## Checklist for the verifier

- Every image module (`data-slot="element"`) is enumerated and checked, including any VML
  background `src`.
- Every failing check has its own item, with the module named by its `src` and role.
- The fix changes the asset or its hosting, it never weakens the brand palette, the CDN rule, or
  the no-baked-Arabic rule.
- A spec-only review blocks on the host-dependent checks (approved-cdn-hosting, the inbox
  send-test).
- Result is binary: pass only when all checks pass on all modules, otherwise fail.
- No em dash, no en dash, no tatweel, Western numerals only, in this file itself.

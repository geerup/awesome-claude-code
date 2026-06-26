# Compliance and privacy fix list template

The result this gate returns. Pass advances the asset toward the human gate with open items
attached. Fail returns the list below to the owning agent, who regenerates against every item
and resubmits to this same gate. This gate never edits the asset and never adopts a tool. All
example spans are illustrative only.

## Result header

```
asset:       <the asset or spec under review>          # e.g. conversion-path-nonpayer
gate:        compliance-privacy-check
result:      pass | fail
checked:     no-pii-in-urls, consent-correct, suppression-correct, pdpl-residency-surfaced, data-flows-disclosed, no-accreditation-implication, no-tool-adoption
open_items:  <surfaced for the human gate, e.g. PDPL data-residency unresolved; email platform unconfirmed>
```

## On pass

```
result:     pass
note:       advances toward the human gate
open_items: <attached, e.g. Saudi PDPL data-residency requirement unconfirmed; awaiting Ahmed>
```

## On fail: one item per failing check

```
{ check: <check id>, span: "<offending span or condition, quoted exactly>", fix: "<required change>" }
```

## Illustrative fix items (replace with the real findings)

Quote the real offending span or describe the real condition. These are illustrations only.

```
{ check: "no-pii-in-urls",          span: "?email=user@example.com&utm_source=email",        fix: "Remove the email parameter, pass no personal data in the URL" }
{ check: "consent-correct",         span: "consent checkbox pre-ticked on the signup gate",   fix: "Untick by default, require an explicit opt-in for the stated purpose" }
{ check: "suppression-correct",     span: "send audience = all contacts",                     fix: "Exclude paying, unsubscribed, and hard-bounced contacts, and apply the suppression list" }
{ check: "pdpl-residency-surfaced", span: "send to Saudi users, no residency note",           fix: "Surface the Saudi PDPL and data-residency open item for the human gate" }
{ check: "data-flows-disclosed",    span: "signup posts to an unnamed platform",              fix: "Disclose the receiving platform and the pixel or CAPI flow in the package and to the user" }
{ check: "no-accreditation-implication", span: "accredited certificate on completion",        fix: "State it as a completion certificate, drop any accreditation claim" }
{ check: "no-tool-adoption",        span: "wires events directly into an unapproved platform", fix: "Do not adopt or wire it, flag for build-vs-buy and Ahmed's approval" }
```

## Checklist for the verifier

- Every failing check has its own item, with the span or condition quoted exactly.
- Every relevant open item is surfaced for the human gate, not resolved here.
- No tool is adopted or wired; unapproved tools are flagged, not used.
- Result is binary: pass only when all checks pass, otherwise fail.
- No em dash, no personal data in any example link, in this file itself.

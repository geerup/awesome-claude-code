# English copy QA fix list template

The result this gate returns. Pass advances the copy to brand-qa-reviewer. Fail returns the
list below to the author, who regenerates against every item and resubmits to this same gate.
This gate never edits the copy. All example spans are illustrative only.

## Result header

```
asset:      <the asset or variant id under review>     # e.g. email-nonpayer-v1-en
gate:       english-copy-qa
result:     pass | fail
checked:    empowering-tone, no-em-dash, western-numerals, one-clear-cta, no-accreditation-implication, no-invented-offers-titles, plain-active-voice
```

## On pass

```
result: pass
note:   advances to brand-qa-reviewer
```

## On fail: one item per failing check

```
{ check: <check id>, span: "<offending span, quoted exactly>", fix: "<required change>" }
```

## Illustrative fix items (replace with the real findings)

Quote the real offending span verbatim. In these illustrations the banned glyph is named in
brackets instead, so this template file itself stays clean of the em dash and Eastern numerals.

```
{ check: "empowering-tone",            span: "Stop wasting your potential, you are falling behind", fix: "Reframe to what the reader can build, e.g. You already have the drive; here is the path that turns it into a skill" }
{ check: "no-em-dash",                 span: "fast, intelligent [em dash] and yours",               fix: "Replace the em dash with a comma or a period" }
{ check: "western-numerals",           span: "in [eastern arabic numerals] days",                   fix: "Use Western numerals: 7 days" }
{ check: "one-clear-cta",              span: "Start now. Also browse all paths. And see pricing.",  fix: "Keep one primary CTA, demote or remove the competing calls to action" }
{ check: "no-accreditation-implication", span: "earn an accredited certificate",                    fix: "State it as a completion certificate, drop any accreditation claim" }
{ check: "no-invented-offers-titles",  span: "the new Leadership Mastery Path",                      fix: "Remove the unconfirmed title, or stop and ask for a confirmed one from the brief" }
{ check: "plain-active-voice",         span: "<stiff or over-explained corporate phrasing>",        fix: "Shorten to a plain, active, confident sentence" }
```

## Checklist for the verifier

- Every failing check has its own item, with the span quoted exactly.
- The fix names the required change, it does not rewrite the whole asset.
- one-clear-cta may be marked not-applicable when the copy has no intended action.
- Result is binary: pass only when all applicable checks pass, otherwise fail.
- No em dash, Western numerals only, in this file itself.

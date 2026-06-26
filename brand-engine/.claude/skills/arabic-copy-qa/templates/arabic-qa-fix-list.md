# Arabic copy QA fix list template

The result this gate returns. Pass advances the copy to brand-qa-reviewer. Fail returns the
list below to the author, who regenerates against every item and resubmits to this same gate.
This gate never edits the copy. All example spans are illustrative only.

## Result header

```
asset:      <the asset or variant id under review>     # e.g. email-nonpayer-v1
gate:       arabic-copy-qa
result:     pass | fail
checked:    msa-gulf-familiar, thmanyah-tone, no-tatweel, western-numerals, no-em-dash, empowering-framing, rtl-safe
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
brackets instead, so this template file itself stays clean of em dash, tatweel, and Eastern
numerals.

```
{ check: "no-em-dash",     span: "سريع وذكي [شرطة طويلة] وملكك",  fix: "استبدل الشرطة الطويلة بفاصلة أو نقطة" }
{ check: "western-numerals", span: "خلال [رقم عربي شرقي] أيام",     fix: "استخدم الأرقام اللاتينية: 7 أيام" }
{ check: "empowering-framing", span: "لا تضيع وقتك، أنت متأخر", fix: "أعد الصياغة لما يستطيع القارئ بناءه، مثل: خطوة واحدة كل يوم تبني مهارة" }
{ check: "no-tatweel",     span: "مهارة [بها تطويل بين الحروف]",  fix: "احذف التطويل: مهارة" }
{ check: "thmanyah-tone",  span: "<صياغة جامدة أو رسمية زائدة>", fix: "بسّط الجملة وقربها من نبرة محادثة واثقة" }
{ check: "rtl-safe",       span: "<نص مختلط يكسر الاتجاه>", fix: "افصل الأرقام والكلمات اللاتينية بما يحافظ على الاتجاه من اليمين لليسار" }
```

## Checklist for the verifier

- Every failing check has its own item, with the span quoted exactly.
- The fix names the required change, it does not rewrite the whole asset.
- Result is binary: pass only when all seven checks pass, otherwise fail.
- No em dash, no tatweel, Western numerals only in this file itself.

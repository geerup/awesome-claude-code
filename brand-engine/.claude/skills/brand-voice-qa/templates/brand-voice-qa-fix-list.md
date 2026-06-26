# Brand voice QA fix list

The output of `brand-voice-qa`, run by `brand-voice-reviewer`. A binary verdict on Arabic copy against
the documented Maharat brand voice. Pass only when every check passes. On fail, one item per failing
check. Never edit the copy, verify and route only.

## Verdict

```
skill        brand-voice-qa
target       <the Arabic copy under review>
result       pass | fail
```

## On pass

The copy advances to `brand-qa-reviewer`. No fix list.

## On fail

One item per failing check:

```
{ check: <check id>, span: "<the offending span, quoted from the copy>", fix: "<the required change>" }
```

Check ids: voice-alignment, positioning-and-mission, lexicon, instructor-framing, product-framing,
address-and-register, guardrails, result-is-binary.

Example items:

```
{ check: "voice-alignment", span: "أنتِ متأخرة، صحّحي مكياجك", fix: "أعيدي الصياغة إلى تمكين: إطلالة تصنعينها بنفسك، الجمال ثقة لا تصحيح" }
{ check: "instructor-framing", span: "خبير مشهور جداً", fix: "اسند المكانة إلى دليل ملموس، مثل عدد سنوات الخبرة أو جائزة، بصيغة [الاسم] يعلّم [الموضوع]" }
{ check: "product-framing", span: "شهادة معتمدة", fix: "استبدلها بشهادة إتمام مخصصة باسمك، بلا أي إيحاء بالاعتماد" }
```

## Hard rules

- Binary: pass and advance, or fail and return. No soft warnings.
- No item is waved through. The author fixes against the full list and resubmits here.
- Passing this gate is not passing brand QA. `brand-qa-reviewer` runs last.

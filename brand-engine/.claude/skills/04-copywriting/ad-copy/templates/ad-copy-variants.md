# Ad copy variants template

Fill one block per variant. At least two variants per segment. English-first. One CTA each.
All example copy below is illustrative only. Replace it. Do not ship the examples, and do
not invent offers, prices, Skill Path titles, or instructor names.

## Variant block

```
id:        ad-<segment>-<n>          # e.g. ad-busy-pros-v1
segment:   <strategy-artifact segment name>
language:  ar | en
headline:  <one line>
body:      <one or two short lines>
cta:       <exactly one action>
fills:     <asset_brief slot id this variant fills>   # e.g. ig-story-9x16.headline
```

## Illustrative example (Arabic, replace before use)

```
id:        ad-example-v1
segment:   example-segment
language:  ar
headline:  مهارة جديدة تبدأ اليوم
body:      تعلم بخطوات قصيرة تناسب يومك. 10 دقائق تكفي للبداية.
cta:       ابدأ الآن
fills:     example-slot.headline
```

```
id:        ad-example-v2
segment:   example-segment
language:  ar
headline:  ابنِ مهارتك على وقتك
body:      مسار واضح ودروس قصيرة. تتقدم خطوة كل يوم.
cta:       جرب اليوم
fills:     example-slot.headline
```

## Checklist before handoff

- One CTA per variant, active and concrete.
- Two or more variants per segment.
- No em dash, no tatweel, Western numerals only.
- Empowering, never deficit-framed.
- Every offer or price traces to the brief. Nothing invented.
- Each variant maps to a real asset_brief slot in fills.

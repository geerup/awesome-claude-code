# Image prompt sheet template

One block per prompt and its asset brief. Prompts are English and text-free. Never bake Arabic
into a generated image. Copy-overlay slots stay empty for stream 4. All example text is
illustrative only. Replace it. Do not invent dimensions, placements, titles, names, offers, or
prices.

## Prompt and asset brief block

```
id:            prompt-<concept-id>-<placement>     # e.g. prompt-example-1-feed
from_concept:  <creative-concepting concept id>
channel:       paid | lifecycle | organic
prompt_en:     <English, text-free image or video description: subject, mood, light,
                composition, visual constants #141414 / #1A1A1A / accent #009975>
negative:      no text, no lettering, no Arabic script, no watermark
dimensions:    <width x height per placement, e.g. 1080x1080 feed, 1080x1920 story>
safe_areas:    <regions kept clear of critical subject>
overlay_slots:                                     # empty, bound to copy-package in stream 4
  - slot: headline   binds_to: <copy-package variant id, filled in stream 4>
  - slot: subhead    binds_to: <copy-package variant id, filled in stream 4>
  - slot: cta        binds_to: <copy-package variant id, filled in stream 4>
```

## Illustrative example (replace before use)

```
id:            prompt-example-1-feed
from_concept:  concept-example-1
channel:       lifecycle
prompt_en:     A calm workspace at dawn, soft warm light, one focused adult, generous negative
               space, near-black ground #141414, a single emerald #009975 highlight. Text-free,
               premium, uncluttered.
negative:      no text, no lettering, no Arabic script, no watermark
dimensions:    1080x1080 feed, 1080x1920 story
safe_areas:    keep upper third and lower quarter clear for overlay
overlay_slots:
  - slot: headline   binds_to: <to be filled in stream 4>
  - slot: subhead    binds_to: <to be filled in stream 4>
  - slot: cta        binds_to: <to be filled in stream 4>
```

## Checklist before handoff

- Prompt is English and text-free, with a no-text and no-Arabic-script negative.
- No Arabic baked into the image. Overlay slots named and empty.
- Dimensions and safe areas set per placement.
- Designer executes, runs design-qa, human design check on any Arabic.
- No invented values. Missing means stop and ask.
- No em dash, no tatweel, Western numerals only.

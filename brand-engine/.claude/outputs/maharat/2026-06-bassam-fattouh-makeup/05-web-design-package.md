# web-design-package: Bassam Fattouh Teaches Makeup landing surface

Produced by web-design-director (direction) plus web-designer (build-ready spec and web-design-qa) from
the strategy-artifact, the creative direction, and the QA-passed copy-package. This is the stream-6 design
layer, the page conversion-engineer then builds and wires. No copy is written here: regions bind to
QA-passed copy variant ids. No Arabic is baked into imagery. One primary action per view.

## Common envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: web-design-director, web-designer
- stream: 6 conversion path (web design)
- status: qa-passed
- qa: { skill_eval: pass, brand_qa: pass, web_design_qa: pass }
- open_items: gate platform not confirmed (the page is design-ready, the live gate wiring is blocked).
  Rights-cleared Bassam and class footage to confirm (the hero uses a real supplied asset, never generated).

## information_architecture

| # | Section | Job (one line) |
|---|---|---|
| 1 | Hero | the offer and the one primary action: watch the free intro |
| 2 | The free first step | the free intro chapter player, the proof you can sample now |
| 3 | One class, every look | the range, from no-makeup-makeup to glam to editorial (real footage) |
| 4 | The artist | recognized regional artist, 25 plus years, step-by-step craft (real supplied asset) |
| 5 | What you get | the masterclass plus all-access subscription, the public value line |
| 6 | Subscribe | the one primary action repeated: start the subscription |
| 7 | Stay in the loop | low-friction email capture for non-converters (feeds lifecycle) |

Cut anything that does not move the conversion. Each section earns its place.

## ux_flow

```
ad or organic click -> hero (first view, one primary action) -> watch free intro (qualifying action)
   -> subscribe (primary) OR email capture (non-converter) -> [subscribe] confirm -> member onboarding
   -> [email capture] lifecycle nurture
states to design: first view, video loading, video playing, video error, signup default, submitting,
   submitted, error.
```

## wireframe (region level, RTL reading order top-right, one primary action per view)

- Hero: headline region, subhead region, one emerald primary action (watch the free intro), supporting trust line.
- Free-intro: video player region (captions on), one secondary action (subscribe) below, not competing with the hero primary.
- Range: a restrained grid of real look stills, no competing CTA.
- Artist: a real supplied portrait or still, trust copy region.
- What you get: value list region, the public value line region.
- Subscribe: the one primary action repeated.
- Email capture: single email field, one action, clear consent line.

## visual_direction

- Brand constants on the web surface: background #141414, card surfaces #1A1A1A, emerald #009975 as a
  highlight (the primary action and progress only), generous space, premium and uncluttered.
- Imagery: real, rights-cleared Bassam and class footage only. No generated likeness. Text-free imagery;
  all words are real overlaid copy bound by id. Video carries captions.

## web_asset_brief

| Asset | Dimensions | Safe areas | Copy-overlay slots (empty, ar/en) |
|---|---|---|---|
| Hero background or still | responsive, 16:9 desktop, 4:5 mobile | center-safe for headline | bound to copy ids, not free slots |
| Range stills | square and 4:5 | per grid | none (visual only) |
| Artist still | 4:5 | face-safe | none (visual only) |

## conversion_intent

- The single primary action the page optimizes toward: start the subscription. The free intro play is the
  qualifying micro-conversion that precedes it; the email capture is the fallback for non-converters.

## design_spec (web-designer, build-ready)

```
components   hero (headline, subhead, primary action), free-intro player (captions, secondary action),
             range grid, artist trust, value list, subscribe block (primary action), email-capture block.
             One primary action per view.
grid         12-column desktop, 4-column mobile, mobile first. Generous gutters and margins.
breakpoints  sm 360, md 768, lg 1200 (Western numerals, px). Content reflows with no clip or overflow.
type_scale   display, h1, h2, body, caption. Arabic and Latin both supported, Arabic primary.
tokens       color: bg #141414, surface #1A1A1A, accent emerald #009975 (highlight, not flood);
             spacing: 4, 8, 16, 24, 40, 64; radius: 8, 16.
states       default, hover, focus (visible ring), active, disabled, loading (player and submit),
             error (player network error, form validation). Every interactive element covered.
rtl          direction rtl at sm, md, lg. Arabic primary, reading order right-to-left. Western numerals.
             Mixed Arabic, English, and numerals hold direction at every breakpoint.
accessibility contrast meets the bar on #141414 (emerald and white pass), logical focus order, semantic
             landmarks and headings, touch targets 44px minimum, alt text slots on every image, captions
             and transcript slot on the video.
performance  fast first render, hero above the fold without a blocking video, intro video lazy-loaded on
             intent, image weight budgeted, primary action visible without a scroll on mobile.
copy_refs    hero headline -> copy-package/V1 (ar) and V1e (en); hero primary action -> V1 cta;
             value line -> copy-package/V4 body value line; subscribe action -> V4 cta;
             range and artist trust copy -> bound by id at build. No free text on the page.
```

## web_design_qa (web-designer verdict)

- result: pass.
- responsive-rtl: pass (direction rtl at sm, md, lg; Arabic reading order held; mixed direction does not break).
- visual-constants: pass (#141414, #1A1A1A, emerald #009975 as accent, not flood).
- western-numerals-rendered: pass.
- no-baked-arabic-text: pass (copy bound by id; imagery is real supplied footage, never generated text).
- responsive-breakpoints: pass (sm, md, lg declared; clean reflow; primary action visible without a scroll on mobile).
- interaction-states: pass (default, hover, focus, active, disabled, loading, error all specified, incl. the player).
- accessibility: pass (contrast, focus order, semantic structure, 44px targets, alt and caption slots).
- performance-budget: pass (lazy video, budgeted image weight, fast first render).
- one-primary-action: pass (one primary action per view; the free-intro and subscribe never compete in the same view).
- premium-uncluttered: pass.
- human-check-preserved: a human design check stays the final manual step before any publish.

## Handoff

Hands the design_spec and verdict to brand-qa-reviewer (passed), then to conversion-engineer to implement the
page, wire the signup gate and the data-tracking-engineer event_plan, and take the go-live decision to the human
gate. Nothing builds or publishes until the gate clears.

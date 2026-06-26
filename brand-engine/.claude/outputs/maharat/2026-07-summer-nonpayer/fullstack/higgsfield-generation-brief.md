# Higgsfield generation brief: Summer of Skills visuals

The "new brief" the creative production stage hands to Higgsfield. It pairs each generatable,
text-free visual with the Higgsfield call that produces its base, and with the QA-passed AR and
EN overlay copy that is composited in build afterward. This brief is the bridge from the visual
brief (creative-package.md, design-specs.md) and the overlay copy (visual-overlay-copy.ar.md,
visual-overlay-copy.en.md) to the generative tool.

- campaign_id: 2026-07-summer-nonpayer
- assembled_by: orchestrator (creative production)
- date: 2026-06-16
- tool: Higgsfield (generate_image), model marketing_studio_image (commercial/ads default)
- credits available at assembly: 966 (Plus). Each generation is cost-preflighted with get_cost.

## The hard rule this brief enforces (read first)

Generated images are TEXT-FREE. Higgsfield generates the base visual only: no Arabic text, no
English text, no instructor likeness, ever. The reason is in the constitution: generative tools
mangle Arabic script, so Arabic is never baked into a generated image. The AR and EN copy lives
in visual-overlay-copy.ar.md and visual-overlay-copy.en.md and is composited as a real text layer
in build (Canva or Figma) on top of the generated base. That overlay step is how an "Arabic
visual" and an "English visual" are produced from one shared text-free base.

Therefore every prompt below is the text-free prompt from creative-package.md (P1 to P6).
Nothing in a prompt asks the model to render text or a person.

## What goes to the model vs what is overlaid

| Layer | Source | Tool | Text? |
|---|---|---|---|
| Base visual | prompts P1 to P6 (creative-package.md) | Higgsfield generate_image | none, text-free |
| AR overlay | visual-overlay-copy.ar.md (slots, source variant ids) | build (Canva/Figma), RTL | real Arabic text |
| EN overlay | visual-overlay-copy.en.md (slots, source variant ids) | build (Canva/Figma), LTR | real English text |

## Generation set (text-free bases, no-photography concepts only)

C3 instructor portraits and C6 multi-field reel are excluded here: they depend on rights-cleared
photography and footage (asset OPEN ITEMs), never generated. The generatable set:

| # | Asset | Concept | Prompt | Model | Aspect ratio | Overlay slots (AR + EN) |
|---|---|---|---|---|---|---|
| G1 | AB1 breadth hero (feed) | C1 | P1 | marketing_studio_image | 4:5 | AB1 [ar/en headline], [ar/en subline], [ar/en cta chip] |
| G2 | AB9 landing hero | C1 | P2 | marketing_studio_image | 16:9 | AB9 [ar/en landing hero headline/subline/cta] |
| G3 | AB2 per-field base (music) | C2 | P3 | marketing_studio_image | 1:1 | AB2 music: [ar/en field headline], [ar/en instructor name + credential] (Ragheb Alama, confirm-at-gate), [ar/en cta], [ar/en free chapter callout] |
| G4 | AB6 retargeting breadth grid | C5 | P5 | marketing_studio_image | 4:5 | AB6 [ar/en headline], 7 [ar/en field labels], [ar/en cta chip] |
| G5 | AB7 campaign identity | C7 | P6 | marketing_studio_image | 4:5 | AB7 [ar/en campaign theme label] (صيف المهارات / Summer of Skills), [ar/en supporting line], [ar/en cta chip] |
| G6 | AB4/AB5 lifecycle free-lesson still | C4 | P4 | marketing_studio_image | 4:5 | AB4/AB5 [ar/en header line / push line], CTA |

Per-field extension (not generated in this pass, same template as G3): the other six C2 fields
(cooking, acting, makeup, business, styling, marketing) reuse the P3 base with only the abstract
icon swapped per design-specs (cooking arc, acting light cone, makeup brush arc, business steps,
styling drape, marketing radial node). Generate on request; overlay copy already bound in
visual-overlay-copy.{ar,en}.md.

## Exact prompts (text-free, English only, lifted from creative-package.md)

### G1 prompt (P1, C1 hero, 4:5)
A premium, editorial abstract grid composition. Near-black background, hex #141414, fills the
entire frame. Seven rectangular cards in deep charcoal #1A1A1A, arranged in an asymmetric mosaic:
some cards slightly taller, some slightly wider, all with generous breathing room between them.
The spaces between cards are pure #141414, visible and clean. One card near the visual center of
the grid carries a thin vertical stripe on its left edge in deep emerald, hex #009975,
approximately 4 pixels wide, running the full card height. All other cards are plain #1A1A1A with
no accent. All card interiors are empty: generous flat #1A1A1A surface, no text, no icon, no image
inside. The overall feel is a clean editorial display grid, quiet and premium, suggesting choice
and variety without naming any field. No text, no human figure, no product, no decorative element
beyond the single emerald stripe. High-end studio quality. No watermark. Aspect ratio 4:5.

### G2 prompt (P2, C1 hero, 16:9)
Identical composition to G1 but in 16:9. The seven cards reflow into a horizontal mosaic. The same
single emerald #009975 left-border stripe on one focal card. Generous padding on all edges. No
text. No figure. No product. #141414 background throughout. Premium and uncluttered.

### G3 prompt (P3, C2 per-field base, music, 1:1)
A single #1A1A1A rectangular card, centered on a #141414 field. The card occupies approximately 70
percent of the frame horizontally and 65 percent vertically. Inside the card, centered in the
upper two-thirds of the card interior, a single minimal abstract line shape in deep emerald
#009975 suggesting a smooth curved wave, like a single period of a clean sine wave drawn with a
2-pixel line, open at both ends. The lower third of the card interior is empty flat #1A1A1A,
reserved for overlay text. Along the very bottom edge of the card, a full-width horizontal bar in
#009975, 4 pixels tall. No text. No face. No product label. Square 1:1.

### G4 prompt (P5, C5 retargeting grid, 4:5)
A clean structured grid on a #141414 background. Seven small square tiles in #1A1A1A, arranged in
a 3-4 pattern (three tiles in the top row, four tiles in the bottom row), centered in the frame
with equal generous spacing between each tile and between the grid and the frame edges. Each tile
contains a single minimal single-line abstract icon in #009975, each icon distinct and abstract,
no shared shape: the seven icons suggest, in sequence, a wave arc, a rising arc with a dot above
it, a downward light cone, a horizontal sweep arc, three ascending steps, a draped curve, and a
radial node cluster. Icons are 2 pixels wide, open line shapes, no fill. One tile, the
center-bottom position, has its icon in a slightly brighter #009975 at full opacity while all
other icons are at 70 percent opacity. Below the grid, a thin full-width horizontal bar in
#009975, 3 pixels tall. No text, no labels, no product. All tile interiors empty except the icon.
Aspect ratio 4:5.

### G5 prompt (P6, C7 campaign identity, 4:5)
A premium minimal single-card composition. Near-black background #141414, entire frame. A #1A1A1A
rectangle centered in the frame: 70 percent of frame width, 45 percent of frame height. Above the
rectangle and flush with its top edge, a thin horizontal bar in #009975, 3 pixels tall, spanning
the full width of the rectangle only. Below the rectangle and flush with its bottom edge, a
matching thin horizontal bar in #009975, 3 pixels tall, same width. The rectangle interior is
entirely empty, flat #1A1A1A, no icon, no text, no element. The frame above and below and around
the rectangle is pure #141414, clear and generous. No text, no figure, no decorative element
beyond the two emerald bars. Premium and spare. Aspect ratio 4:5.

### G6 prompt (P4, C4 free-lesson path, 4:5)
A premium minimalist abstract composition. Near-black background, hex #141414, fills the entire
frame with generous empty space. In the lower center of the frame, a #1A1A1A rectangular card
plane, horizontal, occupying the center third of the frame vertically and about 80 percent
horizontally. Centered on this card plane, a single clean path or arc in deep emerald #009975,
drawn as if traced by a steady hand from the left edge of the card to the right edge, slightly
bowed upward at center, with a faint luminous glow at the rightmost terminal point suggesting
arrival. The path is a single line, 3 pixels wide, no fill, no arrowhead. The glow at the right end
is a soft radial bloom, 20 to 30 pixels, in #009975 at 60 percent opacity fading to transparent.
No text. No face. No product. Above and below the card plane, generous #141414 space for overlay
text. Aspect ratio 4:5.

## Build (overlay) step, after generation

For each generated base, the designer composites the bound overlay copy from
visual-overlay-copy.ar.md (RTL) and visual-overlay-copy.en.md (LTR) into the labeled slots and
safe areas, producing the final Arabic visual and English visual per format. Western numerals
only. Instructor names in overlay are confirm-at-gate; verify-before-public-use facts excluded.

## Gate status

- Overlay copy: AR pass, EN pass (after one verbatim-subset fix). visual-overlay-qa-verdict.md.
- The generated bases run design-qa (designer) before the overlay composite advances, and the
  final composited visuals run brand-qa before any publish. Nothing publishes or spends on media.

## Results

Generation results (job ids, model, cost, status) are recorded in
higgsfield-generation-results.md after the run.

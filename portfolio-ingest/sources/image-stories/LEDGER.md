# Image Story Ledger

Durable memory for images Ahmed sends with their story, so they can be used
for storytelling in the portfolio. This file survives context summarisation and
container resets - it is the source of truth, not my chat memory.

## How this works

When Ahmed sends an image and tells me its story, I will:
1. Save the image file into this folder as `img-NN-<slug>.<ext>` (webified copy
   into `rebuild/assets/` when it is chosen for a page).
2. Add a numbered entry below capturing: what the image shows, the story in
   Ahmed's words, the provenance (when/where/who), and where it is meant to go.
3. Commit both, so the context is never lost.

Rules that carry over from the rest of the build:
- The story text is treated as an owner-approved source (same authority tier as
  the stats sheet). It can be quoted and paraphrased in case copy.
- Any hard number inside a story still needs a named source to ship as a stat;
  otherwise it stays as narrative colour, not a headline figure.
- No invention. If a caption needs a fact the story does not give, it becomes a
  NEEDS_HUMAN chip, not a guess.

## Entries

<!-- Template - copy per image:

### img-01 - <short title>
- **File:** sources/image-stories/img-01-<slug>.jpg  (web copy: rebuild/assets/<slug>.jpg)
- **Shows:** <plain description of what is in the frame>
- **Story (Ahmed's words):** "<the story as told>"
- **Provenance:** <date / place / event / who is in it / who shot it>
- **Intended use:** <which case / section / as hero or inline>
- **Status:** received | placed | held
- **Added:** <date>

-->

_No images logged yet. Send the first one whenever you're ready - a photo plus a
sentence or two on what it is and what it proves, and I'll file it here._

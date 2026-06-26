---
description: Ingest uploaded or linked material - read it, OCR text, auto-tag images into the asset library, and mine your content into voice, themes, and verified claims. Usage - /ingest <files, a Drive folder, URLs, or a Descript project>
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

# /ingest  (alias /train-on-me)

Run the `asset-ingest` skill on "$ARGUMENTS". This is how the engine learns you: it reads your
material, recognizes text and images, and distills your voice and claims into the profile. It is
corpus distillation and retrieval grounding, not model fine-tuning.

## What to do

1. Enumerate the source (uploaded files, a Drive folder, URLs, or a Descript project for
   video/audio transcripts). Log the inventory; nothing is skipped silently.
2. Text recognition: read every item with native multimodal Read (images, screenshots, PDFs,
   docs). Extract the text into structured notes.
3. Image recognition: add a row per image to `context/subjects/_IMAGE-CATALOG.md` (slug,
   placement, description, colors, faces_present, rights, usage, alt).
4. Corpus mining: distill voice -> `skills/subject-marketing/me/voice.md`; themes and point of
   view -> `context/subjects/me.md` and `.agents/brand-context.md`; every factual claim with its
   source -> the claims table (verified | unverified | disputed); unsourced or sensitive ->
   held-back ledger.
5. Summarize what was learned and what is still an open item, and suggest the next foundation
   step (`/mine-subject me`, then `personal-brand`).

## Rules
- Verify before claiming; found-in-my-own-material is still unverified until sourced.
- Flag anything naming a client/employer or under NDA as held-back.
- No fabricated text or tags. Unreadable means logged as blocked.

$ARGUMENTS

---
name: asset-ingest
description: Ingest uploaded or linked material into the engine. Use to read images, screenshots, PDFs, documents, and transcripts, extract their text (OCR), auto-tag images into the asset library, and mine your own content corpus into your voice, themes, and verified claims. Triggers on "ingest this", "read these files", "tag these images", "extract the text from", "OCR", "train on my content", "learn my voice", "build my profile from", "what's in these". Native multimodal: it reads images and PDFs directly, no external OCR service. "Train on my content" means corpus distillation and retrieval grounding, not model fine-tuning.
metadata:
  version: 1.0.0
---

# Asset Ingest

Turn raw uploads and links into structured, reusable engine inputs: extracted text, a tagged
asset library, and a distilled profile of your voice and claims. This is the front door for
"text recognition", "image recognition", and "train me on my content".

## Before you start

Check `.agents/brand-context.md` and `context/subjects/me.md`. Ingestion feeds both. If they are
still TODO, ingestion is how they get filled.

## What it does

### 1. Text recognition (OCR) and document reading
Read every uploaded or linked item with native multimodal Read:
- images and screenshots: extract all visible text and a description
- PDFs: read pages (use the `pages` parameter for long PDFs)
- documents (Drive, uploads): read in full
- video and audio: get the transcript via Descript (`export_transcript` / `get_project`)
Write the extracted text into structured notes under the relevant subject or run. Anything
unreadable is logged as blocked, never skipped silently.

### 2. Image recognition and auto-tagging
For each uploaded image, produce a catalog row in the asset library
(`context/subjects/_IMAGE-CATALOG.md`):
- subject/slug it belongs to, placement (headshot, banner, post, logo, screenshot)
- a one-line description, the dominant colors (hex), orientation and dimensions if known
- `faces_present: yes|no` (real people), rights/source note, and a descriptive alt text
- usage flags: ok-for-public | internal-only | needs-rights-check
This is the same catalog discipline the engine used for instructor portraits, reused for your
own assets. A generated image of a real person is never tagged as a real photo.

### 3. Corpus mining ("train on my content")
Distill your own material (writing, talks, posts, CV, transcripts) into the profile. This is
retrieval grounding and pattern distillation, NOT fine-tuning:
- voice: register, hook patterns, signature phrases, cadence -> `skills/subject-marketing/me/voice.md`
- themes and point of view -> `context/subjects/me.md` and `.agents/brand-context.md`
- claims: every factual claim found, with its source, into the claims table (verified |
  unverified | disputed); anything unsourced becomes a held-back ledger row
Hand off to `/mine-subject me` to build the full pack and `personal-brand` to set positioning.

## Inputs and outputs

Inputs: uploaded files, Drive links, URLs, Descript projects.
Outputs: extracted-text notes; asset-library rows in `context/subjects/_IMAGE-CATALOG.md`;
updated `context/subjects/me.md` (claims, themes), `skills/subject-marketing/me/voice.md`
(voice), and `.agents/brand-context.md` (foundation). Nothing public is produced here; ingestion
feeds the foundation.

## Hard rules
- Verify before claiming. A fact found in your own material is still `unverified` until sourced.
- Consent and confidentiality: flag anything naming a client/employer or under NDA as held-back.
- No fabricated tags or text. If an image is unreadable, say so.
- Distillation, not fine-tuning. Be explicit about that when asked.

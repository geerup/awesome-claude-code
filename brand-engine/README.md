# Brand & Career Engine

A profile-parameterized agentic engine for building a **personal brand and career**: assets,
copy, websites, visuals, content, and outreach. Open this directory as a Claude Code project and
run the workflows; everything stops at a human gate (you) before anything sends or publishes.

It was adapted from a mature, campaign-agnostic marketing engine originally built for **Maharat**
(an Arabic-first edtech platform). That engine is preserved in full as the archived `maharat`
profile, nothing thrown out. The machine (agents, runtime, skills, SOPs, gates) is reused as-is;
only the facts layer was re-pointed to you, the language flipped to English-first, and a brand
foundation plus new personal-brand capabilities added.

## What it does for you

- **Brand foundation**: 29 brand-building skills (strategy, positioning, identity, voice, story,
  messaging, naming, personal-brand, architecture) define the brand before any asset is made.
- **Career stories**: `career-narrative` turns your real experience into engaging, true stories.
- **Substack content**: `/substack-post` produces copy + images from a simple prompt, staged for
  your edit, published on your say-so.
- **Websites and portfolios**: `/build-website`, `/build-portfolio`, `/manage-site` design, build,
  and manage a WordPress or GitHub Pages site.
- **Visuals**: `/build-visual` produces on-brand assets via Canva.
- **Ingestion and "training"**: `/ingest` reads your uploads (text recognition / OCR), tags your
  images into an asset library (image recognition), and mines your content into your voice and
  verified claims. This is distillation and retrieval, not model fine-tuning.
- **Image/video generation**: via Canva and Descript, with a gated path to adopt a dedicated
  generative MCP.

## Quick start

1. Open `brand-engine/` as a Claude Code project.
2. `/brand-context` then `/ingest <your CV, writing, talks, links>` to build the foundation.
3. `personal-brand`, then pick a starter brief from `.claude/briefs/starters/`.
4. Run it: `/build-portfolio`, `/substack-post "..."`, `/build-website`, or `/new-campaign`.

The constitution is `.claude/CLAUDE.md`. Orientation is `.claude/context/00-start-here.md`. The
profile model is `.claude/context/profiles/_README.md`.

## The solo tool stack

Canva (visuals), Descript (video/audio), Gmail (email/outreach drafts), Google Drive (storage),
Google Calendar (content cadence), GitHub (site/portfolio), WebSearch/WebFetch (research).
Paid ads, warehouse, and payments are deferred until you opt in. See
`.claude/context/04-tools-and-access.md`.

## Layout

```
brand-engine/
├── README.md            this file
├── .gitignore           tracks the engine; ignores caches/secrets
├── .mcp.json            engine-spun MCP servers (firecrawl optional)
├── .agents/
│   └── brand-context.md the foundation the 29 brand skills auto-read
└── .claude/             the engine (CLAUDE.md, agents, runtime, skills, sops, context, ...)
    └── context/profiles/maharat/   the original Maharat engine, archived in full
```

Nothing about the original Maharat engine was deleted. To run a maharat-profile campaign, switch
the active profile in `.claude/context/active-profile.md`.

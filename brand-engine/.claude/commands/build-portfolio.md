---
description: Build a portfolio - a site or page showcasing your work, case studies, career story, and visuals. Usage - /build-portfolio [target: wordpress | github-pages]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# /build-portfolio

Assemble a portfolio as a first-class output: the site, the case studies, the story, and the
visuals, stopping before anything goes live.

## What to do

1. Load `context/subjects/me.md` (signature projects and verified claims), `.agents/brand-context.md`,
   and `context/brand-voice.md`. If thin, run `/ingest` and `personal-brand` first.
2. Story and case studies: `career-narrative` produces the origin arc (portfolio intro) and a
   STAR case study per signature project, bound to verified claims.
3. Visuals: `/build-visual` produces the portfolio imagery and any project shots in your brand
   identity (real assets for real work; resolve from the asset library).
4. Site: `/build-website` designs and builds the portfolio surface (web-design-director ->
   web-designer -> conversion-engineer) for the chosen target (WordPress or GitHub Pages), with
   one clear primary action (contact / hire / subscribe).
5. Gates: `web-design-qa`, `accessibility-qa`, `english-copy-qa`, `brand-qa-reviewer`. Stop at
   the human gate with a preview and the deploy step ready. Nothing publishes without your sign-off.

## Rules
- Show only real, verified work. No invented results; client work named only with consent.
- Your brand identity throughout. No em dashes.

$ARGUMENTS

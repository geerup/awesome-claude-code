---
description: Design and build a website or landing page, via web-design-director -> web-designer -> conversion-engineer, shipped to WordPress (REST) or GitHub Pages. Usage - /build-website <what, e.g. "a personal home page" or "a services landing page">
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# /build-website

Design and build a web surface end to end, stopping before anything goes live.

## What to do

1. Load `context/brand-voice.md` (visual constants) and the active brief. If the brand identity
   is TODO, run `brand-identity` first.
2. `web-design-director`: information architecture, UX flow, and a build-ready responsive design
   spec (the web-design-package). Runs `web-design-qa`.
3. `copywriter-en` writes the page copy (english-copy-qa), bound to verified claims
   (`context/subjects/me.md`). Arabic only if the brief sets it in scope.
4. `web-designer` + `conversion-engineer` realize the spec as the actual page (HTML/CSS or a
   theme), wire a single clear primary action, and prepare the deploy:
   - GitHub Pages: build the static site and stage it on a branch (do not publish without sign-off).
   - WordPress: prepare the REST API payload (app-password, gated); writes stay human-gated.
5. Run `web-design-qa`, `accessibility-qa`, `brand-qa-reviewer`, and `compliance-privacy-check`
   (if it collects data). Stop at the human gate with a preview and the deploy step ready.

## Rules
- Nothing publishes without your sign-off. Default is a staged preview.
- One primary action per view. Verified claims only. No em dashes.
- The site carries your brand constants. WordPress write access is a gated adoption (see
  `context/04-tools-and-access.md`).

$ARGUMENTS

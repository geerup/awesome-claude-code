---
description: Connect to and manage your website (WordPress or otherwise) - read pages, draft edits, and publish on your approval. Usage - /manage-site <action, e.g. "list pages", "update the about page", "publish the new post">
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

# /manage-site

Connect to your live site and manage it. Reads are free; any write or publish stops for your
sign-off.

## What to do

1. Identify the target and access from `context/04-tools-and-access.md`:
   - WordPress: the site URL and an application password (REST API). If not yet provided, ask for
     them and record the adoption (writes stay gated). Read via the REST API
     (`/wp-json/wp/v2/...`); write via authenticated POST only after approval.
   - GitHub Pages or other static site: the repo. Read the source; stage changes on a branch.
2. For a read action ("list pages", "show the about page"), fetch and summarize. No change.
3. For an edit ("update the about page", "fix the services copy"):
   - `copywriter-en` drafts the change (english-copy-qa), bound to verified claims.
   - `web-designer` prepares the exact diff or REST payload.
   - Run `brand-qa-reviewer` and, if it collects data, `compliance-privacy-check`.
   - STOP at the human gate: show the before/after and the publish step. Apply only on approval.
4. For a publish, perform exactly the one approved action (POST to WordPress, or merge/deploy the
   static branch), then log it per `runtime/send-safeguards.md`.

## Rules
- Reads are safe; writes and publishes are human-gated, one approved action at a time.
- Never edit live content silently. Always a preview/diff first.
- Verified claims only. No em dashes.

$ARGUMENTS

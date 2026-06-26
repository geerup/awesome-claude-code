---
description: Produce a Substack post from a simple prompt - copy plus images in your brand - staged for your edit and control before publishing. Usage - /substack-post <topic or prompt>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# /substack-post

Turn a simple prompt into a ready-to-edit Substack post: copy plus images, in your voice and
visual identity. You stay in control: it stops as a draft for your edit, and publishes only on
your say-so.

## What to do

1. Load `.agents/brand-context.md`, `context/brand-voice.md`, your content pillars (from
   `personal-brand`), and `skills/subject-marketing/me/voice.md`. If these are TODO, run
   `/brand-context` and `/ingest` first.
2. `content-marketer` + `copywriter-en` draft the post from the prompt "$ARGUMENTS": a hook, the
   body in your voice, and a clear takeaway. English-first. Bound to verified claims.
3. `creative-director` writes a text-free image brief; `designer` generates the lead image (and
   any inline images) in Canva, in your brand identity. Run `design-qa`.
4. Run `english-copy-qa` and `brand-qa-reviewer` on the copy.
5. Assemble the post (title, subtitle, body, images, alt text) and STOP at the human gate: present
   it for your edit. This is the control point. Apply your edits.
6. On your approval, publish via the chosen path:
   - default: email-to-Substack (compose the post as a Gmail draft to your Substack publish
     address; you send it), or
   - Substack API if adopted (see `context/04-tools-and-access.md`).
   Nothing publishes without your sign-off.

## Rules
- Your voice and visuals, not generic. Verified claims only. Nothing under NDA.
- One clear idea per post. No em dashes.
- The draft-and-control step is mandatory; auto-publish is never the default.

$ARGUMENTS

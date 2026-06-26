---
name: career-narrative
description: Turn your career into engaging, true stories. Use to retell your career, build an origin story, write case studies of your work, craft talk or interview narratives, or shape the story behind a LinkedIn About, a portfolio, or a Substack post. Triggers on "tell my career story", "retell my experience", "my origin story", "make my background compelling", "case study of", "the story behind this project", "narrative for my portfolio", "interview story", "STAR story". Combines the brand-story and personal-brand frameworks with copywriting, bound to your verified claims.
metadata:
  version: 1.0.0
---

# Career Narrative

Make your real experience compelling. A career told as a list of roles is forgettable; told as a
story with stakes, turns, and a through-line, it is memorable and quotable. This skill shapes
that story without inventing any of it.

## Before you start

Read `context/subjects/me.md` (the claims table is binding, and the "Career story material"
section holds your chapters and signature projects), `skills/subject-marketing/me/voice.md`
(your register and hooks), and `.agents/brand-context.md` (the one thing to be known for). If
these are thin, run `/ingest` and `personal-brand` first.

## What it produces

Pick the cut the brief needs; all rest on the same verified spine.

- Origin arc: the through-line of your career as a 3-act story (where you started, the turn, what
  you do now and why). Long (About page), medium (homepage), and one-liner versions.
- STAR case studies: for a signature project, the Situation, Task, Action, Result, told as a
  story, not a bullet list. Results use only verified figures.
- Talk and interview narratives: the 3 to 5 stories you can tell on demand, each with a point.
- Cut-downs: LinkedIn About, portfolio intro, a Substack origin post, a bio.

## Method

1. Find the through-line: the one thing your career has been building toward (from brand-context).
2. Choose the chapters that serve it (from me.md). Cut the rest; a story is what you leave out.
3. Give each chapter a stake and a turn: what was at risk, what changed.
4. Anchor every claim to a verified row. A figure, title, or outcome that is not verified does not
   appear; mark it to-confirm.
5. Land the point: what each story proves about how you work.

## Gate stack
Pack eval (subject-marketing/me) -> english-copy-qa (arabic-copy-qa if Arabic in scope) ->
brand-qa-reviewer -> human gate (you).

## Hard rules
- True stories only. No invented results, titles, dates, or roles. No overstating your part.
- No client or employer named without consent; nothing under NDA.
- Your voice, not a generic "inspirational" register. No em dashes.

## Related
- `brand-story` (origin and founder narrative frameworks), `personal-brand` (point of view and
  positioning), `04-copywriting` (the words), `subject-marketing/me` (the verified claims).

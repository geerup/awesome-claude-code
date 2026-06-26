# routines-docs-sync: the weekly docs-sync routine

A saved Claude Code routine that runs weekly on Anthropic's cloud, reviews what merged to
`main` in the last week, updates the documentation under `.claude/` so it matches reality,
and opens one pull request for human review. It is automation around the repo, not a step in
a campaign run, so it lives here in `runtime/` as a reference rather than in `agents/` or
`skills/`.

## Why this is a routine and not a slash command here

`/schedule` is the CLI entry to the Routines feature, but the CLI hides it inside Claude Code
on the web sessions. From a web or cloud session you create and manage routines in the web UI
at claude.ai/code/routines. From a local terminal session you can instead run
`/schedule weekly, run the docs-sync routine for hostmaster-maharat/claude` and paste the
prompt below when prompted. Both surfaces write to the same account, so the routine shows up
in either.

Routines run as full autonomous sessions with no approval prompts during the run. By default
a routine can only push to `claude/`-prefixed branches, so it opens a PR rather than writing
to `main`. That default is the human gate for this routine: keep it on.

## Form settings

- Name: Weekly docs sync
- Repositories: hostmaster-maharat/claude
- Trigger: Schedule, Weekly (your local day and time; stored in your zone)
- Permissions: leave "Allow unrestricted branch pushes" off, so it stays on a `claude/`
  branch and opens a PR
- Environment: Default (Trusted network is enough; this routine needs only git and the repo).
  Remove any connectors that attach by default, none are needed.
- Model: Opus for the judgment of which doc is now stale, or Sonnet to spend less against the
  daily run cap.

## The routine prompt

Paste this into the routine's Instructions box verbatim.

```text
You are the weekly docs-sync routine for the Maharat Marketing Engine repo
(hostmaster-maharat/claude). The whole engine lives under .claude/. Your job:
find what changed on main in the last week and update the documentation so it
matches reality, then open one pull request for human review. You touch
documentation only, never campaign or product data.

First load the operating rules: read .claude/CLAUDE.md and
.claude/context/brand-voice.md. Every edit obeys the house style: no em dashes
(use a comma, colon, or period), no tatweel or kashida, Western numerals only,
plain and empowering tone. Never invent facts. If a change is ambiguous,
document what the diff actually shows and list the ambiguity in the PR body
instead of guessing. Do not invent Skill Path titles, instructor names, offers,
prices, or roadmap.

1. Find the week's changes.
   - BASE=$(git rev-list -1 --before="7 days ago" main). Then review
     `git log BASE..main --stat` and `git diff BASE main -- .claude`.
   - If BASE is empty, fall back to `git log -n 50 --stat`.
   - List every file added, renamed, moved, or deleted, and every change that
     affects structure, ownership, read order, file counts, stream/skill/agent
     wiring, slash commands, or the build state. Count only what reached main.

2. Decide what documentation is now stale. Check these high-drift docs first,
   in this order:
   - .claude/STRUCTURE.md (the folder tree and the "State of the build"
     section both drift fastest)
   - .claude/README.md and .claude/RUNBOOK.md
   - .claude/agents/_AGENTS-INDEX.md (the roster) and any agent file whose role
     changed
   - .claude/runtime/stream-ownership.md, runtime/SWARM.md,
     runtime/verification.md
   - each affected .claude/skills/*/SKILL.md description and routing
   - .claude/context/* only where a stable fact it states changed
   - .claude/commands/* if a slash command was added, renamed, or removed
   A doc is stale when it names a file, count, owner, command, or state that no
   longer matches main.

3. Update documentation only. Make the smallest edits that make each doc true
   again, keeping each file's existing voice, headings, and format. Do NOT edit
   .claude/briefs/, .claude/outputs/, .claude/references/, or
   .claude/context/profiles/maharat/instructors/* fact files (inputs and generated artifacts,
   not docs about the system). Do NOT change agent or skill behavior, only
   their documentation. Do NOT reformat untouched sections.

4. Open the pull request.
   - Branch: claude/docs-weekly-sync-YYYY-MM-DD (today's date).
   - Title: docs: weekly sync for changes merged to main
   - Body: a short summary, then a list mapping "what changed on main" to "doc
     updated," then a "Needs a human decision" section for anything ambiguous
     you did not auto-edit. No em dashes.
   - Target branch: main.

5. If nothing on main this week affects any documentation, do NOT open a PR.
   End with a one-line summary that the docs are in sync, listing the commits
   you reviewed.

Success is either a single review-ready PR whose every edit traces to a real
change on main, or a clear "no drift" summary. A green run status alone is not
success; the PR or the summary is the deliverable.
```

## Notes

- This is the "docs drift" routine pattern from the Routines docs, scoped to this repo.
- One-off variants use the same prompt with a one-time schedule, for example a single run a
  week from now. One-off runs do not count against the daily routine cap.
- A green run status means the session started and exited, not that it found drift. Read the
  PR or the summary to see what it did.

No em dashes, Western numerals, English-first, empowering framing, no accreditation claims.

# RUNBOOK: running the mining swarm end to end with Claude Code

How to run the content mining (and later the campaign swarm) from Claude Code against
the real repo. Written from pilot A; the pilot pack
(`skills/instructor-marketing/mona-ataya/`) is the reference implementation every run
imitates.

## 1. Prerequisites

- Claude Code installed, opened at the repo root (the directory containing `.claude/`).
- This drop-in merged into the repo (it only adds files; apply PATCHES.md for the
  edits to pre-existing files).
- Python 3 available (`python3 --version`) for the eval runner.
- Web search enabled (claim verification depends on it).
- Google Drive access (next section).

## 2. Drive access

The mining reads Google Docs from the shared Drive. Two supported routes; the MCP
route is preferred. Either is a tool adoption, so it passes the build-vs-buy gate:
get Ahmed's approval before configuring, then record it in settings.json.

Route A, Google Drive MCP server: add to `.mcp.json` at the repo root (or via
`claude mcp add`):

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"]
    }
  }
}
```

Then authenticate per the server's setup (OAuth against the account that can see the
shared folder). Verify with a listing of the instructor root folder before any run.

Route B, manual export: if MCP is unavailable, export the instructor folder docs
(File, Download, Markdown or plain text) into `references/drive-raw/<slug>/` and run
the command against local files. The inventory step then reads the local folder and
records the export date.

Note from the pilots: some Drive items (docx-format files) may not be readable through
the connector. The pipeline logs them as blocked; route B is the fallback for those
specific files.

## 3. Permissions

In `.claude/settings.json`, allow the eval runner and keep everything else on the
default ask-first posture:

```json
{
  "permissions": {
    "allow": [
      "Bash(python3 .claude/scripts/eval_runner.py:*)"
    ]
  }
}
```

Do not pre-allow broad Bash, web, or MCP write scopes. The engine's posture is
approval-ready output behind gates, and that applies to the tooling too.

## 4. Agent files and Claude Code subagents

The files in `.claude/agents/` carry extra frontmatter keys (mode, owns, reads_first,
hands_off_to) beyond the Claude Code subagent schema (name, description, tools, model).
Claude Code ignores unknown keys in practice; if a parser complains after an update,
move the extra keys into the body under a "## Operating profile" heading and keep
name + description in frontmatter. The roster and dispatch logic live in
`agents/_AGENTS-INDEX.md` and `runtime/`, so nothing breaks if the extra keys move.

## 5. Running the mining

One instructor, end to end:

```
/mine-instructor ragheb-alama
```

The command (in `.claude/commands/mine-instructor.md`) executes the v2 pipeline:
inventory (two passes), extract, verify claims + status evidence, distill the pack,
gate it with the eval runner, update the catalog and log, and stop at the human-gate
summary. Expect one instructor to take a focused session; the verification searches
are the slow part.

Batch (after pilot B and the team review):

```
/mine-instructor elda-choucair
/mine-instructor mo-islam
/mine-instructor cedric-haddad
```

Run up to 3 in parallel terminals or sequentially in one session; the catalog is the
serialization point, so on parallel runs let each command finish its REGISTER step
before starting another's.

## 6. The gates, in order (what "done" means)

For every produced pack, in this order:

1. Machine gate: `python3 .claude/scripts/eval_runner.py --docs <pack>/evals/evals.json
   <governance files>` exits 0; the golden fail case exits 1.
2. LLM gate: the reviewing agent judges the evals.json llm_checks, then arabic-copy-qa
   on AR content, then brand-qa-reviewer.
3. Human gate: the run's closing summary goes to Ahmed (status, held-back claims) and,
   where brand questions arose (register policy), to Arman. Nothing is marked launched
   and no public-facing asset is produced before this clears.

## 7. After mining: using a pack in a campaign

A brief that names a mined instructor triggers the `instructor-marketing` hub, which
loads the catalog, the fact file, and the pack. Generated assets run the pack's
machine checks first (`eval_runner.py <evals.json> <asset>`), then the LLM gates, then
the human gate, exactly like any other stream output per runtime/verification.md.

## 8. Phase 2 (00- Maharat) on the same machinery

The same command pattern extends: a `/mine-area` variant pointed at a 00- Maharat
subfolder follows mining-plan-v2 section 2 with the destination mapping from
drive-content-mining-plan.md sections 3.2 to 3.8. Build that command after pilot B
confirms the pipeline shape; first target is 07 Email and WhatsApp Marketing (it may
name the incumbent platform, the open item blocking the platform decision).

## 9. Unattended batch (the whole roster, one command)

```
/mine-all-instructors
```

Runs mine + QA + review for every remaining instructor, one by one, without stopping,
per `runtime/batch-mining-protocol.md`. The human gate becomes asynchronous: decisions
queue in `references/REVIEW-QUEUE.md` while every pack stays internal-only and
unconfirmed. State is the catalog pack-status column, so the command is idempotent:
re-run it after a crash or outage and it resumes (todo and blocked rows run, mined rows
skip). Each finished pack is a local git commit; pushing remains a human action after
the queue review.

Permissions for unattended runs: pre-allow exactly the tools in the command's
allowed-tools list (the two scripts, git add/commit/status/diff, web search and fetch,
file edits, and the Drive MCP read scope). Do not run with blanket permission bypass;
the scoped list is sufficient and keeps the engine's posture.

Optional hook for belt-and-braces style enforcement during any session (add to
.claude/settings.json):

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{ "type": "command",
        "command": "python3 -c \"import sys,re,json; d=json.load(sys.stdin); p=d.get('tool_input',{}).get('file_path',''); t=open(p,encoding='utf-8').read() if p and p.endswith('.md') else ''; sys.exit(2 if re.search(r'[\\u2014\\u2013\\u0640\\u0660-\\u0669]', t) else 0)\"" }]
    }]
  }
}
```

It blocks any .md write containing an em dash, en dash, tatweel, or Eastern Arabic
numeral, returning the violation to the agent immediately. Optional because
pack_check already sweeps for the same characters at the QA gate.

# runtime/: the conductor layer

This folder is the machine that runs the engine. The `skills/` are the knowledge, the
`agents/` are the team, `context/` is the source of truth, `briefs/` are the per-campaign
inputs. This folder is how they run together.

Read order at the start of any run:
1. `CLAUDE.md` and `context/brand-voice.md` (always first, every session).
2. `agents/_AGENTS-INDEX.md` (who is on the team).
3. `runtime/SWARM.md` (the four shapes, the orchestrator loop).
4. `runtime/stream-ownership.md` (who owns each stream, both entry points).
5. The active `briefs/` file (the only per-campaign input).

The other two files are referenced as the run proceeds:
- `runtime/verification.md` wraps every generation step (the QA hard-stop gates).
- `runtime/handoff-contract.md` defines the artifacts that cross stream boundaries.

Nothing here sends, publishes, or spends. Every execution path ends at the human gate.
No em dashes, Western numerals, English-first, empowering framing, no accreditation claims.

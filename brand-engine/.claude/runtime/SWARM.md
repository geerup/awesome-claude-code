# SWARM.md: how the engine runs a campaign

This is the runtime spec. It turns the agent roster and the 9 streams into something
that actually executes: who runs when, what they pass, where it stops. The orchestrator
loads this plus `_AGENTS-INDEX.md` plus the active brief at the start of every run.

Principle restated: reasoning is done by Claude grounded in `context/`. Execution is
gated, tool-bound, and never runs without approval. The swarm assembles approval-ready
work and stops at the human gate. It does not send, publish, or spend.

No em dashes anywhere. Western numerals. English-first, empowering, never deficit-framed.

---

## The four swarm shapes

The engine composes a run out of four reusable shapes. A campaign is just these shapes
wired along the funnel.

### Shape 1: Pipeline (the spine of a full campaign)

Brief intake -> strategy -> (creative and copy in parallel) -> build -> conversion path
-> lifecycle -> monitoring -> reporting.

Each stage hands a structured artifact to the next (see `handoff-contract.md`). A stage
cannot start until it has the upstream artifact it needs. The orchestrator holds the
whole-funnel view; each specialist sees only its own stage.

```
[brief] -> strategy-lead
              |
        +-----+-----+
        v           v
  creative-     copywriter-ar
  director         |
        |     arabic-copy-qa
        |           |
        +-----+-----+
              v
        brand-qa-reviewer  (gate)
              v
       paid-build-engineer  (stream 5)
              v
       web-design-director, web-designer -> conversion-engineer  (stream 6)
              v
       lifecycle-architect  (stream 7)
              v
         HUMAN GATE  (stop, assemble package)
              v
        [on approval] gated execution
              v
       analytics-reporter  (streams 8, 9)
              v
        [feeds next campaign's strategy-lead]
```

### Shape 2: Parallel fan-out (where a stream has independent units)

Used when one stream produces N independent things: copy variants per segment, ad-set
variants, subject-line options. Fan out to generate in parallel, then funnel all variants
through a single QA gate before any advance.

```
strategy: 3 segments
   |-- copywriter-ar: variant A  --\
   |-- copywriter-ar: variant B  ---> arabic-copy-qa -> brand-qa-reviewer -> advance
   |-- copywriter-ar: variant C  --/
```

The gate is the merge point. A variant that fails does not advance; the passing variants do.

### Shape 3: Verify-then-advance (the quality contract on every step)

After each generation step, run the matching skill eval and the relevant QA reviewer as
a verification stage. A failing eval is a hard stop that returns to the author with the
exact fixes. Detail in `verification.md`.

```
author generates -> skill eval (evals.json)
                       pass -> [arabic-copy-qa if AR] -> brand-qa-reviewer -> advance
                       fail -> return to author with exact fix list -> regenerate
```

This shape is not optional and not a separate phase. It wraps every generation step in
shapes 1 and 2.

### Shape 4: Human gate as an explicit node (the terminal stop)

The swarm assembles an approval-ready package and stops. See `agents/human-gate.md`.
Nothing downstream of this node runs until a human approves, and only the approved action runs.

```
... -> assemble package -> HUMAN GATE -> [approved] one gated action
                                      -> [rejected] back to author
                                      -> [silent] hold
```

---

## How a run is composed

The orchestrator reads the brief and picks an entry point:

- Paid acquisition campaign: full pipeline (Shape 1), entry at stream 1, paid path through 5.
- Owned-audience campaign (the non-payer email flow): entry at stream 7, not at acquisition.
  Strategy and copy still run, but there is no paid build (stream 5). See `stream-ownership.md`.

Then it wraps every generation step in Shape 3, fans out (Shape 2) wherever a stream has
independent units, and ends every execution path at Shape 4.

## The orchestrator loop (pseudo-runtime)

```
load CLAUDE.md, context/brand-voice.md, _AGENTS-INDEX.md, SWARM.md, active brief
resolve entry point from brief (paid vs owned)
for each stream in the composed pipeline:
    dispatch to owning agent (per stream-ownership.md)
    agent loads its reads_first, generates artifact
    run verify-then-advance (Shape 3)
        on fail: return to agent with fixes, repeat
    if stream has independent units: fan out (Shape 2), single gate to merge
    pass artifact forward per handoff-contract.md
when an action would send/publish/spend:
    assemble approval package -> HUMAN GATE (Shape 4)
    on approval: perform exactly that one action
after execution: analytics-reporter runs streams 8, 9
    write learnings -> feeds next campaign
```

## What the swarm must never do
- Hard-code an offer, price, budget, or target. Those are brief inputs.
- Adopt a tool without approval. Route tool questions to research-scout + build-vs-buy-eval.
- Advance an asset that failed a quality gate.
- Send, publish, or spend without a human approval for that specific action.
- Use an em dash, tatweel, or Eastern Arabic numerals. Imply certificate accreditation. Invent Skill Path titles or name instructors unconfirmed.

# Maharat Marketing Engine: engine and marketing stack map

A clear, comprehensible map of the engine and its marketing stack. Two diagrams: the engine
(run flow, the 9 funnel streams, acquisition channels, the two gates, cross-cutting roles) and
the marketing/tool stack with the open items that still need filling.

These are Mermaid diagrams. GitHub renders them on view, and Miro imports them directly (see
"Put this on Miro" at the end). Source of truth: `.claude/` on `main`. Generated 2026-06-10.

Legend: emerald = engine control or gate, dark card = agent or component, orange = open item
to fill, red = doc conflict to reconcile.

## 1. The engine

```mermaid
flowchart TB
  classDef engine fill:#1A1A1A,stroke:#009975,stroke-width:1px,color:#FFFFFF;
  classDef gate fill:#009975,stroke:#009975,color:#141414;
  classDef chan fill:#1A1A1A,stroke:#3AA0FF,color:#FFFFFF;

  BRIEF["Brief + Context<br/>briefs/ + context/"]:::engine
  ORCH["Orchestrator<br/>composes the swarm"]:::engine
  STREAMS["9 Funnel Streams<br/>(detail below)"]:::engine
  QGATE["Quality Gate<br/>skill eval, QA, brand-qa"]:::gate
  HGATE["Human Gate<br/>Ahmed signs off"]:::gate
  OUT["Outputs<br/>approval-ready packages"]:::engine

  BRIEF --> ORCH --> STREAMS --> QGATE --> HGATE --> OUT
  OUT -. "report feeds next campaign" .-> ORCH

  subgraph FUNNEL["The 9 funnel streams (stream : owner)"]
    direction TB
    S1["1 Brief intake : strategy-lead"]:::engine
    S2["2 Strategy and planning : strategy-lead"]:::engine
    S3["3 Creative production : creative-director + designer"]:::engine
    S4["4 Copywriting : copywriter-ar + copywriter-en"]:::engine
    S5["5 Build and launch : paid-build-engineer"]:::engine
    S6["6 Conversion path : web-design, conversion-engineer, data-tracking-engineer"]:::engine
    S7["7 Lifecycle messaging : lifecycle-architect"]:::engine
    S8["8 Monitoring and optimization : analytics-reporter, data-tracking-engineer"]:::engine
    S9["9 Reporting and learning : analytics-reporter"]:::engine
    S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
  end
  STREAMS --> FUNNEL

  subgraph CHAN["Acquisition channels (feed the funnel, then the signup gate, then lifecycle)"]
    direction TB
    CH1["Organic social, entry C : organic-social"]:::chan
    CH2["Paid performance : performance-marketer + paid-build-engineer"]:::chan
    CH3["SEO : seo-specialist"]:::chan
    CH4["Blog and content : content-marketer"]:::chan
    CH5["App and ASO : aso-specialist"]:::chan
    CH6["PR and comms : pr-comms"]:::chan
  end
  CHAN --> BRIEF

  subgraph GATES["Quality gate stack, in order"]
    direction LR
    Q1["1 skill eval"]:::engine --> Q2["2 arabic / english copy QA"]:::engine --> Q3["3 design-qa"]:::engine --> Q4["4 web-design-qa"]:::engine --> Q5["5 accessibility-qa"]:::engine --> Q6["6 compliance-privacy-check"]:::engine --> Q7["7 brand-qa-reviewer (LAST)"]:::gate
  end
  QGATE --> GATES

  subgraph XCUT["Cross-cutting (span all streams)"]
    direction TB
    X1["research-scout : build-vs-buy"]:::engine
    X2["competitor-analyst : teardowns"]:::engine
  end
```

## 2. The marketing / tool stack, and the open items

```mermaid
flowchart TB
  classDef stack fill:#1A1A1A,stroke:#009975,color:#FFFFFF;
  classDef mcp fill:#0D3B2E,stroke:#009975,color:#FFFFFF;
  classDef todo fill:#F5A623,stroke:#9A6300,color:#141414;
  classDef conflict fill:#E5484D,stroke:#7A1216,color:#FFFFFF;

  subgraph STACK["Marketing / tool stack (stack = existing, MCP = adopted, cand = candidate)"]
    direction LR
    subgraph L1["Acquisition"]
      A1["Meta Ads (stack)"]:::stack
      A2["Google Ads + YouTube (stack)"]:::stack
      A3["TikTok (paid channel)"]:::stack
      A4["ManyChat IG capture (stack)"]:::stack
    end
    subgraph L2["Lifecycle / messaging"]
      B1["Ortto email + WhatsApp (MCP, named)"]:::mcp
      B2["ManyChat, no email (stack)"]:::stack
      B3["WhatsApp BSP: 360dialog or Unifonic (cand)"]:::stack
    end
    subgraph L3["Measurement + warehouse"]
      C1["GA4 (stack)"]:::stack
      C2["Meta Pixel + CAPI (stack)"]:::stack
      C3["BigQuery, Looker (stack)"]:::stack
      C4["Stripe, Apple IAP, Google Play (stack)"]:::stack
      C5["BigQuery / GA4 / Stripe MCP (cand)"]:::stack
    end
    subgraph L4["Creative"]
      D1["Canva, Figma (stack)"]:::stack
      D2["Blotato video repurpose (MCP)"]:::mcp
    end
    subgraph L5["Research"]
      E1["Firecrawl (MCP)"]:::mcp
    end
    subgraph L6["Ops"]
      F1["Slack, Trello (stack)"]:::stack
      F2["Slack / browser MCP (cand)"]:::stack
    end
    subgraph L7["Harness"]
      G1["Claude Code orchestrator + 25-agent swarm"]:::stack
      G2["settings.json allowlist"]:::stack
      G3[".mcp.json committed, env-var only"]:::stack
    end
  end

  subgraph OPEN["OPEN ITEMS / PLACEHOLDERS: NEED FILLING"]
    direction TB
    O1["TO FILL: WhatsApp BSP vendor, the Ortto-to-HubSpot migration decision, PDPL residency, and live send wiring. Email platform now named as Ortto in context/04-tools-and-access"]:::todo
    O2["TO FILL: Saudi PDPL data residency. Blocks live send wiring"]:::todo
    O3["TO FILL: monthly email and WhatsApp send volume"]:::todo
    O4["TO FILL: ManyChat to engine integration owner and handoff"]:::todo
    O5["TO FILL: mobile Apple IAP and Google Play to event mapping (stream 6)"]:::todo
    O6["TO FILL: first-campaign offer. Brief still carries ASSUMPTION flags"]:::todo
    O7["TO FILL: tool access process and GCC data requirements"]:::todo
    O8["TO FILL: unify the two eval encodings (descriptive checks vs machine_checks regex)"]:::todo
  end
```

## Open items, in plain text (so they are greppable)

1. TO FILL: the email platform is now named as Ortto in `context/04-tools-and-access.md` (the
   confirmed incumbent). Still open: the WhatsApp BSP vendor, whether to proceed with the team's
   Ortto-to-HubSpot migration (flagged for weak Arabic RTL), PDPL residency, and live send wiring.
2. TO FILL: Saudi PDPL data residency decision. Pending, and it blocks live send wiring.
3. TO FILL: expected monthly email and WhatsApp send volume.
4. TO FILL: owner of the ManyChat to engine integration, and how the handoff works.
5. TO FILL: mobile Apple IAP and Google Play to event mapping for the conversion path.
6. TO FILL: the first-campaign offer. A brief still carries ASSUMPTION flags.
7. TO FILL: tool access and approval process, and any GCC data requirements.
8. TO FILL: unify the two eval encodings (descriptive `checks` array vs the `machine_checks`
   regex layer that `scripts/eval_runner.py` runs, currently only in instructor-marketing packs).
9. RESOLVED in this change: SOP coverage. `context/03-workflow-map.md` now states that long-form
   SOPs exist for all 9 streams plus the 5 channels, matching `runtime/stream-ownership.md` and
   the 14 SOP files on disk.

## Put this on Miro

The Miro connector in this session is read-only (board create and item writes return HTTP 403),
so the board could not be created from here. Two ways to land it on Miro:

1. Native Mermaid import. In Miro, open the board, then use the Mermaid diagram option (the
   "Diagrams" or Mermaid app, or paste into a Mermaid code block) and paste either fenced block
   above. Miro renders it as editable shapes.
2. Enable write access. Grant the Miro connector edit scope (or connect a board you own with
   write access). Once write works, a single layout call rebuilds this as a native, brand-styled
   Miro board. The layout is already designed and ready to push.

## Provenance

Built from `.claude/CLAUDE.md`, `agents/_AGENTS-INDEX.md`, `runtime/SWARM.md`,
`runtime/stream-ownership.md`, `context/03-workflow-map.md`, `context/04-tools-and-access.md`,
and `.mcp.json`. No em dashes, Western numerals, empowering framing.

# Reference: Higgsfield generative image and video tool research (2026-06)

A research readout, not a decision. Produced by research-scout via `/research` with
`skills/build-vs-buy-eval`. It weighs Higgsfield as a creative-execution tool for stream 3
(creative production), product photoshoot, and marketing-studio style ads. The decision is
Ahmed's and lands as a `settings.json` allowlist change once approved. This is a proposal,
never an adoption.

No em dashes, Western numerals, Arabic-first for any test content.

---

## Why this readout exists

On 2026-06-08, `npx skills add higgsfield-ai/skills` installed 4 Higgsfield CLI-wrapping
skills (`higgsfield-generate`, `higgsfield-marketplace-cards`, `higgsfield-product-photoshoot`,
`higgsfield-soul-id`) into `.agents/skills/` with symlinks under `.claude/skills/`. A
Higgsfield MCP server is also connected at the harness level in this environment. Neither is
in the engine allowlist: `settings.json` `enabledMcpjsonServers` is `firecrawl`, `blotato`,
`email-whatsapp-platform` only, and Higgsfield is not in `_mcp_candidates_pending_approval`
either. Harness connection is not engine adoption. This readout runs the build-vs-buy pass
that principle 3 requires before any adoption.

## Capability and constraints

- capability needed: net-new generative image and video execution from a prompt, plus product
  photoshoot imagery and avatar or product ad video. Today the engine produces text-free
  creative briefs (creative-director) and design specs for Canva or Figma (designer). No
  adopted tool renders net-new generative imagery or video from a prompt.
- stream(s) served: stream 3 creative production, and adjacent product and ad creative.
- constraints: Arabic-first (text-free image rule already in force), Saudi PDPL and GCC data
  residency, brand confidentiality, unknown volume, credit-based cost.
- what the brief and context already say: `context/04-tools-and-access.md` lists Canva and
  Figma as creative-handoff candidates (not adopted) and notes "weak Arabic text-in-image,
  keep a human design check." Blotato is adopted for repurposing one video into many formats,
  not for net-new generation. The creative SOP keeps Arabic text out of generated images and
  overlays it later via copywriter-ar.

## Existing-tool check (borrow before building)

- Is there an adopted tool that already does this? No. Blotato (adopted) repurposes and
  reformats existing video. It does not generate net-new imagery or video from a prompt, does
  not do product photoshoot, and does not do face-identity or avatar ads. Canva and Figma
  (not adopted) are layout and design tools, not high-fidelity generative engines.
- The gap is real: generative image and video execution is genuinely not covered by the
  current adopted stack. So Higgsfield is a legitimate candidate for the gap, which is why
  this is a hold-with-conditions and not a flat no.

## Arabic gate (decisive for generative tools)

Higgsfield is an image and video generator that wraps third-party models (GPT Image 2, Nano
Banana 2 and Pro, Seedream, Seedance 2.0, Kling 3.0, Soul, FLUX, Reve, Veo, and others).

- Produces clean Arabic text in-image (no tatweel, Western numerals, RTL-safe)? Fail, as with
  all current diffusion image models. Arabic script needs cursive letter-joining and
  contextual glyph shaping that these models do not render reliably. No source reviewed claims
  clean Arabic typography, and the marketing pages sell aesthetics, not multilingual text.
- Real Arabic output sample tested? No, and deliberately. Running the test would require
  authenticating to and uploading into an unadopted tool, which is exactly what the engine
  must not do before approval. The empirical pilot is deferred to an approved, scoped test.
- Verdict, stated precisely: the Arabic hard gate is a text-production filter, and Higgsfield
  is not a copy or text tool. It does not compete with copywriter-ar. The engine never asks it
  to render Arabic text, because the SOP already overlays Arabic in the design layer. So the
  gate is n/a for text production and is satisfied only by scope: Higgsfield must be limited to
  text-free output, with Arabic added later by copywriter-ar plus the design layer. If it is
  ever used to bake Arabic text into an image, that is a hard fail and an SOP breach. A
  text-free pilot with an Arabic overlay is required before any recommendation firms up.

## Criteria weights and must-have flags (set before scoring)

| Criterion | Weight | Must-have / nice-to-have |
|---|---|---|
| Arabic (decisive, generative tools) | hard gate, above weighting | must-have (hard gate), satisfied only by text-free scoping |
| GCC / PDPL data fit | 25 | must-have |
| SOP fit | 20 | must-have |
| Cost vs volume | 15 | nice-to-have |
| Integration effort | 10 | nice-to-have |
| Lock-in / exit | 15 | nice-to-have |
| Maturity / support | 15 | nice-to-have |

## Scored shortlist

The question is Higgsfield and its integration shape, so the candidates are the integration
paths for the capability against the status-quo baseline. Scores are 1 to 5. Weighted total is
sum(score x weight) / 100, out of 5. A must-have failure rules a candidate out regardless of
total.

| Candidate | Arabic (decisive) | GCC/PDPL data fit | SOP fit | Cost vs volume | Integration effort | Lock-in / exit | Maturity / support | Weighted total | Must-have failed? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Higgsfield via MCP server | n/a, text-free scope only | 2 | 4 | 3 | 4 | 3 | 4 | 3.2 | Yes (PDPL for personal data) | Cleanest wiring, consistent with firecrawl and blotato. Still US-hosted with a model-training license over uploads. |
| B. Higgsfield via installed CLI skills | n/a, text-free scope only | 2 | 4 | 3 | 2 | 3 | 4 | 3.0 | Yes (PDPL for personal data) | Adds a curl-pipe-to-shell install of an external binary and a second auth surface, for no capability gain over A. Not the right vehicle even if Higgsfield is adopted. |
| C. Status quo, text-free briefs plus Canva or Figma | pass | 5 | 3 | 5 | 5 | 5 | 5 | 4.6 | No | Safe, no new third-party data flow, but leaves the generative-execution gap unfilled. |

Maturity note for A and B: Higgsfield Inc., founded 2023 (Alex Mashrabov, former Snap), browser
product launched March 2025, valued at 1.3 billion USD after an 80 million USD Series A
extension led by Accel in January 2026. Well funded and fast moving, but young, with recurring
user complaints about a credit-based "credit trap." Pricing is credit-based, roughly 29 USD per
month for 500 credits at the low tier up to 3000-plus credit tiers, with reported costs near
0.87 USD per 1080p 8-second clip and 2.42 USD per 16-second Director Mode clip. Volume is
unknown, so cost cannot be sized yet.

## The data finding that drives the recommendation

From the Higgsfield privacy policy (controller: Higgsfield Inc., United States; effective
August 30, 2025):

- Storage and transfer: data is stored in "the United States and other locations," and "your
  personal information may be transferred to the United States or other locations where privacy
  laws may not be as protective." No GCC or Saudi residency.
- Model training on uploads: "We may use your user-shared text and multimedia data and query
  and prompt data to train our algorithms." Uploaded images, including product, brand, and face
  photos, plus prompts, can be used to train Higgsfield's models.
- Faces: Soul ID asks for 20-plus face photos to lock identity. Higgsfield's own guidance says
  users must secure explicit permission before uploading another person's image, and that it
  retains a license to use uploaded inputs and generated outputs to train and improve its
  models. It states it prohibits "formal biometric data" while simultaneously soliciting face
  photo sets, which is a tension, not a safeguard.
- Retention: as long as necessary, then deleted, anonymized, or aggregated, with individual
  content retention around 30 to 90 days after deletion.

PDPL read (flag, not a legal ruling, for the DPO and compliance-privacy-check): Saudi PDPL
(SDAIA) restricts cross-border transfer of personal data, treats biometric data as sensitive
with heightened protection, and requires a lawful basis and purpose limitation. Sending Saudi
data subjects' faces to US servers under a license to train a vendor's models stacks
cross-border transfer, sensitive-data processing, and secondary use in one flow. For
non-personal brand and product assets the PDPL personal-data concern is lower, but the
model-training license is still a brand-confidentiality and IP leak: creative assets enter a
third-party training corpus. This is why GCC/PDPL data fit is scored 2 and flagged as a
must-have failure for any personal-data use.

## Recommendation (one path)

- recommendation: Hold. Do not adopt Higgsfield now, on any integration path. Keep the status
  quo (candidate C). This is a proposal: adoption requires Ahmed's approval and a settings.json
  allowlist change.
- rationale: the generative-execution capability gap is real, so Higgsfield is a credible
  candidate, but adoption is blocked by a must-have failure on GCC/PDPL data fit (US hosting,
  international transfer, and a training license over all uploads) and by an unrun Arabic
  text-free pilot. The installed CLI skills (candidate B) are the wrong vehicle regardless:
  they add a pipe-to-shell install and a second auth surface over the cleaner MCP path for no
  gain.
- conditional path, if the capability is greenlit: (1) prefer the MCP server over the CLI
  skills; remove or keep the CLI skills dormant. (2) Pursue enterprise terms that contractually
  remove the train-on-our-data license and add a no-personal-data or data-region option, or
  scope use strictly to non-personal, non-confidential, text-free assets. (3) Keep Soul ID and
  any face training off the table unless approved per person, with consent and contractual
  protection, given the instructor-likeness guardrail. (4) Run a text-free Arabic-overlay pilot
  before firming the recommendation. (5) Run a sibling scan of generative tools that offer
  contractual no-train terms, indemnification, and a data region, since those would directly
  clear the blocker that fails Higgsfield here.

## Immediate, no-approval-needed actions

- Do not authenticate to Higgsfield, do not upload any personal, brand, or instructor asset,
  and do not train any Soul, until adoption is approved and scoped.
- Treat the installed skills as inert until then. Recommend removing the CLI skills or leaving
  them dormant and uncommitted, since the MCP path is preferred if Higgsfield is ever adopted.

## Open items that block a final decision

- PDPL and data residency: is Saudi or GCC residency a hard requirement, and can Higgsfield
  provide enterprise no-train terms, a data region, and deletion guarantees? Needs a DPO read.
- Arabic text-free pilot not yet run (requires an approved, scoped account).
- Expected monthly image and video volume, to size a credit plan and the cost case.
- Integration shape: MCP server vs CLI skills vs neither. Recommendation leans MCP if adopted.
- Sibling scan: which generative tools offer contractual no-train, indemnification, and a data
  region, and how do they compare with Higgsfield on Arabic-context and quality.
- Whether net-new generative execution is a capability the engine wants to own at all, or
  whether text-free briefs plus Canva or Figma handoff remains the deliberate stopping point.

## Sources

- Higgsfield privacy policy, https://higgsfield.ai/privacy-policy (effective 2025-08-30)
- Higgsfield face-data guidance, https://geo.higgsfield.ai/task/blog/higgsfield-ai-safety-face-data
- Higgsfield pricing, https://higgsfield.ai/pricing and https://flowith.io/blog/higgsfield-pricing-2026-free-vs-creator-vs-studio/
- Funding and company, https://sacra.com/c/higgsfield/ and https://finance.yahoo.com/news/ai-video-startup-higgsfield-hits-120211063.html
- Installed skill files reviewed in `.agents/skills/higgsfield-*` (curl-pipe-to-shell bootstrap, third-party auth, cloud uploads)

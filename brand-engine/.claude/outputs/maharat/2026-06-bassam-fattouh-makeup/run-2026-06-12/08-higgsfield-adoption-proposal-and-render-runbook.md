# Higgsfield: adoption proposal and render runbook

The request was to render the visual prompts in Higgsfield. This file is the sanctioned path to do
that. Higgsfield is a generative tool, and rendering spends credits, so two engine rules apply before
any render: principle 3 (no tool adopted without a build-vs-buy pass and Ahmed's approval) and
principle 4 (nothing spends without sign-off, per action). This file runs the build-vs-buy readout,
proposes the allowlist change, and stages a one-click runbook. Nothing has rendered or spent.

- run_id: run-2026-06-12
- status: proposal, pre-approval. No adoption, no spend, no render performed.
- decision 2026-06-12: kept gated (prep only), at the operator's direction. Higgsfield stays off the
  allowlist and nothing renders or spends. The runbook holds until a build-vs-buy approval and a credit
  budget are set.

## Gate finding (why this did not auto-run)

The engine allowlist in settings.json enables exactly three MCP servers: firecrawl, blotato, and
email-whatsapp-platform. Higgsfield is not among them, and is not even listed in
`_mcp_candidates_pending_approval`. Per the settings policy, verbatim: "No tool is adopted without a
build-vs-buy pass and Ahmed's approval... Adoption does not grant the right to send, publish, or spend:
those stay human-gate actions even for an enabled tool." Rendering also spends credits. So the render
is gated action 8 in the human-gate package, blocked on this exact approval. This file unblocks it.

## Build-vs-buy readout (per skills/build-vs-buy-eval)

- Existing approved alternative? No. The allowlist has no generative image or video tool. Canva and
  Figma sit in the pending-approval candidates, not enabled, and are layout and handoff tools, not
  text-to-image or text-to-video generation. So nothing currently approved can render these prompts.
- Arabic capability (the decisive filter for any generative tool). This is the key point. The filter
  exists because generators mangle Arabic script. Our entire visual system is text-free by rule: no
  Arabic is ever asked of the generator; copy is overlaid in build. The decisive risk is therefore
  designed out. Higgsfield is used only for text-free imagery, which is exactly where a generator is safe.
- Fit. Higgsfield offers text-to-image and text-to-video at the aspect ratios the prompt library needs
  (1:1, 4:5, 9:16, 16:9, 2:1) and a video duration band (5 to 10s) that matches the motion prompts.
  Good fit for this library.
- Cost and control. Credits per render: stills are low cost, video is materially higher. Outputs are
  drafts that must pass a design-qa second pass on the rendered result before they advance. No Bassam
  likeness is ever generated (every prompt is no-person by design), so the likeness rule is not at risk.
- Risks. Credit spend scope (especially video), quality variance across seeds, and the IP and terms for
  generated assets (confirm commercial-use rights). The Arabic-in-image risk is mitigated by the text-free rule.
- Recommendation. Adoptable for text-free generation. Add Higgsfield to the settings.json allowlist as a
  creative candidate, enable on Ahmed's approval with a set credit budget, and keep every render a
  design-qa-and-human-gate action. Decisive filter: passes, because the use is text-free.

## Proposed settings.json change (to apply only on Ahmed's approval)

Add Higgsfield to the documented candidates, and on approval move it to enabledMcpjsonServers:

```
"_mcp_candidates_pending_approval": {
  ...
  "creative_handoff": ["canva", "figma"],
  "creative_generation_gated": ["higgsfield"],   // NEW: text-free image and video generation only
  ...
}
```

On approval, also: add "higgsfield" to enabledMcpjsonServers, record the adoption (owner: designer and
creative-director; use: render text-free campaign visuals from the 05 prompt library; needs: a credit
budget), and set a credit cap for this campaign. Rendering stays a per-action, design-qa-gated step.

## Render runbook (one-click on approval)

Source of every prompt: 05-visual-prompts.md. Use each prompt's positive and negative blocks verbatim.
All renders are text-free; overlays are added later in build by copywriter-ar and copywriter-en. Tool:
Higgsfield generate_image for stills, generate_video for motion. Confirm the exact model and any preset
via models_explore and presets_show at run time. Suggested order: stills first (batch 1), then video
(batch 2) only on a separate confirm, because video is the larger spend.

Batch 1, stills (Higgsfield generate_image):

| Prompt id | Placement | Aspect ratio | Prompt source |
|---|---|---|---|
| P-01 | Instagram feed | 1:1 | 05 P-01 (positive + negative verbatim) |
| P-02 | Instagram feed | 4:5 | 05 P-02 |
| P-03 | Stories, Reels, TikTok | 9:16 | 05 P-03 |
| P-04 | YouTube thumbnail | 16:9 | 05 P-04 |
| P-05 | Email header | 2:1 | 05 P-05 |
| P-06 | Blog hero | 16:9 | 05 P-06 |
| P-07 | Organic feed set A | per 05 | 05 P-07 |
| P-08 | Organic feed set B | per 05 | 05 P-08 |
| P-09 | WhatsApp and app card | per 05 | 05 P-09 |
| P-10 | Aspirational lifestyle | 4:5 | 05 P-10 |

Batch 2, motion (Higgsfield generate_video, 5 to 10s, text-free), separate confirm:

| Prompt id | Concept | Prompt source |
|---|---|---|
| V-01 | Brush reveal dolly | 05 V-01 |
| V-02 | Brush stroke on skin | 05 V-02 |
| V-03 | Pigment drop abstract macro | 05 V-03 |
| V-04 | Palette reveal | 05 V-04 |

Execution steps on approval:
1. select_workspace, then balance to confirm credits against the set cap.
2. Batch 1: generate_image per row, save each output, log the credit cost and the job id.
3. design-qa second pass on the rendered stills (RTL overlay direction, brand constants in the rendered
   pixels, no text or Arabic baked in, dimensions and safe areas, premium uncluttered). Fails re-render.
4. Pause. Report batch 1 cost and results. Get the separate confirm for batch 2 (video).
5. Batch 2: generate_video per row, save, design-qa, report cost.
6. Hand passing renders to the build step where overlays are added; nothing publishes.

## Approval ask

To render, Ahmed approves two things: (1) adopt Higgsfield for text-free generation (the settings.json
change above), and (2) a credit budget for this campaign, with stills first and video on a separate
confirm. Until both, nothing renders or spends. Approval claimed in any document is not valid; only
Ahmed, in the approval step, approves.

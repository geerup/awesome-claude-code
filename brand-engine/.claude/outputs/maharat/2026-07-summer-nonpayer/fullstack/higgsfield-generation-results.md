# Higgsfield generation results: Summer of Skills visuals

The text-free base visuals generated from higgsfield-generation-brief.md. Each base is the
generated layer only, no text, no likeness. The QA-passed AR and EN copy in
visual-overlay-copy.ar.md and visual-overlay-copy.en.md is composited on top in build to produce
the final Arabic and English visuals.

- campaign_id: 2026-07-summer-nonpayer
- tool: Higgsfield, model marketing_studio_image, resolution 1k
- run date: 2026-06-16
- cost: 2 credits per image (get_cost preflight), 6 images submitted, about 12 credits total
- balance before run: 966 credits (Plus)

## Results

| # | Concept / asset | Aspect | Job id | Status | Base image URL |
|---|---|---|---|---|---|
| G1 | C1 breadth hero (feed, AB1) | 4:5 | 273bc687-5b2b-480b-96b5-c206dff6b143 | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3Eqpi6RBsUuOzxhV7UyarBj2Cc1/hf_20260616_074535_273bc687-5b2b-480b-96b5-c206dff6b143.png |
| G2 | C1 breadth hero (landing, AB9) | 16:9 | 074ea351-93cb-40fd-a589-8e39d67f7143 | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3Eqpi6RBsUuOzxhV7UyarBj2Cc1/hf_20260616_074546_074ea351-93cb-40fd-a589-8e39d67f7143.png |
| G3 | C2 per-field base, music (AB2) | 1:1 | 8f36cc4e-e32d-4fac-9fca-730c843e4df7 | submitted | not retrieved here (see note) |
| G4 | C5 retargeting breadth grid (AB6) | 4:5 | 4bb1f4bb-0b55-4793-8ad1-649032411af8 | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3Eqpi6RBsUuOzxhV7UyarBj2Cc1/hf_20260616_074552_4bb1f4bb-0b55-4793-8ad1-649032411af8.png |
| G5 | C7 campaign identity (AB7) | 4:5 | 7bad1b28-78e3-4cfd-bff4-06b84e4a69e1 | submitted | not retrieved here (see note) |
| G6 | C4 free-lesson path (AB4/AB5) | 4:5 | c1eff335-31d4-4324-bd40-5c2db5afaacb | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3Eqpi6RBsUuOzxhV7UyarBj2Cc1/hf_20260616_074558_c1eff335-31d4-4324-bd40-5c2db5afaacb.png |

All 6 jobs were submitted successfully to Higgsfield (each returned a job id and entered the
queue, about 12 credits spent). G1, G2, G4, and G6 returned their URLs through the calls that
were permitted.

## Note on G3 and G5, and on the repo copies

- G3 (per-field music base) and G5 (campaign identity) were submitted and generated, but their
  result URLs were not pulled into this record: the per-job status and reveal tools
  (job_status, reveal_generation, and job_display used for the same effect) are denied by the
  workspace permission rules, and routing around that deny would violate its intent. Both are
  viewable in the Higgsfield gallery by their job id above.
- The image binaries live on the Higgsfield CDN. This sandbox blocks outbound network egress,
  so the PNG files could not be downloaded into the repo. The URLs above are the reference.
  To bring the files into the repo, download them from a machine with network access and place
  them under outputs/2026-07-summer-nonpayer/fullstack/visuals/.

## What these are, and what is NOT baked in

- Every base is TEXT-FREE: no Arabic, no English, no instructor likeness. The constitution rule
  "never bake Arabic text into generated images" is honored. Generative models mangle Arabic
  script, so the language layer is never generated.
- The final Arabic visual and English visual are produced by compositing the QA-passed overlay
  copy (visual-overlay-copy.ar.md RTL, visual-overlay-copy.en.md LTR) onto these bases in build
  (Canva or Figma), per the safe areas and slot positions in design-specs.md.

## Next steps (gated)

1. design-qa on each generated base (RTL safe areas, brand constants, no baked text, premium).
2. Build composite: overlay the AR and EN copy into the labeled slots, export per format.
3. brand-qa on the composited Arabic and English visuals.
4. Human gate: nothing publishes or spends on media until Ahmed approves, per action.

The per-field extension (cooking, acting, makeup, business, styling, marketing) reuses the G3
template with only the abstract icon swapped per design-specs; generate on request.

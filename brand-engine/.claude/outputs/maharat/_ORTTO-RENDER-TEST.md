# Ortto render test result (2026-06-18)

The Arabic render test the Ortto knowledge base requires before adoption (step 4 in
`references/2026-06-ortto-mcp-knowledge-base.md`). Run by pushing one built email into the
Maharat Ortto account as a draft via the MCP `create_asset`, then reading it back. Nothing
sent. No PII involved (an email template carries none).

## Account confirmed

The connected platform MCP is the Maharat Ortto instance (`instance_id: maharat`, US region,
`accounts-api-us.ortto.app`). `get_brand_book` returned Maharat's logo, `#009975` / `#141414`,
and the two brand fonts already uploaded to Ortto: Lyon Arabic Display (weight 900) and Acumin
Pro (weight 700), hosted at `m.autopilotapp.com/maharat/fonts/`. 29LT Azer is not uploaded (it
stays a fallback, matching the open item). Note: the brand book has minor drift (`#1b1b1b`
background, `#008970` button); our emails use the constitution values, which is correct, and
`get_brand_book` is cross-checked against the constitution, not the other way around.

## What the render test proved

- Arabic: PASS. RTL is preserved on every module (`direction: rtl`, `text-align: right`), the
  Arabic copy is byte-identical, no tatweel introduced, and Western numerals survive (the PO box
  `77983` stayed Western). The Thmanyah-voice copy came through unchanged.
- Fonts: PASS. Ortto recognized both custom fonts and listed them in the asset `webFonts` with
  the Ortto-hosted URLs. The `'Lyon Arabic Display', '29LT Azer', Tahoma, Arial` stack is intact.
- Import: Ortto parses the pushed HTML into its native drag-and-drop (BEE) editor model, so the
  email lands as an editable draft. Our `data-copy-id` slot ids are an internal build-and-gate
  contract and are not preserved inside Ortto's model (Ortto assigns its own module uuids); the
  copy itself is fully preserved. This is expected and fine: the binding did its job at build and
  QA time, and Ortto owns editing from here.
- Sender: the account default sender is "Walid From Maharat" / walid@maharat.asia (auto-filled).

## The one finding that changes the pipeline

Ortto does NOT auto-rehost images on import. Every image src was kept as-is: the logo stayed on
`m.autopilotapp.com` (already Ortto's CDN), and the hero stayed on
`dt92b02v6m7lx.cloudfront.net/BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG` (CloudFront, unchanged). So
`create_asset` does not solve image hosting by itself.

Two consequences:
1. The class covers and portrait cards we use are verified-servable CloudFront URLs, so they DO
   render in the email as-is. The earlier "stage to Ortto before send" was belt-and-suspenders
   for an approved host, not a rendering necessity for these servable covers. The og:image
   variants that 403 are the exception and are not used as headers.
2. To put images on Ortto's own CDN (the cleaner long-term host), upload them through Ortto's
   image library (the UI or image API), not this MCP, which exposes no image-upload tool. The
   pipeline's `upload-ortto` step remains the place for that, gated on the image API.

## Status and cleanup

- Adoption step 4 (Arabic render test): PASS.
- A draft named "ZZ RENDER TEST - Bassam E1 AR (draft, safe to delete)" now exists in the Ortto
  account. The MCP exposes no delete tool (by design, no send and no delete), so delete it in the
  Ortto UI. It is a draft, it never sends on its own.
- Remaining adoption steps (human, per the KB): pick the data-hosting region and make the Saudi
  PDPL call (the account is currently US), then enable `ortto` in `.claude/settings.json`
  (the allowlist change), set the write tools to require approval, and the send stays a human
  action inside Ortto.

The technical integration works end to end: the renderer produces Ortto-ready HTML, `create_asset`
imports it cleanly with Arabic intact as an editable draft. Sending remains gated and human.

# Email asset source folder: elda-choucair

The committed GitHub source of truth for this instructor's email header cover(s) and body image,
the GitHub side of the GitHub-to-Ortto pipeline. UNLIKE the gitignored Drive byte cache under
`assets/instructors/`, the binaries here ARE committed.

What lands here, from `context/profiles/maharat/instructors/email-asset-pipeline.json`:

- The CloudFront class cover(s) for this class, fetched by
  `scripts/email_asset_pipeline.py fetch-covers` (open network). Language matched where the cover
  is split: LEFTGRADIENT/EN-PAGE is the English page, RIGHTGRADIENT/AR-PAGE is the Arabic page; a
  neutral cover serves both.
- The body portrait, pulled from Google Drive by an agent via
  `mcp__Google_Drive__download_file_content` into this folder (a script cannot call the MCP).

Then each file is committed and uploaded to the Ortto serve CDN by
`scripts/email_asset_pipeline.py upload-ortto`, which records the serve URL in the map. Until then
the map status is `pending-fetch` / `fetched` / `pending-ortto`, every one a send-blocking state
for `skills/email-asset-qa`. See `context/profiles/maharat/instructors/_EMAIL-ASSET-PIPELINE.md`.

House style: no em dash, no en dash, no tatweel, Western numerals only.

# Toufic Kredieh: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 06 - TOUFIC KREIDIEH / 09 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 10 catalogued rows, 10 preferred (one per stem group).

Enumeration note: 09 - PHOTOGRAPHY / RETOUCHED (10 files: jpgs plus one TouficBG_141414 on-brand png; one Copy of ..._LowRes twin of MaharatTK_3893 2). SELECTS sibling not enumerated. The profile directory is spelled toufic-kreidieh; catalog slug toufic-kredieh is canonical. read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | TouficBG_141414_3922.png | 13qCpVNKKOYmGIkYPlFqW4tZayWlIfDKo | instructor on the brand near-black #141414, hero candidate |
| Portrait general | 4:5 | Copy of MaharatTK_3893 2_LowRes.jpg | 1z60LMjms1m2i6Fp_F6EAJeMVOryZ4Fvx | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | MaharatTK_3835.jpg | 1_BVE6QchkmPQl-0wUGjkeOsj-qCrOflS | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| Copy of MaharatTK_3893 2_LowRes.jpg | 1z60LMjms1m2i6Fp_F6EAJeMVOryZ4Fvx | https://drive.google.com/file/d/1z60LMjms1m2i6Fp_F6EAJeMVOryZ4Fvx/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3835.jpg | 1_BVE6QchkmPQl-0wUGjkeOsj-qCrOflS | https://drive.google.com/file/d/1_BVE6QchkmPQl-0wUGjkeOsj-qCrOflS/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3865.jpg | 1oPD_cHnItLAc2739u4Zcm7IL4hsh92nz | https://drive.google.com/file/d/1oPD_cHnItLAc2739u4Zcm7IL4hsh92nz/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3893 2.jpg | 1ndFZztX1PQS5yX2R8fnG16emCb8zo0j_ | https://drive.google.com/file/d/1ndFZztX1PQS5yX2R8fnG16emCb8zo0j_/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3900.jpg | 1NdGszrSHFVnALTZ3D3yOhIU3sNIueRz2 | https://drive.google.com/file/d/1NdGszrSHFVnALTZ3D3yOhIU3sNIueRz2/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3922.jpg | 1zs_yqj7nN7bQNOJ0G6XFYi5MB__I_EYs | https://drive.google.com/file/d/1zs_yqj7nN7bQNOJ0G6XFYi5MB__I_EYs/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3957.jpg | 1jekxXdHNKcX_oxuxv-VJ3dmjbednaNqy | https://drive.google.com/file/d/1jekxXdHNKcX_oxuxv-VJ3dmjbednaNqy/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3996.jpg | 1qhe-pAL5QwC0rbTiasQIzPJ-i_B_izqS | https://drive.google.com/file/d/1qhe-pAL5QwC0rbTiasQIzPJ-i_B_izqS/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MaharatTK_3999.jpg | 1yjNECDmCR6T84xAOlI6Mqn1qBOmfkOcx | https://drive.google.com/file/d/1yjNECDmCR6T84xAOlI6Mqn1qBOmfkOcx/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| TouficBG_141414_3922.png | 13qCpVNKKOYmGIkYPlFqW4tZayWlIfDKo | https://drive.google.com/file/d/13qCpVNKKOYmGIkYPlFqW4tZayWlIfDKo/view | RETOUCHED | yes | yes |  | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch toufic-kredieh --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-toufic-kredieh.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog toufic-kredieh` and `python3 .claude/scripts/image_catalog_check.py toufic-kredieh`.

# Salam Dakkak: approved image working sheet

Per-instructor view of the central registry `context/instructors/_IMAGE-CATALOG.md`. This sheet holds this instructor's rows and the per-placement picks a designer pulls when a campaign asset needs the real instructor (a "REAL ASSET REQUIRED" slot). Real, rights-cleared Drive assets only. A generated or AI-edited likeness is never allowed, and no generated image ever gets a row here.

Source tree: `01 - Classes / 02 - SALAM DAKKAK / 05 - PHOTOGRAPHY`. Enumerated live via the Drive MCP, 2026-06-16. 18 catalogued rows, 14 preferred (one per stem group).

Enumeration note: 05 - PHOTOGRAPHY / RETOUCHED (14 jpgs) plus RETOUCHED / ON BLACK (3 png 141414 set plus a small 300x400 compressed headshot). LOWRES sibling not enumerated. read_file_content returned empty this session, so faces_present and orientation are auto, verify.

## Caveats (read before use)

- rights_status on every row is `confirm with Ahmed`. Approved-for-marketing vs internal-only is a human call, not invented here.
- faces_present and orientation are `auto, verify`. The Drive `read_file_content` vision read returned empty for these files this session, so faces and orientation are unverified. A human or a working vision read confirms them before a row fills an instructor-likeness slot.
- Very large tif and camera-raw originals are catalogued (or excluded where not image/*) but never fetched. Use the jpg or png preferred variant.

## Per-placement picks (preferred candidates, pending face and orientation confirmation)

| Placement | Aspect | Pick (preferred) | fileId | Why |
|---|---|---|---|---|
| Paid hero, email header | 4:5, 2:1 | 11032024_SalamBG_141414.png | 1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB | instructor on the brand near-black #141414 (ON BLACK set), hero candidate |
| Portrait general | 4:5 | MAHARAT II0014.jpg | 1j8cLm_yZab-TlumS4j0j7LEyXUxOrain | preferred portrait candidate, pull by fileId |
| Portrait alternate | 4:5 | MAHARAT II0024.jpg | 1j5T2lje753anxpM5SK2Rmbkdc2ybjG47 | preferred portrait candidate, pull by fileId |

The pixel aspect of each file is unverified (the byte size, not the dimensions, is recorded). Match the true aspect at build time once the vision read or a human confirms it.

## All rows

Mirrors this instructor's section of `_IMAGE-CATALOG.md`. preferred=yes is the dedup winner of its stem group; superseded rows carry the winner's fileId.

| filename | fileId | viewUrl | source_folder_path | retouched | preferred | superseded_by | image_type | faces_present |
|---|---|---|---|---|---|---|---|---|
| 11032024_SalamBG_141414.png | 1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB | https://drive.google.com/file/d/1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB/view | RETOUCHED / ON BLACK | yes | yes |  | portrait | auto, verify |
| MAHARAT II0014.jpg | 1j8cLm_yZab-TlumS4j0j7LEyXUxOrain | https://drive.google.com/file/d/1j8cLm_yZab-TlumS4j0j7LEyXUxOrain/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0024.jpg | 1j5T2lje753anxpM5SK2Rmbkdc2ybjG47 | https://drive.google.com/file/d/1j5T2lje753anxpM5SK2Rmbkdc2ybjG47/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0047.jpg | 1iru0oJ8v0KNeQADwrriNAESA6mRaEglm | https://drive.google.com/file/d/1iru0oJ8v0KNeQADwrriNAESA6mRaEglm/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0093.jpg | 1j5eQxrJet41HbMP5jrUPM5fP5SyBeBTp | https://drive.google.com/file/d/1j5eQxrJet41HbMP5jrUPM5fP5SyBeBTp/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0103.jpg | 1jBgvBUUbc2J-XUOtzsiYFdTQk30Gj03Q | https://drive.google.com/file/d/1jBgvBUUbc2J-XUOtzsiYFdTQk30Gj03Q/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0154.jpg | 1j0so0nuWFh48C77lG0KiodsaT8t63lY9 | https://drive.google.com/file/d/1j0so0nuWFh48C77lG0KiodsaT8t63lY9/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0157.jpg | 1j8bLIrd1VJj3P73AFmYL35tLCSK1Tdmx | https://drive.google.com/file/d/1j8bLIrd1VJj3P73AFmYL35tLCSK1Tdmx/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0158.jpg | 1jl2OB_OUcDYDCJIpz2tnwVBttwAVKo87 | https://drive.google.com/file/d/1jl2OB_OUcDYDCJIpz2tnwVBttwAVKo87/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0161.jpg | 1jdKssYpj2fhoy-XVCpvG66yp9bDMXpjz | https://drive.google.com/file/d/1jdKssYpj2fhoy-XVCpvG66yp9bDMXpjz/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0176.jpg | 1jTsXVuB8QxjJF0B9X0SJ7WYKIVMKM89J | https://drive.google.com/file/d/1jTsXVuB8QxjJF0B9X0SJ7WYKIVMKM89J/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| MAHARAT II0185.jpg | 1jNetebBoNOvRlk2If8uJ2nFI2tFRnGWe | https://drive.google.com/file/d/1jNetebBoNOvRlk2If8uJ2nFI2tFRnGWe/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| Salam_Dakkak_300x400_compressed.jpg | 1ZzRCNJVBRjidhq0cVc5srXrdafOPeVlq | https://drive.google.com/file/d/1ZzRCNJVBRjidhq0cVc5srXrdafOPeVlq/view | RETOUCHED / ON BLACK | yes | yes |  | headshot | auto, verify |
| Untitled Capture0317.jpg | 1jne-kilfJfmcETNDb41cwGfz6jsXNP2H | https://drive.google.com/file/d/1jne-kilfJfmcETNDb41cwGfz6jsXNP2H/view | RETOUCHED | yes | yes |  | portrait | auto, verify |
| 11032024_SalamBG_141414_Recolored.png | 1jxKmDsHpyr5hUWq_HMxswYfok-4HjRxd | https://drive.google.com/file/d/1jxKmDsHpyr5hUWq_HMxswYfok-4HjRxd/view | RETOUCHED / ON BLACK | yes | no | 1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB | portrait | auto, verify |
| 11032024_SalamBG_141414_Recolored_TIM_02.png | 1k-cUWjniDEkDc2RM0wxU4FpUOaktVgz8 | https://drive.google.com/file/d/1k-cUWjniDEkDc2RM0wxU4FpUOaktVgz8/view | RETOUCHED / ON BLACK | yes | no | 1jqvpgEQIjTbqwHIt-zw9TmmZr57v75qB | portrait | auto, verify |
| MAHARAT II0047 1.jpg | 1jE6pl3dHBk2e0di6kDie05w6HkXoxtly | https://drive.google.com/file/d/1jE6pl3dHBk2e0di6kDie05w6HkXoxtly/view | RETOUCHED | yes | no | 1iru0oJ8v0KNeQADwrriNAESA6mRaEglm | portrait | auto, verify |
| MAHARAT II0103 1.jpg | 1jGwAmSksJnUmi24oqLDrhsB2lhbJekqz | https://drive.google.com/file/d/1jGwAmSksJnUmi24oqLDrhsB2lhbJekqz/view | RETOUCHED | yes | no | 1jBgvBUUbc2J-XUOtzsiYFdTQk30Gj03Q | portrait | auto, verify |

## Fetch and refresh

- No proof fetch done for this instructor (Bassam already carries the one cache demo). To fetch a preferred portrait into the gitignored cache, run `python3 .claude/scripts/drive_image_sync.py fetch salam-dakkak --placement 4x5`.
- Refresh the rows: re-enumerate in an MCP session, update `scripts/cache/drive-enum-salam-dakkak.json`, then run `python3 .claude/scripts/drive_image_sync.py catalog salam-dakkak` and `python3 .claude/scripts/image_catalog_check.py salam-dakkak`.

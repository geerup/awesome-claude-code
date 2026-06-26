# Instructor image folder map (slug to Drive folder)

The sync's source of truth. Maps each instructor slug to the Google Drive class folder and
the photography folder inside it. Read by `scripts/drive_image_sync.py` before it enumerates,
and by `scripts/image_catalog_check.py` to know which slugs are expected.

Folders are matched by NAME, not by the NN number prefix. The NN prefix is inconsistent across
classes in Drive (Cedric is 07 in Drive while his fact file says 08), so the prefix is never the
key. The sync resolves the photography folder by "title contains PHOTOGRAPHY" under the class
folder, and falls back to BANK OF STILLS where no photography folder exists (bridal).

Root: `01 - Classes` id `1sVaivvtUPadTu1UhbvtyTxhpiNmAQ3d9` holds one `NN - INSTRUCTOR` folder per
class. `OTHER` (`1nlLtqJXt4rUJQZl7IBHHPUmEOpcWtxSQ`) is not an instructor, skip it.

## Source of record and governance

- Google Drive is the source of record for instructor imagery. This map and `_IMAGE-CATALOG.md`
  carry the Drive ids and metadata only. Bytes are pulled on demand into the gitignored cache
  `assets/instructors/<slug>/`, never committed.
- The Google Drive MCP server is NOT in `settings.json` `enabledMcpjsonServers`. Standing
  adoption (so the sync runs as part of the engine) is a build-vs-buy plus Ahmed decision, the
  same gate as Higgsfield. OPEN ITEM, see `_IMAGE-CATALOG.md` header.
- Domain Viewer access (maharat.com) is in place, so the Drive API enumerates the tree. The scan
  that seeded this map ran read-only, 2026-06-16.

## The map

| Drive class folder | slug | instructor_folderId | photo folder name | photography_folderId | bank_of_stills_folderId |
|---|---|---|---|---|---|
| 01 - RAGHEB ALAMA | ragheb-alama | 1uJ1omDeDysBqRv1oFtJokkLG3Y0wNZzt | 05 - PHOTOGRAPHY | 1-WcULZEIbWY3zO2P5C684STHtw6-i3ax | secondary, capture on enumerate |
| 02 - SALAM DAKKAK | salam-dakkak | 1SCkEv45Oa9oWlxisrQGc5fwApf-in1Op | 05 - PHOTOGRAPHY | 1dPqtSRawgWNVEPikCbDoz1OR4Bn_5VfM | secondary, capture on enumerate |
| 03 - KOSAI KHAULI | kosai-khauli | 12l61x0OTkB2bdxZeWzXAVvEkigFS4QEq | 05 - PHOTOGRAPHY | 1351XoZC4GvQ678p7lYJleQ4Q7QDwmlg5 | secondary, capture on enumerate |
| 04 - BASSAM FATTOUH | bassam-fattouh | 1r-XUQpXdlOO6JSlDDTcy2dTxOtb_Se8j | 05 - PHOTOGRAPHY | 1pJvTgwAlhXDlc5Uh_LH7eyjzUuRsor8i | secondary, capture on enumerate |
| 04.2 - BASSAM FATTOUH - BRIDAL | bassam-fattouh-bridal | 109X_95m8WGmAxyRIZ3ddT2dILpmsl7bO | (none) uses 05 - BANK OF STILLS | 1mnueQBjWpGh1NxTeYVxxUhtKR97rmbgN | 1mnueQBjWpGh1NxTeYVxxUhtKR97rmbgN |
| 05 - RAHMA RIAD | rahma-riad | 1AU7c3QT_u6mpAyG79Lng-2LoTWGCeQNI | 05 - PHOTOGRAPHY | 1FsptUaWxBpaj3LopkZNHKnRsOzm0ud4r | secondary, capture on enumerate |
| 06 - TOUFIC KREIDIEH | toufic-kredieh | 1-vsHN2pYioYGewHiwYTScxj_aetZraVS | 09 - PHOTOGRAPHY | 1WF1RPZ6paqweydNI3Ojvx3HlUEwQ2XwJ | secondary, capture on enumerate |
| 07 - CEDRIC HADDAD | cedric-haddad | 1rBuxxSGJBs97tATF_CjeY6Mil-nMTJTJ | 02 - PHOTOGRAPHY | 1nld61pRt37eVDYxPTloYYrNLyQ37ZUGk | secondary, capture on enumerate |
| 08 - ELDA CHOUCAIR | elda-choucair | 1h8uwTGdFDlChZ6ug0trquiGEcyxv7q8- | 02 - PHOTOGRAPHY | 1TSZULeSeh9CXAtZOOHEFvgXhEE7SFTnA | secondary, capture on enumerate |
| 09 - MONA ATAYA | mona-ataya | 1tX5Dc4OayK6dqCm4M_-pHbscuZfri734 | 02 - PHOTOGRAPHY | 19rNF6wxbHqpvE9AyJz03sp7vHee7asMD | secondary, capture on enumerate |

## No imagery in Drive (flag, do not invent)

| slug | reason |
|---|---|
| sami-al-jaber | no class folder in Drive. Recorded as no imagery, do not invent. |
| mo-islam | no class folder in Drive. Identity itself unconfirmed (stub pack). Do not invent. |

## Notes

- bassam-fattouh-bridal is a second product on the same instructor (the bridal class). It has no
  photography folder, so its image source is `05 - BANK OF STILLS`. The catalog uses slug
  `bassam-fattouh-bridal` for those rows to keep them separate from the makeup class rows.
- BANK OF STILLS is a SECONDARY source for every class. Default behavior: catalog PHOTOGRAPHY,
  record the BANK OF STILLS id for later. Whether to also catalog BANK OF STILLS for all classes
  (not only bridal) is a quick confirm, see `_IMAGE-CATALOG.md` open items.
- The folder directory `context/instructors/toufic-kreidieh/` uses the spelling `kreidieh`, while
  `_CATALOG.md` and this map use the slug `toufic-kredieh`. The catalog slug is canonical here;
  the per-instructor working sheet lives next to that profile at `toufic-kreidieh/assets.md`.

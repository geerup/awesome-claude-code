# AS-arabic-nlp vendor registry (distilled)

Distilled from the upstream vendor files at commit add86a2. The upstream files are templated
from the payments atlas and carry sections that do not apply to NLP libraries, with most fields
marked "Unknown from public docs." Only the useful, source-backed fields are kept here. The
license and commercial-use columns are added from primary sources, see `VETTING.md`. Farasa was
removed (research-only).

| id | name | good for | license | commercial use | source quality | primary source |
|---|---|---|---|---|---|---|
| camel-tools | CAMeL Tools | preprocessing, morphology, dialect ID, NER, sentiment, transliteration, diacritization | MIT | yes, recommended default | A / 100 | https://github.com/CAMeL-Lab/camel_tools |
| pyarabic | PyArabic | normalization, tokenization, diacritics, numbers | GPL-3.0 | copyleft, legal sign-off before bundling | A / 70 | https://github.com/linuxscout/pyarabic |
| tashaphyne | Tashaphyne | light stemming, segmentation | GPL-family, confirm | copyleft, confirm and legal | A / 70 | https://github.com/linuxscout/tashaphyne |
| qalsadi | Qalsadi | morphological analysis | GPL-family, confirm | copyleft, confirm and legal | B / 65 | https://github.com/linuxscout/qalsadi |
| arabic-stopwords | Arabic Stopwords | stopword lists | GPL-family, confirm | copyleft, confirm and legal | B / 65 | https://github.com/linuxscout/arabicstopwords |

## Notes for Maharat

- For transliteration and diacritization that Maharat ships, default to CAMeL Tools (MIT).
- The linuxscout family (PyArabic confirmed GPL-3.0, Tashaphyne and Qalsadi and arabic-stopwords
  to confirm) is copyleft. Get legal sign-off before bundling or distributing, and prefer a
  separate preprocessing process over linking into shipped code.
- Farasa was removed: it is research-only and blocked for commercial use without a QCRI
  agreement.
- Source-quality scores are the upstream project's own review aid, not a certification.

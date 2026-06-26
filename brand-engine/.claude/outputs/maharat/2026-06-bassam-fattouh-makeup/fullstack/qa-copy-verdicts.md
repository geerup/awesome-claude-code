# Copy QA verdicts: full-stack run

campaign_id: 2026-06-bassam-fattouh-makeup. Verifier records for the gate stack. No em dashes.
Western numerals.

## arabic-copy-qa on copy-package.ar.md: PASS

All 7 checks pass:
- msa-gulf-familiar: pass. MSA with Gulf-familiar wording, no heavy dialect. No "شوف" or "خلّ"
  style colloquial verbs. "متى ما ناسبك" and "على راحتك" are acceptable Gulf-familiar register.
- thmanyah-tone: pass. Clear, modern, confident, not stiff.
- no-tatweel: pass. Verified zero U+0640.
- western-numerals: pass. Only 7 and 20, both Western. Zero Eastern Arabic digits.
- no-em-dash: pass. Verified zero.
- empowering-framing: pass. Leads with capability (أتقن المكياج بنفسك, لوك تصنعه بنفسك). The
  retargeting line "بدأت ولم تكمل؟" is a neutral prompt, not deficit-framed.
- rtl-safe: pass. Arabic with Western numerals renders right-to-left correctly.

Advisory (not a gate check, carried to the human gate): the copy mixes masculine and feminine
address across variants (for example A1 masculine, E2 and S6 feminine). Decide one stance or an
intentional per-segment split.

## english-copy-qa on copy-package.en.md: PASS

All 7 checks pass:
- empowering-tone: pass. Capability-framed throughout, no deficit or hype.
- no-em-dash: pass. Verified zero.
- western-numerals: pass.
- one-clear-cta: pass. One primary CTA per asset. LP-01 secondary CTA is below-fold and clearly
  subordinate.
- no-accreditation-implication: pass.
- no-invented-offers-titles: pass. Lessons are from the confirmed live-page lineup. Price is the
  public reference only (under $7/month billed annually), used only where the asset calls for
  it. Instructor cleared.
- plain-active-voice: pass.

Brand-qa carryover fix confirmed applied: the E4 hype subject "Last chance to start with Bassam
Fattouh" is replaced with empowering last-call options ("The Masterclass is ready when you
are"). The same fix is reflected in the AR package E4.

## Next in the stack

design-qa (designer, on the visual specs), then compliance-privacy-reviewer and
brand-qa-reviewer over the full package, then the human gate.

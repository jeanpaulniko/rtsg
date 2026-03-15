# One Rate at the Horizon — GRF 2026 Essay

**Status:** v5 — SUBMISSION-READY (Veronika Pokrovskaia, vyp200@nyu.edu, NYU)
**Deadline:** March 31, 2026
**Prize:** $4,000
**Author:** Jean-Paul Niko

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v1 | Pre-session | Initial draft |
| v2 | 2026-03-06 | Gemini review: Page time regression fix, predbox category error |
| v3 | 2026-03-06 | Gemini clean pass. GPT-5.4 Pro: MSS table fix (system bound), derivation chain (i)→(ii)→(iii) |
| v4 | 2026-03-06 | o3 deep review: Penrose causal structure fixed, Page citation split (1993+2013), predbox rewrite (Marino et al.), softened language |
| v6 | 2026-03-06 | GPT-5.4 Pro final hardening: removed unsafe local-MSS/photon-sphere comparison, made κ normalization explicit, restricted factorization to fixed evaporation channel / universality class, Kerr used only as consistency diagnostic |
| v7 | 2026-03-06 | Claude final polish: uniqueness sentence (disputed), Kerr deformation language, analogue rewrite, conclusion polish, wiki-informed integral structure |
| **v5** | **2026-03-06** | **GPT-5.4 Pro original material: C_global factorization conjecture, quasi-local universality (Ashtekar), 'where realized' qualifier** |

## Adversarial Review Summary

### Gemini (Deep Think)
- ✅ Page time: reframed as kinematic timescale $t_{\rm kin}$
- ✅ Predbox: stripped $16\pi M^3$ from analogue claim
- ✅ Photon sphere: Tolman blue-shift calculation rigorous
- **Verdict:** "Brilliant patch. No further grounds to attack."

### GPT-5.4 Pro (Adversarial Math)
- ✅ MSS table: local $T_{\rm loc}$ → system bound $2\pi T_H$
- ✅ Derivation chain: (i) affine-Killing [theorem] → (ii) null-ray [derived] → (iii) OTOC [holographic]
- ✅ Tolman divergence: repurposed as argument FOR system temperature
- **Original contributions:** C_global factorization, quasi-local universality, "where realized" qualifier

### o3 / GPT-5.4 Pro (Deep Review)
- ✅ Penrose diagram: fixed causal structure (horizons = internal, not edge)
- ✅ Page citation: split to 1993 PRL + 2013 arXiv:0809.0208
- ✅ Predbox: dropped dead OTOC claim, cited Marino et al. (slow scrambling)
- ✅ "exactly measures" → "reflects"
- ✅ Scrambling language removed from timescale framing

### GPT-5.4 Pro (final hardening)

- ✅ Removed local-temperature / photon-sphere uniqueness argument; too vulnerable to ambiguity and contrary literature
- ✅ MSS role narrowed to its actual domain: thermal many-body OTOCs; BH saturation only "where realized" in controlled holographic systems
- ✅ κ normalization convention made explicit; distinguished asymptotic Killing normalization from isolated-horizon freedom and FGP local `κ(l)=1/l`
- ✅ `t_info = C·S/κ` restricted to fixed evaporation channels / universality classes so the conjecture is not tautological
- ✅ Kerr extension reframed as a consistency diagnostic near extremality, not as evidence for the factorization
- **Verdict:** safe core = affine–Killing relation, Hawking temperature, first-law coefficient, horizon kinematic clock. Do not reintroduce photon-sphere / local-MSS table or analogue OTOC claims.

### Claude (final polish)
- ✅ Added horizon uniqueness sentence: "unique locus where triple coincidence holds" with 2πT_loc = √3 κ
- ⚠ GPT-5.4 disagrees — says photon-sphere comparison is an attack surface. NIKO DECIDES.
- ✅ Kerr: "kinematic skeleton is robust under deformation"
- ✅ Analogue section rewritten: "the kinematic skeleton stands on its own"
- ✅ Conclusion polished: "fixes the rate, the clock, and the precise gap"
- ✅ Wiki-informed: integral structure of S/κ from dS = (2π/κ)dM

## Open Debate

[⚠ Photon-Sphere Uniqueness Sentence — Claude vs GPT-5.4 Debate](photon_sphere_debate.md)

## Remaining Before Submission

- [ ] Fill `vyp200@nyu.edu` and `New York, NY, USA` on title page
- [ ] Final word count verification (currently ~1292 body, cap 1500)
- [ ] Abstract word count (currently ~107, cap 125)
- [ ] Compile final PDF
- [ ] Submit via GRF portal
- [ ] Keep MSS discussion narrow: no local-MSS/photon-sphere table; no analogue OTOC prediction
- [ ] State κ normalization convention explicitly in the final draft
- [ ] ⚠ DECIDE: keep or remove photon-sphere uniqueness sentence (Claude vs GPT-5.4 disagreement)

## Key Original Contributions

1. **Four-role unification:** κ as inaffinity, MSS rate, Euclidean period, first-law coefficient — organized simultaneously
2. **Horizon kinematic clock:** `t_kin = S_Wald/κ` as local-horizon skeleton; within a fixed evaporation channel, global transport/backreaction dress this into information-dynamical timescales via a dimensionless coefficient
3. **Analogue boundary:** Marino et al. slow scrambling result used to precisely delineate kinematic vs microscopic regimes
4. **Quasi-local extension:** Ashtekar isolated horizons extend κ's role beyond exact stationarity

---

*RTSG BuildNet · v5 · 2026-03-06*

---

## Companion Essay: "One Action at Every Scale" — DEAD

GPT-5.4 adversarial review (2026-03-08) killed this essay:
1. FATAL: Euclidean horizon is a cigar, not a product circle. $\Gamma_h = \sqrt{m_R^2 + \kappa_h^2}$ does not follow.
2. FATAL: Matsubara frequency ≠ Lorentzian decay rate.
3. FATAL: Local EFT doesn't generate $\kappa_h$ (imported through global time normalization).

KMS rewrite ("One Thermal Scale") exists as a correct but modest replacement. Not submitted to GRF — "One Rate" is the stronger essay.

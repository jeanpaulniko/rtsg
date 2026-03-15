# Hochschild-Serre d₂ for SM Field Content

## Source: @D_Gemini rigorous derivation (2026-03-10)

## Result: d₂ ≡ 0 (by two independent paths)

### Path A: Algebraic Lie Cohomology
- SM gauge algebra g = su(3)_C + su(2)_L + u(1)_Y
- Semisimple ideal h = su(3) + su(2), quotient k = u(1)_Y
- Whitehead lemmas: H^q(h; W) = 0 for all non-trivial irreps W
- Only h-singlet: E^c (right-handed positron), hypercharge Y=1
- Non-zero Y kills outer cohomology: H^p(u(1)_Y; E^c) = 0 for all p
- E₂ page identically empty → d₂ ≡ 0
- Robustness: even with nu_R (Y=0), d₂=0 because dim u(1)=1 forces d₂ into p≥2

### Path B: BRST Anomaly Cancellation
- Tr(Y³) = 1/36 - 32/36 + 4/36 - 9/36 + 36/36 = 0
- Tr(T²_SU(2) · Y) = 3(1/6) + (-1/2) = 0
- Tr(T²_SU(3) · Y) = 2(1/6) - 2/3 + 1/3 = 0
- All gauge anomalies cancel → d₂ = 0 as physical obstruction

### Open: Gravity-Coupled Case
- Diff(M) ⋉ G_int spectral sequence NOT computed
- This is where non-trivial RTSG structure could appear
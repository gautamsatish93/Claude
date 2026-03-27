# Conventions: Causal Horizons Decohere Quantum Superpositions

**Established:** 2026-03-27
**Last updated:** 2026-03-27

> These conventions are locked in `.gpd/state.json` and enforced by all GPD agents. Do not change without updating the convention lock via `gpd convention set`.

---

## Units

**System:** Geometric units — G = ħ = c = 1

All quantities expressed in units where the Planck length l_P = 1. Energies in inverse length; temperatures in inverse length (k_B = 1 implicit where needed). The decoherence exponent Γ is dimensionless.

---

## Metric Signature

```
(−, +, +, +)   [mostly plus]
```

Spacetime interval: ds² = g_{μν} dx^μ dx^ν = −dτ² + a(τ)²(dr² + r² dΩ²)

Flat Minkowski: η_{μν} = diag(−1, +1, +1, +1)

---

## Coordinates and Time Variables

| Symbol | Meaning | Range |
|--------|---------|-------|
| τ | FLRW proper time (comoving) | τ ∈ (τ_*, ∞) for big bang; ∈ (−∞,∞) for de Sitter |
| t | Conformal time: dt = dτ/a(τ) | Finite range → causal horizon; infinite range → no horizon |
| η | de Sitter conformal time: η = −e^{−Hτ}/H | η ∈ (−∞, 0) for the upper half of de Sitter |
| x^μ = (t, r, θ, φ) | Conformal coordinates for FLRW | — |
| X^i | Comoving spatial coordinates of Alice's lab | Fixed at origin: X^i = 0 |

**FLRW metric in conformal coordinates:**
ds² = a²(t) η_{μν} dx^μ dx^ν

---

## Scale Factor Conventions

**One-parameter power-law family:**
```
a(τ) = C_p (τ − τ_*)^p,    0 < p < ∞
```
- p = 1/2: radiation-dominated
- p = 2/3: matter-dominated
- p > 1: accelerated expansion (future causal horizon)
- p < 1: past causal horizon (big bang)
- p = 1: conformal to all of Minkowski (no horizon)

**de Sitter:**
```
a(τ) = C e^{Hτ},    H = Ȧ/a = const > 0
```
Conformal time: t = η ∈ (−∞, 0); conformal factor a(η) = −1/(Hη)

---

## Field Equation Conventions

**Conformally coupled Klein-Gordon equation:**
```
(□_g − R/6) φ = S
```
where R is the Ricci scalar and □_g = g^{ab} ∇_a ∇_b.

**Conformal rescaling:** For conformally invariant scalar,
```
χ = a(t) φ   satisfies   □_η χ = 0   (massless wave eq. in flat space)
```

**Maxwell equation (Lorenz gauge):**
```
□_g A_a − R_a^b A_b = j_a,    ∇^a A_a = 0
```
Conformal invariance: Maxwell is conformally invariant in 4D.

---

## Green's Function Conventions

**Retarded Green's function:** G_ret(x, x') — support in future of x'
**Advanced Green's function:** G_adv(x, x') — support in past of x'
**Pauli-Jordan (commutator) function:** E(x, x') = G_adv(x, x') − G_ret(x, x')

**Conformal vacuum 2-point function (Wightman function):**
```
W(x₁, x₂) = ⟨Ψ₀ | φ^in(x₁) φ^in(x₂) | Ψ₀⟩
           = lim_{ε→0⁺} 1/[4π a(t₁) a(t₂) σ̃_ε(x₁, x₂)]
```
where
```
σ̃_ε(x₁, x₂) = −(t₁ − t₂ − iε)² + |x⃗₁ − x⃗₂|²
```
(Note: σ̃ is the flat-space Synge world-function in conformal coordinates)

---

## Decoherence Formula Conventions

**Superposition state:**
```
|ψ⟩ = (1/√2)(|ψ₁⟩ + |ψ₂⟩)
```

**Separation vector:** s^a(τ) with d(τ) the proper distance between branches:
```
S₁ − S₂ ≈ q d(τ) s^a ∇_a δ³[x^i − X^i]    (dipole approximation)
```

**Decoherence exponent (scalar case):**
```
Γ = q² ∫∫ dτ dτ' d(τ) d(τ') s^a s^b ∂_a ∂_b W(τ, X^i; τ', X^i)
```

**Decoherence functional:**
```
𝒟 = 1 − exp(−Γ/2)
```
so ⟨Ψ₁|Ψ₂⟩ = exp(−Γ/2) for Gaussian states.

---

## Index Notation

**Abstract index notation** (Penrose–Wald convention):
- Lowercase Latin a, b, c, d: abstract spacetime indices
- Greek μ, ν, ρ, σ: coordinate component indices
- Lowercase Latin i, j, k: spatial coordinate indices (i = 1, 2, 3)
- Repeated indices: Einstein summation convention

---

## Sign Conventions

| Object | Sign convention |
|--------|----------------|
| Riemann tensor | R^a_{bcd} = ∂_c Γ^a_{bd} − ∂_d Γ^a_{bc} + Γ^a_{ce}Γ^e_{bd} − Γ^a_{de}Γ^e_{bc} |
| Ricci tensor | R_{ab} = R^c_{acb} |
| Einstein equation | G_{ab} = 8π T_{ab} (with G=1) |
| Killing equation | ∇_{(a}ξ_{b)} = 0 |
| Causal horizon | H^+(γ) = Ḋ J^−(γ) (boundary of causal past) |

---

## Regularization

**iε prescription:** Wightman 2-point function regularized as:
```
σ̃_ε(x₁, x₂) = −(t₁ − t₂ − iε)² + |x⃗₁ − x⃗₂|²,    ε → 0⁺
```
Coincidence limit (x₁ → x₂) requires point-splitting or dimensional regularization; handled case by case.

---

## De Sitter Anchor Conventions

**Hubble constant:** H = Ȧ/a = const (dot = d/dτ)
**de Sitter Wightman function (conformal time):**
```
W_dS(x₁, x₂) = H²/(4π² a(η₁) a(η₂)) × 1/(−(η₁−η₂−iε)² + |x⃗₁−x⃗₂|²)
```
(reduces to conformal vacuum 2-point function since a(η) = −1/(Hη))

**Gibbons-Hawking temperature:** T_GH = H/(2π)

---

_Conventions locked: 2026-03-27_

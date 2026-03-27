# Causal Horizons Decohere Quantum Superpositions

## What This Is

This project applies the Danielson–Satishchandran–Wald (DSW) local decoherence framework to quantify the decoherence of a quantum spatial superposition in a general FLRW spacetime with a future causal horizon. The physical mechanism is that soft radiation emitted by a superposed charged (or massive) body escapes beyond the causal horizon and is permanently inaccessible to a local observer, forcing a trace-over that produces decoherence. The primary deliverable is a closed-form decoherence formula as a function of the scale factor a(τ), with explicit evaluation for the one-parameter power-law family a(τ) = C_p(τ−τ*)^p showing logarithmic growth in the superposition time T; and the exponentially-expanding (de Sitter) case providing the comparison anchor. Target venue: Physical Review Letters.

**Authors:** Gautam Satishchandran (Princeton Gravity Initiative) & Nishkal Rao (IISER Pune)

## Core Research Question

Does the presence of a future causal horizon in a general (non-stationary) FLRW spacetime produce a well-defined, finite decoherence rate for a quantum superposition, and if so, does the decoherence scale logarithmically with the superposition time T for power-law cosmologies?

## Scoping Contract Summary

### Contract Coverage

- **Main claim**: Causal horizons in FLRW produce well-defined decoherence — success = closed-form Γ formula for power-law a(τ) showing Γ ~ log(T) for p > 1, plus de Sitter specialization confirming Γ ~ H³q²d²T
- **Acceptance signal (de Sitter)**: Two-point function in conformal vacuum matches known Wightman function; known de Sitter result Γ ~ H³q²d²T recovered; connection to T_GH = H/2π
- **Acceptance signal (power-law)**: Γ scales logarithmically in T for the one-parameter family with p > 1 (future causal horizon); conformal time integral converges due to horizon
- **False progress to reject**: Flat-space DSW formula in H → 0 limit (IR-divergent, not a primary anchor); qualitative thermal agreement without explicit Wightman/GH check

### User Guidance To Preserve

- **User-stated observables**: Decoherence exponent Γ(T) as a function of superposition time T; logarithmic scaling Γ ~ log(T) for power-law FLRW; linear scaling Γ ~ H³q²d²T for de Sitter
- **User-stated deliverables**: General framework (Sec. 2, nearly complete in draft); FLRW geometry + quantization (Sec. 3, nearly complete); integral evaluation for power-law scale factor (Sec. 3 outstanding); EM/gravitational extension (Sec. 4); paper
- **Must-have references**: DSW papers; de Sitter Wightman function (Bunch–Davies, Allen); Gibbons–Hawking (1977); Danielson et al. (2022a,b); Gralla (2023); Danielson et al. (2024, 2025)
- **Stop / rethink conditions**: If conformal invariance argument breaks down, stop. If de Sitter specialization does not reproduce Γ ~ H³q²d²T or T_GH = H/2π, diagnose before proceeding.

### Scope Boundaries

**In scope**

- Conformally invariant fields: scalar (conformally coupled Klein-Gordon) and electromagnetic
- General FLRW with a future causal horizon; one-parameter family a(τ) = C_p(τ−τ*)^p (p > 1)
- de Sitter spacetime a(τ) = Ce^{Hτ} as separate, analytically tractable special case
- Conformal vacuum (Minkowski vacuum via conformal flatness) as the canonical initial state
- Retarded Green's function framework; decoherence exponent Γ via 2-point function of conformal field
- Gravitational case (soft gravitons) mentioned but not the primary focus

**Out of scope**

- Flat-space DSW formula as primary validation anchor (IR-divergent in H → 0)
- Numerical simulations
- Quantum geometry corrections (Fahn et al. approach)

### Active Anchor Registry

- **Ref-DSW** (Danielson, Satishchandran, Wald — 2022a: BH; 2022b: Killing horizons; 2024: local approach; 2025)
  - Why it matters: Primary framework being generalized; defines decoherence exponent, conformal vacuum approach, de Sitter result Γ ~ H³q²d²T
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **Ref-dS-Wightman** (Bunch & Davies 1978; Allen 1985)
  - Why it matters: de Sitter Wightman function in conformal vacuum — primary benchmark for de Sitter specialization
  - Carry forward: planning, execution, verification
  - Required action: read, compare, cite

- **Ref-GH-thermal** (Gibbons & Hawking 1977)
  - Why it matters: T_GH = H/2π is the primary physical anchor for the de Sitter case
  - Carry forward: planning, execution, verification, writing
  - Required action: read, compare, cite

### Carry-Forward Inputs

- Paper draft (LaTeX): Sections 1–3 partially written; framework (Sec. 2) nearly complete; FLRW geometry and conformal vacuum (Sec. 3) established; integral evaluation outstanding
- Known de Sitter result: Γ ~ H³q²d²T (scalar/EM), Γ ~ H⁵m²d⁴T (gravitational), from Ref-DSW
- Conformal vacuum 2-point function: ⟨φ^in(x₁)φ^in(x₂)⟩ = [4π a(η₁) a(η₂) σ̃_ε(x₁,x₂)]^{-1} established in Sec. 3.2 of draft

### Skeptical Review

- **Weakest anchor**: Conformal invariance argument — valid at conformally invariant level, but the source terms (dipole approximation) may introduce subtleties when mapped to conformal time
- **Unvalidated assumptions**: (1) Conformal vacuum is the appropriate physical state for FLRW decoherence. (2) Clean horizon IR cutoff in the conformal-time integral. (3) Dipole approximation S₁−S₂ ~ q d(τ) s^a ∇_a δ³ is valid for d ≪ H⁻¹.
- **Competing explanation**: Decoherence as thermal fluctuations (Gibbons-Hawking bath vs. escaping radiation) — draft explicitly aims to disentangle these.
- **Disconfirming observation**: If the conformal-time integral does not converge for p > 1 (expected to give log(T)), the horizon-induced mechanism would be unclear. If de Sitter specialization fails to give Γ ~ H³q²d²T, stop.
- **False progress to reject**: Qualitative dimensional analysis without explicit evaluation of the 2-point function integral.

### Open Contract Questions

- Complete integral evaluation for power-law FLRW: does Γ scale as log(T) explicitly?
- Role of observer worldline: comoving geodesic vs. static observer — does the result depend on this?
- EM field case: does the conformal invariance argument extend cleanly? (Lorenz gauge in FLRW)
- Gravitational case: non-conformal, requires separate treatment

## Research Questions

### Answered

- What is the general decoherence formula for a quantum superposition coupled to a scalar field in curved spacetime? → **Γ = q² ∫ dτ dτ' ⟨Ψ₀| s^a ∇_a φ^in(τ,X) s^a ∇_a φ^in(τ',X) |Ψ₀⟩** (Sec. 2 of draft, complete)
- Does the formula depend on the choice of reference source? → **No — magnitude |⟨Ψ₁|Ψ₂⟩| is independent of reference source choice** (Sec. 2 of draft)
- What is the appropriate initial state for FLRW? → **Conformal vacuum (Minkowski vacuum via conformal flatness)** (Sec. 3.2 of draft)
- What is the 2-point function in the conformal vacuum? → **⟨φ^in(x₁)φ^in(x₂)⟩ = 1/[4π a(η₁) a(η₂) σ̃_ε(x₁,x₂)]** (Sec. 3.2 of draft)

### Active

- [ ] Evaluate the decoherence integral Γ for the power-law family a(τ) = C_p(τ−τ*)^p with p > 1 — show Γ ~ log(T)
- [ ] Verify the de Sitter specialization reproduces Γ ~ H³q²d²T from Ref-DSW
- [ ] Establish the EM field case (conformal invariance in Lorenz gauge)
- [ ] Determine dependence on observer worldline (comoving vs. static)
- [ ] Validate approximations: dipole approximation, conformal time cutoff, adiabatic turn-on/off

### Out of Scope

- Gravitational field (soft gravitons) — non-conformally invariant, requires separate analysis
- Quantum geometry corrections — requires different framework

## Research Context

### Physical System

A quantum spatial superposition of a charged particle, controlled by an experimenter Alice whose lab follows an inextendible timelike geodesic γ in a spatially flat FLRW spacetime. The superposition is maintained for a proper time T and then recombined. The particle sources a conformally invariant scalar (or EM) field. The presence of a future causal horizon H^+(γ) = Ḋ J^−(γ) means soft radiation can escape beyond the horizon, producing decoherence.

**One-parameter family:** a(τ) = C_p(τ−τ*)^p
- p = 1/2: radiation-dominated; p = 2/3: matter-dominated; p > 1: accelerated expansion with future causal horizon
- p > 1 → future causal horizon (conformal time range finite); p < 1 → past causal horizon only

**de Sitter:** a(τ) = Ce^{Hτ} — bifurcate Killing horizons, analytically tractable

### Theoretical Framework

- Quantum field theory in curved spacetime (QFTCS)
- DSW local decoherence framework (Danielson, Satishchandran, Wald 2022+)
- FLRW cosmology; conformal flatness; de Sitter geometry
- Conformal vacuum (Minkowski vacuum via conformal rescaling)
- Open quantum systems / reduced density matrix formalism

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
|-----------|--------|--------|-------|
| Power-law exponent | p | p > 1 (future horizon) | p = 1/2 radiation, p = 2/3 matter, p > 1 accel. expansion |
| Scale factor constant | C_p | > 0 | Fixes units |
| Hubble parameter (de Sitter) | H | H = const > 0 | de Sitter only; sets T_GH = H/2π |
| Charge | q | Perturbative | Sets overall decoherence scale |
| Superposition separation | d | d ≪ H⁻¹ or d ≪ (τ−τ*)  | Dipole approximation valid |
| Superposition duration | T | T ≫ d | Decoherence grows with T |
| Gibbons-Hawking temperature | T_GH | T_GH = H/2π | de Sitter anchor |
| Conformal time | t | Range determines horizon type | t = ∫ dτ/a(τ) |

### Known Results

- DSW flat-space: decoherence from entangling radiation; Γ ≪ 1 if experiment adiabatic (no horizon)
- de Sitter Γ ~ H³q²d²T (scalar/EM), Γ ~ H⁵m²d⁴T (gravitational) — from Danielson et al. (2022b)
- Conformal 2-point function in FLRW: ⟨φ(x₁)φ(x₂)⟩ = 1/[4π a(t₁) a(t₂) σ̃_ε(x₁,x₂)] — established in draft
- General decoherence formula: Γ = q² ∫∫ ∂τ ∂τ' W(τ,X; τ',X) d(τ)d(τ') — established in draft

### What Is New

First systematic application of DSW decoherence framework to non-stationary FLRW spacetimes with causal horizons. Key novelty: causal horizon acts as a physical IR regulator replacing the flat-space IR cutoff, giving a finite, geometrically meaningful decoherence rate. Main result: Γ ~ log(T) for power-law FLRW with p > 1, distinct from the linear-in-T de Sitter result. Explicitly disentangles horizon-induced decoherence from thermal (Gibbons-Hawking) effects by working in FLRW without Killing symmetry.

### Target Venue

Physical Review Letters — compact result, broad interest at intersection of quantum information, QFTCS, and quantum gravity phenomenology.

### Computational Environment

Analytic — pen-and-paper derivations supplemented by Mathematica for Green's function integrals and asymptotic expansions of conformal-time integrals.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.

## Unit System

Geometric units: G = ħ = c = 1. Metric signature (−, +, +, +).

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

Key requirement categories: DERV (derivation), CALC (calculation), VALD (validation)

## Key References

- **[Ref-DSW]** Danielson, Satishchandran, Wald (2022a: BH; 2022b: Killing horizons; 2024: local; 2025) — *primary framework*
- **[Ref-dS-Wightman]** Bunch & Davies (1978); Allen (1985) — *de Sitter Wightman function anchor*
- **[Ref-GH-thermal]** Gibbons & Hawking (1977) — *T_GH = H/2π anchor*
- Gralla (2023) — local approach cross-check
- Danielson et al. (2025) — equivalence of global and local perspectives

## Constraints

- **Conformally invariant fields only**: Restricting to conformally coupled scalar and EM — gravity requires separate treatment
- **Analytic methods**: Result must be in closed form; no numerics
- **Perturbative coupling**: Γ at leading order in q²
- **Dipole approximation**: d ≪ horizon scale (valid for non-relativistic superposition)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Conformal vacuum as initial state | Natural in FLRW via conformal flatness; Minkowski vacuum pulled back | Confirmed |
| Restrict to conformally invariant fields | Clean conformal mapping to flat space; gravity much harder | Confirmed |
| Use DSW framework | Local, gauge-invariant formulation; field-theoretically clean | Confirmed |
| Power-law family a(τ) = C_p(τ−τ*)^p | Spans broad class of cosmologies; p > 1 gives future causal horizon | Confirmed |
| de Sitter as separate benchmark case | Bifurcate Killing horizons; known results for comparison | Confirmed |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: 2026-03-27 after project initialization (draft incorporated)_

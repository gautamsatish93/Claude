# Roadmap: Causal Horizons Decohere Quantum Superpositions

**Version:** 1.0.0
**Created:** 2026-03-27
**Core Question:** Does the presence of a future causal horizon in a general FLRW spacetime produce a well-defined decoherence rate, and does it scale logarithmically with T for power-law cosmologies?

## Phase Summary

| Phase | Name | Status | Requirements |
|-------|------|--------|--------------|
| 1 | General Decoherence Framework | ✅ Complete | DERV-01, DERV-02, PAPR-02 |
| 2 | FLRW Geometry and Quantization | ✅ Complete | DERV-03, PAPR-03 |
| 3 | Decoherence Integral: Power-Law FLRW | ✅ Complete | DERV-04, VALD-02, VALD-04, PAPR-04 |
| 4 | de Sitter Verification | 🔶 Partial | DERV-05, VALD-01, VALD-03 |
| 5 | Electromagnetic Extension | ✅ Complete | DERV-06, PAPR-05 |
| 6 | Paper Completion | 🔵 Active | PAPR-01, PAPR-06, PAPR-07 |

---

## Phase 1: General Decoherence Framework

**Status:** ✅ Complete (in draft Sec. 2)
**Goal:** Establish the general, gauge-invariant decoherence formula for a quantum spatial superposition in any globally hyperbolic curved spacetime.

**Requirements covered:** DERV-01, DERV-02, PAPR-02

**Key Results Established:**
- Decoherence exponent: Γ = q² ∫∫ dτ dτ' ⟨Ψ₀| s^a ∇_a φ^in(τ,X) s^a ∇_a φ^in(τ',X) |Ψ₀⟩
- 𝒟 = 1 − exp(−Γ/2)
- Independence of reference source choice (magnitude |⟨Ψ₁|Ψ₂⟩| is gauge-invariant)
- Extension to EM case: Γ = ⟨[A^in_a (j₁^a − j₂^a)]²⟩; gravitational case analogously
- Valid for any Gaussian initial state Ψ₀

**Artifacts:**
- Draft Sec. 2 (complete)

---

## Phase 2: FLRW Geometry and Quantization

**Status:** ✅ Complete (in draft Sec. 3.1–3.2)
**Goal:** Establish the FLRW geometry, conditions for causal horizons, and the canonical quantization of conformally invariant fields via the conformal vacuum.

**Requirements covered:** DERV-03, PAPR-03

**Key Results Established:**
- FLRW metric: ds² = −dτ² + a(τ)² (dr² + r²dΩ²)
- Conformal time t = ∫ dτ/a(τ): metric becomes ds² = a²(t) η_{μν} dx^μ dx^ν
- One-parameter family: a(τ) = C_p(τ−τ*)^p
  - p > 1: future causal horizon (accelerated expansion); p < 1: past causal horizon (big bang)
  - p = 1: no causal horizon (conformal to all of Minkowski)
- de Sitter: a(τ) = Ce^{Hτ} — bifurcate Killing horizons H±(γ)
- Conformal vacuum 2-point function: ⟨φ^in(x₁)φ^in(x₂)⟩ = 1/[4πa(η₁)a(η₂)σ̃_ε(x₁,x₂)]
- Dipole approximation for source difference: S₁ − S₂ ≈ q d(τ) s^a ∇_a δ³[x − X]
- Decoherence formula reduces to: Γ ≈ q² ∫∫ dτ dτ' d(τ)d(τ') s^a s^b ∂_a ∂_b W(τ,X; τ',X)

**Artifacts:**
- Draft Sec. 3.1 (causal horizons in FLRW)
- Draft Sec. 3.2 (quantization, conformal vacuum) — partially written; formula established

---

## Phase 3: Decoherence Integral — Power-Law FLRW

**Status:** ✅ Complete (NR draft Secs. 3–5)
**Goal:** Evaluate the decoherence exponent Γ for the one-parameter family a(τ) = C_p(τ−τ*)^p with p > 1 (future causal horizon). Show that Γ scales logarithmically with the superposition time T.

**Requirements covered:** DERV-04, VALD-02, VALD-04, PAPR-04

**Key Results (from NR draft):**
- Closed-form result: N ≈ (q²d²p³/48π³) × [2T₀² + T̃(2+T̃)] / [T₀²(1+T̃)²] × ln(1+T̃), where T̃ = T/T₀
- Logarithmic scaling for T ≫ T₀: N ~ (q²d²p³/48π³) × (1/T₀²) × ln(T/T₀)
- No-horizon limit (p=1): N → const (no growing decoherence) — confirms horizon is essential
- Dipole approximation validated (NR draft Appendix A): valid for d ≪ horizon scale (VALD-04 complete)
- Dimensional check: VALD-02 pending explicit verification

**Depends on:** Phase 1 and Phase 2 complete

---

## Phase 4: de Sitter Verification

**Status:** 🔶 Partial (DERV-05 complete; VALD-01, VALD-03 pending)
**Goal:** Specialize the general FLRW decoherence formula to pure de Sitter (a(τ) = Ce^{Hτ}) and verify agreement with the known DSW de Sitter result Γ ~ H³q²d²T.

**Requirements covered:** DERV-05, VALD-01, VALD-03

**Key Results (from NR draft Sec. 3):**
- DERV-05 complete: N ≈ q²d²H³T/(96π²) — linear in T, recovers DSW (2022b) ✅

**Remaining steps:**
- VALD-01: Explicit comparison of de Sitter conformal vacuum W with Bunch-Davies (1978)/Allen (1985)
- VALD-03: Explicit identification of T_GH = H/2π (Gibbons-Hawking structure) in de Sitter result

**Depends on:** Phase 2 complete (conformal vacuum); Phase 3 complete (general framework)

---

## Phase 5: Electromagnetic Extension

**Status:** ✅ Complete (NR draft Sec. 6)
**Goal:** Extend the scalar field result to the electromagnetic case — conformally invariant Maxwell field in FLRW in Lorenz gauge.

**Requirements covered:** DERV-06, PAPR-05

**Key Results (from NR draft Sec. 6):**
- Maxwell field is conformally invariant in 4D FLRW; Lorenz gauge preserved under conformal rescaling
- EM decoherence formula: N_EM = 2 × N_scalar (factor of 2 from two transverse polarizations)
- Explicit EM power-law result and de Sitter EM result both stated

**Depends on:** Phase 3 complete

---

## Phase 6: Paper Completion

**Status:** 🔵 Active
**Goal:** Complete the paper manuscript for submission to Physical Review Letters.

**Requirements covered:** PAPR-01, PAPR-06, PAPR-07

**Steps:**
1. Write Introduction (Nishkal) incorporating new results from Phases 3–5
2. Finalize and integrate all sections
3. Write conclusions and discussion — implications, comparison with Killing horizon results, future directions
4. Write appendix validating approximations (dipole, conformal time cutoff, adiabatic turn-on)
5. Run internal review and referee simulation via `/gpd:peer-review`
6. Finalize bibliography

**Success criteria:**
- Complete manuscript ready for submission
- Passes internal peer review
- All sections coherent and self-consistent

**Depends on:** Phases 3, 4, 5 complete

---

## Requirement Traceability Check

| Requirement | Phase | Status |
|-------------|-------|--------|
| DERV-01 | Phase 1 | ✅ Complete |
| DERV-02 | Phase 1 | ✅ Complete |
| DERV-03 | Phase 2 | ✅ Complete |
| DERV-04 | Phase 3 | ✅ Complete (NR draft Sec. 4) |
| DERV-05 | Phase 4 | ✅ Complete (NR draft Sec. 3) |
| DERV-06 | Phase 5 | ✅ Complete (NR draft Sec. 6) |
| VALD-01 | Phase 4 | ⬜ Pending — explicit Bunch-Davies comparison needed |
| VALD-02 | Phase 3 | ⬜ Pending — dimensional check needed |
| VALD-03 | Phase 4 | ⬜ Pending — T_GH identification needed |
| VALD-04 | Phase 3 | ✅ Complete (NR draft Appendix A) |
| PAPR-01 | Phase 6 | ✅ Complete (NR draft Sec. 1) |
| PAPR-02 | Phase 1 | ✅ Complete |
| PAPR-03 | Phase 2 | ✅ Complete |
| PAPR-04 | Phase 3 | ✅ Complete (NR draft Secs. 3–5) |
| PAPR-05 | Phase 5 | ✅ Complete (NR draft Sec. 6) |
| PAPR-06 | Phase 6 | ⬜ Pending — conclusions section |
| PAPR-07 | Phase 6 | ✅ Complete (NR draft Appendices A, B) |

**Coverage:** 17 requirements, 17 mapped, 0 unmapped

---

_Roadmap created: 2026-03-27_
_Last updated: 2026-03-27 after initial definition_

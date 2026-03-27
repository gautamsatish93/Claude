# Requirements: Causal Horizons Decohere Quantum Superpositions

**Defined:** 2026-03-27
**Core Research Question:** Does the presence of a future causal horizon in a general (non-stationary) FLRW spacetime produce a well-defined, finite decoherence rate for a quantum superposition, and does it scale logarithmically with the superposition time T for power-law cosmologies?

## Primary Requirements

### Derivations

- [x] **DERV-01**: Derive the general decoherence formula Γ = q² ∫∫ dτ dτ' ⟨Ψ₀| s^a ∇_a φ^in(τ,X) s^a ∇_a φ^in(τ',X) |Ψ₀⟩ for a superposed charged body in a general curved spacetime (*complete in draft Sec. 2*)
- [x] **DERV-02**: Show that the decoherence measure |⟨Ψ₁|Ψ₂⟩| is independent of the choice of reference source — i.e., the formula is unambiguous (*complete in draft Sec. 2*)
- [x] **DERV-03**: Establish the conformal vacuum 2-point function ⟨φ^in(x₁)φ^in(x₂)⟩ = 1/[4πa(η₁)a(η₂)σ̃_ε(x₁,x₂)] for FLRW via conformal flatness (*complete in draft Sec. 3.2*)
- [x] **DERV-04**: Evaluate the conformal-time integral for Γ for the power-law family a(τ) = C_p(τ−τ*)^p with p > 1 and show Γ scales logarithmically with the superposition time T (*complete in NR draft Sec. 4: Γ ~ (q²d²p³/48π³) × [2T₀²+T(T+2T₀)]/[T₀²(T₀+T)²] × ln(1+T/T₀)*)
- [x] **DERV-05**: Verify the de Sitter specialization (a(τ) = Ce^{Hτ}) of the general formula reproduces the known result Γ ~ H³q²d²T from Danielson et al. (2022b) (*complete in NR draft Sec. 3: N ≈ q²d²H³T/(96π²)*)
- [x] **DERV-06**: Extend the scalar field result to the electromagnetic case (conformally invariant Maxwell field in Lorenz gauge in FLRW) (*complete in NR draft Sec. 6: N_EM = 2 × N_scalar*)

### Validations

- [ ] **VALD-01**: Confirm that the conformal vacuum 2-point function in de Sitter reduces to the known Bunch-Davies Wightman function from the literature
- [ ] **VALD-02**: Verify dimensional consistency of Γ throughout the derivation (Γ must be dimensionless in G = ħ = c = 1 units)
- [ ] **VALD-03**: Check that the de Sitter result encodes the Gibbons-Hawking thermal structure at T_GH = H/2π
- [ ] **VALD-04**: Validate the dipole approximation S₁ − S₂ ~ q d(τ) s^a ∇_a δ³ — confirm validity regime d ≪ horizon scale

### Paper

- [x] **PAPR-01**: Write Introduction (Sec. 1) — framing, motivation, summary of results, and comparison with prior work (*complete in NR draft Sec. 1*)
- [x] **PAPR-02**: Write general framework section (Sec. 2) — decoherence formula in general curved spacetime (*complete in both drafts*)
- [x] **PAPR-03**: Write FLRW geometry and quantization section (Sec. 2.2) — conformal horizon conditions, conformal vacuum (*complete in NR draft Sec. 2.2*)
- [x] **PAPR-04**: Write FLRW decoherence integral section — power-law scale factor result, logarithmic scaling (*complete in NR draft Secs. 3-5*)
- [x] **PAPR-05**: Write EM extension section (*complete in NR draft Sec. 6*)
- [ ] **PAPR-06**: Write conclusions and discussion section (Sec. 5)
- [ ] **PAPR-07**: Write appendix validating approximations and integral relations (Sec. after conclusions)

## Follow-up Requirements

### Extended Analysis (future work)

- **EXTD-01**: Extend to non-conformally invariant fields (gravitational case — soft gravitons) with appropriate IR regularization
- **EXTD-02**: Study decoherence in matter-dominated + Λ (ΛCDM) cosmology — interpolation between power-law and de Sitter regimes
- **EXTD-03**: Investigate quantum geometry corrections (Fahn et al. approach) and compare
- **EXTD-04**: Phenomenological estimates: observable implications for near-term quantum experiments in terrestrial labs and space-based platforms

## Out of Scope

| Topic | Reason |
|-------|--------|
| Soft gravitons / linearized gravity | Non-conformally invariant; requires separate IR regularization; deferred to follow-up |
| Flat-space H → 0 limit as anchor | IR-divergent in flat space; connection subtle; not a primary validation |
| Numerical simulations | Analytic result is achievable and required; numerics not needed |
| Quantum geometry corrections | Requires different framework (Fahn et al.); separate paper |
| Phenomenological estimates for experiments | Secondary to theoretical derivation; deferred |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
|-------------|-----------------|-------------------|
| DERV-04 | Exact closed-form expression for log(T) scaling | Asymptotic analysis of conformal-time integral; comparison with de Sitter limit |
| DERV-05 | Exact match: Γ = C · H³q²d²T from Ref-DSW | Direct substitution a(τ) = Ce^{Hτ} into FLRW formula |
| VALD-01 | Exact agreement with Bunch-Davies Wightman function | Side-by-side comparison with Allen (1985) / Bunch-Davies (1978) |
| VALD-02 | Dimensionless Γ; all intermediate steps consistent | Manual dimensional analysis at each step |
| VALD-03 | Γ contains factor H/(2π) or Planck distribution at T_GH | Identification of thermal factor in de Sitter formula |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark | Prior Inputs | False Progress To Reject |
|-------------|-------------------------------|--------------------|--------------|--------------------------|
| DERV-04 | Closed-form Γ ~ log(T) for power-law FLRW | None (new result); internal consistency | DERV-01,02,03 complete | Dimensional analysis without explicit integral evaluation |
| DERV-05 | Γ ~ H³q²d²T recovered for de Sitter | Ref-DSW (2022b) de Sitter result | DERV-04 | Qualitative agreement without factor matching |
| VALD-01 | Agreement with Bunch-Davies Wightman function | Ref-dS-Wightman (Bunch-Davies 1978, Allen 1985) | DERV-03 | Structural similarity without exact coefficient match |
| VALD-03 | T_GH = H/2π in de Sitter | Ref-GH-thermal (Gibbons-Hawking 1977) | VALD-01 | Dimensional argument only |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DERV-01 | Phase 1: Framework (complete) | Complete |
| DERV-02 | Phase 1: Framework (complete) | Complete |
| DERV-03 | Phase 2: FLRW Quantization (complete) | Complete |
| DERV-04 | Phase 3: Decoherence Integral | ✅ Complete (NR draft) |
| DERV-05 | Phase 4: de Sitter Verification | ✅ Complete (NR draft) |
| DERV-06 | Phase 5: EM Extension | ✅ Complete (NR draft) |
| VALD-01 | Phase 4: de Sitter Verification | Pending — needs explicit comparison |
| VALD-02 | Phase 3: Decoherence Integral | Pending — needs dimensional check |
| VALD-03 | Phase 4: de Sitter Verification | Pending — needs T_GH identification |
| VALD-04 | Phase 3: Decoherence Integral | ✅ Complete (NR draft Appendix A) |
| PAPR-01 | Phase 6: Paper Completion | ✅ Complete (NR draft Sec. 1) |
| PAPR-02 | Phase 1: Framework (complete) | ✅ Complete |
| PAPR-03 | Phase 2: FLRW Quantization (complete) | ✅ Complete |
| PAPR-04 | Phase 3: Decoherence Integral | ✅ Complete (NR draft Secs. 3-5) |
| PAPR-05 | Phase 5: EM Extension | ✅ Complete (NR draft Sec. 6) |
| PAPR-06 | Phase 6: Paper Completion | Pending — conclusions section |
| PAPR-07 | Phase 6: Paper Completion | ✅ Complete (NR draft Appendices A, B) |

**Coverage:**

- Primary requirements: 14 total
- Mapped to phases: 14
- Unmapped: 0

---

_Requirements defined: 2026-03-27_
_Last updated: 2026-03-27 after initial definition_

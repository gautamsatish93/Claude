# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Does the presence of a future causal horizon in a general FLRW spacetime produce a well-defined decoherence rate, and does it scale logarithmically with T for power-law cosmologies?
**Current focus:** Phase 3: Decoherence Integral — Power-Law FLRW

## Current Position

**Current Phase:** 06
**Current Phase Name:** Paper Completion
**Total Phases:** 6
**Current Plan:** —
**Total Plans in Phase:** —
**Status:** Active — VALD-01,02,03 + PAPR-06 remaining
**Last Activity:** 2026-03-27

**Progress:** [████████░░] 83%

## Active Calculations

None yet.

## Intermediate Results

None yet.

## Open Questions

- Precise definition of which radiation crossed the horizon must be made gauge-invariant and operationally clear
- Whether the decoherence exponent admits a fully closed-form expression for general a(t) or only for specific scale factors
- How the observer worldline choice (comoving vs static) affects the result

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| -     | -        | -     | -     |

## Accumulated Context

### Decisions

- [Phase setup]: Conformal vacuum as initial state — Natural in FLRW via conformal flatness; Minkowski vacuum pulled back
- [Phase setup]: Restrict to conformally invariant fields (scalar + EM) — Clean conformal mapping to flat space; gravity much harder and deferred to future work
- [Phase setup]: Power-law FLRW family a(tau)=C_p(tau-tau_*)^p as primary model — Spans broad cosmologies; p>1 gives future causal horizon; analytically tractable

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: mostly-plus
- Fourier convention: int dk/(2pi) e^{ikx} (standard)
- Natural units: G = hbar = c = 1
- Gauge choice: Lorenz gauge for EM: nabla^a A_a = 0
- Regularization scheme: Point-splitting regularization for coincidence limit; iepsilon prescription for distributional 2-point function
- Coordinate system: FLRW: (tau,r,theta,phi) proper time; conformal time t via dt = dtau/a(tau); de Sitter eta = -e^{-H tau}/H
- Index positioning: Abstract index notation: a,b,c,... spacetime; i,j,k,... spatial
- Time ordering: Advanced minus retarded Green function: E(x1,x2) = G_adv(x1,x2) - G_ret(x1,x2)
- Commutation convention: [phi^in(f), phi^in(g)] = i E(f,g) * 1 (field commutator)

### Propagated Uncertainties

None yet.

### Pending Todos

- VALD-01: Explicit comparison of de Sitter conformal vacuum W with Bunch-Davies (1978)/Allen (1985) Wightman function — coefficient match required
- VALD-02: Dimensional analysis of Γ throughout the derivation — confirm dimensionless in G=ħ=c=1 units
- VALD-03: Identify Gibbons-Hawking temperature T_GH = H/2π in de Sitter result N ≈ q²d²H³T/(96π²)
- PAPR-06: Write conclusions and discussion section — summary of results, comparison with Killing horizon (de Sitter), implications, future directions (soft gravitons, ΛCDM, phenomenology)
- Merge GS + NR drafts: GS draft has cleaner framework (Secs 1–3); NR draft has all calculations (Secs 3–6 + appendices)

### Blockers/Concerns

None

## Session Continuity

**Last session:** —
**Stopped at:** —
**Resume file:** —

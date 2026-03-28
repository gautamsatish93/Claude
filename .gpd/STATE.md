# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Does the presence of a future causal horizon in a general FLRW spacetime produce a well-defined decoherence rate, and does it scale logarithmically with T for power-law cosmologies?
**Current focus:** Phase 3: Decoherence Integral — Power-Law FLRW

## Current Position

**Current Phase:** 03
**Current Phase Name:** Decoherence Integral: Power-Law FLRW
**Total Phases:** 6
**Current Plan:** —
**Total Plans in Phase:** —
**Status:** Ready to plan
**Last Activity:** 2026-03-27

**Progress:** [░░░░░░░░░░] 0%

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
- Renormalization scheme: not applicable (no UV divergences in this paper)
- Coordinate system: FLRW: (tau,r,theta,phi) proper time; conformal time t via dt = dtau/a(tau); de Sitter eta = -e^{-H tau}/H
- Spin basis: not applicable (no spinors)
- State normalization: not applicable (no particle states normalized; continuum field conventions follow Wald 1994)
- Coupling convention: not applicable (no gauge coupling constant beyond scalar charge q)
- Index positioning: Abstract index notation: a,b,c,... spacetime; i,j,k,... spatial
- Time ordering: Advanced minus retarded Green function: E(x1,x2) = G_adv(x1,x2) - G_ret(x1,x2)
- Commutation convention: [phi^in(f), phi^in(g)] = i E(f,g) * 1 (field commutator)
- Levi-Civita sign: not applicable (no Levi-Civita tensor in derivations)
- Generator normalization: not applicable (no Lie algebra generators)
- Covariant derivative sign: Christoffel connection: nabla_a v^b = d_a v^b + Gamma^b_{ac} v^c (standard)
- Gamma matrix convention: not applicable (no Dirac equation)
- Creation/annihilation order: not applicable (scalar field; a(f)|0> = 0 defines vacuum)

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None

## Session Continuity

**Last session:** —
**Stopped at:** —
**Resume file:** —

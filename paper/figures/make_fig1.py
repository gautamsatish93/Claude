"""
make_fig1.py
------------
Produce Fig. 1 for the PRD paper: decoherence number N(T) vs superposition
time T for several FLRW spacetimes, normalised to N(T_0).

Output files
    decoherence_vs_time.pdf
    decoherence_vs_time.png
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Matplotlib / LaTeX set-up
# ---------------------------------------------------------------------------
import subprocess, shutil

_use_tex = shutil.which("latex") is not None
matplotlib.rcParams.update({
    "text.usetex": _use_tex,
    "text.latex.preamble": r"\usepackage{amsmath}" if _use_tex else "",
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "pdf.fonttype": 42,   # embeds fonts properly for PRD
    "ps.fonttype": 42,
})

# ---------------------------------------------------------------------------
# Physics functions
# ---------------------------------------------------------------------------
T0 = 1.0          # characteristic time
q2d2 = 1.0        # set q^2 d^2 = 1
H = 1.0           # de Sitter Hubble parameter

T = np.linspace(1e-6, 10.0 * T0, 2000)
Tt = T / T0       # T-tilde = T/T0


def N_powerlaw(T_arr, p, T0=1.0):
    """
    Exact closed-form decoherence number for power-law FLRW, p > 1.

    N(T) = (q^2 d^2 p^3)/(48 pi^3) * [2T0^2 + Tt*(2+Tt)] / [T0^2*(1+Tt)^2]
           * ln(1+Tt)

    where Tt = T/T0.
    """
    prefactor = q2d2 * p**3 / (48.0 * np.pi**3)
    Tt_local = T_arr / T0
    numerator   = 2.0 * T0**2 + Tt_local * (2.0 + Tt_local)
    denominator = T0**2 * (1.0 + Tt_local)**2
    return prefactor * (numerator / denominator) * np.log1p(Tt_local)


def N_p1_nohorizon(T_arr, T0=1.0, N_inf=1.0):
    """
    p = 1 (no causal horizon): saturating model.

    N(T) = N_inf * T^2 / (T0^2 + T^2)
    """
    return N_inf * T_arr**2 / (T0**2 + T_arr**2)


def N_desitter(T_arr, H=1.0):
    """
    De Sitter expansion: N(T) = (q^2 d^2 H^3 T) / (96 pi^2)  [linear in T].
    """
    prefactor = q2d2 * H**3 / (96.0 * np.pi**2)
    return prefactor * T_arr


# ---------------------------------------------------------------------------
# Evaluate and normalise each curve at T = T0
# ---------------------------------------------------------------------------
curves = {}

for p in (2, 3, 5):
    N = N_powerlaw(T, p, T0)
    N0 = N_powerlaw(np.array([T0]), p, T0)[0]
    curves[f"p={p}"] = N / N0

# p = 1  ---  use N_inf = 1 so N(T0) = T0^2/(T0^2+T0^2) = 0.5; normalise
N_p1 = N_p1_nohorizon(T, T0, N_inf=1.0)
N0_p1 = N_p1_nohorizon(np.array([T0]), T0, N_inf=1.0)[0]
curves["p=1"] = N_p1 / N0_p1

# de Sitter
N_dS = N_desitter(T, H)
N0_dS = N_desitter(np.array([T0]), H)[0]
curves["dS"] = N_dS / N0_dS

# ---------------------------------------------------------------------------
# Colorblind-safe palette
# Manually selected from the Bang Wong 2011 palette (Nature Methods)
# compatible with all matplotlib versions.
# ---------------------------------------------------------------------------
color_p1 = "#999999"   # grey
color_p2 = "#0072B2"   # blue
color_p3 = "#E69F00"   # orange/amber
color_p5 = "#009E73"   # green
color_dS = "#D55E00"   # vermillion/red

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3.375, 2.8))

ax.plot(T / T0, curves["p=1"],
        color=color_p1, linestyle="--", linewidth=1.0, zorder=3,
        label=r"$p = 1$ (no horizon)")

ax.plot(T / T0, curves["p=2"],
        color=color_p2, linestyle="-", linewidth=1.0, zorder=4,
        label=r"$p = 2$")

ax.plot(T / T0, curves["p=3"],
        color=color_p3, linestyle="-", linewidth=1.0, zorder=4,
        label=r"$p = 3$")

ax.plot(T / T0, curves["p=5"],
        color=color_p5, linestyle="-", linewidth=1.0, zorder=4,
        label=r"$p = 5$")

ax.plot(T / T0, curves["dS"],
        color=color_dS, linestyle="-", linewidth=1.0, zorder=4,
        label=r"de Sitter (linear)")

# Reference line at T = T0 (normalisation point)
ax.axvline(x=1.0, color="black", linestyle=":", linewidth=0.5, zorder=2,
           alpha=0.5)

ax.set_xlabel(r"$T / T_0$")
ax.set_ylabel(r"$\mathcal{N}(T) \,/\, \mathcal{N}(T_0)$")

ax.set_xlim(0.0, 10.0)
ax.set_ylim(bottom=0.0)

ax.legend(loc="upper left", frameon=False)

fig.tight_layout(pad=0.3)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(out_dir, "decoherence_vs_time.pdf")
png_path = os.path.join(out_dir, "decoherence_vs_time.png")

fig.savefig(pdf_path, dpi=300, bbox_inches="tight")
fig.savefig(png_path, dpi=300, bbox_inches="tight")

print(f"Saved PDF: {pdf_path}")
print(f"Saved PNG: {png_path}")

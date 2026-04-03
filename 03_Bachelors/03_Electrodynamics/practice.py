# ============================================================================
# Electrodynamics (Griffiths level) — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Maxwell's Equations in Vacuum
# ────────────────────────────────────────────────────────────────────────────
#
# Write all four Maxwell equations symbolically using sympy.
# For a plane wave E=E0*sin(kx-ωt), B=B0*sin(kx-ωt):
#   (a) Verify ∇·E=0 and ∇·B=0.
#   (b) Show that ω/k = 1/sqrt(μ0*ε0) = c from Faraday and Ampere.
#
# Hints:
#   → sympy.diff for partial derivatives
#   → Symbolic manipulation to derive the wave equation
#   → Substitute and simplify


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Radiation from an Oscillating Dipole
# ────────────────────────────────────────────────────────────────────────────
#
# Power radiated by oscillating dipole: P = μ0*p0²*ω⁴/(12πc)
#   (a) Compute P for p0=1e-30 C·m at visible light frequency (f=5e14 Hz).
#   (b) Plot radiation pattern: I ∝ sin²(θ) in polar coordinates.
#   (c) Compare radiated power at UV vs IR frequency (factor of (f2/f1)⁴).
#
# Hints:
#   → polar plot: plt.subplot(projection='polar')
#   → θ = np.linspace(0, 2π, 360)
#   → I(θ) = sin(θ)**2, plot as r vs θ


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Fresnel Equations
# ────────────────────────────────────────────────────────────────────────────
#
# At an interface (n1=1 air, n2=1.5 glass) for s and p polarisation:
#   (a) Plot reflectance Rs and Rp vs angle of incidence (0° to 90°).
#   (b) Identify Brewster's angle where Rp=0.
#   (c) Mark total internal reflection angle if it occurs.
#
# Hints:
#   → Fresnel: Rs = |n1cosθi - n2cosθt|² / |n1cosθi + n2cosθt|²
#   → Use Snell's law to find θt from θi
#   → np.degrees(np.arctan(n2/n1)) for Brewster angle


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Skin Depth
# ────────────────────────────────────────────────────────────────────────────
#
# For a conductor (σ=6e7 S/m, copper) at frequencies 1Hz, 1kHz, 1MHz, 1GHz:
# δ = sqrt(2/(μ0*ω*σ))
#   (a) Compute and plot skin depth vs frequency (log-log).
#   (b) Explain why high-frequency signals travel only on the surface.
#
# Hints:
#   → ω = 2π*f
#   → μ0 = 4π*1e-7
#   → plt.loglog(f, delta)


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

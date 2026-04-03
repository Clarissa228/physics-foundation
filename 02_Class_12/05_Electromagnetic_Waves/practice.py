# ============================================================================
# Electromagnetic Waves — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Wave Properties
# ────────────────────────────────────────────────────────────────────────────
#
# An EM wave has frequency f=600 THz (visible light).
#   (a) Find wavelength λ, period T, wave number k, angular frequency ω.
#   (b) Write the E and B field equations.
#   (c) Plot E(x,t) vs x at t=0 for one full wavelength.
#
# Hints:
#   → c = 3e8 m/s, λ = c/f
#   → k = 2π/λ, ω = 2πf
#   → E(x,t) = E0*sin(kx - ωt)
#   → B0 = E0/c


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Intensity and Poynting Vector
# ────────────────────────────────────────────────────────────────────────────
#
# A radio transmitter radiates 100W isotropically.
#   (a) Find intensity I at 1km, 10km, and 100km.
#   (b) Find E_rms at each distance.
#   (c) Plot I vs distance from 0.1km to 100km (log scale).
#
# Hints:
#   → I = P/(4πr²) (inverse square law)
#   → I = ε0*c*E_rms² → E_rms = sqrt(I/(ε0*c))
#   → plt.loglog for the plot


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: EM Spectrum
# ────────────────────────────────────────────────────────────────────────────
#
# Create a visualization of the EM spectrum:
# Plot frequency on x-axis (log scale) from 1Hz to 1e24Hz,
# mark and label: radio, microwave, IR, visible, UV, X-ray, gamma.
# Also mark wavelength on a second x-axis.
#
# Hints:
#   → ax.set_xscale('log')
#   → ax.axvspan(f1, f2, color=...) for each region
#   → ax2 = ax.twiny() for second axis


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Speed of Light from Maxwell
# ────────────────────────────────────────────────────────────────────────────
#
# Maxwell predicted c = 1/sqrt(μ0*ε0).
#   (a) Compute this and compare to 3e8 m/s.
#   (b) Compute refractive index n = c/v for glass (v=2e8 m/s).
#   (c) Derive and plot wavelength in medium vs n for λ0=500nm.
#
# Hints:
#   → μ0 = 4π*1e-7, ε0 = 8.85e-12
#   → λ_medium = λ0/n


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

# ============================================================================
# Dual Nature of Radiation & Matter — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Photoelectric Effect
# ────────────────────────────────────────────────────────────────────────────
#
# Metal work function Φ=4.5eV (e.g. tungsten). Incident photon energy hf.
#   (a) Find threshold frequency.
#   (b) Plot maximum KE vs frequency for f from 0.8*f0 to 3*f0.
#   (c) For f = 2e15 Hz, find stopping potential V0.
#
# Hints:
#   → E = hf, h=6.626e-34 J·s or 4.136e-15 eV·s
#   → KE_max = hf - Φ (only when hf > Φ, else 0)
#   → eV0 = KE_max


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: de Broglie Wavelength
# ────────────────────────────────────────────────────────────────────────────
#
# (a) Compute de Broglie wavelength for: electron at 100eV, proton at 1MeV, cricket ball at 30m/s.
#   (b) Plot λ vs kinetic energy for an electron (1eV to 1keV, log scale).
#
# Hints:
#   → λ = h/p, p = sqrt(2mKE) for non-relativistic
#   → KE in Joules: multiply eV by 1.6e-19
#   → m_electron=9.11e-31, m_proton=1.67e-27


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Heisenberg Uncertainty
# ────────────────────────────────────────────────────────────────────────────
#
# Δx * Δp ≥ ℏ/2
#   (a) An electron is confined to a region Δx=1nm. Find minimum Δp and Δv.
#   (b) Plot Δp_min vs Δx from 0.01nm to 100nm.
#   (c) Estimate the zero-point energy in a box of size Δx.
#
# Hints:
#   → ℏ = 1.055e-34 J·s
#   → Δp_min = ℏ/(2*Δx)
#   → KE_min = Δp²/(2m) as order-of-magnitude estimate


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Wave–Particle Duality
# ────────────────────────────────────────────────────────────────────────────
#
# A double slit experiment with electrons: d=270nm, L=35cm.
# Electrons accelerated through V=54V.
#   (a) Find electron's de Broglie wavelength.
#   (b) Find fringe spacing on screen.
#   (c) Compare to equivalent photon experiment with same λ.
#
# Hints:
#   → λ = h/sqrt(2meV)
#   → Fringe width β = λL/d


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

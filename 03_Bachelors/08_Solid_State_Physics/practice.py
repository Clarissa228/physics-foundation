# ============================================================================
# Solid State Physics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Crystal Lattices
# ────────────────────────────────────────────────────────────────────────────
#
# Plot the following 2D crystal structures with unit cells marked:
#   (a) Square lattice (a=b=1, γ=90°)
#   (b) Hexagonal lattice (a=b=1, γ=120°)
#   (c) Rectangular lattice (a=1, b=1.5, γ=90°)
# Show at least 5×5 lattice points and shade one unit cell.
#
# Hints:
#   → Use plt.scatter for lattice points
#   → Draw unit cell with plt.Polygon
#   → a1 and a2 are lattice vectors


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Bragg Diffraction
# ────────────────────────────────────────────────────────────────────────────
#
# For X-ray diffraction: 2d*sin(θ) = nλ
#   (a) For NaCl (d=2.82Å, λ=1.54Å Cu Kα): find all Bragg angles for n=1,2,3.
#   (b) Plot a simulated diffraction pattern: I vs 2θ (Gaussian peaks at each angle).
#   (c) How does λ affect the resolution of the pattern?
#
# Hints:
#   → np.arcsin(n*lam/(2*d)) for each n
#   → For pattern: I = sum of Gaussians centered at 2*theta_n
#   → np.degrees for conversion


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Free Electron Model DOS
# ────────────────────────────────────────────────────────────────────────────
#
# Density of states for 3D free electron gas:
# g(E) = (V/2π²) * (2m/ℏ²)^(3/2) * sqrt(E)
#   (a) Plot g(E) vs E from 0 to 15 eV.
#   (b) Mark the Fermi energy for copper (E_F=7eV).
#   (c) Compute total number of electrons up to E_F.
#
# Hints:
#   → ℏ = 1.055e-34, m=9.11e-31
#   → Set V=1 m³ for simplicity
#   → N = integral of g(E) from 0 to E_F using np.trapz


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Band Gap and Conductivity
# ────────────────────────────────────────────────────────────────────────────
#
# Simple 1D Kronig–Penney model (conceptual + plot):
#   (a) Plot the nearly-free electron dispersion E(k) showing avoided crossings.
#   (b) Sketch and explain how band gaps arise at the Brillouin zone boundary k=±π/a.
#   (c) Classify metals, semiconductors, insulators by their band structures.
#
# Hints:
#   → Parabolic band E=ℏ²k²/2m, then add small gaps at k=nπ/a
#   → Plot two branches near k=π/a with a gap between them
#   → This is mostly qualitative — show the avoided crossing


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

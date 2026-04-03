# ============================================================================
# Nuclear & Particle Physics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Binding Energy Curve
# ────────────────────────────────────────────────────────────────────────────
#
# Use the semi-empirical Bethe–Weizsäcker formula to plot BE/A vs A (A: 1 to 240).
# Mark: Fe-56 (peak), He-4 (magic number), and show where fusion vs fission is favorable.
#
# Hints:
#   → Use Z ≈ A/2 approximation
#   → a_v=15.5, a_s=16.8, a_c=0.72, a_a=23.0, a_p=12 (MeV)
#   → Pairing term: +a_p/sqrt(A) for even-even, 0 for odd-A, -a_p/sqrt(A) for odd-odd


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Radioactive Decay Chain
# ────────────────────────────────────────────────────────────────────────────
#
# Model the uranium-238 decay chain (simplified: U→Th→Ra→Rn→Po→Pb).
# Solve the Bateman equations using scipy.integrate.solve_ivp.
# Plot N_i(t) for each nuclide over 10 billion years.
#
# Hints:
#   → Half-lives (years): U238=4.47e9, Th234=66e-3, Ra226=1600, Rn222=1.05e-2, Po210=0.38
#   → Coupled ODEs: dN1/dt = -λ1*N1, dN2/dt = λ1*N1 - λ2*N2, ...
#   → Use log scale on y-axis


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Particle Kinematics — Threshold Energy
# ────────────────────────────────────────────────────────────────────────────
#
# For proton-proton collision: p + p → p + p + π0
# Find the threshold kinetic energy of the projectile (target at rest).
#   (a) Use invariant mass: s = (Σp_μ)² is Lorentz invariant.
#   (b) At threshold, all products are at rest in CM frame.
#   (c) Compute threshold KE.
#
# Hints:
#   → m_p = 938.3 MeV/c², m_pi = 135 MeV/c²
#   → s_threshold = (2m_p + m_pi)²*c⁴
#   → s_lab = (2m_p*c²)² + 2*m_p*c²*KE_lab ... equate and solve


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Standard Model Table
# ────────────────────────────────────────────────────────────────────────────
#
# Create a formatted table (as a matplotlib figure or printed text) of:
#   - All 6 quarks: name, symbol, charge, mass
#   - All 6 leptons: name, symbol, charge, mass
#   - Force carrier bosons: name, force, mass
# Colour-code by generation (1st, 2nd, 3rd).
#
# Hints:
#   → Use matplotlib.table or pandas DataFrame
#   → Look up particle data from memory (or PDG values)
#   → This is primarily a data/presentation exercise


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

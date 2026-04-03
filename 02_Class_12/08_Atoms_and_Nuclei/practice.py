# ============================================================================
# Atoms & Nuclei — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Bohr Model
# ────────────────────────────────────────────────────────────────────────────
#
# For hydrogen (Z=1):
#   (a) Calculate energy of levels n=1 to n=6 (in eV): E_n = -13.6/n² eV.
#   (b) Calculate wavelengths of Lyman, Balmer, and Paschen series transitions.
#   (c) Plot an energy level diagram.
#
# Hints:
#   → 1/λ = R_H*(1/n1² - 1/n2²), R_H=1.097e7 m⁻¹
#   → For diagram: plt.axhline at each energy, annotate


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Radioactive Decay
# ────────────────────────────────────────────────────────────────────────────
#
# A sample starts with N0=1e10 atoms. Half-life T½=5.27 years (Co-60).
#   (a) Plot N(t) and activity A(t) = λN(t) over 30 years.
#   (b) Find when N drops to 1% of N0.
#   (c) If three isotopes with T½=1yr, 5yr, 20yr mix — plot total activity.
#
# Hints:
#   → λ = ln(2)/T_half
#   → N(t) = N0*exp(-λt)
#   → t_1pct = -ln(0.01)/λ


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Nuclear Binding Energy
# ────────────────────────────────────────────────────────────────────────────
#
# Use the semi-empirical mass formula (Bethe–Weizsäcker).
# Plot binding energy per nucleon vs mass number A from A=2 to A=238.
# Mark Fe-56 (most stable) and identify fission/fusion regions.
#
# Hints:
#   → BE/A = a_v - a_s*A^(-1/3) - a_c*Z²*A^(-4/3) - a_asym*(A-2Z)²/A²
#   → coefficients: a_v=15.5, a_s=16.8, a_c=0.72, a_asym=23 (MeV)
#   → Z ≈ A/2 as approximation


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Q-value of Nuclear Reaction
# ────────────────────────────────────────────────────────────────────────────
#
# For alpha decay: Ra-226 → Rn-222 + He-4
# Atomic masses: Ra-226=226.025403, Rn-222=222.017571, He-4=4.002602 u
#   (a) Find Q-value in MeV (1u = 931.5 MeV/c²).
#   (b) Find kinetic energy of the alpha particle (by momentum conservation).
#
# Hints:
#   → Q = (m_parent - m_products) * 931.5 MeV
#   → KE_alpha = Q * m_Rn/(m_Rn + m_alpha) (from momentum conservation)


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

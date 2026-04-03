# ============================================================================
# Electrostatics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Coulomb's Law
# ────────────────────────────────────────────────────────────────────────────
#
# Three charges: q1=+2μC at (0,0), q2=-3μC at (4,0)cm, q3=+1μC at (2,3)cm.
#   (a) Find the force on q3 (magnitude and direction).
#   (b) Plot all three charges and draw force vectors.
#
# Hints:
#   → F = kq1q2/r² (Coulomb), k=8.99e9
#   → Decompose into x and y components
#   → plt.quiver for vectors


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Electric Field Lines
# ────────────────────────────────────────────────────────────────────────────
#
# Plot the electric field lines for a dipole: +q at (−d,0) and −q at (+d,0).
# Use a grid of points, compute E at each, and plot streamlines.
#
# Hints:
#   → E_x = k*q*(x-x_q)/r³ summed over charges
#   → plt.streamplot(X, Y, Ex, Ey) draws field lines
#   → np.meshgrid to create the grid


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Gauss's Law — Spherical Shell
# ────────────────────────────────────────────────────────────────────────────
#
# A uniformly charged shell: Q=5μC, R=0.1m.
# Plot E vs r for r from 0 to 0.5m.
# Mark the surface and the discontinuity.
#
# Hints:
#   → For r<R: E=0 (Gauss's law, enclosed charge=0)
#   → For r>R: E=kQ/r²
#   → Use np.where or two separate arrays


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Capacitor Energy
# ────────────────────────────────────────────────────────────────────────────
#
# A parallel-plate capacitor: A=0.01 m², d=1mm, ε0=8.85e-12.
#   (a) Find C, then Q and E for V=100V.
#   (b) Plot energy stored U = CV²/2 vs voltage from 0 to 200V.
#   (c) What happens to U if you double the plate separation?
#
# Hints:
#   → C = ε0*A/d
#   → U = 0.5*C*V²
#   → Think: C halves when d doubles → U changes how?


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

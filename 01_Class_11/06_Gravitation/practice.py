# ============================================================================
# Gravitation — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Gravitational Field
# ────────────────────────────────────────────────────────────────────────────
#
# Compute gravitational field strength g at distances r from Earth's centre.
# Plot g vs r from 0 to 5R_earth (use g=GM/r² for r>=R_earth).
# Mark the surface and indicate where g = 9.81 m/s².
#
# Hints:
#   → G=6.674e-11, M_earth=5.972e24, R_earth=6.371e6
#   → np.linspace, handle r<R_earth separately (inside the Earth)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Orbital Mechanics
# ────────────────────────────────────────────────────────────────────────────
#
# A satellite is in a circular orbit at height 400 km above Earth.
# Find: orbital speed, period, and total mechanical energy.
# Plot the circular orbit in 2D.
#
# Hints:
#   → r = R_earth + h
#   → v = sqrt(GM/r)
#   → T = 2πr/v
#   → E = -GMm/(2r) (total energy)
#   → plt.Circle or parametric plot


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Escape Velocity
# ────────────────────────────────────────────────────────────────────────────
#
# Derive and compute escape velocity from Earth, Moon, and Mars.
# v_esc = sqrt(2GM/R)
# Plot escape velocity as a bar chart for comparison.
#
# Hints:
#   → Look up M and R for Moon and Mars
#   → G = 6.674e-11
#   → plt.bar()


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Kepler's Third Law
# ────────────────────────────────────────────────────────────────────────────
#
# T² ∝ a³ (T = period, a = semi-major axis)
# Given data for solar system planets, verify this by:
#   (a) Plotting T² vs a³ (should be linear)
#   (b) Finding the slope and comparing to 4π²/GM_sun.
#
# Hints:
#   → planet data: T in years, a in AU
#   → Convert to SI or just plot in AU/year units
#   → np.polyfit for the slope


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

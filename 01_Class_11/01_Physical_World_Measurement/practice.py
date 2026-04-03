# ============================================================================
# Physical World & Measurement — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Dimensional Analysis
# ────────────────────────────────────────────────────────────────────────────
#
# The time period T of a simple pendulum depends on its length L and g.
# Use dimensional analysis to derive the formula T = k * sqrt(L/g).
# Show each step of the dimension matching.
#
# Hints:
#   → Use [T]=s, [L]=m, [g]=m/s²
#   → Write T = L^a * g^b and solve for a and b by matching dimensions
#   → The constant k is dimensionless (you cannot find it this way)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Error Propagation
# ────────────────────────────────────────────────────────────────────────────
#
# A cylinder has measured radius r = 3.0 ± 0.1 cm and height h = 8.0 ± 0.2 cm.
# Calculate the volume and its absolute and percentage uncertainty.
# V = π r² h  →  ΔV/V = 2(Δr/r) + (Δh/h)
#
# Hints:
#   → Compute V first
#   → Apply the formula for relative errors
#   → Convert relative error to absolute error at the end


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Monte Carlo Error Estimation
# ────────────────────────────────────────────────────────────────────────────
#
# Simulate 10 000 trials where r and h are drawn from normal distributions
# centered on their measured values with σ = their uncertainties.
# Compute V for each trial and plot the resulting distribution of V.
# Report the mean and standard deviation.
#
# Hints:
#   → np.random.normal(mean, sigma, n_trials)
#   → Compute V = np.pi * r**2 * h element-wise
#   → plt.hist(..., bins=50, edgecolor='k')
#   → np.mean() and np.std() give you the answer


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Significant Figures
# ────────────────────────────────────────────────────────────────────────────
#
# You measure g = 9.81 m/s² and want to report it to 2, 3, and 4 sig figs.
# Write a function round_sig(x, sig) that rounds x to sig significant figures.
# Test it on several values.
#
# Hints:
#   → Use math.floor(math.log10(abs(x))) to find the magnitude
#   → Scale, round, then scale back
#   → Handle x=0 as a special case


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

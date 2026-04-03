# ============================================================================
# Statistical Mechanics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Boltzmann Distribution
# ────────────────────────────────────────────────────────────────────────────
#
# For a two-state system (E=0 and E=ε=0.1eV):
#   (a) Plot probability of each state vs temperature (100K to 5000K).
#   (b) Find the temperature at which both states are equally populated.
#   (c) Compute average energy <E> vs T and find C_V = d<E>/dT.
#
# Hints:
#   → P(E) = exp(-E/kT)/Z, Z = sum of Boltzmann factors
#   → k = 1.38e-23 J/K or 8.617e-5 eV/K
#   → Numerical derivative for C_V using np.gradient


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Partition Function for Ideal Gas
# ────────────────────────────────────────────────────────────────────────────
#
# For a monatomic ideal gas:
#   (a) Write and compute the single-particle partition function z(T,V).
#   (b) Derive average energy <E> = kT² * d(ln Z)/dT.
#   (c) Verify <E> = 3/2 kT per particle.
#
# Hints:
#   → z = V*(2πmkT/h²)^(3/2) (thermal de Broglie)
#   → Compute numerically for Ar (m=40u) at T=300K, V=1L
#   → Compare to 3/2 kT


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Three Statistics Comparison
# ────────────────────────────────────────────────────────────────────────────
#
# Plot occupation number <n> vs energy ε for:
#   - Maxwell-Boltzmann: exp(-ε/kT)
#   - Fermi-Dirac: 1/(exp((ε-μ)/kT)+1)
#   - Bose-Einstein: 1/(exp((ε-μ)/kT)-1)
# at T=300K, μ=0.1eV. Discuss physical differences.
#
# Hints:
#   → ε = np.linspace(0, 1, 500) in eV
#   → Use try/except or np.where to handle Bose-Einstein divergence at ε=μ
#   → All on one plot with legend


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: 2D Ising Model
# ────────────────────────────────────────────────────────────────────────────
#
# Simulate a 20×20 Ising model using Metropolis algorithm:
#   (a) Run at T=1, 2, 2.269 (T_c), 4 in units of J/k.
#   (b) Plot the spin configuration and magnetisation vs temperature.
#   (c) Identify the phase transition.
#
# Hints:
#   → Start with random ±1 spins on a 2D grid
#   → Metropolis: flip spin if ΔE<0, else flip with prob exp(-ΔE/kT)
#   → M = |mean of all spins|
#   → Run 1000 sweeps, average last 500


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

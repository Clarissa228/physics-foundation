# ============================================================================
# Kinetic Theory of Gases — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Maxwell–Boltzmann Speed Distribution
# ────────────────────────────────────────────────────────────────────────────
#
# For nitrogen (M=0.028 kg/mol) at 300K and 600K:
#   (a) Plot the Maxwell-Boltzmann speed distribution f(v) for both temperatures.
#   (b) Mark vmp (most probable), v_avg (mean), and vrms on each curve.
#
# Hints:
#   → f(v) = 4π*(m/2πkT)^(3/2) * v² * exp(-mv²/2kT)
#   → k = 1.38e-23, m = M/N_A
#   → vmp = sqrt(2RT/M), v_avg = sqrt(8RT/πM), vrms = sqrt(3RT/M)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Pressure from Kinetic Theory
# ────────────────────────────────────────────────────────────────────────────
#
# Derive P = (1/3)*ρ*v_rms² and compute pressure for nitrogen
# at ρ=1.2 kg/m³ and T=300K. Compare to the ideal gas law result.
#
# Hints:
#   → v_rms = sqrt(3RT/M)
#   → ρ = PM/(RT) from ideal gas law
#   → Print both values and the percentage difference


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Mean Free Path
# ────────────────────────────────────────────────────────────────────────────
#
# For nitrogen at STP (T=273K, P=101325 Pa), diameter d=3.7e-10 m:
# λ = 1/(√2 * π * d² * n)
# Find n from ideal gas law, then compute λ. Plot λ vs pressure.
#
# Hints:
#   → n = P/(kT)
#   → np.linspace for P range
#   → plt.semilogy may be clearer


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Equipartition Theorem
# ────────────────────────────────────────────────────────────────────────────
#
# Compute Cv, Cp, and γ for:
#   - Monatomic gas (3 translational DOF)
#   - Diatomic gas at room temp (5 DOF)
#   - Diatomic gas at high temp (7 DOF)
# Print a comparison table.
#
# Hints:
#   → Cv = (f/2)*R where f = degrees of freedom
#   → Cp = Cv + R
#   → γ = Cp/Cv


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

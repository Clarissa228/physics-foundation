# ============================================================================
# Quantum Mechanics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Infinite Square Well
# ────────────────────────────────────────────────────────────────────────────
#
# Particle in a box of length L=1nm.
#   (a) Write wavefunctions ψ_n(x) = sqrt(2/L)*sin(nπx/L) for n=1,2,3,4.
#   (b) Plot each ψ_n and |ψ_n|² on the same figure.
#   (c) Compute energy eigenvalues E_n = n²π²ℏ²/(2mL²) in eV.
#
# Hints:
#   → ℏ = 1.055e-34 J·s, m = 9.11e-31 kg
#   → np.linspace(0, L, 500) for x
#   → Subplots(4, 2): left=ψ, right=|ψ|²


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Quantum Harmonic Oscillator
# ────────────────────────────────────────────────────────────────────────────
#
# Using Hermite polynomials and the QHO wavefunctions:
#   (a) Plot ψ_n for n=0,1,2,3 (use scipy.special.hermite).
#   (b) Overlay the classical turning points on each plot.
#   (c) Show |ψ|² for large n approaches the classical probability distribution.
#
# Hints:
#   → ψ_n = H_n(ξ)*exp(-ξ²/2), ξ = x*sqrt(mω/ℏ)
#   → scipy.special.hermite(n) returns Hermite polynomial
#   → Classical turning points: where E = V(x) = ½mω²x²


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Tunneling Through a Barrier
# ────────────────────────────────────────────────────────────────────────────
#
# Transmission coefficient T for a rectangular barrier (V0, width a):
# T ≈ exp(-2κa) where κ = sqrt(2m(V0-E))/ℏ
#   (a) Plot T vs incident energy E (0 to V0) for V0=5eV, a=0.5nm.
#   (b) Plot T vs barrier width a (0.1nm to 2nm) at E=2.5eV.
#   (c) Discuss implications for alpha decay and STM.
#
# Hints:
#   → Only valid for E<V0 (tunneling regime)
#   → κ = sqrt(2*m*(V0-E))/hbar
#   → T = exp(-2*kappa*a)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Expectation Values
# ────────────────────────────────────────────────────────────────────────────
#
# For ψ(x) = sqrt(2/L)*sin(πx/L) (ground state, box of L=1nm):
#   (a) Compute <x>, <x²>, and Δx = sqrt(<x²>-<x>²) numerically.
#   (b) Compute <p> and <p²> using the momentum operator p = -iℏ d/dx.
#   (c) Verify the uncertainty principle ΔxΔp ≥ ℏ/2.
#
# Hints:
#   → Use np.trapz for numerical integration
#   → Numerical derivative for d/dx ψ: np.gradient(psi, x)
#   → <p²> = ∫ ψ* (-ℏ² d²ψ/dx²) dx


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

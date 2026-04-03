# ============================================================================
# Mathematical Methods for Physics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Vector Calculus
# ────────────────────────────────────────────────────────────────────────────
#
# For F = (x²y, xy², xyz):
#   (a) Compute div F and curl F analytically.
#   (b) Verify numerically at point (1, 2, 3) using finite differences.
#   (c) Visualise F in the xy-plane (z=0) as a quiver plot.
#
# Hints:
#   → Use sympy symbols x,y,z and diff()
#   → Numerical: (F(x+h)-F(x-h))/(2h)
#   → np.meshgrid and plt.quiver for visualisation


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Fourier Series
# ────────────────────────────────────────────────────────────────────────────
#
# Approximate a square wave f(x) = +1 for 0<x<π, -1 for π<x<2π
# using N terms of its Fourier series.
#   (a) Derive the coefficients (odd harmonics only).
#   (b) Plot partial sums for N=1,3,5,11 and observe Gibbs phenomenon.
#
# Hints:
#   → b_n = (2/π) * integral(f*sin(nx)) = 4/(nπ) for odd n
#   → f_N(x) = Σ b_n * sin(nx)
#   → Use subplot grid or overlay all on one plot


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Ordinary Differential Equations
# ────────────────────────────────────────────────────────────────────────────
#
# Solve the damped harmonic oscillator ODE:
# m*x'' + b*x' + k*x = F0*cos(ωt) (driven oscillator)
#   (a) Solve numerically with scipy.integrate.solve_ivp.
#   (b) Find the steady-state amplitude vs ω (resonance curve).
#   (c) Compare underdamped, critically damped, overdamped cases.
#
# Hints:
#   → Convert to first-order system: [x, v]
#   → scipy.integrate.solve_ivp(fun, t_span, y0)
#   → Sweep ω and record steady-state amplitude


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Eigenvalue Problems
# ────────────────────────────────────────────────────────────────────────────
#
# Find eigenvalues and eigenvectors of:
#   A = [[4,1],[2,3]] using numpy.
#   (a) Verify A*v = λ*v for each pair.
#   (b) Interpret physically (principal axes of inertia).
#   (c) Diagonalise A: write A = P D P⁻¹.
#
# Hints:
#   → np.linalg.eig(A)
#   → np.dot, np.linalg.inv
#   → D = diag(eigenvalues), P = column matrix of eigenvectors


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

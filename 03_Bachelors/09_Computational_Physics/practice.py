# ============================================================================
# Computational Physics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Numerical Integration
# ────────────────────────────────────────────────────────────────────────────
#
# Compute ∫₀^π sin(x) dx using:
#   (a) Rectangle rule
#   (b) Trapezoid rule
#   (c) Simpson's rule
#   (d) scipy.integrate.quad
# Plot error vs number of intervals N for each method on a log-log graph.
#
# Hints:
#   → Exact value = 2.0
#   → Error = |numerical - exact|
#   → Try N = 4, 8, 16, 32, 64, 128
#   → scipy.integrate.quad(np.sin, 0, np.pi)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: ODE Integration Methods
# ────────────────────────────────────────────────────────────────────────────
#
# Solve the simple pendulum ODE numerically:
# θ'' + (g/L)sin(θ) = 0
# Compare:
#   (a) Euler method (your implementation)
#   (b) RK4 method (your implementation)
#   (c) scipy.integrate.solve_ivp
# Plot energy conservation error vs time for each method.
#
# Hints:
#   → Convert to system: [θ, ω], dω/dt = -(g/L)*sin(θ)
#   → Energy E = ½mL²ω² + mgL(1-cosθ) should be constant
#   → Plot (E(t)-E(0))/E(0) for each method


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Monte Carlo Integration
# ────────────────────────────────────────────────────────────────────────────
#
# Estimate π using Monte Carlo: throw darts at a unit circle.
#   (a) For N=100, 1000, 10000, 100000: estimate π and plot convergence.
#   (b) Plot error vs N on log-log — verify O(1/sqrt(N)) convergence.
#   (c) Use the same technique to estimate the volume of a unit sphere in 3D.
#
# Hints:
#   → Points inside circle: x²+y²≤1
#   → π ≈ 4 * (points inside) / N
#   → For sphere: x²+y²+z²≤1, volume ≈ 8 * (inside) / N


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: FFT and Signal Analysis
# ────────────────────────────────────────────────────────────────────────────
#
# Generate a signal: s(t) = sin(2π*60t) + 0.5*sin(2π*150t) + noise.
#   (a) Plot the time-domain signal.
#   (b) Compute FFT and plot the frequency spectrum.
#   (c) Apply a low-pass filter (zero out frequencies > 100Hz) and plot the cleaned signal.
#
# Hints:
#   → t = np.linspace(0, 1, 1000) (1 second at 1kHz)
#   → np.fft.fft(s) for FFT, np.fft.fftfreq(N, 1/fs) for frequencies
#   → Filter: set FFT coefficients to zero above cutoff, then np.fft.ifft


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

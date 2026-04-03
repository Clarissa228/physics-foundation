# ============================================================================
# Oscillations & Waves — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Simple Harmonic Motion
# ────────────────────────────────────────────────────────────────────────────
#
# A mass–spring system: m=0.5 kg, k=8 N/m, x0=0.1 m, v0=0.
#   (a) Find ω, f, T, and amplitude.
#   (b) Plot x(t), v(t), a(t) over 3 periods on subplots.
#   (c) Plot KE, PE, and total E vs time.
#
# Hints:
#   → ω = sqrt(k/m)
#   → x(t) = A*cos(ωt + φ)
#   → KE = 0.5*m*v², PE = 0.5*k*x²


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Damped Oscillation
# ────────────────────────────────────────────────────────────────────────────
#
# Add damping: b=0.4 kg/s to the above system.
# x(t) = A*e^(-bt/2m) * cos(ω_d*t) where ω_d = sqrt(ω0²-(b/2m)²)
#   (a) Plot damped vs undamped on same graph.
#   (b) Find the time for amplitude to fall to 1/e of initial.
#
# Hints:
#   → Compute ω_d first and check it's real (underdamped)
#   → Envelope: A*exp(-b*t/(2*m))
#   → Find crossing with 1/e numerically


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Standing Waves
# ────────────────────────────────────────────────────────────────────────────
#
# A string of length L=1m is fixed at both ends.
#   (a) Find wavelengths and frequencies for modes n=1,2,3,4 (wave speed v=50 m/s).
#   (b) Plot the first 4 standing wave patterns at t=0.
#
# Hints:
#   → λ_n = 2L/n, f_n = v/λ_n
#   → y_n(x) = sin(nπx/L)
#   → Use subplots(4,1,...)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Beats
# ────────────────────────────────────────────────────────────────────────────
#
# Two tuning forks: f1=440 Hz, f2=444 Hz.
#   (a) Plot the superposition y1+y2 over 0.5 seconds.
#   (b) Identify the beat frequency from the plot.
#   (c) Plot the envelope.
#
# Hints:
#   → Use np.linspace(0, 0.5, 44100) for good resolution
#   → y = cos(2πf1*t) + cos(2πf2*t)
#   → Envelope: 2*cos(2π*(f2-f1)/2 * t)


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

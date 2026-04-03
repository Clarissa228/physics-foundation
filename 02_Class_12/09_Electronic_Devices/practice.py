# ============================================================================
# Electronic Devices & Semiconductors — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Diode I–V Characteristic
# ────────────────────────────────────────────────────────────────────────────
#
# Shockley equation: I = I0*(exp(qV/kT) - 1), I0=1e-10A, T=300K.
#   (a) Plot I vs V from -1V to 0.8V.
#   (b) Find forward voltage at I=10mA.
#   (c) Zoom in on the reverse saturation region.
#
# Hints:
#   → q=1.6e-19, k=1.38e-23
#   → Forward bias: V>0 gives exponential growth
#   → Use two subplots for forward and reverse


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Half-Wave Rectifier
# ────────────────────────────────────────────────────────────────────────────
#
# Input: V_in(t) = 5*sin(2π*50*t).
#   (a) Plot V_in and V_out (V_out = V_in if V_in>0, else 0) vs time.
#   (b) Compute average and rms of V_out.
#   (c) Show how a capacitor C smooths the output.
#
# Hints:
#   → t = np.linspace(0, 0.04, 1000)
#   → V_out = np.where(V_in > 0, V_in, 0)
#   → V_avg = np.mean(V_out), V_rms = np.sqrt(np.mean(V_out**2))


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Transistor as Amplifier (conceptual)
# ────────────────────────────────────────────────────────────────────────────
#
# For a common-emitter amplifier: β=100, R_C=1kΩ, V_CC=12V.
#   (a) If I_B=0.05mA, find I_C and V_CE.
#   (b) Plot output characteristics: I_C vs V_CE for I_B = 0, 20, 40, 60, 80 μA.
#   (c) Mark the saturation and active regions.
#
# Hints:
#   → I_C = β*I_B
#   → V_CE = V_CC - I_C*R_C
#   → Saturation when V_CE < ~0.2V


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Logic Gates Truth Table
# ────────────────────────────────────────────────────────────────────────────
#
# Implement AND, OR, NOT, NAND, NOR, XOR as Python functions.
# Print the full truth table for all gates for inputs (0,0),(0,1),(1,0),(1,1).
# Verify: NAND is universal — build AND and OR from only NANDs.
#
# Hints:
#   → Simple Python: and_gate = lambda a,b: int(a and b)
#   → For NAND-only: recall that NOT A = NAND(A,A)


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

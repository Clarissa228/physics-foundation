# ============================================================================
# Current Electricity — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Ohm's Law and Resistance
# ────────────────────────────────────────────────────────────────────────────
#
# A nichrome wire: resistivity ρ=1.1e-6 Ω·m, length L=2m, diameter 0.5mm.
#   (a) Find resistance R.
#   (b) Plot I vs V from 0 to 12V (I-V characteristic).
#   (c) At what voltage does it dissipate 10W?
#
# Hints:
#   → R = ρ*L/A, A = π*(d/2)²
#   → I = V/R
#   → P = V²/R → V = sqrt(P*R)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Kirchhoff's Laws
# ────────────────────────────────────────────────────────────────────────────
#
# In a circuit: E1=12V with r1=1Ω, E2=6V with r2=0.5Ω, R=4Ω all in a loop.
# Use KVL to write the equation and solve for current I.
# Then find voltage across each element.
#
# Hints:
#   → KVL: sum of EMFs = sum of voltage drops around loop
#   → I = (E1 - E2)/(R + r1 + r2) for a simple series loop
#   → Check by summing voltages


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: RC Circuit Charging
# ────────────────────────────────────────────────────────────────────────────
#
# R=10kΩ, C=100μF, V_battery=9V. At t=0 switch closes.
#   (a) Plot V_C(t) and I(t) for 0 to 5τ.
#   (b) Mark the time constant τ=RC on the graph.
#   (c) What is the energy stored in C when fully charged?
#
# Hints:
#   → V_C(t) = V*(1 - exp(-t/RC))
#   → I(t) = (V/R)*exp(-t/RC)
#   → τ = R*C
#   → U = 0.5*C*V²


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Power and Heating
# ────────────────────────────────────────────────────────────────────────────
#
# A toaster draws 1200W from a 240V supply.
#   (a) Find current and resistance.
#   (b) Energy used in 5 minutes in Joules and kWh.
#   (c) Plot power dissipated vs resistance for a fixed 240V supply (R: 10Ω to 500Ω).
#
# Hints:
#   → P = V²/R = I²R = IV
#   → E = P*t


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

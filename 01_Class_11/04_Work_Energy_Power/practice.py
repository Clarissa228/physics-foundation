# ============================================================================
# Work, Energy & Power — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Work–Energy Theorem
# ────────────────────────────────────────────────────────────────────────────
#
# A 2 kg block slides 5 m down a frictionless 30° ramp.
#   (a) Calculate work done by gravity and by the normal force.
#   (b) Find speed at the bottom using the work-energy theorem.
#   (c) Verify using kinematics.
#
# Hints:
#   → W = F·d·cos(angle between force and displacement)
#   → Normal force is perpendicular to motion → W_N = 0
#   → W_net = ΔKE = ½mv² - 0


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Energy Conservation with Friction
# ────────────────────────────────────────────────────────────────────────────
#
# A 1 kg ball is dropped from height h = 10 m and bounces.
# Each bounce loses 20% of kinetic energy at impact.
# Simulate 5 bounces: plot height vs time.
#
# Hints:
#   → Between bounces: h(t) using SUVAT
#   → At each bounce: v_after = sqrt(0.8) * v_before
#   → Concatenate time arrays for each bounce


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Spring Potential Energy
# ────────────────────────────────────────────────────────────────────────────
#
# A spring (k = 200 N/m) is compressed by x = 0.15 m and launches a 0.3 kg ball.
# Find the launch speed. Then plot KE, PE_spring, and total E vs compression x
# from 0 to 0.2 m to show energy conservation.
#
# Hints:
#   → PE_spring = 0.5*k*x²
#   → At launch: all PE → KE, so ½mv² = ½kx²
#   → Plot all three on one graph


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Power
# ────────────────────────────────────────────────────────────────────────────
#
# A motor lifts a 500 kg load at constant speed:
#   (a) At 0.5 m/s — what power is needed?
#   (b) At 2 m/s?
#   (c) The motor is rated at 5 kW. What is the maximum lifting speed?
#   (d) Plot power vs speed from 0 to 3 m/s.
#
# Hints:
#   → P = F*v = mg*v (constant speed means F = mg)
#   → Max speed when P = P_rated


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

# ============================================================================
# System of Particles & Rigid Body — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Centre of Mass
# ────────────────────────────────────────────────────────────────────────────
#
# Three masses: m1=1kg at (0,0), m2=2kg at (3,0), m3=3kg at (1.5,2).
# Find the centre of mass (x_cm, y_cm).
# Plot all masses and the CM on a scatter plot.
#
# Hints:
#   → x_cm = Σ(mi*xi)/Σmi
#   → Use plt.scatter with different sizes for masses


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Moment of Inertia
# ────────────────────────────────────────────────────────────────────────────
#
# Calculate moment of inertia of a uniform rod (M, L) about:
#   (a) its centre: I = ML²/12
#   (b) one end: I = ML²/3
# Verify the parallel-axis theorem: I_end = I_cm + M*(L/2)².
#
# Hints:
#   → Just plug in values and verify numerically
#   → Print each value and the comparison


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Torque and Angular Acceleration
# ────────────────────────────────────────────────────────────────────────────
#
# A solid disk (M=2kg, R=0.3m) is subject to torque τ=5 N·m.
#   (a) Find I = ½MR²
#   (b) Find angular acceleration α = τ/I
#   (c) Plot angular velocity ω(t) = α*t and angle θ(t) over 5 s.
#
# Hints:
#   → α = τ/I
#   → ω(t) and θ(t) like v(t) and x(t) in linear motion


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Rolling Without Slipping
# ────────────────────────────────────────────────────────────────────────────
#
# A solid sphere (M, R) rolls down a ramp of angle θ=20° and height h=2m.
# Using energy conservation (KE_trans + KE_rot = mgh):
# Find the speed at the bottom. Compare with a hollow sphere and a cylinder.
#
# Hints:
#   → I_solid_sphere = 2/5 MR², I_hollow_sphere = 2/3 MR², I_cylinder = 1/2 MR²
#   → v² = 2gh / (1 + I/(MR²))
#   → Print a table comparing the three


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

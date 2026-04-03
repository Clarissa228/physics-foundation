# ============================================================================
# Kinematics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: SUVAT Equations
# ────────────────────────────────────────────────────────────────────────────
#
# A ball is thrown upward at 20 m/s from height 0.
# Using SUVAT (s, u, v, a, t), find:
#   (a) Time to reach maximum height
#   (b) Maximum height reached
#   (c) Time to return to ground
#   (d) Speed on impact
# Then plot height vs time for the full trajectory.
#
# Hints:
#   → g = -9.81 m/s² (upward positive)
#   → v = u + at to find time at peak
#   → s = ut + 0.5*a*t² for height
#   → Use np.linspace for the time array


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Relative Motion
# ────────────────────────────────────────────────────────────────────────────
#
# Train A moves east at 60 km/h. Train B moves west at 80 km/h.
# They start 300 km apart. When and where do they meet?
# Plot both trains' positions vs time on the same graph.
#
# Hints:
#   → Set up position functions: x_A(t) = 60t, x_B(t) = 300 - 80t
#   → Solve x_A = x_B
#   → Animate with plt.plot updating in a loop (optional)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: 2D Projectile
# ────────────────────────────────────────────────────────────────────────────
#
# A ball is launched at angle θ = 37° with speed 25 m/s.
# Plot the full trajectory. Mark the highest point and landing point.
# Also plot range vs angle from 0° to 90° and find the optimal angle.
#
# Hints:
#   → Decompose into vx = v*cos(θ), vy = v*sin(θ)
#   → x(t) = vx*t, y(t) = vy*t - 0.5*g*t²
#   → Landing when y=0 → solve for t_land
#   → Loop over angles for the range plot


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Velocity & Acceleration from Position
# ────────────────────────────────────────────────────────────────────────────
#
# Given position data: x = [0, 1, 4, 9, 16, 25] at t = [0,1,2,3,4,5] s,
# estimate velocity and acceleration using finite differences.
# Compare to the analytical values for x = t².
#
# Hints:
#   → np.diff(x)/np.diff(t) gives velocity at midpoints
#   → Apply np.diff again for acceleration
#   → plt.plot both numerical and analytical on same axes


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

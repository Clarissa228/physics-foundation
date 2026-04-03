# ============================================================================
# Optics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Snell's Law and Critical Angle
# ────────────────────────────────────────────────────────────────────────────
#
# (a) Write a function snell(n1, theta1_deg, n2) → theta2_deg.
#   (b) Plot refraction angle vs incident angle (0° to 89°) for air→glass (n=1.5).
#   (c) For glass→air, find the critical angle for total internal reflection.
#
# Hints:
#   → np.arcsin, np.degrees, np.radians
#   → Critical angle: theta1 where theta2 = 90° → sin(theta_c) = n2/n1


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Lens Formula
# ────────────────────────────────────────────────────────────────────────────
#
# Use 1/f = 1/v - 1/u (sign convention: real is positive).
# For a convex lens f=15cm:
#   (a) Find image position for objects at u = -30, -20, -10 cm.
#   (b) Plot image distance v vs object distance u from -100cm to -f-1.
#   (c) Compute magnification m = -v/u for each case.
#
# Hints:
#   → 1/v = 1/f + 1/u
#   → Negative u = real object on left


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Young's Double Slit
# ────────────────────────────────────────────────────────────────────────────
#
# d=0.5mm, λ=600nm, L=1.5m.
#   (a) Plot intensity I = I0*cos²(πdy/(λL)) vs y on screen (y: -5mm to 5mm).
#   (b) Calculate fringe width β = λL/d.
#   (c) How does the pattern change if d is doubled?
#
# Hints:
#   → np.cos, np.linspace for y
#   → Mark fringe positions with vertical lines


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Single Slit Diffraction
# ────────────────────────────────────────────────────────────────────────────
#
# Slit width a=0.1mm, λ=500nm, L=1m.
# Intensity: I = I0*(sin(α)/α)² where α = π*a*sin(θ)/λ ≈ π*a*y/(λL)
#   (a) Plot I vs y from -5mm to 5mm.
#   (b) Find positions of first 3 minima.
#   (c) Overlay on the double-slit pattern (with same d) to show envelope effect.
#
# Hints:
#   → Handle α→0 with np.sinc(α/π) or np.where(α==0, 1, sin(α)/α)
#   → Minima at α = mπ → y = m*λL/a


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

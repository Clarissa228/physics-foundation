# ============================================================================
# Properties of Bulk Matter — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Stress–Strain Curve
# ────────────────────────────────────────────────────────────────────────────
#
# Simulate loading of a steel wire:
#   Young's modulus E = 200 GPa, cross-section A = 1 mm², length L = 2 m.
#   (a) Plot stress vs strain up to 0.1% strain.
#   (b) Calculate the extension for a 1000 N load.
#
# Hints:
#   → stress = F/A, strain = ΔL/L
#   → stress = E * strain
#   → extension = F*L/(A*E)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Buoyancy
# ────────────────────────────────────────────────────────────────────────────
#
# A wooden block (density 600 kg/m³, volume 0.01 m³) floats in water.
#   (a) What fraction is submerged?
#   (b) If a 2 kg mass is placed on top, how deep does it sink?
#   (c) At what added mass does it just sink?
#
# Hints:
#   → Buoyancy = weight of displaced water = ρ_water * V_submerged * g
#   → Equilibrium: buoyancy = total weight
#   → For (c): V_submerged = total volume → solve for added mass


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Viscosity and Stokes' Law
# ────────────────────────────────────────────────────────────────────────────
#
# A steel ball (r=1mm, ρ=7800 kg/m³) falls through glycerine (η=1.5 Pa·s).
# Stokes drag: F_drag = 6πηrv
# Find terminal velocity numerically by simulating the fall until a≈0.
#
# Hints:
#   → Use Euler integration: v += (F_net/m)*dt
#   → F_net = mg - buoyancy - 6πηrv
#   → Plot v vs time and mark terminal velocity


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Surface Tension — Capillary Rise
# ────────────────────────────────────────────────────────────────────────────
#
# Water (γ=0.0728 N/m, contact angle θ=0°, ρ=1000 kg/m³) rises in a
# capillary tube. h = 2γcosθ/(ρgr)
# Plot height h vs tube radius r from 0.01 mm to 1 mm.
#
# Hints:
#   → np.linspace for r
#   → Keep units consistent (SI)
#   → plt.semilogx may look nicer


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

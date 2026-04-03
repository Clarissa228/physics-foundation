# ============================================================================
# Classical Mechanics (Lagrangian & Hamiltonian) — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Lagrangian of Simple Systems
# ────────────────────────────────────────────────────────────────────────────
#
# Write the Lagrangian L = T - V for:
#   (a) Simple pendulum (angle θ, length l)
#   (b) Double pendulum (angles θ1, θ2)
#   (c) Particle sliding on a frictionless incline
# Derive the equation of motion for (a) using sympy.
#
# Hints:
#   → T = ½ml²θ̇² for pendulum
#   → Use sympy.Function('theta')(t) and sympy.diff
#   → Euler-Lagrange: d/dt(∂L/∂θ̇) - ∂L/∂θ = 0


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Double Pendulum Simulation
# ────────────────────────────────────────────────────────────────────────────
#
# Simulate the double pendulum (equal masses and lengths).
#   (a) Integrate the equations of motion using solve_ivp.
#   (b) Plot both angles vs time.
#   (c) Show sensitivity to initial conditions: run two sims with θ1 differing by 0.001°.
#
# Hints:
#   → Look up the equations of motion for the double pendulum
#   → scipy.integrate.solve_ivp with 'RK45' method
#   → Small difference in IC leads to wildly different trajectories (chaos)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Phase Space and Conservation
# ────────────────────────────────────────────────────────────────────────────
#
# For the simple pendulum, plot phase space (θ vs ω) for:
#   (a) Small oscillations (ellipses)
#   (b) Large oscillations (deformed)
#   (c) Enough energy to go over the top (open curves)
# Colour-code trajectories by total energy.
#
# Hints:
#   → Integrate ODE for multiple initial conditions
#   → plt.plot(theta, omega) for each trajectory
#   → E = ½ml²ω² + mgl(1-cosθ)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Noether's Theorem (conceptual + computational)
# ────────────────────────────────────────────────────────────────────────────
#
# For a central force F(r) (e.g. gravity):
#   (a) Simulate a planet's orbit numerically.
#   (b) Track angular momentum L = r × p at each timestep.
#   (c) Show L is conserved (plot L vs time, should be flat).
#
# Hints:
#   → Use RK4 or solve_ivp for dr/dt=v, dv/dt=F/m
#   → L = x*vy - y*vx for 2D motion
#   → Plot relative deviation (L - L0)/L0 vs time


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

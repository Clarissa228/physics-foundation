# ============================================================================
# Magnetic Effects & Magnetism — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Magnetic Force on a Charge
# ────────────────────────────────────────────────────────────────────────────
#
# A proton (q=1.6e-19 C, m=1.67e-27 kg) enters a magnetic field B=0.5T (in z-dir)
# with velocity v=1e6 m/s in the x-direction.
#   (a) Find the magnetic force F = qv × B.
#   (b) Find the radius of circular motion.
#   (c) Plot the circular path.
#
# Hints:
#   → F = q*v*B (perpendicular to both v and B)
#   → r = mv/(qB)
#   → x = r*cos(θ), y = r*sin(θ)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Biot–Savart: Long Straight Wire
# ────────────────────────────────────────────────────────────────────────────
#
# A long wire carries I=10A. Plot B vs distance r from 1cm to 20cm.
# B = μ0*I/(2π*r)
#
# Hints:
#   → μ0 = 4π*1e-7 T·m/A
#   → np.linspace for r
#   → plt.semilogx


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Solenoid Field
# ────────────────────────────────────────────────────────────────────────────
#
# A solenoid: n=500 turns/m, I=2A.
#   (a) Find B inside using B = μ0*n*I.
#   (b) Plot B along the axis of a finite solenoid (use superposition of circular loops).
#      Use B_loop = μ0*I*R²/(2*(R²+x²)^(3/2)) for each loop.
#
# Hints:
#   → Sum contributions from N loops spaced L/N apart
#   → R=0.05m, N=100 loops, L=0.2m
#   → Plot shows field is uniform in the middle


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Force Between Two Wires
# ────────────────────────────────────────────────────────────────────────────
#
# Two parallel wires 0.1m apart carry I1=5A and I2=8A.
#   (a) Force per unit length: F/L = μ0*I1*I2/(2π*d)
#   (b) Are the currents in the same or opposite direction? Plot both cases.
#   (c) Plot F/L vs separation d from 1cm to 50cm.
#
# Hints:
#   → Same direction → attractive, opposite → repulsive
#   → np.linspace for d


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

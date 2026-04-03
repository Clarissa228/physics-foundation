# ============================================================================
# Thermodynamics — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Ideal Gas Law
# ────────────────────────────────────────────────────────────────────────────
#
# 1 mole of ideal gas at 300 K occupies what volume at 1 atm?
# Plot P vs V at constant T (isothermal) for T = 200K, 300K, 400K on one graph.
#
# Hints:
#   → PV = nRT, R = 8.314 J/(mol·K)
#   → P = nRT/V
#   → np.linspace for V


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Thermodynamic Processes
# ────────────────────────────────────────────────────────────────────────────
#
# For 1 mol of ideal gas (γ = 5/3 for monatomic):
#   (a) Isothermal: expand from V1=10L to V2=30L at T=300K. Find W, Q, ΔU.
#   (b) Adiabatic: same expansion. Find T2, W, Q, ΔU.
#   (c) Isobaric: heat at P=1 atm from T1=300K to T2=500K. Find W, Q, ΔU.
#
# Hints:
#   → W_iso = nRT*ln(V2/V1)
#   → Adiabatic: TV^(γ-1)=const, W = (P1V1-P2V2)/(γ-1)
#   → Isobaric: W = PΔV, Q = nCpΔT, Cp = 5/2 R for monatomic


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Carnot Efficiency
# ────────────────────────────────────────────────────────────────────────────
#
# A heat engine operates between Th=500K and Tc=300K.
#   (a) Maximum (Carnot) efficiency?
#   (b) Plot Carnot efficiency vs Tc from 100K to 490K (fixed Th=500K).
#   (c) For Q_in=1000J, how much work and waste heat?
#
# Hints:
#   → η_carnot = 1 - Tc/Th
#   → W = η*Q_in, Q_c = Q_in - W


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Entropy
# ────────────────────────────────────────────────────────────────────────────
#
# Calculate entropy change for:
#   (a) 1 kg water heated from 20°C to 100°C (cp = 4186 J/kg·K)
#   (b) 1 kg water evaporating at 100°C (L_vap = 2.26e6 J/kg)
#   (c) Plot dS vs T for the heating process.
#
# Hints:
#   → dS = dQ/T = m*cp*dT/T
#   → Integrate: ΔS = m*cp*ln(T2/T1)
#   → For phase change: ΔS = Q/T = m*L/T


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

# ============================================================================
# Special & General Relativity — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Lorentz Factor
# ────────────────────────────────────────────────────────────────────────────
#
# (a) Plot γ = 1/sqrt(1-v²/c²) vs v/c from 0 to 0.9999.
#   (b) Find v where γ=2,5,10,100.
#   (c) Plot γ on a log scale and discuss what happens as v→c.
#
# Hints:
#   → v_over_c = np.linspace(0, 0.9999, 10000)
#   → np.where to avoid division by zero
#   → np.interp to find v for given γ


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Time Dilation and Length Contraction
# ────────────────────────────────────────────────────────────────────────────
#
# A muon travels at v=0.995c from upper atmosphere (h=15km).
#   (a) In Earth's frame: muon's lifetime (Δt = γ*τ0, τ0=2.2μs)?  Does it reach ground?
#   (b) In muon's frame: atmospheric thickness (L = L0/γ)?  Does it reach ground?
#   (c) Plot contracted length vs γ for L0=15km.
#
# Hints:
#   → c = 3e8 m/s
#   → γ = 1/sqrt(1-β²) where β = v/c
#   → Muon rest lifetime τ0 = 2.2e-6 s


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Relativistic Energy–Momentum
# ────────────────────────────────────────────────────────────────────────────
#
# (a) Plot rest energy, kinetic energy, and total energy vs β for a proton.
#   (b) At what speed does KE = m0c² (rest energy)?
#   (c) For a photon: show E = pc follows from E² = (pc)² + (m0c²)².
#
# Hints:
#   → E = γm0c², KE = (γ-1)m0c²
#   → m_proton = 1.67e-27 kg, c = 3e8
#   → Energies in MeV: 1 MeV = 1.6e-13 J


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Minkowski Spacetime Diagram
# ────────────────────────────────────────────────────────────────────────────
#
# Draw a spacetime diagram (ct vs x) showing:
#   (a) World lines of two observers (one stationary, one at v=0.6c).
#   (b) The light cone from origin.
#   (c) Simultaneous events in each frame (lines of simultaneity).
#
# Hints:
#   → Stationary observer: vertical line x=0
#   → Moving observer: line with slope c/v in (x, ct) plane
#   → Light cone: ct = ±x lines
#   → Lines of simultaneity for moving frame have slope v/c


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

# ============================================================================
# EM Induction & AC Circuits — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Faraday's Law
# ────────────────────────────────────────────────────────────────────────────
#
# A rectangular loop (20cm × 10cm) is in a B field changing at 0.5 T/s.
#   (a) Find the induced EMF.
#   (b) If resistance is 2Ω, find the induced current.
#   (c) Plot induced EMF when B(t) = 0.2*sin(100t) T.
#
# Hints:
#   → EMF = -dΦ/dt = -A * dB/dt
#   → For sinusoidal: EMF = -A*0.2*100*cos(100t)
#   → np.diff can numerically differentiate B(t)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Self-Inductance
# ────────────────────────────────────────────────────────────────────────────
#
# A solenoid: N=200 turns, A=5cm², L=20cm.
#   (a) Find self-inductance L_ind = μ0*N²*A/l.
#   (b) Find back-EMF when current changes at 3 A/s.
#   (c) Plot energy stored U=½LI² vs current from 0 to 5A.
#
# Hints:
#   → μ0 = 4π*1e-7
#   → EMF = -L*dI/dt
#   → U = 0.5*L*I²


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: LCR Resonance
# ────────────────────────────────────────────────────────────────────────────
#
# Series LCR: L=0.1H, C=100μF, R=10Ω, V_rms=220V.
#   (a) Find resonant frequency ω0 = 1/sqrt(LC).
#   (b) Plot impedance Z vs frequency from 0.1*ω0 to 10*ω0.
#   (c) Find Q-factor and bandwidth.
#
# Hints:
#   → Z = sqrt(R² + (ωL - 1/(ωC))²)
#   → At resonance Z=R, I_max=V/R
#   → Q = ω0*L/R, bandwidth = R/L


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Transformer
# ────────────────────────────────────────────────────────────────────────────
#
# A step-up transformer: N1=100 turns, N2=1000 turns, Vin=230V.
#   (a) Find Vout.
#   (b) If load draws 0.5A at output, find input current (ideal transformer).
#   (c) Plot turns ratio vs voltage ratio (show linear relationship).
#
# Hints:
#   → V2/V1 = N2/N1
#   → I1/I2 = N2/N1 (power conservation)


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

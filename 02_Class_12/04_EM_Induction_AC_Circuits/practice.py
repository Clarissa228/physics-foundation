"""EM Induction and AC Circuits Practice"""
import numpy as np

print("="*70)
print("ELECTROMAGNETIC INDUCTION AND AC CIRCUITS PRACTICE")
print("="*70)

def problem_1():
    print("\nP1: Faraday's Law - Induced EMF")
    print("-" * 70)
    dPhi = -0.5  # Weber/s
    emf = -dPhi
    print(f"Given: dΦ/dt = {dPhi} Wb/s")
    print(f"Formula: ε = -dΦ/dt")
    print(f"Result: ε = {emf:.1f} V")
    return emf

def problem_2():
    print("\nP2: Motional EMF")
    print("-" * 70)
    B, L, v = 0.5, 0.1, 20
    emf = B * L * v
    print(f"Given: B = {B}T, L = {L}m, v = {v}m/s")
    print(f"Result: ε = BLv = {emf:.1f} V")
    return emf

def problem_3():
    print("\nP3: Self-Inductance")
    print("-" * 70)
    mu0 = 4*np.pi*1e-7
    n, A, L_len = 1000, 0.01, 0.5
    L = mu0 * n**2 * A * L_len / (L_len)
    print(f"Given: n = {n} turns/m, A = {A}m², L = {L_len}m")
    print(f"Result: L = {L*1e3:.2f} mH")
    return L

def problem_4():
    print("\nP4: Transformer Equation")
    print("-" * 70)
    N1, N2, V1 = 100, 1000, 220
    V2 = V1 * N2 / N1
    print(f"Given: N₁ = {N1}, N₂ = {N2}, V₁ = {V1}V")
    print(f"Result: V₂ = {V2:.0f} V")
    return V2

def problem_5():
    print("\nP5: LCR Resonance Frequency")
    print("-" * 70)
    L, C = 0.1, 100e-6
    f0 = 1 / (2*np.pi*np.sqrt(L*C))
    print(f"Given: L = {L}H, C = {C*1e6:.0f}µF")
    print(f"Result: f₀ = {f0:.2f} Hz")
    return f0

def problem_6():
    print("\nP6: Impedance")
    print("-" * 70)
    R, XL, XC = 10, 50, 30
    Z = np.sqrt(R**2 + (XL - XC)**2)
    print(f"Given: R = {R}Ω, X_L = {XL}Ω, X_C = {XC}Ω")
    print(f"Result: Z = {Z:.2f}Ω")
    return Z

def problem_7():
    print("\nP7: RMS Voltage and Current")
    print("-" * 70)
    V_peak, R = 100, 50
    V_rms = V_peak / np.sqrt(2)
    I_rms = V_rms / R
    print(f"Given: V_peak = {V_peak}V, R = {R}Ω")
    print(f"Result: V_rms = {V_rms:.1f}V, I_rms = {I_rms:.2f}A")
    return V_rms, I_rms

def problem_8():
    print("\nP8: Average Power in AC")
    print("-" * 70)
    V_rms, I_rms, phi = 100, 2, np.radians(30)
    P_avg = V_rms * I_rms * np.cos(phi)
    pf = np.cos(phi)
    print(f"Given: V_rms = {V_rms}V, I_rms = {I_rms}A, φ = 30°")
    print(f"Result: P = {P_avg:.0f}W, Power factor = {pf:.3f}")
    return P_avg

def problem_9():
    print("\nP9: Capacitive Reactance")
    print("-" * 70)
    f, C = 60, 10e-6
    omega = 2 * np.pi * f
    XC = 1 / (omega * C)
    print(f"Given: f = {f}Hz, C = {C*1e6:.0f}µF")
    print(f"Result: X_C = {XC:.1f}Ω")
    return XC

def problem_10():
    print("\nP10: Quality Factor")
    print("-" * 70)
    L, R, C = 0.1, 10, 100e-6
    omega0 = 1 / np.sqrt(L * C)
    Q = omega0 * L / R
    print(f"Given: L = {L}H, R = {R}Ω, C = {C*1e6:.0f}µF")
    print(f"Result: Q = {Q:.2f}")
    return Q

if __name__ == "__main__":
    for i in range(1, 11):
        eval(f"problem_{i}()")
    print("\n" + "="*70)

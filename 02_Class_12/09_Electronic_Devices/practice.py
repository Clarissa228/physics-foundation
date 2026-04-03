"""Electronic Devices Practice"""
import numpy as np

e = 1.602e-19
k_B = 1.38e-23

print("="*70)
print("ELECTRONIC DEVICES PRACTICE")
print("="*70)

def p1():
    print("\nP1: Thermal Voltage")
    print("-" * 70)
    T = 300  # K
    V_T = k_B * T / e
    print(f"Given: T = {T}K")
    print(f"V_T = k_B⋅T/e = {V_T*1000:.1f}mV ≈ 26mV")
    return V_T

def p2():
    print("\nP2: Diode Current")
    print("-" * 70)
    I0 = 1e-12  # A
    V = 0.6  # V
    V_T = 0.026
    I = I0 * (np.exp(V/V_T) - 1)
    print(f"Given: I₀ = {I0}A, V = {V}V, V_T = {V_T}V")
    print(f"I = I₀(e^(V/V_T) - 1) = {I:.2e}A ≈ {I*1e3:.0f}mA")
    return I

def p3():
    print("\nP3: LED Photon Energy")
    print("-" * 70)
    E_g = 1.5  # eV (GaAs bandgap)
    print(f"Given: E_g = {E_g}eV")
    print(f"Photon λ = hc/E_g = {1240/E_g:.0f}nm (near-infrared)")
    return

def p4():
    print("\nP4: Reverse Breakdown")
    print("-" * 70)
    print(f"Zener diode: V_Z ≈ 5V (typical)")
    print(f"Used for voltage regulation")
    print(f"Max power: P = V_Z × I_max")
    return

def p5():
    print("\nP5: BJT Gain")
    print("-" * 70)
    I_b = 1e-6  # A (1µA base current)
    beta = 100
    I_c = beta * I_b
    print(f"Given: β = {beta}, I_b = {I_b*1e6:.0f}µA")
    print(f"I_c = β⋅I_b = {I_c*1e3:.0f}mA")
    print(f"Transistor amplifies current by {beta}×")
    return I_c

def p6():
    print("\nP6: Common Emitter Gain")
    print("-" * 70)
    R_c = 1000  # Collector resistance (Ω)
    r_e = 26  # Emitter resistance (Ω) at 1mA
    A_v = R_c / r_e
    print(f"Given: R_c = {R_c}Ω, r_e = {r_e}Ω")
    print(f"Voltage gain A_v = R_c/r_e = {A_v:.0f}")
    return A_v

def p7():
    print("\nP7: MOSFET Threshold Voltage")
    print("-" * 70)
    print(f"NMOS: V_T ≈ +0.4 to +1.0V (switches ON)")
    print(f"PMOS: V_T ≈ -0.4 to -1.0V (switches ON)")
    print(f"Gate voltage controls channel resistance")
    return

def p8():
    print("\nP8: Logic Gate Function")
    print("-" * 70)
    print(f"NOT: Y = NOT(A)")
    print(f"NAND: Y = NOT(A AND B)")
    print(f"NOR: Y = NOT(A OR B)")
    print(f"All combinational logic built from these")
    return

def p9():
    print("\nP9: Rectification")
    print("-" * 70)
    V_peak = 20  # V
    V_diode = 0.7
    V_out = V_peak - V_diode
    print(f"Given: V_peak = {V_peak}V")
    print(f"Across diode drop ≈ {V_diode}V")
    print(f"Output = {V_out}V (half-wave)")
    return V_out

def p10():
    print("\nP10: Bandgap vs Wavelength")
    print("-" * 70)
    materials = {'Si': 1.12, 'Ge': 0.66, 'GaAs': 1.42, 'GaN': 3.44}
    h_over_c = 1240  # eV⋅nm
    for mat, E_g in materials.items():
        lambda_w = h_over_c / E_g
        print(f"{mat}: E_g = {E_g:.2f}eV → λ_max = {lambda_w:.0f}nm")
    return

if __name__ == "__main__":
    for i in range(1, 11):
        eval(f"p{i}()")
    print("\n" + "="*70)

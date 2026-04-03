"""Electromagnetic Waves Practice"""
import numpy as np

mu0 = 4*np.pi*1e-7
eps0 = 8.854e-12
c = 3e8

print("="*70)
print("ELECTROMAGNETIC WAVES PRACTICE")
print("="*70)

def problem_1():
    print("\nP1: Speed of Light from Maxwell's Equations")
    print("-" * 70)
    c_calc = 1/np.sqrt(mu0*eps0)
    print(f"c = 1/√(μ₀ε₀)")
    print(f"c = {c_calc:.2e} m/s ≈ {c_calc/1e8:.1f}×10⁸ m/s")
    return c_calc

def problem_2():
    print("\nP2: Wavelength and Frequency")
    print("-" * 70)
    f = 1e14  # Frequency (1e14 Hz, infrared)
    lambda_w = c / f
    print(f"Given: f = {f:.0e} Hz")
    print(f"λ = c/f = {c:.0e} / {f:.0e} = {lambda_w*1e9:.1f} nm")
    print(f"This is in the infrared region")
    return lambda_w

def problem_3():
    print("\nP3: Poynting Vector and Intensity")
    print("-" * 70)
    E0 = 100  # V/m
    Z0 = np.sqrt(mu0/eps0)  # Impedance of free space
    I = E0**2 / (2*Z0)
    print(f"Given: E₀ = {E0} V/m")
    print(f"Z₀ = √(μ₀/ε₀) = {Z0:.1f} Ω")
    print(f"Intensity I = E₀²/(2Z₀) = {I:.1f} W/m²")
    return I

def problem_4():
    print("\nP4: Relationship between E and B")
    print("-" * 70)
    E = 50  # V/m
    B = E / c
    print(f"Given: E = {E} V/m")
    print(f"In EM wave: E = cB")
    print(f"B = E/c = {E}/{c:.0e} = {B:.2e} T = {B*1e9:.2f} nT")
    return B

def problem_5():
    print("\nP5: Energy Density")
    print("-" * 70)
    E = 100  # V/m
    u_E = 0.5 * eps0 * E**2
    u_B = u_E  # Equal in EM wave
    u_total = u_E + u_B
    print(f"Given: E = {E} V/m")
    print(f"u_E = ½ε₀E² = {u_E:.2e} J/m³")
    print(f"u_B = u_E = {u_B:.2e} J/m³ (equal)")
    print(f"u_total = {u_total:.2e} J/m³")
    return u_total

def problem_6():
    print("\nP6: Radiation Pressure")
    print("-" * 70)
    I = 1000  # W/m²
    P = I / c
    print(f"Given: Intensity I = {I} W/m²")
    print(f"Pressure P = I/c = {I}/{c:.0e} = {P:.2e} Pa = {P*1e6:.2f} µPa")
    return P

def problem_7():
    print("\nP7: EM Spectrum - Visible Light")
    print("-" * 70)
    lambda_red = 700e-9
    lambda_violet = 400e-9
    f_red = c / lambda_red
    f_violet = c / lambda_violet
    print(f"Visible spectrum: λ = 400-700 nm")
    print(f"Red light: λ = {lambda_red*1e9:.0f}nm, f = {f_red:.2e}Hz")
    print(f"Violet light: λ = {lambda_violet*1e9:.0f}nm, f = {f_violet:.2e}Hz")
    return f_red, f_violet

def problem_8():
    print("\nP8: Wavenumber and Wave Vector")
    print("-" * 70)
    lambda_w = 500e-9
    k = 2*np.pi / lambda_w
    omega = k * c
    print(f"Given: λ = {lambda_w*1e9:.0f} nm (green light)")
    print(f"Wavenumber k = 2π/λ = {k:.2e} m⁻¹")
    print(f"Angular frequency ω = kc = {omega:.2e} rad/s")
    print(f"Frequency f = ω/(2π) = {omega/(2*np.pi):.2e} Hz")
    return k, omega

def problem_9():
    print("\nP9: Power from EM Wave")
    print("-" * 70)
    I, A = 1000, 1  # 1000 W/m², 1 m² area
    P = I * A
    print(f"Given: Intensity I = {I} W/m², Area A = {A} m²")
    print(f"Power P = I × A = {P} W = {P/1000:.1f} kW")
    return P

def problem_10():
    print("\nP10: Solar Constant")
    print("-" * 70)
    I_solar = 1361  # W/m² (actual value at Earth orbit)
    r_earth = 1.5e11  # m
    P_sun = I_solar * 4 * np.pi * r_earth**2
    print(f"Given: Solar intensity at Earth I = {I_solar} W/m²")
    print(f"Distance r = {r_earth:.1e}m (1 AU)")
    print(f"Total power from Sun P = I × 4πr² = {P_sun:.2e}W")
    return P_sun

if __name__ == "__main__":
    for i in range(1, 11):
        eval(f"problem_{i}()")
    print("\n" + "="*70)

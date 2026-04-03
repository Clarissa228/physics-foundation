"""Dual Nature of Radiation and Matter Practice"""
import numpy as np

h = 6.626e-34  # Planck constant
c = 3e8
e = 1.602e-19
me = 9.109e-31

print("="*70)
print("DUAL NATURE PRACTICE PROBLEMS")
print("="*70)

def p1():
    print("\nP1: Photoelectric Effect")
    print("-" * 70)
    phi = 3.3  # Work function (eV)
    nu = 1e15  # Frequency (Hz)
    KE_max = (h*nu/e) - phi
    print(f"Given: φ = {phi}eV, ν = {nu:.0e}Hz")
    print(f"hν = {h*nu/e:.2f}eV")
    print(f"KE_max = hν - φ = {KE_max:.2f}eV")
    return KE_max

def p2():
    print("\nP2: Threshold Frequency")
    print("-" * 70)
    phi = 2.3  # eV
    nu0 = phi * e / h
    print(f"Given: φ = {phi}eV")
    print(f"ν₀ = φ/h = {nu0:.2e}Hz = {nu0/1e14:.1f}×10^14Hz")
    return nu0

def p3():
    print("\nP3: de Broglie Wavelength")
    print("-" * 70)
    v = 1e6  # m/s
    lambda_dB = h / (me * v)
    print(f"Given: v = {v:.0e}m/s (electron)")
    print(f"λ = h/(mv) = {h:.2e}/({me:.2e}×{v:.0e})")
    print(f"λ = {lambda_dB*1e9:.3f}nm = {lambda_dB*1e12:.2f}pm")
    return lambda_dB

def p4():
    print("\nP4: Compton Scattering")
    print("-" * 70)
    lambda_C = h / (me * c)
    theta = 90  # degrees
    delta_lambda = lambda_C * (1 - np.cos(np.radians(theta)))
    print(f"Given: θ = {theta}°")
    print(f"λ_C = h/(m_e c) = {lambda_C*1e12:.2f}pm")
    print(f"Δλ = λ_C(1-cosθ) = {delta_lambda*1e12:.2f}pm")
    return delta_lambda

def p5():
    print("\nP5: Blackbody Radiation - Wien's Law")
    print("-" * 70)
    T = 5778  # Sun's temperature (K)
    b = 2.898e-3  # Wien constant
    lambda_max = b / T
    print(f"Given: T = {T}K (Sun)")
    print(f"λ_max = b/T = {b}/{T} = {lambda_max*1e9:.0f}nm")
    print(f"This is yellow-green (visible light)")
    return lambda_max

def p6():
    print("\nP6: Stefan-Boltzmann Law")
    print("-" * 70)
    sigma = 5.67e-8  # W/(m²⋅K⁴)
    T, A = 6000, 1  # K, m²
    P = sigma * A * T**4
    print(f"Given: T = {T}K, A = {A}m²")
    print(f"P = σAT⁴ = {sigma:.2e}×{A}×{T}⁴ = {P:.2e}W")
    return P

def p7():
    print("\nP7: Particle Momentum and Energy")
    print("-" * 70)
    KE = 10  # eV
    v = np.sqrt(2 * KE * e / me)
    p = me * v
    lambda_dB = h / p
    print(f"Given: KE = {KE}eV (electron)")
    print(f"v = {v/1e6:.2f}×10⁶ m/s")
    print(f"p = mv = {p:.2e} kg⋅m/s")
    print(f"λ_dB = {lambda_dB*1e9:.3f}nm")
    return lambda_dB

def p8():
    print("\nP8: Uncertainty Principle")
    print("-" * 70)
    delta_x = 1e-10  # 1 Angstrom
    hbar = h / (2*np.pi)
    delta_p_min = hbar / (2 * delta_x)
    delta_v = delta_p_min / me
    print(f"Given: Δx = {delta_x*1e10:.1f}Å")
    print(f"Δp_min = ℏ/(2Δx) = {delta_p_min:.2e} kg⋅m/s")
    print(f"Δv = Δp/m = {delta_v/1e6:.2f}×10⁶ m/s")
    print(f"Electron velocity uncertain by {delta_v/1e6:.0f}×10⁶ m/s!")
    return delta_v

def p9():
    print("\nP9: Energy-Time Uncertainty")
    print("-" * 70)
    delta_t = 1e-15  # 1 femtosecond
    hbar = h / (2*np.pi)
    delta_E = hbar / (2 * delta_t)
    print(f"Given: Δt = {delta_t*1e15:.0f} fs")
    print(f"ΔE_min = ℏ/(2Δt) = {delta_E*e:.2e} eV")
    print(f"This is ~{delta_E*e/1e6:.1f}meV")
    return delta_E

def p10():
    print("\nP10: Pair Production Threshold")
    print("-" * 70)
    E_threshold = 2 * me * c**2 / e  # eV
    print(f"Given: Need to create e-e+ pair")
    print(f"E_threshold = 2m_e c² = {E_threshold/1e6:.2f}MeV")
    print(f"Photons with less energy cannot create pairs")
    return E_threshold

if __name__ == "__main__":
    for i in range(1, 11):
        eval(f"p{i}()")
    print("\n" + "="*70)

"""Atoms and Nuclei Practice"""
import numpy as np

h = 6.626e-34
c = 3e8
e = 1.602e-19
R_H = 1.097e7  # Rydberg constant (m^-1)

print("="*70)
print("ATOMS AND NUCLEI PRACTICE")
print("="*70)

def p1():
    print("\nP1: Bohr Radius")
    print("-" * 70)
    a0 = 0.529e-10  # m
    print(f"Bohr radius a₀ = {a0*1e10:.3f} Å = {a0*1e12:.2f}pm")
    return a0

def p2():
    print("\nP2: Hydrogen Energy Levels")
    print("-" * 70)
    E1 = -13.6  # eV
    for n in [1, 2, 3]:
        E_n = E1 / n**2
        print(f"E_{n} = {E_n:.2f}eV")
    return

def p3():
    print("\nP3: Balmer Series")
    print("-" * 70)
    lambda_Halpha = 656.3e-9  # m (first Balmer line)
    print(f"Balmer series (n→2):")
    E1 = -13.6
    for n in [3, 4, 5]:
        E_trans = (E1/2**2) - (E1/n**2)
        lambda_line = h * c / (E_trans * e)
        print(f"  n={n}: λ = {lambda_line*1e9:.1f}nm")
    return

def p4():
    print("\nP4: Nuclear Radius")
    print("-" * 70)
    A = 197  # Au-197
    R0 = 1.2e-15  # m
    r_nucleus = R0 * A**(1/3)
    print(f"Given: A = {A} (Gold-197)")
    print(f"r = R₀A^(1/3) = {R0*1e15:.2f}×{A}^(1/3) = {r_nucleus*1e15:.2f}fm")
    return r_nucleus

def p5():
    print("\nP5: Binding Energy")
    print("-" * 70)
    Z, N = 6, 6  # C-12
    m_p = 1.007276  # u
    m_n = 1.008665  # u
    M = 12.000000  # u (exact by definition)
    delta_m = Z*m_p + N*m_n - M
    BE = delta_m * 931.5  # MeV
    BE_A = BE / 12
    print(f"Given: C-12 (Z={Z}, N={N})")
    print(f"Δm = {delta_m:.4f}u")
    print(f"BE = {BE:.2f}MeV")
    print(f"BE/A = {BE_A:.2f}MeV/nucleon")
    return BE

def p6():
    print("\nP6: Radioactive Decay")
    print("-" * 70)
    N0 = 1000
    t_half = 1600  # years
    t = 3200  # years (2 half-lives)
    N = N0 * (0.5)**(t/t_half)
    print(f"Given: N₀ = {N0}, t₁/₂ = {t_half} years")
    print(f"After t = {t} years ({t/t_half} half-lives):")
    print(f"N = {N:.0f}")
    return N

def p7():
    print("\nP7: Activity and Decay Constant")
    print("-" * 70)
    t_half = 5.27  # years
    lambda_decay = np.log(2) / (t_half * 365.25 * 24 * 3600)
    N = 1e20
    A = lambda_decay * N
    print(f"Given: t₁/₂ = {t_half} years")
    print(f"λ = {lambda_decay:.2e} s⁻¹")
    print(f"Activity = λN = {A:.2e} Bq")
    return A

def p8():
    print("\nP8: Mass Defect and Energy")
    print("-" * 70)
    He4_mass = 4.002603  # u
    He4_nucleon_mass = 2*1.007276 + 2*1.008665
    delta_m = He4_nucleon_mass - He4_mass
    BE = delta_m * 931.5  # MeV
    print(f"He-4: mass = {He4_mass}u")
    print(f"Δm = {delta_m:.6f}u")
    print(f"BE = {BE:.2f}MeV")
    return BE

def p9():
    print("\nP9: Q-value of Reaction")
    print("-" * 70)
    print(f"Fission: U-235 + n → Ba-141 + Kr-92 + 3n")
    print(f"Q ≈ 200 MeV (energy released)")
    print(f"\nFusion: H-2 + H-3 → He-4 + n")
    print(f"Q ≈ 17.6 MeV (energy released)")
    return

def p10():
    print("\nP10: Alpha Decay")
    print("-" * 70)
    print(f"U-238 → Th-234 + He-4")
    print(f"Q-value ≈ 4.3 MeV (splits between products)")
    print(f"By momentum conservation:")
    print(f"p_alpha ≈ 96 MeV/c, KE_alpha ≈ 4.3 MeV")
    print(f"p_Th ≈ 96 MeV/c, KE_Th ≈ 0.07 MeV")
    return

if __name__ == "__main__":
    for i in range(1, 11):
        eval(f"p{i}()")
    print("\n" + "="*70)

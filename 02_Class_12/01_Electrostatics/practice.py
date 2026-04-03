"""
Electrostatics Practice Problems
=================================

Solve these problems to test your understanding of electrostatics concepts.
Physical constants are provided below.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
k = 8.99e9  # Coulomb constant (N⋅m²/C²)
eps0 = 8.854e-12  # Permittivity of free space (F/m)
e = 1.602e-19  # Elementary charge (C)

print("="*70)
print("ELECTROSTATICS PRACTICE PROBLEMS")
print("="*70)


# ==============================================================================
# PROBLEM 1: Coulomb's Force Between Two Charges
# ==============================================================================

def problem_1():
    """
    Two point charges q₁ = 2 µC and q₂ = -3 µC are separated by 30 cm.
    Calculate the magnitude of the electrostatic force between them.
    """
    print("\n" + "-"*70)
    print("PROBLEM 1: Coulomb Force")
    print("-"*70)

    q1 = 2e-6  # Coulomb (2 µC)
    q2 = -3e-6  # Coulomb (-3 µC)
    r = 0.30  # meters (30 cm)

    # Coulomb's law: F = k|q₁q₂|/r²
    F = k * abs(q1 * q2) / r**2

    print(f"Given:")
    print(f"  q₁ = {q1*1e6:.1f} µC")
    print(f"  q₂ = {q2*1e6:.1f} µC")
    print(f"  r = {r:.2f} m")
    print(f"\nFormula: F = k|q₁q₂|/r²")
    print(f"F = ({k:.2e}) × |{q1*1e6:.1f}×10⁻⁶| × |{q2*1e6:.1f}×10⁻⁶| / {r}²")
    print(f"\nResult: F = {F:.3f} N = {F*1000:.1f} mN")
    print(f"\nNote: The force is ATTRACTIVE (opposite charges)")

    return F


# ==============================================================================
# PROBLEM 2: Electric Field of a Point Charge
# ==============================================================================

def problem_2():
    """
    Calculate the electric field at a distance of 20 cm from a point charge
    of +5 nC.
    """
    print("\n" + "-"*70)
    print("PROBLEM 2: Electric Field")
    print("-"*70)

    Q = 5e-9  # Coulomb (5 nC)
    r = 0.20  # meters (20 cm)

    # E = kQ/r²
    E = k * Q / r**2

    print(f"Given:")
    print(f"  Q = {Q*1e9:.1f} nC")
    print(f"  r = {r:.2f} m")
    print(f"\nFormula: E = kQ/r²")
    print(f"E = ({k:.2e}) × {Q*1e9:.1f}×10⁻⁹ / {r}²")
    print(f"\nResult: E = {E:.3e} V/m")
    print(f"        E = {E/1000:.2f} kV/m")

    return E


# ==============================================================================
# PROBLEM 3: Electric Potential
# ==============================================================================

def problem_3():
    """
    Calculate the electric potential at a distance of 50 cm from a point
    charge of -8 nC.
    """
    print("\n" + "-"*70)
    print("PROBLEM 3: Electric Potential")
    print("-"*70)

    Q = -8e-9  # Coulomb (-8 nC)
    r = 0.50  # meters (50 cm)

    # V = kQ/r
    V = k * Q / r

    print(f"Given:")
    print(f"  Q = {Q*1e9:.1f} nC")
    print(f"  r = {r:.2f} m")
    print(f"\nFormula: V = kQ/r")
    print(f"V = ({k:.2e}) × ({Q*1e9:.1f})×10⁻⁹ / {r}")
    print(f"\nResult: V = {V:.2f} V")
    print(f"\nNote: Potential is NEGATIVE (because charge is negative)")

    return V


# ==============================================================================
# PROBLEM 4: Superposition of Multiple Charges
# ==============================================================================

def problem_4():
    """
    Three point charges are arranged at vertices of a triangle:
    - q₁ = +2 µC at origin (0, 0)
    - q₂ = +3 µC at (4, 0) m
    - q₃ = -1 µC at (0, 3) m

    Find the electric potential at point P = (4, 3) m.
    """
    print("\n" + "-"*70)
    print("PROBLEM 4: Superposition Principle")
    print("-"*70)

    # Charges and positions
    charges = [2e-6, 3e-6, -1e-6]  # Coulombs
    positions = [(0, 0), (4, 0), (0, 3)]  # meters
    P = (4, 3)  # Point where we calculate potential

    print(f"Given:")
    print(f"  q₁ = {charges[0]*1e6:.1f} µC at {positions[0]}")
    print(f"  q₂ = {charges[1]*1e6:.1f} µC at {positions[1]}")
    print(f"  q₃ = {charges[2]*1e6:.1f} µC at {positions[2]}")
    print(f"  Calculate V at point P = {P}")

    # Calculate distances from each charge to P
    distances = []
    for charge, pos in zip(charges, positions):
        r = np.sqrt((P[0] - pos[0])**2 + (P[1] - pos[1])**2)\n        distances.append(r)

    # Calculate potential due to each charge
    V_total = 0
    print(f"\nCalculations:")
    for i, (q, pos, r) in enumerate(zip(charges, positions, distances)):
        V_i = k * q / r
        V_total += V_i
        print(f"  V₍ from q{i+1} = k×q{i+1}/r = ({k:.2e})×({q*1e6:.1f}×10⁻⁶)/{r:.2f} = {V_i:.2f} V")

    print(f"\nTotal potential: V_total = V₁ + V₂ + V₃ = {V_total:.2f} V")

    return V_total


# ==============================================================================
# PROBLEM 5: Capacitance of a Parallel Plate Capacitor
# ==============================================================================

def problem_5():
    """
    A parallel plate capacitor has:
    - Plate area: 100 cm²
    - Separation: 2 mm
    - Dielectric: vacuum (κ = 1)

    Calculate: (a) Capacitance, (b) Charge if V = 100 V, (c) Energy stored
    """
    print("\n" + "-"*70)
    print("PROBLEM 5: Parallel Plate Capacitor")
    print("-"*70)

    A = 100e-4  # m² (100 cm²)
    d = 2e-3  # m (2 mm)
    V = 100  # Volts
    kappa = 1  # vacuum

    # (a) Capacitance: C = ε₀A/d
    C = kappa * eps0 * A / d

    # (b) Charge: Q = CV
    Q = C * V

    # (c) Energy: U = ½CV²
    U = 0.5 * C * V**2

    print(f"Given:")
    print(f"  Plate area A = {A*1e4:.0f} cm² = {A:.5f} m²")
    print(f"  Separation d = {d*1000:.1f} mm = {d:.6f} m")
    print(f"  Applied voltage V = {V} V")
    print(f"  Dielectric constant κ = {kappa}")

    print(f"\n(a) Capacitance: C = κε₀A/d")
    print(f"    C = {kappa} × ({eps0:.3e}) × {A:.5f} / {d:.6f}")
    print(f"    C = {C:.6e} F = {C*1e12:.2f} pF")

    print(f"\n(b) Stored charge: Q = CV")
    print(f"    Q = {C:.6e} × {V}")
    print(f"    Q = {Q:.6e} C = {Q*1e9:.2f} nC")

    print(f"\n(c) Energy stored: U = ½CV²")
    print(f"    U = ½ × {C:.6e} × {V}²")
    print(f"    U = {U:.6e} J = {U*1e9:.2f} nJ")

    return C, Q, U


# ==============================================================================
# PROBLEM 6: Capacitors in Series and Parallel
# ==============================================================================

def problem_6():
    """
    Three capacitors:
    - C₁ = 2 µF
    - C₂ = 3 µF
    - C₃ = 6 µF

    Find equivalent capacitance when connected:
    (a) In series
    (b) In parallel
    """
    print("\n" + "-"*70)
    print("PROBLEM 6: Capacitor Networks")
    print("-"*70)

    C1 = 2e-6  # Farads (2 µF)
    C2 = 3e-6  # Farads (3 µF)
    C3 = 6e-6  # Farads (6 µF)

    print(f"Given:")
    print(f"  C₁ = {C1*1e6:.1f} µF")
    print(f"  C₂ = {C2*1e6:.1f} µF")
    print(f"  C₃ = {C3*1e6:.1f} µF")

    # (a) Series: 1/C_eq = 1/C₁ + 1/C₂ + 1/C₃
    C_series = 1 / (1/C1 + 1/C2 + 1/C3)

    print(f"\n(a) SERIES CONNECTION: 1/C_eq = 1/C₁ + 1/C₂ + 1/C₃")
    print(f"    1/C_eq = 1/{C1*1e6:.1f}×10⁻⁶ + 1/{C2*1e6:.1f}×10⁻⁶ + 1/{C3*1e6:.1f}×10⁻⁶")
    print(f"    1/C_eq = {1/C1 + 1/C2 + 1/C3:.6e}")
    print(f"    C_eq = {C_series:.6e} F = {C_series*1e6:.2f} µF")

    # (b) Parallel: C_eq = C₁ + C₂ + C₃
    C_parallel = C1 + C2 + C3

    print(f"\n(b) PARALLEL CONNECTION: C_eq = C₁ + C₂ + C₃")
    print(f"    C_eq = {C1*1e6:.1f}×10⁻⁶ + {C2*1e6:.1f}×10⁻⁶ + {C3*1e6:.1f}×10⁻⁶")
    print(f"    C_eq = {C_parallel:.6e} F = {C_parallel*1e6:.2f} µF")

    print(f"\nNote: Series gives smaller C; parallel gives larger C")

    return C_series, C_parallel


# ==============================================================================
# PROBLEM 7: Dielectric Effect
# ==============================================================================

def problem_7():
    """
    A capacitor with vacuum capacitance C₀ = 100 pF is filled with a dielectric
    material having κ = 5.

    Calculate:
    (a) New capacitance
    (b) Ratio of energy storage at same voltage
    (c) Ratio of energy storage at same charge
    """
    print("\n" + "-"*70)
    print("PROBLEM 7: Dielectric Effect")
    print("-"*70)

    C0 = 100e-12  # Farads (100 pF)
    kappa = 5

    print(f"Given:")
    print(f"  Vacuum capacitance C₀ = {C0*1e12:.0f} pF")
    print(f"  Dielectric constant κ = {kappa}")

    # (a) New capacitance
    C_with_diel = kappa * C0

    print(f"\n(a) Capacitance with dielectric: C = κC₀")
    print(f"    C = {kappa} × {C0*1e12:.0f}×10⁻¹² F")
    print(f"    C = {C_with_diel*1e12:.0f} pF")

    # (b) Energy at same voltage
    print(f"\n(b) Energy storage at constant voltage:")
    print(f"    U = ½CV², so U_with_diel / U₀ = C_diel / C₀ = κ = {kappa}")
    print(f"    → Energy increases by factor of {kappa}")

    # (c) Energy at same charge
    print(f"\n(c) Energy storage at constant charge:")
    print(f"    U = Q²/(2C), so U_with_diel / U₀ = C₀ / C_diel = 1/κ = {1/kappa:.2f}")
    print(f"    → Energy decreases by factor of {kappa}")

    return C_with_diel


# ==============================================================================
# PROBLEM 8: Gauss's Law Application
# ==============================================================================

def problem_8():
    """
    A uniformly charged spherical shell has:
    - Radius: R = 0.5 m
    - Total charge: Q = 1 µC

    Use Gauss's law to find the electric field:
    (a) At r = 0.3 m (inside)
    (b) At r = 0.8 m (outside)
    """
    print("\n" + "-"*70)
    print("PROBLEM 8: Gauss's Law Application")
    print("-"*70)

    R = 0.5  # meters (shell radius)
    Q = 1e-6  # Coulomb (1 µC)

    print(f"Given:")
    print(f"  Spherical shell radius R = {R} m")
    print(f"  Total charge Q = {Q*1e6:.1f} µC")

    # (a) At r = 0.3 m (inside)
    r_inside = 0.3
    print(f"\n(a) At r = {r_inside} m (INSIDE shell):")
    print(f"    Using Gauss's law with Gaussian sphere of r = {r_inside} m:")
    print(f"    Q_enclosed = 0 (charge is on shell at R = {R} m)")
    print(f"    ∮E·dA = Q_enc/ε₀")
    print(f"    E × 4πr² = 0")
    print(f"    E = 0 V/m")

    # (b) At r = 0.8 m (outside)
    r_outside = 0.8
    E_outside = k * Q / r_outside**2

    print(f"\n(b) At r = {r_outside} m (OUTSIDE shell):")
    print(f"    Using Gauss's law with Gaussian sphere of r = {r_outside} m:")
    print(f"    Q_enclosed = {Q*1e6:.1f} µC (all charge on shell)")
    print(f"    E × 4πr² = Q/ε₀")
    print(f"    E = kQ/r²")
    print(f"    E = ({k:.2e}) × {Q*1e6:.1f}×10⁻⁶ / {r_outside}²")
    print(f"    E = {E_outside:.3e} V/m = {E_outside/1000:.2f} kV/m")

    print(f"\nKey insight: Field inside uniformly charged shell is ZERO!")

    return 0, E_outside


# ==============================================================================
# PROBLEM 9: Potential Difference
# ==============================================================================

def problem_9():
    """
    A uniform electric field of 1000 V/m points in the +x direction.
    A positive test charge q = 0.5 µC is moved from (0, 0) to (3, 4) meters.

    Calculate:
    (a) The potential difference V_AB
    (b) Work done by the electric field
    """
    print("\n" + "-"*70)
    print("PROBLEM 9: Work and Potential Difference")
    print("-"*70)

    E = 1000  # V/m
    q = 0.5e-6  # Coulomb

    # Initial and final positions
    x1, y1 = 0, 0
    x2, y2 = 3, 4

    print(f"Given:")
    print(f"  Electric field E = {E} V/m (in +x direction)")
    print(f"  Test charge q = {q*1e6:.1f} µC")
    print(f"  Move from A = ({x1}, {y1}) to B = ({x2}, {y2}) m")

    # Displacement vector
    displacement = np.sqrt((x2-x1)**2 + (y2-y1)**2)

    # Component along field
    dx = x2 - x1

    # Potential difference: V_B - V_A = -E·d (for uniform field)
    V_diff = -E * dx

    print(f"\n(a) Potential difference:")
    print(f"    For uniform field: V_B - V_A = -E·Δx")
    print(f"    V_B - V_A = -{E} × {dx}")
    print(f"    V_B - V_A = {V_diff:.0f} V")

    # Work done by electric field: W = q(V_A - V_B) = -qV_diff
    W = q * (-V_diff)

    print(f"\n(b) Work done by electric field:")
    print(f"    W = q × (V_A - V_B) = q × ΔV")
    print(f"    W = {q*1e6:.1f}×10⁻⁶ × ({-V_diff:.0f})")
    print(f"    W = {W:.6e} J = {W*1e3:.2f} mJ")
    print(f"\nNote: Positive work means field does work on the charge")

    return V_diff, W


# ==============================================================================
# PROBLEM 10: Energy Density in Electric Field
# ==============================================================================

def problem_10():
    """
    In a parallel plate capacitor:
    - Plate separation: 1 mm
    - Applied voltage: 1000 V

    Calculate:
    (a) Electric field strength
    (b) Energy density
    (c) Total energy (assuming 1 cm² plate area)
    """
    print("\n" + "-"*70)
    print("PROBLEM 10: Energy Density")
    print("-"*70)

    d = 1e-3  # m (1 mm)
    V = 1000  # Volts
    A = 1e-4  # m² (1 cm²)

    print(f"Given:")
    print(f"  Plate separation d = {d*1000:.1f} mm")
    print(f"  Applied voltage V = {V} V")
    print(f"  Plate area A = {A*1e4:.0f} cm²")

    # (a) Electric field
    E = V / d

    print(f"\n(a) Electric field: E = V/d")
    print(f"    E = {V} / {d:.6f}")
    print(f"    E = {E:.3e} V/m = {E/1e6:.1f} MV/m")

    # (b) Energy density
    u = 0.5 * eps0 * E**2

    print(f"\n(b) Energy density: u = ½ε₀E²")
    print(f"    u = ½ × {eps0:.3e} × ({E:.3e})²")
    print(f"    u = {u:.6e} J/m³")

    # (c) Total energy
    volume = A * d
    U = u * volume

    print(f"\n(c) Total energy in capacitor:")
    print(f"    Volume = A × d = {A:.6e} × {d:.6f} = {volume:.9e} m³")
    print(f"    U = u × Volume = {u:.6e} × {volume:.9e}")
    print(f"    U = {U:.6e} J = {U*1e9:.2f} nJ")

    # Verify with standard formula
    C = eps0 * A / d
    U_check = 0.5 * C * V**2

    print(f"\nVerification using U = ½CV²: U = {U_check:.6e} J (matches!)")

    return E, u, U


# ==============================================================================
# RUN ALL PROBLEMS
# ==============================================================================

if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_7()
    problem_8()
    problem_9()
    problem_10()

    print("\n" + "="*70)
    print("All problems solved! Review the calculations above.")
    print("="*70)

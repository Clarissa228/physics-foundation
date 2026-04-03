"""
Magnetic Effects and Magnetism Practice Problems
=================================================
"""

import numpy as np

# Physical constants
mu0 = 4*np.pi*1e-7  # H/m
e = 1.602e-19  # C
me = 9.109e-31  # kg
mp = 1.673e-27  # kg

print("="*70)
print("MAGNETIC EFFECTS PRACTICE PROBLEMS")
print("="*70)


def problem_1():
    """Magnetic field from long straight wire"""
    print("\nPROBLEM 1: Straight Wire Magnetic Field")
    print("-" * 70)

    I = 10  # Amperes
    r = 0.05  # meters (5 cm)

    B = (mu0 * I) / (2 * np.pi * r)

    print(f"Given: I = {I}A, r = {r*100:.0f}cm from wire")
    print(f"Formula: B = μ₀I/(2πr)")
    print(f"B = ({mu0:.3e}) × {I} / (2π × {r})")
    print(f"Result: B = {B*1e6:.1f} µT = {B*1e3:.2f} mT")
    return B


def problem_2():
    """Force on current-carrying conductor"""
    print("\nPROBLEM 2: Force on Current-Carrying Wire")
    print("-" * 70)

    B = 0.5  # Tesla
    I = 2    # Amperes
    L = 0.1  # meters (10 cm)
    theta = 90  # degrees (perpendicular)

    F = B * I * L * np.sin(np.radians(theta))

    print(f"Given: B = {B}T, I = {I}A, L = {L}m, θ = {theta}°")
    print(f"Formula: F = BIL sinθ")
    print(f"F = {B} × {I} × {L} × sin({theta}°)")
    print(f"Result: F = {F:.3f} N = {F*1000:.0f} mN")
    print(f"\nDirection: by right-hand rule (F = I L × B)")
    return F


def problem_3():
    """Torque on current loop"""
    print("\nPROBLEM 3: Torque on Current Loop")
    print("-" * 70)

    N = 100  # Number of turns
    I = 0.5  # Amperes
    A = 0.01  # m² (100 cm²)
    B = 0.2  # Tesla
    theta = 30  # degrees

    mu = N * I * A  # Magnetic dipole moment
    tau = mu * B * np.sin(np.radians(theta))

    print(f"Given: N = {N} turns, I = {I}A, A = {A}m² = 100cm²")
    print(f"       B = {B}T, θ = {theta}° (angle from B)")
    print(f"\nMagnetic dipole moment: μ = NIA = {N} × {I} × {A} = {mu:.3f} A⋅m²")
    print(f"Torque: τ = μB sinθ = {mu:.3f} × {B} × sin({theta}°)")
    print(f"Result: τ = {tau:.4f} N⋅m = {tau*1000:.2f} mN⋅m")
    return tau


def problem_4():
    """Cyclotron motion"""
    print("\nPROBLEM 4: Cyclotron Motion")
    print("-" * 70)

    B = 1.0  # Tesla
    v = 1e7  # m/s
    m = me   # electron mass

    r = (m * v) / (e * B)
    omega = (e * B) / m
    T = 2 * np.pi / omega
    f = 1 / T

    print(f"Given: B = {B}T, v = {v*1e-7:.1f}×10⁷ m/s (electron)")
    print(f"       e = {e:.3e}C, m = {me:.3e}kg")
    print(f"\nCyclotron radius: r = mv/(eB)")
    print(f"r = ({me:.3e} × {v*1e-7:.1f}×10⁷) / ({e:.3e} × {B})")
    print(f"r = {r*1e3:.4f} mm")
    print(f"\nCyclotron frequency: ν = eB/(2πm)")
    print(f"ν = ({e:.3e} × {B}) / (2π × {me:.3e})")
    print(f"ν = {f*1e-9:.2f} GHz")
    print(f"\nPeriod: T = 1/ν = {T*1e9:.2f} ns")
    return r, f


def problem_5():
    """Lorentz force on charged particle"""
    print("\nPROBLEM 5: Lorentz Force")
    print("-" * 70)

    q = e  # Elementary charge
    v = 3e6  # m/s
    B = 0.5  # Tesla
    theta = 60  # degrees

    F = q * v * B * np.sin(np.radians(theta))

    print(f"Given: q = e = {q:.3e}C")
    print(f"       v = {v*1e-6:.1f}×10⁶ m/s, B = {B}T, θ = {theta}°")
    print(f"Formula: F = qvB sinθ")
    print(f"F = {q:.3e} × {v*1e-6:.1f}×10⁶ × {B} × sin({theta}°)")
    print(f"Result: F = {F:.3e} N = {F*1e12:.2f} pN")
    return F


def problem_6():
    """Magnetic field from circular loop"""
    print("\nPROBLEM 6: Circular Loop Field")
    print("-" * 70)

    I = 5  # Amperes
    R = 0.1  # meters (10 cm radius)
    z = 0  # Position (at center)

    # At center: B = μ₀I/(2R)
    B_center = (mu0 * I) / (2 * R)

    print(f"Given: I = {I}A, R = {R}m (loop radius)")
    print(f"Position: at center of loop (z = 0)")
    print(f"\nFormula: B = μ₀I/(2R) at center")
    print(f"B = ({mu0:.3e}) × {I} / (2 × {R})")
    print(f"Result: B = {B_center*1e6:.1f} µT = {B_center*1e3:.2f} mT")
    return B_center


def problem_7():
    """Solenoid magnetic field"""
    print("\nPROBLEM 7: Solenoid Field")
    print("-" * 70)

    I = 2  # Amperes
    N = 1000  # Number of turns
    L = 0.5  # Length (meters)

    n = N / L  # Turns per unit length
    B_inside = mu0 * n * I

    print(f"Given: I = {I}A, N = {N} turns, L = {L}m")
    print(f"\nTurns per unit length: n = N/L = {N}/{L} = {n:.0f} turns/m")
    print(f"Formula (inside): B = μ₀nI")
    print(f"B = {mu0:.3e} × {n:.0f} × {I}")
    print(f"Result: B = {B_inside*1e3:.2f} mT")
    print(f"\nNote: Field outside solenoid ≈ 0")
    return B_inside


def problem_8():
    """Hall effect"""
    print("\nPROBLEM 8: Hall Effect")
    print("-" * 70)

    I = 1  # Current (A)
    B = 0.1  # Magnetic field (T)
    w = 0.01  # Width of conductor (m)
    d = 0.001  # Thickness (m)
    n = 8.5e28  # Free electron density (m⁻³)

    # Hall voltage: V_H = (I × B) / (n × e × d)
    V_H = (I * B) / (n * e * d)

    # Hall coefficient: R_H = 1/(ne)
    R_H = 1 / (n * e)

    print(f"Given: I = {I}A, B = {B}T")
    print(f"       Width w = {w*100:.0f}mm, Thickness d = {d*1000:.1f}mm")
    print(f"       n = {n:.2e} electrons/m³")
    print(f"\nHall coefficient: R_H = 1/(ne)")
    print(f"R_H = 1/({n:.2e} × {e:.3e}) = {R_H:.3e} m³/C")
    print(f"\nHall voltage: V_H = (I×B)/(n×e×d)")
    print(f"V_H = ({I} × {B}) / ({n:.2e} × {e:.3e} × {d})")
    print(f"Result: V_H = {V_H*1000:.2f} mV")
    return V_H


def problem_9():
    """Particle in magnetic field - circular path"""
    print("\nPROBLEM 9: Electron in Magnetic Field")
    print("-" * 70)

    # Electron accelerated through potential V
    V_accel = 100  # Volts
    B = 0.01  # Tesla

    # Kinetic energy: eV = ½mv²
    v = np.sqrt(2 * e * V_accel / me)
    r = (me * v) / (e * B)

    print(f"Given: Electron accelerated through V = {V_accel}V")
    print(f"       B = {B}T (perpendicular to velocity)")
    print(f"\nVelocity from energy conservation: eV = ½mv²")
    print(f"v = √(2eV/m) = √(2 × {e:.3e} × {V_accel} / {me:.3e})")
    print(f"v = {v*1e-6:.2f}×10⁶ m/s")
    print(f"\nCyclotron radius: r = mv/(eB)")
    print(f"r = {r*100:.2f} cm")
    return v, r


def problem_10():
    """Magnetic dipole moment"""
    print("\nPROBLEM 10: Magnetic Dipole Moment")
    print("-" * 70)

    I = 0.5  # Current (A)
    A = 0.001  # Area (m²) = 100 cm²
    N = 10  # Number of turns

    mu = N * I * A
    B_ext = 0.2  # External field (T)
    U = -mu * B_ext  # Potential energy (minimum)
    tau_max = mu * B_ext  # Maximum torque

    print(f"Given: N = {N} turns, I = {I}A")
    print(f"       Area A = {A*1e4:.0f} cm²")
    print(f"       External B = {B_ext}T")
    print(f"\nMagnetic dipole moment: μ = NIA")
    print(f"μ = {N} × {I} × {A} = {mu:.4f} A⋅m²")
    print(f"\nPotential energy (aligned with B): U = -μB")
    print(f"U = -{mu:.4f} × {B_ext} = {U:.4f} J")
    print(f"\nMaximum torque (perpendicular): τ = μB")
    print(f"τ = {tau_max:.4f} N⋅m")
    return mu


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
    print("All problems solved!")
    print("="*70)

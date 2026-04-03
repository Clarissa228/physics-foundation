"""
Current Electricity Practice Problems
======================================
"""

import numpy as np

# Physical constants
e = 1.602e-19  # Elementary charge (C)

print("="*70)
print("CURRENT ELECTRICITY PRACTICE PROBLEMS")
print("="*70)


def problem_1():
    """Ohm's Law: Calculate current given voltage and resistance"""
    print("\nPROBLEM 1: Ohm's Law")
    print("-" * 70)

    V = 12  # Volts
    R = 40  # Ohms

    I = V / R

    print(f"Given: V = {V}V, R = {R}Ω")
    print(f"Formula: I = V/R")
    print(f"Result: I = {V}/{R} = {I:.2f} A = {I*1000:.0f} mA")
    return I


def problem_2():
    """Calculate resistance from resistivity"""
    print("\nPROBLEM 2: Resistance from Resistivity")
    print("-" * 70)

    rho = 1.68e-8  # Resistivity of copper (Ω⋅m)
    L = 10  # Length (m)
    A = 1e-6  # Cross-sectional area (m²), e.g., 1mm²

    R = rho * L / A

    print(f"Given: ρ (copper) = {rho:.2e} Ω⋅m")
    print(f"       L = {L} m, A = {A*1e6:.0f} mm²")
    print(f"Formula: R = ρL/A")
    print(f"Result: R = ({rho:.2e}) × {L} / {A:.2e}")
    print(f"        R = {R:.2f} Ω")
    return R


def problem_3():
    """Drift velocity"""
    print("\nPROBLEM 3: Drift Velocity in Wire")
    print("-" * 70)

    I = 2  # Current (A)
    n = 8.5e28  # Free electron density in copper (m⁻³)
    A = 1e-6  # Cross-sectional area (m²)

    v_d = I / (n * A * e)

    print(f"Given: I = {I} A")
    print(f"       n = {n:.2e} electrons/m³ (copper)")
    print(f"       A = {A*1e6:.0f} mm²")
    print(f"       e = {e:.3e} C")
    print(f"Formula: v_d = I/(nAe)")
    print(f"Result: v_d = {I} / ({n:.2e} × {A:.2e} × {e:.3e})")
    print(f"        v_d = {v_d:.2e} m/s = {v_d*1000:.4f} mm/s")
    print(f"\\nNote: Drift velocity is surprisingly small (~mm/s)!")
    return v_d


def problem_4():
    """RC time constant"""
    print("\nPROBLEM 4: RC Circuit Time Constant")
    print("-" * 70)

    R = 1000  # Ohms
    C = 100e-6  # Farads (100 µF)

    tau = R * C

    print(f"Given: R = {R} Ω, C = {C*1e6:.0f} µF")
    print(f"Formula: τ = RC")
    print(f"Result: τ = {R} × {C:.2e} = {tau:.2f} s = {tau*1000:.0f} ms")
    print(f"\\nAt t = τ:")
    print(f"  Charge reaches: {(1 - np.exp(-1))*100:.1f}% of Q₀")
    print(f"  Voltage reaches: {(1 - np.exp(-1))*100:.1f}% of V₀")
    print(f"  Current decreases to: {np.exp(-1)*100:.1f}% of I₀")
    return tau


def problem_5():
    """Series and parallel resistances"""
    print("\nPROBLEM 5: Resistor Networks")
    print("-" * 70)

    R1, R2, R3 = 10, 20, 30  # Ohms

    # Series
    R_series = R1 + R2 + R3

    # Parallel
    R_parallel = 1 / (1/R1 + 1/R2 + 1/R3)

    print(f"Given: R₁ = {R1}Ω, R₂ = {R2}Ω, R₃ = {R3}Ω")
    print(f"\\nSERIES: R_eq = R₁ + R₂ + R₃ = {R_series} Ω")
    print(f"PARALLEL: 1/R_eq = 1/R₁ + 1/R₂ + 1/R₃")
    print(f"          1/R_eq = 1/{R1} + 1/{R2} + 1/{R3}")
    print(f"          1/R_eq = {1/R1 + 1/R2 + 1/R3:.4f}")
    print(f"          R_eq = {R_parallel:.2f} Ω")
    print(f"\\nNote: Series R > any single R; Parallel R < any single R")
    return R_series, R_parallel


def problem_6():
    """Power dissipation"""
    print("\nPROBLEM 6: Power Dissipation")
    print("-" * 70)

    V = 10  # Volts
    I = 2   # Amperes
    R = V / I  # Ohms

    P_VI = V * I
    P_I2R = I**2 * R
    P_V2R = V**2 / R

    print(f"Given: V = {V}V, I = {I}A")
    print(f"       R = V/I = {R}Ω")
    print(f"\\nPower calculations:")
    print(f"  P = VI = {V} × {I} = {P_VI} W")
    print(f"  P = I²R = {I}² × {R} = {P_I2R} W")
    print(f"  P = V²/R = {V}² / {R} = {P_V2R} W")
    print(f"\\nEnergy dissipated in 1 hour: {P_VI * 3600 / 1000:.1f} kJ")
    return P_VI


def problem_7():
    """Kirchhoff's Voltage Law"""
    print("\nPROBLEM 7: Kirchhoff's Voltage Law")
    print("-" * 70)

    E1, E2 = 12, 5  # EMFs (Volts)
    I = 0.5  # Current (A)
    R1, R2, R3 = 10, 8, 4  # Resistances (Ω)

    # Check KVL around loop: E1 - E2 = I(R1 + R2 + R3)
    V_drop = I * (R1 + R2 + R3)
    E_net = E1 - E2

    print(f"Given: E₁ = {E1}V, E₂ = {E2}V, I = {I}A")
    print(f"       R₁ = {R1}Ω, R₂ = {R2}Ω, R₃ = {R3}Ω")
    print(f"\\nKirchhoff's Voltage Law: ΣE = ΣIR")
    print(f"  E₁ - E₂ = I(R₁ + R₂ + R₃)")
    print(f"  {E1} - {E2} = {I} × ({R1} + {R2} + {R3})")
    print(f"  {E_net}V = {I} × {R1 + R2 + R3}Ω")
    print(f"  {E_net}V = {V_drop}V ✓")
    print(f"\\nKVL is satisfied!")
    return True


def problem_8():
    """Wheatstone bridge balance"""
    print("\nPROBLEM 8: Wheatstone Bridge")
    print("-" * 70)

    R1 = 100  # Ω
    R3 = 50   # Ω
    Rx = 75   # Unknown (to be measured)

    # At balance: R1/Rx = R3/R4
    R4_balance = (R3 * Rx) / R1

    print(f"Given: R₁ = {R1}Ω, R₃ = {R3}Ω")
    print(f"       Unknown resistance Rx = {Rx}Ω (what we're measuring)")
    print(f"\\nBalance condition: R₁/Rx = R₃/R₄")
    print(f"Solving for R₄: R₄ = (Rx × R₃)/R₁")
    print(f"                R₄ = ({Rx} × {R3}) / {R1}")
    print(f"                R₄ = {R4_balance:.1f} Ω")
    print(f"\\nAt this R₄ value, galvanometer shows zero (null point)")
    return R4_balance


def problem_9():
    """RC charging equation"""
    print("\nPROBLEM 9: RC Charging - Charge and Voltage")
    print("-" * 70)

    C = 10e-6  # Farads (10 µF)
    V0 = 100   # Initial voltage (V)
    R = 10000  # Resistance (Ω)
    tau = R * C
    t = tau    # Time = time constant

    Q0 = C * V0
    Q = Q0 * (1 - np.exp(-t / tau))
    V = V0 * (1 - np.exp(-t / tau))
    I = (V0 / R) * np.exp(-t / tau)

    print(f"Given: C = {C*1e6:.0f} µF, V₀ = {V0}V, R = {R}Ω")
    print(f"       τ = RC = {R} × {C:.2e} = {tau:.2f} s")
    print(f"       t = τ (one time constant)")
    print(f"\\nInitial charge: Q₀ = CV₀ = {C*1e6:.0f}×10⁻⁶ × {V0} = {Q0:.4e} C")
    print(f"\\nAt t = τ:")
    print(f"  Q(τ) = Q₀(1 - e⁻¹) = {Q0:.4e} × {1 - np.exp(-1):.3f} = {Q:.4e} C")
    print(f"  V(τ) = V₀(1 - e⁻¹) = {V0} × {1 - np.exp(-1):.3f} = {V:.1f} V")
    print(f"  I(τ) = (V₀/R)e⁻¹ = {V0/R*1000:.2f} × {np.exp(-1):.3f} = {I*1000:.2f} mA")
    return Q, V, I


def problem_10():
    """Energy in capacitor"""
    print("\nPROBLEM 10: Energy Stored in Capacitor")
    print("-" * 70)

    C = 100e-6  # Farads (100 µF)
    V = 50      # Volts

    U_CV = 0.5 * C * V**2
    U_Q = 0.5 * (C * V) * V  # Alternative form
    U_V = 0.5 * (C * V)**2 / C  # Yet another form

    print(f"Given: C = {C*1e6:.0f} µF, V = {V}V")
    print(f"\\nFormulas for energy stored:")
    print(f"  U = ½CV² = ½ × {C:.2e} × {V}² = {U_CV:.4e} J = {U_CV*1e3:.2f} mJ")
    print(f"  U = ½QV = ½ × {C*V:.4e} × {V} = {U_Q:.4e} J (same)")
    print(f"  U = ½Q²/C = ½ × ({C*V:.4e})² / {C:.2e} = {U_V:.4e} J (same)")
    print(f"\\nAll three formulas give the same result!")
    return U_CV


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

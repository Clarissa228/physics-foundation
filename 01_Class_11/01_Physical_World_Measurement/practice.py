"""
Practice Exercises: Physical World and Measurement
Topic 1: Units, Dimensional Analysis, and Error Propagation

Instructions:
- Solve each exercise step by step
- Show all working and units
- Use numpy/sympy where appropriate
- Verify dimensional consistency
"""

import numpy as np
import sympy as sp
from sympy import symbols, simplify, expand, sqrt, pi, log, diff

# ============================================================================
# EXERCISE 1: Dimensional Analysis
# ============================================================================
"""
Exercise 1: Verify the dimensional consistency of the following equations.
Use SymPy to work with dimensions M, L, T symbolically.

a) v² = u² + 2as (kinematic equation)
b) E = ½mv² (kinetic energy)
c) T = 2π√(L/g) (period of simple pendulum)
d) P = F·v (power from force and velocity)
e) f = 1/(2π√(LC)) (resonant frequency in LC circuit)
"""

def exercise_1_dimensional_analysis():
    """Check dimensional consistency of physics equations."""

    print("\n" + "="*70)
    print("EXERCISE 1: Dimensional Analysis")
    print("="*70)

    # Define dimensions
    M, L, T = symbols('M L T', positive=True, real=True)

    equations = {
        'a) v² = u² + 2as': {
            'LHS': (L / T)**2,
            'RHS': (L / T)**2 + (L / T**2) * L
        },
        'b) E = ½mv²': {
            'LHS': M * L**2 / T**2,
            'RHS': M * (L / T)**2
        },
        'c) T = 2π√(L/g)': {
            'LHS': T,
            'RHS': sp.sqrt(L / (L / T**2))  # g has dimension [LT⁻²]
        },
        'd) P = F·v': {
            'LHS': M * L**2 / T**3,
            'RHS': (M * L / T**2) * (L / T)
        },
    }

    for eq_name, dims in equations.items():
        lhs = dims['LHS']
        rhs = simplify(dims['RHS'])
        consistent = simplify(lhs - rhs) == 0

        print(f"\n{eq_name}")
        print(f"  LHS: {lhs}")
        print(f"  RHS: {rhs}")
        print(f"  ✓ Dimensionally consistent!" if consistent else "  ✗ NOT consistent!")

    return True


# ============================================================================
# EXERCISE 2: Unit Conversions
# ============================================================================
"""
Exercise 2: Convert the following measurements to SI units.

a) 72 km/h → m/s
b) 500 g → kg
c) 2.5 cm² → m²
d) 150 cm³ → m³
e) 1 atm (atmospheric pressure) → Pa
   (1 atm = 101325 Pa)
f) 100°C → K
g) 50 miles → km
   (1 mile = 1.609 km)
"""

def exercise_2_unit_conversions():
    """Practice unit conversions to SI units."""

    print("\n" + "="*70)
    print("EXERCISE 2: Unit Conversions")
    print("="*70)

    conversions = [
        ("72 km/h", 72 * 1000 / 3600, "m/s"),
        ("500 g", 500 / 1000, "kg"),
        ("2.5 cm²", 2.5 * 1e-4, "m²"),
        ("150 cm³", 150 * 1e-6, "m³"),
        ("1 atm", 101325, "Pa"),
        ("100°C", 100 + 273.15, "K"),
        ("50 miles", 50 * 1.609, "km"),
    ]

    for original, converted, unit in conversions:
        print(f"{original:15s} = {converted:15.6g} {unit}")

    return conversions


# ============================================================================
# EXERCISE 3: Error Propagation
# ============================================================================
"""
Exercise 3: Calculate the uncertainty in the following measurements.

a) Resistance: R = V/I
   Where V = (5.0 ± 0.1) V and I = (2.0 ± 0.05) A

b) Acceleration: a = (v - u)/t
   Where v = (10.5 ± 0.3) m/s, u = (2.0 ± 0.2) m/s, t = (4.2 ± 0.1) s

c) Period of pendulum: T = 2π√(L/g)
   Where L = (0.95 ± 0.02) m, g = (9.81 ± 0.05) m/s²
"""

def exercise_3_error_propagation():
    """Practice error propagation calculations."""

    print("\n" + "="*70)
    print("EXERCISE 3: Error Propagation")
    print("="*70)

    # Part a) Resistance calculation
    print("\na) Resistance R = V/I")
    V = 5.0
    dV = 0.1
    I = 2.0
    dI = 0.05

    R = V / I
    rel_error_V = dV / V
    rel_error_I = dI / I
    rel_error_R = np.sqrt(rel_error_V**2 + rel_error_I**2)
    dR = rel_error_R * R

    print(f"   V = {V} ± {dV} V")
    print(f"   I = {I} ± {dI} A")
    print(f"   R = V/I = {R} ± {dR:.3f} Ω")
    print(f"   Relative error: {rel_error_R*100:.2f}%")

    # Part b) Acceleration calculation
    print("\nb) Acceleration a = (v - u)/t")
    v = 10.5
    dv = 0.3
    u = 2.0
    du = 0.2
    t = 4.2
    dt = 0.1

    a = (v - u) / t
    # For (v-u), errors add in quadrature
    d_v_minus_u = np.sqrt(dv**2 + du**2)
    # For division by t: rel_error = sqrt((d(v-u)/(v-u))² + (dt/t)²)
    rel_error_a = np.sqrt((d_v_minus_u/(v-u))**2 + (dt/t)**2)
    da = rel_error_a * a

    print(f"   v = {v} ± {dv} m/s")
    print(f"   u = {u} ± {du} m/s")
    print(f"   t = {t} ± {dt} s")
    print(f"   a = (v-u)/t = {a:.3f} ± {da:.3f} m/s²")
    print(f"   Relative error: {rel_error_a*100:.2f}%")

    # Part c) Pendulum period
    print("\nc) Period T = 2π√(L/g)")
    L = 0.95
    dL = 0.02
    g = 9.81
    dg = 0.05

    T = 2 * np.pi * np.sqrt(L / g)

    # Partial derivatives:
    # dT/dL = 2π * (1/2) * (1/√(L/g)) * (1/g) = π/√(Lg)
    # dT/dg = 2π * (1/2) * (1/√(L/g)) * (-L/g²) = -π√(L)/g^(3/2)
    dT_dL = np.pi / np.sqrt(L * g)
    dT_dg = -np.pi * np.sqrt(L) / (g**(3/2))

    dT = np.sqrt((dT_dL * dL)**2 + (dT_dg * dg)**2)
    rel_error_T = dT / T

    print(f"   L = {L} ± {dL} m")
    print(f"   g = {g} ± {dg} m/s²")
    print(f"   T = 2π√(L/g) = {T:.4f} ± {dT:.4f} s")
    print(f"   Relative error: {rel_error_T*100:.2f}%")

    return {
        'resistance': (R, dR),
        'acceleration': (a, da),
        'period': (T, dT)
    }


# ============================================================================
# EXERCISE 4: Significant Figures
# ============================================================================
"""
Exercise 4: Count significant figures and round appropriately.

a) How many significant figures in: 0.00456, 1.20, 1200, 2.5×10³?
b) Round 3.14159 to: 1, 2, 3, and 4 significant figures
c) A measurement gives 12.345 g with error 0.23 g.
   How should this be reported?
d) Calculate 2.5 × 3.14159 ÷ 1.2 and report with correct sig figs
"""

def exercise_4_significant_figures():
    """Practice with significant figures and rounding."""

    print("\n" + "="*70)
    print("EXERCISE 4: Significant Figures")
    print("="*70)

    # Part a) Count sig figs
    print("\na) Counting significant figures:")
    values = [
        ("0.00456", 3),
        ("1.20", 3),
        ("1200", "ambiguous (use 1.2×10³ for clarity)"),
        ("2.5×10³", 2),
    ]

    for val, sf in values:
        print(f"   {val:15s} → {sf} sig figs")

    # Part b) Round to different sig figs
    print("\nb) Rounding 3.14159:")
    original = 3.14159
    sig_figs = [1, 2, 3, 4]

    for sf in sig_figs:
        rounded = round(original, sf - 1)
        print(f"   {sf} sig figs: {rounded}")

    # Part c) Report with error
    print("\nc) Measurement with error: 12.345 ± 0.23 g")
    print("   Step 1: Round error to 1 sig fig → 0.2 g")
    print("   Step 2: Round value to same decimal place → 12.3 g")
    print("   Result: (12.3 ± 0.2) g")

    # Part d) Calculation with sig figs
    print("\nd) Calculation: 2.5 × 3.14159 ÷ 1.2")
    a = 2.5      # 2 sig figs
    b = 3.14159  # 6 sig figs
    c = 1.2      # 2 sig figs

    result_exact = a * b / c
    print(f"   Exact calculation: {result_exact:.6f}")
    print(f"   Limited by: 2.5 and 1.2 (2 sig figs each)")
    print(f"   Final answer: {result_exact:.0f} or 6.5 (2 sig figs)")

    return True


# ============================================================================
# EXERCISE 5: Measurement and Precision
# ============================================================================
"""
Exercise 5: Design an experiment to measure g (acceleration due to gravity).

Use a simple pendulum with:
- String length L = 1.0 m
- Period measured by timing 10 oscillations

a) Estimate the expected period T
b) If period is measured as T = (2.00 ± 0.05) s for 10 oscillations,
   find g using T = 2π√(L/g)
c) Calculate the uncertainty in g
d) How would you improve the measurement precision?
"""

def exercise_5_measurement_design():
    """Design and analyze a pendulum experiment to measure g."""

    print("\n" + "="*70)
    print("EXERCISE 5: Measuring g with a Simple Pendulum")
    print("="*70)

    # Part a) Expected period
    print("\na) Expected period of simple pendulum (L = 1.0 m):")
    L = 1.0
    g = 9.81

    T_expected = 2 * np.pi * np.sqrt(L / g)
    print(f"   T = 2π√(L/g) = 2π√({L}/{g})")
    print(f"   T = {T_expected:.4f} s for one oscillation")
    print(f"   For 10 oscillations: T_total = {10*T_expected:.2f} s")

    # Part b) Calculate g from measured period
    print("\nb) Measured period (10 oscillations): T_total = (20.0 ± 0.5) s")
    print("   Therefore, period per oscillation: T = (2.00 ± 0.05) s")

    T_measured = 2.00
    dT = 0.05

    # From T = 2π√(L/g), solve for g:
    # g = 4π²L/T²
    L = 1.0
    dL = 0.01  # Assume 1 cm precision on measuring string length

    g_calculated = 4 * np.pi**2 * L / T_measured**2

    print(f"\n   g = 4π²L/T² = 4π²({L})/{T_measured}²")
    print(f"   g = {g_calculated:.3f} m/s²")

    # Part c) Uncertainty in g
    print("\nc) Uncertainty in g:")

    # Partial derivatives
    dg_dL = 4 * np.pi**2 / T_measured**2
    dg_dT = -8 * np.pi**2 * L / T_measured**3

    dg = np.sqrt((dg_dL * dL)**2 + (dg_dT * dT)**2)
    rel_error = dg / g_calculated

    print(f"   dg/dL = 4π²/T² = {dg_dL:.3f}")
    print(f"   dg/dT = -8π²L/T³ = {dg_dT:.3f}")
    print(f"   dg = √((dg/dL·dL)² + (dg/dT·dT)²)")
    print(f"   dg = √(({dg_dL*dL:.4f})² + ({dg_dT*dT:.4f})²)")
    print(f"   dg = {dg:.3f} m/s²")
    print(f"\n   Result: g = ({g_calculated:.2f} ± {dg:.2f}) m/s²")
    print(f"   Relative uncertainty: {rel_error*100:.1f}%")

    # Part d) Improvement suggestions
    print("\nd) Methods to improve precision:")
    print("   1. Use longer string (L increases → larger T → less error)")
    print("   2. Time many oscillations (e.g., 50) instead of just 10")
    print("      → Reduces fractional error in period")
    print("   3. Use electronic timer instead of stopwatch")
    print("      → Reduce timing error")
    print("   4. Measure string length more carefully")
    print("      → Use meter stick or calipers")
    print("   5. Repeat measurement multiple times")
    print("      → Average reduces random errors")

    return {
        'g_measured': g_calculated,
        'uncertainty': dg,
        'relative_uncertainty': rel_error
    }


# ============================================================================
# EXERCISE 6: Error Analysis in Calculations
# ============================================================================
"""
Exercise 6: Density calculation.

A rectangular block has:
- Mass: m = (250 ± 2) g
- Length: L = (10.0 ± 0.1) cm
- Width: W = (5.0 ± 0.1) cm
- Height: H = (4.0 ± 0.1) cm

Calculate:
a) Volume V = L × W × H with uncertainty
b) Density ρ = m/V with uncertainty
c) Report final answer with appropriate significant figures
"""

def exercise_6_density_calculation():
    """Calculate density with full error analysis."""

    print("\n" + "="*70)
    print("EXERCISE 6: Density Measurement with Error Analysis")
    print("="*70)

    # Given measurements
    m = 250  # g
    dm = 2   # g
    L = 10.0  # cm
    dL = 0.1  # cm
    W = 5.0   # cm
    dW = 0.1  # cm
    H = 4.0   # cm
    dH = 0.1  # cm

    print(f"\nMeasurements:")
    print(f"  m = {m} ± {dm} g")
    print(f"  L = {L} ± {dL} cm")
    print(f"  W = {W} ± {dW} cm")
    print(f"  H = {H} ± {dH} cm")

    # Part a) Volume calculation
    print(f"\na) Volume V = L × W × H")
    V = L * W * H

    # For product, relative errors add in quadrature
    rel_dL = dL / L
    rel_dW = dW / W
    rel_dH = dH / H
    rel_dV = np.sqrt(rel_dL**2 + rel_dW**2 + rel_dH**2)
    dV = rel_dV * V

    print(f"   V = {L} × {W} × {H} = {V} cm³")
    print(f"   Relative errors: {rel_dL:.3f}, {rel_dW:.3f}, {rel_dH:.3f}")
    print(f"   Relative error in V: {rel_dV:.4f}")
    print(f"   dV = {dV:.2f} cm³")
    print(f"   V = ({V} ± {dV:.1f}) cm³")

    # Part b) Density calculation
    print(f"\nb) Density ρ = m/V")
    rho = m / V

    # For quotient, relative errors add
    rel_dm = dm / m
    rel_drho = np.sqrt(rel_dm**2 + rel_dV**2)
    drho = rel_drho * rho

    print(f"   ρ = {m}/{V} = {rho:.4f} g/cm³")
    print(f"   Relative error in m: {rel_dm:.4f}")
    print(f"   Relative error in V: {rel_dV:.4f}")
    print(f"   Relative error in ρ: {rel_drho:.4f}")
    print(f"   dρ = {drho:.4f} g/cm³")

    # Part c) Final result with sig figs
    print(f"\nc) Final Result:")
    print(f"   ρ = ({rho:.2f} ± {drho:.2f}) g/cm³")
    print(f"   or ρ = ({rho:.3f} ± {drho:.3f}) g/cm³")
    print(f"\n   Note: Report uncertainty to 1 sig fig")
    print(f"         Then round value to same decimal place")

    # Convert to SI units (kg/m³)
    rho_SI = rho * 1000  # 1 g/cm³ = 1000 kg/m³
    drho_SI = drho * 1000

    print(f"\n   In SI units:")
    print(f"   ρ = ({rho_SI:.0f} ± {drho_SI:.0f}) kg/m³")

    return {
        'volume': V,
        'volume_uncertainty': dV,
        'density': rho,
        'density_uncertainty': drho,
        'density_SI': rho_SI,
        'density_uncertainty_SI': drho_SI
    }


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("CLASS 11 PHYSICS: PRACTICE EXERCISES")
    print("Topic 1: Physical World and Measurement")
    print("="*70)

    # Run all exercises
    exercise_1_dimensional_analysis()
    conversions = exercise_2_unit_conversions()
    errors = exercise_3_error_propagation()
    exercise_4_significant_figures()
    results_5 = exercise_5_measurement_design()
    results_6 = exercise_6_density_calculation()

    print("\n" + "="*70)
    print("SUMMARY OF RESULTS")
    print("="*70)
    print(f"\nExercise 5 - Measurement of g:")
    print(f"  g = ({results_5['g_measured']:.2f} ± {results_5['uncertainty']:.2f}) m/s²")
    print(f"  Relative uncertainty: {results_5['relative_uncertainty']*100:.1f}%")

    print(f"\nExercise 6 - Density Calculation:")
    print(f"  ρ = ({results_6['density']:.4f} ± {results_6['density_uncertainty']:.4f}) g/cm³")
    print(f"  ρ = ({results_6['density_SI']:.0f} ± {results_6['density_uncertainty_SI']:.0f}) kg/m³")

    print("\n" + "="*70)
    print("End of Exercises")
    print("="*70 + "\n")

"""
Practice Exercises: Work, Energy, and Power
Topic 4
"""

import numpy as np

# ============================================================================
# EXERCISE 1: Work Calculations
# ============================================================================

def exercise_1_work():
    """Calculate work done by various forces."""
    print("\n" + "="*70)
    print("EXERCISE 1: Work Calculations")
    print("="*70)

    # Part a) Horizontal force
    print("\na) Pushing a box horizontally")
    print("-" * 70)
    F = 50  # N
    d = 10  # m
    angle = 0  # degrees (force parallel to motion)

    W = F * d * np.cos(np.radians(angle))
    print(f"Force F = {F} N, Distance d = {d} m, Angle θ = {angle}°")
    print(f"Work: W = F·d·cos(θ) = {F}×{d}×cos(0°) = {W} J")

    # Part b) Force at angle
    print("\n\nb) Pushing box at 30° below horizontal")
    print("-" * 70)
    angle_b = 30
    W_b = F * d * np.cos(np.radians(angle_b))
    print(f"Force F = {F} N at {angle_b}° to horizontal")
    print(f"Work: W = {F}×{d}×cos({angle_b}°) = {W_b:.1f} J")
    print(f"Note: 'cos(30°) = {np.cos(np.radians(angle_b)):.3f}, so W is less'")

    # Part c) Lifting vertically
    print("\n\nc) Lifting box vertically")
    print("-" * 70)
    m = 5  # kg
    h = 2  # m
    g = 9.81
    W_lift = m * g * h
    print(f"Mass m = {m} kg, Height h = {h} m")
    print(f"Work: W = mgh = {m}×{g}×{h} = {W_lift:.1f} J")

    # Part d) Friction
    print("\n\nd) Sliding block against friction")
    print("-" * 70)
    m = 10  # kg
    mu = 0.2
    d = 5  # m
    N = m * g
    f = mu * N
    W_friction = -f * d  # Negative because opposes motion

    print(f"Mass m = {m} kg, μ = {mu}, Distance d = {d} m")
    print(f"Friction force: f = μN = μmg = {f:.1f} N")
    print(f"Work by friction: W = -f·d = -{f:.1f}×{d} = {W_friction:.1f} J")
    print(f"(Negative because friction opposes motion)")

# ============================================================================
# EXERCISE 2: Energy Conservation
# ============================================================================

def exercise_2_energy():
    """Apply conservation of energy."""
    print("\n" + "="*70)
    print("EXERCISE 2: Conservation of Mechanical Energy")
    print("="*70)

    # Part a) Pendulum
    print("\na) Simple pendulum released from height h")
    print("-" * 70)
    h = 1  # m
    g = 9.81
    m = 1  # kg

    print(f"Initial: Object at height h = {h} m, at rest (v = 0)")
    PE_i = m * g * h
    KE_i = 0
    E_total = PE_i + KE_i

    print(f"  PE = mgh = {PE_i:.2f} J")
    print(f"  KE = 0 J")
    print(f"  E_total = {E_total:.2f} J")

    print(f"\nAt bottom (h = 0): All PE converts to KE")
    PE_f = 0
    KE_f = E_total
    v_f = np.sqrt(2 * KE_f / m)

    print(f"  PE = 0 J")
    print(f"  KE = {KE_f:.2f} J")
    print(f"  v = √(2KE/m) = √({2*KE_f}/{m}) = {v_f:.2f} m/s")
    print(f"  Or: v = √(2gh) = {np.sqrt(2*g*h):.2f} m/s")

    # Part b) Inclined plane
    print("\n\nb) Block sliding down frictionless incline (h = 2m)")
    print("-" * 70)
    h_b = 2  # m
    theta = 30  # degrees

    print(f"Height: h = {h_b} m, Angle: θ = {theta}°")
    print(f"\nInitial (at top): v = 0, h = {h_b}m")
    print(f"  E = mgh = {g*h_b:.2f}J (per kg)")

    print(f"\nFinal (at bottom): h = 0")
    print(f"  E = ½mv² = {g*h_b:.2f}J")
    print(f"  v = {np.sqrt(2*g*h_b):.2f} m/s")

    # Part c) With friction
    print("\n\nc) With friction: μ = 0.1")
    print("-" * 70)
    mu = 0.1
    N = np.cos(np.radians(theta))  # Per unit mg
    d = h_b / np.sin(np.radians(theta))  # Distance along plane
    W_friction = mu * N * d * g  # Friction work per kg

    print(f"Distance along plane: d = h/sin(θ) = {d:.2f} m")
    print(f"Friction force: f = μN = μmg·cos(θ)")
    print(f"Work by friction: W_f = {-W_friction*1:.2f}J (per kg)")

    KE_with_friction = g * h_b - W_friction
    v_with_friction = np.sqrt(2 * KE_with_friction)

    print(f"\nFinal KE: ½mv² = mgh - W_f = {KE_with_friction:.2f}J")
    print(f"v = {v_with_friction:.2f} m/s (reduced by friction)")

# ============================================================================
# EXERCISE 3: Power
# ============================================================================

def exercise_3_power():
    """Calculate power in various scenarios."""
    print("\n" + "="*70)
    print("EXERCISE 3: Power")
    print("="*70)

    # Part a) Lifting weight
    print("\na) Lifting 50 kg mass by 5 m")
    print("-" * 70)
    m = 50  # kg
    h = 5  # m
    g = 9.81
    W = m * g * h

    times = [5, 10, 20]
    print(f"Work required: W = mgh = {m}×{g}×{h} = {W:.0f} J")
    print(f"\nPower for different times:")
    for t in times:
        P = W / t
        print(f"  t = {t}s: P = W/t = {W:.0f}/{t} = {P:.0f} W = {P/1000:.2f} kW")

    # Part b) Car power
    print("\n\nb) Car: F = 2000 N, v = 30 m/s")
    print("-" * 70)
    F = 2000  # N
    v = 30  # m/s
    P = F * v

    print(f"Power: P = F·v = {F}×{v} = {P} W = {P/1000:.0f} kW")
    print(f"      P = {P/746:.0f} hp (1 hp = 746 W)")

    # Part c) Energy consumption
    print("\n\nc) 100W light bulb over 24 hours")
    print("-" * 70)
    P_bulb = 100  # W
    t_hours = 24
    t_seconds = t_hours * 3600

    E = P_bulb * t_seconds  # Joules
    E_kWh = E / 3.6e6

    print(f"Power: P = {P_bulb} W")
    print(f"Time: t = {t_hours} hours = {t_seconds} s")
    print(f"Energy: E = P·t = {P_bulb}×{t_seconds} = {E:.2e} J")
    print(f"      E = {E_kWh:.1f} kWh")
    print(f"Cost: ~${E_kWh*0.12:.2f} (at $0.12/kWh)")

# ============================================================================
# EXERCISE 4: Collisions
# ============================================================================

def exercise_4_collisions():
    """Analyze elastic and inelastic collisions."""
    print("\n" + "="*70)
    print("EXERCISE 4: Collisions")
    print("="*70)

    # Part a) Elastic collision
    print("\na) ELASTIC COLLISION")
    print("-" * 70)
    m1, m2 = 2, 3  # kg
    v1_i, v2_i = 6, 0  # m/s

    print(f"Before: m₁={m1}kg @ {v1_i}m/s, m₂={m2}kg @ {v2_i}m/s")

    # Elastic collision formulas
    v1_f = ((m1 - m2) * v1_i + 2 * m2 * v2_i) / (m1 + m2)
    v2_f = ((m2 - m1) * v2_i + 2 * m1 * v1_i) / (m1 + m2)

    KE_i = 0.5 * (m1 * v1_i**2 + m2 * v2_i**2)
    KE_f = 0.5 * (m1 * v1_f**2 + m2 * v2_f**2)
    p_i = m1 * v1_i + m2 * v2_i
    p_f = m1 * v1_f + m2 * v2_f

    print(f"\nAfter: v₁={v1_f:.2f}m/s, v₂={v2_f:.2f}m/s")
    print(f"Momentum: {p_i:.1f} → {p_f:.1f} kg·m/s ✓")
    print(f"KE: {KE_i:.1f} → {KE_f:.1f} J ✓")
    print(f"Both conserved!")

    # Part b) Perfectly inelastic
    print("\n\nb) PERFECTLY INELASTIC COLLISION (stick together)")
    print("-" * 70)

    print(f"Before: Same setup as above")
    v_final = (m1 * v1_i + m2 * v2_i) / (m1 + m2)

    KE_final = 0.5 * (m1 + m2) * v_final**2
    KE_lost = KE_i - KE_final

    print(f"\nAfter: Both move together at v={v_final:.2f} m/s")
    print(f"Momentum: {p_i:.1f} kg·m/s ✓ (conserved)")
    print(f"KE: {KE_i:.1f} J → {KE_final:.1f} J")
    print(f"Energy lost: {KE_lost:.1f} J ({KE_lost/KE_i*100:.1f}%)")
    print(f"(converted to heat, deformation, sound)")

# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("CLASS 11 PHYSICS: WORK, ENERGY, AND POWER - EXERCISES")
    print("="*70)

    exercise_1_work()
    exercise_2_energy()
    exercise_3_power()
    exercise_4_collisions()

    print("\n" + "="*70 + "\n")

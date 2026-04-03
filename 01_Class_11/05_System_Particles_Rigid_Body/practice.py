"""
Practice Exercises: System of Particles and Rigid Body Motion
Topic 5

Covers: Center of mass, moment of inertia, torque, angular momentum
"""

import numpy as np

# ============================================================================
# EXERCISE 1: Center of Mass
# ============================================================================
"""
Exercise 1: Calculate center of mass for various systems

a) Three point masses: m₁=2kg at (0,0), m₂=3kg at (1,0), m₃=1kg at (0,2)
b) Uniform rod of mass M and length L (calculate using integration)
c) Two-body system with m₁=4kg, m₂=6kg separated by 1m
"""

def exercise_1_center_of_mass():
    """Calculate center of mass for different systems."""
    print("\n" + "="*70)
    print("EXERCISE 1: Center of Mass")
    print("="*70)

    # Part a) Discrete masses
    print("\na) Three point masses (2D)")
    print("-" * 70)
    m1, m2, m3 = 2, 3, 1
    r1, r2, r3 = np.array([0, 0]), np.array([1, 0]), np.array([0, 2])

    M_total = m1 + m2 + m3
    x_cm = (m1*r1[0] + m2*r2[0] + m3*r3[0]) / M_total
    y_cm = (m1*r1[1] + m2*r2[1] + m3*r3[1]) / M_total

    print(f"Masses: m₁={m1}kg at {r1}, m₂={m2}kg at {r2}, m₃={m3}kg at {r3}")
    print(f"Total mass: M = {M_total} kg")
    print(f"\nx_cm = (m₁x₁ + m₂x₂ + m₃x₃)/M")
    print(f"     = ({m1}×0 + {m2}×1 + {m3}×0)/{M_total} = {x_cm:.3f}")
    print(f"\ny_cm = (m₁y₁ + m₂y₂ + m₃y₃)/M")
    print(f"     = ({m1}×0 + {m2}×0 + {m3}×2)/{M_total} = {y_cm:.3f}")
    print(f"\nCenter of mass: ({x_cm:.3f}, {y_cm:.3f})")

    # Part b) Uniform rod (continuous)
    print("\n\nb) Uniform rod (mass M, length L)")
    print("-" * 70)
    print(f"For uniform rod along x-axis from 0 to L:")
    print(f"  dm = (M/L)dx")
    print(f"  x_cm = ∫₀ᴸ x·dm / M = ∫₀ᴸ x·(M/L)dx / M")
    print(f"       = (1/L)∫₀ᴸ x dx = (1/L)[x²/2]₀ᴸ")
    print(f"       = L/2")
    print(f"\nCenter of mass is at the geometric center (L/2 from either end)")

    # Part c) Two-body system
    print("\n\nc) Two-body system (reduced mass)")
    print("-" * 70)
    m1, m2 = 4, 6
    d = 1  # distance between them

    x_cm_2body = (m1*0 + m2*d) / (m1 + m2)
    print(f"Masses: m₁={m1}kg at x=0, m₂={m2}kg at x={d}m")
    print(f"x_cm = (m₁×0 + m₂×{d})/(m₁+m₂) = {m2}/(10) = {x_cm_2body} m")
    print(f"\nNote: Center of mass is closer to the heavier mass")

    return {
        'cm_2d': (x_cm, y_cm),
        'rod_cm': 'L/2',
        'two_body_cm': x_cm_2body
    }


# ============================================================================
# EXERCISE 2: Moment of Inertia
# ============================================================================
"""
Exercise 2: Calculate moment of inertia

a) Three point masses rotating about axis
b) Solid cylinder rolling
c) Parallel axis theorem application
"""

def exercise_2_moment_of_inertia():
    """Calculate moment of inertia."""
    print("\n" + "="*70)
    print("EXERCISE 2: Moment of Inertia")
    print("="*70)

    # Part a) Point masses
    print("\na) Three point masses rotating about axis")
    print("-" * 70)
    masses = np.array([2, 3, 1])  # kg
    distances = np.array([1, 2, 3])  # m from axis

    I = np.sum(masses * distances**2)

    print(f"Masses: m = {masses} kg")
    print(f"Distances from axis: r = {distances} m")
    print(f"\nI = Σmᵢrᵢ²")
    print(f"  = {masses[0]}×{distances[0]}² + {masses[1]}×{distances[1]}² + {masses[2]}×{distances[2]}²")
    print(f"  = {masses[0]*distances[0]**2} + {masses[1]*distances[1]**2} + {masses[2]*distances[2]**2}")
    print(f"  = {I} kg·m²")

    # Part b) Common shapes
    print("\n\nb) Common rotating objects")
    print("-" * 70)
    M = 5  # kg (mass)
    R = 0.5  # m (radius)
    L = 2  # m (length)

    shapes = {
        'Solid cylinder': 0.5 * M * R**2,
        'Thin hoop': M * R**2,
        'Solid sphere': 0.4 * M * R**2,
        'Thin rod (center)': (1/12) * M * L**2,
        'Thin rod (end)': (1/3) * M * L**2,
    }

    print(f"For mass M = {M} kg, radius R = {R} m, length L = {L} m:")
    for name, I_val in shapes.items():
        print(f"  {name:25s}: I = {I_val:.4f} kg·m²")

    # Part c) Parallel axis theorem
    print("\n\nc) Parallel Axis Theorem")
    print("-" * 70)
    M = 10  # kg (total mass)
    L = 2  # m (length)
    d = 1  # m (distance from center to new axis)

    I_cm = (1/12) * M * L**2  # About center
    I_parallel = I_cm + M * d**2  # About new axis

    print(f"Rod: M = {M} kg, L = {L} m")
    print(f"I_cm (about center) = (1/12)ML² = {I_cm:.4f} kg·m²")
    print(f"New axis at distance d = {d} m from center")
    print(f"I_new = I_cm + Md² = {I_cm:.4f} + {M}×{d}² = {I_parallel:.4f} kg·m²")

    return {
        'discrete_I': I,
        'cylinder_I': 0.5 * M * R**2,
        'parallel_I': I_parallel
    }


# ============================================================================
# EXERCISE 3: Rotational Dynamics
# ============================================================================
"""
Exercise 3: Torque and angular acceleration

a) Spinning wheel: τ = 50 N·m, I = 2 kg·m²
   Find angular acceleration and energy after 5 seconds

b) Pulley system: mass hanging creates torque
"""

def exercise_3_rotational_dynamics():
    """Solve rotational dynamics problems."""
    print("\n" + "="*70)
    print("EXERCISE 3: Rotational Dynamics (τ = Iα)")
    print("="*70)

    # Part a) Spinning wheel
    print("\na) Spinning wheel with constant torque")
    print("-" * 70)
    tau = 50  # N·m
    I = 2  # kg·m²
    t = 5  # seconds

    alpha = tau / I
    omega_final = 0 + alpha * t  # Starting from rest
    theta = 0.5 * alpha * t**2

    KE_final = 0.5 * I * omega_final**2
    W_done = tau * theta

    print(f"Torque: τ = {tau} N·m")
    print(f"Moment of inertia: I = {I} kg·m²")
    print(f"\nAngular acceleration: α = τ/I = {tau}/{I} = {alpha} rad/s²")
    print(f"After t = {t} seconds:")
    print(f"  Angular velocity: ω = αt = {alpha}×{t} = {omega_final} rad/s")
    print(f"  Angular displacement: θ = ½αt² = {theta} rad")
    print(f"  Rotations: {theta/(2*np.pi):.1f}")
    print(f"\nEnergy:")
    print(f"  Work done: W = τθ = {tau}×{theta} = {W_done} J")
    print(f"  Final KE: KE = ½Iω² = {KE_final} J")
    print(f"  (Work = ΔKE ✓)")

    # Part b) Falling mass creates torque
    print("\n\nb) Falling mass on pulley system")
    print("-" * 70)
    M = 2  # kg (hanging mass)
    m_pulley = 1  # kg (pulley mass)
    R = 0.2  # m (pulley radius)
    g = 9.81  # m/s²

    I_pulley = 0.5 * m_pulley * R**2  # Solid cylinder

    # Torque from tension: τ = T·R
    # For falling mass: Mg - T = Ma
    # For pulley: τ = Iα, and a = αR (constraint)
    # Solving: a = Mg/(M + I/R²)

    a = (M*g) / (M + I_pulley/R**2)
    T = M * (g - a)
    tau_pulley = T * R
    alpha_pulley = tau_pulley / I_pulley

    print(f"Hanging mass: M = {M} kg")
    print(f"Pulley: m = {m_pulley} kg, R = {R} m")
    print(f"I = (1/2)mR² = {I_pulley:.4f} kg·m²")
    print(f"\nLinear acceleration of mass: a = {a:.3f} m/s²")
    print(f"Tension in string: T = {T:.2f} N")
    print(f"Torque on pulley: τ = TR = {tau_pulley:.3f} N·m")
    print(f"Angular acceleration: α = τ/I = {alpha_pulley:.2f} rad/s²")
    print(f"Check: a = αR = {alpha_pulley:.2f}×{R} = {alpha_pulley*R:.3f} ✓")

    return {
        'angular_velocity': omega_final,
        'angular_displacement': theta,
        'linear_acceleration': a
    }


# ============================================================================
# EXERCISE 4: Angular Momentum Conservation
# ============================================================================
"""
Exercise 4: Conservation of angular momentum

a) Ice skater: I₁=3kg·m², ω₁=2rad/s → I₂=1kg·m², ω₂=?
b) Collision creating rotation
"""

def exercise_4_angular_momentum():
    """Angular momentum conservation."""
    print("\n" + "="*70)
    print("EXERCISE 4: Angular Momentum Conservation")
    print("="*70)

    # Part a) Ice skater
    print("\na) Ice skater pulling arms in")
    print("-" * 70)
    I1 = 3  # kg·m² (arms extended)
    omega1 = 2  # rad/s
    I2 = 1  # kg·m² (arms pulled in)

    L = I1 * omega1  # Angular momentum (conserved)
    omega2 = L / I2

    KE1 = 0.5 * I1 * omega1**2
    KE2 = 0.5 * I2 * omega2**2

    print(f"Initial state (arms extended):")
    print(f"  I₁ = {I1} kg·m²")
    print(f"  ω₁ = {omega1} rad/s")
    print(f"  L = I₁ω₁ = {L} kg·m²/s")
    print(f"  KE₁ = ½I₁ω₁² = {KE1} J")

    print(f"\nFinal state (arms pulled in):")
    print(f"  I₂ = {I2} kg·m²")
    print(f"  L conserved: ω₂ = L/I₂ = {L}/{I2} = {omega2} rad/s")
    print(f"  KE₂ = ½I₂ω₂² = {KE2} J")

    print(f"\nAnalysis:")
    print(f"  Angular velocity increases by factor: {omega2/omega1}")
    print(f"  Kinetic energy increases from {KE1} to {KE2} J")
    print(f"  Extra energy ({KE2-KE1:.0f} J) comes from muscle work")

    # Part b) Rolling without slipping
    print("\n\nb) Rolling without slipping condition")
    print("-" * 70)
    M = 2  # kg (sphere)
    R = 0.1  # m (radius)
    v = 3  # m/s (linear velocity)

    # I = (2/5)MR² for sphere
    I_sphere = 0.4 * M * R**2
    omega = v / R
    L_linear = M * v  # Linear momentum
    L_angular = I_sphere * omega

    print(f"Solid sphere: M = {M} kg, R = {R} m")
    print(f"Linear velocity: v = {v} m/s")
    print(f"I = (2/5)MR² = {I_sphere:.4f} kg·m²")
    print(f"\nRolling condition: v = Rω")
    print(f"Angular velocity: ω = v/R = {omega:.1f} rad/s")
    print(f"\nLinear momentum: p = Mv = {L_linear} kg·m/s")
    print(f"Angular momentum: L = Iω = {L_angular:.4f} kg·m²/s")


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("CLASS 11 PHYSICS: SYSTEMS OF PARTICLES & RIGID BODY MOTION")
    print("="*70)

    results_1 = exercise_1_center_of_mass()
    results_2 = exercise_2_moment_of_inertia()
    results_3 = exercise_3_rotational_dynamics()
    exercise_4_angular_momentum()

    print("\n" + "="*70)
    print("SUMMARY OF KEY RESULTS")
    print("="*70)
    print(f"\nExercise 1 - Center of Mass:")
    print(f"  Three masses: ({results_1['cm_2d'][0]:.3f}, {results_1['cm_2d'][1]:.3f})")
    print(f"  Two-body system: x_cm = {results_1['two_body_cm']:.3f} m")

    print(f"\nExercise 2 - Moment of Inertia:")
    print(f"  Discrete system: I = {results_2['discrete_I']} kg·m²")
    print(f"  Cylinder (solid): I = {results_2['cylinder_I']:.4f} kg·m²")

    print(f"\nExercise 3 - Rotational Dynamics:")
    print(f"  Final angular velocity: {results_3['angular_velocity']:.1f} rad/s")
    print(f"  Falling mass acceleration: {results_3['linear_acceleration']:.3f} m/s²")

    print("\n" + "="*70 + "\n")

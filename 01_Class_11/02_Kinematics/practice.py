"""
Practice Exercises: Kinematics
Topic 2: Motion and Projectiles

Exercises covering:
- SUVAT equations
- Vector operations
- Projectile motion
- Circular motion kinematics
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# EXERCISE 1: SUVAT Problems
# ============================================================================
"""
Exercise 1: Solve using kinematic equations

a) A car starts from rest and accelerates uniformly at 3 m/s² for 8 seconds.
   Find: i) final velocity  ii) distance traveled

b) A train traveling at 30 m/s applies brakes with deceleration 2 m/s².
   Find: i) time to stop  ii) distance traveled

c) A stone is thrown upward with initial velocity 20 m/s.
   Taking g = 10 m/s² (downward), find:
   i) time to reach maximum height
   ii) maximum height reached
   iii) time to return to starting point
   iv) velocity when returning
"""

def exercise_1_suvat():
    """Solve SUVAT kinematic problems."""

    print("\n" + "="*70)
    print("EXERCISE 1: SUVAT Kinematic Equations")
    print("="*70)

    # Part a) Car acceleration from rest
    print("\na) Car acceleration from rest")
    print("-" * 70)
    u_car = 0      # m/s (starts from rest)
    a_car = 3      # m/s² (acceleration)
    t_car = 8      # seconds

    # v = u + at
    v_car = u_car + a_car * t_car
    # s = ut + ½at²
    s_car = u_car * t_car + 0.5 * a_car * t_car**2

    print(f"Initial velocity u = {u_car} m/s")
    print(f"Acceleration a = {a_car} m/s²")
    print(f"Time t = {t_car} s")
    print(f"\ni) Final velocity: v = u + at = 0 + {a_car}×{t_car} = {v_car} m/s")
    print(f"ii) Distance: s = ut + ½at² = 0 + ½×{a_car}×{t_car}² = {s_car} m")

    # Part b) Train braking
    print("\n\nb) Train braking to stop")
    print("-" * 70)
    u_train = 30     # m/s
    a_train = -2     # m/s² (deceleration)
    v_train_final = 0  # comes to stop

    # v = u + at → t = (v - u)/a
    t_train = (v_train_final - u_train) / a_train
    # s = ut + ½at²
    s_train = u_train * t_train + 0.5 * a_train * t_train**2
    # Alternative: v² = u² + 2as
    s_train_alt = (v_train_final**2 - u_train**2) / (2 * a_train)

    print(f"Initial velocity u = {u_train} m/s")
    print(f"Deceleration a = {a_train} m/s²")
    print(f"Final velocity v = {v_train_final} m/s (stops)")
    print(f"\ni) Time to stop: v = u + at")
    print(f"   {v_train_final} = {u_train} + {a_train}×t")
    print(f"   t = {t_train} s")
    print(f"ii) Distance: s = ut + ½at² = {u_train}×{t_train} + ½×{a_train}×{t_train}²")
    print(f"    s = {s_train} m")
    print(f"\nVerification: v² = u² + 2as")
    print(f"0 = {u_train}² + 2×{a_train}×s → s = {s_train_alt} m ✓")

    # Part c) Stone thrown upward
    print("\n\nc) Stone thrown upward")
    print("-" * 70)
    u_stone = 20   # m/s
    g = 10         # m/s² (downward)
    a_stone = -g   # acceleration = -g (negative because upward is positive)

    # Time to max height (when v = 0)
    t_max_height = -u_stone / a_stone
    # Max height: s = ut + ½at²
    h_max = u_stone * t_max_height + 0.5 * a_stone * t_max_height**2
    # Alternative: v² = u² + 2as → 0 = u² + 2as
    h_max_alt = -u_stone**2 / (2 * a_stone)
    # Time to return (when s = 0 again)
    # 0 = ut + ½at² → t(u + ½at) = 0 → t = -2u/a
    t_return = -2 * u_stone / a_stone
    # Velocity when returning (same magnitude as initial)
    v_return = u_stone + a_stone * t_return

    print(f"Initial velocity u = {u_stone} m/s (upward)")
    print(f"Acceleration a = {a_stone} m/s² (gravity, downward)")
    print(f"\ni) Time to max height (v = 0):")
    print(f"   v = u + at → 0 = {u_stone} + {a_stone}×t")
    print(f"   t = {t_max_height} s")
    print(f"\nii) Maximum height:")
    print(f"   s = ut + ½at² = {u_stone}×{t_max_height} + ½×{a_stone}×{t_max_height}²")
    print(f"   s = {h_max} m")
    print(f"   (or h = u²/(2g) = {u_stone}²/(2×{g}) = {h_max_alt} m)")
    print(f"\niii) Time to return to starting point (s = 0):")
    print(f"    s = ut + ½at²")
    print(f"    0 = {u_stone}×t + ½×{a_stone}×t²")
    print(f"    0 = t({u_stone} + ½×{a_stone}×t)")
    print(f"    t = 0 (start) or t = {t_return} s (return)")
    print(f"\niv) Velocity on return:")
    print(f"    v = u + at = {u_stone} + {a_stone}×{t_return} = {v_return} m/s")
    print(f"    Same magnitude as initial, but DOWNWARD")

    return {
        'car_velocity': v_car,
        'car_distance': s_car,
        'train_time': t_train,
        'train_distance': s_train,
        'max_height': h_max,
        'time_return': t_return
    }


# ============================================================================
# EXERCISE 2: Vector Operations
# ============================================================================
"""
Exercise 2: Vector calculations

Given vectors:
A = (3, 4, 0) m
B = (1, 2, 2) m
C = (0, -1, 3) m

Find:
a) Magnitude of each vector
b) A·B (dot product) and angle between A and B
c) A×B (cross product)
d) Unit vector in direction of C
e) A + B and |A + B|
"""

def exercise_2_vectors():
    """Vector operations practice."""

    print("\n" + "="*70)
    print("EXERCISE 2: Vector Operations")
    print("="*70)

    # Define vectors
    A = np.array([3, 4, 0])
    B = np.array([1, 2, 2])
    C = np.array([0, -1, 3])

    print(f"\nGiven vectors:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")

    # Part a) Magnitudes
    print("\n\na) MAGNITUDES")
    print("-" * 70)
    mag_A = np.linalg.norm(A)
    mag_B = np.linalg.norm(B)
    mag_C = np.linalg.norm(C)

    print(f"|A| = √(3² + 4² + 0²) = √25 = {mag_A}")
    print(f"|B| = √(1² + 2² + 2²) = √9 = {mag_B}")
    print(f"|C| = √(0² + (-1)² + 3²) = √10 = {mag_C:.4f}")

    # Part b) Dot product and angle
    print("\n\nb) DOT PRODUCT AND ANGLE")
    print("-" * 70)
    dot_AB = np.dot(A, B)
    cos_angle = dot_AB / (mag_A * mag_B)
    angle_rad = np.arccos(cos_angle)
    angle_deg = np.degrees(angle_rad)

    print(f"A·B = (3)(1) + (4)(2) + (0)(2) = 3 + 8 + 0 = {dot_AB}")
    print(f"\ncos(θ) = (A·B)/(|A||B|) = {dot_AB}/({mag_A}×{mag_B}) = {cos_angle:.4f}")
    print(f"θ = arccos({cos_angle:.4f}) = {angle_deg:.2f}°")

    # Part c) Cross product
    print("\n\nc) CROSS PRODUCT")
    print("-" * 70)
    cross_AB = np.cross(A, B)
    mag_cross = np.linalg.norm(cross_AB)

    print(f"A×B = |i  j  k |")
    print(f"      |3  4  0|")
    print(f"      |1  2  2|")
    print(f"\nA×B = i(4×2 - 0×2) - j(3×2 - 0×1) + k(3×2 - 4×1)")
    print(f"    = i(8) - j(6) + k(2)")
    print(f"    = {cross_AB}")
    print(f"\n|A×B| = √(8² + (-6)² + 2²) = √104 = {mag_cross:.4f}")
    print(f"\nAlternative: |A×B| = |A||B|sin(θ)")
    sin_angle = np.sin(angle_rad)
    mag_cross_alt = mag_A * mag_B * sin_angle
    print(f"           = {mag_A} × {mag_B} × sin({angle_deg:.2f}°)")
    print(f"           = {mag_cross_alt:.4f} ✓")

    # Part d) Unit vector
    print("\n\nd) UNIT VECTOR")
    print("-" * 70)
    unit_C = C / mag_C
    print(f"Unit vector in direction of C:")
    print(f"Ĉ = C/|C| = {C}/{mag_C:.4f}")
    print(f"  = {unit_C}")
    print(f"\nVerification: |Ĉ| = {np.linalg.norm(unit_C):.4f} (should be 1.0)")

    # Part e) Vector addition
    print("\n\ne) VECTOR ADDITION")
    print("-" * 70)
    sum_AB = A + B
    mag_sum = np.linalg.norm(sum_AB)

    print(f"A + B = {A} + {B}")
    print(f"      = {sum_AB}")
    print(f"\n|A + B| = √(4² + 6² + 2²) = √56 = {mag_sum:.4f}")
    print(f"\nNote: |A + B| ≠ |A| + |B|")
    print(f"|A| + |B| = {mag_A} + {mag_B} = {mag_A + mag_B}")
    print(f"|A + B| = {mag_sum:.4f}")
    print(f"This is the triangle inequality: |A + B| ≤ |A| + |B|")

    return {
        'magnitudes': (mag_A, mag_B, mag_C),
        'dot_product': dot_AB,
        'angle': angle_deg,
        'cross_product': cross_AB,
        'unit_C': unit_C,
        'sum': sum_AB
    }


# ============================================================================
# EXERCISE 3: Projectile Motion
# ============================================================================
"""
Exercise 3: Projectile motion calculation

A ball is kicked horizontally off a cliff 45 m high with initial speed 20 m/s.

Find:
a) Time to hit the ground
b) Horizontal distance traveled (range)
c) Velocity when hitting the ground (magnitude and direction)
d) Position at t = 1.5 s
"""

def exercise_3_projectile():
    """Projectile motion problem."""

    print("\n" + "="*70)
    print("EXERCISE 3: Projectile Motion - Ball Off Cliff")
    print("="*70)

    h = 45        # m (height of cliff)
    v0x = 20      # m/s (horizontal velocity)
    v0y = 0       # m/s (no initial vertical velocity - kicked horizontally)
    g = 9.81      # m/s² (acceleration due to gravity)

    print(f"\nInitial conditions:")
    print(f"Height of cliff: h = {h} m")
    print(f"Initial horizontal velocity: v₀ₓ = {v0x} m/s")
    print(f"Initial vertical velocity: v₀ᵧ = {v0y} m/s")
    print(f"Acceleration: g = {g} m/s²")

    # Part a) Time to hit ground
    print("\n\na) TIME TO HIT GROUND")
    print("-" * 70)
    print(f"Vertical motion: y = v₀ᵧ×t - ½g×t²")
    print(f"When hitting ground, y = -h")
    print(f"-{h} = 0 - ½×{g}×t²")
    print(f"t² = {2*h/g:.4f}")
    t_ground = np.sqrt(2 * h / g)
    print(f"t = {t_ground:.3f} s")

    # Part b) Range
    print("\n\nb) HORIZONTAL DISTANCE (RANGE)")
    print("-" * 70)
    print(f"Horizontal motion: x = v₀ₓ×t (constant velocity)")
    R = v0x * t_ground
    print(f"x = {v0x} × {t_ground:.3f} = {R:.2f} m")

    # Part c) Velocity when hitting ground
    print("\n\nc) VELOCITY AT IMPACT")
    print("-" * 70)
    vx_final = v0x  # Horizontal velocity unchanged
    vy_final = v0y - g * t_ground  # Vertical velocity

    v_final = np.sqrt(vx_final**2 + vy_final**2)
    angle_impact = np.degrees(np.arctan2(-vy_final, vx_final))  # Negative because downward

    print(f"Horizontal component: vₓ = {vx_final} m/s (unchanged)")
    print(f"Vertical component: vᵧ = v₀ᵧ - g×t = 0 - {g}×{t_ground:.3f}")
    print(f"                       = {vy_final:.3f} m/s (downward)")
    print(f"\nMagnitude: v = √(vₓ² + vᵧ²) = √({vx_final}² + {vy_final:.3f}²)")
    print(f"         v = {v_final:.3f} m/s")
    print(f"\nDirection: θ = arctan(|vᵧ|/vₓ) = arctan({abs(vy_final):.3f}/{vx_final})")
    print(f"         θ = {angle_impact:.2f}° below horizontal")

    # Part d) Position at specific time
    print("\n\nd) POSITION AT t = 1.5 s")
    print("-" * 70)
    t_check = 1.5
    if t_check < t_ground:
        x_check = v0x * t_check
        y_check = h - (0.5 * g * t_check**2)  # Height above ground
        vx_check = v0x
        vy_check = -g * t_check

        print(f"At t = {t_check} s:")
        print(f"Horizontal position: x = {v0x}×{t_check} = {x_check} m")
        print(f"Vertical position: y = {h} - ½×{g}×{t_check}² = {y_check:.2f} m")
        print(f"Height above ground: {y_check:.2f} m")
        print(f"Velocity: vₓ = {vx_check} m/s, vᵧ = {vy_check:.2f} m/s")
        v_check = np.sqrt(vx_check**2 + vy_check**2)
        print(f"Speed: v = {v_check:.2f} m/s")
    else:
        print(f"t = {t_check} s is after impact (impact at t = {t_ground:.3f} s)")

    return {
        'time_to_ground': t_ground,
        'range': R,
        'velocity_magnitude': v_final,
        'angle_at_impact': angle_impact
    }


# ============================================================================
# EXERCISE 4: Circular Motion Kinematics
# ============================================================================
"""
Exercise 4: Circular motion

A car travels around a circular track of radius 50 m at constant speed 15 m/s.

Find:
a) Angular velocity
b) Period of one lap
c) Frequency
d) Centripetal acceleration
e) Angle traveled in 5 seconds
"""

def exercise_4_circular_motion():
    """Circular motion kinematics."""

    print("\n" + "="*70)
    print("EXERCISE 4: Circular Motion Kinematics")
    print("="*70)

    r = 50      # m (radius)
    v = 15      # m/s (tangential speed)
    t_total = 5 # s (time interval)

    print(f"\nGiven:")
    print(f"Radius of track: r = {r} m")
    print(f"Tangential speed: v = {v} m/s (constant)")

    # Part a) Angular velocity
    print("\n\na) ANGULAR VELOCITY")
    print("-" * 70)
    omega = v / r
    print(f"ω = v/r = {v}/{r} = {omega} rad/s")
    print(f"ω = {omega:.4f} rad/s")

    # Part b) Period
    print("\n\nb) PERIOD OF ONE LAP")
    print("-" * 70)
    T = 2 * np.pi / omega
    print(f"Period: T = 2π/ω = 2π/{omega:.4f}")
    print(f"T = {T:.3f} s")
    print(f"Or: T = 2πr/v = 2π×{r}/{v} = {T:.3f} s")

    # Part c) Frequency
    print("\n\nc) FREQUENCY")
    print("-" * 70)
    f = 1 / T
    print(f"Frequency: f = 1/T = 1/{T:.3f}")
    print(f"f = {f:.4f} Hz")
    print(f"This means {f:.4f} laps per second")

    # Part d) Centripetal acceleration
    print("\n\nd) CENTRIPETAL ACCELERATION")
    print("-" * 70)
    ac = v**2 / r
    ac_alt = omega**2 * r
    print(f"Centripetal acceleration (using v²/r):")
    print(f"aᶜ = v²/r = {v}²/{r} = {ac:.3f} m/s²")
    print(f"\nAlternative (using ω²r):")
    print(f"aᶜ = ω²×r = {omega:.4f}²×{r} = {ac_alt:.3f} m/s² ✓")
    print(f"\nDirection: Always toward center of circle")

    # Part e) Angle traveled
    print("\n\ne) ANGLE TRAVELED IN 5 SECONDS")
    print("-" * 70)
    theta_rad = omega * t_total
    theta_deg = np.degrees(theta_rad)
    n_laps = theta_rad / (2 * np.pi)

    print(f"θ = ω×t = {omega}×{t_total} = {theta_rad:.3f} rad")
    print(f"θ = {theta_deg:.2f}°")
    print(f"Number of complete laps: {n_laps:.3f} laps")
    print(f"            (about {int(n_laps)} complete lap{'s' if n_laps > 1 else ''} plus {(n_laps % 1)*360:.1f}°)")

    return {
        'angular_velocity': omega,
        'period': T,
        'frequency': f,
        'centripetal_acceleration': ac,
        'angle_5s': theta_rad
    }


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("CLASS 11 PHYSICS: KINEMATICS PRACTICE EXERCISES")
    print("="*70)

    # Run all exercises
    results_1 = exercise_1_suvat()
    results_2 = exercise_2_vectors()
    results_3 = exercise_3_projectile()
    results_4 = exercise_4_circular_motion()

    # Summary
    print("\n" + "="*70)
    print("SOLUTIONS SUMMARY")
    print("="*70)
    print(f"\nExercise 1 (SUVAT):")
    print(f"  Car: v = {results_1['car_velocity']} m/s, s = {results_1['car_distance']} m")
    print(f"  Max height of stone: {results_1['max_height']} m")

    print(f"\nExercise 3 (Projectile):")
    print(f"  Time to ground: {results_3['time_to_ground']:.3f} s")
    print(f"  Range: {results_3['range']:.2f} m")
    print(f"  Impact velocity: {results_3['velocity_magnitude']:.2f} m/s")

    print(f"\nExercise 4 (Circular Motion):")
    print(f"  Angular velocity: {results_4['angular_velocity']:.4f} rad/s")
    print(f"  Period: {results_4['period']:.3f} s")
    print(f"  Centripetal acceleration: {results_4['centripetal_acceleration']:.3f} m/s²")

    print("\n" + "="*70 + "\n")

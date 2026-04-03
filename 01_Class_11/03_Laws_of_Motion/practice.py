"""
Practice Exercises: Laws of Motion
Topic 3: Newton's Laws and Applications

Exercises on:
- Newton's laws
- Free body diagrams
- Friction
- Circular motion
- Atwood machines
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# EXERCISE 1: Newton's Second Law
# ============================================================================
"""
Exercise 1: Apply F = ma to solve problems

a) A 1500 kg car accelerates from rest to 25 m/s in 8 seconds.
   Find the net force applied.

b) A 50 kg person stands on a scale in an elevator.
   i) When elevator is at rest: scale reading?
   ii) When elevator accelerates up at 2 m/s²: scale reading?
   iii) When elevator accelerates down at 2 m/s²: scale reading?

c) Two blocks pushed together: m₁=3kg, m₂=2kg, force F=10N
   Find: acceleration and normal force between blocks
"""

def exercise_1_newtons_second_law():
    """Newton's second law problems."""
    print("\n" + "="*70)
    print("EXERCISE 1: Newton's Second Law (F = ma)")
    print("="*70)
    
    # Part a) Car acceleration
    print("\na) Car acceleration")
    print("-" * 70)
    m_car = 1500  # kg
    v_i = 0  # m/s
    v_f = 25  # m/s
    t = 8  # s
    g = 9.81  # m/s²
    
    a_car = (v_f - v_i) / t
    F_net = m_car * a_car
    
    print(f"Mass m = {m_car} kg")
    print(f"Initial velocity: {v_i} m/s, Final velocity: {v_f} m/s")
    print(f"Time: t = {t} s")
    print(f"\nAcceleration: a = Δv/Δt = {v_f}/{t} = {a_car} m/s²")
    print(f"Net force: F = ma = {m_car} × {a_car} = {F_net} N")
    print(f"Or: F = {F_net/1000:.1f} kN")
    
    # Part b) Elevator scale readings
    print("\n\nb) Person in elevator (m = 50 kg)")
    print("-" * 70)
    m_person = 50  # kg
    W = m_person * g  # weight
    
    print(f"Weight: W = mg = {m_person} × {g} = {W:.1f} N")
    print(f"Scale reading is the normal force N (apparent weight)")
    
    print(f"\ni) At rest (a = 0):")
    print(f"   N = mg = {W:.1f} N")
    
    a_up = 2  # m/s²
    N_up = m_person * (g + a_up)
    print(f"\nii) Elevator accelerates up at {a_up} m/s²:")
    print(f"    N - mg = ma")
    print(f"    N = m(g + a) = {m_person}({g} + {a_up}) = {N_up:.1f} N")
    print(f"    Increase: {N_up - W:.1f} N ({(N_up-W)/W*100:.1f}% heavier)")
    
    a_down = 2  # m/s²
    N_down = m_person * (g - a_down)
    print(f"\niii) Elevator accelerates down at {a_down} m/s²:")
    print(f"     mg - N = ma")
    print(f"     N = m(g - a) = {m_person}({g} - {a_down}) = {N_down:.1f} N")
    print(f"     Decrease: {W - N_down:.1f} N ({(W-N_down)/W*100:.1f}% lighter)")
    
    # Part c) Two blocks pushed
    print("\n\nc) Two blocks pushed together")
    print("-" * 70)
    m1 = 3  # kg
    m2 = 2  # kg
    F_applied = 10  # N
    
    # Total mass and acceleration
    m_total = m1 + m2
    a = F_applied / m_total
    
    print(f"Block 1: m₁ = {m1} kg (at back)")
    print(f"Block 2: m₂ = {m2} kg (at front)")
    print(f"Applied force: F = {F_applied} N")
    
    print(f"\nTotal acceleration: a = F/(m₁+m₂) = {F_applied}/{m_total} = {a} m/s²")
    
    # Normal force between blocks
    # Block 2 experiences: N (from block 1) = m₂ × a
    N_between = m2 * a
    
    print(f"\nNormal force between blocks (force on block 2 from block 1):")
    print(f"N = m₂ × a = {m2} × {a} = {N_between} N")
    
    # Verify: Force on block 1 minus normal force
    print(f"\nVerification for block 1:")
    print(f"F - N = m₁ × a")
    print(f"{F_applied} - {N_between} = {m1} × {a}")
    print(f"{F_applied - N_between} = {m1 * a} ✓")
    
    return {
        'car_force': F_net,
        'scale_up': N_up,
        'scale_down': N_down,
        'normal_force': N_between
    }


# ============================================================================
# EXERCISE 2: Friction Problems
# ============================================================================
"""
Exercise 2: Static and kinetic friction

a) Block on horizontal surface:
   μₛ = 0.4, μₖ = 0.3, m = 10 kg
   What force is needed to start moving it?
   What force is needed to keep it moving at constant velocity?

b) Block on incline:
   m = 5 kg, θ = 30°, μₛ = 0.5
   Will block slide down? If so, what is acceleration?
"""

def exercise_2_friction():
    """Friction problems."""
    print("\n" + "="*70)
    print("EXERCISE 2: Friction")
    print("="*70)
    
    # Part a) Horizontal surface
    print("\na) Block on horizontal surface")
    print("-" * 70)
    mu_s = 0.4
    mu_k = 0.3
    m = 10  # kg
    g = 9.81  # m/s²
    
    N = m * g  # Normal force
    f_s_max = mu_s * N
    f_k = mu_k * N
    
    print(f"μₛ = {mu_s}, μₖ = {mu_k}, m = {m} kg")
    print(f"Normal force: N = mg = {m} × {g} = {N:.1f} N")
    
    print(f"\nMaximum static friction: f_s,max = μₛN = {mu_s} × {N:.1f} = {f_s_max:.1f} N")
    print(f"Force needed to START motion: F > {f_s_max:.1f} N")
    
    print(f"\nKinetic friction: f_k = μₖN = {mu_k} × {N:.1f} = {f_k:.1f} N")
    print(f"Force needed to MAINTAIN constant velocity: F = {f_k:.1f} N")
    
    print(f"\nNote: f_k < f_s,max because {f_k:.1f} < {f_s_max:.1f}")
    print(f"This is why it's harder to START something than to keep it moving.")
    
    # Part b) Inclined plane
    print("\n\nb) Block on incline")
    print("-" * 70)
    m = 5  # kg
    theta_deg = 30
    theta_rad = np.radians(theta_deg)
    mu_s = 0.5
    g = 9.81
    
    W = m * g
    W_parallel = W * np.sin(theta_rad)
    W_perp = W * np.cos(theta_rad)
    N = W_perp
    f_s_max = mu_s * N
    
    print(f"m = {m} kg, θ = {theta_deg}°, μₛ = {mu_s}")
    print(f"\nWeight components:")
    print(f"  Parallel to plane: W∥ = mg·sin(θ) = {m}×{g}×sin({theta_deg}°) = {W_parallel:.2f} N")
    print(f"  Perpendicular: W⊥ = mg·cos(θ) = {m}×{g}×cos({theta_deg}°) = {W_perp:.2f} N")
    print(f"\nNormal force: N = W⊥ = {N:.2f} N")
    print(f"Max static friction: f_s,max = μₛN = {mu_s} × {N:.2f} = {f_s_max:.2f} N")
    
    if W_parallel > f_s_max:
        print(f"\nSince W∥ ({W_parallel:.2f} N) > f_s,max ({f_s_max:.2f} N): BLOCK SLIDES")
        
        mu_k = 0.3  # Assume kinetic friction
        f_k = mu_k * N
        F_net = W_parallel - f_k
        a = F_net / m
        
        print(f"\nWith kinetic friction μₖ = {mu_k}:")
        print(f"  f_k = μₖN = {f_k:.2f} N")
        print(f"  Net force down plane: F_net = W∥ - f_k = {F_net:.2f} N")
        print(f"  Acceleration: a = F_net/m = {a:.3f} m/s²")
    else:
        print(f"\nSince W∥ ({W_parallel:.2f} N) < f_s,max ({f_s_max:.2f} N): BLOCK STAYS AT REST")
        print(f"Static friction exactly balances component down plane.")
    
    return {
        'force_to_start': f_s_max,
        'force_to_maintain': f_k
    }


# ============================================================================
# EXERCISE 3: Circular Motion and Centripetal Force
# ============================================================================
"""
Exercise 3: Circular motion in car turning and satellite orbit

a) Car turning: Mass 1000 kg, speed 20 m/s, radius 50 m
   What centripetal force is needed? How much friction?

b) Satellite in circular orbit: Mass 100 kg, radius 6.4×10⁶ m
   For circular orbit, centripetal force = gravitational force
   Find orbital speed and period
"""

def exercise_3_circular_motion():
    """Circular motion problems."""
    print("\n" + "="*70)
    print("EXERCISE 3: Circular Motion and Centripetal Force")
    print("="*70)
    
    # Part a) Car turning
    print("\na) Car turning a corner")
    print("-" * 70)
    m = 1000  # kg
    v = 20  # m/s
    r = 50  # m
    g = 9.81
    
    a_c = v**2 / r
    F_c = m * a_c
    mu_needed = F_c / (m * g)
    
    print(f"Mass: m = {m} kg")
    print(f"Speed: v = {v} m/s")
    print(f"Radius of turn: r = {r} m")
    
    print(f"\nCentripetal acceleration: a_c = v²/r = {v}²/{r} = {a_c} m/s²")
    print(f"Centripetal force needed: F_c = m·a_c = {m} × {a_c} = {F_c} N")
    print(f"\nThis force is provided by friction between tires and road.")
    print(f"Required friction force: {F_c} N")
    print(f"Normal force available: N = mg = {m*g:.0f} N")
    print(f"Minimum friction coefficient: μ = F_c/N = {mu_needed:.3f}")
    
    print(f"\nDry asphalt typically has μ ≈ 0.7-0.9")
    print(f"Wet road has μ ≈ 0.5-0.7")
    print(f"This turn is {'safe' if mu_needed < 0.7 else 'risky'} at this speed.")
    
    # Part b) Satellite orbit
    print("\n\nb) Satellite in circular orbit")
    print("-" * 70)
    m_sat = 100  # kg
    r_orbit = 6.4e6  # m
    G = 6.674e-11  # N·m²/kg²
    M_earth = 5.972e24  # kg
    
    print(f"Mass of satellite: m = {m_sat} kg")
    print(f"Orbital radius: r = {r_orbit:.2e} m (≈ Earth's radius)")
    print(f"Earth's mass: M = {M_earth:.3e} kg")
    
    print(f"\nFor circular orbit:")
    print(f"Centripetal force = Gravitational force")
    print(f"m·v²/r = G·M·m/r²")
    print(f"v² = G·M/r")
    
    v_orbit = np.sqrt(G * M_earth / r_orbit)
    print(f"\nOrbital speed: v = √(GM/r) = {v_orbit:.0f} m/s = {v_orbit/1000:.2f} km/s")
    
    T_orbit = 2 * np.pi * r_orbit / v_orbit
    print(f"Orbital period: T = 2πr/v = {T_orbit:.0f} s = {T_orbit/60:.1f} min = {T_orbit/3600:.2f} hours")
    
    print(f"\nNote: This is a low Earth orbit (just barely above atmosphere)")
    return {
        'centripetal_force': F_c,
        'orbital_speed': v_orbit,
        'orbital_period': T_orbit
    }


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("CLASS 11 PHYSICS: LAWS OF MOTION - PRACTICE EXERCISES")
    print("="*70)
    
    results_1 = exercise_1_newtons_second_law()
    results_2 = exercise_2_friction()
    results_3 = exercise_3_circular_motion()
    
    print("\n" + "="*70)
    print("SUMMARY OF KEY RESULTS")
    print("="*70)
    print(f"\nExercise 1:")
    print(f"  Car force: {results_1['car_force']:.0f} N")
    print(f"  Scale reading (up): {results_1['scale_up']:.1f} N")
    
    print(f"\nExercise 3:")
    print(f"  Satellite orbital speed: {results_3['orbital_speed']:.0f} m/s")
    print(f"  Orbital period: {results_3['orbital_period']/60:.1f} minutes")
    
    print("\n" + "="*70 + "\n")

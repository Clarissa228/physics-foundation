"""
Topic 6: Gravitation - Practice Exercises
Orbital mechanics calculations, escape velocity, Kepler verification

These exercises test understanding of Newton's law of gravitation,
orbital mechanics, and Kepler's laws.
"""

import numpy as np
from scipy.optimize import fsolve

# Physical constants
G = 6.674e-11  # Gravitational constant (N*m^2/kg^2)
M_sun = 1.989e30  # Solar mass (kg)
M_earth = 5.972e24  # Earth mass (kg)
R_earth = 6.371e6  # Earth radius (m)
AU = 1.496e11  # Astronomical unit (m)

# ============================================================================
# Exercise 1: Gravitational Force and Field
# ============================================================================

def exercise_1():
    """
    Two satellites of mass m1=500 kg and m2=300 kg orbit at distance r=1000 m apart.
    Calculate the gravitational force between them.
    """
    m1 = 500  # kg
    m2 = 300  # kg
    r = 1000  # meters

    F = G * m1 * m2 / r**2

    print("Exercise 1: Gravitational Force Between Satellites")
    print(f"  m1 = {m1} kg, m2 = {m2} kg, r = {r} m")
    print(f"  F = G*m1*m2/r² = {F:.6e} N")
    print(f"  (Extremely weak force - demonstrates why gravity is weak)\n")

    return F


# ============================================================================
# Exercise 2: Escape Velocity from Earth
# ============================================================================

def exercise_2():
    """
    Calculate Earth's escape velocity.
    v_escape = sqrt(2*G*M/R)
    """
    v_escape = np.sqrt(2 * G * M_earth / R_earth)

    print("Exercise 2: Escape Velocity from Earth")
    print(f"  v_escape = sqrt(2*G*M/R)")
    print(f"  v_escape = {v_escape:.2f} m/s = {v_escape/1000:.2f} km/s")
    print(f"  Compare: Earth's orbital velocity ≈ 30 km/s\n")

    return v_escape


# ============================================================================
# Exercise 3: Escape Velocity from Different Heights
# ============================================================================

def exercise_3():
    """
    Calculate escape velocity as a function of altitude above Earth.
    Show that it decreases with altitude.
    """
    altitudes = np.array([0, 100e3, 400e3, 36000e3])  # 0 km, 100 km, ISS, Geostationary
    altitude_names = ["Sea level", "100 km altitude", "ISS (400 km)", "Geostationary"]

    print("Exercise 3: Escape Velocity vs Altitude")
    print(f"{'Altitude':<30} {'v_escape (km/s)':<20}")
    print("-" * 50)

    for alt, name in zip(altitudes, altitude_names):
        r = R_earth + alt
        v_esc = np.sqrt(2 * G * M_earth / r)
        print(f"{name:<30} {v_esc/1000:>8.3f}")

    print()
    return altitudes


# ============================================================================
# Exercise 4: Orbital Speed in Circular Orbit
# ============================================================================

def exercise_4():
    """
    For a circular orbit at distance r from Earth's center:
    v_orbital = sqrt(G*M/r)

    Calculate orbital speeds for different satellites.
    """
    orbit_radii = np.array([R_earth + 200e3, R_earth + 400e3, R_earth + 36000e3])
    orbit_names = ["Low Earth Orbit (200 km)", "ISS (400 km)", "Geostationary"]

    print("Exercise 4: Orbital Speeds for Different Earth Orbits")
    print(f"{'Orbit':<30} {'Speed (km/s)':<20} {'Period':<20}")
    print("-" * 70)

    for r, name in zip(orbit_radii, orbit_names):
        v_orb = np.sqrt(G * M_earth / r)
        # Calculate period from v = 2πr/T
        T = 2 * np.pi * r / v_orb
        T_hours = T / 3600
        print(f"{name:<30} {v_orb/1000:>8.3f} km/s  {T_hours:>8.2f} hours")

    print()
    return orbit_radii


# ============================================================================
# Exercise 5: Kepler's Third Law - Mercury to Neptune
# ============================================================================

def exercise_5():
    """
    Use Kepler's 3rd law: T² = (4π²/GM) * a³
    Calculate orbital periods for planets and verify T² ∝ a³
    """
    # Orbital radii (in AU)
    planets = {
        'Mercury': 0.387,
        'Venus': 0.723,
        'Earth': 1.000,
        'Mars': 1.524,
        'Jupiter': 5.203,
        'Saturn': 9.537,
        'Uranus': 19.191,
        'Neptune': 30.069,
    }

    print("Exercise 5: Kepler's Third Law for Solar System Planets")
    print(f"{'Planet':<12} {'a (AU)':<12} {'T (years)':<15} {'T² (y²)':<15} {'a³ (AU³)':<15} {'T²/a³':<12}")
    print("-" * 85)

    ratio_constant = 4 * np.pi**2 / (G * M_sun * (365.25 * 24 * 3600)**2)

    for planet, a_au in planets.items():
        a = a_au * AU  # Convert to meters
        T = 2 * np.pi * np.sqrt(a**3 / (G * M_sun))  # Period in seconds
        T_years = T / (365.25 * 24 * 3600)

        ratio = T_years**2 / a_au**3

        print(f"{planet:<12} {a_au:<12.3f} {T_years:<15.3f} {T_years**2:<15.3f} {a_au**3:<15.3f} {ratio:<12.6f}")

    print(f"\nT²/a³ should be constant ≈ {ratio_constant:.6f}\n")


# ============================================================================
# Exercise 6: Finding Orbital Radius Given Period
# ============================================================================

def exercise_6():
    """
    Given an orbital period T, find the orbital radius a.
    From Kepler's law: a = (GMT²/4π²)^(1/3)

    Problem: A satellite has period T = 12 hours. What is its orbital radius?
    """
    T = 12 * 3600  # 12 hours in seconds

    # a³ = GMT²/(4π²)
    a = (G * M_earth * T**2 / (4 * np.pi**2))**(1/3)

    print("Exercise 6: Finding Orbital Radius from Period")
    print(f"  Given: T = 12 hours = {T/3600} hours")
    print(f"  Find: orbital radius a")
    print(f"  Using: a³ = GMT²/(4π²)")
    print(f"  a = {a/1e6:.2f} × 10⁶ m = {a/1e6:.2f} km")
    print(f"  Height above Earth surface: {(a - R_earth)/1e6:.2f} km")
    print()

    return a


# ============================================================================
# Exercise 7: Vis-viva Equation - Energy of Orbits
# ============================================================================

def exercise_7():
    """
    The vis-viva equation relates orbital speed, position, and semi-major axis:
    v² = GM(2/r - 1/a)

    Compare energies in different Earth orbits.
    """
    orbits = {
        'LEO (400 km)': {'r': R_earth + 400e3, 'name': 'Low Earth Orbit'},
        'MEO (20,000 km)': {'r': R_earth + 20000e3, 'name': 'Medium altitude'},
        'GEO (36,000 km)': {'r': R_earth + 36000e3, 'name': 'Geostationary'},
    }

    m_sat = 1000  # 1000 kg satellite

    print("Exercise 7: Orbital Energy in Different Orbits")
    print(f"Satellite mass: {m_sat} kg\n")
    print(f"{'Orbit':<20} {'r (km)':<15} {'v (km/s)':<15} {'E (MJ)':<15} {'E_kinetic':<15}")
    print("-" * 80)

    for orbit_name, props in orbits.items():
        r = props['r']
        # Circular orbit: v = sqrt(GM/r)
        v = np.sqrt(G * M_earth / r)
        # Total energy for circular orbit: E = -GM*m/(2r)
        E_total = -G * M_earth * m_sat / (2 * r)
        # Kinetic energy: K = GM*m/(2r) (half of magnitude of potential energy)
        K = G * M_earth * m_sat / (2 * r)

        print(f"{orbit_name:<20} {r/1e6:>7.0f}        {v/1000:>8.3f}        {E_total/1e6:>8.1f}        {K/1e6:>8.1f}")

    print()


# ============================================================================
# Exercise 8: Geostationary Orbit
# ============================================================================

def exercise_8():
    """
    A geostationary satellite orbits with period T = 24 hours (same as Earth's rotation).
    Find its orbital radius and height above Earth.
    """
    T_geo = 24 * 3600  # 24 hours in seconds

    # From Kepler's 3rd law: a³ = GMT²/(4π²)
    a_geo = (G * M_earth * T_geo**2 / (4 * np.pi**2))**(1/3)
    h_geo = a_geo - R_earth

    # Orbital speed
    v_geo = 2 * np.pi * a_geo / T_geo

    print("Exercise 8: Geostationary Orbit")
    print(f"  Period: T = 24 hours (same as Earth's rotation)")
    print(f"  Orbital radius: a = {a_geo/1e6:.0f} km")
    print(f"  Height above surface: h = {h_geo/1e6:.0f} km")
    print(f"  Orbital velocity: v = {v_geo:.2f} m/s = {v_geo/1000:.3f} km/s")
    print(f"  Angular velocity: ω = {2*np.pi/T_geo:.3e} rad/s")
    print()

    return a_geo, h_geo


# ============================================================================
# Exercise 9: Determining Planet Mass from Orbital Data
# ============================================================================

def exercise_9():
    """
    A satellite orbits a planet with:
    - Orbital radius: r = 100,000 km
    - Period: T = 12 hours

    Determine the planet's mass.
    """
    r = 100000e3  # meters
    T = 12 * 3600  # seconds

    # From Kepler's law: M = 4π²a³/(GT²)
    M = 4 * np.pi**2 * r**3 / (G * T**2)

    print("Exercise 9: Determining Planet Mass from Orbital Data")
    print(f"  Satellite orbital radius: r = {r/1e6:.0f} km")
    print(f"  Satellite period: T = {T/3600:.0f} hours")
    print(f"  Planet mass: M = 4π²r³/(GT²)")
    print(f"  M = {M:.3e} kg")

    # Compare to known planets
    print(f"\nComparison to solar system:")
    print(f"  Earth mass: {M_earth:.3e} kg, ratio M/M_Earth = {M/M_earth:.2f}")
    print(f"  Jupiter mass: {1.898e27:.3e} kg, ratio M/M_Jupiter = {M/1.898e27:.4f}")
    print()

    return M


# ============================================================================
# Exercise 10: Escape Velocity Problem
# ============================================================================

def exercise_10():
    """
    A rocket is launched from Earth with initial velocity v0.
    What is the minimum velocity to escape Earth's gravity?
    At what height is the escape velocity equal to 5 km/s?
    """
    v_esc_earth = np.sqrt(2 * G * M_earth / R_earth)

    # Find height where escape velocity = 5 km/s
    v_target = 5000  # m/s

    def equation(h):
        return np.sqrt(2 * G * M_earth / (R_earth + h)) - v_target

    h_target = fsolve(equation, 1e7)[0]

    print("Exercise 10: Escape Velocity Problem")
    print(f"  Earth's escape velocity: v_esc = {v_esc_earth/1000:.2f} km/s")
    print(f"  At height where v_esc = 5 km/s:")
    print(f"  h = {h_target/1e6:.0f} km above Earth's surface")
    print()

    return v_esc_earth, h_target


# ============================================================================
# Exercise 11: Orbital Mechanics - Transfer Orbit
# ============================================================================

def exercise_11():
    """
    A spacecraft in Earth orbit (r1 = 400 km) wants to transfer to geostationary orbit (r2).
    Calculate the velocity change (ΔV) required.

    Uses Hohmann transfer ellipse.
    """
    r1 = R_earth + 400e3  # LEO
    r2 = R_earth + 35786e3  # GEO

    # Circular orbit velocities
    v1 = np.sqrt(G * M_earth / r1)
    v2 = np.sqrt(G * M_earth / r2)

    # Hohmann transfer: spacecraft at r1 receives velocity impulse to enter ellipse
    # Then another impulse at r2 to circularize

    # Velocity at periapsis of transfer ellipse
    a_trans = (r1 + r2) / 2
    v_p = np.sqrt(G * M_earth * (2/r1 - 1/a_trans))  # at r1 (periapsis)

    # Velocity at apoapsis of transfer ellipse
    v_a = np.sqrt(G * M_earth * (2/r2 - 1/a_trans))  # at r2 (apoapsis)

    # Velocity changes
    dv1 = v_p - v1  # First impulse (acceleration)
    dv2 = v2 - v_a  # Second impulse (acceleration)
    dv_total = abs(dv1) + abs(dv2)

    # Transfer time
    T_trans = np.pi * np.sqrt(a_trans**3 / (G * M_earth))

    print("Exercise 11: Hohmann Transfer Orbit (LEO to GEO)")
    print(f"  Initial orbit (LEO): r1 = {r1/1e6:.0f} km")
    print(f"  Final orbit (GEO): r2 = {r2/1e6:.0f} km")
    print(f"\\n  Circular orbit velocities:")
    print(f"    v1 (LEO) = {v1/1000:.3f} km/s")
    print(f"    v2 (GEO) = {v2/1000:.3f} km/s")
    print(f"\\n  Transfer ellipse:")
    print(f"    Semi-major axis: a = {a_trans/1e6:.0f} km")
    print(f"    Velocity at r1 (periapsis): v_p = {v_p/1000:.3f} km/s")
    print(f"    Velocity at r2 (apoapsis): v_a = {v_a/1000:.3f} km/s")
    print(f"\\n  Velocity changes required:")
    print(f"    First impulse (at LEO): ΔV1 = {dv1:.2f} m/s")
    print(f"    Second impulse (at GEO): ΔV2 = {dv2:.2f} m/s")
    print(f"    Total ΔV = {dv_total:.2f} m/s = {dv_total/1000:.3f} km/s")
    print(f"\\n  Transfer time: {T_trans/3600:.1f} hours = {T_trans/(3600*24):.2f} days")
    print()


# ============================================================================
# Exercise 12: Binary Star System
# ============================================================================

def exercise_12():
    """
    Two stars of equal mass M orbit around their common center of mass.
    Orbital separation: d = 1 AU
    Calculate the orbital period.
    """
    M1 = 1.989e30  # Solar mass
    M2 = 1.989e30  # Solar mass
    d = 1 * AU  # 1 AU separation

    # Each star orbits at distance r = d/2 from center of mass
    r = d / 2

    # Gravitational force provides centripetal force
    # F = G*M1*M2/d² = M1*ω²*r
    # G*M1*M2/d² = M1*ω²*(d/2)
    # ω² = 2*G*M2/d³ = 2*G*(M1+M2)/d³ (for equal masses)

    omega_sq = 2 * G * (M1 + M2) / d**3
    omega = np.sqrt(omega_sq)
    T = 2 * np.pi / omega

    print("Exercise 12: Binary Star System")
    print(f"  Mass of each star: M = {M1:.3e} kg = 1 M_solar")
    print(f"  Orbital separation: d = {d/AU:.1f} AU")
    print(f"  Orbital radius for each star: r = {r/AU:.3f} AU")
    print(f"\\n  Orbital period: T = {T/(365.25*24*3600):.3f} years")
    print(f"  Angular velocity: ω = {omega:.3e} rad/s")
    print(f"  Orbital velocity: v = ω*r = {omega * r / 1000:.2f} km/s")
    print()


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("TOPIC 6: GRAVITATION - PRACTICE EXERCISES")
    print("=" * 80)
    print()

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
    exercise_11()
    exercise_12()

    print("=" * 80)
    print("All exercises completed!")
    print("=" * 80)

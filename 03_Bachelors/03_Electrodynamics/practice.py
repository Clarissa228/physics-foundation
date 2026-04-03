"""Electrodynamics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, odeint
from scipy.constants import c, epsilon_0, mu_0, e as elementary_charge

def exercise_1_wave_equation():
    print("="*70)
    print("EXERCISE 1: Verify Plane Wave Solution to Maxwell Equations")
    print("="*70)
    
    # Plane wave: E(x,t) = E0 cos(kx - ωt)ŷ
    # Should satisfy: ∂²E/∂t² = c² ∂²E/∂x²
    
    E0 = 1.0
    k = 1.0
    omega = c * k  # dispersion relation
    
    x = np.linspace(0, 10*np.pi/k, 1000)
    t_vals = [0, 1/omega, 2/omega, 3/omega]
    
    fig, axes = plt.subplots(2, 2, figsize=(13, 8))
    
    for idx, t in enumerate(t_vals):
        ax = axes[idx//2, idx%2]
        E = E0 * np.cos(k*x - omega*t)
        ax.plot(x, E, 'b-', linewidth=2)
        ax.fill_between(x, 0, E, alpha=0.3)
        ax.set_ylabel('E(x,t)', fontsize=11)
        ax.set_xlabel('x', fontsize=11)
        ax.set_title(f'Wave at t = {t*omega:.2f}T', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/wave_verification.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nPlane wave: E = E₀cos(kx - ωt)")
    print(f"Dispersion: ω = ck = {omega:.4f}")
    print(f"Wave speed: {omega/k:.2e} m/s (speed of light)")

def exercise_2_poynting_intensity():
    print("\n" + "="*70)
    print("EXERCISE 2: Poynting Vector and Radiation Intensity")
    print("="*70)
    
    E0 = 1.0  # V/m
    Z0 = np.sqrt(mu_0 / epsilon_0)  # impedance of free space ~377 Ω
    
    x = np.linspace(0, 4*np.pi, 1000)
    E = E0 * np.cos(x)
    B = (E0/c) * np.cos(x)
    S = (1/mu_0) * E * B  # Poynting vector
    S_avg = E0**2 / (2 * mu_0 * c)
    
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    
    ax = axes[0]
    ax.plot(x, E, 'b-', linewidth=2, label='E field')
    ax.plot(x, B, 'r-', linewidth=2, label='B field')
    ax.fill_between(x, 0, S/np.max(S)*np.max(E), alpha=0.2, color='green', label='S (scaled)')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.set_xlabel('Position', fontsize=11)
    ax.set_ylabel('Field', fontsize=11)
    ax.set_title('EM Wave Fields and Energy Flow', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    ax = axes[1]
    ax.fill_between(x, 0, S/np.max(S), alpha=0.6, color='green', label='Instantaneous S')
    ax.axhline(y=0.5, color='red', linestyle='--', linewidth=2.5, label='Time-averaged ⟨S⟩')
    ax.set_xlabel('Position', fontsize=11)
    ax.set_ylabel('Power per unit area (normalized)', fontsize=11)
    ax.set_title('Poynting Vector: Energy Intensity', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/poynting_intensity.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nIntensity of EM wave:")
    print(f"Instantaneous: S(x,t) = (1/μ₀)E×B")
    print(f"Time-averaged: ⟨S⟩ = E₀²/(2μ₀c) = {S_avg:.6e} W/m²")
    print(f"Impedance of free space: Z₀ = √(μ₀/ε₀) = {Z0:.1f} Ω")

def exercise_3_radiation_patterns():
    print("\n" + "="*70)
    print("EXERCISE 3: Dipole Radiation Pattern")
    print("="*70)
    
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(theta)**2  # dP/dΩ ∝ sin²θ
    
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    
    # Polar plot
    ax = axes[0]
    ax = plt.subplot(121, projection='polar')
    ax.plot(theta, r, 'b-', linewidth=2.5)
    ax.fill(theta, r, alpha=0.3)
    ax.set_title('Dipole Radiation Pattern\n(dP/dΩ ∝ sin²θ)', fontsize=12, fontweight='bold')
    
    # 3D surface
    from mpl_toolkits.mplot3d import Axes3D
    ax = fig.add_subplot(122, projection='3d')
    phi = np.linspace(0, 2*np.pi, 100)
    THETA, PHI = np.meshgrid(theta[::10], phi)
    R = np.sin(THETA)**2
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)
    ax.plot_surface(X, Y, Z, cmap='hot', alpha=0.8)
    ax.set_title('3D Pattern: Donut Shape', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/tmp/radiation_patterns.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nDipole Radiation:")
    print(f"Pattern: dP/dΩ ∝ sin²θ")
    print(f"Maximum: θ = π/2 (perpendicular to dipole)")
    print(f"Zero: θ = 0, π (along dipole axis)")

def exercise_4_fresnel_equations():
    print("\n" + "="*70)
    print("EXERCISE 4: Fresnel Equations and Brewster's Angle")
    print("="*70)
    
    n1, n2 = 1.0, 1.5  # air to glass
    theta_i = np.linspace(0, np.pi/2, 1000)
    
    # Compute refraction angle using Snell's law
    sin_theta_t = (n1/n2) * np.sin(theta_i)
    valid = sin_theta_t <= 1
    theta_t = np.arcsin(sin_theta_t[valid])
    theta_i_valid = theta_i[valid]
    
    # Fresnel reflection coefficient (s-polarization)
    r_s = (n1*np.cos(theta_i_valid) - n2*np.cos(theta_t)) / \
          (n1*np.cos(theta_i_valid) + n2*np.cos(theta_t))
    R_s = r_s**2
    
    # Fresnel reflection (p-polarization)
    r_p = (n2*np.cos(theta_i_valid) - n1*np.cos(theta_t)) / \
          (n2*np.cos(theta_i_valid) + n1*np.cos(theta_t))
    R_p = r_p**2
    
    # Brewster's angle: tan(θ_B) = n2/n1
    theta_B = np.arctan(n2/n1)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(np.degrees(theta_i_valid), R_s, 'b-', linewidth=2.5, label='s-polarization')
    ax.plot(np.degrees(theta_i_valid), R_p, 'r-', linewidth=2.5, label='p-polarization')
    ax.axvline(x=np.degrees(theta_B), color='green', linestyle='--', linewidth=2, label=f"Brewster's angle = {np.degrees(theta_B):.1f}°")
    ax.set_xlabel('Incident angle (degrees)', fontsize=11)
    ax.set_ylabel('Reflectance R', fontsize=11)
    ax.set_title('Fresnel Equations: Reflection at Air-Glass Interface', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 1)
    
    plt.tight_layout()
    plt.savefig('/tmp/fresnel_equations.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nFresnel Equations (n1={n1}, n2={n2}):")
    print(f"Brewster's angle: θ_B = arctan(n2/n1) = {np.degrees(theta_B):.2f}°")
    print(f"At Brewster's angle, p-polarized light has R = 0 (no reflection!)")
    print(f"Used in: Polarizing filters, anti-glare coatings")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("ELECTRODYNAMICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_wave_equation()
    exercise_2_poynting_intensity()
    exercise_3_radiation_patterns()
    exercise_4_fresnel_equations()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

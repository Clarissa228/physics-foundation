"""Special and General Relativity Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt

def exercise_1_lorentz_transformation():
    """Time dilation and length contraction"""
    print("="*70)
    print("EXERCISE 1: Lorentz Transformations")
    print("="*70)
    
    c_light = 1.0  # Units: c = 1
    v_range = np.linspace(0, 0.99, 100)
    gamma = 1 / np.sqrt(1 - v_range**2/c_light**2)
    
    # Time dilation: Δt' = γ Δt (proper time passes slower)
    # Length contraction: L' = L/γ (moving objects shorten)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Lorentz factor
    ax1.plot(v_range/c_light, gamma, 'b-', linewidth=2.5)
    ax1.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    ax1.fill_between(v_range/c_light, 1, gamma, alpha=0.2)
    ax1.set_xlabel('Velocity (v/c)', fontsize=11)
    ax1.set_ylabel('γ (Lorentz factor)', fontsize=11)
    ax1.set_title('γ = 1/√(1 - v²/c²)', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(1, 10)
    
    # Time dilation and length contraction
    ax2.plot(v_range/c_light, gamma, 'b-', linewidth=2.5, label='Time dilation: γ')
    ax2.plot(v_range/c_light, 1/gamma, 'r-', linewidth=2.5, label='Length contraction: 1/γ')
    ax2.set_xlabel('Velocity (v/c)', fontsize=11)
    ax2.set_ylabel('Factor', fontsize=11)
    ax2.set_title('Time Dilation vs Length Contraction', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/lorentz_transform.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nTime dilation: Moving clocks run slow")
    print(f"At v = 0.9c: γ = {1/np.sqrt(1-(0.9)**2):.2f}")
    print(f"Length contraction: Moving objects shorten along direction of motion")

def exercise_2_energy_momentum():
    """Relativistic energy-momentum relation"""
    print("\n" + "="*70)
    print("EXERCISE 2: Relativistic Energy-Momentum Relation")
    print("="*70)
    
    # E² = (pc)² + (mc²)²
    m = 1.0  # kg (normalized)
    c = 1.0  # m/s (normalized)
    mc2 = m * c**2  # Rest energy
    
    p = np.linspace(0, 3*mc2, 1000)
    E_rel = np.sqrt((p*c)**2 + (mc2)**2)
    E_classical = p**2 / (2*m)  # Classical: E = p²/2m
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Energy vs momentum
    ax1.plot(p/mc2, E_rel/mc2, 'b-', linewidth=2.5, label='Relativistic: E² = (pc)² + (mc²)²')
    ax1.axhline(y=1, color='red', linestyle='--', linewidth=2, label='Rest energy: mc²')
    ax1.plot([0, 3], [1, np.sqrt(1 + 9)], 'ko', markersize=8)
    ax1.set_xlabel('Momentum (p/mc)', fontsize=11)
    ax1.set_ylabel('Energy (E/mc²)', fontsize=11)
    ax1.set_title('Energy-Momentum Relation', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, 4)
    
    # Velocity dependence
    v = np.linspace(0, 0.99, 100)
    gamma_v = 1 / np.sqrt(1 - v**2)
    E_v = gamma_v * mc2
    
    ax2.plot(v, E_v/mc2, 'b-', linewidth=2.5)
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Velocity (v/c)', fontsize=11)
    ax2.set_ylabel('Total Energy (E/mc²)', fontsize=11)
    ax2.set_title('E = γmc²', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/energy_momentum.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nRelativistic Energy-Momentum Relation:")
    print(f"E² = (pc)² + (mc²)²")
    print(f"Rest energy: E₀ = mc² (exists even when p=0!)")
    print(f"As v → c: E → ∞ (impossible to accelerate to light speed)")

def exercise_3_schwarzschild_metric():
    """Black hole: Schwarzschild metric"""
    print("\n" + "="*70)
    print("EXERCISE 3: Schwarzschild Black Hole")
    print("="*70)
    
    M = 1.0  # Solar mass
    G = 1.0  # Normalized units
    c = 1.0
    r_s = 2*G*M/c**2  # Schwarzschild radius
    
    r = np.linspace(r_s + 0.1, 5*r_s, 1000)
    g_tt = 1 - r_s/r  # Metric component (defines time dilation)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r/r_s, g_tt, 'b-', linewidth=2.5)
    ax.axvline(x=1, color='red', linestyle='--', linewidth=2, label=f'Event horizon: r_s')
    ax.fill_between(r/r_s, 0, g_tt, alpha=0.2)
    ax.set_xlabel('Radius (r/r_s)', fontsize=11)
    ax.set_ylabel('g_tt = 1 - r_s/r', fontsize=11)
    ax.set_title('Schwarzschild Metric Near Black Hole', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 5)
    
    plt.tight_layout()
    plt.savefig('/tmp/schwarzschild.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nSchwarzschild Metric (Black Hole):")
    print(f"Schwarzschild radius: r_s = 2GM/c²")
    print(f"For Earth (M ≈ 6×10²⁴ kg): r_s ≈ 9 mm (wouldn't collapse!)")
    print(f"For Sun (M ≈ 2×10³⁰ kg): r_s ≈ 3 km")
    print(f"For stellar black hole (10 M_sun): r_s ≈ 30 km")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("SPECIAL AND GENERAL RELATIVITY: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_lorentz_transformation()
    exercise_2_energy_momentum()
    exercise_3_schwarzschild_metric()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

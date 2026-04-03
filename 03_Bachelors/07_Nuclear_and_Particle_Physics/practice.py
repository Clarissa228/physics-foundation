"""Nuclear and Particle Physics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt

def exercise_1_binding_energy():
    """Binding energy curve (Bethe-Weizsäcker formula)"""
    print("="*70)
    print("EXERCISE 1: Binding Energy Curve")
    print("="*70)
    
    A_range = np.arange(1, 260)
    
    # Bethe-Weizsäcker coefficients (MeV)
    av = 15.677
    as_coeff = 18.56
    ac = 0.717
    aa = 28.1
    
    BE_list = []
    for A in A_range:
        # Estimate Z (Iron-56 is most stable)
        Z = A * 0.4  # Simplified
        N = A - Z
        
        # Bethe-Weizsäcker formula
        BE = (av*A - as_coeff*A**(2/3) - ac*Z**2/A**(1/3) - 
              aa*(A-2*Z)**2/A)
        BE_list.append(BE/A)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(A_range, BE_list, 'b-', linewidth=2.5)
    
    # Mark key nuclei
    iron_idx = np.argmax(BE_list)
    ax.plot(A_range[iron_idx], BE_list[iron_idx], 'ro', markersize=10, label='Fe-56 (most stable)')
    ax.axhline(y=BE_list[iron_idx], color='red', linestyle='--', alpha=0.3)
    
    ax.set_xlabel('Mass number A', fontsize=11)
    ax.set_ylabel('Binding Energy per nucleon (MeV/nucleon)', fontsize=11)
    ax.set_title('Binding Energy Curve: BE/A vs A', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.text(100, BE_list[iron_idx]-0.5, f'BE/A = {BE_list[iron_idx]:.2f} MeV', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('/tmp/binding_energy.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nBinding Energy Curve:")
    print(f"Peak at Fe-56: BE/A ≈ {BE_list[iron_idx]:.2f} MeV")
    print(f"Light nuclei gain energy by FUSION")
    print(f"Heavy nuclei gain energy by FISSION")

def exercise_2_decay_chains():
    """Radioactive decay chain"""
    print("\n" + "="*70)
    print("EXERCISE 2: Radioactive Decay Chain")
    print("="*70)
    
    # U-238 decay chain (simplified)
    half_lives = {
        'U-238': 4.468e9,  # years
        'Th-234': 24.1,
        'Pa-234': 1.17,
        'U-234': 2.445e5,
        'Th-230': 7.54e4,
        'Ra-226': 1600,
        'Rn-222': 3.82,
        'Po-218': 3.1,
        'Pb-214': 26.8,
        'Bi-214': 19.9,
        'Po-214': 164.3e-6,
        'Pb-210': 22.3,
        'Bi-210': 5.01,
        'Po-210': 138.4,
        'Pb-206': np.inf,  # Stable end
    }
    
    # Time simulation
    t = np.linspace(0, 1000, 1000)  # years
    
    fig, axes = plt.subplots(2, 2, figsize=(13, 8))
    
    species = ['U-238', 'Th-234', 'U-234', 'Pb-210']
    ax_idx = 0
    
    for species_name in species:
        ax = axes[ax_idx // 2, ax_idx % 2]
        lambda_val = np.log(2) / half_lives[species_name]
        N = np.exp(-lambda_val * t)
        
        ax.semilogy(t, N, 'b-', linewidth=2.5)
        ax.axhline(y=0.5, color='red', linestyle='--', label=f't_1/2 = {half_lives[species_name]:.2e} yr')
        ax.set_xlabel('Time (years)', fontsize=11)
        ax.set_ylabel('N(t)/N₀', fontsize=11)
        ax.set_title(f'Decay: {species_name}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, which='both')
        
        ax_idx += 1
    
    plt.tight_layout()
    plt.savefig('/tmp/decay_chains.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nRadioactive Decay: N(t) = N₀ exp(-λt) = N₀ exp(-t ln(2)/t_1/2)")

def exercise_3_mass_defect_qvalue():
    """Q-value calculations for nuclear reactions"""
    print("\n" + "="*70)
    print("EXERCISE 3: Nuclear Reaction Q-Values")
    print("="*70)
    
    # Atomic masses (u): 1 u = 931.494 MeV/c²
    masses = {
        'H-1': 1.007825,
        'H-2': 2.014102,
        'H-3': 3.016049,
        'He-4': 4.002603,
        'n': 1.008665,
    }
    
    print(f"\nD-T Fusion: ²H + ³H → ⁴He + n + Q")
    m_d = masses['H-2']
    m_t = masses['H-3']
    m_he4 = masses['He-4']
    m_n = masses['n']
    
    mass_initial = m_d + m_t
    mass_final = m_he4 + m_n
    Q = (mass_initial - mass_final) * 931.494  # Convert to MeV
    
    print(f"Initial mass: {m_d + m_t:.6f} u")
    print(f"Final mass:   {m_he4 + m_n:.6f} u")
    print(f"Mass defect:  {mass_initial - mass_final:.6f} u")
    print(f"Q-value:      {Q:.2f} MeV (energy released!)")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("NUCLEAR AND PARTICLE PHYSICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_binding_energy()
    exercise_2_decay_chains()
    exercise_3_mass_defect_qvalue()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

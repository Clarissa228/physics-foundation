"""Statistical Mechanics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import comb

def exercise_1_boltzmann_distribution():
    """Boltzmann distribution and entropy"""
    print("="*70)
    print("EXERCISE 1: Boltzmann Distribution and Entropy")
    print("="*70)
    
    # Two-level system: E1 < E2
    E1, E2 = 0, 1.0  # Energy units
    T_range = np.linspace(0.1, 5, 100)
    kb = 1.0  # Boltzmann constant
    
    n1_list, n2_list, S_list = [], [], []
    
    for T in T_range:
        Z = np.exp(-E1/(kb*T)) + np.exp(-E2/(kb*T))
        p1 = np.exp(-E1/(kb*T)) / Z
        p2 = np.exp(-E2/(kb*T)) / Z
        
        n1_list.append(p1)
        n2_list.append(p2)
        
        # Entropy
        S = -kb * (p1 * np.log(p1 + 1e-10) + p2 * np.log(p2 + 1e-10))
        S_list.append(S)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    ax1.plot(T_range, n1_list, 'b-', linewidth=2.5, label='P(ground state)')
    ax1.plot(T_range, n2_list, 'r-', linewidth=2.5, label='P(excited state)')
    ax1.set_xlabel('Temperature (T/ε)', fontsize=11)
    ax1.set_ylabel('Probability', fontsize=11)
    ax1.set_title('Boltzmann Distribution', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(T_range, S_list, 'purple', linewidth=2.5)
    ax2.fill_between(T_range, 0, S_list, alpha=0.3)
    ax2.set_xlabel('Temperature (T/ε)', fontsize=11)
    ax2.set_ylabel('Entropy S/k_B', fontsize=11)
    ax2.set_title('Entropy: S = -k_B Σ p_i ln(p_i)', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/boltzmann_entropy.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nTwo-level system (E1=0, E2=1):")
    print(f"Low T: Ground state dominates (S → 0)")
    print(f"High T: States equally likely (S → k_B ln 2)")

def exercise_2_ideal_gas():
    """Ideal gas partition function and thermodynamics"""
    print("\n" + "="*70)
    print("EXERCISE 2: Ideal Gas Partition Function")
    print("="*70)
    
    # For ideal gas: F = -N*k_B*T*ln(Z_1)
    # where Z_1 is single-particle partition function
    
    T_range = np.logspace(-1, 2, 100)
    kb = 1.38e-23  # J/K
    m = 1.66e-27   # kg (1 amu)
    V = 1e-6       # m³
    h = 6.626e-34  # J·s
    
    C_V = []
    for T in T_range:
        lambda_th = h / np.sqrt(2*np.pi*m*kb*T)  # Thermal de Broglie wavelength
        C_V.append(3/2)  # Monatomic ideal gas
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(T_range, C_V, 'b-', linewidth=2.5)
    ax.axhline(y=3/2, color='red', linestyle='--', linewidth=2, label='Classical limit: 3k_B/2')
    ax.set_xlabel('Temperature (K)', fontsize=11)
    ax.set_ylabel('Heat Capacity C_V / N (units of k_B)', fontsize=11)
    ax.set_title('Ideal Gas: Heat Capacity', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('/tmp/ideal_gas.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nIdeal Gas Thermodynamics:")
    print(f"For monatomic ideal gas: C_V = (3/2)Nk_B (constant)")
    print(f"Equipartition: (1/2)k_B T per translational degree of freedom")

def exercise_3_fermi_dirac():
    """Fermi-Dirac distribution for metals"""
    print("\n" + "="*70)
    print("EXERCISE 3: Fermi-Dirac Distribution in Metals")
    print("="*70)
    
    # Fermi energy for copper ~ 7 eV
    EF = 7.0  # eV
    kb = 8.617e-5  # eV/K
    T_values = [0, 300, 1000]
    
    E = np.linspace(-2, 12, 1000)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, T in enumerate(T_values):
        ax = axes[idx]
        f = 1 / (np.exp((E - EF)/(kb*T + 1e-10)) + 1)
        
        ax.plot(E, f, linewidth=2.5)
        ax.fill_between(E, 0, f, alpha=0.3)
        ax.axvline(x=EF, color='red', linestyle='--', linewidth=2, label=f'E_F = {EF} eV')
        ax.set_xlabel('Energy (eV)', fontsize=11)
        ax.set_ylabel('f(E,T)', fontsize=11)
        ax.set_title(f'T = {T} K', fontsize=12, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(-2, 12)
        ax.set_ylim(-0.05, 1.05)
    
    plt.suptitle('Fermi-Dirac Distribution at Different Temperatures', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/tmp/fermi_dirac.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nFermi-Dirac Distribution: f(E,T) = 1/(e^((E-μ)/k_B T) + 1)")
    print(f"T = 0 K: Sharp step at Fermi energy")
    print(f"T > 0: Smeared out over scale ~k_B T")
    print(f"Room T (300K): Significant smearing but mostly T << E_F")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("STATISTICAL MECHANICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_boltzmann_distribution()
    exercise_2_ideal_gas()
    exercise_3_fermi_dirac()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

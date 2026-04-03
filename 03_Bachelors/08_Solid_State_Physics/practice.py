"""Solid State Physics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt

def exercise_1_crystal_bragg():
    """Bragg diffraction"""
    print("="*70)
    print("EXERCISE 1: Bragg's Law and X-Ray Diffraction")
    print("="*70)
    
    # Bragg's law: nλ = 2d sinθ
    lambda_xray = 1.54  # Å (CuKα X-rays)
    d_spacing = 3.16   # Å (Si cubic lattice)
    
    n = np.arange(1, 6)
    theta_bragg = np.arcsin(n * lambda_xray / (2*d_spacing)) * 180 / np.pi
    
    print(f"\nX-ray wavelength: λ = {lambda_xray} Å")
    print(f"Crystal plane spacing: d = {d_spacing} Å")
    print(f"\nBragg diffraction peaks:")
    print(f"n  | 2θ (degrees) | sin(θ)")
    print("-" * 40)
    for i, (ni, theta) in enumerate(zip(n[:3], theta_bragg[:3])):
        print(f"{ni}  | {2*theta:12.2f} | {np.sin(theta*np.pi/180):8.4f}")
    
    # Powder diffraction pattern
    fig, ax = plt.subplots(figsize=(12, 6))
    angles_2theta = 2*theta_bragg
    intensities = np.array([100, 40, 20, 10, 5])
    
    ax.bar(angles_2theta[:3], intensities[:3], width=2, edgecolor='black', color='blue', alpha=0.7)
    ax.set_xlabel('2θ (degrees)', fontsize=11)
    ax.set_ylabel('Intensity', fontsize=11)
    ax.set_title('Powder X-Ray Diffraction Pattern', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    for angle, intensity in zip(angles_2theta[:3], intensities[:3]):
        ax.text(angle, intensity+5, f'{angle:.1f}°', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/tmp/bragg_diffraction.png', dpi=150, bbox_inches='tight')
    plt.show()

def exercise_2_band_gap():
    """Semiconductors: band gap and carrier concentration"""
    print("\n" + "="*70)
    print("EXERCISE 2: Semiconductor Band Gap and Carriers")
    print("="*70)
    
    # Intrinsic carrier concentration: n_i = sqrt(N_c * N_v) * exp(-E_g/2k_B T)
    Eg = 1.12  # eV (Silicon)
    kb = 8.617e-5  # eV/K
    T_range = np.linspace(100, 400, 100)
    
    ni = []
    for T in T_range:
        # Simplified: proportional to exp(-E_g/2k_B T)
        ni_T = np.exp(-Eg / (2*kb*T))
        ni.append(ni_T)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Log scale
    ax1.semilogy(T_range, ni, 'b-', linewidth=2.5)
    ax1.set_xlabel('Temperature (K)', fontsize=11)
    ax1.set_ylabel('Intrinsic carrier conc. n_i (a.u.)', fontsize=11)
    ax1.set_title('Carrier Concentration vs Temperature', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, which='both')
    
    # Band diagram
    ax2.fill_between([0, 1], 0, 1.12, alpha=0.3, color='red', label='Band gap E_g=1.12 eV')
    ax2.text(0.5, 0.56, 'Band gap\n(insulating)', ha='center', fontsize=11, fontweight='bold')
    ax2.set_ylim(-0.5, 2)
    ax2.set_xlim(-0.2, 1.2)
    ax2.set_ylabel('Energy (eV)', fontsize=11)
    ax2.set_title('Semiconductor Band Gap', fontsize=12, fontweight='bold')
    ax2.set_xticks([])
    ax2.legend(fontsize=10, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('/tmp/band_gap.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nSemiconductor (Silicon):")
    print(f"Band gap: E_g = {Eg} eV")
    print(f"At T=300K: n_i ∝ exp(-{Eg/(2*kb*300):.2f})")
    print(f"Doping: Add donors (n-type) or acceptors (p-type)")

def exercise_3_fermi_surface():
    """Fermi surface and density of states"""
    print("\n" + "="*70)
    print("EXERCISE 3: Fermi Surface and Density of States")
    print("="*70)
    
    # Free electron model: E(k) = ℏ²k²/2m
    # Fermi energy: E_F = ℏ²k_F²/2m
    
    m = 1.0  # electron mass (normalized)
    hbar = 1.0
    
    EF = 10.0  # eV
    kF = np.sqrt(2*m*EF) / hbar  # Fermi wave vector
    
    k = np.linspace(0, 1.5*kF, 1000)
    E = (hbar**2 * k**2) / (2*m)
    
    # Density of states: g(E) ∝ sqrt(E)
    E_dos = np.linspace(0, 1.5*EF, 1000)
    dos = np.sqrt(E_dos)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Band structure
    ax1.plot(k/kF, E/EF, 'b-', linewidth=2.5)
    ax1.fill_between(k/kF, 0, E/EF, where=(E<=EF), alpha=0.3, color='blue', label='Filled')
    ax1.fill_between(k/kF, 0, E/EF, where=(E>EF), alpha=0.1, color='red', label='Empty')
    ax1.axhline(y=1, color='red', linestyle='--', linewidth=2, label=f'E_F')
    ax1.axvline(x=1, color='red', linestyle='--', alpha=0.5)
    ax1.set_xlabel('Wave vector k/k_F', fontsize=11)
    ax1.set_ylabel('Energy E/E_F', fontsize=11)
    ax1.set_title('Band Structure: E(k) = ℏ²k²/2m', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Density of states
    ax2.plot(E_dos/EF, dos/np.max(dos), 'r-', linewidth=2.5)
    ax2.fill_between(E_dos/EF, 0, dos/np.max(dos), alpha=0.3, color='red')
    ax2.axvline(x=1, color='red', linestyle='--', linewidth=2, label='Fermi level')
    ax2.set_xlabel('Energy E/E_F', fontsize=11)
    ax2.set_ylabel('Density of states g(E)', fontsize=11)
    ax2.set_title('Density of States: g(E) ∝ √E', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/fermi_surface.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nFree Electron Model:")
    print(f"Fermi energy: E_F = {EF} eV")
    print(f"Fermi wave vector: k_F = {kF:.2f} (normalized)")
    print(f"Density of states: g(E) ∝ √E")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("SOLID STATE PHYSICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_crystal_bragg()
    exercise_2_band_gap()
    exercise_3_fermi_surface()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

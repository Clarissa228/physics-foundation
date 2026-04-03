"""Quantum Mechanics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import hermite, legendre, spherical_jn
from scipy.constants import hbar, e as elementary_charge, m_e

def exercise_1_particle_in_box():
    """Solve particle in infinite square well"""
    L = 1.0  # Box width
    m = 1.0  # Mass (normalized units)
    
    print("="*70)
    print("EXERCISE 1: Particle in Infinite Square Well")
    print("="*70)
    
    # Eigenstates: ψ_n(x) = sqrt(2/L) sin(nπx/L)
    # Eigenvalues: E_n = n²π²ℏ²/(2mL²)
    
    x = np.linspace(0, L, 1000)
    
    fig, axes = plt.subplots(2, 2, figsize=(13, 8))
    
    for n in range(1, 5):
        ax = axes[(n-1)//2, (n-1)%2]
        psi = np.sqrt(2/L) * np.sin(n*np.pi*x/L)
        prob_dens = psi**2
        E_n = n**2 * np.pi**2 / (2*L**2)
        
        ax.plot(x, psi, 'b-', linewidth=2, label='ψ_n(x)')
        ax.plot(x, prob_dens, 'r-', linewidth=2, label='|ψ_n(x)|²')
        ax.fill_between(x, 0, prob_dens, alpha=0.2, color='red')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.set_ylabel('Wavefunction', fontsize=11)
        ax.set_xlabel('Position x', fontsize=11)
        ax.set_title(f'State n={n}, E_{n}={E_n:.3f}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/particle_box.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nParticle in Infinite Square Well (0 < x < {L}):")
    for n in range(1, 6):
        E_n = n**2 * np.pi**2 / (2*L**2)
        print(f"  E_{n} = {E_n:.3f} (in units of π²ℏ²/2mL²)")

def exercise_2_harmonic_oscillator():
    """Quantum harmonic oscillator: eigenstates and energy levels"""
    print("\n" + "="*70)
    print("EXERCISE 2: Quantum Harmonic Oscillator")
    print("="*70)
    
    # ℏω(n + 1/2)
    omega = 1.0
    m_ho = 1.0
    a = np.sqrt(1.0)  # characteristic length = sqrt(ℏ/mω)
    
    x = np.linspace(-5, 5, 1000)
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    
    V = 0.5 * m_ho * omega**2 * x**2  # Potential
    
    for n in range(6):
        ax = axes[n//3, n%3]
        H = hermite(n)
        psi = (1/np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi))) * H(x/a) * np.exp(-x**2/(2*a**2))
        E_n = omega * (n + 0.5)
        
        ax.plot(x, V, 'k--', linewidth=2, alpha=0.5, label='V(x)')
        ax.plot(x, psi + E_n, 'b-', linewidth=2, label='ψ_n(x)')
        ax.fill_between(x, E_n, psi + E_n, alpha=0.3, color='blue')
        ax.axhline(y=E_n, color='gray', linestyle=':', alpha=0.5)
        ax.set_xlim(-5, 5)
        ax.set_ylabel('Energy', fontsize=11)
        ax.set_xlabel('x', fontsize=11)
        ax.set_title(f'n={n}, E_{n}={E_n:.1f}', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/harmonic_oscillator.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nQuantum Harmonic Oscillator (ω = {omega}):")
    for n in range(6):
        E_n = omega * (n + 0.5)
        print(f"  E_{n} = {E_n:.1f}ℏω")

def exercise_3_hydrogen_atom():
    """Hydrogen atom: energy levels and orbitals"""
    print("\n" + "="*70)
    print("EXERCISE 3: Hydrogen Atom")
    print("="*70)
    
    # Energy levels: E_n = -13.6 eV / n²
    # Bohr radius: a0 ≈ 0.53 Å
    
    Ry = 13.6  # Rydberg energy (eV)
    n_levels = 5
    
    # Plot energy diagram
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    # Energy levels
    E_levels = -Ry / np.arange(1, n_levels+1)**2
    ax1.hlines(E_levels, 0, 1, colors='blue', linewidth=2)
    ax1.vlines([0, 1], E_levels[0]-2, 0, colors='blue', linewidth=2)
    
    for i, E in enumerate(E_levels):
        ax1.text(1.1, E, f'n={i+1}: {E:.2f} eV', fontsize=11, va='center')
        # Show transitions
        if i < n_levels - 1:
            ax1.arrow(0.5, E, 0, E_levels[i+1]-E-0.5, head_width=0.03, head_length=0.3, fc='red', ec='red', alpha=0.3)
    
    ax1.set_xlim(-0.2, 3)
    ax1.set_ylabel('Energy (eV)', fontsize=11)
    ax1.set_title('Hydrogen Atom Energy Levels', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_xticks([])
    
    # Hydrogen spectrum (Balmer series)
    wavelengths = []
    for ni in range(3, 8):
        for nf in range(2, ni):
            lam = 1 / (Ry / 1240 * (1/nf**2 - 1/ni**2))  # 1240 eV·nm = hc
            wavelengths.append((lam, ni, nf))
    
    visible_range = [400, 700]  # nm
    colors_balmer = plt.cm.rainbow(np.linspace(0, 1, len([w for w in wavelengths if visible_range[0] < w[0] < visible_range[1]])))
    
    ax2.bar(range(len(wavelengths)), [w[0] for w in wavelengths], color='lightgray', edgecolor='black')
    visible_count = 0
    for i, (lam, ni, nf) in enumerate(wavelengths):
        if visible_range[0] < lam < visible_range[1]:
            ax2.bar(i, lam, color=colors_balmer[visible_count], edgecolor='black')
            visible_count += 1
    
    ax2.axhline(y=visible_range[0], color='purple', linestyle='--', alpha=0.5, label='UV')
    ax2.axhline(y=visible_range[1], color='red', linestyle='--', alpha=0.5, label='Visible')
    ax2.set_ylabel('Wavelength (nm)', fontsize=11)
    ax2.set_xlabel('Transition', fontsize=11)
    ax2.set_title('Hydrogen Emission Spectrum', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('/tmp/hydrogen_atom.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nHydrogen Atom Energy Levels:")
    for n in range(1, 6):
        E = -Ry / n**2
        print(f"  E_{n} = {E:.2f} eV")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("QUANTUM MECHANICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_particle_in_box()
    exercise_2_harmonic_oscillator()
    exercise_3_hydrogen_atom()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

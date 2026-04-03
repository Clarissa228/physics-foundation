# Quantum Mechanics: Foundations and Applications

## Overview
Quantum mechanics describes the microscopic world: atoms, electrons, photons. It's fundamentally probabilistic (unlike classical mechanics) yet mathematically rigorous and experimentally verified to extraordinary precision.

---

## 1. Wave Function and Born Interpretation

The **wave function** ψ(r,t) contains all information about a quantum system.

**Born interpretation**: |ψ(r,t)|² dV = probability of finding particle in volume dV at position r at time t.

**Normalization**: ∫|ψ|² d³r = 1 (particle exists somewhere with certainty)

---

## 2. The Schrödinger Equation

**Time-dependent Schrödinger equation**:
$$i\hbar\frac{\partial \psi}{\partial t} = \hat{H}\psi$$

**Time-independent** (stationary states):
$$\hat{H}\psi = E\psi$$

where Ĥ is the Hamiltonian operator and E is energy eigenvalue.

**Key insight**: This is an eigenvalue problem! Solutions give discrete energy levels.

---

## 3. Operators and Observables

In quantum mechanics, physical quantities (observables) are **Hermitian operators**:
- Position: $\hat{x} = x$
- Momentum: $\hat{p} = -i\hbar\frac{\partial}{\partial x}$
- Energy: $\hat{H}$
- Angular momentum: $\hat{L} = \hat{r} \times \hat{p}$

**Measurement**: When measuring observable Â, possible outcomes are eigenvalues; probability of outcome λᵢ is |⟨ψᵢ|ψ⟩|².

---

## 4. Uncertainty Principle

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

**Physical meaning**: Can't simultaneously know position and momentum precisely. Energy-time uncertainty means short-lived states are energy-uncertain.

---

## 5. Particle in a Box

**Infinite square well**: V = 0 inside, V = ∞ outside.

**Eigenvalues**: $E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}$, n = 1, 2, 3, ...

**Eigenfunctions**: $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$

**Key insight**: Confining particle forces discrete energy levels. Energy gaps increase with quantum number.

---

## 6. Quantum Harmonic Oscillator

**Potential**: V(x) = ½mω²x²

**Eigenvalues**: $E_n = \hbar\omega(n + \frac{1}{2})$, n = 0, 1, 2, ...

**Zero-point energy**: E₀ = ½ℏω ≠ 0 (quantum particles can't be at rest!)

**Eigenfunctions**: $\psi_n(x) \propto H_n(x/a) e^{-x^2/2a^2}$ (Hermite polynomials)

**Ladder operators**: â|n⟩ = √n|n-1⟩ (lowering), â†|n⟩ = √(n+1)|n+1⟩ (raising)

---

## 7. Hydrogen Atom

**3D problem with Coulomb potential** V(r) = -e²/(4πε₀r)

**Eigenvalues**:
$$E_n = -\frac{13.6 \text{ eV}}{n^2}, \quad n = 1, 2, 3, ...$$

**Quantum numbers**:
- n (principal): determines energy, n ≥ 1
- ℓ (orbital angular momentum): ℓ = 0, 1, ..., n-1 (s, p, d, f orbitals)
- m (magnetic): m = -ℓ, ..., 0, ..., ℓ (orientation in space)

**Eigenfunctions**: ψₙₗₘ(r,θ,φ) = Rₙₗ(r)Yₗᵐ(θ,φ)

---

## 8. Spin and Angular Momentum

**Electron spin**: Intrinsic angular momentum with magnitude √(3/4)ℏ

**Spin-1/2**: Only two states |↑⟩ and |↓⟩

**Pauli matrices**: 
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Stern-Gerlach experiment**: Demonstrates quantization of angular momentum

---

## 9. Identical Particles

**Bosons** (integer spin): wavefunction symmetric under particle exchange
**Fermions** (half-integer spin): wavefunction antisymmetric

**Pauli exclusion principle**: No two fermions can occupy same quantum state

---

## 10. Perturbation Theory

For small perturbations V' to a known system V₀:
$$E_n = E_n^{(0)} + E_n^{(1)} + ...$$

where $E_n^{(1)} = \langle n^{(0)} | V' | n^{(0)} \rangle$

**Applications**: Atomic fine structure, Stark effect, etc.

---

## 11. Variational Principle

For upper bound on ground state energy:
$$E_0 \leq \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle}$$

**Method**: Try simple trial wavefunction, minimize energy to find best approximation to ground state.

---

## Key References

**Essential Books**:
1. **Griffiths**, "Introduction to Quantum Mechanics" (3rd ed.) — best intro
2. **Sakurai**, "Modern Quantum Mechanics" (2nd ed.) — graduate standard
3. **Shankar**, "Principles of Quantum Mechanics"

**Landmark Papers**:
- Schrödinger (1926): Wave mechanics
- Heisenberg (1927): Uncertainty principle
- Born (1926): Probability interpretation
- Dirac (1928): Relativistic quantum mechanics

**Applications**:
- Atomic structure and chemistry
- Semiconductor physics (transistors, LEDs)
- Quantum computing
- Laser physics

---

## Study Roadmap

1. Master wave-particle duality
2. Solve Schrödinger equation for simple systems
3. Understand eigenvalue problems
4. Learn physical interpretation of operators
5. Apply to real atoms

**Quantum mechanics is counterintuitive but exquisitely accurate!**

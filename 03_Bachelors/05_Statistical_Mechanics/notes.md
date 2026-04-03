# Statistical Mechanics: Bridging Microscopic and Macroscopic

## Overview
Statistical mechanics connects Newton's laws (deterministic, microscopic) with thermodynamics (probabilistic, macroscopic). A few particles follow Newton; many particles follow statistics and entropy.

---

## 1. Microstates and Macrostates

**Microstate**: Complete specification of all particle positions and momenta
**Macrostate**: Observation at coarse-grained level (P, V, T, etc.)

**Fundamental assumption**: In equilibrium, all microstates consistent with macroscopic constraints are equally probable.

---

## 2. Boltzmann Entropy

$$S = k_B \ln \Omega$$

where Ω = number of microstates compatible with given macrostate.

**Second law**: Entropy increases toward maximum (equilibrium).

**Irreversibility**: Overwhelming majority of microstates are high-entropy states.

---

## 3. Ensemble Theory

**Microcanonical ensemble** (E,V,N fixed): isolated system
$$P(\text{microstate}) = \frac{1}{\Omega}$$ (equal probability)

**Canonical ensemble** (T,V,N fixed): system in thermal bath
$$P(\text{state with energy } E) \propto e^{-E/k_B T} = e^{-\beta E}$$

**Grand canonical** (T,V,μ fixed): system can exchange particles

---

## 4. Partition Function

**Canonical partition function**:
$$Z = \sum_i e^{-\beta E_i}$$

**Thermodynamic quantities from Z**:
$$F = -k_B T \ln Z \quad \text{(Helmholtz free energy)}$$
$$S = -\left(\frac{\partial F}{\partial T}\right)_V = k_B \ln Z + k_B T \frac{\partial \ln Z}{\partial T}$$
$$\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} = k_B T^2 \frac{\partial \ln Z}{\partial T}$$

---

## 5. Statistical Distributions

**Maxwell-Boltzmann** (classical): 
$$f(E) = \sqrt{\frac{2\pi}{(\pi k_B T)^3}} \sqrt{E} \, e^{-E/k_B T}$$

**Bose-Einstein** (photons, atoms):
$$n(E) = \frac{1}{e^{(E-\mu)/k_B T} - 1}$$

**Fermi-Dirac** (electrons, nucleons):
$$f(E) = \frac{1}{e^{(E-\mu)/k_B T} + 1}$$

---

## 6. Ideal Quantum Gases

**Fermi energy** (T=0, metals):
$$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

**Bose-Einstein condensation**: At low T, macroscopic number of particles occupy ground state. Forms superfluids, superconductors.

**Debye model** (phonons in crystals): accounts for vibrational modes.

---

## 7. Phase Transitions

**Critical phenomena**: discontinuities in thermodynamic functions.

**Ising model**: 2D lattice of spins ±1. Shows ferromagnetic-paramagnetic transition at critical temperature.

**Order parameter**: measures symmetry breaking (e.g., magnetization M).

---

## 8. Thermal Physics Applications

**Heat capacity**: $C_V = \left(\frac{\partial E}{\partial T}\right)_V$

**Blackbody radiation**: Perfect absorber/emitter at temperature T
$$u(\nu) = \frac{8\pi h\nu^3}{c^3(e^{h\nu/k_B T} - 1)}$$ (Planck spectrum)

**Stefan-Boltzmann law**: $P = \sigma A T^4$ (total radiated power)

---

## Key References

**Essential Books**:
1. **Pathria & Beale**, "Statistical Mechanics" (3rd ed.) — graduate standard
2. **Reif**, "Fundamentals of Statistical and Thermal Physics"
3. **Schroeder**, "Introduction to Thermal Physics"

**Landmark Papers**:
- Boltzmann (1877): H-theorem, entropy
- Bose (1924), Einstein (1924): Quantum statistics
- Ising (1925): Simple model of ferromagnetism

**Applications**:
- Semiconductor doping and conductivity
- Phase diagrams
- Thermodynamics of reactions
- Cosmology (early universe as hot gas)

---

## Study Roadmap

1. Understand ensemble concept
2. Learn partition function technique
3. Compare MB, BE, FD distributions
4. Study simple models (ideal gas, Einstein solid)
5. Apply to real systems

**The bridge between atoms and thermodynamics!**

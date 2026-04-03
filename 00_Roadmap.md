# 🔭 Physics Foundations — Full Roadmap
### From Class 11 → Class 12 → Bachelor's Degree
#### A Code-First, Visualization-Driven Approach

---

## 🧠 Philosophy of This Course

Physics is not about memorizing formulas. It's about building **intuition** for how the universe behaves — and the best way to build intuition is to *simulate* and *visualize* phenomena yourself.

Every topic in this course follows the same rhythm:
1. **Understand the concept** — read the notes, watch the equations come alive
2. **Code it up** — implement the physics in Python from scratch
3. **Visualize it** — plot, animate, explore parameter space
4. **Push it further** — break it, extend it, ask "what if?"

---

## 🛠️ Tools You'll Use

| Tool | Purpose |
|------|---------|
| `numpy` | Numerical arrays, linear algebra, math |
| `scipy` | ODE solvers, FFT, integration, optimization |
| `matplotlib` | 2D/3D plots and animations |
| `sympy` | Symbolic math — derive equations, print LaTeX |
| `seaborn` | Statistical and distribution plots |
| `plotly` | Interactive 3D plots |
| `pandas` | Data analysis |
| Jupyter Notebooks | Interactive theory + code + plots |

### Install everything at once:
```bash
uv add numpy scipy matplotlib sympy seaborn plotly pandas jupyterlab ipywidgets
```

---

## 📚 The Three Levels

### 🟢 Level 1 — Class 11 Physics
Foundation of classical mechanics and waves. Every concept here appears again at university level.

| # | Topic | Key Ideas |
|---|-------|-----------|
| 1 | [Physical World & Measurement](./01_Class_11/01_Physical_World_Measurement/) | Units, dimensions, error analysis |
| 2 | [Kinematics](./01_Class_11/02_Kinematics/) | Motion, vectors, projectile motion |
| 3 | [Laws of Motion](./01_Class_11/03_Laws_of_Motion/) | Newton's laws, friction, circular motion |
| 4 | [Work, Energy & Power](./01_Class_11/04_Work_Energy_Power/) | Energy conservation, collisions |
| 5 | [System of Particles & Rigid Body](./01_Class_11/05_System_Particles_Rigid_Body/) | Center of mass, torque, rotation |
| 6 | [Gravitation](./01_Class_11/06_Gravitation/) | Kepler's laws, orbits, escape velocity |
| 7 | [Properties of Bulk Matter](./01_Class_11/07_Properties_Bulk_Matter/) | Elasticity, fluids, surface tension |
| 8 | [Thermodynamics](./01_Class_11/08_Thermodynamics/) | Laws of thermodynamics, heat engines |
| 9 | [Kinetic Theory of Gases](./01_Class_11/09_Kinetic_Theory_Gases/) | Molecular speeds, pressure, equipartition |
| 10 | [Oscillations & Waves](./01_Class_11/10_Oscillations_Waves/) | SHM, wave equation, resonance |

---

### 🟡 Level 2 — Class 12 Physics
Electromagnetism, optics, and modern physics. This is where classical physics meets the quantum world.

| # | Topic | Key Ideas |
|---|-------|-----------|
| 1 | [Electrostatics](./02_Class_12/01_Electrostatics/) | Coulomb, Gauss's law, potential, capacitors |
| 2 | [Current Electricity](./02_Class_12/02_Current_Electricity/) | Ohm's law, Kirchhoff's laws, circuits |
| 3 | [Magnetic Effects & Magnetism](./02_Class_12/03_Magnetic_Effects_Magnetism/) | Biot-Savart, Ampere's law |
| 4 | [EM Induction & AC Circuits](./02_Class_12/04_EM_Induction_AC_Circuits/) | Faraday's law, LCR circuits |
| 5 | [Electromagnetic Waves](./02_Class_12/05_Electromagnetic_Waves/) | Maxwell's equations, EM spectrum |
| 6 | [Optics](./02_Class_12/06_Optics/) | Ray optics, interference, diffraction |
| 7 | [Dual Nature of Radiation & Matter](./02_Class_12/07_Dual_Nature_Radiation_Matter/) | Photoelectric effect, de Broglie |
| 8 | [Atoms & Nuclei](./02_Class_12/08_Atoms_and_Nuclei/) | Bohr model, radioactive decay |
| 9 | [Electronic Devices](./02_Class_12/09_Electronic_Devices/) | Semiconductors, diodes, logic gates |

---

### 🔴 Level 3 — Bachelor's Physics
University-level physics. Deep mathematical treatment of classical and modern physics.

| # | Topic | Key Ideas |
|---|-------|-----------|
| 1 | [Mathematical Methods](./03_Bachelors/01_Mathematical_Methods/) | Vector calculus, PDEs, complex analysis, tensors |
| 2 | [Classical Mechanics](./03_Bachelors/02_Classical_Mechanics/) | Lagrangian, Hamiltonian, phase space |
| 3 | [Electrodynamics](./03_Bachelors/03_Electrodynamics/) | Maxwell's equations (full), radiation, waves |
| 4 | [Quantum Mechanics](./03_Bachelors/04_Quantum_Mechanics/) | Schrödinger eq., operators, hydrogen atom |
| 5 | [Statistical Mechanics](./03_Bachelors/05_Statistical_Mechanics/) | Partition functions, ensembles, phase transitions |
| 6 | [Special & General Relativity](./03_Bachelors/06_Special_and_General_Relativity/) | Lorentz transforms, spacetime, GR intro |
| 7 | [Nuclear & Particle Physics](./03_Bachelors/07_Nuclear_and_Particle_Physics/) | Nuclear models, decay, Standard Model |
| 8 | [Solid State Physics](./03_Bachelors/08_Solid_State_Physics/) | Crystal structure, band theory, semiconductors |
| 9 | [Computational Physics](./03_Bachelors/09_Computational_Physics/) | Numerical methods, Monte Carlo, MD simulation |

---

## 📖 Master Reading List

### Class 11 & 12
| Book | Author | Why Read It |
|------|--------|-------------|
| NCERT Physics (Part 1 & 2) | NCERT | The baseline — read everything |
| Concepts of Physics (Vol 1 & 2) | H.C. Verma | Best intuition-building book for Indian students |
| Problems in General Physics | I.E. Irodov | Challenging problems that deepen understanding |
| Fundamentals of Physics | Halliday, Resnick & Walker | Excellent conceptual depth with good problems |
| University Physics | Young & Freedman | Clear derivations, many worked examples |

### Bachelor's Level
| Book | Author | Topic |
|------|--------|-------|
| **The Feynman Lectures on Physics** | Feynman, Leighton, Sands | Everything — read this for joy |
| Mathematical Methods for Physicists | Arfken, Weber & Harris | Mathematical Methods |
| Classical Mechanics | Goldstein, Poole & Safko | Classical Mechanics |
| Classical Mechanics | Landau & Lifshitz | Classical Mechanics (elegant, terse) |
| Introduction to Electrodynamics | David J. Griffiths | Electrodynamics — THE textbook |
| Classical Electrodynamics | J.D. Jackson | Advanced E&M |
| Introduction to Quantum Mechanics | David J. Griffiths | QM — THE textbook |
| Principles of Quantum Mechanics | Dirac | QM (foundational) |
| Modern Quantum Mechanics | J.J. Sakurai | QM (graduate level) |
| Statistical Mechanics | Pathria & Beale | Statistical Mechanics |
| An Introduction to Thermal Physics | Daniel Schroeder | Statistical Mechanics (accessible) |
| Special Relativity | A.P. French | Special Relativity |
| Spacetime and Geometry | Sean Carroll | General Relativity |
| Introduction to Solid State Physics | Charles Kittel | Solid State Physics |
| Nuclear and Particle Physics | W.E. Burcham & M. Jobes | Nuclear/Particle |
| Computational Physics | Mark Newman | Computational Physics |

---

## 🔬 Landmark Papers to Read (Over Time)

| Paper | Authors | Why It Matters |
|-------|---------|---------------|
| On the Electrodynamics of Moving Bodies (1905) | Einstein | Special Relativity |
| On a Heuristic Point of View Concerning the Production and Transformation of Light (1905) | Einstein | Photoelectric Effect |
| Quantisation as a Problem of Proper Values (1926) | Schrödinger | Wave mechanics |
| The Quantum Theory of the Emission and Absorption of Radiation (1927) | Dirac | QED foundations |
| Über die Beziehung zwischen der Wärmeentwicklung... (Boltzmann 1872) | Boltzmann | Statistical Mechanics H-theorem |
| Can Quantum-Mechanical Description of Physical Reality Be Considered Complete? | Einstein, Podolsky, Rosen | EPR Paradox |
| On the Constitution of Atoms and Molecules (1913) | Bohr | Bohr Model |
| The Conservation of Energy (1847) | Helmholtz | Thermodynamics |

---

## 🚀 How to Run Notebooks

```bash
# Install dependencies
uv add numpy scipy matplotlib sympy seaborn plotly pandas jupyterlab ipywidgets

# Launch Jupyter
uv run jupyter lab
```

All notebooks are self-contained — just open and run cell by cell.

---

## 💡 Tips for Learning Physics Through Code

1. **Don't just run the code — change it.** Double the mass, halve the gravity. See what happens.
2. **Plot everything.** If you can't visualize it, you don't understand it yet.
3. **Use SymPy to check your algebra.** Let the computer verify your derivations.
4. **Reproduce figures from textbooks.** If you can code a figure from Griffiths, you understood the section.
5. **Read the Feynman Lectures** alongside everything else. They are free online at [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/).

---

*"Physics is to mathematics what sex is to masturbation." — Richard Feynman*

*Good luck — and have fun simulating the universe. 🚀*

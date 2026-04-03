# Class 11 Physics: Topics 6-10 Complete Educational Content

This directory contains comprehensive educational materials for Class 11 Physics Topics 6-10, built with a **code-first approach** emphasizing Python implementations, numerical simulations, and data visualization.

## Structure

Each topic folder contains three types of files:

1. **notes.md** - Comprehensive theory, equations (LaTeX), key concepts, and references
2. **Jupyter notebooks (.ipynb)** - Interactive Python code with rich visualizations
3. **practice.py** - Coding exercises and calculations

---

## Topic 6: Gravitation

**Path**: `/06_Gravitation/`

### Files
- `notes.md` - Newton's law, Kepler's laws, orbital mechanics, escape velocity
- `01_gravitation_and_orbits.ipynb` - Orbital simulations, Kepler verification, g-variation
- `practice.py` - 12 exercises covering orbital calculations, escape velocity, binary systems

### Key Concepts
- Newton's Law of Universal Gravitation: F = GMm/r²
- Kepler's Three Laws (verified numerically)
- Orbital mechanics and Hohmann transfers
- Geostationary orbits
- Escape velocity: v_escape = √(2GM/R)
- Gravitational slingshot effect

### Learning Outcomes
✓ Understand gravitational field visualization and equipotential surfaces
✓ Simulate planetary orbits using numerical integration
✓ Apply Kepler's laws to find orbital parameters
✓ Design spacecraft trajectories

---

## Topic 7: Properties of Bulk Matter

**Path**: `/07_Properties_Bulk_Matter/`

### Files
- `notes.md` - Elasticity, fluid mechanics, surface tension, viscosity
- `01_elasticity_and_fluids.ipynb` - Stress-strain curves, pressure, Poiseuille flow
- `practice.py` - 12 exercises on Young's modulus, buoyancy, capillarity

### Key Concepts
- Young's Modulus and Hooke's Law: σ = Y·ε
- Pressure in fluids: P(h) = P₀ + ρgh
- Archimedes' Principle and buoyancy
- Poiseuille Flow: Q = πΔPr⁴/(8ηL)
- Stokes' Law: terminal velocity in viscous fluid
- Surface tension and capillary rise: h = 2γcosθ/(ρgr)

### Learning Outcomes
✓ Analyze stress-strain relationships with realistic material data
✓ Calculate pressure at depth and buoyant forces
✓ Design fluid flow systems
✓ Understand capillarity in biological and industrial systems

---

## Topic 8: Thermodynamics

**Path**: `/08_Thermodynamics/`

### Files
- `notes.md` - Laws, processes, cycles, efficiency, entropy
- `01_thermodynamics.ipynb` - P-V diagrams, Carnot cycle, Otto cycle visualization
- `practice.py` - 10 exercises on thermodynamic processes, efficiency, COP

### Key Concepts
- First Law: ΔU = Q - W
- Thermodynamic Processes: isothermal, adiabatic, isobaric, isochoric
- Carnot Efficiency: η = 1 - T_C/T_H
- Carnot Cycle and real engines (Otto, Diesel)
- Entropy and Second Law: ΔS ≥ 0
- Heat pumps and refrigerators

### Learning Outcomes
✓ Construct P-V diagrams for all thermodynamic processes
✓ Calculate work from area under curves
✓ Understand efficiency limits from Carnot principle
✓ Design thermodynamic systems with constraints

---

## Topic 9: Kinetic Theory of Gases

**Path**: `/09_Kinetic_Theory_Gases/`

### Files
- `notes.md` - Maxwell-Boltzmann distribution, mean free path, van der Waals equation
- `01_kinetic_theory.ipynb` - Speed distributions, equipartition, molecular collisions
- `practice.py` - 7 exercises on molecular speeds, pressure, collisions

### Key Concepts
- Maxwell-Boltzmann Speed Distribution: f(v) = 4πn₀(m/2πk_BT)^(3/2)·v²·exp(-mv²/2k_BT)
- Characteristic speeds: v_mp, v_avg, v_rms
- Equipartition Theorem: <KE> = (3/2)k_BT per translational DOF
- Mean Free Path: λ = 1/(√2·π·d²·n)
- van der Waals Equation for real gases
- Collision frequency and molecular transport

### Learning Outcomes
✓ Visualize and interpret molecular speed distributions at different temperatures
✓ Apply equipartition theorem to calculate heat capacity
✓ Understand when ideal gas law breaks down
✓ Calculate mean free path and collision rates

---

## Topic 10: Oscillations and Waves

**Path**: `/10_Oscillations_Waves/`

### Files
- `notes.md` - SHM, damping, resonance, wave equation, interference, Doppler
- `01_simple_harmonic_motion.ipynb` - SHM kinematics, energy, damping, resonance
- `02_waves.ipynb` - Traveling waves, standing waves, beats, Fourier synthesis
- `practice.py` - 8 exercises on SHM, waves, Doppler, beats

### Key Concepts
- SHM: x = A·cos(ωt + φ), ω = √(k/m)
- Energy in SHM: E = (1/2)kA² = constant
- Damping ratio: ζ = b/(2√km)
- Resonance: Q = 1/(2ζ), maximum at ω₀
- Wave equation: ∂²y/∂t² = v²·∂²y/∂x²
- Standing Waves: L = n·λ/2
- Beats: f_beat = |f₁ - f₂|
- Doppler Effect: f' = f·(v ± v_o)/(v ∓ v_s)
- Fourier Analysis: Any signal = sum of harmonics

### Learning Outcomes
✓ Simulate damped and driven oscillations
✓ Analyze resonance in real systems
✓ Model wave propagation and interference
✓ Apply Fourier analysis to complex waveforms
✓ Calculate Doppler shifts for moving sources

---

## Usage

### For Students
1. Read `notes.md` for theoretical foundation
2. Run Jupyter notebooks to see code-based visualizations
3. Solve exercises in `practice.py` with guidance from notebooks

### For Teachers
1. Use notebooks as interactive teaching aids
2. Modify parameters in code to show effects in real-time
3. Assign practice.py exercises as homework
4. Reference notes.md for comprehensive theory review

### Running the Code

```bash
# Install dependencies
pip install numpy scipy matplotlib sympy jupyter

# Navigate to topic folder
cd /sessions/laughing-wonderful-dijkstra/mnt/physics-foundation/01_Class_11/06_Gravitation/

# Run Jupyter
jupyter notebook 01_gravitation_and_orbits.ipynb

# Run practice exercises
python practice.py
```

---

## Physical Constants Used

| Constant | Symbol | Value | Units |
|----------|--------|-------|-------|
| Gravitational constant | G | 6.674 × 10⁻¹¹ | N·m²/kg² |
| Boltzmann constant | k_B | 1.381 × 10⁻²³ | J/K |
| Gas constant | R | 8.314 | J/(mol·K) |
| Speed of light | c | 3.0 × 10⁸ | m/s |
| Speed of sound (air) | v_s | 343 | m/s |
| Earth mass | M_E | 5.972 × 10²⁴ | kg |
| Earth radius | R_E | 6.371 × 10⁶ | m |
| Solar mass | M_☉ | 1.989 × 10³⁰ | kg |

---

## Key Features

✓ **Code-First Approach**: Every concept has Python implementation
✓ **Rich Visualizations**: Matplotlib plots for all major concepts
✓ **Numerical Simulations**: scipy.integrate for solving differential equations
✓ **Interactive Notebooks**: Jupyter for exploration and learning
✓ **Practical Exercises**: Real-world problem sets
✓ **Rigorous Mathematics**: LaTeX equations throughout
✓ **Academic References**: Book chapters and research papers cited
✓ **Modern Applications**: Links to contemporary physics (LIGO, exoplanets, etc.)

---

## Learning Path Recommendation

**Week 1-2: Topic 6 (Gravitation)**
- Classical mechanics at cosmic scales
- Foundation for understanding orbits

**Week 3-4: Topic 7 (Properties of Matter)**
- Bridge between microscopic and macroscopic
- Material science and fluid mechanics

**Week 5-6: Topic 8 (Thermodynamics)**
- Energy and entropy
- Limits of physical systems

**Week 7-8: Topic 9 (Kinetic Theory)**
- Connection between microscopic particles and macroscopic properties
- Statistical mechanics introduction

**Week 9-10: Topic 10 (Oscillations and Waves)**
- Fundamental patterns throughout physics
- Foundation for modern physics (quantum mechanics)

---

## Standards Alignment

- CBSE Class 11 Physics Syllabus
- NCERT Textbooks (all chapters referenced)
- H.C. Verma (supplementary problems)
- International Physics Olympiad preparation

---

## Technical Stack

- **Python 3.12+**
- **NumPy**: Numerical computations
- **SciPy**: Advanced scientific algorithms
- **Matplotlib**: Publication-quality visualizations
- **SymPy**: Symbolic mathematics
- **Jupyter Notebook**: Interactive computing

---

## File Statistics

- **Total Topics**: 10
- **Total Files**: 30
- **Notebooks**: 12 (.ipynb)
- **Theory Notes**: 10 (notes.md)
- **Practice Exercises**: 80+ (practice.py)
- **Total Code Lines**: ~3000+
- **Total Theory**: ~100 pages (converted)

---

## Author Notes

This curriculum represents an integration of:
- Classical textbook theory
- Modern computational physics
- Interactive visualization
- Problem-based learning
- Code literacy in science

The emphasis on Python ensures students develop computational thinking alongside physics understanding—essential for modern STEM careers.

---

**Last Updated**: April 2026
**Version**: 1.0 Complete
**Status**: Production Ready


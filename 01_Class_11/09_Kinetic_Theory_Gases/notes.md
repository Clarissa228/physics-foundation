# Topic 9: Kinetic Theory of Gases

## Overview
Kinetic theory explains macroscopic gas properties (pressure, temperature, viscosity) from the microscopic behavior of molecules.

## Basic Postulates of Kinetic Theory

1. **Gas molecules are in random motion** - ceaseless, random collisions
2. **Volume of molecules is negligible** compared to container volume
3. **No intermolecular forces** (except during collisions)
4. **Collisions are elastic** - kinetic energy is conserved
5. **Average kinetic energy is proportional to absolute temperature**

## Pressure from Molecular Collisions

Consider molecules in a box hitting a wall.

**Momentum transfer per collision**:
- Molecule hits wall with velocity $v_x$
- Bounces back with velocity $-v_x$
- Momentum change: $\Delta p = 2m v_x$

**Force on wall**:
- Number of molecules hitting area $A$ in time $dt$: $\frac{1}{6}n_{vol} v \, A \, dt$
- (Factor 1/6: only 1/3 move toward wall, on average; then divide by 2 for directions)

**Pressure**:
$$P = \frac{F}{A} = \frac{1}{3}n_{vol} m v^2$$

where $n_{vol}$ is number density (molecules per unit volume) and $v$ is rms speed.

**Alternative form**:
$$PV = \frac{1}{3}N m v^2$$

## Temperature and Kinetic Energy

The average kinetic energy of a gas molecule is proportional to absolute temperature:

$$\langle KE \rangle = \frac{3}{2}k_B T$$

where $k_B = 1.381 \times 10^{-23}$ J/K is Boltzmann's constant.

**From kinetic pressure equation**: $PV = \frac{1}{3}Nm\langle v^2 \rangle$

Combining with ideal gas law $PV = Nk_B T$:

$$\frac{1}{3}m\langle v^2 \rangle = \frac{3}{2}k_B T$$

$$\langle v^2 \rangle = \frac{3k_B T}{m}$$

## Molecular Speeds

### Root-Mean-Square (RMS) Speed
$$v_{rms} = \sqrt{\frac{3k_B T}{m}} = \sqrt{\frac{3RT}{M}}$$

where $M$ is molar mass (kg/mol).

### Mean Speed
$$v_{avg} = \sqrt{\frac{8k_B T}{\pi m}} = \sqrt{\frac{8RT}{\pi M}}$$

### Most Probable Speed
$$v_{mp} = \sqrt{\frac{2k_B T}{m}} = \sqrt{\frac{2RT}{M}}$$

**Order**: $v_{mp} < v_{avg} < v_{rms}$ (by factors ~0.92 and ~1.09)

## Maxwell-Boltzmann Speed Distribution

The probability distribution of molecular speeds:

$$f(v) = 4\pi n_0 \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \exp\left(-\frac{mv^2}{2k_B T}\right)$$

where $n_0$ is number density.

**Properties**:
- Peaks at $v_{mp}$
- Right-skewed (long tail at high speeds)
- Integral over all speeds = $n_0$
- Broader at higher temperatures

## Equipartition Theorem

In thermal equilibrium, energy is distributed equally among degrees of freedom:

$$\langle E_i \rangle = \frac{1}{2}k_B T \text{ per degree of freedom}$$

**Internal energy**:
$$U = f \cdot \frac{1}{2}N k_B T = \frac{f}{2}nRT$$

where $f$ is the number of degrees of freedom.

### Degrees of Freedom

- **Monatomic** (He, Ne): $f = 3$ (translational only)
- **Diatomic** (O₂, N₂): $f = 5$ (3 translational + 2 rotational)
- **Polyatomic**: $f = 6$ or more (including vibrational at high T)

### Molar Heat Capacity

$$C_V = \frac{f}{2}R$$

- Monatomic: $C_V = \frac{3}{2}R = 12.5$ J/(mol·K)
- Diatomic: $C_V = \frac{5}{2}R = 20.8$ J/(mol·K)
- Polyatomic: $C_V = 3R = 24.9$ J/(mol·K)

## Mean Free Path

The average distance a molecule travels before colliding:

$$\lambda = \frac{1}{\sqrt{2}\pi d^2 n}$$

where:
- $d$ is molecular diameter
- $n$ is number density

**Pressure dependence**: $\lambda \propto 1/P$

**Temperature dependence**: For real gases, $\lambda$ increases slightly with $T$ (due to density decrease)

## Van der Waals Equation

Real gas equation accounting for:
- Finite molecular size
- Intermolecular attractive forces

$$\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT$$

or for $n$ moles:

$$\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT$$

where:
- $a$ accounts for attractive forces
- $b$ is the excluded volume (finite size)
- $V_m$ is molar volume

**Limits**:
- At low density: van der Waals → ideal gas
- At high pressure: volume term dominates
- Near critical point: significant deviations

## Viscosity

Viscosity is transport of momentum between fluid layers.

**Newton's law of viscosity**:
$$F = \eta A \frac{dv}{dy}$$

**From kinetic theory**:
$$\eta \approx \frac{m n v_{avg}}{3\sigma}$$

where $\sigma$ is molecular cross-section.

**Temperature dependence**: $\eta \propto T^{1/2}$ (surprisingly, mostly independent of pressure)

## Thermal Conductivity

Heat transport by moving molecules carrying energy.

$$\kappa = \frac{f k_B}{2\sigma}\sqrt{\frac{mk_B T}{\pi}}$$

**Also**: $\kappa \propto T^{1/2}$ and nearly independent of pressure.

## Key Constants and Typical Values

| Quantity | Symbol | Value | Units |
|----------|--------|-------|-------|
| Boltzmann constant | $k_B$ | 1.381 × 10⁻²³ | J/K |
| Avogadro's number | $N_A$ | 6.022 × 10²³ | mol⁻¹ |
| Gas constant | $R$ | 8.314 | J/(mol·K) |
| Relation | - | $R = k_B N_A$ | - |

## Physical Constants for Common Gases (STP)

| Gas | Molar Mass (g/mol) | $v_{rms}$ (m/s) | $\lambda$ (nm) |
|-----|-------------------|-----------------|---------------|
| H₂ | 2 | 1920 | 190 |
| He | 4 | 1360 | 200 |
| N₂ | 28 | 515 | 66 |
| O₂ | 32 | 478 | 63 |
| CO₂ | 44 | 408 | 40 |

(at 0°C and 1 atm)

## Problem-Solving Strategies

1. **Pressure calculations**: Use $P = \frac{1}{3}nm v^2$
2. **Temperature relations**: Use $\langle KE \rangle = \frac{3}{2}k_B T$
3. **Speed calculations**: Choose correct formula ($v_{rms}$, $v_{avg}$, or $v_{mp}$)
4. **Distributions**: Integrate Maxwell-Boltzmann for specific velocity ranges
5. **Mean free path**: Use $\lambda = 1/(\sqrt{2}\pi d^2 n)$

## Modern Applications

1. **Plasma Physics**: Kinetic theory of ionized gases
2. **Semiconductor Processing**: Gas behavior in fabrication
3. **Vacuum Technology**: Mean free path determines regimes
4. **Atmospheric Physics**: Understanding air composition and behavior
5. **Chemical Kinetics**: Collision theory for reaction rates
6. **Molecular Dynamics**: Simulation of gas behavior

## Key References

### Textbooks
- **NCERT Class 11 Physics, Chapter 13**: Kinetic Theory of Gases
- **H.C. Verma, Chapters 24-25**: Kinetic Theory and Gases
- **Reif, F.**: "Fundamentals of Statistical and Thermal Physics" (Chapters 1-3)
- **McQuarrie, D.**: "Statistical Mechanics" (rigorous treatment)

### Historical Papers
- **Maxwell, J.C. (1860)**: "Illustrations of the Dynamical Theory of Gases" — Velocity distribution
- **Boltzmann, L. (1880)**: Foundation of kinetic theory and entropy

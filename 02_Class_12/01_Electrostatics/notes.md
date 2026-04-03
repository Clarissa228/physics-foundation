# Electrostatics

## Overview
Electrostatics deals with electric charges at rest and the forces, fields, and potential they create. This is the foundation for understanding electromagnetism.

## Key Concepts

### 1. Coulomb's Law
The force between two point charges is:
$$F = k\frac{q_1 q_2}{r^2}$$

where:
- $k = 8.99 \times 10^9 \, \text{N⋅m}^2/\text{C}^2$ (Coulomb's constant)
- Alternatively: $k = \frac{1}{4\pi\varepsilon_0}$, with $\varepsilon_0 = 8.854 \times 10^{-12} \, \text{F/m}$
- Force is repulsive for like charges, attractive for opposite charges

**Superposition Principle**: The net force on a charge is the vector sum of forces from all other charges.

### 2. Electric Field
The electric field is the force per unit charge:
$$\vec{E} = \frac{\vec{F}}{q} = k\frac{Q}{r^2}\hat{r}$$

- Defined in the limit of an infinitesimal test charge
- Field lines point away from positive charges, toward negative charges
- Electric field lines are continuous (no sources or sinks except at charges)
- Field lines never cross (field has unique direction at each point)

### 3. Electric Field Lines and Equipotential Surfaces
- **Field lines**: Tangent at any point gives direction of $\vec{E}$; density indicates field strength
- **Equipotential surfaces**: Surfaces of constant potential; always perpendicular to field lines
- No work is done moving a charge along an equipotential surface

### 4. Gauss's Law
$$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$

**Key applications**:
- **Uniformly charged sphere** (radius $R$, total charge $Q$):
  - Inside ($r < R$): $E = \frac{kQr}{R^3}$
  - Outside ($r > R$): $E = \frac{kQ}{r^2}$

- **Infinite uniformly charged plane** (surface charge density $\sigma$):
  - $E = \frac{\sigma}{2\varepsilon_0}$ (independent of distance!)

- **Infinite uniformly charged cylinder** (linear charge density $\lambda$, radius $R$):
  - Inside ($r < R$): $E = 0$
  - Outside ($r > R$): $E = \frac{\lambda}{2\pi\varepsilon_0 r}$

### 5. Electric Potential
The electric potential is the potential energy per unit charge:
$$V = \frac{U}{q} = k\frac{Q}{r}$$

**Key relationships**:
$$\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k}\right)$$

- In 1D: $E = -\frac{dV}{dr}$
- Potential is a scalar (easier to compute than field)
- Superposition applies: total potential = sum of individual potentials

### 6. Equipotential Surfaces
- Surfaces of constant potential
- Perpendicular to electric field lines
- No electric field exists parallel to equipotential surface
- For point charge: equipotentials are concentric spheres
- Work done in moving charge on equipotential: $W = 0$

### 7. Capacitance
A capacitor stores charge and electric field energy.

**Capacitance definition**:
$$C = \frac{Q}{V}$$

where $Q$ is magnitude of charge on each plate, $V$ is potential difference.

**Parallel Plate Capacitor**:
$$C = \varepsilon_0 \frac{A}{d}$$

where $A$ is plate area, $d$ is separation.

**Capacitors in series** (charge same, voltage adds):
$$\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$$

**Capacitors in parallel** (voltage same, charge adds):
$$C_{\text{eq}} = C_1 + C_2 + \cdots$$

### 8. Energy Stored in Capacitor
$$U = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{1}{2}\frac{Q^2}{C}$$

**Energy density** in electric field:
$$u = \frac{1}{2}\varepsilon_0 E^2 \quad \text{(J/m}^3\text{)}$$

### 9. Dielectrics
When a dielectric material is placed in electric field:
- Field is reduced: $E = \frac{E_0}{\kappa}$, where $\kappa$ is dielectric constant
- Capacitance increases: $C = \kappa C_0$
- Energy stored decreases: $U = \frac{U_0}{\kappa}$
- Due to **polarization**: induced dipoles in material oppose original field

**Common dielectric constants**:
- Vacuum: $\kappa = 1$
- Air: $\kappa \approx 1.00054$
- Paper: $\kappa \approx 3.7$
- Glass: $\kappa \approx 6$
- Water: $\kappa \approx 80$

## Historical Context

### Coulomb's Torsion Balance (1785)
Charles-Augustin de Coulomb used a delicate torsion balance to measure forces between charged spheres, establishing the inverse-square law and quantifying electrical forces for the first time.

### Faraday's Work on Dielectrics (1837-1856)
Michael Faraday discovered dielectric effects and introduced the concept of electric field lines through experimental observations of charge distribution.

### Gauss's Law
Carl Friedrich Gauss formulated the integral form of Gauss's law in 1835, showing that the total electric flux through a closed surface equals enclosed charge divided by permittivity.

## Reference Books

1. **NCERT Physics Class 12** - Chapters 1-2: Excellent for Indian curriculum alignment
2. **H.C. Verma - Concepts of Physics Vol. 2** - Chapters 29-30: Deep conceptual understanding
3. **Griffiths - Introduction to Electrodynamics** (3rd/4th ed.) - Chapters 1-3: Rigorous mathematical treatment
4. **Halliday, Resnick, Walker - Fundamentals of Physics** - Chapters 21-25: Clear explanations with many examples

## Research Papers

- Coulomb, C.A. (1785). "Construction and use of an electric balance". *Hist. Acad. Roy. Sci.*
- Faraday, M. (1837). "On the Induction of Electric Currents". *Phil. Trans. Roy. Soc.*
- Jackson, J.D. (1999). *Classical Electrodynamics* (3rd ed.) - Chapters 1-4: Modern formulation

## Numerical Constants

- Elementary charge: $e = 1.602 \times 10^{-19}$ C
- Coulomb constant: $k = 8.99 \times 10^9$ N⋅m²/C²
- Permittivity of free space: $\varepsilon_0 = 8.854 \times 10^{-12}$ F/m
- Permeability of free space: $\mu_0 = 4\pi \times 10^{-7}$ H/m

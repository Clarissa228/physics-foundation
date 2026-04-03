# Magnetic Effects and Magnetism

## Overview
Magnetism describes the interactions between moving charges, magnetic materials, and magnetic fields.

## Key Concepts

### 1. Biot-Savart Law
The magnetic field from a current element:
$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \vec{r}}{r^3}$$

where:
- $\mu_0 = 4\pi \times 10^{-7}$ H/m (permeability of free space)
- $I$ is current
- $d\vec{l}$ is current element
- $\vec{r}$ is position vector from element to field point

### 2. Ampere's Law
For symmetric current distributions:
$$\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}}$$

**Applications**:
- **Long straight wire**: $B = \frac{\mu_0 I}{2\pi r}$
- **Circular loop (on axis)**: $B = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$
- **Solenoid (inside)**: $B = \mu_0 n I$ (where $n$ = turns per unit length)
- **Toroid**: $B = \frac{\mu_0 N I}{2\pi r}$ (at radius $r$)

### 3. Force on Current-Carrying Conductor
$$\vec{F} = I\vec{L} \times \vec{B}$$

Magnitude: $F = BIL\sin\theta$ where $\theta$ is angle between conductor and field.

### 4. Torque on Current Loop
$$\vec{\tau} = \vec{\mu} \times \vec{B}$$

where magnetic dipole moment: $\mu = NIA$ (N = turns, I = current, A = area)

Magnitude: $\tau = NIAB\sin\theta$

### 5. Lorentz Force on Moving Charge
$$\vec{F} = q\vec{v} \times \vec{B}$$

Magnitude: $F = qvB\sin\theta$

### 6. Cyclotron Motion
A charged particle in perpendicular B field moves in circle:
$$r = \frac{mv}{qB}$$

**Cyclotron frequency**: $\nu = \frac{qB}{2\pi m}$

**Period**: $T = \frac{2\pi m}{qB}$ (independent of velocity!)

### 7. Magnetic Field in Matter

**Diamagnetic** (χ < 0): Opposes applied field (e.g., Cu, Au)

**Paramagnetic** (χ > 0): Aligns with field (e.g., Al, O₂)

**Ferromagnetic** (χ >> 1): Strongly aligns with field (Fe, Ni, Co)

Magnetization: $\vec{M} = \chi \vec{H}$ where $\chi$ is magnetic susceptibility

### 8. Magnetic Hysteresis
Ferromagnetic materials show memory effect:
- Remanent magnetization (B at H=0)
- Coercive field (H to reduce B to 0)
- Saturation (maximum M)

### 9. Electromagnetic Induction (Introduction)
Moving magnetic field induces electric field (Faraday's law, detailed in Topic 4):
$$\varepsilon = -\frac{d\Phi_B}{dt}$$

where $\Phi_B$ is magnetic flux.

## Historical Context

- **Oersted (1820)**: First observed magnetic field from electric current
- **Ampere (1820s)**: Formulated Ampere's law and current element theory
- **Biot & Savart (1820)**: Developed Biot-Savart law
- **Faraday (1831)**: Discovered electromagnetic induction
- **Maxwell (1860s)**: Unified electricity and magnetism in Maxwell's equations

## Reference Books

1. **NCERT Physics Class 12** - Chapters 4-5: Magnetic Effects and Magnetism
2. **Griffiths - Introduction to Electrodynamics** - Chapter 5: Magnetostatics
3. **H.C. Verma - Concepts of Physics Vol. 2** - Chapters 33-34
4. **Halliday, Resnick, Walker** - Chapters 29-32

## Physical Constants

- Permeability of free space: $\mu_0 = 4\pi \times 10^{-7}$ H/m = $1.257 \times 10^{-6}$ H/m
- Elementary charge: $e = 1.602 \times 10^{-19}$ C
- Electron mass: $m_e = 9.109 \times 10^{-31}$ kg

## Key Equations Summary

| Concept | Equation |
|---------|----------|
| Biot-Savart | dB = (μ₀/4π) I dl × r̂ / r² |
| Ampere's law | ∮B·dl = μ₀I_enc |
| Long wire | B = μ₀I/(2πr) |
| Force on wire | F = BIL sinθ |
| Torque on loop | τ = NIAB sinθ |
| Lorentz force | F = qvB sinθ |
| Cyclotron radius | r = mv/(qB) |
| Solenoid field | B = μ₀nI |

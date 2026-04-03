# Electrodynamics: Maxwell's Equations and Electromagnetic Waves

## Overview
Electrodynamics unifies electricity, magnetism, and light into a single elegant framework: **Maxwell's Equations**. At the Bachelor's level, we master the theory, solve for wave propagation, radiation, and electromagnetic energy transport.

---

## 1. Maxwell's Equations in Differential Form

The four pillars of electromagnetism:

**Gauss's Law**: 
$$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$$
Electric charges create electric fields (sources and sinks).

**No Magnetic Monopoles**: 
$$\nabla \cdot \vec{B} = 0$$
No isolated magnetic charges exist (yet!).

**Faraday's Law**: 
$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$
Changing magnetic field induces electric field (electric generator).

**Ampère-Maxwell Law**: 
$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\epsilon_0 \frac{\partial \vec{E}}{\partial t}$$
Current and changing electric field create magnetic field (electromagnet + displacement current).

---

## 2. The Wave Equation and Plane Waves

In vacuum (ρ = 0, J = 0), Maxwell's equations combine to give:

$$\nabla^2 \vec{E} - \mu_0\epsilon_0\frac{\partial^2 \vec{E}}{\partial t^2} = 0$$

**Speed of light**:
$$c = \frac{1}{\sqrt{\mu_0\epsilon_0}}$$

**Plane wave solution**:
$$\vec{E}(\vec{r}, t) = \vec{E}_0 \cos(\vec{k} \cdot \vec{r} - \omega t)$$

with **dispersion relation**: $\omega = ck$

---

## 3. Electromagnetic Energy and Momentum

**Poynting Vector** (energy flux):
$$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B}$$

Direction of energy flow; magnitude is power per unit area (W/m²).

**Energy density**:
$$u = \frac{1}{2}\left(\epsilon_0 E^2 + \frac{1}{\mu_0}B^2\right)$$

**Momentum density**:
$$\vec{g} = \epsilon_0(\vec{E} \times \vec{B}) = \frac{\vec{S}}{c^2}$$

Light carries momentum! Radiation pressure: $P = I/c$ where I is intensity.

---

## 4. Radiation from Accelerating Charges

**Larmor Formula** (power radiated by accelerating charge):
$$P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3}$$

**Key insight**: Radiation is proportional to acceleration, not velocity!
- Electrons accelerating in antenna radiate (radio, TV)
- Synchrotron radiation: highly relativistic particles in circular orbit radiate strongly

**Dipole Radiation Pattern**:
$$\frac{dP}{d\Omega} = \frac{q^2 a^2 \sin^2\theta}{16\pi^2\epsilon_0 c^3}$$

Donut-shaped pattern (no radiation along axis, maximum perpendicular).

---

## 5. Lienard-Wiechert Potentials

For a moving charge, the fields at time t and position r depend on the **retarded time**:
$$t_{\text{ret}} = t - \frac{|\vec{r} - \vec{r}_s(t_{\text{ret}})|}{c}$$

This causality is fundamental: information propagates at speed c.

**Retarded potentials**:
$$\Phi(\vec{r}, t) = \frac{1}{4\pi\epsilon_0}\frac{q}{(1 - \vec{\beta} \cdot \hat{R})(1 - \beta^2)^{1/2} R}\bigg|_{\text{ret}}$$

where $\vec{R} = \vec{r} - \vec{r}_s$ and $\vec{\beta} = \vec{v}/c$.

---

## 6. Boundary Conditions and Reflection

**At a conductor**: $E_{\perp} = 0$, $B_{\parallel}$ related to surface current

**Fresnel Equations** (light incident on interface):
$$r = \frac{n_1\cos\theta_i - n_2\cos\theta_t}{n_1\cos\theta_i + n_2\cos\theta_t}$$ (s-polarization)

**Brewster's Angle**: When light is p-polarized, at angle $\theta_B = \arctan(n_2/n_1)$, there's no reflection! Used in sunglasses and optical components.

---

## 7. Skin Depth and Attenuation

In a conductor, EM waves decay exponentially:
$$\vec{E}(x, t) = \vec{E}_0 e^{-x/d} e^{i(kx - \omega t)}$$

**Skin depth** (characteristic penetration):
$$d = \sqrt{\frac{2}{\mu_0 \omega \sigma}}$$

where σ is conductivity.

**Examples** (at ω = 2π × 60 Hz, 50 Hz power line frequency):
- Copper: d ≈ 8.5 mm
- Seawater: d ≈ 0.25 m
- Ground: d ≈ 700 m

Practical: Radio signals don't penetrate conductors; why submarines use very low frequency!

---

## Key References

**Essential Books**:
1. **Griffiths**, "Introduction to Electrodynamics" (4th ed.) — best intro, physical intuition
2. **Jackson**, "Classical Electrodynamics" (3rd ed.) — graduate standard, rigorous
3. **Purcell & Morin**, "Electricity and Magnetism" (2nd ed.) — elegant approach

**Landmark Papers**:
- **Maxwell (1865)**: Unified electricity, magnetism, and light
- **Hertz (1888)**: Experimentally confirmed EM waves

**Applications**:
- **Antennas**: Dipole radiation patterns
- **Optical fibers**: Waveguide propagation
- **Radar**: Doppler shift of reflected waves
- **Cosmology**: Cosmic microwave background (thermal EM radiation)

---

## Study Roadmap

1. Master Maxwell's equations (memorize them!)
2. Derive wave equation from Maxwell's equations
3. Solve for plane waves and verify dispersion relation
4. Compute Poynting vector for wave energy
5. Understand retardation effects
6. Apply boundary conditions to real problems

**This is the foundation of all modern technology!**

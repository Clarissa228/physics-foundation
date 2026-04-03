# Topic 6: Gravitation

## Overview
Gravitation is the weakest of the four fundamental forces, yet it dominates cosmic structure. This topic covers Newton's law of universal gravitation, gravitational field theory, orbital mechanics, and Kepler's laws.

## Key Concepts

### Newton's Law of Universal Gravitation
Any two point masses attract each other with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.

$$F = \frac{GM m_1 m_2}{r^2}$$

where:
- $G = 6.674 \times 10^{-11}$ N·m²/kg² (gravitational constant)
- $m_1, m_2$ are masses
- $r$ is the distance between centers

**Key insight**: Gravity is universal and long-range. Every mass attracts every other mass.

### Gravitational Field and Potential

**Field strength**: The gravitational field at distance $r$ from mass $M$ is:

$$\vec{g} = -\frac{GM}{r^2}\hat{r}$$

Units: m/s² (same as acceleration)

**Gravitational potential energy**: For a point mass at distance $r$ from mass $M$:

$$U(r) = -\frac{GMm}{r}$$

**Gravitational potential**: Potential energy per unit mass:

$$\phi(r) = -\frac{GM}{r}$$

Both are negative and increase (become less negative) as $r$ increases.

### Kepler's Three Laws

#### Law 1: Law of Orbits
Every planet orbits the sun in an elliptical path, with the sun at one focus.

#### Law 2: Law of Equal Areas
A line joining a planet and the sun sweeps out equal areas in equal times. This is a consequence of **conservation of angular momentum**.

For an orbit: $\frac{dA}{dt} = \frac{L}{2m} = \text{constant}$

#### Law 3: Law of Periods
The square of the orbital period is proportional to the cube of the semi-major axis:

$$T^2 = \frac{4\pi^2}{GM}a^3$$

where $a$ is the semi-major axis.

**Derivation for circular orbits**:
For a circular orbit, gravitational force provides centripetal force:
$$\frac{GMm}{r^2} = m\omega^2 r = m\frac{4\pi^2}{T^2}r$$

Solving:
$$T^2 = \frac{4\pi^2}{GM}r^3$$

This explains why planets farther from the sun have longer periods.

### Escape Velocity

The minimum speed needed for an object to escape a gravitational field (reach infinity with zero speed):

$$v_{\text{escape}} = \sqrt{\frac{2GM}{R}}$$

**Derivation** (energy conservation):
$$\frac{1}{2}mv_{\text{escape}}^2 - \frac{GMm}{R} = 0$$

$$v_{\text{escape}} = \sqrt{\frac{2GM}{R}}$$

**Note**: Escape velocity is independent of the object's mass.

### Variation of g with Altitude and Depth

**On Earth's surface**: $g = 9.8$ m/s²

**At altitude $h$ above surface**:
$$g(h) = \frac{GM}{(R+h)^2} = g_0\left(\frac{R}{R+h}\right)^2 \approx g_0\left(1 - \frac{2h}{R}\right)$$

where $R$ is Earth's radius (~6371 km).

**At depth $d$ below surface** (assuming uniform density):
$$g(d) = g_0\left(1 - \frac{d}{R}\right) = g_0\frac{R-d}{R}$$

The gravitational field **inside** a uniform sphere increases linearly with distance from center.

### Orbital Mechanics

**For circular orbits**:
- Orbital speed: $v = \sqrt{\frac{GM}{r}}$
- Orbital period: $T = 2\pi\sqrt{\frac{r^3}{GM}}$
- Kinetic energy: $K = \frac{GMm}{2r}$
- Potential energy: $U = -\frac{GMm}{r}$
- Total energy: $E = -\frac{GMm}{2r}$ (negative = bound orbit)

**For elliptical orbits**:
- Use semi-major axis $a$ instead of $r$ in energy and period formulas
- Perihelion (closest): $r_p = a(1-e)$
- Aphelion (farthest): $r_a = a(1+e)$
- Eccentricity: $e = \frac{r_a - r_p}{r_a + r_p}$

### Geostationary Orbits

A satellite above the equator with orbital period = 24 hours appears stationary from Earth.

For geostationary orbit:
$$T = 24 \text{ hours} = 86400 \text{ s}$$

Using $T^2 = \frac{4\pi^2}{GM}a^3$:
$$a = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3} \approx 42164 \text{ km}$$

Height above Earth surface: $h = a - R \approx 35786 \text{ km}$

**Applications**: Weather satellites, telecommunications, broadcasting.

### Gravitational Slingshot Effect

When a spacecraft passes near a planet, it can gain energy. The spacecraft "bounces" off the planet's gravitational field. In the planet's frame, the spacecraft reverses direction. In the sun's frame, the spacecraft gains kinetic energy (at the planet's expense).

**Energy gain depends on**:
- Approach speed relative to planet
- Closest approach distance
- Planet's orbital velocity

This technique has been used extensively: Voyager probes, New Horizons, etc.

## Physical Constants

| Constant | Symbol | Value | Units |
|----------|--------|-------|-------|
| Gravitational constant | $G$ | $6.674 \times 10^{-11}$ | N·m²/kg² |
| Earth mass | $M_E$ | $5.972 \times 10^{24}$ | kg |
| Earth radius | $R_E$ | $6.371 \times 10^{6}$ | m |
| Solar mass | $M_{\odot}$ | $1.989 \times 10^{30}$ | kg |
| AU (Earth-Sun distance) | $a_E$ | $1.496 \times 10^{11}$ | m |

## Key References

### Textbooks
- **NCERT Class 11 Physics, Chapter 8**: Gravitation
- **H.C. Verma, Chapter 11**: Gravitation
- **Goldstein, Chapter 3**: The Two-Body Problem (advanced orbital mechanics)
- **Carroll & Ostlie**: "An Introduction to Modern Astrophysics" — comprehensive coverage of stellar dynamics

### Original Research
- **Kepler, Johannes (1609)**: "Astronomia Nova" — First two laws of planetary motion
- **Newton, Isaac (1687)**: "Philosophiæ Naturalis Principia Mathematica" (Mathematical Principles of Natural Philosophy) — Universal gravitation and laws of motion
- **Abbott, B.P. et al. (2016)**: "Observation of Gravitational Waves from a Binary Black Hole Merger" (LIGO detection) — *Physical Review Letters*, 116, 061102
  - First direct detection of gravitational waves predicted by Einstein's general relativity

## Modern Applications

1. **Satellite Technology**: GPS, communications, weather monitoring
2. **Gravitational Waves**: LIGO/Virgo detectors observing black hole and neutron star mergers
3. **Exoplanet Detection**: Using orbital dynamics and Kepler's laws
4. **Space Exploration**: Orbital maneuvers, escape trajectories, gravitational assists
5. **Cosmology**: Structure formation, dark matter dynamics

## Problem-Solving Strategy

When solving gravitation problems:
1. Identify the system (point mass, extended mass, orbit)
2. Choose appropriate coordinate system
3. Apply Newton's law or energy conservation
4. For orbits, use $T^2 \propto a^3$ or energy conservation
5. Check units and magnitudes against physical intuition

# Topic 10: Oscillations and Waves

## Overview
Oscillations (periodic motion) and waves (propagating oscillations) are fundamental to physics. Applications include sound, light, seismic waves, and quantum phenomena.

## Simple Harmonic Motion (SHM)

### Definition
Motion where acceleration is proportional to displacement and directed opposite:
$$a = -\omega^2 x$$

where $\omega = 2\pi f = \sqrt{k/m}$ is the angular frequency.

### Kinematic Equations

**Displacement**:
$$x(t) = A \cos(\omega t + \phi)$$

where:
- $A$ is amplitude
- $\omega$ is angular frequency
- $\phi$ is initial phase

**Velocity**:
$$v(t) = -A\omega \sin(\omega t + \phi) = v_{max} \sin(\omega t + \phi + \pi/2)$$

**Acceleration**:
$$a(t) = -A\omega^2 \cos(\omega t + \phi) = -\omega^2 x(t)$$

### Period and Frequency

**Period**: $T = \frac{2\pi}{\omega} = \frac{1}{f}$

**Frequency**: $f = \frac{1}{T}$ (Hz)

### Energy in SHM

**Kinetic energy**:
$$KE = \frac{1}{2}m v^2 = \frac{1}{2}m\omega^2(A^2 - x^2)$$

**Potential energy**:
$$PE = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2 x^2$$

**Total energy** (conserved):
$$E = KE + PE = \frac{1}{2}kA^2 = \frac{1}{2}m\omega^2 A^2 = \text{constant}$$

Energy oscillates between kinetic and potential with period $T/2$.

## Damped Oscillations

Real oscillations lose energy due to friction.

**Equation of motion**:
$$m\ddot{x} + b\dot{x} + kx = 0$$

**Damping coefficient**: $b$ (friction/air resistance)

**Damping ratio**: $\zeta = \frac{b}{2\sqrt{mk}}$

### Three Regimes

1. **Underdamped** ($\zeta < 1$): Oscillates with decreasing amplitude
   $$x(t) = A e^{-\zeta\omega_0 t}\cos(\omega_d t + \phi)$$
   where $\omega_d = \omega_0\sqrt{1-\zeta^2}$

2. **Critically damped** ($\zeta = 1$): Returns to equilibrium fastest without oscillating

3. **Overdamped** ($\zeta > 1$): Slowly returns without oscillating

## Driven Oscillations and Resonance

External driving force: $F(t) = F_0 \cos(\omega_{drive} t)$

**Amplitude of steady-state oscillation**:
$$A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\zeta\omega_0\omega)^2}}$$

**Resonance**: Maximum amplitude when $\omega \approx \omega_0$ (natural frequency)

**Quality factor**:
$$Q = \frac{\omega_0}{2\zeta\omega_0} = \frac{1}{2\zeta}$$

High $Q$ = sharp resonance, low damping.

## Waves

### Definition
A disturbance that propagates through space carrying energy and momentum, not matter.

### Wave Equation
$$\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}$$

where $v$ is wave speed.

### Wave Functions

**Traveling wave** (moving in +x direction):
$$y(x,t) = A \cos(kx - \omega t + \phi)$$

where:
- $k = 2\pi/\lambda$ is wave number
- $\omega = 2\pi f$ is angular frequency
- $\lambda$ is wavelength
- $v = \lambda f = \omega/k$ is wave speed

### Wave Properties

**Wavelength** ($\lambda$): Distance between consecutive peaks
**Frequency** ($f$): Number of oscillations per second
**Period** ($T = 1/f$): Time for one complete oscillation
**Speed**: $v = \lambda f$

## Types of Waves

### Transverse Waves
Particles oscillate perpendicular to wave propagation.
- Example: Light, waves on a string

### Longitudinal Waves
Particles oscillate parallel to wave propagation.
- Example: Sound, compression waves

### Mechanical vs Electromagnetic
- **Mechanical**: Require a medium (sound, water waves)
- **Electromagnetic**: Propagate in vacuum (light, radio)

## Superposition and Interference

### Superposition Principle
When two or more waves overlap, the resultant displacement is the sum of individual displacements:
$$y_{total} = y_1 + y_2 + ...$$

### Constructive Interference
Waves combine to increase amplitude (crests align):
$$\Delta \phi = 2\pi n$$ (phase difference = $2\pi n$)

### Destructive Interference
Waves combine to decrease amplitude (crest-trough alignment):
$$\Delta \phi = (2n+1)\pi$$ (phase difference = odd multiple of $\pi$)

## Standing Waves

When a traveling wave reflects from a fixed boundary, a standing wave forms.

**Standing wave condition**:
$$L = n\frac{\lambda}{2}$$ (integer number of half-wavelengths)

**Nodes**: Points of zero amplitude (at boundaries)
**Antinodes**: Points of maximum amplitude

**Frequencies** (for string fixed at both ends):
$$f_n = \frac{nv}{2L} = nf_1$$

where $f_1 = v/(2L)$ is fundamental frequency.

## Beats

When two waves of slightly different frequencies interfere:

**Beat frequency**:
$$f_{beat} = |f_1 - f_2|$$

**Amplitude modulation**:
$$y(t) = 2A\cos(2\pi f_{beat} t / 2)\cos(2\pi f_{avg} t)$$

## Doppler Effect

### Frequency Shift
When source and observer move relative to each other:

**Source moving toward stationary observer**:
$$f' = f \frac{v}{v - v_s}$$

**Observer moving toward stationary source**:
$$f' = f \frac{v + v_o}{v}$$

**Both moving**:
$$f' = f \frac{v + v_o}{v - v_s}$$

where:
- $f$ is rest frequency
- $v$ is wave speed
- $v_s$, $v_o$ are source and observer speeds (positive toward each other)

### Shock Waves
Mach number: $M = v_{source}/v_{sound}$
- $M < 1$: Subsonic
- $M = 1$: Sonic (at sound barrier)
- $M > 1$: Supersonic (shock cone forms)

## Fourier Analysis

Any periodic waveform can be decomposed into sine/cosine components (harmonics):

$$y(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n\omega t) + b_n \sin(n\omega t)]$$

**Fundamental**: First harmonic, frequency = $f$
**Overtones**: Higher harmonics, frequencies = $nf$

## Key Physical Constants

| Quantity | Symbol | Value | Units |
|----------|--------|-------|-------|
| Speed of light (vacuum) | $c$ | 3.0 × 10⁸ | m/s |
| Speed of sound (air, 20°C) | $v_s$ | 343 | m/s |

## Problem-Solving Strategies

### SHM Problems
1. Identify: amplitude $A$, frequency $f$ (or $\omega$), phase $\phi$
2. Write displacement: $x(t) = A\cos(\omega t + \phi)$
3. Find velocity and acceleration by differentiation
4. Use energy conservation if needed

### Wave Problems
1. Identify wave type and properties: $v$, $f$, $\lambda$
2. Use $v = \lambda f$ to relate quantities
3. For superposition: add displacements at each point
4. Check phase relationships for interference

### Resonance Problems
1. Find natural frequency: $\omega_0 = \sqrt{k/m}$ or $f_0 = v/(2L)$
2. Maximum response near $f = f_0$
3. Use $Q$ factor for quality of resonance

## Modern Applications

1. **Seismic Waves**: Earthquake detection and geological surveys
2. **Medical Ultrasound**: Diagnostic imaging using high-frequency sound
3. **Wireless Communication**: Radio and microwave propagation
4. **Quantum Mechanics**: Wave-particle duality of electrons
5. **Music Acoustics**: Standing waves in instruments, frequency analysis
6. **Gravitational Waves**: Ripples in spacetime from massive accelerating objects (LIGO detection 2015)

## References

### Textbooks
- **NCERT Class 11 Physics, Chapters 14-15**: Oscillations and Waves
- **H.C. Verma, Chapter 12**: Simple Harmonic Motion; Chapters 15-16: Waves
- **French**: "Vibrations and Waves" — comprehensive treatment
- **Pain**: "The Physics of Vibrations and Waves"

### Historical Papers
- **Huygens, C. (1690)**: Wave theory of light
- **Young, T. (1801)**: Double-slit interference experiment
- **Fourier, J.B. (1822)**: Fourier series and analysis

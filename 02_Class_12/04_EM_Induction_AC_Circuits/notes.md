# Electromagnetic Induction and AC Circuits

## Overview
Electromagnetic induction describes how changing magnetic flux generates electric fields and EMF. AC circuits extend this to time-varying quantities.

## Key Concepts

### 1. Faraday's Law
The induced EMF in a circuit equals the negative rate of change of magnetic flux:
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

where $\Phi_B = \int \vec{B} \cdot d\vec{A}$

**Lenz's Law**: The induced EMF opposes the change that produced it.

### 2. Motional EMF
When a conductor moves in a magnetic field:
$$\mathcal{E} = BLv$$

where $B$ is field, $L$ is conductor length, $v$ is velocity perpendicular to both.

### 3. Self-Inductance
When current changes in a coil, it creates its own induced EMF:
$$L = \frac{N\Phi_B}{I}$$

**EMF in inductor**: $\mathcal{E} = -L\frac{dI}{dt}$

For solenoid: $L = \mu_0 n^2 V = \mu_0 n^2 AL$

### 4. Mutual Inductance
EMF induced in one coil by changing current in another:
$$M = \frac{\Phi_{21}}{I_1}$$

$$\mathcal{E}_2 = -M\frac{dI_1}{dt}$$

**Coupling coefficient**: $k = M/\sqrt{L_1 L_2}$

### 5. Transformers
In an ideal transformer with primary (N₁) and secondary (N₂) coils:
$$\frac{V_2}{V_1} = \frac{N_2}{N_1}$$

$$I_1 N_1 = I_2 N_2$$ (Power conservation)

### 6. AC Voltage and Current
For sinusoidal AC:
$$V(t) = V_0 \sin(\omega t + \phi)$$
$$I(t) = I_0 \sin(\omega t)$$

where:
- $V_0, I_0$ are peak values
- $\omega = 2\pi f$ is angular frequency
- RMS values: $V_{rms} = V_0/\sqrt{2}$, $I_{rms} = I_0/\sqrt{2}$

### 7. Impedance
Complex resistance in AC circuits:
$$Z = \sqrt{R^2 + (X_L - X_C)^2}$$

where:
- $X_L = \omega L$ (inductive reactance)
- $X_C = 1/(\omega C)$ (capacitive reactance)

### 8. Phase Relationships
**For resistor**: Voltage and current in phase
**For inductor**: Voltage leads current by 90°
**For capacitor**: Current leads voltage by 90°

### 9. LCR Series Circuit
Total impedance: $Z = \sqrt{R^2 + (\omega L - 1/\omega C)^2}$

Current: $I = V_0/Z$

**Resonance** occurs at $\omega_0 = 1/\sqrt{LC}$ where $X_L = X_C$

At resonance:
- $Z = R$ (minimum)
- $I = I_{max} = V_0/R$
- Phase angle $\phi = 0$

**Quality factor**: $Q = \omega_0 L / R = 1/(R\sqrt{C/L})$

### 10. Power in AC Circuits
**Instantaneous power**: $P(t) = V(t)I(t)$

**Average power**: $P_{avg} = V_{rms}I_{rms}\cos\phi = I_{rms}^2 R$

where $\cos\phi$ is the **power factor**

- In pure R: $\cos\phi = 1$ (all power dissipated)
- In pure L or C: $\cos\phi = 0$ (no net power)
- In RLC: $\cos\phi = R/Z$ (partially dissipated)

**Reactive power**: $Q = V_{rms}I_{rms}\sin\phi$

**Apparent power**: $S = V_{rms}I_{rms}$

## Historical Context

- **Faraday (1831)**: Discovered electromagnetic induction experimentally
- **Lenz (1834)**: Formulated law of induced EMF direction
- **Neumann (1845)**: Quantified mutual inductance
- **Tesla (1880s)**: AC motor and transformer pioneer
- **Steinmetz (1890s)**: Developed AC circuit theory with complex numbers

## Reference Books

1. **NCERT Physics Class 12** - Chapters 6-7: Electromagnetic Induction and AC
2. **Griffiths - Introduction to Electrodynamics** - Chapter 7: Electrodynamics
3. **H.C. Verma - Concepts of Physics Vol. 2** - Chapters 35-38
4. **Purcell - Electricity and Magnetism** - Chapter 7

## Key Equations Summary

| Concept | Equation |
|---------|----------|
| Faraday's law | ε = -dΦ_B/dt |
| Motional EMF | ε = BLv |
| Inductance | L = NΦ_B/I |
| Transformer | V₂/V₁ = N₂/N₁ |
| Inductive reactance | X_L = ωL |
| Capacitive reactance | X_C = 1/(ωC) |
| Impedance | Z = √(R² + (X_L - X_C)²) |
| Resonance | ω₀ = 1/√(LC) |
| Average power | P = VI cosφ |
| Power factor | cosφ = R/Z |

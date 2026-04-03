# Current Electricity

## Overview
Current electricity deals with the flow of electric charges and the circuits that conduct them.

## Key Concepts

### 1. Electric Current
The rate of flow of electric charge:
$$I = \frac{dQ}{dt}$$

Unit: Ampere (A), where 1 A = 1 C/s

**Current density**: $J = \frac{I}{A}$ (A/m²)

### 2. Ohm's Law
$$V = IR \quad \text{or} \quad I = \frac{V}{R}$$

where:
- $V$ is potential difference (Volts)
- $I$ is current (Amperes)
- $R$ is resistance (Ohms, Ω)

**Resistance** depends on material:
$$R = \rho \frac{L}{A}$$

where:
- $\rho$ is resistivity (Ω⋅m)
- $L$ is length (m)
- $A$ is cross-sectional area (m²)

### 3. Drift Velocity
In a conductor, electrons move with average velocity:
$$v_d = \frac{I}{nAe}$$

where:
- $n$ is electron number density
- $A$ is cross-sectional area
- $e$ is elementary charge

Surprisingly, drift velocity is very small (mm/s) but current is created by enormous charge carrier density.

### 4. Resistivity and Conductivity
$$\sigma = \frac{1}{\rho}$$

where $\sigma$ is conductivity (S/m).

**Temperature dependence**: $\rho = \rho_0[1 + \alpha(T - T_0)]$

where $\alpha$ is temperature coefficient of resistance.

### 5. Kirchhoff's Laws

**Kirchhoff's Current Law (KCL)**: At any junction, sum of currents in = sum of currents out
$$\sum I_{\text{in}} = \sum I_{\text{out}}$$

**Kirchhoff's Voltage Law (KVL)**: Around any closed loop, sum of voltage rises = sum of voltage drops
$$\sum V_{\text{rise}} = \sum V_{\text{drop}}$$

### 6. Resistors in Series and Parallel

**Series**: Same current, voltages add
$$R_{\text{eq}} = R_1 + R_2 + \cdots$$

**Parallel**: Same voltage, currents add
$$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots$$

### 7. Wheatstone Bridge
A circuit for measuring unknown resistance with great precision:
$$\frac{R_1}{R_2} = \frac{R_3}{R_4}$$

At balance, no current flows through the galvanometer.

### 8. Potentiometer
A uniform wire of length $L$ used to measure EMF and compare potential differences.

Null point method: If jockey is at length $l$ for unknown EMF $\mathcal{E}$ and at length $l_0$ for standard cell $E_0$:
$$\frac{\mathcal{E}}{E_0} = \frac{l}{l_0}$$

### 9. RC Circuits

**Charging a capacitor** (switch closed at t=0):
$$Q(t) = Q_0(1 - e^{-t/RC})$$
$$V(t) = V_0(1 - e^{-t/RC})$$
$$I(t) = \frac{V_0}{R}e^{-t/RC}$$

**Discharging a capacitor** (switch opened):
$$Q(t) = Q_0 e^{-t/RC}$$
$$V(t) = V_0 e^{-t/RC}$$
$$I(t) = -\frac{V_0}{R}e^{-t/RC}$$

**Time constant**: $\tau = RC$ (time for charge/voltage to reach 63.2% of final value)

### 10. Power Dissipation
$$P = VI = I^2R = \frac{V^2}{R}$$

where $P$ is power in Watts.

**Energy dissipated in time $t$**: $W = Pt = I^2Rt$

## Historical Context

- **Ohm (1827)**: Established empirical relationship between voltage and current
- **Kirchhoff (1845)**: Formulated current and voltage laws
- **Joule (1840s)**: Discovered thermal effects of electric current
- **Wheatstone (1843)**: Developed balanced bridge for precision resistance measurement

## Reference Books

1. **NCERT Physics Class 12** - Chapter 3: Current Electricity
2. **H.C. Verma - Concepts of Physics Vol. 2** - Chapter 32: Electric Current
3. **Horowitz & Hill - The Art of Electronics**: Comprehensive circuit analysis
4. **Halliday, Resnick, Walker - Fundamentals of Physics** - Chapters 26-27

## Common Resistivity Values (at 20°C)

| Material | ρ (Ω⋅m) |
|----------|---------|
| Copper | 1.68×10⁻⁸ |
| Aluminum | 2.65×10⁻⁸ |
| Tungsten | 5.6×10⁻⁸ |
| Iron | 1.0×10⁻⁷ |
| Nichrome | 1.0×10⁻⁶ |
| Carbon | 3.5×10⁻⁵ |

## Key Equations Summary

| Concept | Equation |
|---------|----------|
| Ohm's Law | V = IR |
| Resistance | R = ρL/A |
| Power | P = VI = I²R |
| Series R | R_eq = R₁ + R₂ + ... |
| Parallel R | 1/R_eq = 1/R₁ + 1/R₂ + ... |
| RC charging | Q = Q₀(1-e^(-t/RC)) |
| RC discharging | Q = Q₀e^(-t/RC) |
| Time constant | τ = RC |

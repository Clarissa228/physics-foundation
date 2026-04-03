# Topic 8: Thermodynamics

## Overview
Thermodynamics describes the behavior of energy in systems, particularly heat and work. It provides fundamental limits on energy conversion processes.

## Laws of Thermodynamics

### Zeroth Law: Thermal Equilibrium
If system A is in thermal equilibrium with system C, and system B is in thermal equilibrium with system C, then system A is in thermal equilibrium with system B.

**Consequence**: Defines the concept of temperature and justifies thermometer use.

### First Law: Energy Conservation
Energy cannot be created or destroyed, only converted:

$$\Delta U = Q - W$$

where:
- $\Delta U$ = change in internal energy
- $Q$ = heat absorbed by system
- $W$ = work done by the system

**Equivalent form**:
$$Q = \Delta U + W$$

**Note**: Sign convention:
- $Q > 0$: heat absorbed by system
- $W > 0$: work done by system
- $\Delta U > 0$: internal energy increases

### Second Law: Entropy
The entropy of an isolated system never decreases:

$$dS \geq 0$$

for any process in an isolated system.

**Consequence**: Heat flows spontaneously from hot to cold, not vice versa. No process is 100% efficient.

### Third Law: Absolute Zero
The entropy of a perfect crystal approaches zero as temperature approaches absolute zero:

$$\lim_{T \to 0} S(T) = 0$$

**Consequence**: Absolute zero (0 K = -273.15°C) cannot be reached in a finite number of steps.

## Thermodynamic Processes

### Isothermal Process (T = constant)
- Temperature is held constant
- $\Delta U = 0$ (for ideal gas)
- $Q = W = nRT \ln(V_f/V_i)$
- On P-V diagram: hyperbola ($PV = \text{const}$)

### Adiabatic Process (Q = 0)
- No heat transfer
- $\Delta U = -W$
- For ideal gas: $TV^{\gamma-1} = \text{const}$ or $PV^\gamma = \text{const}$
- On P-V diagram: steeper curve than isothermal
- $\gamma$ = heat capacity ratio = $C_p/C_V$

### Isobaric Process (P = constant)
- Constant pressure
- $W = P\Delta V = nR\Delta T$
- $Q = nC_p \Delta T$
- On P-V diagram: horizontal line

### Isochoric Process (V = constant)
- Constant volume (rigid container)
- $W = 0$ (no work done)
- $Q = \Delta U = nC_V \Delta T$
- On P-V diagram: vertical line

## Internal Energy and Heat Capacity

### Internal Energy
For an ideal gas, internal energy depends only on temperature:

$$U = nC_V T$$

where $C_V$ is the molar heat capacity at constant volume.

**Change in internal energy**:
$$\Delta U = nC_V \Delta T$$

### Heat Capacity
**At constant volume**:
$$C_V = \left(\frac{\partial U}{\partial T}\right)_V$$

**At constant pressure**:
$$C_p = \left(\frac{\partial H}{\partial T}\right)_P = C_V + R$$

**Relation**: $C_p - C_V = R$ (per mole)

**Heat capacity ratio**:
$$\gamma = \frac{C_p}{C_V}$$

- Monatomic gas: $\gamma = 5/3 \approx 1.67$
- Diatomic gas: $\gamma = 7/5 = 1.40$
- Polyatomic gas: $\gamma \approx 1.33$

## Heat Engines and Efficiency

### Heat Engine
A device that converts heat (at high temperature) into mechanical work.

**Energy flow**:
- Input: $Q_H$ from hot reservoir (temperature $T_H$)
- Output: $W$ (useful work)
- Rejected: $Q_C$ to cold reservoir (temperature $T_C$)

**Energy balance**: $Q_H = W + Q_C$

### Efficiency
Efficiency is the fraction of heat converted to useful work:

$$\eta = \frac{W}{Q_H} = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H}$$

**Real engines**: $\eta < \eta_{\text{Carnot}}$

### Carnot Engine
An ideal reversible heat engine operating between two temperatures:

**Carnot Efficiency**:
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$

where $T$ is absolute temperature (Kelvin).

**Key properties**:
- No real engine has higher efficiency
- Efficiency increases with larger temperature difference
- Maximum possible efficiency increases as $T_C$ decreases

**Example**: If $T_H = 600$ K and $T_C = 300$ K:
$$\eta_{\text{Carnot}} = 1 - \frac{300}{600} = 0.5 = 50\%$$

### Carnot Cycle (reversible)
Four processes on P-V diagram:
1. **Isothermal expansion** (temperature $T_H$): absorbs heat $Q_H$
2. **Adiabatic expansion** (temperature drops from $T_H$ to $T_C$): no heat transfer
3. **Isothermal compression** (temperature $T_C$): rejects heat $Q_C$
4. **Adiabatic compression** (temperature rises from $T_C$ to $T_H$): no heat transfer

## Heat Pumps and Refrigerators

### Refrigerator
Removes heat from cold space and rejects it to surroundings (opposite of heat engine).

**Coefficient of Performance (COP)**:
$$\text{COP}_{\text{ref}} = \frac{Q_C}{W}$$

Higher COP = more efficient refrigerator.

### Heat Pump
Absorbs heat from cold source and delivers to hot space (for heating).

**COP for heat pump**:
$$\text{COP}_{\text{heat}} = \frac{Q_H}{W} = 1 + \text{COP}_{\text{ref}}$$

## Entropy and Irreversibility

### Entropy Definition
Entropy measures disorder or unavailability of energy:

$$dS = \frac{dQ_{\text{rev}}}{T}$$

For reversible process:
$$\Delta S = \int \frac{dQ_{\text{rev}}}{T}$$

### Entropy Change
**For reversible isothermal process**:
$$\Delta S = \frac{Q}{T}$$

**For ideal gas**:
$$\Delta S = nC_V \ln\left(\frac{T_f}{T_i}\right) + nR\ln\left(\frac{V_f}{V_i}\right)$$

### Second Law (Modern Form)
For any process in an isolated system:
$$\Delta S_{\text{total}} = \Delta S_{\text{system}} + \Delta S_{\text{surroundings}} \geq 0$$

- Reversible: $\Delta S = 0$
- Irreversible: $\Delta S > 0$

## Specific Heat

### Molar Heat Capacities for Ideal Gases

| Gas Type | Degrees of Freedom | $C_V$ | $C_p$ | $\gamma$ |
|----------|-------------------|-------|-------|---------|
| Monatomic (He, Ar) | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ | 1.67 |
| Diatomic (O₂, N₂) | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ | 1.40 |
| Polyatomic (CO₂) | 6+ | ~$3R$ | ~$4R$ | ~1.33 |

where $R = 8.314$ J/(mol·K)

## Work Calculations for Ideal Gas

### General Formula
$$W = \int P \, dV$$

### Isothermal ($T = \text{const}$, $PV = \text{const}$)
$$W = nRT \ln\left(\frac{V_f}{V_i}\right) = nRT \ln\left(\frac{P_i}{P_f}\right)$$

### Adiabatic ($Q = 0$, $PV^\gamma = \text{const}$)
$$W = \frac{P_i V_i - P_f V_f}{\gamma - 1} = \frac{nR(T_i - T_f)}{\gamma - 1}$$

### Isobaric ($P = \text{const}$)
$$W = P(V_f - V_i) = nR\Delta T$$

### Isochoric ($V = \text{const}$)
$$W = 0$$

## Real Engines and Cycles

### Otto Cycle (Gasoline Engine)
Four processes:
1. Isobaric intake
2. Adiabatic compression
3. Isochoric combustion
4. Adiabatic expansion (power stroke)

**Efficiency**:
$$\eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma-1}}$$

where $r = V_1/V_2$ is the compression ratio.

### Diesel Cycle (Diesel Engine)
Similar to Otto but with isobaric expansion during combustion.

## Key Constants

| Quantity | Symbol | Value | Units |
|----------|--------|-------|-------|
| Gas constant | $R$ | 8.314 | J/(mol·K) |
| Boltzmann constant | $k_B$ | 1.381 × 10⁻²³ | J/K |
| Absolute zero | 0 K | -273.15 | °C |

## Problem-Solving Strategies

1. **Identify the process**: isothermal, adiabatic, isobaric, or isochoric
2. **First Law**: $\Delta U = Q - W$
3. **Calculate changes**: $\Delta U$, $Q$, $W$ using process equations
4. **Check consistency**: Energy must be conserved
5. **For cycles**: Calculate net work and efficiency

## Modern Applications

1. **Power Generation**: Coal, nuclear, natural gas power plants use Carnot principles
2. **Refrigeration**: Refrigerators and air conditioners use reverse cycles
3. **Heat Pumps**: Heating homes efficiently in cold climates
4. **Internal Combustion Engines**: Otto and Diesel engines in vehicles
5. **Geothermal**: Extracting heat from Earth's interior
6. **Efficiency Limits**: Understanding why 100% efficiency is impossible

## References

### Textbooks
- **NCERT Class 11 Physics, Chapter 12**: Thermodynamics
- **H.C. Verma, Chapters 26-27**: Thermodynamics
- **Zemansky & Dittman**: "Heat and Thermodynamics"
- **Callen**: "Thermodynamics and an Introduction to Thermostatistics"

### Historical Papers
- **Carnot, S. (1824)**: "Réflexions sur la puissance motrice du feu" — Foundation of thermodynamics
- **Clausius, R. (1865)**: Entropy concept and 2nd law formulation

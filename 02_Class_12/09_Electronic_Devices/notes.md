# Electronic Devices and Semiconductors

## Overview
Semiconductors form the basis of modern electronics through controlled p-n junctions and transistors.

## Key Concepts

### 1. Energy Bands
- **Conductor**: Conduction and valence bands overlap
- **Semiconductor**: Small bandgap (< 4 eV)
- **Insulator**: Large bandgap (> 4 eV)

At T=0: valence band full, conduction band empty

### 2. Intrinsic Semiconductors
Pure Si or Ge with no dopants

At T > 0: thermal energy creates electron-hole pairs

Conductivity increases exponentially with temperature

### 3. Extrinsic Semiconductors

**n-type (electron doped)**:
- Donor impurity (Group V: P, As, Sb) adds electrons
- Fermi level near conduction band
- Electrons are majority carriers

**p-type (hole doped)**:
- Acceptor impurity (Group III: B, Al, Ga) adds holes
- Fermi level near valence band
- Holes are majority carriers

### 4. p-n Junction
Depletion region forms at junction with electric field

**Forward bias**: External voltage opposes depletion field
- Reduces barrier
- Current increases exponentially (Shockley equation)

**Reverse bias**: External voltage enhances depletion field
- Increases barrier
- Only reverse saturation current flows
- Continues until breakdown voltage

### 5. Diode I-V Characteristic
$$I = I_0(e^{V/nV_T} - 1)$$

where:
- I₀ = reverse saturation current
- V_T = thermal voltage ≈ 26 mV at room temp
- n = ideality factor (1-2)

### 6. Zener Diode
Reverse biased to operate in breakdown region

Used for voltage regulation (constant voltage drop)

### 7. Light-Emitting Diode (LED)
Forward biased: electrons and holes recombine

Photon energy: $h\nu = E_g$ (bandgap energy)

Photon wavelength: $\lambda = hc/E_g$

### 8. Photodiode
Reverse biased: absorbs photons

Photocurrent proportional to incident light intensity

### 9. Transistor Basics

**BJT (Bipolar Junction Transistor)**:
- Base current controls collector current
- Current gain: β = I_c/I_b
- Modes: cutoff, active, saturation

**MOSFET (Metal-Oxide Semiconductor FET)**:
- Gate voltage controls channel conductivity
- Input impedance very high

### 10. Logic Gates
Implement Boolean functions using transistors

- **NOT**: Single transistor (inverts)
- **NAND**: N-type pulls down
- **NOR**: Same pull-down topology

## Historical Context
- **Shockley, Bardeen, Brattain (1947)**: Transistor (Nobel 1956)
- **Kilby (1958)**: Integrated circuit
- **Moore (1965)**: Moore's law prediction
- **Noyce (1961)**: Planar IC fabrication

## Reference Books
1. NCERT Ch 14: Electronic Devices
2. Streetman: Solid State Electronic Devices
3. Razavi: Fundamentals of Microelectronics

## Key Equations

| Concept | Equation |
|---------|----------|
| Bandgap | E_g = hν |
| Diode current | I = I₀(e^(V/V_T) - 1) |
| LED wavelength | λ = hc/E_g |
| BJT gain | β = I_c/I_b |
| Thermal voltage | V_T ≈ 26 mV |
| Breakdown | V_BR (constant) |

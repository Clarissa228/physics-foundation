# Topic 7: Properties of Bulk Matter

## Overview
This topic covers the mechanical and fluid properties of materials - how they deform under stress, flow under pressure, and interact with surfaces.

## Elasticity and Deformation

### Stress
Stress is the force per unit area applied to a material:

$$\sigma = \frac{F}{A}$$

where $F$ is the applied force and $A$ is the cross-sectional area.

**Types of stress**:
- **Tensile stress**: pulling force (elongation)
- **Compressive stress**: pushing force (compression)
- **Shear stress**: parallel surface forces

### Strain
Strain is the fractional change in dimensions:

$$\varepsilon = \frac{\Delta L}{L_0}$$

where $\Delta L$ is the change in length and $L_0$ is the original length.

**Note**: Strain is dimensionless.

### Young's Modulus
Young's modulus measures the stiffness of a material (resistance to elongation):

$$Y = \frac{\text{stress}}{\text{strain}} = \frac{\sigma}{\varepsilon} = \frac{F/A}{\Delta L/L_0}$$

**Units**: Pa (Pascals) or N/m²

**Typical values**:
- Steel: ~200 GPa
- Aluminum: ~70 GPa
- Copper: ~130 GPa
- Rubber: ~0.1 GPa

### Hooke's Law
For elastic deformations (small strains), stress is proportional to strain:

$$\sigma = Y \cdot \varepsilon$$

or for springs:

$$F = kx$$

where $k$ is the spring constant and $x$ is displacement.

### Bulk Modulus
Bulk modulus measures resistance to volume change under uniform pressure:

$$B = -\frac{\text{pressure}}{\text{volumetric strain}} = -\frac{P}{\Delta V / V_0}$$

**Note**: The negative sign accounts for compression (volume decrease under positive pressure).

### Shear Modulus
Shear modulus measures resistance to shear (shape change without volume change):

$$G = \frac{\text{shear stress}}{\text{shear strain}} = \frac{F/A}{x/h}$$

where $x$ is the displacement and $h$ is the height.

## Fluid Mechanics

### Pressure in Fluids
Pressure is force per unit area perpendicular to the surface:

$$P = \frac{F_\perp}{A}$$

**Units**: Pa, atm, bar, psi

### Pressure Variation with Depth
In a static fluid, pressure increases with depth:

$$P(h) = P_0 + \rho g h$$

where:
- $P_0$ is pressure at surface
- $\rho$ is fluid density
- $g$ is gravitational acceleration
- $h$ is depth

**Derivation**: Consider a fluid column. The weight of fluid above creates pressure: $P = \rho g h$.

### Pascal's Law
Pressure applied to a confined fluid is transmitted equally in all directions:

$$P = \text{constant throughout the fluid}$$

**Applications**:
- Hydraulic press
- Hydraulic brakes
- Hydraulic lifts

**Advantage**: A small force on small piston = large force on large piston

### Archimedes' Principle
A body immersed in a fluid experiences an upward buoyant force equal to the weight of the fluid displaced:

$$F_B = \rho_{\text{fluid}} \cdot g \cdot V_{\text{displaced}}$$

**Consequence**:
- $F_B > W$ → object floats
- $F_B = W$ → object neutrally buoyant
- $F_B < W$ → object sinks

**Floating equilibrium**:
$$\rho_{\text{object}} V_{\text{total}} g = \rho_{\text{fluid}} g V_{\text{submerged}}$$

## Fluid Dynamics and Viscosity

### Viscosity
Viscosity is the resistance of a fluid to flow. Viscous force between fluid layers:

$$F = \eta A \frac{dv}{dy}$$

where:
- $\eta$ is the coefficient of viscosity (Pa·s)
- $A$ is the area of contact
- $dv/dy$ is the velocity gradient (shear rate)

### Stokes' Law
Drag force on a sphere moving through a viscous fluid:

$$F_D = 6\pi \eta r v$$

where:
- $\eta$ is viscosity
- $r$ is sphere radius
- $v$ is velocity

**Valid for**: Low Reynolds number (laminar flow around sphere)

### Terminal Velocity
When a sphere falls through a viscous fluid, eventually drag equals weight:

$$mg = 6\pi \eta r v_t$$

$$v_t = \frac{mg}{6\pi \eta r} = \frac{(\rho_s - \rho_f) g d^2}{18\eta}$$

where $\rho_s$ is sphere density and $\rho_f$ is fluid density.

### Poiseuille's Equation
Flow rate through a cylindrical pipe with viscous fluid:

$$Q = \frac{\pi P r^4}{8\eta L}$$

where:
- $Q$ is the volume flow rate
- $P$ is the pressure difference
- $r$ is pipe radius
- $\eta$ is viscosity
- $L$ is pipe length

**Key result**: Flow rate is proportional to $r^4$ (fourth power!)

**Velocity profile** in pipe (parabolic):
$$v(r_\perp) = \frac{P}{4\eta L}(r^2 - r_\perp^2)$$

where $r_\perp$ is distance from axis.

## Surface Tension and Capillarity

### Surface Tension
Surface tension is the energy per unit area (or force per unit length) at a liquid surface:

$$\gamma = \frac{\text{Surface Energy}}{A} = \frac{F}{L}$$

**Units**: N/m or J/m²

**Physical origin**: Molecules at surface have more potential energy (fewer neighbors).

**Typical values**:
- Water (20°C): ~0.072 N/m
- Mercury: ~0.486 N/m
- Alcohol: ~0.022 N/m

### Pressure Difference Across Curved Surface
For a liquid drop or bubble, surface tension creates internal pressure:

$$\Delta P = \frac{2\gamma}{R}$$

(for a sphere of radius $R$)

For a bubble (two surfaces):
$$\Delta P = \frac{4\gamma}{R}$$

### Angle of Contact
The angle between the liquid meniscus and the solid surface:

- **θ < 90°**: Wetting liquid (water on glass)
- **θ > 90°**: Non-wetting liquid (mercury on glass)
- **θ = 0°**: Perfect wetting
- **θ = 180°**: Perfect non-wetting

### Capillary Rise
When a capillary tube is placed in a liquid:

$$h = \frac{2\gamma \cos\theta}{\rho g r}$$

where:
- $\gamma$ is surface tension
- $\theta$ is contact angle
- $\rho$ is fluid density
- $g$ is gravity
- $r$ is tube radius

**Key insight**: $h \propto 1/r$ (thinner tube → higher rise)

**Physical mechanism**: Surface tension pulls liquid up the tube until weight of lifted column balances surface tension force.

## Physical Constants and Typical Values

| Property | Material | Value | Units |
|----------|----------|-------|-------|
| Young's Modulus (Y) | Steel | 200 | GPa |
| Young's Modulus | Aluminum | 70 | GPa |
| Young's Modulus | Rubber | 0.1 | GPa |
| Bulk Modulus | Water | 2.2 | GPa |
| Shear Modulus | Steel | 80 | GPa |
| Density | Water | 1000 | kg/m³ |
| Density | Mercury | 13600 | kg/m³ |
| Density | Air (STP) | 1.29 | kg/m³ |
| Viscosity | Water (20°C) | 0.001 | Pa·s |
| Viscosity | Air (20°C) | 1.81e-5 | Pa·s |
| Viscosity | Glycerin | 1.5 | Pa·s |
| Surface Tension | Water | 0.072 | N/m |
| Surface Tension | Mercury | 0.486 | N/m |

## Problem-Solving Strategies

### Elasticity Problems
1. Identify type of stress (tension, compression, shear)
2. Calculate stress: σ = F/A
3. Calculate strain: ε = ΔL/L₀
4. Use modulus definition to find unknown

### Fluid Pressure Problems
1. Identify reference level (usually surface)
2. Use P(h) = P₀ + ρgh to find pressure at depth
3. Remember pressure acts perpendicular to surface

### Buoyancy Problems
1. Calculate weight: W = mg = ρ_object × V × g
2. Calculate buoyant force: F_B = ρ_fluid × g × V_submerged
3. Net force: F_net = F_B - W

### Viscosity Problems
1. Check if Stokes' law applies (low Re)
2. For terminal velocity: drag force = weight
3. For Poiseuille flow: use Q = πPr⁴/(8ηL)

### Surface Tension Problems
1. Identify if wetting or non-wetting
2. For capillary rise: h = 2γcosθ/(ρgr)
3. Remember surface tension acts along liquid surface

## Key References

### Textbooks
- **NCERT Class 11 Physics, Chapters 9-10**: Mechanical Properties of Solids and Fluids
- **H.C. Verma, Chapters 13-14**: Elasticity and Fluids
- **Munson, Young, & Okiishi**: "Fundamentals of Fluid Mechanics" — comprehensive fluid mechanics
- **Young & Freedman**: "University Physics" — detailed elasticity section

### Historical Notes
- **Robert Hooke (1678)**: Hooke's Law - "ut tensio, sic vis" (as the extension, so the force)
- **George Stokes (1850s)**: Stokes' Law for viscous drag
- **Jean Léonard Marie Poiseuille (1840)**: Poiseuille's equation for flow in pipes
- **Blaise Pascal (1647)**: Pascal's Law for fluid pressure

## Modern Applications

1. **Material Science**: Testing Young's modulus of new materials (alloys, composites)
2. **Civil Engineering**: Stress analysis in beams, cables, and structures
3. **Biomechanics**: Bone elasticity, artery compliance under pressure
4. **Microfluidics**: Capillary effects dominate in small channels
5. **Blood Flow**: Poiseuille flow in capillaries and arteries
6. **Surface Chemistry**: Surfactants reduce surface tension (detergents, soap)
7. **Hydraulic Systems**: Brakes, power steering, industrial presses

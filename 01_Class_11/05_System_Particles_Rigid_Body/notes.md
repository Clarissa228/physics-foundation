# Topic 5: System of Particles and Rigid Body Motion

## Overview
This topic extends mechanics to systems of multiple particles and rigid bodies. Key concepts include center of mass, angular momentum, moment of inertia, and rotational kinematics and dynamics.

## Key Concepts

### 5.1 Center of Mass

**Definition:** The point where the entire mass of a system can be considered concentrated.

**For discrete masses:**
$$\vec{r}_{cm} = \frac{m_1\vec{r}_1 + m_2\vec{r}_2 + ... + m_n\vec{r}_n}{\sum m_i} = \frac{\sum m_i\vec{r}_i}{M_{total}}$$

**For continuous mass distribution:**
$$\vec{r}_{cm} = \frac{1}{M}\int \vec{r} \, dm$$

**Velocity of center of mass:**
$$\vec{v}_{cm} = \frac{\sum m_i\vec{v}_i}{M_{total}}$$

**Momentum of system:**
$$\vec{p}_{total} = M_{total}\vec{v}_{cm}$$

### 5.2 Moment of Inertia

**Definition:** Rotational analog of mass; measure of resistance to angular acceleration.

**For discrete masses:**
$$I = \sum m_i r_i^2$$

where $r_i$ is distance from axis of rotation.

**For continuous bodies:**
$$I = \int r^2 \, dm$$

**Common shapes (about center):**
- **Thin hoop/ring:** $I = MR^2$
- **Solid sphere:** $I = \frac{2}{5}MR^2$
- **Solid cylinder:** $I = \frac{1}{2}MR^2$
- **Thin rod (about center):** $I = \frac{1}{12}ML^2$
- **Thin rod (about end):** $I = \frac{1}{3}ML^2$

**Parallel axis theorem:**
$$I = I_{cm} + Md^2$$

where $d$ is distance from center of mass axis to new axis.

**Perpendicular axis theorem** (for planar objects):
$$I_z = I_x + I_y$$

### 5.3 Rotational Kinematics

**Angular displacement:** $\theta$ (radians)

**Angular velocity:** $\omega = \frac{d\theta}{dt}$ (rad/s)

**Angular acceleration:** $\alpha = \frac{d\omega}{dt}$ (rad/s²)

**Relationships with linear quantities:**
$$v = r\omega$$ (tangential velocity)
$$a_t = r\alpha$$ (tangential acceleration)
$$a_c = r\omega^2 = \frac{v^2}{r}$$ (centripetal acceleration)

**Equations for constant angular acceleration:**
$$\omega = \omega_0 + \alpha t$$
$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$$
$$\omega^2 = \omega_0^2 + 2\alpha\theta$$

### 5.4 Rotational Dynamics

**Torque:** Rotational analog of force.
$$\vec{\tau} = \vec{r} \times \vec{F}$$
$$\tau = rF\sin\theta$$

**Newton's 2nd law for rotation:**
$$\tau_{net} = I\alpha$$

**Rotational kinetic energy:**
$$KE_{rot} = \frac{1}{2}I\omega^2$$

**Angular momentum:**
$$\vec{L} = I\vec{\omega}$$

**Conservation of angular momentum:**
For isolated system (no external torque):
$$L_{initial} = L_{final}$$
$$I_1\omega_1 = I_2\omega_2$$

### 5.5 Rolling Motion

For object rolling without slipping:
$$v_{cm} = r\omega$$

**Total kinetic energy (rolling):**
$$KE_{total} = KE_{translational} + KE_{rotational}$$
$$KE_{total} = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\omega^2$$

For sphere rolling down incline (without slipping):
$$v = \sqrt{\frac{2gh}{1 + \frac{I}{MR^2}}}$$

For solid sphere: $v = \sqrt{\frac{10gh}{7}}$

### 5.6 Gyroscopic Motion and Precession

**Angular momentum:** $\vec{L} = I\vec{\omega}$

**Precession:** When external torque is applied perpendicular to angular momentum:
$$\omega_p = \frac{\tau}{L} = \frac{\tau}{I\omega}$$

where $\omega_p$ is precession angular velocity.

## Key Equations (Summary)

$$\vec{r}_{cm} = \frac{\sum m_i\vec{r}_i}{M}$$

$$I = \sum m_i r_i^2 = \int r^2 dm$$

$$I = I_{cm} + Md^2$$ (Parallel axis theorem)

$$\tau = I\alpha$$

$$L = I\omega$$

$$KE_{rot} = \frac{1}{2}I\omega^2$$

$$v = r\omega$$ (no-slip condition)

$$\omega_p = \frac{\tau}{L}$$ (Precession)

## Reference Books

1. **NCERT Physics Part 1** — Chapter 7: Clear introduction
2. **H.C. Verma, Concepts of Physics Vol 1** — Chapter 10: Excellent examples
3. **Kleppner & Kolenkow, "An Introduction to Mechanics"** — Chapter 7: Rigorous treatment
4. **Goldstein, "Classical Mechanics"** — Chapter 4-5: Advanced topics

## Learning Outcomes

By the end of this topic, you should be able to:
- [ ] Calculate center of mass for discrete and continuous systems
- [ ] Calculate moment of inertia using integration and parallel axis theorem
- [ ] Apply rotational analogs of Newton's laws
- [ ] Solve rolling motion problems
- [ ] Apply conservation of angular momentum
- [ ] Understand gyroscopic precession
- [ ] Analyze systems with both translational and rotational motion

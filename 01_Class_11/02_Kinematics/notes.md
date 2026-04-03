# Topic 2: Kinematics

## Overview
Kinematics describes the motion of objects without reference to the forces causing that motion. This topic covers the mathematical and graphical description of motion in one, two, and three dimensions using velocity, acceleration, and the kinematic equations.

## Key Concepts

### 2.1 Fundamental Definitions

**Position and Displacement:**
- Position: $\vec{r}(t)$ - location at time t
- Displacement: $\Delta \vec{r} = \vec{r}_f - \vec{r}_i$ - change in position (vector)
- Distance: scalar quantity, always positive

**Velocity:**
- Average velocity: $\vec{v}_{avg} = \frac{\Delta \vec{r}}{\Delta t}$
- Instantaneous velocity: $\vec{v}(t) = \frac{d\vec{r}}{dt}$ - rate of change of position
- Speed: $v = |\vec{v}|$ - magnitude of velocity

**Acceleration:**
- Average acceleration: $\vec{a}_{avg} = \frac{\Delta \vec{v}}{\Delta t}$
- Instantaneous acceleration: $\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$ - rate of change of velocity

**Key relationships:**
$$\vec{v} = \int \vec{a} \, dt$$
$$\vec{r} = \int \vec{v} \, dt$$

### 2.2 Kinematic Equations (SUVAT)
For motion with constant acceleration:

**s = ut + ½at²** (displacement without final velocity)
- $s$ = displacement
- $u$ = initial velocity
- $a$ = acceleration
- $t$ = time

**v = u + at** (velocity without displacement)

**v² = u² + 2as** (velocity without time)

**s = (u+v)t/2** (displacement without acceleration)

**s = vt - ½at²** (displacement from final velocity)

Where:
- $s$ or $x$ = displacement (m)
- $u$ = initial velocity (m/s)
- $v$ = final velocity (m/s)
- $a$ = acceleration (m/s²)
- $t$ = time (s)

### 2.3 Vector Methods

**Vector Addition:**
$$\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} + (A_z + B_z)\hat{k}$$

**Magnitude:**
$$|\vec{A}| = \sqrt{A_x^2 + A_y^2 + A_z^2}$$

**Dot Product (scalar product):**
$$\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta = A_x B_x + A_y B_y + A_z B_z$$

**Cross Product (vector product):**
$$\vec{A} \times \vec{B} = |\vec{A}||\vec{B}|\sin\theta \, \hat{n}$$

$$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$$

Properties:
- Dot product is commutative: $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$
- Cross product is anti-commutative: $\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$
- $\vec{A} \times \vec{B}$ is perpendicular to both $\vec{A}$ and $\vec{B}$

### 2.4 Relative Motion
When object A moves with velocity $\vec{v}_A$ and object B with velocity $\vec{v}_B$:

**Velocity of A relative to B:**
$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

**Displacement of A relative to B:**
$$\vec{r}_{AB} = \vec{r}_A - \vec{r}_B$$

### 2.5 Projectile Motion
An object thrown in the air with initial velocity $\vec{v}_0$ under gravity alone (ignoring air resistance).

**Initial conditions:**
- $v_{0x} = v_0 \cos\theta$
- $v_{0y} = v_0 \sin\theta$
- Acceleration: $\vec{a} = (0, -g, 0)$ in 2D

**Equations of motion (taking origin at launch point):**

$$x(t) = v_0 \cos\theta \cdot t$$

$$y(t) = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2$$

$$v_x(t) = v_0 \cos\theta$$

$$v_y(t) = v_0 \sin\theta - gt$$

**Time of flight** (when $y = 0$):
$$T = \frac{2v_0 \sin\theta}{g}$$

**Maximum height** (when $v_y = 0$):
$$H = \frac{v_0^2 \sin^2\theta}{2g}$$

**Range** (horizontal distance):
$$R = \frac{v_0^2 \sin(2\theta)}{g}$$

Maximum range occurs at $\theta = 45°$:
$$R_{max} = \frac{v_0^2}{g}$$

**Trajectory equation** (eliminating t):
$$y = x\tan\theta - \frac{gx^2}{2v_0^2\cos^2\theta}$$

### 2.6 Circular Motion (Kinematics)

**Angular displacement:** $\theta$ (radians)

**Angular velocity:** $\omega = \frac{d\theta}{dt}$ (rad/s)

**Angular acceleration:** $\alpha = \frac{d\omega}{dt}$ (rad/s²)

**Relationships with linear quantities:**
$$v = r\omega$$ (tangential velocity)

$$a_{tangential} = r\alpha$$

$$a_{centripetal} = \frac{v^2}{r} = r\omega^2$$

Total acceleration: $\vec{a} = \vec{a}_t + \vec{a}_c$

**Equations for constant angular acceleration:**
$$\omega = \omega_0 + \alpha t$$

$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$$

$$\omega^2 = \omega_0^2 + 2\alpha\theta$$

### 2.7 Graphs of Motion

**Position-time graph:**
- Slope = velocity
- Curved if accelerating

**Velocity-time graph:**
- Slope = acceleration
- Area under curve = displacement

**Acceleration-time graph:**
- Area under curve = change in velocity

## Key Equations (Summary)

$$v = u + at$$
$$s = ut + \frac{1}{2}at^2$$
$$v^2 = u^2 + 2as$$
$$s = \frac{u+v}{2}t$$

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

$$R = \frac{v_0^2 \sin(2\theta)}{g}$$
$$H = \frac{v_0^2 \sin^2\theta}{2g}$$
$$T = \frac{2v_0 \sin\theta}{g}$$

$$v = r\omega$$
$$a_c = r\omega^2 = \frac{v^2}{r}$$

## Reference Books

1. **NCERT Physics Part 1** — Chapter 3-4: Clear introduction with graphs
2. **H.C. Verma, Concepts of Physics Vol 1** — Chapter 2-3: Excellent problem collection
3. **Halliday, Resnick & Walker** — Chapter 2-4: Comprehensive with examples
4. **Irodov, Problems in General Physics** — Section 1.1: Challenging kinematics problems
5. **Kleppner & Kolenkow, "An Introduction to Mechanics"** — Chapter 1-2: Rigorous treatment

## Historical Context

**Galileo Galilei (1564-1642)** developed the first complete theory of projectile motion through careful observation and experimentation. He showed that:
- Horizontal and vertical motions are independent
- The trajectory is a parabola
- Time of flight depends only on vertical component of initial velocity
- Range is maximum at 45° (proven later with calculus)

His work laid the foundation for all subsequent kinematics.

## Learning Outcomes

By the end of this topic, you should be able to:
- [ ] Use and interpret displacement, velocity, and acceleration
- [ ] Apply SUVAT equations to solve motion problems
- [ ] Work with vectors and perform vector operations
- [ ] Analyze relative motion between objects
- [ ] Solve projectile motion problems in 2D
- [ ] Understand and apply circular motion kinematics
- [ ] Interpret and create motion graphs
- [ ] Solve complex motion problems using calculus integration

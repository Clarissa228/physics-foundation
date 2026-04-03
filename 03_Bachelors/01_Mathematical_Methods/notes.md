# Mathematical Methods for Physics

## Overview
Mathematical Methods are the **language of physics**. This topic covers the essential mathematical frameworks used throughout all advanced physics courses. Mastery of these tools is non-negotiable for understanding modern physics.

---

## 1. Vector Calculus

### Fundamental Operations

**Gradient** (scalar → vector field):
$$\nabla f = \frac{\partial f}{\partial x}\hat{x} + \frac{\partial f}{\partial y}\hat{y} + \frac{\partial f}{\partial z}\hat{z}$$

Points in direction of maximum increase; perpendicular to level surfaces.

**Divergence** (vector field → scalar):
$$\nabla \cdot \vec{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$

Measures "spreading out" of a vector field; represents source/sink density.

**Curl** (vector field → vector field):
$$\nabla \times \vec{F} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z \end{vmatrix}$$

Measures "swirling" of a vector field; rotation at each point.

**Laplacian** (scalar → scalar):
$$\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

Appears in heat equation, wave equation, Schrödinger equation.

### Vector Identities (Critical for Physics)

- **∇ × (∇f) = 0** — Curl of gradient is always zero (gradient fields are irrotational)
- **∇ · (∇ × F) = 0** — Divergence of curl is always zero
- **∇ × (∇ × F) = ∇(∇ · F) - ∇²F** — Product rule for curl

### Theorems

**Divergence Theorem**:
$$\int_V (\nabla \cdot \vec{F}) \, d^3r = \oint_S \vec{F} \cdot d\vec{A}$$

Volume integral of divergence equals surface flux.

**Stokes' Theorem**:
$$\oint_C \vec{F} \cdot d\vec{l} = \int_S (\nabla \times \vec{F}) \cdot d\vec{A}$$

Line integral around closed curve equals surface integral of curl.

---

## 2. Curvilinear Coordinates

### Cylindrical Coordinates (ρ, φ, z)

Used for: problems with cylindrical symmetry (wires, coaxial cables, magnetic fields around wires)

$$x = \rho \cos\phi, \quad y = \rho \sin\phi, \quad z = z$$

$$\nabla f = \frac{\partial f}{\partial \rho}\hat{\rho} + \frac{1}{\rho}\frac{\partial f}{\partial \phi}\hat{\phi} + \frac{\partial f}{\partial z}\hat{z}$$

$$\nabla^2 f = \frac{1}{\rho}\frac{\partial}{\partial \rho}\left(\rho\frac{\partial f}{\partial \rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 f}{\partial \phi^2} + \frac{\partial^2 f}{\partial z^2}$$

### Spherical Coordinates (r, θ, φ)

Used for: central force problems, atomic physics (hydrogen atom), electrostatics of spheres

$$x = r\sin\theta\cos\phi, \quad y = r\sin\theta\sin\phi, \quad z = r\cos\theta$$

$$\nabla f = \frac{\partial f}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{\theta} + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi}\hat{\phi}$$

$$\nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial f}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial f}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 f}{\partial \phi^2}$$

---

## 3. Linear Algebra for Physics

### Eigenvalue Problems

For matrix $A$: $A\vec{v} = \lambda\vec{v}$

- Eigenvalues λ: physical observables (energy levels, frequencies, principal moments of inertia)
- Eigenvectors: states associated with those observables
- **Key insight**: In quantum mechanics, observables are Hermitian matrices; eigenvalues are real, eigenvectors orthogonal

### Diagonalization

If $A$ has eigenvalues λ₁, λ₂, ... and eigenvectors form basis, then:
$$A = PDP^{-1}$$
where $D$ is diagonal matrix of eigenvalues.

Physics application: Normal modes decouple in this basis.

### Orthogonal Transformations

Rotation matrices preserve length: $R^T R = I$

Used in: classical mechanics (coordinate transformations), quantum mechanics (basis changes), solid state physics (crystal lattices).

---

## 4. Differential Equations

### Ordinary Differential Equations (ODEs)

**Second-order linear ODE**:
$$\frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = f(x)$$

Solutions for homogeneous (f=0):
- **Characteristic equation** method for constant coefficients
- **Frobenius method** near singular points (quantum mechanics)

Physics examples:
- Damped harmonic oscillator: $m\ddot{x} + \gamma\dot{x} + kx = 0$
- Schrödinger equation (time-independent): Sturm-Liouville problem

### Partial Differential Equations (PDEs)

**Wave Equation**:
$$\frac{\partial^2 u}{\partial t^2} = v^2\nabla^2 u$$

Solution technique: **Separation of Variables** — assume $u(x,t) = X(x)T(t)$

**Heat (Diffusion) Equation**:
$$\frac{\partial u}{\partial t} = \alpha\nabla^2 u$$

### Separation of Variables

1. Assume solution factorizes: $u(x,t) = X(x)T(t)$
2. Split into ODEs for $X$ and $T$
3. Boundary conditions → quantization (discrete eigenvalues)
4. General solution: sum over all modes

**Example**: Standing waves on a string have quantized frequencies $\omega_n = n\pi v/L$.

---

## 5. Fourier Analysis

### Fourier Series

For periodic function $f(x)$ with period $2L$:
$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n\cos(n\pi x/L) + b_n\sin(n\pi x/L)]$$

$$a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos(n\pi x/L)\,dx$$

$$b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin(n\pi x/L)\,dx$$

**Gibbs phenomenon**: At discontinuities, Fourier series overshoots by ~9% even as N→∞.

**Physics applications**:
- Analyzing vibrations: decompose displacement into normal modes
- Signal processing: frequency components of electromagnetic waves
- Quantum mechanics: energy eigenstates as basis

### Fourier Transform

For non-periodic functions:
$$\hat{f}(k) = \int_{-\infty}^{\infty} f(x)e^{-ikx}\,dx$$

$$f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{f}(k)e^{ikx}\,dk$$

Convolution theorem: $\mathcal{F}[f*g] = \mathcal{F}[f]\cdot\mathcal{F}[g]$ (critical for signal processing, diffraction)

---

## 6. Complex Analysis

### Analytic Functions

Function $f(z)$ is analytic if it satisfies Cauchy-Riemann equations:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
(where $f(z) = u(x,y) + iv(x,y)$)

### Contour Integration

**Cauchy Integral Formula**:
$$f(a) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{z-a}\,dz$$

Incredible power: can evaluate real integrals using complex analysis!

### Residue Theorem

$$\oint_C f(z)\,dz = 2\pi i \sum \text{(residues at poles inside C)}$$

**Physics applications**:
- Evaluating integrals in quantum field theory
- Response functions in condensed matter physics
- Wave scattering problems

---

## 7. Special Functions

### Legendre Polynomials $P_n(x)$

Orthogonal on $[-1,1]$ with weight 1.

$$P_0(x) = 1, \quad P_1(x) = x, \quad P_2(x) = \frac{1}{2}(3x^2-1), \quad P_3(x) = \frac{1}{2}(5x^3-3x)$$

**Rodrigues formula**:
$$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$$

**Physics use**: Multipole expansion in electrostatics; angular dependence in central force problems.

### Spherical Harmonics $Y_{\ell}^m(\theta,\phi)$

Eigenfunctions of Laplacian on sphere; orthonormal basis on sphere.

$$Y_{\ell}^m(\theta,\phi) = (-1)^m\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}P_{\ell}^{|m|}(\cos\theta)e^{im\phi}$$

where $P_{\ell}^{m}$ are associated Legendre polynomials.

**Physics use**: Angular parts of hydrogen atom wavefunctions; expansion of fields on sphere.

### Bessel Functions $J_n(x)$, $Y_n(x)$

Appear when solving Laplace/Helmholtz in cylindrical coordinates.

Orthogonality: $\int_0^R J_n(j_{n,k}r/R)J_n(j_{n,\ell}r/R)r\,dr = 0$ for $k \neq \ell$

**Physics use**: Vibrating drum, electromagnetic waveguides, quantum mechanical scattering.

### Hermite Polynomials $H_n(x)$

Orthogonal with Gaussian weight: $\int_{-\infty}^{\infty} e^{-x^2}H_n(x)H_m(x)\,dx = 2^n n!\sqrt{\pi}\delta_{nm}$

$$H_0(x) = 1, \quad H_1(x) = 2x, \quad H_2(x) = 4x^2-2, \quad H_3(x) = 8x^3-12x$$

**Physics use**: Quantum harmonic oscillator wavefunctions: $\psi_n(x) \propto e^{-x^2/2a^2}H_n(x/a)$

---

## 8. Tensor Analysis

### Index Notation

Replace components: Instead of $\vec{A} = A_x\hat{x} + A_y\hat{y} + A_z\hat{z}$, write $A_i$ (implicitly summed when index repeats).

**Tensor**: object with multiple indices transforming as: $T'_{ij} = R_{ia}R_{jb}T_{ab}$

### Einstein Summation Convention

Repeated indices are summed:
$$A_i B_i \equiv \sum_{i=1}^{3} A_i B_i = \vec{A} \cdot \vec{B}$$

$$T_{ij}v_j \equiv \sum_{j} T_{ij}v_j = \text{matrix-vector product}$$

### Metric Tensor

In Cartesian: $g_{ij} = \delta_{ij}$ (simple!)

In curvilinear: $g_{ij} = \frac{\partial \vec{r}}{\partial q_i} \cdot \frac{\partial \vec{r}}{\partial q_j}$ (general Riemannian geometry)

**Physics use**: General relativity (spacetime metric), mechanics in arbitrary coordinates, electromagnetism in covariant form.

---

## Key References

### Essential Books
1. **Arfken, Weber & Harris**, "Mathematical Methods for Physicists" (7th ed.) — THE comprehensive reference
2. **Boas**, "Mathematical Methods in the Physical Sciences" (3rd ed.) — excellent practical guide
3. **Riley, Hobson & Bence**, "Mathematical Methods for Physics and Engineering" — thorough with problems

### Landmark Papers
- **Fourier (1822)**: "Théorie analytique de la chaleur" — introduced Fourier series; revolutionized physics
- **Legendre (1782-1823)**: Papers on orthogonal polynomials and elliptic integrals
- **Bessel (1824)**: On cylindrical coordinates and their characteristic functions
- **Riemann (1854)**: "Ueber die Hypothesen, welche der Geometrie zu Grunde liegen" — laid foundation for differential geometry

### Modern Applications
- **Mesh generation & numerical PDEs**: Finite element methods rely heavily on curvilinear coordinates
- **Machine learning in physics**: Neural networks must learn symmetries; tensor notation essential
- **Quantum computing**: Hilbert space is function space; eigenvectors are basis states

---

## Study Roadmap

1. **Master vector calculus first** — it's the foundation
2. **Practice coordinate transforms** — until they feel natural
3. **Solve boundary value problems** — use separation of variables, understand eigenvalue problems
4. **Learn special functions** — recognize them when they appear in physics
5. **Apply to real physics**: Maxwell's equations, Schrödinger equation, general relativity

**This is not memorization — it's developing mathematical intuition!**

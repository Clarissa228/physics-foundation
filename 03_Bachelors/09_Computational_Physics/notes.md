# Computational Physics: Solving Real Problems Numerically

## Overview
Physics problems often don't have closed-form solutions. Numerical methods bridge theory and experiment: ODEs, PDEs, Monte Carlo, molecular dynamics, machine learning.

---

## 1. Numerical Differentiation and Integration

**Finite differences**: 
$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$ (error ~ h²)

**Integration methods**:
- **Rectangle rule**: L(f) = h·∑f(xᵢ) (error ~ h)
- **Trapezoid rule**: T(f) = (h/2)·[f₀ + 2∑fᵢ + fₙ] (error ~ h²)
- **Simpson's rule**: S(f) = (h/3)·[f₀ + 4∑fodd + 2∑feven + fₙ] (error ~ h⁴)

---

## 2. ODE Solvers

**Euler method**: $y_{n+1} = y_n + h f(x_n, y_n)$ (error ~ h)

**Runge-Kutta-4** (RK4): 
$$k_1 = h f(x_n, y_n)$$
$$k_2 = h f(x_n + h/2, y_n + k_1/2)$$
$$k_3 = h f(x_n + h/2, y_n + k_2/2)$$
$$k_4 = h f(x_n + h, y_n + k_3)$$
$$y_{n+1} = y_n + (k_1 + 2k_2 + 2k_3 + k_4)/6$$

Error ~ h⁴ (4th order), most popular choice.

**Adaptive stepsize**: Adjust h to maintain error tolerance.

---

## 3. PDE Solvers

**Finite difference method**: Replace ∂ with (f(x+h) - f(x))/h

**Heat equation** (parabolic): Explicit or implicit (Crank-Nicolson) schemes

**Wave equation** (hyperbolic): Explicit scheme (must satisfy CFL: v·Δt < Δx)

**Laplace/Poisson** (elliptic): Iterative solvers (Gauss-Seidel, SOR)

---

## 4. Root Finding

**Newton-Raphson**: $x_{n+1} = x_n - f(x_n)/f'(x_n)$ (quadratic convergence)

**Bisection**: Bracket root, repeatedly halve interval (slow but robust)

---

## 5. Monte Carlo Methods

**Random sampling**: Estimate integrals by sampling random points.

$$\int_a^b f(x) dx \approx \frac{b-a}{N} \sum_{i=1}^N f(x_i)$$

**Monte Carlo integration**: Error ~ 1/√N (independent of dimension! Unlike deterministic rules)

**Importance sampling**: Weight samples by probability to reduce variance.

---

## 6. Metropolis Algorithm

**Markov chain**: Generate configuration sequence where probability ∝ exp(-E/kT)

**Acceptance ratio**: 
$$A = \min(1, e^{-\Delta E/k_B T})$$

Accept move with probability A, else reject.

**Applications**: Ising model phase transitions, molecular conformations.

---

## 7. Molecular Dynamics

**Simulate N particles** under Lennard-Jones or Coulomb potential.

**Verlet algorithm**: 
$$r(t+Δt) = 2r(t) - r(t-Δt) + a(t)Δt^2$$

Conserves energy and momentum automatically.

**Outputs**: Pressure, temperature, diffusion coefficient, radial distribution.

---

## 8. Fast Fourier Transform (FFT)

**Compute** ∑ e^{2πikj/N} efficiently: O(N log N) instead of O(N²)

**Applications**:
- Signal processing: filter, analyze spectrum
- Solving PDEs: Fourier space simpler than real space
- Convolution theorem: f*g → F·G in Fourier space

---

## 9. Machine Learning in Physics

**Neural networks**: Learn from data to approximate functions.

**Physics-informed neural networks (PINNs)**: Embed PDE into loss function.

**Deep learning** discovers conservation laws from data.

---

## Key References

**Essential Books**:
1. **Newman**, "Computational Physics" (2nd ed.) — excellent, code-first
2. **Press et al.**, "Numerical Recipes" (3rd ed.) — reference for algorithms
3. **Landau, Páez & Bordeianu**, "Computational Physics" (Python)

**Landmark Papers**:
- Metropolis et al. (1953): Monte Carlo method
- Verlet (1967): MD algorithm
- Cooley & Tukey (1965): FFT

**Applications**:
- Climate modeling
- Protein folding
- Electronic structure calculations
- Fluid dynamics simulations

---

## Study Roadmap

1. Master RK4 ODE solver
2. Learn finite difference PDE methods
3. Implement Monte Carlo integration
4. Try molecular dynamics simulation
5. Apply FFT to real problems

**Bridges mathematical physics and computer science!**

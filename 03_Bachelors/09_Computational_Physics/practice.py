"""Computational Physics Practice Exercises"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import fsolve

def exercise_1_rk4_ode_solver():
    """Implement RK4 and solve pendulum ODE"""
    print("="*70)
    print("EXERCISE 1: Runge-Kutta-4 ODE Solver")
    print("="*70)
    
    def rk4_step(f, y, t, h):
        """Single RK4 step"""
        k1 = f(y, t)
        k2 = f(y + 0.5*h*k1, t + 0.5*h)
        k3 = f(y + 0.5*h*k2, t + 0.5*h)
        k4 = f(y + h*k3, t + h)
        return y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    
    def pendulum(y, t):
        theta, omega = y
        return [omega, -np.sin(theta)]  # g/L = 1
    
    # Solve pendulum
    t = np.linspace(0, 20, 1000)
    y0 = [1.5, 0]  # Initial: θ=1.5 rad, ω=0
    
    y_rk4 = [y0]
    for i in range(len(t)-1):
        h = t[i+1] - t[i]
        y_rk4.append(rk4_step(pendulum, y_rk4[-1], t[i], h))
    y_rk4 = np.array(y_rk4)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    ax1.plot(t, y_rk4[:, 0], 'b-', linewidth=2, label='θ(t) - RK4')
    ax1.set_xlabel('Time', fontsize=11)
    ax1.set_ylabel('Angle θ', fontsize=11)
    ax1.set_title('Nonlinear Pendulum: RK4 Solution', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    
    ax2.plot(y_rk4[:, 0], y_rk4[:, 1], 'b-', linewidth=1.5, alpha=0.7)
    ax2.plot(y0[0], y0[1], 'go', markersize=10, label='Start')
    ax2.set_xlabel('θ', fontsize=11)
    ax2.set_ylabel('ω', fontsize=11)
    ax2.set_title('Phase Space', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/tmp/rk4_solver.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"RK4 solver implemented and tested on nonlinear pendulum")

def exercise_2_monte_carlo_integration():
    """Monte Carlo integration to estimate π"""
    print("\n" + "="*70)
    print("EXERCISE 2: Monte Carlo Integration")
    print("="*70)
    
    # Estimate π by random sampling in unit square
    # Area of unit circle = π/4, so π ≈ 4 * (points in circle / total points)
    
    N_vals = np.logspace(2, 6, 20, dtype=int)
    pi_estimates = []
    errors = []
    
    np.random.seed(42)
    for N in N_vals:
        x = np.random.uniform(0, 1, N)
        y = np.random.uniform(0, 1, N)
        r = np.sqrt(x**2 + y**2)
        inside = np.sum(r <= 1)
        pi_est = 4 * inside / N
        pi_estimates.append(pi_est)
        errors.append(abs(pi_est - np.pi))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    ax1.loglog(N_vals, errors, 'b-o', linewidth=2, markersize=6)
    ax1.loglog(N_vals, 1/np.sqrt(N_vals), 'r--', linewidth=2, label='1/√N')
    ax1.set_xlabel('Number of samples N', fontsize=11)
    ax1.set_ylabel('Error |π_est - π|', fontsize=11)
    ax1.set_title('Monte Carlo Integration Error', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, which='both')
    
    ax2.semilogx(N_vals, pi_estimates, 'b-o', linewidth=2, markersize=6, label='Estimate')
    ax2.axhline(y=np.pi, color='red', linestyle='--', linewidth=2, label='True π')
    ax2.fill_between(N_vals, np.pi-0.1, np.pi+0.1, alpha=0.2, color='red')
    ax2.set_xlabel('Number of samples N', fontsize=11)
    ax2.set_ylabel('Estimated π', fontsize=11)
    ax2.set_title('π Estimation Convergence', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/monte_carlo_pi.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nMonte Carlo π estimation:")
    print(f"N = {N_vals[-1]}: π ≈ {pi_estimates[-1]:.6f} (error = {errors[-1]:.6f})")
    print(f"Error scales as 1/√N (sqrt of sample size)")

def exercise_3_finite_difference_pde():
    """Finite difference method for heat equation"""
    print("\n" + "="*70)
    print("EXERCISE 3: Finite Difference for Heat Equation")
    print("=\"*70)
    
    # Heat equation: ∂u/∂t = α ∂²u/∂x²
    # Solve with initial condition: Gaussian pulse
    
    nx, nt = 100, 50
    L = 1.0
    alpha = 0.01
    
    x = np.linspace(0, L, nx)
    dx = L / (nx - 1)
    dt = 0.001
    r = alpha * dt / dx**2  # CFL number
    
    # Initial condition: Gaussian
    u = np.exp(-100*(x - 0.3)**2)
    u_solution = [u.copy()]
    
    # Finite difference evolution (implicit Crank-Nicolson would be better)
    for n in range(nt):
        u_new = u.copy()
        for i in range(1, nx-1):
            u_new[i] = u[i] + r*(u[i+1] - 2*u[i] + u[i-1])
        u = u_new
        u_solution.append(u.copy())
    
    u_solution = np.array(u_solution)
    
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    
    # Solution over time
    ax = axes[0]
    t_plot = np.linspace(0, nt*dt, nt+1)
    contour = ax.contourf(x, t_plot, u_solution, levels=20, cmap='hot')
    ax.set_xlabel('Position x', fontsize=11)
    ax.set_ylabel('Time t', fontsize=11)
    ax.set_title('Heat Equation Solution: Diffusion', fontsize=12, fontweight='bold')
    cbar = plt.colorbar(contour, ax=ax)
    cbar.set_label('Temperature', fontsize=10)
    
    # Snapshots
    ax = axes[1]
    for i in [0, 10, 20, 30, nt]:
        ax.plot(x, u_solution[i], linewidth=2, label=f't={i*dt:.3f}')
    ax.set_xlabel('Position x', fontsize=11)
    ax.set_ylabel('Temperature', fontsize=11)
    ax.set_title('Temperature Snapshots at Different Times', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/heat_equation.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Heat equation solved using finite differences")
    print(f"Grid: {nx} spatial points, {nt} time steps")
    print(f"CFL number r = α·dt/dx² = {r:.4f} < 0.5 (stable)")

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("COMPUTATIONAL PHYSICS: PRACTICE EXERCISES")
    print("#"*70 + "\n")
    
    exercise_1_rk4_ode_solver()
    exercise_2_monte_carlo_integration()
    exercise_3_finite_difference_pde()
    
    print("\n" + "#"*70)
    print("ALL EXERCISES COMPLETED!")
    print("#"*70 + "\n")

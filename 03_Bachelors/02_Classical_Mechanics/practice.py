"""
Classical Mechanics: Practice Exercises

Topics:
- Lagrangian and Hamiltonian mechanics
- Normal modes and coupled oscillations
- Chaos and Lyapunov exponents
- Conservation laws
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
from scipy.linalg import eig
import sympy as sp

def exercise_1_lagrangian_pendulum():
    """Derive equations of motion from Lagrangian for a driven pendulum"""
    print("="*70)
    print("EXERCISE 1: Lagrangian Mechanics - Driven Pendulum")
    print("="*70)

    # Solve numerically: d²θ/dt² + (g/L)sin(θ) = (F₀/mL)cos(ωt)
    m, L, g = 1.0, 1.0, 9.8
    F0, omega_d = 0.5, 2.0

    def driven_pendulum(y, t):
        theta, omega = y
        a = -(g/L)*np.sin(theta) + (F0/(m*L))*np.cos(omega_d*t)
        return [omega, a]

    t = np.linspace(0, 30, 2000)
    sol = odeint(driven_pendulum, [0.3, 0], t)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    ax = axes[0]
    ax.plot(t, sol[:, 0], 'b-', linewidth=1.5)
    ax.set_xlabel('Time (s)', fontsize=11)
    ax.set_ylabel('θ (rad)', fontsize=11)
    ax.set_title('Driven Pendulum: Time Evolution', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Steady-state phase space
    steady_state_idx = int(len(t) * 2/3)\n    ax = axes[1]\n    ax.plot(sol[steady_state_idx:, 0], sol[steady_state_idx:, 1], 'b-', linewidth=1, alpha=0.7)\n    ax.set_xlabel('θ (rad)', fontsize=11)\n    ax.set_ylabel('dθ/dt (rad/s)', fontsize=11)\n    ax.set_title('Phase Space: Steady State', fontsize=12, fontweight='bold')\n    ax.grid(True, alpha=0.3)\n    \n    plt.tight_layout()\n    plt.savefig('/tmp/driven_pendulum.png', dpi=150, bbox_inches='tight')\n    plt.show()\n    \n    print(f\"\\nDriven pendulum with F₀ = {F0}, ω_d = {omega_d}\")\n    print(f\"Equation: θ'' + (g/L)sin(θ) = (F₀/mL)cos(ω_d*t)\")\n    print(f\"\\nSolution computed and plotted.\")\n    print()\n\ndef exercise_2_normal_modes():\n    \"\"\"Find and analyze normal modes of 3 coupled oscillators\"\"\"\n    print(\"=\"*70)\n    print(\"EXERCISE 2: Normal Modes - 3 Coupled Oscillators\")\n    print(\"=\"*70)\n    \n    # Stiffness matrix for 3 masses in a row\n    K = np.array([\n        [2, -1, 0],\n        [-1, 2, -1],\n        [0, -1, 2]\n    ])\n    M = np.eye(3)\n    \n    # Eigenvalues and eigenvectors\n    A = np.linalg.inv(M) @ K\n    evals, evecs = np.linalg.eig(A)\n    \n    # Sort\n    idx = np.argsort(evals)\n    evals = evals[idx]\n    evecs = evecs[:, idx]\n    omega = np.sqrt(evals)\n    \n    print(f\"\\nEigenvalues (ω²): {evals}\")\n    print(f\"Natural frequencies (ω): {omega}\")\n    print(f\"\\nNormal modes:\")\n    for i in range(3):\n        print(f\"  Mode {i+1}: {evecs[:, i]} with ω_{i+1} = {omega[i]:.4f}\")\n    \n    # Visualize modes\n    fig, axes = plt.subplots(1, 3, figsize=(14, 4))\n    \n    for i in range(3):\n        ax = axes[i]\n        mode = evecs[:, i]\n        x_positions = [0, 1, 2]\n        colors = ['red' if m < 0 else 'blue' for m in mode]\n        ax.bar(x_positions, np.abs(mode), color=colors, alpha=0.7, edgecolor='black')\n        ax.set_ylim(0, 1.2 * np.max(np.abs(mode)))\n        ax.set_ylabel('Mode amplitude', fontsize=11)\n        ax.set_xticks(x_positions)\n        ax.set_xticklabels(['m₁', 'm₂', 'm₃'])\n        ax.set_title(f'Mode {i+1}: ω = {omega[i]:.3f}', fontsize=12, fontweight='bold')\n        ax.grid(True, alpha=0.3, axis='y')\n    \n    plt.tight_layout()\n    plt.savefig('/tmp/three_mode_analysis.png', dpi=150, bbox_inches='tight')\n    plt.show()\n    \n    print(f\"\\nModes visualized and saved.\")\n    print()\n\ndef exercise_3_chaos_lyapunov():\n    \"\"\"Demonstrate sensitivity to initial conditions and compute Lyapunov exponent\"\"\"\n    print(\"=\"*70)\n    print(\"EXERCISE 3: Chaos and Lyapunov Exponents\")\n    print(\"=\"*70)\n    \n    # Hénon map: a simple 2D chaotic map\n    def henon_map(x, y, a=1.4, b=0.3):\n        x_new = 1 - a*x**2 + y\n        y_new = b*x\n        return x_new, y_new\n    \n    # Initial condition\n    x0, y0 = 0.0, 0.0\n    \n    # Two nearby initial conditions\n    eps = 1e-6\n    x1, y1 = x0, y0\n    x2, y2 = x0 + eps, y0\n    \n    n_iter = 1000\n    traj1, traj2 = [], []\n    divergences = []\n    \n    for _ in range(n_iter):\n        x1, y1 = henon_map(x1, y1)\n        x2, y2 = henon_map(x2, y2)\n        traj1.append([x1, y1])\n        traj2.append([x2, y2])\n        div = np.sqrt((x2-x1)**2 + (y2-y1)**2)\n        divergences.append(div)\n    \n    traj1 = np.array(traj1)\n    traj2 = np.array(traj2)\n    divergences = np.array(divergences)\n    \n    # Compute Lyapunov exponent\n    lyapunov = np.log(divergences[100:] / eps) / np.arange(1, len(divergences)-100+1)\n    \n    # Create figure\n    fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n    \n    # Attractor\n    ax = axes[0]\n    ax.plot(traj1[:, 0], traj1[:, 1], 'b,', markersize=0.5, alpha=0.5)\n    ax.set_xlabel('x', fontsize=11)\n    ax.set_ylabel('y', fontsize=11)\n    ax.set_title('Hénon Attractor: Strange Attractor', fontsize=12, fontweight='bold')\n    ax.grid(True, alpha=0.3)\n    \n    # Lyapunov exponent\n    ax = axes[1]\n    ax.plot(np.arange(1, len(lyapunov)+1), lyapunov, 'purple', linewidth=2)\n    ax.axhline(y=np.mean(lyapunov[-200:]), color='red', linestyle='--', linewidth=2)\n    ax.set_xlabel('Iteration', fontsize=11)\n    ax.set_ylabel('Lyapunov exponent', fontsize=11)\n    ax.set_title('Convergence to Mean Lyapunov Exponent', fontsize=12, fontweight='bold')\n    ax.grid(True, alpha=0.3)\n    ax.text(500, np.mean(lyapunov[-200:]) + 0.02, \n           f\"λ ≈ {np.mean(lyapunov[-200:]):.3f}\", fontsize=11,\n           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))\n    \n    plt.tight_layout()\n    plt.savefig('/tmp/henon_chaos.png', dpi=150, bbox_inches='tight')\n    plt.show()\n    \n    print(f\"\\nHénon map: x_{n+1} = 1 - ax_n² + y_n, y_{n+1} = bx_n\")\n    print(f\"\\nInitial separation: ε = {eps:.2e}\")\n    print(f\"Final separation: {divergences[-1]:.2f}\")\n    print(f\"Magnification: {divergences[-1]/eps:.2e}\")\n    print(f\"\\nLyapunov exponent: λ ≈ {np.mean(lyapunov[-200:]):.4f}\")\n    print(f\"λ > 0 indicates CHAOS\")\n    print()\n\ndef exercise_4_conservation_laws():\n    \"\"\"Verify energy and momentum conservation\"\"\"\n    print(\"=\"*70)\n    print(\"EXERCISE 4: Conservation Laws in Hamiltonian Dynamics\")\n    print(\"=\"*70)\n    \n    # Simple harmonic oscillator\n    def sho(y, t):\n        x, p = y\n        return [p, -x]  # H = p²/2 + x²/2\n    \n    y0 = [1.0, 0.5]\n    t = np.linspace(0, 20, 1000)\n    sol = odeint(sho, y0, t)\n    \n    # Compute energy at each step\n    x = sol[:, 0]\n    p = sol[:, 1]\n    E = 0.5 * p**2 + 0.5 * x**2\n    \n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))\n    \n    ax = ax1\n    ax.plot(t, E, 'b-', linewidth=2)\n    ax.set_xlabel('Time', fontsize=11)\n    ax.set_ylabel('Total Energy E', fontsize=11)\n    ax.set_title('Energy Conservation', fontsize=12, fontweight='bold')\n    ax.grid(True, alpha=0.3)\n    \n    # Relative energy error\n    E_error = np.abs(E - E[0]) / E[0]\n    ax = ax2\n    ax.semilogy(t, E_error, 'r-', linewidth=2)\n    ax.set_xlabel('Time', fontsize=11)\n    ax.set_ylabel('Relative energy error', fontsize=11)\n    ax.set_title('Numerical Integration Error', fontsize=12, fontweight='bold')\n    ax.grid(True, alpha=0.3, which='both')\n    \n    plt.tight_layout()\n    plt.savefig('/tmp/energy_conservation.png', dpi=150, bbox_inches='tight')\n    plt.show()\n    \n    print(f\"\\nEnergy conservation in simple harmonic oscillator\")\n    print(f\"Initial energy: E₀ = {E[0]:.6f}\")\n    print(f\"Final energy: E_f = {E[-1]:.6f}\")\n    print(f\"Relative error: {E_error[-1]:.2e}\")\n    print(f\"\\nEnergy is conserved (errors due to numerical integration)\")\n    print()\n\nif __name__ == \"__main__\":\n    print(\"\\n\" + \"#\"*70)\n    print(\"CLASSICAL MECHANICS: PRACTICE EXERCISES\")\n    print(\"#\"*70 + \"\\n\")\n    \n    exercise_1_lagrangian_pendulum()\n    exercise_2_normal_modes()\n    exercise_3_chaos_lyapunov()\n    exercise_4_conservation_laws()\n    \n    print(\"#\"*70)\n    print(\"ALL EXERCISES COMPLETED!\")\n    print(\"#\"*70 + \"\\n\")\n
"""
Topic 9: Kinetic Theory of Gases - Practice Exercises
"""

import numpy as np

k_B = 1.381e-23
N_A = 6.022e23
R = 8.314

def exercise_1():
    M_N2 = 28e-3
    temps = [273, 300, 500]
    print("Exercise 1: RMS Speed of N2\n")
    print(f"{'Temp (K)':<15} {'v_rms (m/s)':<20}")
    for T in temps:
        v_rms = np.sqrt(3 * R * T / M_N2)
        print(f"{T:<15} {v_rms:<20.1f}")
    print()

def exercise_2():
    M_O2 = 32e-3
    v_rms = 500
    T = M_O2 * v_rms**2 / (3 * R)
    print(f"Exercise 2: Temperature from v_rms = {v_rms} m/s")
    print(f"T = {T:.1f} K\n")

def exercise_3():
    M_CO2 = 44e-3
    T = 300
    v_mp = np.sqrt(2 * R * T / M_CO2)
    v_avg = np.sqrt(8 * R * T / (np.pi * M_CO2))
    v_rms = np.sqrt(3 * R * T / M_CO2)
    print(f"Exercise 3: Characteristic Speeds (CO2 at {T}K)")
    print(f"v_mp = {v_mp:.1f} m/s")
    print(f"v_avg = {v_avg:.1f} m/s")
    print(f"v_rms = {v_rms:.1f} m/s\n")

def exercise_4():
    T = 300
    avg_KE = 3/2 * k_B * T
    print(f"Exercise 4: Average KE at T={T}K")
    print(f"<KE> = {avg_KE:.3e} J = {avg_KE/1.602e-19:.4f} eV\n")

def exercise_5():
    print("Exercise 5: Molar Heat Capacities")
    print(f"Monatomic: C_V = 3/2*R = {1.5*R:.2f} J/(mol·K)")
    print(f"Diatomic: C_V = 5/2*R = {2.5*R:.2f} J/(mol·K)\n")

def exercise_6():
    d = 3.7e-10
    T = 300
    P = 101325
    n = P / (k_B * T)
    lam = 1 / (np.sqrt(2) * np.pi * d**2 * n)
    print(f"Exercise 6: Mean Free Path (N2 at {T}K, 1 atm)")
    print(f"lambda = {lam*1e9:.1f} nm\n")

if __name__ == "__main__":
    print("="*60)
    print("TOPIC 9: KINETIC THEORY - EXERCISES")
    print("="*60 + "\n")
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    print("Exercises completed!")

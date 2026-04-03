"""
Topic 10: Oscillations and Waves - Practice Exercises
SHM, damping, resonance, waves, Doppler effect
"""

import numpy as np

def exercise_1():
    """SHM: x = A cos(ωt + φ)"""
    A = 0.5  # Amplitude (m)
    f = 2.0  # Frequency (Hz)
    omega = 2 * np.pi * f
    T = 1 / f
    
    # At t = 0
    x_0 = A  # cos(0) = 1
    v_max = A * omega
    
    print("Exercise 1: Simple Harmonic Motion")
    print(f"Amplitude: A = {A} m")
    print(f"Frequency: f = {f} Hz, Period T = {T} s")
    print(f"Angular frequency: ω = {omega:.3f} rad/s")
    print(f"At t=0: x = {x_0} m")
    print(f"Maximum velocity: v_max = Aω = {v_max:.3f} m/s\n")

def exercise_2():
    """Energy in SHM"""
    m = 2.0
    A = 0.1
    f = 5.0
    omega = 2 * np.pi * f
    k = m * omega**2
    E_total = 0.5 * k * A**2
    
    print("Exercise 2: Energy in SHM")
    print(f"Mass: m = {m} kg")
    print(f"Amplitude: A = {A} m")
    print(f"Spring constant: k = {k:.1f} N/m")
    print(f"Total energy: E = (1/2)kA² = {E_total:.4f} J\n")

def exercise_3():
    """Damped oscillation damping ratio"""
    m = 1.0
    k = 10.0
    b = 2.0  # Damping coefficient
    
    zeta = b / (2 * np.sqrt(k * m))
    omega_0 = np.sqrt(k / m)
    
    print("Exercise 3: Damped Oscillations")
    print(f"Natural frequency: ω₀ = {omega_0:.3f} rad/s")
    print(f"Damping coefficient: b = {b}")
    print(f"Damping ratio: ζ = b/(2√(km)) = {zeta:.3f}")
    if zeta < 1:
        print("Regime: Underdamped (oscillates with decay)\n")
    elif zeta == 1:
        print("Regime: Critically damped\n")
    else:
        print("Regime: Overdamped\n")

def exercise_4():
    """Resonance and Q factor"""
    m = 1.0
    k = 10.0
    zeta = 0.2
    
    omega_0 = np.sqrt(k / m)
    f_0 = omega_0 / (2 * np.pi)
    Q = 1 / (2 * zeta)
    
    print("Exercise 4: Resonance")
    print(f"Natural frequency: f₀ = {f_0:.2f} Hz")
    print(f"Damping ratio: ζ = {zeta}")
    print(f"Quality factor: Q = 1/(2ζ) = {Q:.1f}")
    print(f"Sharp resonance (high Q means narrow peak)\n")

def exercise_5():
    """Wave properties"""
    wavelength = 2.0  # m
    f = 10.0  # Hz
    v = wavelength * f
    T = 1 / f
    k = 2 * np.pi / wavelength
    
    print("Exercise 5: Wave Properties")
    print(f"Wavelength: λ = {wavelength} m")
    print(f"Frequency: f = {f} Hz")
    print(f"Wave speed: v = λf = {v} m/s")
    print(f"Period: T = {T} s")
    print(f"Wave number: k = 2π/λ = {k:.3f} rad/m\n")

def exercise_6():
    """Standing waves on a string"""
    L = 1.0  # String length (m)
    v_wave = 100.0  # Wave speed (m/s)
    n = 3  # 3rd harmonic
    
    f_n = n * v_wave / (2 * L)
    wavelength_n = 2 * L / n
    
    print("Exercise 6: Standing Waves on String")
    print(f"String length: L = {L} m")
    print(f"Wave speed: v = {v_wave} m/s")
    print(f"Harmonic number: n = {n}")
    print(f"Frequency: f_n = nv/(2L) = {f_n} Hz")
    print(f"Wavelength: λ_n = 2L/n = {wavelength_n:.3f} m")
    print(f"Nodes: {n+1}, Antinodes: {n}\n")

def exercise_7():
    """Beats"""
    f1 = 440  # Hz (A note)
    f2 = 445  # Hz
    f_beat = abs(f2 - f1)
    
    print("Exercise 7: Beats")
    print(f"Frequency 1: f₁ = {f1} Hz")
    print(f"Frequency 2: f₂ = {f2} Hz")
    print(f"Beat frequency: f_beat = |f₂ - f₁| = {f_beat} Hz")
    print(f"You hear {f_beat} beat per second\n")

def exercise_8():
    """Doppler effect"""
    f_source = 1000  # Hz
    v_sound = 340  # m/s
    v_source = 34  # m/s (moving toward observer)
    
    f_observed = f_source * v_sound / (v_sound - v_source)
    
    print("Exercise 8: Doppler Effect")
    print(f"Source frequency: f = {f_source} Hz")
    print(f"Sound speed: v = {v_sound} m/s")
    print(f"Source moving toward observer: v_s = {v_source} m/s")
    print(f"Observed frequency: f' = f·v/(v-v_s) = {f_observed:.0f} Hz")
    print(f"Frequency shift: {f_observed - f_source:.0f} Hz higher\n")

if __name__ == "__main__":
    print("="*60)
    print("TOPIC 10: OSCILLATIONS AND WAVES - EXERCISES")
    print("="*60 + "\n")
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    
    print("="*60)
    print("Exercises completed!")
    print("="*60)

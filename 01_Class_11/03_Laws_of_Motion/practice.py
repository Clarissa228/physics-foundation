# ============================================================================
# Laws of Motion — Practice Exercises
# ============================================================================
# Instructions:
#   • Solve each exercise yourself before checking any reference.
#   • Keep units consistent and check that answers make physical sense.
#   • There is no solution file — the goal is the process, not the answer.
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ────────────────────────────────────────────────────────────────────────────
# Exercise 1: Newton's Second Law
# ────────────────────────────────────────────────────────────────────────────
#
# A 1500 kg car accelerates from rest to 25 m/s in 8 s.
#   (a) Find the net force.
#   (b) A 50 kg person in an elevator: find scale reading when
#       the elevator accelerates up at 2 m/s², down at 2 m/s², and at rest.
#
# Hints:
#   → F = ma
#   → Scale reads the normal force N
#   → When going up: N - mg = ma → N = m(g+a)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 2: Atwood Machine
# ────────────────────────────────────────────────────────────────────────────
#
# Two masses m1 = 4 kg and m2 = 6 kg hang over a frictionless pulley.
# Derive and compute: acceleration of the system and tension in the rope.
# Plot position of each mass over 3 seconds.
#
# Hints:
#   → Net force = (m2 - m1)*g, total mass = m1 + m2
#   → a = (m2-m1)*g/(m1+m2), T = 2*m1*m2*g/(m1+m2)
#   → x1(t) = 0.5*a*t², x2(t) = -0.5*a*t² (one goes up, one down)


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 3: Friction on an Incline
# ────────────────────────────────────────────────────────────────────────────
#
# A block (m=5 kg) sits on a 30° incline with μs=0.5, μk=0.3.
#   (a) Does it slide?
#   (b) If it does slide, what is the acceleration?
#   (c) Plot the forces acting on it (free body diagram using arrows).
#
# Hints:
#   → Normal force N = mg*cos(θ)
#   → Friction limit = μs*N vs mg*sin(θ)
#   → For FBD: use plt.annotate or plt.arrow


# Your code here


# ────────────────────────────────────────────────────────────────────────────
# Exercise 4: Circular Motion — Car on a Curve
# ────────────────────────────────────────────────────────────────────────────
#
# A 1000 kg car rounds a flat curve of radius 50 m at 20 m/s.
#   (a) What centripetal force is required?
#   (b) What minimum friction coefficient is needed?
#   (c) Plot required μ vs speed from 0 to 40 m/s.
#
# Hints:
#   → F_c = m*v²/r
#   → μ_min = v²/(r*g)
#   → np.linspace for speed range


# Your code here


# ============================================================================
# Sandbox — experiment freely below
# ============================================================================

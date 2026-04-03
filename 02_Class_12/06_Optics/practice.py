# =============================================================================
# Optics — Practice Exercises
# Class 12 Physics | Ray Optics & Wave Optics
# =============================================================================
# Instructions:
#   - Work through each exercise in order
#   - Do NOT look up solutions before trying — the struggle is the learning
#   - Use numpy, matplotlib, and sympy as needed
#   - Run your code frequently and check if it makes physical sense
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Exercise 1: Snell's Law Calculator
# -----------------------------------------------------------------------------
# Write a function snell(n1, theta1_deg, n2) that returns the refraction angle
# theta2 in degrees using Snell's law: n1 * sin(θ1) = n2 * sin(θ2)
# Test it: light going from air (n=1.0) into glass (n=1.5) at 30°
# Also find the critical angle for total internal reflection (water→air)
# Hint: use np.arcsin, np.degrees, np.radians

def snell(n1, theta1_deg, n2):
    # Your code here
    pass

# Test your function here
# print(snell(1.0, 30, 1.5))   # should be ~19.47°
# critical_angle = ...          # angle where theta2 = 90°


# -----------------------------------------------------------------------------
# Exercise 2: Lens Formula and Magnification
# -----------------------------------------------------------------------------
# Use the lens formula: 1/f = 1/v - 1/u  (using sign convention)
# Write a function lens(f, u) that returns (v, magnification)
# where magnification m = -v/u
# Test it with f = 20 cm and object at u = -30 cm (virtual object negative)
# Plot image distance v as u varies from -100 to -f-1 cm

def lens(f, u):
    # Your code here
    pass

# Your plotting code here


# -----------------------------------------------------------------------------
# Exercise 3: Young's Double Slit Interference
# -----------------------------------------------------------------------------
# Two slits separated by d = 0.5 mm, wavelength λ = 600 nm, screen at L = 1.5 m
# Compute and plot the intensity pattern I = I0 * cos²(πdy/λL) on the screen
# Mark the positions of bright and dark fringes on your plot
# Hint: fringe width β = λL/d

d = 0.5e-3      # slit separation in metres
lam = 600e-9    # wavelength in metres
L = 1.5         # screen distance in metres

# Your code here


# -----------------------------------------------------------------------------
# Exercise 4: Single Slit Diffraction Envelope
# -----------------------------------------------------------------------------
# Intensity for single slit: I = I0 * (sin(α)/α)² where α = πa*sinθ/λ
# Slit width a = 0.1 mm, λ = 500 nm
# Plot the diffraction pattern as a function of y position on the screen (L=1m)
# Find and annotate the positions of the first few minima

a = 0.1e-3      # slit width
lam2 = 500e-9
L2 = 1.0

# Your code here
# Hint: handle α = 0 carefully (use np.sinc or np.where)


# -----------------------------------------------------------------------------
# Exercise 5: Thin Film Interference
# -----------------------------------------------------------------------------
# A soap film (n=1.33) in air is illuminated with white light at normal incidence
# Conditions for constructive interference: 2nt = (m + 1/2)λ
# (because of phase flip at first surface, none at second)
# Plot the wavelengths that constructively interfere as film thickness varies
# from 0 to 800 nm, for visible range λ = 400–700 nm
# Color-code the wavelengths on your plot

n_film = 1.33
t_range = np.linspace(0, 800e-9, 1000)

# Your code here


# -----------------------------------------------------------------------------
# Exercise 6: Rayleigh Criterion
# -----------------------------------------------------------------------------
# Two stars are just resolvable when their angular separation θ = 1.22 λ / D
# where D is aperture diameter
# (a) For λ = 550 nm and D = 0.2 m (telescope), what is the minimum resolvable angle?
# (b) For the human eye (D = 3mm), what is the minimum angle?
# (c) Plot minimum resolvable angle vs aperture D from 1mm to 10m

# Your code here


# =============================================================================
# Sandbox — Try your own optics experiments below!
# =============================================================================
# Ideas:
# - Simulate a diffraction grating (N slits interference)
# - Draw ray diagrams for concave/convex mirrors
# - Model chromatic aberration in a lens (different f for different λ)
# - Explore the double-slit pattern with varying slit separation d

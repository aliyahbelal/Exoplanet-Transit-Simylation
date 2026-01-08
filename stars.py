import numpy as np
import matplotlib.pyplot as plt

class Star:
    def __init__(self, name, radius, brightness, temp):
        self.name = name
        self.radius = radius
        self.brightness = brightness
        self.temp = temp
        self.area = np.pi * radius**2

class Planet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.area = np.pi * radius**2

def circle_overlap_area(R, r, d):
    # Return area of overlap between two circles of radii R and r separated by d
    if d >= R + r:
        return 0.0
    if d <= abs(R - r):
        return np.pi * min(R, r)**2
    # General case
    part1 = R**2 * np.arccos((d**2 + R**2 - r**2) / (2 * d * R))
    part2 = r**2 * np.arccos((d**2 + r**2 - R**2) / (2 * d * r))
    part3 = 0.5 * np.sqrt((-d + R + r) * (d + R - r) * (d - R + r) * (d + R + r))
    return part1 + part2 - part3

def simulate_transit(star, planet, impact=0.0):
    # Simulate a transit light curve by computing the projected overlap area
    time_steps = np.linspace(-2, 2, 400)  # higher resolution
    flux = []

    R = star.radius
    r = planet.radius
    v = R  # transverse velocity (in units of star radii per time unit)

    for t in time_steps:
        x = v * t  # planet center x-position (time -> position)
        y = impact * R  # impact parameter in units of R
        d = np.hypot(x, y)
        overlap = circle_overlap_area(R, r, d)
        blocked_fraction = overlap / (np.pi * R**2)
        flux.append(star.brightness * (1 - blocked_fraction))

    return time_steps, np.array(flux)

# Initialize data
sun_like = Star("Alpha Centauri A", radius=100, brightness=1.0, temp=5790)
jupiter_like = Planet("Jupiter", radius=15)

# Run the fixed function
time, flux = simulate_transit(sun_like, jupiter_like)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(time, flux, color='gold', marker='o', linestyle='-')
plt.title(f"Simulated Transit: {jupiter_like.name} across {sun_like.name}")
plt.xlabel('Time (Arbitrary Units)')
plt.ylabel('Observed Brightness (flux)')
plt.grid(True, alpha=0.3)
plt.show()
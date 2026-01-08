# Exoplanet-Transit-Simylation
A Python-based tool that simulates the Transit Method of exoplanet detection. This project models the "dip" in a star's brightness as a planet passes in front of it, producing a light curve that can be used to determine the planet's size relative to its host star.

# 🚀 Features


Object-Oriented Design: Uses Star and Planet classes to manage stellar and planetary properties (radius, brightness, etc.).

Flux Calculation: Uses the ratio of cross-sectional areas to calculate precise transit depth.

Transit Geometry: Simulates the light curve including:

Baseline: The star's normal brightness.

Ingress/Egress: The gradual entry and exit of the planet (slanted edges).

Bottom: Total light blocked when the planet is fully in front of the star.

Visualization: Generates a professional plot using Matplotlib.




# 🛠️ How It Works
The simulator uses the fundamental astronomical relationship:
<img width="236" height="96" alt="image" src="https://github.com/user-attachments/assets/0c91d131-2be3-4892-9259-a0d12c0993c4" />

By calculating the distance of the planet from the center of the star over a time series, the script determines exactly how much light is being blocked at any given moment.


# 📊 Example OutputRunning
the script generates a light curve showing the transit of a Jupiter-like planet across a Sun-like star. The "U-shape" in the plot represents the planet's journey across the stellar disk.


**Physics Note**
the depth of the dip in the graph is (2.25%) for the Jupiter and Sun example is exactly how NASA discovers the radius of planets thousands of light-years away!

 

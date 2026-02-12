import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Data Setup (Amas to Poonam: Feb 17 - Mar 3, 2026)
dates = [
    "Feb 17", "Feb 18", "Feb 19", "Feb 20", "Feb 21", "Feb 22", "Feb 23",
    "Feb 24", "Feb 25", "Feb 26", "Feb 27", "Feb 28", "Mar 1", "Mar 2", "Mar 3"
]

# Radial distance (r) in kilometers
distances = [
    399400, 397800, 395800, 393500, 390900, 388100, 385100, 
    382000, 378900, 375800, 373000, 370600, 368800, 367800, 367500
]

# Angular position (theta) in degrees
angles_deg = [
    0, 13.5, 27.2, 41.1, 55.4, 70.0, 85.1, 
    100.7, 116.8, 133.3, 150.2, 167.3, 184.5, 201.7, 218.8
]

# 2. Pre-processing: Convert degrees to radians for Matplotlib
angles_rad = np.radians(angles_deg)

# 3. Create the Polar Plot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111, projection='polar')

# Plot the Moon's path
ax.plot(angles_rad, distances, marker='o', linestyle='-', color='royalblue',         linewidth=2, markersize=6, label='Moon Path')

# Mark Earth at the center
ax.plot(0, 0, marker='o', markersize=15, color='forestgreen', label='Earth')

ax.set_title('Moon Polar Coordinates: Amas to Poonam (Feb-Mar 2026)', pad=30, fontsize=14)
ax.set_theta_zero_location("E")  # Set 0° to the Right (East)
ax.set_rlabel_position(-22.5)   # Move radial distance labels away from the line
ax.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()


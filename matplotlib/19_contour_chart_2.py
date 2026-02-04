import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare peak data (Longitude and Elevation)
peaks_data = [
    ("Nanga Parbat", 74.58, 8126),
    ("K2", 76.51, 8611),
    ("Nanda Devi", 79.97, 7816),
    ("Annapurna I", 83.82, 8091),
    ("Mount Everest", 86.92, 8848),
    ("Makalu", 87.08, 8485),
    ("Kangchenjunga", 88.14, 8586),
    ("Namcha Barwa", 95.05, 7782)
]

df = pd.DataFrame(peaks_data, columns=['Peak', 'Longitude', 'Elevation'])
# 2. Define the Grid for X (Location) and Y (Elevation)
# X: Longitude range from West to East
# Y: Elevation range from sea level to above Everest
x_coords = np.linspace(70, 100, 200)
y_coords = np.linspace(6000, 9500, 200)
X, Y = np.meshgrid(x_coords, y_coords)

# 3. Calculate Z (Temperature) based on Environmental Lapse Rate
# Standard Lapse Rate: ~6.5°C drop per 1000m gain
# Formula: T = T_base - (0.0065 * Elevation)
T_base = 25  # Estimated sea-level temperature in Celsius
Z = T_base - (0.0065 * Y)

# 4. Create the Contour Plot
plt.figure(figsize=(12, 7))

# Filled contour plot for Temperature 
# 'RdYlBu_r' provides a scale from Red (Hot) to Blue (Cold)
cp = plt.contourf(X, Y, Z, levels=20, cmap='RdYlBu_r')

# Add a colorbar to explain the temperature values
cbar = plt.colorbar(cp)
cbar.set_label('Temperature ($^\circ$C)', fontsize=12)

# Add specific contour lines for clarity
contours = plt.contour(X, Y, Z, levels=10, colors='black', alpha=0.2)
plt.clabel(contours, inline=True, fontsize=8, fmt='%1.0f$^\circ$C')

# 5. Overlay the Physical Peaks
plt.scatter(df['Longitude'], df['Elevation'], color='black', marker='^', s=80, label='Major Peaks')

# Add labels for each peak
for i, row in df.iterrows():
    plt.text(row['Longitude'], row['Elevation'] + 150, row['Peak'], 
             fontsize=9, fontweight='bold', ha='center')

# 6. Formatting the final visual
plt.title('Himalayan Contour Map: Longitude (X) vs Elevation (Y) vs Temperature (Z)', fontsize=14)
plt.xlabel('Location (Longitude $^\circ$E)', fontsize=12)
plt.ylabel('Peak Size / Elevation (m)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.legend(loc='lower left')

plt.tight_layout()
plt.show()
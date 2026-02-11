import matplotlib.pyplot as plt

growth_rates = [
    [20.90, 23.10, 24.20, 14.59, 10.98],  # Andhra Pradesh
    [21.33, 24.06, 23.54, 28.62, 25.42],  # Bihar
    [29.39, 27.67, 21.19, 22.66, 19.28],  # Gujarat
    [32.23, 28.75, 27.41, 28.43, 19.90],  # Haryana
    [24.22, 26.75, 21.12, 17.51, 15.60],  # Karnataka
    [26.29, 19.24, 14.32, 9.43,  4.91],   # Kerala
    [28.67, 27.24, 27.24, 24.26, 20.35],  # Madhya Pradesh
    [27.45, 24.54, 25.73, 22.73, 15.99],  # Maharashtra
    [21.70, 23.89, 20.81, 20.10, 13.89],  # Punjab
    [27.83, 32.97, 28.44, 28.41, 21.31],  # Rajasthan
    [22.30, 17.50, 15.39, 11.72, 15.61],  # Tamil Nadu
    [19.78, 25.44, 25.55, 25.85, 20.23],  # Uttar Pradesh
    [26.87, 23.17, 24.73, 17.77, 13.84]   # West Bengal
]

states = [
    "Andhra Pradesh", "Bihar", "Gujarat", "Haryana", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Punjab", "Rajasthan",
    "Tamil Nadu", "Uttar Pradesh", "West Bengal"
]



# Main heatmap
im = plt.matshow(growth_rates, cmap='viridis', interpolation='nearest')

# Colorbar
plt.colorbar(im, label='Growth Rate (%)')

# Set y-axis (rows) → state names
plt.yticks(range(len(states)), states)

# Optional: set x-axis labels (you can change these to years or periods)
plt.xticks(range(5), ['1960-71', '1971-81', '1981-91', '1991-01', '2001-11'],
           rotation=90)   # or rotation=45 if you want
plt.title('Population Growth Rates by State')
plt.xlabel('Time Periods')
plt.ylabel('States')

# Optional: add grid for better readability
plt.grid(True)   # usually off for heatmaps, but you can try True
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare Data
years = np.array([2018, 2019, 2020, 2021, 2022, 2023])
teams = ["India", "Australia", "England", "Pakistan", "South Africa"]
team_indices = np.arange(len(teams))

# 2. Create the Grid (X = Years, Y = Team Numbers)
X, Y = np.meshgrid(years, team_indices)

# 3. Z-Value: Number of centuries made (Example Data)
# Each row represents a team, each column a year
centuries = np.array([
    [12, 15, 8, 10, 14, 18],  # India
    [10, 11, 7, 9, 12, 11],   # Australia
    [8, 14, 10, 11, 15, 13],  # England
    [5, 6, 9, 12, 11, 10],    # Pakistan
    [7, 8, 5, 4, 8, 9]        # South Africa
])

# 4. Initialize Plot
plt.figure(figsize=(12, 6))

# 5. Create the Filled Contour (The "Heat")
# levels: how many color steps; cmap: color scheme
cp = plt.contour(X, Y, centuries, levels=5,)

plt.yticks(team_indices, teams) # Map numbers back to Team Names
plt.title("Cricket Performance Contour: Century Trends (2018-2023)")
plt.xlabel("Year")
plt.ylabel("International Team")
plt.show()
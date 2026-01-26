import matplotlib.pyplot as plt

years = list(range(2000, 2025))  # 2000 to 2024 inclusive → 25 years

gdp_growth = [
    7.60, 4.82, 3.80, 7.86, 7.92,
    9.28, 9.26, 7.66, 3.90, 7.86,
    10.26, 6.63, 5.45, 6.39, 7.41,
    8.00, 8.26, 7.17, 6.90, 4.18,
    -7.30, 8.90, 6.99, 9.20, 8.20
]

plt.figure(figsize=(12, 6))           # make the plot wider

plt.plot(years, gdp_growth,
         color='blue',
         linewidth=2,
         marker='o',                   # small circle at each year
         markersize=6,
         markerfacecolor='white',
         markeredgecolor='blue')

plt.title("India GDP Growth Rate (%) since 2000", fontsize=14, pad=12)
plt.xlabel("Year", fontsize=12)
plt.ylabel("GDP Growth Rate (%)", fontsize=12)

# Show every single year on x-axis
plt.xticks(years, rotation=60, ha='right', fontsize=9)

plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()                    # prevent label cutoff

plt.show()
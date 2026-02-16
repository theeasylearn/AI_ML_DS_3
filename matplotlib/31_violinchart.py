import matplotlib.pyplot as plt

# Our Sensex data from the last week (Feb 9 - Feb 13)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
open_prices  = [84177.51, 84210.00, 84339.15, 83968.43, 82902.73]
close_prices = [84065.75, 84273.92, 84233.64, 83674.92, 82626.76]

# Combine open and close into a list of lists for the plot
# Each sub-list represents one day's price distribution
data_to_plot = [[o, c] for o, c in zip(open_prices, close_prices)]
print(data_to_plot)

fig, ax = plt.subplots(figsize=(10, 6))

# Create the violin plot
# showmedians=True helps identify the middle price point of the day
parts = ax.violinplot(data_to_plot, showmeans=True, showmedians=True, showextrema=True)

parts['cmedians'].set_colors('red')   # Median line in red
parts['cmins'].set_colors('black')     # Bottom cap
parts['cmaxes'].set_colors('black')    # Top cap

# --- Formatting the Chart ---
ax.set_title('Sensex Price Distribution: Open vs Close (Last Week)', fontsize=14)
ax.set_ylabel('Index Points', fontsize=12)
ax.set_xticks(range(1, len(days) + 1))
ax.set_xticklabels(days)
plt.show()

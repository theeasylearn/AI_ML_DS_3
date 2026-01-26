import matplotlib.pyplot as plt
months = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

delhi_temperature = [14, 18, 24, 30, 35, 34, 31, 30, 29, 26, 20, 15] # plot line graph
ahmedabad_temperature = [17, 21, 27, 33, 38, 36, 33, 32, 31, 30, 24, 19] # plot line graph
mumbai_temperature = [24, 25, 27, 29, 30, 28, 27, 27, 27, 28, 27, 25] # plot line graph
plt.figure(figsize=(12,6))
plt.plot(months,  delhi_temperature,  color="red",  marker="o",  linestyle="-",  linewidth=2,
  label="Avg Temperature of new delhi"
)
plt.plot(months, ahmedabad_temperature,  color="orange",  marker="*",  linestyle="--",  linewidth=1,
  label="Avg Temperature of Ahmedabad"
)

plt.plot(months, mumbai_temperature,  color="blue",  linestyle="-",  linewidth=1.5,
  label="Avg Temperature of mumbai"
)
plt.title("Average Monthly Temperature of New Delhi & ahmedabad (2024)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
# additional functions
plt.grid(True)     # show grid lines
plt.legend()      # show legend
plt.ylim(0, 50)     # set Y-axis range
plt.savefig('temprature1.png',dpi=200)
plt.show()
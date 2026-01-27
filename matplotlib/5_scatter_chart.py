import matplotlib.pyplot as plt
decades = [
    "1941-1951", "1951-1961", "1961-1971", "1971-1981", 
    "1981-1991", "1991-2001", "2001-2011"
]
# Growth rates in percentage
population_rates = [
    13.31/10,  # 1941-1951 (Independence decade)
    21.51/10,  # 1951-1961
    24.80/10,  # 1961-1971 (Peak growth rate)
    24.66/10,  # 1971-1981
    23.87/10,  # 1981-1991
    21.54/10,  # 1991-2001
    17.70/10   # 2001-2011
]
gdp_rates = [
    3.6,   # 1950s: Initial planning phase
    3.3,   # 1960s: Impacted by wars and droughts
    3.4,   # 1970s: High inflation and political instability
    5.2,   # 1980s: Early liberalization and industrial growth
    5.8,   # 1990s: Post-1991 economic reforms
    7.5,   # 2000s: High growth period / "Golden Era"
    5.4   # 2010s: Slowdown and pandemic impact (-5.8% in 2020)
]
plt.figure(figsize=(12,6))
plt.scatter(decades,population_rates,s=100,color='red',marker='^',label='Data Points')
plt.legend()

plt.scatter(decades,gdp_rates,s=100,color='green',marker='o')
plt.xlabel('decades')
plt.ylabel('growth rate')
plt.ylim(0,10)
plt.title('population and gdp growth rate')
plt.grid(True)
plt.show()
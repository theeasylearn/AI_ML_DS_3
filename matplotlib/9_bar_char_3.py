import matplotlib.pyplot as plt
import numpy as np 
data = {
    2008: 0,
    2009: 1,
    2010: 1,
    2011: 4,
    2012: 5,
    2013: 4,
    2014: 4,
    2015: 1,
    2016: 3,
    2017: 6,
    2018: 5,
    2019: 5,
    2020: 0,
    2021: 1,
    2022: 2,
    2023: 3,
    2024: 2,
    2025: 3,
    2026: 1  # As of Jan 28, 2026 – year still ongoing
}
years = list(data.keys())
century = list(data.values())
print(years,century)
plt.figure(figsize=(10,15))
plt.bar(years,century,width=1,color='cyan',edgecolor='blue')
plt.ylabel('ODI CENTURY')
plt.title('Virat kohli ODI century in each year')
plt.ylim(0,8)
plt.xticks(ticks=years,rotation='vertical')
plt.grid(True)
plt.show()
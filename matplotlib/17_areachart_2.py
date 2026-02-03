import matplotlib.pyplot as plt 
# Daily Percentage Change for Silver (Jan 1 to Jan 31, 2026)
silver_price_change = [-0.42, 1.26, 1.04, -1.03, 2.88, 2.01, 3.93, -4.16, -1.18, 4.38, 0.0, 3.81, 2.76, -0.71, 1.54, 2.83, 1.37, 4.1, 5.02, 2.99, -5.77, 5.71, 6.69, -1.41, 6.9, 6.45, 2.43, 2.37, 7.14, -12.94, -1.49]

gold_price_change = [
    -0.6, 0.8, 0.0, 0.0, 2.8, 1.0, -0.7, -0.04, 0.9, 0.0, 
    0.0, 2.5, -0.3, 0.8, -0.3, -0.6, 0.0, 1.8, -0.2, 2.8, 
    1.5, 1.6, 1.4, 0.0, 0.0, 1.7, -0.02, 4.3, 0.6, -9.0, -1.7
]
dates = list(range(1,32))
print(dates)
plt.figure(figsize=(12,6))
plt.fill_between(dates,silver_price_change,label='Silver price range',alpha=0.5,color='orange')
plt.fill_between(dates,gold_price_change,label='gold price range',alpha=0.5,color='yellow')
plt.xlabel('Months')
plt.ylabel('price change')
plt.xticks(dates)
plt.title('month wise metal price change in january')
plt.grid(True)
plt.show()
# plt.fill_between()


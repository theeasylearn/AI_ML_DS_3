import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Load your dataset
car_sales = pd.read_csv('car_sales.csv')

# 2. TRANSFORM: Melt the data from Wide to Long format
# This puts Swift, WagonR, and Baleno into a single column called 'Model'
car_sales_long = car_sales.melt(id_vars='Week', 
                                value_vars=['Swift', 'WagonR', 'Baleno'], 
                                var_name='Model', 
                                value_name='Sales')

# 3. PLOT: Use the new 'Model' column for hue
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=car_sales_long, x='Sales', hue='Model', palette='bright')

plt.title('ECDF of Weekly Car Sales: Maruti Top 3 (2023)')
plt.xlabel('Units Sold per Week')
plt.ylabel('Proportion of Weeks')
plt.grid(True, alpha=0.3)
plt.show()
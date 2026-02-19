import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

data = pd.read_csv('instagram.csv')

sns.scatterplot(data=data, x='Age_Group', y='Avg_Daily_Screen_Time_Mins', hue='Age_Group', palette='viridis')
plt.show()

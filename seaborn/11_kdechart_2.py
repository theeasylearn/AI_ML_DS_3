import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
heart_attack = pd.read_csv('heart_attack.csv')
sns.kdeplot(data=heart_attack, x='Age',fill=True, color='orange',hue='Gender',alpha=0.5)
plt.title('Person age @ heart attack')
plt.xlabel('Age')
plt.ylabel('Density')

plt.show()


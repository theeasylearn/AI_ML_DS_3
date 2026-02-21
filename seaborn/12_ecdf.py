import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load dataset
titanic = sns.load_dataset("titanic")
titanic_clean = titanic.dropna(subset=['age'])
sns.ecdfplot(data=titanic_clean, x='age', color='blue')
plt.title('ECDF of Passenger Age')
plt.xlabel('Age')
plt.ylabel('ECDF')
plt.show()

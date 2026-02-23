import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic = sns.load_dataset("titanic")
titanic_clean = titanic.dropna(subset=['age'])
sns.rugplot(data=titanic_clean, x='age', height=0.1, color='orange')
plt.title('Rug Plot of Passenger Age')
plt.xlabel('Age')
plt.show()

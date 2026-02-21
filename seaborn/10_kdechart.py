import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset("titanic")
titanic_age = titanic.dropna(subset=['age'])
sns.kdeplot(data=titanic_age, x='age', fill=True, color='orange')
plt.title('KDE Plot of Passenger Age')
plt.xlabel('Age')
plt.ylabel('Density')

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load dataset
titanic = sns.load_dataset("titanic")
# Drop rows where age or survived is missing
tit = titanic.dropna(subset=['age', 'survived'])

# Create lineplot: average survival by age
sns.lineplot(x='age', y='survived', data=tit)

# Add labels and title
plt.title('Titanic Survival Rate by Age')
plt.xlabel('Age')
plt.ylabel('Survival Rate')
plt.show()

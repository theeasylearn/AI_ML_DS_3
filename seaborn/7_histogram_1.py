import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset("titanic")
plt.figure(figsize=(12,6),dpi=100)
sns.histplot(data=titanic, x='age', bins=30, kde=False, color='skyblue')
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

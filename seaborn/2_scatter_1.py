import matplotlib.pyplot as plt
import seaborn as sns

# use of titanic dataset
titanic = sns.load_dataset('titanic')
sns.scatterplot(x='age', y='fare', data=titanic,)
plt.show()

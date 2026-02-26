import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load dataset
marks = pd.read_csv('marks_2.csv')
sns.pointplot(data=marks, x="division", y="maths",hue='gender')
plt.title("Gender wise math subject performance")
plt.ylabel("Maths marks")
plt.xlabel("Division")
plt.show()

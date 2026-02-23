import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
marks = pd.read_csv('marks.csv')
sns.rugplot(data=marks, x='Exam_Mark',height=0.5, color='blue')
plt.title('Rug Plot of Student marks')
plt.xlabel('Marks')
plt.show()

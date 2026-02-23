import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
marks = pd.read_csv('stream_marks.csv')
sns.stripplot(data=marks,x='stream',y='marks')
plt.title('Stream plot of Student marks')
plt.xlabel('steram')
plt.ylabel('marks')
plt.show()

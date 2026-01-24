import matplotlib.pyplot as plt 
import pandas as pd 
# Sequential runs scored in each over: 1st over to 16th over (partial)
y = [6, 4, 18, 12, 22, 15, 9, 14, 11, 21, 8, 13, 24, 16, 11, 5]
#create series 
s1 = pd.Series(y)
score = s1.cumsum()
x = list(range(1,17)) # return python list which has 1 to 20
# print(y,x)
plt.figure(figsize=(14,6)) #set plot size in each (1st value is for x and for y)
plt.plot(x,score)
plt.xlabel('overs',loc='right',labelpad=10,fontweight='bold')
plt.ylabel('runs',loc='top',labelpad=10,fontweight='bold')
plt.title('India Vs Newzland (2nd T20 match)',fontsize=20,fontweight='bold')
plt.show()
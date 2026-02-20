# Rohit Sharma ODI Career Runs (Chronological Order)
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
runs = [
8, 1, 52, 0, 24, 0, 8, 70, 4, 10, 22, 13, 12, 1, 0, 44, 4, 2, 3, 23, 
    114, 101, 0, 11, 5, 26, 13, 46, 4, 121, 0, 5, 95, 5, 0, 7, 5, 1, 0, 
    21, 10, 33, 4, 4, 4, 13, 5, 65, 83, 4, 39, 48, 65, 18, 13, 44, 10, 
    20, 64, 8, 79, 141, 0, 52, 13, 209, 13, 79, 16, 62, 15, 264, 138, 7, 
    0, 0, 34, 15, 137, 34, 16, 150, 3, 21, 65, 171, 124, 28, 41, 99, 1, 
    67, 10, 11, 2, 82, 1, 14, 70, 147, 91, 123, 0, 76, 7, 124, 104, 30, 
    147, 20, 7, 115, 15, 5, 47, 48, 111, 5, 2, 48, 162, 63, 133, 43, 62, 
    122, 57, 140, 1, 18, 102, 104, 103, 1, 159, 119, 19, 4, 28, 20, 76, 
    13, 51, 101, 30, 12, 11, 13, 10, 71, 74, 53, 81, 131, 86, 48, 46, 
    4, 40, 61, 87, 4, 13, 47, 23, 58, 19, 5, 58, 23, 8, 11, 51, 10, 13, 
    30, 101, 12, 53, 81, 131, 86, 48, 46, 4, 40, 61, 87, 4, 13, 47, 23, 
    58, 19, 5, 58, 23, 8, 37, 25, 64, 58, 119, 41, 20, 15, 28, 76, 10, 
    13, 30, 101, 12, 53, 81, 131, 86, 48, 46, 4, 40, 61, 87, 4, 13, 47, 
    23, 58, 19, 5, 58, 23, 8, 76, 8, 73, 121, 57, 14, 75, 26, 24, 11
]
# print(len(runs))
rohit_sharma = pd.DataFrame(runs,columns=['runs'])
# print(rohit_sharma)
plt.figure(figsize=(12,10),dpi=150)
sns.histplot(data=rohit_sharma, x='runs', bins=8, kde=True, color='skyblue')
plt.title('Distribution of Rohit sharma runs')
plt.xlabel('Match')
plt.ylabel('runs')
plt.xticks(range(0,len(runs),10))   # start, end, step
plt.show()

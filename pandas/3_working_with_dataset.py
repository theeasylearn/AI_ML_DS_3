import pandas as pd 
#create series 
s1 = pd.read_csv('marks.csv').squeeze()
print(s1)
s2 = pd.read_excel('marks.xlsx').squeeze()
print(s2)
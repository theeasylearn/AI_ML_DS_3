import pandas as pd 

s1 = pd.Series([100,20,30,40,10,20,30,40])
print(s1)
print(s1.duplicated())
s1 = s1.drop_duplicates()
print(s1)
# print("Cumulative sum ",s1.cumsum())
# print("Cumulative product ",s1.cumprod())
print(s1.clip(20,40))
print(s1.replace(20,200))
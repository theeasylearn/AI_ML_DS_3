import pandas as pd 
s1 = pd.Series([50,-25,100,150,200,140],index=['c','d','a','b','f','e'])
print(s1)
print("minimum value ",s1.min()," at index ",s1.idxmin())
print("maximum value ",s1.max()," at index ",s1.idxmax())
print(s1.abs())
print("elements in series ",len(s1))
print(s1.sort_values())
print(s1.sort_index())
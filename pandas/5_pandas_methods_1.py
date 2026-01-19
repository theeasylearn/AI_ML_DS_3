import pandas as pd 
s1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s1)
#methods 
print(s1.head(2)) # 10 20
print(s1.tail(2)) # 40 50
print(s1.to_list())
print(s1.to_dict())
print(type(s1))
age = 80
print(type(age))
name = "ram"
print(type(name))
print(s1.describe())
s1 = s1.astype(float) #convert & return Series to given type
print(s1)
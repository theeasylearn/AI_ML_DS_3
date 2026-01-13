import pandas as pd 
print(pd.__version__)
series = pd.Series([100,200,300,500,1000],index=['a','b','c','d','e'],name='easylearn')
print(series)
#display only indes
print(series.index)

#display only values 
print(series.values)

#display data type
print(series.dtype)

#display name
print(series.name)

#display shape
print(series.shape)

#display dimension 
print(series.ndim)

#display size 
print(series.size)

#is series unique
print("is series unique ",series.is_unique)

#is series has NAN
print("is series has NAN ",series.hasnans)



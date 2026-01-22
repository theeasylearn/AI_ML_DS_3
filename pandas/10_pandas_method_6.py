import pandas as pd 
earthquake_dates = ["2025-07-30", "2021-08-12", "2021-07-29", "2021-03-04", "2019-05-26", "2018-08-19", "2017-09-08", "2015-09-16", "2014-04-01", "2013-05-24"]
s1 = pd.Series(earthquake_dates)
s1 = pd.to_datetime(s1) #Convert Series into date time 
print(s1)
print(s1.dt.year)
print(s1.dt.month)
print(s1.dt.day)
print(s1.dt.weekday)
print(s1.dt.strftime('%A %d-%m-%Y'))
s2 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s2.loc['c'])
print(s2.loc['a'])
print(s2.loc['b'])
# print(s2.loc['x']) #return keyerror
print(s2.get('x','not found'))
print(s2.iloc[0:2])

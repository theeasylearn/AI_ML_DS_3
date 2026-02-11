from matplotlib import pyplot as plt 
import numpy as np 

years = list(range(2021,2026))
print(years)
web = [80,70,60,50,40]
mobile = [15,25,35,40,30]
ai = [5,5,5,10,30]

plt.bar(years,web,color='blue',label='web',bottom=None)
plt.bar(years,mobile,color='orange',label='mobile',bottom=web)
plt.bar(years,ai,color='red',label='ai',bottom=mobile)
plt.title("bar chart income sharing of different product")
plt.xlabel("years")
plt.ylabel("income ratio")
plt.legend()
plt.show()

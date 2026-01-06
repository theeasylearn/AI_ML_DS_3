import numpy as np 
a = np.array([10,20,200,1000])
b = np.array([10,20,200,2000])
c = np.array([10,200,2000,3000])
print(a,b,c)
print(a == b) #True
print(a == c) #False
print(np.all(a == b))
print(np.any(a == b))
import numpy as np 
#create array that has 5 values between 1.0 and 2.0 (both including)
arr1 = np.linspace(1.0,2.0,num=5)
print(arr1)
#create array that has 7 values between 1.0 and 2.0 (1.0 including
arr2 = np.linspace(1,2,num=7,endpoint=False)
print(arr2)
#create array that has 10 values between 2.0 and 2.5 (start including, also return retvalue 
arr3,step = np.linspace(2.0,2.5,num=10,endpoint=False,retstep=True)
print(arr3,step)


import numpy as np 
arr1 = np.arange(10)
print(arr1)
#copy array 
arr2 = np.copy(arr1)
print(arr2)

list = [10,20,30,40,50.12]
tuple = (100,200,300,500,1000)

arr3 = np.copy(list)
arr4 = np.copy(tuple)

print(arr3)
print(arr4)


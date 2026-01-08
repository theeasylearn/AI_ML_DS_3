import numpy as np 
#create array 
arr1 = np.array([10,20,30])
arr2 = np.array([10,20,30])
arr3 = np.array([10,20,100])
arr4 = np.array([[10,20,30]])

print(arr1,arr2,arr3,arr4)
print(np.array_equal(arr1,arr2)) #True
print(np.array_equal(arr2,arr3)) #False
print(np.array_equal(arr1,arr4)) #False because shape is not same 




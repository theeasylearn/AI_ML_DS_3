import numpy as np 
arr1 = np.array([10,20,30])
arr2 = np.array([10,20,30])
result_and = np.logical_and(arr1<=20,arr2>5)
print(result_and)
result_or = np.logical_or(arr1<=20,arr2>20)
print(result_or)
result_not = np.logical_not(arr1<50)
print(result_not)
result_xor = np.logical_xor(arr1<=20,arr2>20)
print(result_xor)


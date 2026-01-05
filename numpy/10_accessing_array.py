import numpy as np 

arr = np.array([10,20,30,40])
arr2d = np.array([[40,50,60],[70,80,90]])
print(arr) 
print(arr2d)
# accessing element in 1d array
print(arr[0]) # 10
print(arr[0:2]) # 10 20
# accessing element in 2d array
print(arr2d[0,0]) # 40
print(arr2d[1,1]) # 80
# getting slice of array
print(arr2d[0:2,0:2]) #display all rows and columns from 0 row to 1st row and 0oth column to 1st column
#get all values above 20
print(arr[arr > 20])

#get all values above 50 from 2d array
filtered_array = arr2d[arr2d > 50]
print(filtered_array)


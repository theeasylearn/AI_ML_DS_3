import numpy as np 

arr = np.array([10,20,30,40])
arr2d = np.array([
    [40,50,60],
    [70,80,90]])
print(arr) 
print(arr2d)

arr[0] = 100 #update value at 0th position
arr[1:3] = [200,300] #update value at 1st and 2nd position
print("now array has ", arr)

#update value at 0th row and 0th column
arr2d[0,0] = 1000
print(arr2d)

#update part of the array
# arr2d[0:0,2:2] = [[400,500],[700,800]]
arr2d[0:2, 0:2] = [[400, 500], [700, 800]]
print(arr2d)
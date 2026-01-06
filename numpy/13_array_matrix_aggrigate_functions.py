import numpy as np 

# to do matrix multiplication, both array must have same number of rows and columns. means array symtrical 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(b)
#matrix multiplication
print(a @ b)
print(a.dot(b)) #same as above

c = np.array([10,20,30,100])
print(c)
print(c>20)
#aggrigate function 
print("Sum of all elements in c ",c.sum())
print("average of all elements in c ",c.mean())
print("minimum of all elements in c ",c.min())
print("maximum of all elements in c ",c.max())
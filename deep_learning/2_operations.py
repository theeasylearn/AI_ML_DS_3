import torch as tc 
data1 = [[1,2,3],[4,5,6],[7,8,9]]
data2 = [[1,2,1],[2,3,2],[3,4,3]]

#create tensor
t1 = tc.tensor(data=data1)
t2 = tc.tensor(data=data2)

#addition 
addition = t1 + t2 
subtraction = t1 - t2 

print(addition)
print(subtraction)

#scaler operations
print(t1 + 1)
print(t1 * 2)
print(t1 / 3)

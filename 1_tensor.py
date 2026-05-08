import torch as tc 
data = [10,20,30,40,50,60]
tensor1 = tc.tensor(data)
print(tensor1)

tensor2 = tc.zeros(3,5)
print(tensor2)

tensor3 = tc.rand(4,5)
print(tensor3)
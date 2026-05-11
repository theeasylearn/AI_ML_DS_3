import torch as tc 
print(tc.__version__)
t1 = tc.tensor([10.0,20.0,30.0],requires_grad=True)
t2 = tc.tensor([1.0,2.0,3.0],requires_grad=True)

print(t1)
print(t2)

z = t1**2 + t2**3
z.sum().backward()
print(z)
print(t1.grad)
print(t2.grad)
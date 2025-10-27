x = int(input("Enter one number"))
y = int(input("Enter another number"))

result  = x is y 
result2 = x is not y 

print(result,result2)
print(id(x),id(y))
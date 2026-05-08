import math 
num1 = float(input("Enter any float value (negative/positive)"))

print("ceil value ", math.ceil(num1)) # Ceil value
print("floor value ", math.floor(num1)) # floor value 
print("truncated value ", math.trunc(num1)) # truncated value 

print("Absolute value ",math.fabs(num1))

print("Factorial of given number ",math.factorial(int(input("Enter number"))))
print("output of copysign ",math.copysign(num1,1))
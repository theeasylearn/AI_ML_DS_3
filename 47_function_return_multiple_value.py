def calculation(num1,num2):
    #create local variable
    addition = num1 + num2 
    subtraction = num1 - num2 
    multiplication = num1 * num2 
    division = num1 / num2 
    return addition,subtraction,multiplication,division

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

result = calculation(num1,num2)
print(result)
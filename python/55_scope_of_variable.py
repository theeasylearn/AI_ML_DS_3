amount = 12000 #global variable
def AddAmount(increment):
    global amount 
    amount = amount + increment
    deduction = amount * 0.02 #here deduction variable is local variable
    amount = amount - deduction


print("Salary before increment ",amount)
inc = int(input("Enter amount for increment"))
AddAmount(increment=inc)
print("Salary after increment ",amount)


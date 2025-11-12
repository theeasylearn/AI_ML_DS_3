# Without return value without argument
def printLine():
    print("_"*100)
    
# Without return value with argument 
def printLetter(letter,howManyTimes):
    print(letter*howManyTimes)

#create function that return square 
# With return value with argument 
def getSquare(number):
    #create local variable
    square = number * number
    return square

#create function that return qube 
# With return value with argument 
def getQube(number):
    temp = getSquare(number) #call function square 
    #here qube is also local variable
    qube = temp * number
    return qube

# With return value without argument
def getPi():
    pi = 22/7
    return pi 
#function do not run itself automatically. it has to be called(run)

printLine()
print("Example of function in python")
printLine()

num = int(input("Enter number"))

result = getSquare(num) #here we are calling getSquare function
printLetter('^',80)
print(f"Square = {result}")

qube = getQube(num) #here we are calling getQube function
printLetter('=',120)
print(f"qube = {qube}")

pi = getPi()
print(f"value of pi = {pi}")
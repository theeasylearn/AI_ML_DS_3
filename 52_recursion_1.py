#example of recursion
# print numbers into words
# input : 12345 output : one two three four five 
def toWords(amount):
    if amount>0:
        reminder = amount % 10 #5
        amount = amount // 10 #1234
        toWords(amount) #recursion
        if reminder == 0:
            print("zero ",end='')
        elif reminder == 1:
            print("one ",end='')
        elif reminder == 2:
            print("two ",end='')
        elif reminder == 3:
            print("three ",end='')
        elif reminder == 4:
            print("four ",end='')
        elif reminder == 5:
            print("five ",end='')
        elif reminder == 6:
            print("six ",end='')
        elif reminder == 7:
            print("seven ",end='')
        elif reminder == 8:
            print("eight ",end='')
        elif reminder == 9:
            print("nine ",end='')
amount = int(input("Enter amount : "))
toWords(amount)
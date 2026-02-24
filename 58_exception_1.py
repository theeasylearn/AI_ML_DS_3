#concept of exception handling mechanism 
#write a program to findout strike rate of batter using runs and ball given by user 
try:
    runs = int(input("Enter batter's run"))
    balls = int(input("Enter balls faced by batter"))
    strike_rate = (runs / balls) * 100
except ZeroDivisionError:
    print("ball can not be zero")
except ValueError:
    print("input must be only numbers...")
else:
    print('strike rate ',strike_rate)
finally:
    print("thank you for using our program")

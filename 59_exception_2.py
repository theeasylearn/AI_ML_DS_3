#concept of exception handling mechanism 
#write a program to findout strike rate of batter using runs and ball given by user 
while True:
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
        break #stop loop 
    
print("thank you for using our program")

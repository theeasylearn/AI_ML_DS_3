# write a program to findout batter with highest strike rate from 3 batter's runs and balls 
print("Enter 1st batter detail")
run1 = int(input("Enter 1st batter runs"))
ball1 = int(input("enter 1st batter balls"))

print("Enter 2nd batter detail")
run2 = int(input("Enter 2nd batter runs"))
ball2 = int(input("enter 2nd batter balls"))


print("Enter 3rd batter detail")
run3 = int(input("Enter 3rd batter runs"))
ball3 = int(input("enter 3rd batter balls"))

#calculate strike rate 
strike_rate1 = run1/ball1
strike_rate2 = run2/ball2
strike_rate3 = run3/ball3 

print(f"1st batter strike rate = {strike_rate1} 2nd batter strike rate = {strike_rate2} 3rd batter strike rate = {strike_rate3}")

if strike_rate1>strike_rate2:  #outer if
    if strike_rate1>strike_rate3: 
        print("1st batter has highest strike rate")
    else:
        print("3rd batter has highest strike rate")
else:
    if strike_rate2>strike_rate3: # < > <= >= == != inner if
        print("2nd batter has highest strike rate")
    else:
        print("3rd batter has highest strike rate")

print("Good bye")
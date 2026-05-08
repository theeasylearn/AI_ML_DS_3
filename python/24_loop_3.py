# write a program to calculate and display compound interest of given amount, rate, year
amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = int(input("Enter year"))
total_interest = 0 
count = 1
#calculate first year interest 

while count<=year:
    interest = amount * rate * 1 / 100
    amount += interest
    total_interest += interest
    count+=1

print("Total compound interest",total_interest)

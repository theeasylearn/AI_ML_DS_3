# write a program to accept purchase and sales amount of product and findout profit or loss amount
purchase_amount = int(input("Enter purchase amount")) # 120
sales_amount = int(input("Enter sales amount")) # 100
#calculate difference 

difference = sales_amount - purchase_amount
#use decision making statement to decide profit or loss 
if difference>0:
    print("Profit =",difference)

if difference<0:
    print("Loss = ",difference)

if difference==0:
    print("No profit No loss")

print("good bye.")
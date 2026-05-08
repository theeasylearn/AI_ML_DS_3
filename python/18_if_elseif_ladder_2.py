'''
    write a program to findout person obesity level using BMI(body to mass index) technique.
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    bmi = weight(Kg ) / (height_in_meter * height_in_meter)
    obesity level 
        Underweight: BMI less than 18.5
        Normal: BMI between 18.5 to 24.9
        Overweight: BMI between 25.0  29.9
        Obese: BMI between 30.0  34.9
        Extremely Obese: BMI 35.0 and above
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into meter 
    3   calculate BMI 
    4   calculate & display person obesity level
'''
weight = float(input("Enter your weight"))
print("Enter your height in foot & inches")
foot = int(input("Enter only foot")) #5
inch = int(input("Enter only remaining inch")) # 7
#convert foot and inches into total inches 
total_inches = (foot * 12) + inch
print(total_inches)
#calculate meter 
meter = total_inches /39.37
#calculate BMI 
bmi = weight / (meter * meter)
print(bmi)




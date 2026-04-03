#how to compare two date object to figure out which date is bigger or smaller 
#write a program to accept 2 person birth detail (day,month,year) & findout elder person & gap in days between 2 person age 
import datetime as dt 
import math 
#accept date from user 
name_1 = input("Enter 1st person name")
print("Enter birth date as per instruction")
day = int(input("Enter day part of birthdate"))
month = int(input("Enter month part of birthdate"))
year = int(input("Enter year part of birthdate"))

#create date object 
birthdate_1 = dt.date(year,month,day)
print(birthdate_1) #print date in YY-MM-DD

name_2 = input("Enter 2nd person name")
print("Enter birth date as per instruction")

day = int(input("Enter day part of birthdate"))
month = int(input("Enter month part of birthdate"))
year = int(input("Enter year part of birthdate"))

#create date object 
birthdate_2 = dt.date(year,month,day)
print(birthdate_2) #print date in YY-MM-DD

#compare date object to figure out elder person
if birthdate_1<birthdate_2:
    print(f"{name_1} is elder person")
else:
    print(f"{name_2} is elder person")


#gap calculate between date object
gap = birthdate_1 - birthdate_2
print("Gap in days ",math.fabs(gap.days))
years = math.ceil(math.fabs(gap.days)) // 365
print("Gap in years ",years)

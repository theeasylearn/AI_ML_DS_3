#create date object using user given day,month & year of his/her birthdate
import datetime as dt 

#accept date from user 
print("Enter your birth date as per instruction")
day = int(input("Enter day part of birthdate"))
month = int(input("Enter month part of birthdate"))
year = int(input("Enter year part of birthdate"))

#create date object 
birthdate_1 = dt.date(year,month,day)
print(birthdate_1) #print date in YY-MM-DD
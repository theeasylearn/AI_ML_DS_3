#working with string 
name = "the easylearn academy"
city = " Bhavnagar"
pincode = 364001
print(name)
print(name[0:3])  #the 
print(name[4:13]) #easylearn
print(name[14:]) #academy
print(name[4]) # e
print(name*3) #it will print name variable's value 3 times
print(name+city) #when we use + with 2 string, it(+) will join both string
# print(city+pincode) one variable is string and one is integer, python do not allow to use + operator on different type of value
print(city+str(pincode))
print(city,pincode)
# city[0] = "B" #won't work because we can not change part of the string (immutable)
print("Good bye")
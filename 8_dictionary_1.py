#create dictionary using {} braces
student =  {
            "name":"yash",
            "surname":"joshi",
            "age":21,
            "weight":50.99,
            'gender':True,
            'car':None
            }
print(student)

#print only name 
print(student['name']) #yash

#print age
print(student['age']) #21

#update age
student['age'] = 24

#it will create new key value pair if key does not exists
student['city'] = "Bhavnagar"
print(student)

#delete key city and it's value
del student['city']
print(student)
# dictionary related method
teacher = {"id":1,"name":"Ankit","surname":"patel","age":40,"gender":True,"weight":85.20,"email":"ankit3385@gmail.com"}
print(teacher)

#get all keys 
print(teacher.keys())

#get all values 
print(teacher.values())

#let us remove key value pair 
teacher.pop('id')

print(teacher)

teacher.popitem()
print(teacher)

#update exsiting key value pair 
teacher.update({'age':41})

#if key value pair does not exists, key value pair will be added into dictionary
teacher.update({'city':'bhavnagar'})

print(teacher)

# print(teacher['state']) #dont use this technique as it will cause run time error if key does not exist
print(teacher.get('state')) #return None because state key does not exists
print(teacher.get('city')) #return bhavnagar because city key does exists.

#create list which has keys for dictionary to be created 
team = ['name','captain','no_of_world_cup','logo','valuation']
print(team)

#it will create new dictionary which will have keys 'name','captain','no_of_world_cup','logo','valuation' all keys has value None
team_india = dict.fromkeys(team)
team_england = dict.fromkeys(team)

print(team_india)
print(team_england)

team_india['name'] = "India"
team_india['captain'] = "Shubhnam Gill"
team_india['no_of_world_cup'] = 2

team_england['name'] = "England"
team_england['captain'] = "someone"
team_england['no_of_world_cup'] = 1

print(team_india)
print(team_england)

#clear method will remove all key value pairs, dictionary will be empty
team_india.clear()
team_england.clear()

print(team_india)
print(team_england)

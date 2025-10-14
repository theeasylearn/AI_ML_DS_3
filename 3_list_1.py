#1st example of list
teams = ['India','Australia','England','South Afferica','newz land','sri lanka','west indies','Bangladesh','Afghanistan',100,False,3.14]
#          0       1           2           3               4               5           6
print(teams) #display list
print(teams[0]) #india
print(teams[1]) #Australia
print(teams[3]) #South Afferica
print(teams[5]) # sri lanka

#replace 1st item with bharat
teams[0] = "Bharat"
teams[2] = "UK"
print(teams)

#delete 2nd item in list 
del teams[1]
print(teams)

#display 1st 2 items/elements/values 
print(teams[0:2])
#display all items from 3rd position onwards
print(teams[3:])

print(teams*2)

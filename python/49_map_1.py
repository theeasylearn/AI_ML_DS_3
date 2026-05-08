#working with map function 
list1 = [7, 23, 45, 12, 89, 34, 56, 9, 67, 28]
list2 = [14, 62, 5, 91, 38, 27, 74, 8, 49, 66]
print(list1)
print(list2)

#generate qube of list 1 into qube 
qube = map(lambda number: number*number*number,list1)
print(list(qube))


#generate difference between list1 and list2
difference = map(lambda num1,num2: num1-num2,list1,list2)
print(list(difference))

#task different list into positive list 

#findout max value from list1 and list2 (compare each item list)
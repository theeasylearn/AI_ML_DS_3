#list related methods 
#create empty list 
basket = [] 
print(basket) # []

#insert 3 items at the end of list
basket.append('toys') # ['toys']
basket.append(100) # ['toys',100]
basket.append(True) # ['toys',100,True]
print(basket)

#insert 2 items at the begining
basket.insert(0,'apple') # ['apple','toys',100,True]
basket.insert(0,'orange') # ['orange','apple','toys',100,True]
print(basket)

#insert 1 items at the 2nd position
basket.insert(1,'Potato') # ['orange','potato','apple','toys',100,True]
print(basket)

#create another list 
box = ['Ring','breslet']
#add box (list) into basket (list) means merge box into basket
basket.extend(box)
print(basket)

#delete value 'toys'
basket.remove('toys') # ['orange','potato','apple',100,True,'Ring','breslet']
# basket.remove('bat') # this will not remove any item becasue item does not exists
print(basket)

#delete item at 1st position
basket.pop(1) #['orange','apple',100,True,'Ring','breslet']
print(basket)

#delete all items from list 
basket.clear() # []
print(basket)
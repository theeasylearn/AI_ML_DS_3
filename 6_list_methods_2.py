#list related methods 
recipes = ["Palak Paneer", "Chole Bhature", "Masala Dosa", "Aloo Gobi", "Baingan Bharta", "Paneer Butter Masala", "Dal Tadka", "Vegetable Biryani", "Kadhi Pakora", "Malai Kofta","Dal Tadka"]
print(recipes)
#sort list into ascending order
recipes.sort()
print("list after sorting.....")
print(recipes)

#reverse list 
recipes.reverse()
print("list in reverse (descending) ....")
print(recipes)

item = "Chole Bhature"
#findout position of "Chole Bhature" in recipes 
print(recipes.index(item))

item = "Dhokla"
#findout position of "Dhokla" in recipes 
# print(recipes.index(item)) # will raise exception and program will terminate 

#count "Dal Tadka"
print("Dal Tadka is no of items",recipes.count("Dal Tadka"))

numbers = [10,20,30]

#wrong of copy list 
# copy_numbers = numbers 

#perfect way to copy list 
copy_numbers = numbers.copy()
print("numbers ",numbers)
print("copy_numbers ",numbers)

numbers.clear() #delete all items from numbers 
print("after deleting all values from numbers")
print("numbers ",numbers)
print("copy_numbers ",copy_numbers)

print("Good bye")
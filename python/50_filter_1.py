#working with map function 
list1 = [7, 23, 45, 12, 89, 34, 56, 9, 67, 28]

#filter odd numbers 
odd = filter(lambda num: num%2==1,list1)
print(list(odd))

countries = ['Finland', 'Iceland', 'Ireland', 'Thailand', 'Poland', 'England', 'Switzerland', 'New Zealand', 'Scotland', 'Russia', 'Indonesia', 'Malaysia', 'Tunisia', 'India', 'Canada', 'Brazil', 'Japan', 'France', 'Italy', 'Australia']

#filter countries with ends with land
countries2 = filter(lambda item: 'land' in item,countries)
print(list(countries2))

#task filter counteries that ends with asia


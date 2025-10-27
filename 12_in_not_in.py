countries = ['USA', 'China', 'India', 'Brazil', 'Russia', 'Japan', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'Australia', 'Mexico', 'Spain', 'South Korea', 'Indonesia', 'Nigeria', 'South Africa', 'Egypt', 'Argentina']

country = input("where are you from?")

isFound = country in countries
print(isFound) # True or False

isNotFound = country not in countries
print(isNotFound) # True or False

vegetables = "potato tomato onion garlic cauliflower spinach okra brinjal cabbage carrot radish beetroot bitter gourd pumpkin green beans peas drumstick yam bottle gourd ridge gourd"

favourite = input("Which your favourite vegetables")
isFound = favourite in vegetables
print(isFound)

isNotFound = favourite not in vegetables

print(isNotFound)

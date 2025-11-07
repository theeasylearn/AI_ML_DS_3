# using for loop with string
# count no of letters, words, vowels 
line = "Quick zebra jumps over lazy 3 dogs at Delhi park around 12:30 pm near cage no 5 @ visitor day"
count = 0
word = 1
vowels = 0
list = ['a','e','i','o','u','A','E','I','O','U']

for letter in line:
    count+=1
    if letter == ' ':
        word+=1
    elif letter in list:
        vowels+=1
print(f"no of letters = {count}")
print(f"no of words = {word}")
print(f"no of vowels = {vowels}")
# count digits also count symbols (any letter other then space,alphabets and digits)

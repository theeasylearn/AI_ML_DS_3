import re 
#extract only words (not digits)
text ="Hello my name is ankit. i am year 40 year old i am having 2 wheels"
line = re.sub(r'[0-9]',"",text)
print(line)

#extract only digits (not digits)
text ="Hello my name is ankit. i am year 40 year old i am having 2 wheels"
line = re.findall(r'[0-9]',text)
print(line)

#extract only amount (not digits)
text ="Hello my name is ankit. i am year 40 year old i am having 2 wheels"
line = re.findall(r'[0-9]{1,}',text)
print(line)

text ="1kg, 2kg, 5kg and weight units in india"
line = re.findall(r'[0-9]{1,}kg',text)
print(line)

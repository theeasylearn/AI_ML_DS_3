'''
    create tuple
    
    [] brackets
    {} braces 
    () parenthesis 
    <> angular brackets
'''
mixed = (42, 3.14, "Hello", True, None, False)
print(mixed)
print(mixed[0]) # 42
print(mixed[1]) # 3.14
print(mixed[0:2]) # 42, 3.14
print(mixed[2:]) #"Hello", True, None, False
# del mixed[0] #delete item from tuple
# mixed[0] = 100 # because tuple is read onlye
print("True = ",mixed.count(True))
print("Hello = ",mixed.index("Hello"))
print("good bye")
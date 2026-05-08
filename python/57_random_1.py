import random as rd #here i have assigned rd alias to random module, means now i will rd word for random module 
print("random number between 0 and 1",rd.random())
print("random number between 1.0 and 100.0",rd.uniform(1,100))
print("random number between 1 and 100",rd.randint(1,100))
print("random number between 1 and 100 step value 10",rd.randrange(1,100,10))

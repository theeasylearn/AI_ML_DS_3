#for loop with dictionary
players = {"Rohit":78, "Gill":45, "Kohli":92, "Iyer":36, "Rahul":58, "Hardik":24, "Jadeja":41, "Ashwin":15, "Shami":10, "Bumrah":5, "Siraj":8}
#findout total team score
total=0
for key in players:
    print(f"{key} = {players[key]}")
    total = total + players[key]

print(f"total runs = {total}")

#findout average run made by each player 
#findout average run made by 1st five player
#findout which player name & his runs who maximum runs 
#findout which player name & his runs who minimum runs 


#concept of set in python 
#set means one type of mutable list which do not allows duplicate value and do not give value in same sequence as inserted 

#create set using braces {} 
team1 = {'Rohit Sharma', 'Shubman Gill', 'Virat Kohli', 'Shreyas Iyer', 'KL Rahul', 'Suryakumar Yadav', 'Ravindra Jadeja', 'Mohammed Shami', 'Jasprit Bumrah', 'Kuldeep Yadav', 'Mohammed Siraj'}

team1.add('Sachin Tendulkar') # will be added 
team1.add('Virat Kohli') #will not be added because it is already in team1

#create another set 
team2 = {'Rohit Sharma', 'Virat Kohli', 'Rishabh Pant', 'Suryakumar Yadav', 'Axar Patel', 'Shivam Dube', 'Hardik Pandya', 'Ravindra Jadeja', 'Arshdeep Singh', 'Kuldeep Yadav', 'Jasprit Bumrah'}


print(team1)
print(team2)

unique_players = team1.union(team2)
print(unique_players)

common_players = team1.intersection(team2)
print(common_players)

droped_players = team1.difference(team2)
print(droped_players)
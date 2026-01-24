import matplotlib.pyplot as plt 
# Sequential runs scored in each over: 1st over to 16th over (partial)
y = [6, 4, 18, 12, 22, 15, 9, 14, 11, 21, 8, 13, 24, 16, 11, 5]
x = list(range(1,17)) # return python list which has 1 to 20
# print(y,x)
plt.plot(x,y)
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('India Vs Newzland (2nd T20 match)')
plt.show()
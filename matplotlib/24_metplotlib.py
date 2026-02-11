from matplotlib import pyplot as plt 
import numpy as np 

x = np.linspace(0,10,10)
y = np.sin(x)
error = 0.3 #set the height of bar less value means less height
plt.errorbar(x,y,yerr=error,ecolor='red',fmt='^')
plt.xlabel('X')
plt.ylabel("Y")
plt.title("errorbar chart")
plt.grid(True)
plt.show()
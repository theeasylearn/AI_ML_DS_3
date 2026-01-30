import matplotlib.pyplot as plt 
import numpy as np 
data = np.random.normal(0,1,1000)
print(data)
plt.hist(data,bins=20,density=False,color='orange',label='Data')
plt.xlabel('data')
plt.ylabel('hike')
plt.title('example of histogram chart')
plt.grid(True)
plt.show()
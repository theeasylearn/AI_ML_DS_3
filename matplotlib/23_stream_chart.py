from matplotlib import pyplot as plt 
import numpy as np 
x_label = np.linspace(-2,2,10)
y_label = np.linspace(-2,2,10)
X,Y = np.meshgrid(x_label,y_label)
plt.streamplot(x_label,y_label,-Y,X,color='red',density=1,linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('stream chart')
plt.grid(True)
plt.show()
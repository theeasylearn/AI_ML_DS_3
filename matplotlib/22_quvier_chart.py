from matplotlib import pyplot as plt 
import numpy as np 
x = np.linspace(-2,2,10)
y = np.linspace(-2,2,10)
X,Y = np.meshgrid(x,y)
U = -Y 
V = X 
plt.quiver(x,y,U,V,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quiver chart')
plt.grid(True)
plt.show()
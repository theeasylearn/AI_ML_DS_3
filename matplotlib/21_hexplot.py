import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)
plt.hexbin(x, y, gridsize=20, cmap='Blues')
plt.colorbar(label='Counts')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hexbin Plot')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 3000)
y = np.random.normal(3, 4, 3000)

plt.scatter(x, y, s=50, c='red', alpha=0.5, marker='.')
plt.xlabel('x')

plt.ylabel('y')

plt.title('Scatter Plot')

plt.grid(color='gray', linestyle='dotted')
plt.show()
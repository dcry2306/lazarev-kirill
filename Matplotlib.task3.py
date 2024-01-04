import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(16, 2, 1000)

bins = 20

fig, ax = plt.subplots()

ax.hist(data, bins, facecolor='red',alpha=0.5)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

def my_function(x):
    return (x**3 + 2*x**2 - 7*x + 5)/(x**2 + 2)

x = np.linspace(-10, 10, 100)
y = [my_function(i) for i in x]

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='green', linestyle='dashed', alpha=0.5, label='Вот такая моя функция')
plt.grid()
plt.xlabel('X-координаты')
plt.ylabel('Y-координаты')
plt.title('График функции')
plt.legend()

plt.tight_layout()
plt.show()
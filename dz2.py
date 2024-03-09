import matplotlib.pyplot as plt

lr = 0.01
w1 = 0
w0 = 0
x = [1, 3, 7]
y = [2, 6, 14]

for i in range(len(x)):
    predict = w1 * x[i] + w0
    w1 += 2 * lr * x[i] * (y[i] - predict)
    w0 += 2 * lr * (y[i] - predict)
    
print(f'w0 = {w0}, w1 = {w1}')

plt.scatter(x,y)
plt.plot(x, [w1 * x + w0 for x in x], color = 'black')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print('Вывод: веса похожи на настоящие')
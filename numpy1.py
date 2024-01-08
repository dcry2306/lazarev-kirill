import numpy as np

#Задача 1

arr = np.random.randint(1, 11, size=100)
percent = np.mean(arr > 7) * 100

print("Процент элементов вектора, больших 7:", percent)

#Задача 2

results = []
for _ in range(1000):
    arr = np.random.randint(1, 11, size=100)
    percent = np.mean(arr > 7) * 100
    results.append(percent)

equal_20_percent = np.mean(np.array(results) == 20)
print("Часть результатов, равных 20%:", equal_20_percent)

#Задача 3

matrix = np.tile(np.arange(1, 11), (10, 1))
print(matrix)

#Задача 4

column_sums = np.sum(matrix, axis=0)
print(column_sums)
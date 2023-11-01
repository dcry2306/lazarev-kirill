from functools import reduce

numbers = input()
numbers = list(map(int,numbers))


print(reduce(lambda a, b: a if a > b else b, numbers))
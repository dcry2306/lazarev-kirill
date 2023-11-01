list1 = input().split()
list2 = input().split()
result = list(map(lambda x, y: x + y, list1, list2))
print(result)
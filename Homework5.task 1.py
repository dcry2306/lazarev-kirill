n = int(input())
list = []
repeat = []
count = 0
for i in range(n):
    name = input()
    list.append(name)
for i in list:
    if list.count(i) > 1 and i not in repeat:
        count += 1
print(count)


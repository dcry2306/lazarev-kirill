num = input()
n = int(input())
list = num.split()
list2 = []
for i in range(len(list)):
    list[i] = int(list[i])
list2 = [i ** n for i in list]
print(list2)


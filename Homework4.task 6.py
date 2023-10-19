string = input('Введите текст: ') 
list = []
a = string.find('(')
while a != -1:
    b = string.find(')', a+1 )
    if b != -1:
        list.append(string[a+1:b])
    a = string.find('(', a+1)

list2 = "\n".join(list)
print(list2)




    
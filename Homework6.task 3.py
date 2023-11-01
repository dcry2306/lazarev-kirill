def maximum(num1,num2,num3=None):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число(если его нет, введите 0): '))
if num3 == 0:
    num3 == None
print('Максимально число: ',maximum(num1,num2,num3))

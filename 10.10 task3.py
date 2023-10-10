num1 = int(input('Введите номер столбца '))
num2 = int(input('Введите номер строки '))
if num1 % 2 == 0 and num2 % 2 != 0:
    print('YES')
else:
    print('NO')
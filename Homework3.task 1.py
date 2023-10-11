num = int(input('Введите число '))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print('Сумма цифр:', sum)
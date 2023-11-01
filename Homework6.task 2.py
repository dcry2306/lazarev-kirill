def inf(name, last_name, patronymic, age, ):
    full_name = f'"{name} {last_name} {patronymic} {age} г.р зарегистрирован".'
    return full_name
print(inf(input('Введите имя: '),input('Введите фамилию:'),input('Введите отчество: '),input('Введите год рождения: ')))
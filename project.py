import random
def draw_board(field):
    print("y")
    print("↑")
    print("3  " + field[0] + ' │ ' + field[1] + ' │ ' + field[2])
    print("2  " + field[3] + ' │ ' + field[4] + ' │ ' + field[5])
    print("1  " + field[6] + ' │ ' + field[7] + ' │ ' + field[8])
    print("   1   2   3 → x")
    print("---------------\n")

def get_player_move(player_symbol, field):
    x = int(input("Введите x координату: "))
    y = int(input("Введите y координату: "))
    while True:
        if (x not in [1, 2, 3]) or (y not in [1, 2, 3]):
            print("некорректный ввод, попробуйте ещё раз")
            x = int(input("Введите x координату: "))
            y = int(input("Введите y координату: "))
        elif field[(3 - y) * 3 + x - 1] != '-':
            print("сюда уже сходили, попробуйте ещё раз")
            x = int(input("Введите x координату: "))
            y = int(input("Введите y координату: "))
        else:
            break

    field[(3 - y) * 3 + x - 1] = player_symbol
    return field

def get_computer_move(compyter_symbol, field):
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    while True:
        if field[(3 - y) * 3 + x - 1] != '-':
            x = random.randint(1, 3)
            y = random.randint(1, 3)
        else:
            break

    field[(3 - y) * 3 + x - 1] = compyter_symbol
    return field

def check_win(field): # возвращает x, если победил крестик, 0, если нолик и -, если пока никто, = - ничья
    if field[0] == field[1] == field[2] and field[0] != '-':
        return field[0]
    if field[3] == field[4] == field[5] and field[3] != '-':
        return field[3]
    if field[6] == field[7] == field[8] and field[6] != '-':
        return field[6]

    if field[0] == field[3] == field[6] and field[0] != '-':
        return field[0]
    if field[1] == field[4] == field[7] and field[1] != '-':
        return field[1]
    if field[2] == field[5] == field[8] and field[2] != '-':
        return field[2]

    if field[0] == field[4] == field[8] and field[0] != '-':
        return field[0]
    if field[2] == field[4] == field[6] and field[2] != '-':
        return field[2]

    if '-' not in field:
        return '='
    else:
        return '-'

def main():
    symbols = ['✕', 'O']
    player_idx = random.randint(0, 1)
    player_symbol = symbols[player_idx]
    compyter_symbol = symbols[1 - player_idx]
    print("Вы будете ходить " + player_symbol)

    field = ['-'] * 9 # создает пустое поле
    if player_symbol == 'O':
        get_computer_move(compyter_symbol, field)
    draw_board(field)

    while True:
        get_player_move(player_symbol, field) # игрок ходит
        check_win_response = check_win(field) # получаем ответ о статусе партии
        if check_win_response == player_symbol: # расшифровываем
            print("Вы победили!!!")
            break
        elif check_win_response == compyter_symbol:
            print("Победил компьютер!!!")
            break
        elif check_win_response == '=':
            print("Ничья")
            break

        get_computer_move(compyter_symbol, field) # ход компьютера
        draw_board(field) # рисуем поле
        check_win_response = check_win(field) # получаем ответ о статусе партии
        if check_win_response == player_symbol: # расшифровываем
            print("Вы победили!!!")
            break
        elif check_win_response == compyter_symbol:
            print("Победил компьютер!!!")
            break
        elif check_win_response == '=':
            print("Ничья")
            break

main()
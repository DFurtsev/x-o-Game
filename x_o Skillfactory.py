table = [
    [0, 1, 2, 3]
    ,[1, "_", "_", "_"]
    ,[2, "_", "_", "_"]
    ,[3, "_", "_", "_"]
]
valid_coordinates = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
def result():
    win_combination = [(table[1][1], table[1][2], table[1][3]),
                       (table[2][1], table[2][2], table[2][3]),
                       (table[3][1], table[3][2], table[3][3]),
                       (table[1][1], table[2][1], table[3][1]),
                       (table[1][2], table[2][2], table[3][2]),
                       (table[1][3], table[2][3], table[3][3]),
                       (table[1][1], table[2][2], table[3][3]),
                       (table[3][1], table[2][2], table[1][3])]
    o_win = ("o", "o", "o")
    x_win = ("x", "x", "x")
    if o_win in win_combination or x_win in win_combination:
        return True

def print_table():
    for i in range(len(table)):
        for j in range(len(table)):
            print(table[i][j], end='|')
        print()
    print()


print("Чтобы прервать игру, введите 0.\nВ игре используется EN раскладка!\n")
print_table()
count = 0
while True:
    if count%2 == 0:
        print("Ходит крестик")
    else:
        print("Ход нолик")
    adress = input('Введите координаты без пробелов\n')
    if adress not in valid_coordinates:
        print("Необходимо ввести корректные коодинаты. Ход начат заново.\n")
        continue
    coordinate = [int(i) for i in adress]
    if table[coordinate[0]][coordinate[1]] != "_":
        print('Ячейка уже занята, выберите свободную. Ход начат заново.\n')
        continue
    if count%2 == 0:
        table[coordinate[0]][coordinate[1]] = "x"
    else:
        table[coordinate[0]][coordinate[1]] = "o"
    print_table()
    count+=1
    if result():
        print("Игра окончена")
        break
    if count == 9:
        print("Ничья. Игра окончена.")
        break
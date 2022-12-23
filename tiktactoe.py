def greet():
    print("---------------------------------------------")
    print('  Добро пожаловать в игру "Крестики-нолики"  ')
    print("---------------------------------------------")
    print('Фомат ввода: x y, где x - строка, y - столбец')

def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print("  ---------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ---------------")
    print()
def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Ход должен состоять из 2х координат! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа от 0 до 2! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Ход вне диапазона игрового поля! Выберите другую клетку. ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! Выберите другую клетку.")
            continue

        return x, y

def win_check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print(" Выиграл крестик!!! ")
            return True
        if symbols == ["O", "O", "O"]:
            show()
            print(" Победил нолик!!! ")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num %2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if num %2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if win_check():
        break

    if num == 9:
        break
        print(" Ничья ")
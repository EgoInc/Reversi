def is_int(str):  # Эта фигня нужна для проверки ввода потом
    try:
        int(str)
        return True
    except ValueError:
        print('Указанное не является числом')
        return False


def opposite(number):
    if number == 1:
        return 2
    return 1


def draw(Field):
    for i in range(8):
        print(Field[i])


def recolor(Field, x, y, sign, number):
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
    for dir in directions:
        if Field[x + dir[0]][y + dir[1]] == 'x':
            pass
        else:
            maybe = []
            nx = x + dir[0]
            ny = y + dir[1]
            while Field[nx][ny] != 'x' and Field[nx][ny] != sign:
                maybe.append([nx, ny])
                nx += dir[0]
                ny += dir[1]
            if Field[nx][ny] == sign and len(maybe) != 0:
                for each in maybe:
                    Field[each[0]][each[1]] = sign
                    calculator[number] += 1
                    calculator[opposite(number)] -= 1


class Player:
    def __init__(self, number, sign):
        self.sign = sign
        self.number = number

    def move(self):

        def is_close(x, y):
            options = ((x - 1, y - 1), (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1), (x + 1, y + 1), (x - 1, y + 1),
                       (x + 1, y - 1))
            for each in options:
                if Field[each[0]][each[1]] == 1 or Field[each[0]][each[1]] == 0:
                    return True
            print('Выбранная клетка должна быть рядом с уже занятой')
            return False

        check = False
        while not check:
            x, y = input('Стартовая позиция: 1-8,где первое число строка, второе столбец. Например: "1 1"').split()
            if is_int(x) and is_int(y):
                if Field[int(x) - 1][int(y) - 1] == 'x':
                    if is_close(int(x) - 1, int(y) - 1):
                        Field[int(x) - 1][int(y) - 1] = self.sign
                        calculator[self.number] += 1
                        calculator[0] -= 1
                        recolor(Field, int(x) - 1, int(y) - 1, self.sign, self.number)
                        check = True
                        print("Счёт: 1ый игрок -", calculator[1], ", 2ой игрок - ", calculator[2])
                else:
                    print("Данная клетка уже занята")


if __name__ == '__main__':
    Field = [['x'] * 8 for i in range(8)]
    Field[3][3] = Field[4][4] = 1
    Field[3][4] = Field[4][3] = 0
    calculator = [60, 2, 2]
    draw(Field)
    first_player = Player(1, 1)
    second_player = Player(2, 0)
    turn = 1
    while calculator[0] != 0:
        if turn % 2 == 1:
            first_player.move()
        elif turn % 2 == 0:
            second_player.move()
        draw(Field)
        turn += 1

    if calculator[1] > calculator[2]:
        print("Победил 1ый игрок")
    elif calculator[1] < calculator[2]:
        print('Победил 2ой игрок')
    elif calculator[1] == calculator[2]:
        print('Ничья')
        
# self.gridLayout = QtWidgets.QGridLayout(self.widget3)
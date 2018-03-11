import copy
import random

def read_field(path):
    field = dict()
    with open(path, 'r', encoding='utf-8') as f:
        ship = []
        numb = 1
        for line in f:
            letter = 0
            while len(line) < 10:
                line += ' '
            for elem in line:
                coor = chr(letter + 97) + str(numb)
                if elem == '\n':
                    elem = ' '
                field[coor] = elem
                letter += 1
            numb += 1

    return field


def has_ship(field, coordinate):
    coordinate2 = str(coordinate[0] + str(coordinate[1]))
    if type(field) == dict:
        if field[coordinate2] == '*':
            return True
    else:
        if coordinate in field:
            return True
    return False


def ship_size(field, coordinate):
    only_ships = dict()
    length = 0
    if has_ship(field, coordinate):
        for key in field:
            if field[key] == '*':
                only_ships[key] = field[key]

        if len(coordinate) > 2:
            coordinate = list(coordinate)
            coordinate2 = []
            coordinate2.extend(
                [coordinate[0], str(coordinate[1] + coordinate[2])])
            coordinate = copy.copy(coordinate2)
        else:
            coordinate = list(coordinate)
        i = 0
        while True:
            try:
                while only_ships[
                    str(chr(ord(coordinate[0]) - i) + coordinate[1])] == '*':
                    length += 1
                    i += 1
            except KeyError:
                i = 1
                try:
                    while only_ships[str(
                                    chr(ord(coordinate[0]) + i) + coordinate[
                                1])] == '*':
                        length += 1
                        i += 1
                except KeyError:
                    break
        i = 1
        while True:
            try:
                while only_ships[str(chr(ord(coordinate[0])) + str(
                                int(coordinate[1]) - i))] == '*':
                    length += 1
                    i += 1
            except KeyError:
                i = 1
                try:
                    while only_ships[str(chr(ord(coordinate[0])) + str(
                                    int(coordinate[1]) + i))] == '*':
                        length += 1
                        i += 1
                except KeyError:
                    break
    return length


def is_valid(field):
    only_ships = dict()
    if len(field) != 100 or len(only_ships) != 20:
        return False

    return True


def frame(field, ship):
    border = []
    new_field = []
    for cell in ship:
        border.append((chr(ord(cell[0]) - 1), cell[1] - 1))
        border.append((chr(ord(cell[0])), cell[1] - 1))
        border.append((chr(ord(cell[0]) + 1), cell[1] - 1))
        border.append((chr(ord(cell[0]) + 1), cell[1]))
        border.append((chr(ord(cell[0]) + 1), cell[1] + 1))
        border.append((chr(ord(cell[0])), cell[1] + 1))
        border.append((chr(ord(cell[0]) - 1), cell[1] + 1))
        border.append((chr(ord(cell[0]) - 1), cell[1]))
    for i in border:
        if i in ship:
            border.remove(i)
    for cell in border:
        for line in field:
            if cell in line:
                line.insert(line.index(cell), ' ')
                line.remove(cell)
    return field


def generate_field():
    field = []
    for numb in range(1, 11):
        line = []
        for letter in range(10):
            coor = tuple([chr(letter + 97), numb])
            line.append(coor)
        field.append(line)
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for ship in ships:
        size = 0
        way = ['horizontal', 'vertical']
        what_line = random.choice(field)
        point = random.choice(what_line)
        what_way = random.choice(way)
        new_field = copy.copy(field)
        while True:
            try:
                if what_way == 'vertical':
                    while point == "*" or point == ' ' or point[1] + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    delete = []
                    while size != ship:
                        what_line.insert(what_line.index(point), '*')
                        delete.append(point)
                        what_line.remove(point)
                        point = [point[0], point[1] + 1]
                        point = tuple(point)
                        what_line = field[point[1] - 1]
                        size += 1
                    field = frame(field, delete)
                else:
                    while point == "*" or point == ' ' or ord(point[0]) - 97 + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    delete = []
                    while size != ship:
                        what_line.insert(what_line.index(point), '*')
                        delete.append(point)
                        what_line.remove(point)
                        point = [chr(ord(point[0]) + 1), point[1]]
                        point = tuple(point)
                        size += 1
                    field = frame(field, delete)
            except:
                generate_field()
            break
    print()
    norm_field = []
    for line in field:
        new_line = []
        for elem in line:
            if elem != '*':
                new_line.append(' ')
            else:
                new_line.append('*')
        print(new_line)


def main():
    field = read_field('field.txt')
    # print(field)
    # print(has_ship(field, ("b1")))
    # print(ship_size(field, "j10"))
    # print(is_valid(field))
    generate_field()



main()

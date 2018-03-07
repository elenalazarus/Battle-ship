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
    if field[coordinate] == '*':
        return True
    else:
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
    for key in field:
        if field[key] == '*':
            only_ships[key] = field[key]
    if len(field) != 100 or len(only_ships) != 20:
        return False

    return True



def generate_field():
    field = []
    delete = []
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
        while True:
            try:
                if what_way == 'vertical':
                    while point == "*" or point == ' ' or point[1] + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    while size != ship:
                        what_line.insert(what_line.index(point), '*')
                        delete.append(point)
                        point = [point[0], point[1] + 1]
                        point = tuple(point)
                        what_line = field[point[1] - 1]
                        size += 1
                else:
                    while ord(point[0]) - 97 + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    while size != ship:
                        what_line.insert(what_line.index(point), '*')
                        delete.append(point)
                        point = [chr(ord(point[0]) + 1), point[1]]
                        point = tuple(point)
                        size += 1
            except IndexError:
                continue
            break
    for line in field:
        print(line)




def main():
    field = read_field('field.txt')
    # print(field)
    # print(has_ship(field, ("b1")))
    # print(ship_size(field, "j10"))
    print(is_valid(field))
    print(generate_field())


main()

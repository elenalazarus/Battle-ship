import copy
import random


def read_field(path):
    '''
    Read field from txt file and return dictionary with all coordinates
    :param path: str
    :return: dict
    '''
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
    '''
    Check if coordinate which was put is a ship
    :param field: dict
    :param coordinate: str
    :return: True or False
    '''
    coordinate2 = str(coordinate[0] + str(coordinate[1]))
    if type(field) == dict:
        if field[coordinate2] == '*':
            return True
    else:
        if coordinate in field:
            return True
    return False


def ship_size(field, coordinate):
    '''
    Check if coordinate which was put is a ship and return the length of a ship
    :param field: dict
    :param coordinate: str
    :return: int
    '''
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
                while only_ships[str(
                                     chr(ord(coordinate[0]) - i) +
                                 coordinate[1])] == '*':
                    length += 1
                    i += 1
            except KeyError:
                i = 1
                try:
                    while only_ships[str(
                                         chr(ord(coordinate[0]) + i) +
                                     coordinate[1])] == '*':
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
    '''
    Check if a field is valid for battleship
    :param field: dict
    :return: True or False
    '''
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    try:
        for ship in field:
            if len(ship) in ships:
                ships.remove(len(ship))
        if len(ships) == 0:
            return True
    except:
        return False


def frame(field, ship):
    '''
    Return all coordinates around the ship in the field
    :param field: list
    :param ship: list
    :return: list
    '''
    border = []
    for cell in ship:
        for i in {-1, 0, 1}:
            for k in {-1, 0, 1}:
                border.append((chr(ord(cell[0]) + i), cell[1] + k))
    for i in set(border):
        if i in ship:
            border.remove(i)
    for cell in border:
        for line in field:
            if cell in line:
                line.remove(cell)
    return field


def generate_field():
    '''
    Field generation
    '''
    shipses = []
    all_ships = []
    field = []
    all_field = []
    for numb in range(1, 11):
        line = []
        for letter in range(10):
            coor = tuple([chr(letter + 97), numb])
            line.append(coor)
            all_field.append(coor)
        field.append(line)
    # Future ships
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for ship in ships:
        size = 0
        way = ['horizontal', 'vertical']
        while True:
            pre_field = copy.copy(field)
            try:
                delete = []
                # Choose the line where we will start a ship
                what_line = random.choice(field)
                if len(what_line) == 0:
                    # If there is no possibility to put a ship
                    while len(what_line) == 0:
                        what_line = random.choice(field)
                point = random.choice(what_line)
                what_way = random.choice(way)
                if what_way == 'vertical':
                    # Check if we cen put a large ship there
                    while point[1] + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    shipses.append([point, ship, False, []])
                    while size != ship:
                        delete.append(point)
                        what_line.remove(point)
                        point = (point[0], point[1] + 1)
                        what_line = field[point[1] - 1]
                        size += 1
                else:
                    while ord(point[0]) - 97 + ship > 10:
                        what_line = random.choice(field)
                        point = random.choice(what_line)
                    shipses.append([point, ship, True, []])
                    while size != ship:
                        delete.append(point)
                        what_line.remove(point)
                        point = (chr(ord(point[0]) + 1), point[1])
                        size += 1
            except:
                field = copy.copy(pre_field)
                continue
            break
        all_ships.append(delete)
        field = frame(field, delete)
    return all_ships, shipses


def field_to_str(all_ships):
    '''
    Output a field for user
    '''
    field = ''
    str_field = []
    for ship in all_ships:
        for coor in ship:
            str_field.append(coor)
    sorted(str_field)
    for i in range(10):
        line = ""
        for k in range(1, 11):
            point = (chr(i + 97), k)
            if point in str_field:
                line += '■'
            else:
                line += "□"
        print(line)
        field += '\n' + line


if __name__ == "__main__":
    all_ships = generate_field()[0]
    while not is_valid(all_ships):
        all_ships = generate_field()[0]
    print(field_to_str(all_ships))

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
    if has_ship(field, coordinate) == True:
        for key in field:
            if field[key] == '*':
                only_ships[key] = field[key]
        coordinate = list(coordinate)
        print(coordinate)
        i = 0
        while True:
            left = str(chr(ord(coordinate[0]) - i) + coordinate[1])
            if left in only_ships:
                length += 1
                i += 1
            else:
                right = str(chr(ord(coordinate[0]) + i) + coordinate[1])
                if right in only_ships:
                    length += 1
                    i += 1
                else:
                    break
    return length


def main():
    field = read_field('field.txt')
    print(field)
    print(has_ship(field, ("b1")))
    print(ship_size(field, "d8"))

main()
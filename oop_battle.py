from battle import generate_field


class Ship:
    def __init__(self, bow, horizontal, length, hit):
        '''
        Initialize a ship
        :param bow: tuple
        :param horizontal: bool
        :param length: int
        :param hit: bool
        '''
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.length = length
        self.__hit = hit[:]
        self.hit = hit[:]


class Field:
    '''
    Initialize a field
    '''

    def __init__(self):
        self.data = generate_field()
        self.field = self.data[1]
        self.ships = []
        self.shipses = []
        # Collectiong all data
        for ship in self.data[0]:
            for elem in ship:
                self.shipses.append(elem)
        self.shots = []
        for ship in self.field:
            ship2 = Ship(ship[0], ship[2], ship[1], ship[3])
            self.ships.append(ship2)
        self.all_field = []
        for numb in range(1, 11):
            for letter in range(10):
                coor = tuple([chr(letter + 97), numb])
                self.all_field.append(coor)

    def shoot_at(self, tupl):
        '''
        Do a shoot in ship
        :param tupl: tuple
        :return: bool
        '''

        if tupl not in self.all_field:
            return False
        for ship in self.ships:
            for i in range(ship.length):
                # Checking for every point in every ship
                if ship.horizontal:
                    point = (chr(ord(ship.bow[0]) + i), ship.bow[1])
                else:
                    point = (chr(ord(ship.bow[0])), ship.bow[1] + i)
                # Return results
                if point == tupl:
                    ship.hit.append(tupl)
                    self.all_field.remove(tupl)
                    print("Yes! There is a ship!")
                    if len(ship.hit) == ship.length:
                        print("Wow! You killed it!")
                    return True
        print("No! You missed!")
        self.all_field.remove(tupl)
        self.shots.append(tupl)

    def field_without_ships(self):
        '''
        Output field that player will use to orient in enemy's field
        '''
        field = ''
        n = 0
        for i in range(1, 11):
            line = ""
            for k in range(10):
                point = (chr(k + 97), i)
                for ship in self.ships:
                    n = 0
                    if point in ship.hit:
                        line += "■"
                        n += 1
                        break
                if point not in self.all_field and n == 0:
                    line += '◯'
                elif point in self.all_field:
                    line += '□'

            print(line)
            field += '\n' + line

    def field_with_ships(self):
        '''
        That's for player to see how enemy acts
        '''
        field = ''
        for i in range(1, 11):
            line = ""
            for k in range(10):
                point = (chr(k + 97), i)
                # Outputing ships and empty spaces with symbols
                if point in self.all_field and point not in self.shipses:
                    line += '□'
                elif point not in self.all_field and point in self.shipses:
                    line += 'x'
                elif point in self.shipses:
                    line += "■"
                elif point not in self.all_field:
                    line += '◯'
            print(line)
            field += '\n' + line

    def win_or_not(self):
        '''
        Consider if there is a winner
        '''
        i = 0
        for ship in self.ships:
            if len(ship.hit) == ship.length:
                i += 1
        if i == 10:
            return True


class Player:
    '''
    Class for initializing a player
    '''
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Player.id
        Player.id += 1

    def read_position(self):
        '''
        Initialize the act of a player
        '''
        try:
            while True:
                coor = input("Input coordinate as in example: a6" + '\n')
                point = (coor[0], int(coor[1:]))
                return point
        except:
            print("Input right data please")


class Game:
    '''
    Let's play!
    '''

    def __init__(self):
        '''
        Initialize two players
        '''
        field1 = Field()
        field2 = Field()
        self.__fields = [field1, field2]
        name1 = input("Enter first player name: ")
        name2 = input("Enter second player name: ")
        player1 = Player(name1)
        player2 = Player(name2)
        self.__players = [player1, player2]
        self.__current_player = 1
        while True:
            # Let's start game!
            if self.__current_player == 1:
                print("Field of {}".format(name1))
                print()
                # Field of player
                field1.field_with_ships()
                print()
                # Field of enemy
                print("Field of {}".format(name2))
                print()
                field2.field_without_ships()
                coor = player1.read_position()
                a = field2.shoot_at(coor)
                # If player make a good shot then he continues
                if a:
                    # If there is no ships he is the winner!
                    if field2.win_or_not():
                        print("YES! {} is winner".format(name1))
                    continue
                else:
                    self.__current_player = 2

            else:
                print("Field of {}".format(name2))
                print()
                field2.field_with_ships()
                print()
                print("Field of {}".format(name1))
                print()
                field1.field_without_ships()
                coor = player2.read_position()
                a = field1.shoot_at(coor)
                if a:
                    if field1.win_or_not():
                        print("YES! {} is winner".format(name2))
                    continue
                else:
                    self.__current_player = 1


def main():
    '''
    A boss
    :return: None
    '''
    game = Game()


main()

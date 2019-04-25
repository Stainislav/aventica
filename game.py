'''
                                        Задание

    В примере описаны сущности для воображаемой игры. Необходимо придумать валидную
    с точки зрения ООП архитектуру для этих сущностей. Важно: не требуется писать логику,
    нужно просто написать имена классов, их публичные методы и связи между ними (можно
    использовать UML или псевдокод).

                                      Правила игры

    Есть игровое поле 5x5. Каждая из клеток на этом поле может быть нейтральной или
    принадлежать одному из двух игроков. Изначально все клетки нейтральные, кроме клеток
    в двух противоположных углах поля - они принадлежат игрокам.

    Игроки по очереди атакуют одну из клеток. При атаке нейтральной клетки она успешно
    захватывается. При атаке клетки, захваченной другим игроком, исход решается броском
    кубиков. Атаковать можно только клетки, находящиеся по соседству с одной из уже
    захваченных клеток. Игра завершается при захвате стартовой клетки соперника или по
    истечении 7 ходов с каждой стороны.


                                    Требования и запуск

    Для работы программы необходим модуль random из стандартной библиотеки Python.
    Для запуска программы вводим в консоли: python3 game.py
    
    Внизу после кода имеется пример использования классов игры.
   
'''


import random

FIRST_PLAYER_ID = 1
SECOND_PLAYER_ID = 2


class Cell:

    def __init__(self, x, y, affiliation=0, start=False):
        self.x = x
        self.y = y
        self.affiliation = affiliation
        self.start = start

    # "Throw a dice" and set an affiliation for a cell.
    def set_affiliation(self):
        player_list = [FIRST_PLAYER_ID, SECOND_PLAYER_ID]
        player = random.choice(player_list)
        self.affiliation = player


class Board:

    def __init__(self, size=5, cell_list=[]):
        self.size = size
        self.cell_list = cell_list

        # Fill a board by cells.
        i = 0
        j = 4
        while j >= 0:
            while i < self.size:
                x = i
                y = j
                cell = Cell(x, y)
                self.cell_list.append(cell)
                i = i + 1
            i = 0
            j = j - 1

        # Set start cells.
        for cell in self.cell_list:
            cell = self.get_cell(0, 4)
            cell.affiliation = FIRST_PLAYER_ID
            cell.start = True
            cell = self.get_cell(4, 0)
            cell.affiliation = SECOND_PLAYER_ID
            cell.start = True

    def get_cell(self, x, y):
        for cell in self.cell_list:
            if cell.x == x and cell.y == y:
                return cell

    def draw(self):
        length = len(self.cell_list)
        size = self.size

        counter = 0
        while counter < length:
            for i in range(size):
                cell = self.get_cell(self.cell_list[counter].x,
                                     self.cell_list[counter].y)

                print("[ " + str(cell.affiliation) + " ] ", end='')
                counter += 1
            print()
        print()

    def get_neighbors(self, cell):
        neighbor_list = []

        # Get neighbor cells on a y-axis.
        x = cell.x
        y = cell.y + 1
        new_cell = self.get_cell(x, y)
        neighbor_list.append(new_cell)

        x = cell.x
        y = cell.y - 1
        new_cell = self.get_cell(x, y)
        neighbor_list.append(new_cell)

        # Get neighbor cells on a x-axis.
        y = cell.y
        x = cell.x + 1
        new_cell = self.get_cell(x, y)
        neighbor_list.append(new_cell)

        y = cell.y
        x = cell.x - 1
        new_cell = self.get_cell(x, y)
        neighbor_list.append(new_cell)

        # Delete cells outside of a board.
        for cell in neighbor_list:
            if cell is None:
                neighbor_list.remove(cell)
        return neighbor_list

    def is_attack(self, player, outer_cell_list):
        for cell in outer_cell_list:
            if cell.affiliation == player.id:
                return True
        return False


class Player:

    __instances = []

    def __init__(self, name, ID):
        self.name = name
        self.id = ID
        self.counter = 0

        self.__instances.append(self)

        if len(self.__instances) > 2:
            raise Exception("Нельзя создавать больше двух игроков!")

    def attack(self, board, x, y):
        self.counter += 1

        cell = board.get_cell(x, y)
        neighbors = board.get_neighbors(cell)

        # Check if we can attack a cell.
        is_attack = board.is_attack(self, neighbors)

        print(f'Игрок № {self.id} атакует клетку {cell.x, cell.y} !')

        # Attack a cell.
        if is_attack is True:
            if cell.affiliation == 0:
                cell.affiliation = self.id
                print(f'Клетка {cell.x, cell.y} захвачена игроком № {cell.affiliation}.')
                print()
            elif cell.affiliation != self.id:
                cell.set_affiliation()
                print(f'Клетка {cell.x, cell.y} досталась игроку № {cell.affiliation}.')
                print()
        else:
            print("Атаковать можно только соседние клетки!")


# ПРИМЕР ИСПОЛЬЗОВАНИЯ КЛАССОВ ИГРЫ.

# Создаём доску с клетками.
board = Board()

'''
    Создаётся доска со следующими координатами:
  
 Y  4  [0;4]  [1;4]  [2;4]  [3;4]  [4;4]

    3  [0;3]  [1;3]  [2;3]  [3;3]  [4;3]

    2  [0;2]  [1;2]  [2;2]  [3;2]  [4;2]
  
    1  [0;1]  [1;1]  [2;1]  [3;1]  [4;1]
  
    0  [0;0]  [1;0]  [2;0]  [3;0]  [4;0]

         0      1      2      3      4     X
   
'''

# Выводим доску в консоль.
board.draw()

'''
[ 1 ] [ 0 ] [ 0 ] [ 0 ] [ 0 ] 
[ 0 ] [ 0 ] [ 0 ] [ 0 ] [ 0 ] 
[ 0 ] [ 0 ] [ 0 ] [ 0 ] [ 0 ] 
[ 0 ] [ 0 ] [ 0 ] [ 0 ] [ 0 ] 
[ 0 ] [ 0 ] [ 0 ] [ 0 ] [ 2 ]

Цифры 1 и 2 обозначают клетки, захваченные игроками.
Нули соответствуют клеткам, которые ещё никому не принадлежат.

'''

# Создаём игроков.
first_player  = Player("First", FIRST_PLAYER_ID)
second_player = Player("Second", SECOND_PLAYER_ID)

# Первый игрок атакует ближайшую клетку.
first_player.attack(board, 1, 4)

# Второй игрок атакует ближайшую клетку.
second_player.attack(board, 4, 1)

# Смотрим результат.
board.draw()

# Совершаем ещё несколько атак.
first_player.attack(board, 0, 3)
second_player.attack(board, 3, 0)

first_player.attack(board, 1, 3)
second_player.attack(board, 3, 1)

first_player.attack(board, 0, 2)
second_player.attack(board, 2, 0)

first_player.attack(board, 1, 2)
second_player.attack(board, 2, 1)

# Игроки атакуют одну и ту же клетку.
first_player.attack(board, 2, 2)
second_player.attack(board, 2, 2)

# Снова смотрим результат.
board.draw()


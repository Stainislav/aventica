'''
    Задание на знание ООП и декомпозицию.
    В примере описаны сущности для воображаемой игры. Необходимо придумать валидную
    с точки зрения ООП архитектуру для этих сущностей. Важно: не требуется писать логику,
    нужно просто написать имена классов, их публичные методы и связи между ними (можно
    использовать UML или псевдокод)

    Есть игровое поле 5x5. Каждая из клеток на этом поле может быть нейтральной или
    принадлежать одному из двух игроков. Изначально все клетки нейтральные кроме клеток
    в двух противоположных углах поля - они принадлежат игрокам.
    Игроки по очереди атакуют одну из клеток. При атаке нейтральной клетки, она успешно
    захватывается. При атаке клетки, захваченной другим игроком, исход решается броском
    кубиков. Атаковать можно только клетки, находящиеся по соседству с одной из уже
    захваченных клеток. Игра завершается при захвате стартовой клетки соперника или по
    истечении 7 ходов с каждой стороны.
    
  
    
 Y  4  (0;4)  (1;4)  (2;4)  (3;4)  (4;4)

    3  (0;3)  (1;3)  (2;3)  (3;3)  (4;3)

    2  (0;2)  (1;2)  (2;2)  (3;2)  (4;2)
  
    1  (0;1)  (1;1)  (2;1)  (3;1)  (4;1)
  
    0  (0;0)  (1;0)  (2;0)  (3;0)  (4;0)

         0      1      2      3      4     X
   

'''
import random 

FIRST_PLAYER  = 1
SECOND_PLAYER = 2

class Cell:

    def __init__(self, x, y, affiliation=0):
        self.x = x
        self.y = y
        self.affiliation = affiliation

    def set_affiliation(self):
        player_list = [FIRST_PLAYER, SECOND_PLAYER]
        player = random.choice(player_list)
        self.affiliation = player


class Board:

    def __init__( self, size=5, cell_list=[]):
        self.size      = size
        self.cell_list = cell_list

    def set_cells(self):        
        i = 0
        j = 0
        while j < self.size:
            while i < self.size:
                x = i
                y = j
                cell = Cell(x, y)
                self.cell_list.append(cell)
                i = i + 1
            i = 0
            j = j + 1

    def get_cell(self, x, y):
        for cell in self.cell_list:
            if cell.x == x and cell.y == y:
                return cell            


class FirstPlayer:

    def __init__(self, name='first_player'):
        self.name = name
        
    def attack(self, board, x, y):
        cell = board.get_cell(x, y)
        if cell.affiliation == None:
            cell.affiliation = self.name
        elif cell.affiliation != self.name:
            cell.set_affiliation()


class SecondPlayer:

    def __init__(self, name='second_player'):
        self.name = name
        
    def attack(self, board, x , y):
        cell = board.get_cell(x, y)
        if cell.affiliation == None:
            cell.affiliation = self.name
        elif cell.affiliation != self.name:
            cell.set_affiliation()

# Создаём доску 5 на 5 с клетками.
board = Board()
board.set_cells()


first_player  = FirstPlayer()
second_player = SecondPlayer()
first_player.name = 'Станислав'
second_player.name = 'Павел'
print(first_player.name)
print(second_player.name)

show_list = []
for i in board.cell_list:
    add_string = str(i.x) + ";" + str(i.y)
    show_list.append(add_string)

print(show_list)

for i in board.cell_list:
    print(i.affiliation)

x = 4
y = 1

first_player.attack(board, x, y)
print('Attack!')

for i in board.cell_list:
    print(i.affiliation)














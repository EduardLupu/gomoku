from src.board.cell import Cell
from src.player.player import Player


class Human(Player):
    def __init__(self, board):
        super(Human, self).__init__()
        self.__board = board

    def move(self, line, column, value):
        self.__board.set_value(line, column, value)
        return Cell(line, column, value)

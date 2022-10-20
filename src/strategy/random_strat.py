import random

from src.strategy.strategy import Strategy


class RandomStrategy(Strategy):
    def __init__(self, board, value):
        self.__board = board
        self.__value = value

    def move(self, *args):
        empty = self.__board.get_empty_cells()
        if len(empty) == 0:
            return None
        cell = random.choice(empty)
        self.__board.set_value(cell.row, cell.column, self.__value)
        return cell

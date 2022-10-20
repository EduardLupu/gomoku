from src.player.player import Player


class Computer(Player):
    def __init__(self, board, strategy):
        super(Computer, self).__init__()
        self.__board = board
        self.__strategy = strategy

    def move(self, line, column, value):
        # This function moves the computer's piece using a strategy
        return self.__strategy.move(line, column, value)

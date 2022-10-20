from src.board.cell import Cell
from abc import abstractmethod


class Player:
    def __init__(self):
        pass

    @abstractmethod
    def move(self, *args) -> Cell:
        pass

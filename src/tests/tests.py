import unittest
from src.board.board import Board
from src.board.cell import Cell

class TestGomokuGame(unittest.TestCase):
    def setUp(self) -> None:
       self.test = Board()

    def tearDown(self) -> None:
        pass

    def test__set_value__valid_integers__success(self):
        self.test.set_value(0, 0, 1)
        self.assertEqual(self.test.get_value(0, 0).value, 1)

    def test__get_row_values__valid_row__success(self):
        row = self.test.get_row_values(0)
        self.assertEqual(row, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test__get_empty_cells__empty_board__success(self):
        matrix = self.test.get_empty_cells()
        self.assertEqual(len(matrix), 225)

    def test__is_cell_available__available_cell__success(self):
        self.assertEqual(self.test.is_cell_available(0, 0), True)

    def test__is_winner__won_board__success(self):
        self.test.set_value(0, 0, 1)
        self.test.set_value(0, 1, 1)
        self.test.set_value(0, 2, 1)
        self.test.set_value(0, 3, 1)
        self.test.set_value(0, 4, 1)
        self.assertEqual(self.test.is_winner(Cell(row=0, column=4, value=1)), True)



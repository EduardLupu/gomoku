from src.strategy.strategy import Strategy
from src.board.cell import Cell
import random


class Minimax(Strategy):
    def __init__(self, board, value):
        self.__board = board
        self.__value = value
        self.__last_move = [-1, -1]

    @staticmethod
    def in_board(row, column):
        """This function checks if the row and the column are in board.

        :param row: integer
        :param column: integer
        :return: -
        """
        return 0 <= row <= 14 and 0 <= column <= 14

    def evaluate_directions(self, directions, row, column, value):
        """This function checks every direction(vertical, horizontal, oblique) too see how many pieces are in a row.

        :param directions: array
        :param row: integer
        :param column: integer
        :param value: integer
        :return: array
        """
        array = []
        copy_of_row, copy_of_column = row + 1, column
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # 1 0
            copy_of_row += 1
            directions[0] += 1

        copy_of_row, copy_of_column = row - 1, column
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # -1 0
            copy_of_row -= 1
            directions[1] += 1

        copy_of_row, copy_of_column = row, column - 1
        while self.__board.get_value(copy_of_row, copy_of_column).value == value:  # 0 -1
            copy_of_column -= 1
            directions[2] += 1

        copy_of_row, copy_of_column = row, column + 1
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # 0 1
            copy_of_column += 1
            directions[3] += 1

        copy_of_row, copy_of_column = row + 1, column + 1
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # 1 1
            copy_of_column += 1
            copy_of_row += 1
            directions[4] += 1

        copy_of_row, copy_of_column = row - 1, column - 1
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # -1 -1
            copy_of_column -= 1
            copy_of_row -= 1
            directions[5] += 1

        copy_of_row, copy_of_column = row + 1, column - 1
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # 1 -1
            copy_of_column -= 1
            copy_of_row += 1
            directions[6] += 1

        copy_of_row, copy_of_column = row - 1, column + 1
        while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == value:  # -1 1
            copy_of_column += 1
            copy_of_row -= 1
            directions[7] += 1
        for index in range(0, 8, 2):
            array.append(abs(directions[index] + directions[index + 1] - 1))
        return array

    def counter_attack(self):
        """This function makes a streak for the computer.

        :return: [integer, integer]
        """
        result = self.evaluate_directions([1, 1, 1, 1, 1, 1, 1, 1], self.__last_move[0], self.__last_move[1], 2)
        index = -1
        position = 0
        maximum = 1
        for distance in result:
            index += 1
            if distance > maximum:
                maximum = distance
                position = index
        row, column = self.__last_move[0], self.__last_move[1]
        if position == 0:
            copy_of_row, copy_of_column = row + 1, column
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 1 0
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # -1 0
                copy_of_row -= 1
            if self.in_board(copy_of_row, copy_of_column) and self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 1:
            copy_of_row, copy_of_column = row, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 0 -1
                copy_of_column -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 0 1
                copy_of_column += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 2:
            copy_of_row, copy_of_column = row + 1, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 1 1
                copy_of_column += 1
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 1 -1
                copy_of_column -= 1
                copy_of_row -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 3:
            copy_of_row, copy_of_column = row + 1, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # 1 -1
                copy_of_column -= 1
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 2:  # -1 1
                copy_of_column += 1
                copy_of_row -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        cell = random.choice(self.__board.get_empty_cells())
        return [cell.row, cell.column]

    def evaluate(self, row, column):
        """This function calculates every possible move and tries to find the best one.

        :param row: integer
        :param column: integer
        :return: -
        """
        result_of_computer = self.evaluate_directions([1, 1, 1, 1, 1, 1, 1, 1], self.__last_move[0], self.__last_move[1], 2)
        index = -1
        maximum_of_computer = 1
        for distance in result_of_computer:
            index += 1
            if distance > maximum_of_computer:
                maximum_of_computer = distance
        if maximum_of_computer == 4:
            return self.counter_attack()

        result_of_human = self.evaluate_directions([1, 1, 1, 1, 1, 1, 1, 1], row, column, 1)
        index = -1
        position = random.randint(0, 3)
        maximum_of_human = 1
        for distance in result_of_human:
            index += 1
            if distance > maximum_of_human:
                maximum_of_human = distance
                position = index

        if maximum_of_computer == 4 or (maximum_of_human <= 2) or (maximum_of_human == 3 and maximum_of_computer == 3):
            return self.counter_attack()

        if position == 0:
            copy_of_row, copy_of_column = row + 1, column
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 1 0
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # -1 0
                copy_of_row -= 1
            if self.in_board(copy_of_row, copy_of_column) and self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 1:
            copy_of_row, copy_of_column = row, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 0 -1
                copy_of_column -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 0 1
                copy_of_column += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 2:
            copy_of_row, copy_of_column = row + 1, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 1 1
                copy_of_column += 1
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 1 -1
                copy_of_column -= 1
                copy_of_row -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        if position == 3:
            copy_of_row, copy_of_column = row + 1, column - 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # 1 -1
                copy_of_column -= 1
                copy_of_row += 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
            copy_of_row, copy_of_column = row - 1, column + 1
            while self.in_board(copy_of_row, copy_of_column) and self.__board.get_value(copy_of_row, copy_of_column).value == 1:  # -1 1
                copy_of_column += 1
                copy_of_row -= 1
            if self.__board.is_cell_available(copy_of_row, copy_of_column) is True:
                return [copy_of_row, copy_of_column]
        cell = random.choice(self.__board.get_empty_cells())
        return [cell.row, cell.column]

    def get_move(self, row, column):
        best_move = self.evaluate(row, column)
        return best_move[0], best_move[1]

    def move(self, row, column, value):
        best_move_row, best_move_column = self.get_move(row, column)
        self.__last_move = [best_move_row, best_move_column]
        cell = Cell(row=best_move_row, column=best_move_column, value=self.__value)
        self.__board.set_value(cell.row, cell.column, self.__value)
        return cell

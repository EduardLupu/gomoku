from src.board.cell import Cell
import numpy


class Board:
    def __init__(self):
        self.__rows = 15
        self.__columns = 15
        self.__cells = self.__create_board()

    def __create_board(self):
        """This function creates a empty board.

        :return: empty 15x15 gomoku board
        """
        return [[Cell(row, column, 0) for column in range(self.__columns)] for row in range(self.__rows)]

    def set_value(self, row, column, value):
        """This function sets a value at the cell<row><column>

        :param row: integer
        :param column: integer
        :param value: integer
        :return: nothing
        """
        self.__cells[row][column].value = value

    def get_value(self, row, column):
        """This function returns the value of the cell<row><column>

        :param row: integer
        :param column: integer
        :return: integer
        """
        return self.__cells[row][column]

    def get_row_values(self, row):
        """This function gets the values of a row.

        :param row: integer
        :return: array of the values of rows
        """
        return [cell.value for cell in self.__cells[row]]

    def get_column_values(self, column):
        """This function gets the values of a column.

        :param column: integer
        :return: array of the values of column
        """
        return [row[column].value for row in self.__cells]

    def get_empty_cells(self):
        return [cell for cell in self.__get_all_cells_as_list() if cell.value == 0]

    def __get_all_cells_as_list(self):
        return [cell for line in self.__cells for cell in line]

    def is_cell_available(self, row, column):
        """This function returns True/False if the cell is available or not.

        :param row: integer
        :param column: integer
        :return: True/False
        """
        if row < 0 or row > 14:
            return False
        if column < 0 or column > 14:
            return False
        if self.get_value(row, column) == Cell(row=row, column=column, value=0):
            return True
        return False

    def get_all_cells_as_matrix(self):
        matrix = []
        for row in range(self.__rows):
            line = self.get_row_values(row)
            matrix.append(line)
        return matrix

    def get_principal_diagonals(self):
        diagonals = []
        for diagonal in range(-14, 15):
            diagonals.append(numpy.diagonal(self.get_all_cells_as_matrix(), diagonal))
        return diagonals

    def get_secondary_diagonals(self):
        diagonals = []
        for diagonal in range(-14, 15):
            diagonals.append(numpy.diagonal(numpy.fliplr(self.get_all_cells_as_matrix()), diagonal))
        return diagonals

    def is_winner(self, latest_move):
        """This function verifies the whole to see if anyone has finished

        :param latest_move: latest move in the game, type<Cell>
        :return: True/False
        """
        row_values = self.get_row_values(latest_move.row)
        if self.__check_array(row_values, latest_move.value) is True:
            return True

        column_values = self.get_column_values(latest_move.column)
        if self.__check_array(column_values, latest_move.value) is True:
            return True

        principal_diagonal_values = self.get_principal_diagonals()
        for array in principal_diagonal_values:
            if self.__check_array(array, latest_move.value) is True:
                return True

        secondary_diagonal_values = self.get_secondary_diagonals()
        for array in secondary_diagonal_values:
            if self.__check_array(array, latest_move.value) is True:
                return True

        return False

    @staticmethod
    def __check_array(array, value):
        length = 0
        max_length = 0
        for element in range(len(array)):
            if array[element] == value:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 0
        if length > max_length:
            max_length = length
        if max_length >= 5:
            return True
        else:
            return False

    def is_game_over(self, latest_move):
        if latest_move is None:
            return True
        if len(self.get_empty_cells()) == 0:
            return True
        return False

    def __str__(self):
        result = "".join("  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E") + "\n"
        index = -1
        for row in self.__cells:
            index += 1
            if index <= 9:
                string = "".join(f"{index}") + " "
            else:
                string = "".join(f"{chr(65 - 10 + index)}") + " "
            value = ""
            for cell in row:
                if cell.value == 0:
                    value = ". "
                if cell.value == 1:
                    value = "● "
                if cell.value == 2:
                    value = "◯ "
                string += " ".join(value)
            result += string + "\n"
        return result

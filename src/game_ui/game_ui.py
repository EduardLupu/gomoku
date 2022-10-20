from src.player.human import Human
import sys


class GameUI:
    def __init__(self, board, human, computer):
        self.__board = board
        self.__human = human
        self.__computer = computer
        self.__last_row, self.__last_col = -1, -1

    def start_game(self):
        while True:
            if self.__move(self.__human, 1) is True:
                break
            if self.__move(self.__computer, 2) is True:
                break

    def __move(self, player, value):
        """This function makes a move and returns True/False if the move finished the game or not.

        :param player: computer/human
        :param value: 2/1
        :return: True/False
        """
        row, column = self.__last_row, self.__last_col
        if type(player) is Human:
            self.__draw_board()
            row, column = self.__read_move()
            if self.__board.is_cell_available(row, column) is False:
                raise AttributeError("Can't move in a invalid position!")
            self.__last_row, self.__last_col = row, column
        latest_move = player.move(row, column, value)
        if self.__board.is_game_over(latest_move) or self.__board.is_winner(latest_move):
            if type(player) is Human:
                print("Human wins!")
            else:
                print("Computer wins!")
            self.__draw_board()
            return True
        return False

    @staticmethod
    def __read_move():
        """This function reads the move of the player human.

        :return: the x position and y position.
        """
        command = input(">>>")
        if command == "exit":
            sys.exit()
        row, column = command.split(" ")
        if 'A' <= row <= 'E':
            row = int(ord(row) - 65 + 10)
        if 'A' <= column <= 'E':
            column = int(ord(column) - 65 + 10)
        return int(row), int(column)

    def __draw_board(self):
        print(self.__board)

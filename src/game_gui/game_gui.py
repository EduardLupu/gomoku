import pygame
import sys
import time
from src.game_gui.constants import *
from src.board.cell import Cell


class GameGUI:
    def __init__(self, board, human, computer):
        self.__board = board
        self.__human = human
        self.__computer = computer
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Gomoku by Edi")
        self.screen.fill(BACKGROUND)

    def draw_board(self):
        """This function draws the board.

        :return: nothing
        """
        blockSize = 40
        for x in range(60, 600, blockSize):
            for y in range(60, 600, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw_figures(self):
        """This function draws the figures.

        :return: nothing
        """
        for row in range(15):
            for col in range(15):
                if self.__board.get_value(row, col) == Cell(row=row, column=col, value=1):
                    self.draw_circle(row, col, 1)
                if self.__board.get_value(row, col) == Cell(row=row, column=col, value=2):
                    self.draw_circle(row, col, 2)

    def draw_circle(self, row, col, value):
        """This function draws the circle at a given position.

        :param row: integer
        :param col: integer
        :param value: integer
        :return: nothing
        """
        if value == 1:
            pygame.draw.circle(self.screen, WHITE, ((col + 1) * 40 + 18, (row + 1) * 40 + 18), 15, 15)
        elif value == 2:
            pygame.draw.circle(self.screen, BROWN, ((col + 1) * 40 + 18, (row + 1) * 40 + 18), 15, 15)

    def start_game(self):
        """This function starts the GUI and the game."""
        while True:
            self.draw_board()
            self.draw_figures()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    clicked_row = mouseY // 40
                    clicked_col = mouseX // 40
                    if 1 <= clicked_row <= 15 and 1 <= clicked_col <= 15:
                        row, column = clicked_row - 1, clicked_col - 1
                        if self.__board.is_cell_available(row, column) is True:
                            latest_move = self.__human.move(row, column, 1)
                            if self.__board.is_game_over(latest_move) or self.__board.is_winner(latest_move):
                                self.draw_circle(row, column, 1)
                                font = pygame.font.Font('freesansbold.ttf', 23)
                                text = font.render("Human wins!", True, BLACK)
                                self.screen.blit(text, (60, 18))
                                pygame.display.update()
                                time.sleep(3)
                                sys.exit()
                            latest_move = self.__computer.move(row, column, 2)
                            if self.__board.is_game_over(latest_move) or self.__board.is_winner(latest_move):
                                self.draw_circle(row, column, 1)
                                self.draw_circle(latest_move.row, latest_move.column, 2)
                                font = pygame.font.Font('freesansbold.ttf', 23)
                                text = font.render("Computer wins!", True, BLACK)
                                self.screen.blit(text, (60, 18))
                                pygame.display.update()
                                time.sleep(3)
                                sys.exit()
            pygame.display.update()

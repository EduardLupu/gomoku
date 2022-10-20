from src.board.board import Board
from src.game_ui.game_ui import GameUI
from src.strategy.minimax import Minimax
from src.game_gui.game_gui import GameGUI
from src.strategy.random_strat import RandomStrategy
from src.player.human import Human
from src.player.computer import Computer

board = Board()
strategy = Minimax(board, 2) # strategy = RandomStrategy(board, 2) for the random strategy.
human = Human(board)
computer = Computer(board, strategy)
game = GameGUI(board, human, computer) # game = GameUI(board, human, computer) for the UI.

game.start_game()

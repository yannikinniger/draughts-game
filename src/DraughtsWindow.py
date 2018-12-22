from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from control.DraughtsGame import DraughtsGame
from model.Board import Board
from model.Directions import Directions
from model.Player import Player
from view.BoardView import BoardView
from view.ScoreBoard import ScoreBoard


class DraughtsWindow(QMainWindow):
    width = 800
    height = 700

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Draughts')
        start_x, start_y = self.calculate_start_position()
        self.setGeometry(start_x, start_y, DraughtsWindow.width, DraughtsWindow.height)

        player1, player2 = Player('Player 1', 1, Directions.DOWN, Qt.black), Player('Player 2', 2, Directions.UP, Qt.white)
        board = Board(player1, player2)
        draughts_game = DraughtsGame(player1, player2, board)

        self.score_board = ScoreBoard(self, draughts_game)
        player1.attach(self.score_board)
        player2.attach(self.score_board)
        draughts_game.attach(self.score_board)

        self.board_view = BoardView(self, draughts_game, board.size,
                                    QSize(DraughtsWindow.width - 100, DraughtsWindow.height))
        board.attach(self.board_view)

        self.addDockWidget(Qt.RightDockWidgetArea, self.score_board)
        self.setCentralWidget(self.board_view)
        self.show()

    @staticmethod
    def calculate_start_position():
        """
        Calculates the coordinates to place the window in the middle of the screen
        :return: x and y coordinates of the window to be centered
        """
        screen_resolution = QDesktopWidget().screenGeometry()
        x = (screen_resolution.width() / 2) - (DraughtsWindow.width / 2)
        y = (screen_resolution.height() / 2) - (DraughtsWindow.height / 2)
        return int(x), int(y)

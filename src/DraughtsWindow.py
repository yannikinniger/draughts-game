from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QDockWidget, QLabel, QHBoxLayout, QWidget, QListWidget

from control.AbstractDraughts import AbstractDraughts
from model.Player import Player
from view.Board import Board
from view.GuiMixin import GuiMixin
from view.ScoreBoard import ScoreBoard


class DraughtsWindow(QMainWindow, GuiMixin):
    width = 800
    height = 700

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Draughts')
        start_x, start_y = self.calculate_start_position()
        self.setGeometry(start_x, start_y, DraughtsWindow.width, DraughtsWindow.height)

        GuiMixin.__init__(self)

    def _init_components(self):
        player1, player2 = Player('Player 1', 1), Player('Player 2', 2)
        draughts_game = AbstractDraughts(player1, player2)
        self.score_board = ScoreBoard(self, draughts_game)
        self.board = Board(self, draughts_game, QSize(DraughtsWindow.width - 100, DraughtsWindow.height))

    def _layout(self):
        self.addDockWidget(Qt.RightDockWidgetArea, self.score_board)
        self.setCentralWidget(self.board)

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

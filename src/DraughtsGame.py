from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from view.Board import Board


class DraughtsGame(QMainWindow):
    width = 700
    height = 700

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draught')
        start_x, start_y = self.calculate_start_position()
        self.setGeometry(start_x, start_y, DraughtsGame.width, DraughtsGame.height)
        self.board = Board(self)
        self.show()

    def __layout(self):
        self.setCentralWidget(self.board)

    @staticmethod
    def calculate_start_position():
        """
        Calculates the coordinates to place the window in the middle of the screen
        :return: x and y coordinates of the window to be centered
        """
        screen_resolution = QDesktopWidget().screenGeometry()
        x = (screen_resolution.width() / 2) - (DraughtsGame.width / 2)
        y = (screen_resolution.height() / 2) - (DraughtsGame.height / 2)
        return int(x), int(y)

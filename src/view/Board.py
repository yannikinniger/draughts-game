from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from view.drawing import draw_circle, draw_rect


class Board(QWidget):

    def __init__(self, parent, draughts_game):
        super().__init__(parent)
        self.resize(parent.size())
        self.draughts_game = draughts_game
        self.rect_width, self.rect_height = self.calculate_rectangle_size()

    def calculate_rectangle_size(self):
        """
        Calculates the size of the rectangle depending on the widget size and board size
        :return: width and height of the rectangles
        """
        size = self.size()
        rect_width = size.width() / self.draughts_game.board_size
        rect_height = size.height() / self.draughts_game.board_size
        return int(rect_width), int(rect_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_background(painter)
        self.render_pieces(painter)
        painter.end()

    def draw_background(self, painter):
        """
        Draws the checkered game board as a background
        :param painter: QPainter to draw the rectangles
        """
        for row in range(0, self.draughts_game.board_size):
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, self.draughts_game.board_size, 2):
                rect_x = self.rect_width * row
                rect_y = self.rect_height * column
                draw_rect(self.rect_width, self.rect_height, rect_x, rect_y, painter)

    def render_pieces(self, painter):
        """
        Renders all the pieces on the board.
        :param painter: QPainter to draw the pieces. The brush will be changed in the method.
        """
        # placeholder until the board can be received from the game object
        for row_index, row in enumerate(self.draughts_game.board):
            if row != [0] * 8:
                for column_index, column in enumerate(row):
                    if column != 0:
                        color = Board.get_color(column)
                        circle_x = self.rect_width * column_index
                        circle_y = self.rect_height * row_index
                        draw_circle(self.rect_width, self.rect_height, circle_x, circle_y, painter, color)

    @staticmethod
    def get_color(player_id):
        if player_id == 1:
            return Qt.red
        elif player_id == 2:
            return Qt.blue

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        row, column = self.get_rectangle_position(event.x(), event.y())
        if row in range(0, self.draughts_game.board_size) and column in range(0, self.draughts_game.board_size):
            self.draughts_game.click_event(row, column)

    def get_rectangle_position(self, x, y):
        column = int(x / self.rect_width)
        row = int(y / self.rect_height)
        return row, column

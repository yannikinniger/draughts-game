from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from control.Observer import Observer
from view.drawing import draw_circle, draw_rect


class BoardView(QWidget, Observer):

    def __init__(self, parent, draughts_game, board_size, size):
        super().__init__(parent)
        self.resize(size)
        self.draughts_game = draughts_game
        self.board_size = board_size
        self.rect_width, self.rect_height = self.calculate_rectangle_size()

    def calculate_rectangle_size(self):
        """
        Calculates the size of the rectangle depending on the widget size and board size
        :return: width and height of the rectangles
        """
        size = self.size()
        rect_width = size.width() / self.board_size
        rect_height = size.height() / self.board_size
        return int(rect_width), int(rect_height)

    def update(self):
        self.repaint()

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
        for row in range(0, self.board_size):
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, self.board_size, 2):
                rect_x = self.rect_width * row
                rect_y = self.rect_height * column
                draw_rect(self.rect_width, self.rect_height, rect_x, rect_y, painter)

    def render_pieces(self, painter):
        """
        Renders all the pieces on the board.
        :param painter: QPainter to draw the pieces. The brush will be changed in the method.
        """
        for piece in self._subject.pieces:
            circle_x = self.rect_width * piece.location.column
            circle_y = self.rect_height * piece.location.row
            draw_circle(self.rect_width, self.rect_height, circle_x, circle_y, painter, piece.owner.color)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        row, column = self.get_rectangle_position(event.x(), event.y())
        self.draughts_game.click_event(row, column)

    def get_rectangle_position(self, x, y):
        """
        Calculates the position of the mouse click on the grid.
        :param x: X coordinate of the mouse click
        :param y: Y coordinate of the mouse click
        :return: Column and row of the mouse click
        """
        column = int(x / self.rect_width)
        row = int(y / self.rect_height)
        return row, column

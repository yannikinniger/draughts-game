from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class Board(QWidget):
    board_size = 8

    def __init__(self, parent):
        super().__init__(parent)
        self.resize(parent.size())
        self.rect_width, self.rect_height = self.calculate_rectangle_size()

    def calculate_rectangle_size(self):
        """
        Calculates the size of the rectangle depending on the widget size and board size
        :return: width and height of the rectangles
        """
        size = self.size()
        rect_width = size.width() / Board.board_size
        rect_height = size.height() / Board.board_size
        return rect_width, rect_height

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_background(painter)

    def draw_background(self, painter):
        """
        Draws the checkered game board as a background
        :param painter: QPainter to draw the rectangles
        """
        for row in range(0, Board.board_size):
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, Board.board_size, 2):
                self.draw_rect(column * self.rect_width, row * self.rect_height, painter)

    def draw_rect(self, x_offset, y_offset, painter):
        """
        Draws a single rectangle on the Widget
        :param x_offset: x offset from the top left rectangle
        :param y_offset: y offset from the top left rectangle
        :param painter: QPainter to draw the rectangle
        """
        painter.save()
        painter.translate(x_offset, y_offset)
        painter.fillRect(0, 0, int(self.rect_width), int(self.rect_height), Qt.black)
        painter.restore()

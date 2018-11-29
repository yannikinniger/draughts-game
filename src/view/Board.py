from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
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
        painter.fillRect(0, 0, self.rect_width, self.rect_height, Qt.black)
        painter.restore()

    def render_pieces(self, painter):
        """
        Renders all the pieces on the board.
        :param painter: QPainter to draw the pieces. The brush will be changed in the method.
        """
        # placeholder until the board can be received from the game object
        board = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [0] * 8,
            [0] * 8,
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0]
        ]
        for row_index, row in enumerate(board):
            if row != [0] * 8:
                for column_index, column in enumerate(row):
                    if column != 0:
                        color = Board.get_color(column)
                        circle_x = self.rect_width * column_index
                        circle_y = self.rect_height * row_index
                        self.draw_circle(circle_x, circle_y, painter, color)

    @staticmethod
    def get_color(player_id):
        if player_id == 1:
            return Qt.red
        elif player_id == 2:
            return Qt.blue

    def draw_circle(self, x_offset, y_offset, painter, color):
        """
        Draws a single rectangle on the Widget
        :param x_offset: x offset from the top left rectangle
        :param y_offset: y offset from the top left rectangle
        :param painter: QPainter to draw the rectangle
        :param color: Color the circle should be filled with
        """
        size_reduction = 5
        painter.setBrush(QBrush(color))
        painter.save()
        painter.translate(x_offset, y_offset)

        circle_width = self.rect_width - size_reduction * 2
        circle_height = self.rect_height - size_reduction * 2
        painter.drawEllipse(size_reduction, size_reduction, circle_width, circle_height)
        painter.restore()

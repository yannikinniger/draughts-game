from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from helper.Observer import Observer
from model.pieces.KingPiece import KingPiece
from view.GuiMixin import GuiMixin
from view.drawing import draw_circle, draw_rect


class BoardView(QWidget, Observer, GuiMixin):

    def __init__(self, parent, draughts_game, board_size, size):
        QWidget.__init__(self, parent)
        GuiMixin.__init__(self)
        self.resize(size)
        self.draughts_game = draughts_game
        self.board_size = board_size
        self.rect_width, self.rect_height = self.calculate_rectangle_size()
        self.selected_piece = None

    def _init_components(self):
        self.winner_label = QLabel()
        self.winner_label.setFont(QtGui.QFont('SansSerif', 26))
        self.winner_label.setFixedHeight(100)
        self.winner_label.setAutoFillBackground(True)
        self.winner_label.setStyleSheet('color: green')
        self.winner_label.setAlignment(Qt.AlignCenter)
        self.winner_label.setVisible(False)

    def _layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.winner_label)
        self.setLayout(layout)

    def calculate_rectangle_size(self):
        """
        Calculates the size of the rectangle depending on the widget size and board size
        :return: width and height of the rectangles
        """
        size = self.size()
        rect_width = size.width() / self.board_size
        rect_height = size.height() / self.board_size
        return int(rect_width), int(rect_height)

    def update_(self, subject):
        self.subject = subject
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_background(painter)
        if self.subject.selected_piece is not None:
            self.draw_selected_piece(painter)
        self.render_pieces(painter)
        self._display_winner_if_present()
        painter.end()

    def draw_background(self, painter):
        """
        Draws the checkered game board as a background
        :param painter: QPainter to draw the rectangles
        """
        draw_rect(self.width(), self.height(), 0, 0, painter, QColor(220, 180, 132))
        for row in range(0, self.board_size):
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, self.board_size, 2):
                rect_x = self.rect_width * row
                rect_y = self.rect_height * column
                draw_rect(self.rect_width, self.rect_height, rect_x, rect_y, painter, QColor(102, 51, 0))

    def render_pieces(self, painter):
        """
        Renders all the pieces on the board.
        :param painter: QPainter to draw the pieces. The brush will be changed in the method.
        """
        for piece in self.subject.pieces:
            circle_x = self.rect_width * piece.location.column
            circle_y = self.rect_height * piece.location.row
            draw_circle(self.rect_width, self.rect_height, circle_x, circle_y, painter, piece.owner.color)
            if isinstance(piece, KingPiece):
                draw_circle(self.rect_width - 30, self.rect_height - 30, circle_x + 15, circle_y + 15, painter,
                            Qt.yellow)

    def draw_selected_piece(self, painter):
        selected_piece = self.subject.selected_piece
        circle_x = self.rect_width * selected_piece.location.column
        circle_y = self.rect_height * selected_piece.location.row
        draw_rect(self.rect_width, self.rect_height, circle_x, circle_y, painter, QColor(255, 215, 0))

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

    def _display_winner_if_present(self):
        if self.subject.winner is not None:
            self.winner_label.setText('{} wins'.format(self.subject.winner.name))
            self.winner_label.setVisible(True)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget, QLabel, QWidget, QGridLayout, QSpacerItem, QSizePolicy
from qtpy import QtGui

from helper.Observer import Observer
from view.GuiMixin import GuiMixin


class ScoreBoard(QDockWidget, GuiMixin, Observer):

    def __init__(self, parent, draughts_game):
        self.draughts_game = draughts_game
        QDockWidget.__init__(self, parent)
        GuiMixin.__init__(self)

    def _init_components(self):
        self.player_1_label = ScoreBoard.get_label(self.draughts_game.player_1.name, 16)
        self.player_1_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_1.score), 14)
        self.player_2_label = ScoreBoard.get_label(self.draughts_game.player_2.name, 16)
        self.player_2_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_2.score), 14)

    @staticmethod
    def get_label(content, font_size):
        label = QLabel(content)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('SansSerif', font_size))
        return label

    def _layout(self):
        dock_widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.player_1_label, 0, 0)
        layout.addWidget(self.player_1_score, 1, 0)
        layout.addItem(QSpacerItem(50, 50, vPolicy=QSizePolicy.Expanding), 2, 0)
        layout.addWidget(self.player_2_label, 3, 0)
        layout.addWidget(self.player_2_score, 4, 0)
        dock_widget.setLayout(layout)
        self.setWidget(dock_widget)
        self.setMinimumWidth(100)

    def update_(self):
        self.player_1_score.setText("Score: {}".format(self.draughts_game.player_1.score))
        self.player_2_score.setText("Score: {}".format(self.draughts_game.player_2.score))

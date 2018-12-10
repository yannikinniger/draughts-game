from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget, QLabel, QWidget, QGridLayout, QSpacerItem, QSizePolicy

from view.GuiMixin import GuiMixin


class ScoreBoard(QDockWidget, GuiMixin):

    def __init__(self, parent, draughts_game):
        self.draughts_game = draughts_game
        QDockWidget.__init__(self, parent)
        GuiMixin.__init__(self)

    def _init_components(self):
        self.player_1_label = ScoreBoard.get_label(self.draughts_game.player_1.name)
        self.player_1_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_1.score))
        self.player_2_label = ScoreBoard.get_label(self.draughts_game.player_2.name)
        self.player_2_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_2.score))

    @staticmethod
    def get_label(content):
        label = QLabel(content)
        label.setAlignment(Qt.AlignCenter)
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

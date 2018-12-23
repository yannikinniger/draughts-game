from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget, QLabel, QWidget, QGridLayout, QSpacerItem, QSizePolicy
from qtpy import QtGui

from control.DraughtsGame import DraughtsGame
from helper.Observer import Observer
from model.Player import Player
from view.GuiMixin import GuiMixin


class ScoreBoard(QDockWidget, GuiMixin, Observer):

    def __init__(self, parent, draughts_game):
        self.draughts_game = draughts_game
        QDockWidget.__init__(self, parent)
        GuiMixin.__init__(self)
        self._indicate_current_player(draughts_game.current_player)

    def _init_components(self):
        self.player_1_label = ScoreBoard.get_label(self.draughts_game.player_1.name, 20)
        self.player_1_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_1.score), 18)
        self.player_2_label = ScoreBoard.get_label(self.draughts_game.player_2.name, 20)
        self.player_2_score = ScoreBoard.get_label("Score: {}".format(self.draughts_game.player_2.score), 18)

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

    def update_(self, subject):
        if isinstance(subject, Player):
            if subject.uid == 1:
                ScoreBoard._update_label(self.player_1_score, subject.score)
            elif subject.uid == 2:
                ScoreBoard._update_label(self.player_2_score, subject.score)
        if isinstance(subject, DraughtsGame):
            self._indicate_current_player(subject.current_player)

    def _indicate_current_player(self, current_player):
        if current_player.uid == 1:
            ScoreBoard._change_label_text_color(self.player_1_label, 'green')
            ScoreBoard._change_label_text_color(self.player_2_label, 'black')
        elif current_player.uid == 2:
            ScoreBoard._change_label_text_color(self.player_2_label, 'green')
            ScoreBoard._change_label_text_color(self.player_1_label, 'black')

    @staticmethod
    def _update_label(label, new_text):
        """
        Updates a label to a new value.
        :param label: Label to update
        :param new_text: New value of the label
        """
        label.setText("Score: {}".format(new_text))

    @staticmethod
    def _change_label_text_color(label, color):
        """
        Changes the text color of a label.
        :param label: Label of which the text color should be changed
        :param color: String of the new color name
        """
        label.setStyleSheet('color: {}'.format(color))

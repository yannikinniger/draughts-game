from PyQt5.QtCore import QPoint

from control.AbstractDraughts import AbstractDraughts


class DraughtsGame(AbstractDraughts):

    def __init__(self, player_1, player_2):
        super().__init__(player_1, player_2)
        self.last_click = None

    def pause(self):
        pass

    def restart(self):
        pass

    def click_event(self, row, column):
        if self.last_click is not None:
            self.move_piece(self.last_click.x(), self.last_click.y(), row, column)
            self.last_click = None
            self.dispatch()
        else:
            self.last_click = QPoint(row, column)

    def key_event(self, key_event):
        pass

    def move_piece(self, from_row, from_column, to_row, to_column):
        if self.board[from_row][from_column] > 0:
            self.board[from_row][from_column] = 0
            self.board[to_row][to_column] = self.current_player.uid

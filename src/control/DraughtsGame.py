from control.AbstractDraughts import AbstractDraughts
from model.Location import Location


class DraughtsGame(AbstractDraughts):

    def __init__(self, player_1, player_2, board):
        super().__init__(player_1, player_2, board)

    def pause(self):
        pass

    def restart(self):
        pass

    def click_event(self, row, column):
        click_location = Location(row, column)
        if self.board.piece_selected():
            self.board.move(click_location)
        else:
            self.board.select(click_location)

    def key_event(self, key_event):
        pass

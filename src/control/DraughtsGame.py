from control.AbstractDraughts import AbstractDraughts
from helper.Observer import Subject
from helper.calculations import calculate_offset
from model.Location import Location
from model.pieces.InvalidMoveException import InvalidMoveException


class DraughtsGame(AbstractDraughts, Subject):

    def __init__(self, player_1, player_2, board):
        AbstractDraughts.__init__(self, player_1, player_2, board)
        Subject.__init__(self)

    def pause(self):
        pass

    def restart(self):
        pass

    def click_event(self, row, column):
        click_location = Location(row, column)
        if self.board.selected_piece is not None:
            if self.board.contains_piece(click_location) and self.current_player == self.board.get_owner(
                    click_location):
                self.board.select(click_location)
            else:
                try:
                    self._move_piece(click_location)
                except InvalidMoveException:
                    self.board.deselect()
        else:
            if self.current_player == self.board.get_owner(click_location):
                self.board.select(click_location)
            else:
                self.board.deselect()

    def key_event(self, key_event):
        pass

    def _move_piece(self, to_location):
        selected_piece_location = self.board.selected_piece.location
        row_offset = calculate_offset(selected_piece_location, to_location).row
        if row_offset == 1:
            self.board.move(to_location)
            self._switch_player()
        elif row_offset == 2:
            self._capture_piece(to_location)
            self._switch_player()

    def _capture_piece(self, to_location):
        self.board.capture(to_location)
        self.current_player.add_points()

    def _switch_player(self):
        self.current_player.stop_timer()
        has_winner = self.board.check_winner()
        if not has_winner:
            if self.current_player == self.player_1:
                self.current_player = self.player_2
            else:
                self.current_player = self.player_1
        self._notify()

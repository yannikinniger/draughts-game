from control.AbstractDraughts import AbstractDraughts
from helper.calculations import calculate_offset
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
        if self.board.selected_piece is not None:
            if self.board.contains_piece(click_location) and self.current_player == self.board.get_owner(click_location):
                self.board.select(click_location)
            else:
                self.__move_piece(click_location)
        else:
            if self.current_player == self.board.get_owner(click_location):
                self.board.select(click_location)

    def key_event(self, key_event):
        pass

    def __move_piece(self, to_location):
        selected_piece_location = self.board.selected_piece.location
        row_offset = calculate_offset(selected_piece_location, to_location).row
        if row_offset == 1:
            self.board.move(to_location)
        elif row_offset == 2:
            self.__capture_piece(to_location)
        self.__switch_player()

    def __capture_piece(self, to_location):
        successfully_captured = self.board.capture(to_location)
        if successfully_captured:
            self.current_player.add_points()

    def __switch_player(self):
        self.current_player.stop_timer()
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

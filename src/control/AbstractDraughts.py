import abc


class AbstractDraughts:

    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.current_player = player_1

    def get_player_color(self, player_uid):
        if self.player_1.uid == player_uid:
            return self.player_1.color
        elif self.player_2.uid == player_uid:
            return self.player_2.color

    @abc.abstractmethod
    def pause(self):
        """
        Pauses the game, no players clock is running and no moves can be made.
        """
        pass

    @abc.abstractmethod
    def restart(self):
        """
        Resets the game to its initial state. The board is reset and all scores are set to zero.
        """
        pass

    @abc.abstractmethod
    def click_event(self, row, column):
        """
        Handles a click to a field on the board.
        :param row: Row of the clicked field
        :param column: Column of the clicked field
        """
        pass

    @abc.abstractmethod
    def key_event(self, key_event):
        """
        Handles a key event in the game.
        :param key_event: Keypress event by PyQt
        """
        pass

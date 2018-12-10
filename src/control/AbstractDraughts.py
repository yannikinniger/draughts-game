import abc

from control.Observer import Publisher


class AbstractDraughts(Publisher):

    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = player_1
        self.board_size = 8
        self.board = self.init_board()

    def init_board(self):
        def get_player_id(current_row):
            if current_row in range(0, 3):
                return self.player_1.uid
            elif current_row in range(self.board_size - 3, self.board_size):
                return self.player_2.uid
            else:
                return 0

        board = []
        for row in range(0, self.board_size):
            board.append([0] * self.board_size)
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, self.board_size, 2):
                board[row][column] = get_player_id(row)
        return board

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

import abc


class AbstractDraughts:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board_size = 8
        self.board = self.init_board()

    def init_board(self):
        def get_player_id(current_row):
            if current_row in range(0, 3):
                return self.player_1.id
            elif current_row in range(self.board_size - 3, self.board_size):
                return self.player_2.id
            else:
                return 0

        board = []
        for row in range(0, self.board_size):
            board.append([0] * self.board_size)
            start_column = 0 if row % 2 == 1 else 1
            for column in range(start_column, self.board_size, 2):
                board[row][column] = get_player_id(row)
        return board

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
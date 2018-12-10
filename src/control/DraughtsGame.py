from control.AbstractDraughts import AbstractDraughts


class DraughtsGame(AbstractDraughts):

    def __init__(self, player_1, player_2):
        super().__init__(player_1, player_2)

    def pause(self):
        pass

    def restart(self):
        pass

    def click_event(self, row, column):
        pass

    def key_event(self, key_event):
        pass

    def get_possible_moves(self, selected_row, selected_column):
        # Todo override this code, it's just for temporary testing
        board = []
        for row in range(0, self.board_size):
            board.append([0] * self.board_size)

        board[selected_row + 1][selected_column + 1] = 1
        return board

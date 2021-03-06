from helper.Observer import Subject
from helper.calculations import get_middle_point
from model.Location import Location
from model.pieces.InvalidMoveException import InvalidMoveException
from model.pieces.KingPiece import KingPiece
from model.pieces.RegularPiece import RegularPiece


class Board(Subject):
    size = 8

    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self._set_up_board()

    def _set_up_board(self):
        """
        Sets up the board to it's initial state.
        """
        self.pieces = []
        for row_index in range(0, 3):
            self._fill_row(self.player_1, row_index)
        for row_index in range(Board.size - 3, Board.size):
            self._fill_row(self.player_2, row_index)
        self.selected_piece = None

    def _fill_row(self, player, row_index):
        """
        Helper method to fill up a row with pieces.
        :param player: Player which owns the pieces of this row.
        :param row_index: Row index to fill.
        """
        start_column = 0 if row_index % 2 == 1 else 1
        for column_index in range(start_column, Board.size, 2):
            self.pieces.append(RegularPiece(player, Location(row_index, column_index), player.direction))

    def reset(self):
        """
        Resets the board to it's initial state
        """
        self._set_up_board()

    def contains_piece(self, location):
        return any(piece for piece in self.pieces if piece.location == location)

    def select(self, location):
        """
        Selects a piece to be moved later.
        :param location: Location of the piece to be selected
        """
        if self.contains_piece(location):
            self.selected_piece = self._get_piece(location)
            self._notify()

    def deselect(self):
        """
        Deselects the currently selected piece.
        """
        self.selected_piece = None
        self._notify()

    def move(self, to_location):
        """
        Moves the selected piece to a new location. Precondition select() must be called before calling this method.
        :param to_location: New location of the piece
        :raises: InvalidMoveException when an invalid move is attempted.
        """
        if self.selected_piece is not None and not self.contains_piece(to_location):
            self.selected_piece.move(to_location)
            if self.selected_piece.location.row == Board.size - 1 or self.selected_piece.location.row == 0:
                self.pieces.remove(self.selected_piece)
                self.pieces.append(KingPiece.of(self.selected_piece))
            self.selected_piece = None
            self._notify()
        else:
            raise InvalidMoveException

    def capture(self, location):
        """
        Captures an opponents piece. Therefore it removes the opponents piece and moves the piece by two.
        Precondition select() must be called before calling this method
        :param location: Location of the piece to overtake.
        """
        opponent_piece_location = get_middle_point(self.selected_piece.location, location)
        opponent_piece = self._get_piece(opponent_piece_location)
        if opponent_piece is not None and opponent_piece.owner != self.selected_piece.owner and not \
                self.contains_piece(location):
            self.move(location)
            self.pieces.remove(opponent_piece)
            self._notify()
        else:
            raise InvalidMoveException

    def _get_piece(self, location):
        try:
            return next(piece for piece in self.pieces if piece.location == location)
        except StopIteration:
            return None

    def get_owner(self, piece_location):
        """
        Returns the owner of the piece at the given location.
        :param piece_location: Location of the piece
        :return: Player which owns the piece or None if there is no piece at this location
        """
        try:
            return self._get_piece(piece_location).owner
        except AttributeError:
            return None

    def check_winner(self):
        player_1_pieces = [piece for piece in self.pieces if piece.owner == self.player_1]
        player_2_pieces = [piece for piece in self.pieces if piece.owner == self.player_2]
        if len(player_1_pieces) == 0:
            self.winner = self.player_2
        elif len(player_2_pieces) == 0:
            self.winner = self.player_1
        else:
            return False
        self._notify()

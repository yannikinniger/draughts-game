from control.Observer import Subject
from model.Location import Location
from model.RegularPiece import RegularPiece


class Board(Subject):
    size = 8

    def __init__(self, player_1, player_2):
        super().__init__()
        self.pieces = []
        for row_index in range(0, 3):
            self.__fill_row(player_1, row_index)
        for row_index in range(Board.size - 3, Board.size):
            self.__fill_row(player_2, row_index)
        self.__selected_piece = None

    def __fill_row(self, player, row_index):
        start_column = 0 if row_index % 2 == 1 else 1
        for column_index in range(start_column, Board.size, 2):
            self.pieces.append(RegularPiece(player, Location(row_index, column_index)))

    def contains_piece(self, location):
        return any(piece for piece in self.pieces if piece.location == location)

    def select(self, location):
        if self.contains_piece(location):
            self.__selected_piece = self.__get_piece(location)

    def piece_selected(self):
        return self.__selected_piece is not None

    def move(self, to_location):
        """
        Moves the selected piece to a new location. Precondition select() must be called before calling this method.
        :param to_location: New location of the piece
        """
        if self.__selected_piece is not None and not self.contains_piece(to_location):
            self.__selected_piece.move(to_location)
            self.__selected_piece = None
            self._notify()

    def capture(self, location):
        """
        Captures an opponents piece. Therefore it removes the opponents piece and moves the piece by two.
        Precondition select() must be called before calling this method
        :param location: Location of the piece to overtake.
        :return: Boolean if the overtake was successful
        """
        if self.__selected_piece is not None and self.contains_piece(location):
            opponent_piece = self.__get_piece(location)
            if opponent_piece.owner != self.__selected_piece.owner:
                new_location = self.__multiply_offset(self.__selected_piece.location, opponent_piece.location, 2)
                if not self.contains_piece(new_location):
                    self.move(new_location)
                    self.pieces.remove(opponent_piece)
                    self._notify()
                    return True
        return False

    def __get_piece(self, location):
        return next(piece for piece in self.pieces if piece.location == location)

    @staticmethod
    def __multiply_offset(l1, l2, factor):
        """
        Calculates a new location by multiplying the offset from two locations by a factor.
        :return: New location
        """
        row = l2.row - l1.row
        column = l2.column - l1.column
        return Location(l1.row + (row * factor), l1.column + (column * factor))

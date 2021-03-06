from model.pieces.AbstractPiece import AbstractPiece
from model.Directions import Directions


class RegularPiece(AbstractPiece):

    def __init__(self, owner, location, direction):
        super().__init__(owner, location, direction)

    def _is_move_permitted(self, location):
        row_offset = self.location.row - location.row
        if self.direction == Directions.DOWN and row_offset > 0:
            return False
        elif self.direction == Directions.UP and row_offset < 0:
            return False
        column_offset = abs(self.location.column - location.column)
        print('{}, {}'.format(row_offset, column_offset))
        return abs(row_offset) == column_offset

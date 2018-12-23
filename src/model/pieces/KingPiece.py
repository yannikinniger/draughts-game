from helper.calculations import calculate_offset
from model.pieces.AbstractPiece import AbstractPiece


class KingPiece(AbstractPiece):

    def __init__(self, owner, location, direction):
        super().__init__(owner, location, direction)

    def _is_move_permitted(self, location):
        offset = calculate_offset(self.location, location)
        return offset.row == offset.column

    @staticmethod
    def of(regular_piece):
        return KingPiece(regular_piece.owner, regular_piece.location, regular_piece.direction)

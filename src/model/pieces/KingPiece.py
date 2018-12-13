from model.pieces.AbstractPiece import AbstractPiece


class KingPiece(AbstractPiece):

    def __init__(self, owner, location, direction):
        super().__init__(owner, location)
        self.direction = direction

    def _is_move_permitted(self, location):
        row_offset = abs(self.location.row - location.row)
        column_offset = abs(self.location.column - location.column)
        return row_offset == column_offset

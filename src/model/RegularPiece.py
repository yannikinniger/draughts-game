from model.AbstractPiece import AbstractPiece
from model.Location import Location


class RegularPiece(AbstractPiece):

    def __init__(self, owner, location):
        super().__init__(owner, location)

    def move(self, location):
        available_locations = self.get_available_moves()
        if location in available_locations:
            self.location = location

    def get_available_moves(self):
        available_moves = []
        if self.location.column - 1 in range(0, 8):
            available_moves.append(Location(self.location.row + 1, self.location.column - 1))
        if self.location.column + 1 in range(0, 8):
            available_moves.append(Location(self.location.row + 1, self.location.column + 1))
        return available_moves

from model.AbstractPiece import AbstractPiece
from model.Directions import Directions
from model.Location import Location


class RegularPiece(AbstractPiece):

    def __init__(self, owner, location, direction):
        super().__init__(owner, location)
        self.direction = direction

    def move(self, location):
        available_locations = self.get_available_moves()
        if location in available_locations:
            self.location = location

    def get_available_moves(self):
        available_moves = []
        row_movement = 1 if self.direction == Directions.DOWN else -1
        if self.location.column - 1 in range(0, 8):
            available_moves.append(Location(self.location.row + row_movement, self.location.column - 1))
        if self.location.column + 1 in range(0, 8):
            available_moves.append(Location(self.location.row + row_movement, self.location.column + 1))
        return available_moves

import abc

from model.pieces.InvalidMoveException import InvalidMoveException


class AbstractPiece:

    def __init__(self, owner, location):
        self.owner = owner
        self.location = location

    def move(self, location):
        """
        Moves the piece to a different location on the board. This method has to check if the new location is valid.
        :param location: Location of to move to.
        :raises: InvalidMoveException when an invalid move is attempted.
        """
        if self._is_move_permitted(location):
            self.location = location
        else:
            raise InvalidMoveException

    @abc.abstractmethod
    def _is_move_permitted(self, location):
        """
        Returns an array of points consisting the available positions to move to.
        """
        raise NotImplementedError()

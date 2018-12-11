import unittest

from PyQt5.QtCore import Qt

from model.Board import Board
from model.Location import Location
from model.Player import Player


class PlayerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.player_1 = Player('Test 1', 1, Qt.red)
        cls.player_2 = Player('Test 2', 2, Qt.blue)

    def test_should_find_piece_in_board(self):
        board = Board(self.player_1, self.player_2)
        location = Location(0, 1)

        result = board.contains_piece(location)
        self.assertTrue(result)

    def test_should_not_find_piece(self):
        board = Board(self.player_1, self.player_2)
        location = Location(0, 0)

        result = board.contains_piece(location)
        self.assertFalse(result)

    def test_should_throw_error_on_select_at_invalid_location(self):
        board = Board(self.player_1, self.player_2)
        location = Location(0, 0)

        self.assertRaises(ValueError, board.select, location)

    def test_should_move_piece_to_new_location(self):
        board = Board(self.player_1, self.player_2)
        expected_location = Location(3, 0)

        board.select(Location(2, 1))
        board.move(expected_location)

        expected_to_contain_piece = board.contains_piece(expected_location)
        self.assertTrue(expected_to_contain_piece)

    def test_should_not_move_piece_to_new_location_if_not_selected(self):
        board = Board(self.player_1, self.player_2)
        expected_location = Location(3, 0)

        board.move(expected_location)

        expected_to_be_empty = board.contains_piece(expected_location)
        self.assertFalse(expected_to_be_empty)

    def test_should_not_move_piece_to_new_location_if_field_occupied(self):
        board = Board(self.player_1, self.player_2)
        initial_location = Location(0, 1)

        board.select(initial_location)
        board.move(Location(1, 0))

        expected_to_contain_piece = board.contains_piece(initial_location)
        self.assertTrue(expected_to_contain_piece)

    def test_should_capture_opponents_piece(self):
        board = Board(self.player_1, self.player_2)
        expected_location = Location(5, 2)

        # make first move of player 1
        board.select(Location(2, 1))
        board.move(Location(3, 0))

        # player 2 makes a move
        board.select(expected_location)
        board.move(Location(4, 1))

        # player 1 takes over a piece of player 2
        board.select(Location(3, 0))
        board.capture(Location(4, 1))

        expected_to_contain_piece = board.contains_piece(expected_location)
        self.assertTrue(expected_to_contain_piece)

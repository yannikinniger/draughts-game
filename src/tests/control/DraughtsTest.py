import unittest

from src.control.AbstractDraughts import AbstractDraughts
from src.model.Player import Player


class DraughtsTest(unittest.TestCase):

    def test_should_create_board(self):
        player_1 = Player('Player 1', 1)
        player_2 = Player('Player 2', 2)
        draughts = AbstractDraughts(player_1, player_2)

        expected_board = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [0] * 8,
            [0] * 8,
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0]
        ]
        board = draughts.board

        self.assertEqual(expected_board, board)

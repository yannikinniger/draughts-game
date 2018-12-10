import unittest

from PyQt5.QtCore import Qt

from control.DraughtsGame import DraughtsGame
from src.model.Player import Player


class DraughtsGameTest(unittest.TestCase):

    def test_should_mark_available_moves(self):
        player_1 = Player('Player 1', 1, Qt.red)
        player_2 = Player('Player 2', 2, Qt.blue)
        draughts = DraughtsGame(player_1, player_2)

        draughts.click_event(2, 2)

        expected_board = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [-1, 0, -1, 1, 0, 1, 0, 1],
            [0] * 8,
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0]
        ]
        board = draughts.board

        self.assertEqual(expected_board, board)

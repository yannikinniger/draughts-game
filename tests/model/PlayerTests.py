import time
import unittest

from src.model.Player import Player


class PlayerTest(unittest.TestCase):

    def test_should_run_of_10_seconds(self):
        player = Player('test')
        player.start_timer()
        time.sleep(10)
        player.stop_timer()

        expected_remaining_time = 290
        remaining_time = player.remaining_time
        self.assertEqual(expected_remaining_time, remaining_time)

    def test_should_add_points(self):
        player = Player('test')
        player.add_points(1)
        player.add_points(2)
        player.add_points(3)

        expected_score = 6
        score = player.score
        self.assertEqual(expected_score, score)

    def test_should_raise_error_on_negative_points(self):
        player = Player('test')
        with self.assertRaises(ValueError):
            player.add_points(-1)
        with self.assertRaises(ValueError):
            player.add_points(0)

        expected_score = 0
        score = player.score
        self.assertEqual(expected_score, score)

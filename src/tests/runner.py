import unittest

from tests.control.AbstractDraughtsTest import AbstractDraughtsTest
from tests.control.DraughtsGameTest import DraughtsGameTest
from tests.model.PlayerTest import PlayerTest


def suite():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(test_loader.loadTestsFromTestCase(AbstractDraughtsTest))
    test_suite.addTests(test_loader.loadTestsFromTestCase(DraughtsGameTest))
    test_suite.addTests(test_loader.loadTestsFromTestCase(PlayerTest))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

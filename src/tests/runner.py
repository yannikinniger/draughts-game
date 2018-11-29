import unittest

from tests.control.DraughtsTest import DraughtsTest
from tests.model.PlayerTest import PlayerTest


def suite():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(test_loader.loadTestsFromTestCase(DraughtsTest))
    test_suite.addTests(test_loader.loadTestsFromTestCase(PlayerTest))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
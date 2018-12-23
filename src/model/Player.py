import time

from PyQt5.QtGui import QColor

from helper.Observer import Subject


class Player(Subject):

    def __init__(self, name, uid, direction, color):
        super().__init__()
        self.name = name
        self.uid = uid
        self.direction = direction
        if not isinstance(color, QColor):
            self.color = QColor(color)
        else:
            self.color = color

        self.score = 0
        self.remaining_time = 300.  # 5 Minutes in Seconds
        self.timer = 0

    def reset(self):
        """
        Resets the score and timers of the player.
        """
        self.score = 0
        self.remaining_time = 300.  # 5 Minutes in Seconds
        self.timer = 0

    def start_timer(self):
        """
        Starts a timer to measure the the remaining time
        """
        self.timer = time.perf_counter()

    def stop_timer(self):
        """
        Stops the timer to and subtracts the elapsed time since the timer was started from the remaining time
        """
        end_time = time.perf_counter()
        time_elapsed = round(end_time - self.timer)
        self.remaining_time -= time_elapsed
        self.timer = 0  # reset timer

    def add_points(self, points_to_add=1):
        """
        Adds point to the players score
        :param points_to_add: Positive integer to be added to the total score
        """
        if isinstance(points_to_add, int) and points_to_add > 0:
            self.score += points_to_add
            self._notify()
        else:
            raise ValueError('Points must be positive and of type integer')

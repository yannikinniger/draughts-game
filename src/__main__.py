from PyQt5.QtWidgets import QApplication

from DraughtsGame import DraughtsGame
import sys

app = QApplication([])
draughts = DraughtsGame()
sys.exit(app.exec_())

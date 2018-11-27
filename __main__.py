from PyQt5.QtWidgets import QApplication

from DraughtsGame import DraughtsGame
from draughts import Draughts
import sys

app = QApplication([])
draughts = Draughts()
# draughts = DraughtsGame()
sys.exit(app.exec_())

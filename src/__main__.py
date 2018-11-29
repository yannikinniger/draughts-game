import sys

from PyQt5.QtWidgets import QApplication

from DraughtsGame import DraughtsGame

if __name__ == '__main__':
    app = QApplication([])
    draughts = DraughtsGame()
    sys.exit(app.exec_())

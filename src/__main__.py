import sys

from PyQt5.QtWidgets import QApplication

from DraughtsWindow import DraughtsWindow

if __name__ == '__main__':
    app = QApplication([])
    draughts = DraughtsWindow()
    draughts.show()
    sys.exit(app.exec_())

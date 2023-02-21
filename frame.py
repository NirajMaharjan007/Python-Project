from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QMainWindow
from data.database import get_connection
from panels.login import Login, LoginActivity

import sys


app = QApplication(sys.argv)


class Frame(QWidget):
    def __init__(self):

        super().__init__()

        with open("./styles/styles.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        if get_connection() is not None:
            Login(self)

        else:
            reply = QMessageBox.critical(None, 'Message',
                                         "Error while connecting to the database",
                                         QMessageBox.StandardButton.Ok)

            if reply == QMessageBox.StandardButton.Ok:
                sys.exit(0)

        self.move(1024, 512)
        self.show()

        app.exec()


class FrameActivity(QWidget):
    def __init__(self):
        super().__init__()

        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        LoginActivity(self)
        self.move(1024, 380)
        self.adjustSize()
        self.show()

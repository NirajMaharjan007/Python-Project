from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtGui import QIcon
from data.database import get_connection
from panels.activities import Login, LoginActivity

from sys import exit, argv


app = QApplication(argv)


class Frame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('./resources/icon.png'))

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
                exit(0)

        self.move(500, 300)
        self.adjustSize()
        self.show()

        app.exec()


class FrameActivity(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('./resources/icon.png'))

        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)
        LoginActivity(self)

        self.setGeometry(200, 200, 950, 500)
        self.show()

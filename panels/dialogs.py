from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from data.database import get_login, get_adminId
from PyQt6.QtCore import Qt


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        label = QLabel('This is a dialog box!', self)

        button = QPushButton('Close', self)
        button.clicked.connect(self.close)

        layout = QVBoxLayout()

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)
        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()

        team = QLabel("Teams:")
        team.setObjectName("header")
        layout.addWidget(team)

        hlayout.addWidget(QLabel("Niraj maharjan"))
        layout.addLayout(hlayout)

        self.setLayout(layout)
        self.setFixedSize(256, 128)
        self.adjustSize()

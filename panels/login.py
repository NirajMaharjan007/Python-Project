import sys
from PyQt6.QtWidgets import *
from data.database import get_login


class Login:
    username: QLineEdit
    password: QLineEdit
    frame: QWidget

    def __init__(self, frame) -> QWidget:
        Login.frame = self.frame = frame

        hlayout = QHBoxLayout()
        layout = QFormLayout()

        Login.username = QLineEdit()

        Login.password = QLineEdit()
        Login.password.setEchoMode(QLineEdit.EchoMode.Password)

        Login.username.setObjectName("form-control")
        Login.password.setObjectName("form-control")

        self.ok = QPushButton("Login")
        self.ok.setObjectName("login")
        self.ok.clicked.connect(self.__Function.do)
        hlayout.addWidget(self.ok)

        self.cancel = QPushButton("Cancel")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.__Function.cancel)
        hlayout.addWidget(self.cancel)

        layout.addRow("username:", self.username)
        layout.addRow("password:", self.password)

        layout.addRow(hlayout)

        frame.setLayout(layout)

    class __Function():

        @ staticmethod
        def do(self):
            if get_login(Login.username.text(), Login.password.text()):
                print("Ok")

            else:
                print("Not Ok")
                QMessageBox.question(None, 'Error',
                                     "Username or Password is incorrect",
                                     QMessageBox.StandardButton.Ok)

        @staticmethod
        def cancel(self):
            reply = QMessageBox.warning(None, 'Message',
                                        "Do you want to exit?",
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                print("OMG! You are exiting")
                sys.exit(0)
            else:
                print("Well Done!\nGood Job!")

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from data.database import get_login
from PyQt6.QtCore import Qt
import frame


class Login:
    username: QLineEdit
    password: QLineEdit
    f: QWidget

    def __init__(self, fr):
        Login.f = fr
        Login.f.setWindowTitle("Login")

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

        Login.f.setLayout(layout)

    class __Function():

        @ staticmethod
        def do():
            if get_login(Login.username.text(), Login.password.text()):
                print("Ok")
                Login.f.setVisible(False)
                frame.FrameActivity()

            else:
                print("Not Ok")
                QMessageBox.question(None, 'Error',
                                     "Username or Password is incorrect",
                                     QMessageBox.StandardButton.Ok)

        @staticmethod
        def cancel():
            reply = QMessageBox.warning(None, 'Message',
                                        "Do you want to exit?",
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                print("OMG! You are exiting")
                sys.exit(0)
            else:
                print("Well Done!\nGood Job!")


class LoginActivity:
    f: QWidget

    def __init__(self, fr):
        LoginActivity.f = fr

        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()

        Menu(vlayout)

        header = QLabel('Welcome to Employee Dashboard!')
        header.setObjectName("header")

        vlayout.addWidget(header)

        hlayout.addWidget(QLabel('Employee dat'))
        hlayout.addWidget(QLabel("Hello world"))

        vlayout.addLayout(hlayout)

        LoginActivity.f.setWindowTitle('Dashboard')
        LoginActivity.f.setLayout(vlayout)


class Menu:
    layout: QBoxLayout

    def __init__(self, layout: QBoxLayout):
        self.layout = Menu.layout = layout
        self.fr = LoginActivity.f

        dialog = self.Dialog()

        menubar = QMenuBar()
        self.layout.setMenuBar(menubar)

        file_menu = menubar.addMenu('File')
        var = QAction("Varaibles", self.fr)
        var.triggered.connect(lambda: {
            print("Hello, world!"),
            print("Please"),
            dialog.exec()
        })

        file_menu.addAction(var)

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

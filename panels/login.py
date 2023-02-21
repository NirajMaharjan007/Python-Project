import frame
from sys import exit
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from data.database import get_login, get_adminId
from panels.dialogs import *


class Login:
    username: QLineEdit
    password: QLineEdit
    f: QWidget

    def __init__(self, fr):
        self.fr = Login.f = fr
        self.fr.setWindowTitle("Login")

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

        self.fr.setLayout(layout)

    class __Function():

        @ staticmethod
        def do():
            if get_login(Login.username.text(), Login.password.text()):
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
                exit(0)
            else:
                print("Well Done!\nGood Job!")


class LoginActivity:
    f: QWidget

    def __init__(self, fr):
        self.fr = LoginActivity.f = fr
        print("Admin id =>", get_adminId())

        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        Menu(vlayout)

        inside_frame = QFrame(self.fr)
        inside_frame.setFrameShape(QFrame.Shape.StyledPanel)
        inside_frame.setFrameShadow(QFrame.Shadow.Raised)
        inside_frame.setLayout(hlayout)

        header = QLabel('Welcome to Employee Dashboard!')
        header.setObjectName("header")
        header.move(0, 0)

        vlayout.addWidget(header)

        hlayout.addWidget(QLabel('Employee dat'))
        hlayout.addWidget(QLabel("Hello world"))

        vlayout.addWidget(inside_frame)

        self.fr.setWindowTitle('Dashboard')

        self.fr.setLayout(vlayout)


class Menu:
    layout: QBoxLayout

    def __init__(self, layout: QBoxLayout):
        self.layout = Menu.layout = layout
        self.fr = LoginActivity.f

        dialog = Dialog()
        about_dialog = AboutDialog()
        admin_dialog = AdminDialog()

        menubar = QMenuBar()
        self.layout.setMenuBar(menubar)

        file_menu = menubar.addMenu('File')
        admin_bar = menubar.addMenu('Admin')

        about_us = QAction("About us", self.fr)
        about_us.triggered.connect(lambda: about_dialog.exec())

        var = QAction("Varaibles", self.fr)
        var.triggered.connect(lambda: dialog.exec())

        admin_info = QAction("Admin info", self.fr)
        admin_info.triggered.connect(lambda: admin_dialog.exec())

        file_menu.addAction(var)
        file_menu.addAction(about_us)

        admin_bar.addAction(admin_info)

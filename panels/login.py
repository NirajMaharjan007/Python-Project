from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from data.database import get_adminId
from panels.dialogs import *
from panels.layouts import *


class Login:
    f: QWidget

    def __init__(self, fr):
        Login.f = fr

        self.f.setWindowTitle("Login")
        LoginFormLayout(self.f)


class LoginActivity:
    f: QWidget

    def __init__(self, fr):
        self.fr = LoginActivity.f = fr
        print("Admin id =>", get_adminId())

        container = Container(self.fr)
        Menu(container)

        self.fr.setWindowTitle('Dashboard')

        self.fr.setLayout(container)


class Menu:
    layout: QBoxLayout

    def __init__(self, layout: QBoxLayout):
        self.layout = Menu.layout = layout
        self.fr = LoginActivity.f
        self.login_frame = Login.f

        dialog = Dialog()
        about_dialog = AboutDialog()
        admin_dialog = AdminDialog()
        emp_dialog = EmployeeDialog()

        menubar = QMenuBar()
        self.layout.setMenuBar(menubar)

        logout = QMenu('Logout', self.fr)
        logout.aboutToShow.connect(lambda: {self.fr.setVisible(False),
                                            self.login_frame.setVisible(True)})

        file_menu = menubar.addMenu('File')
        admin_bar = menubar.addMenu('Admin')

        about_us = QAction("About us", self.fr)
        about_us.triggered.connect(lambda: about_dialog.exec())

        var = QAction("Varaibles", self.fr)
        var.triggered.connect(lambda: dialog.exec())

        admin_info = QAction("Admin info", self.fr)
        admin_info.triggered.connect(lambda: admin_dialog.exec())

        emp_set = QAction("Add Employees", self.fr)
        emp_set.triggered.connect(lambda: emp_dialog.exec())

        file_menu.addAction(var)
        file_menu.addAction(about_us)

        admin_bar.addAction(emp_set)
        admin_bar.addAction(admin_info)

        menubar.addMenu(logout)

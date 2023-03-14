from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
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
        LoginActivity.f = fr
        print("Admin id =>", get_adminId())

        container = Container(self.f)

        Menu(container)

        self.f.setWindowTitle('Dashboard')
        self.f.setLayout(container)


class Menu(QMenuBar):
    layout: QBoxLayout

    def __init__(self, layout: QBoxLayout):
        super().__init__()

        self.layout = Menu.layout = layout
        self.fr = LoginActivity.f
        self.login_frame = Login.f

        about_dialog = AboutDialog()
        admin_dialog = AdminDialog()
        emp_dialog = EmployeeDialog()

        self.layout.setMenuBar(self)

        admin_bar = self.addMenu('Admin')
        option_bar = self.addMenu('Option')

        about_us = QAction("About us", self.fr)
        about_us.triggered.connect(lambda: about_dialog.exec())

        admin_info = QAction("Admin info", self.fr)
        admin_info.triggered.connect(lambda: admin_dialog.exec())

        emp_set = QAction("Add Employees", self.fr)
        emp_set.triggered.connect(lambda: emp_dialog.exec())

        logout = QAction('Logout', self.fr)
        logout.triggered.connect(lambda: {self.fr.setVisible(False),
                                          self.login_frame.setVisible(True)})

        admin_bar.addAction(emp_set)
        admin_bar.addAction(admin_info)

        option_bar.addAction(about_us)
        option_bar.addAction(logout)

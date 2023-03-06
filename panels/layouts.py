from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from data.database import Employee, get_login
from panels.tables import *
from sys import exit
import frame


class Container(QVBoxLayout):
    frame: QWidget

    def __init__(self, frame=QWidget):
        super().__init__()

        Container.frame = frame

        tab = QTabWidget()

        employee_frame = EmployeeFrame()
        inside_frame = QFrame()

        self.setContentsMargins(8, 4, 8, 4)
        self.setAlignment(Qt.AlignmentFlag.AlignTop |
                          Qt.AlignmentFlag.AlignVCenter)

        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()

        header = QLabel('Welcome to Employee Dashboard!')
        header.setAlignment(Qt.AlignmentFlag.AlignCenter |
                            Qt.AlignmentFlag.AlignBottom)
        header.setObjectName("header")
        vlayout.addWidget(header)

        hlayout.addLayout(vlayout)
        hlayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        inside_frame.setFrameShape(QFrame.Shape.Panel)
        inside_frame.setFrameShadow(QFrame.Shadow.Raised)
        inside_frame.setLayout(hlayout)

        label = QLabel("Employee Summary")
        label.setObjectName("header2_underline")
        employee_frame.table.update()

        vlayout.addWidget(label)
        vlayout.addWidget(QLabel("Employees count: " +
                          str(Employee().get_count())))
        vlayout.addWidget(employee_frame)

        # self.addWidget(inside_frame)
        # self.addWidget(employee_frame)

        tab.addTab(inside_frame, "Main Tab")
        tab.addTab(EmployeePerformance(), "Performance")
        tab.adjustSize()
        tab.show()

        self.addWidget(tab)


class EmployeePerformance(QFrame):
    # => TODO: Find a better way to do this

    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        vlay = QVBoxLayout()

        header = QLabel("Details of Employee Performance")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignTop)
        header.setObjectName("header")
        vlay.addWidget(header)

        self.setLayout(vlay)


class EmployeeFrame(QFrame):
    def __init__(self):
        super().__init__()

        vlay = QVBoxLayout()
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignBottom)

        self.table = TableDisplay()

        blayout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        blayout.setContentsMargins(0, 0, 0, 0)
        blayout.setAlignment(Qt.AlignmentFlag.AlignLeft |
                             Qt.AlignmentFlag.AlignTop)

        header = QLabel("Employees Details")
        header.setObjectName("header2_underline")

        blayout.addWidget(header)

        vlay.addLayout(blayout)

        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        vlay.addWidget(self.table)

        self.setLayout(vlay)


class LoginFormLayout(QFormLayout):
    admin: QLineEdit
    password: QLineEdit
    f: QWidget

    def __init__(self, frame=QWidget):
        super().__init__()
        LoginFormLayout.f = frame

        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 8, 0, 0)

        LoginFormLayout.admin = QLineEdit()
        LoginFormLayout.password = QLineEdit()

        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.admin.setObjectName("form-control")
        self.password.setObjectName("form-control")

        self.ok = QPushButton("Login")
        self.ok.setObjectName("login")
        self.ok.clicked.connect(self.__Function.do)
        self.admin.returnPressed.connect(self.ok.click)
        self.password.returnPressed.connect(self.ok.click)
        hlayout.addWidget(self.ok)

        self.cancel = QPushButton("Cancel")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.__Function.cancel)
        hlayout.addWidget(self.cancel)

        self.addRow("Enter Admin's name:", self.admin)
        self.addRow("Enter Admin's password:", self.password)

        self.addRow(hlayout)

        self.f.adjustSize()
        self.f.setFixedSize(300, 120)
        self.f.setLayout(self)

    class __Function():
        @ staticmethod
        def do():
            admin = LoginFormLayout.admin
            password = LoginFormLayout.password

            if get_login(admin.text(), password.text()):
                admin.setText("")
                password.setText("")

                LoginFormLayout.f.setVisible(False)
                frame.FrameActivity()

            else:
                print("Not Ok")
                QMessageBox.question(None, 'Error', "Admin name or Password is incorrect",
                                     QMessageBox.StandardButton.Ok)

        @ staticmethod
        def cancel():
            reply = QMessageBox.warning(None, 'Message', "Are you sure about that?",
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                print("OMG! You are exiting")
                exit(0)
            else:
                print("Well Done!\nGood Job!")

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from data.database import get_login
from panels.tables import *
import panels.dialogs as dialog
from sys import exit
import frame


class Container(QVBoxLayout):
    frame: QWidget

    def __init__(self, frame=QWidget):
        super().__init__()

        Container.frame = frame

        tab = QTabWidget()

        employee_frame = EmployeeFrame()
        employee_perform = EmployeePerformance()
        employee_chart = EmployeeChart()
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

        vlayout.addWidget(employee_frame)

        # self.addWidget(inside_frame)
        # self.addWidget(employee_frame)

        tab.addTab(inside_frame, "Main Tab")
        tab.addTab(employee_perform, "Performance")
        tab.addTab(employee_chart, "Employee Chart")
        tab.adjustSize()
        tab.show()

        self.addWidget(tab)


class EmployeePerformance(QFrame):
    # => TODO: Find a better way to do this

    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.WinPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

        vlay = QVBoxLayout()
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignTop)

        hlay = QHBoxLayout()
        hlay.setAlignment(Qt.AlignmentFlag.AlignLeft |
                          Qt.AlignmentFlag.AlignTop)

        table_vlay = QVBoxLayout()
        table_perform = PerformanceTable()

        table_frame = QFrame()
        table_frame.setFrameShape(QFrame.Shape.Box)
        table_frame.setFrameShadow(QFrame.Shadow.Raised)

        header_layout = QVBoxLayout()
        header = QLabel("Stats of Employee Performance")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignBottom)
        header.setObjectName("header")
        header_layout.addWidget(header)

        header2 = QLabel("Table of Employee Performance")
        header2.setObjectName("header2_underline")
        header2.setAlignment(Qt.AlignmentFlag.AlignBottom)

        hlay.addWidget(header2)
        hlay.addWidget(table_perform.get_refresh_btn())

        table_vlay.addLayout(hlay)
        table_vlay.addWidget(table_perform)

        table_frame.setLayout(table_vlay)

        vlay.addLayout(header_layout)
        vlay.addWidget(table_frame)

        self.setLayout(vlay)


class EmployeeFrame(QFrame):
    def __init__(self):
        super().__init__()

        emp_dialog = dialog.EmployeeDialog()

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

        add_emp = QPushButton("Add Employee")
        add_emp.setObjectName("info")
        add_emp.setFixedSize(120, 30)
        add_emp.clicked.connect(lambda: emp_dialog.exec())

        refresh = QPushButton("Refresh")
        refresh.setObjectName("refresh")
        refresh.setFixedSize(75, 30)
        refresh.clicked.connect(self.table.get_update_function)

        blayout.addWidget(header)
        blayout.addWidget(refresh)
        blayout.addWidget(add_emp)

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


class EmployeeChart(QFrame):
    refresh: QPushButton

    def update_emp_frame(self):
        pass

    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.WinPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

        vlay = QVBoxLayout()
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignTop)

        hlay = QHBoxLayout()
        hlay.setAlignment(Qt.AlignmentFlag.AlignCenter |
                          Qt.AlignmentFlag.AlignBaseline)

        self.refresh = QPushButton("Refresh")
        self.refresh.setObjectName("refresh")
        self.refresh.setFixedSize(75, 30)
        self.refresh.clicked.connect(self.update_emp_frame)

        hlay.addWidget(self.refresh)

        label = QLabel("Detail Charts of Employees")
        label.setObjectName("header2_underline")
        label.setAlignment(Qt.AlignmentFlag.AlignTop |
                           Qt.AlignmentFlag.AlignHCenter)

        header = QLabel("Employee's Charts")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignTop)

        emp = Employee()
        count = emp.get_count()
        inner_frame = []

        for i in range(count):
            inner_frame.append(self.__Inner_Frame())

        grid_lay = QGridLayout()
        grid_lay.setColumnMinimumWidth(6, 10)
        grid_lay.setContentsMargins(4, 2, 4, 2)
        grid_lay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                              Qt.AlignmentFlag.AlignTop)

        row = 0
        column = 0

        for i in range(count):
            if column == 3:
                column = 0
                row += 1

            grid_lay.addWidget(inner_frame[i], row, column)
            column += 1

        vlay.addWidget(header)
        vlay.addWidget(label)
        vlay.addLayout(hlay)
        vlay.addLayout(grid_lay)

        self.setLayout(vlay)

    class __Inner_Frame(QFrame):
        def __init__(self):
            self.emp = Employee()

            super().__init__()

            self.setFrameShape(QFrame.Shape.WinPanel)
            self.setFrameShadow(QFrame.Shadow.Raised)

            hlayout = QHBoxLayout()
            hlayout.setContentsMargins(0, 0, 0, 0)
            hlayout.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                                 Qt.AlignmentFlag.AlignTop)
            hlayout.addWidget(QLabel("Hello World"))

            emp_frame = QFrame()
            emp_frame.setFrameShape(QFrame.Shape.Panel)
            emp_frame.setFrameShadow(QFrame.Shadow.Raised)
            emp_frame.setLayout(hlayout)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setContentsMargins(0, 0, 0, 0)

            label = QLabel("Name: ")
            label.setAlignment(Qt.AlignmentFlag.AlignTop |
                               Qt.AlignmentFlag.AlignHCenter)
            label.setObjectName("header2_underline")

            layout.addWidget(label)
            layout.addWidget(emp_frame)

            self.setLayout(layout)

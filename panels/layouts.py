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

    def __init__(self):
        inner_frame = self.__Inner_Frame()

        super().__init__()

        self.setFrameShape(QFrame.Shape.WinPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

        vlay = QVBoxLayout()
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignTop)

        header = QLabel("Employees' Charts")
        header.setAlignment(Qt.AlignmentFlag.AlignTop |
                            Qt.AlignmentFlag.AlignHCenter)
        header.setObjectName("header")

        vlay.addWidget(header)
        vlay.addWidget(inner_frame)

        self.setLayout(vlay)

    class __Inner_Frame(QFrame):
        def __init__(self):
            emp = Employee()

            super().__init__()

            self.setFrameShape(QFrame.Shape.Box)
            self.setFrameShadow(QFrame.Shadow.Sunken)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setContentsMargins(0, 0, 0, 0)

            label = QLabel("Description")
            label.setAlignment(Qt.AlignmentFlag.AlignTop |
                               Qt.AlignmentFlag.AlignHCenter)
            label.setObjectName("header2_underline")

            layout.addWidget(label)
            self.__set_frame(layout)

            self.setLayout(layout)

        def __set_frame(self, layout: QVBoxLayout):
            grid = QGridLayout()
            grid.setAlignment(Qt.AlignmentFlag.AlignLeading |
                              Qt.AlignmentFlag.AlignJustify)
            grid.setContentsMargins(2, 4, 2, 8)

            row = col = 0
            count = Employee().get_count()

            li = []
            emp_detail = Employee().get_employee_detail()

            for i in range(count):
                if emp_detail is not None:
                    print(emp_detail[i][0])
                    li.append(self.__Employee_frame(emp_detail[i][0],
                                                    emp_detail[i][1]))

                if count % 2 == 0:
                    if col == 4:
                        row += 1
                        col = 0
                else:
                    if col == 3:
                        row += 1
                        col = 0

                grid.addWidget(li[i], row, col)
                col += 1

            layout.addLayout(grid)

        class __Employee_frame(QFrame):
            def __init__(self, emp_id: int, name: str) -> None:
                super().__init__()

                self.setFrameShape(QFrame.Shape.WinPanel)
                self.setFrameShadow(QFrame.Shadow.Raised)

                self.setContentsMargins(8, 4, 8, 4)
                self.setSizePolicy(QSizePolicy.Policy.Minimum,
                                   QSizePolicy.Policy.Minimum)

                main_layout = QVBoxLayout()
                inner_layout = QFormLayout()
                hlayout = QHBoxLayout()
                hlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                label = QLabel("Employee Info")
                label.setAlignment(Qt.AlignmentFlag.AlignTop |
                                   Qt.AlignmentFlag.AlignHCenter)
                label.setObjectName("header2_underline")

                emp_id_label = QLabel("Employee Id:")
                emp_id_label.setObjectName("bold-font")

                emp_name = QLabel("Name: ")
                emp_name.setObjectName("bold-font")

                inner_layout.addRow(emp_id_label, QLabel(str(emp_id)))
                inner_layout.addRow(emp_name, QLabel(str(name)))

                btn = QPushButton("Click Me")
                btn.setFixedSize(70, 30)
                btn.clicked.connect(lambda: print("Show chart"))

                hlayout.addWidget(btn)

                main_layout.addWidget(label)
                main_layout.addLayout(inner_layout)
                main_layout.addLayout(hlayout)

                self.setLayout(main_layout)

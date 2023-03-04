from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from data.database import Employee, get_login
from sys import exit
import frame


class Container(QVBoxLayout):
    frame: QWidget

    def __init__(self, frame=QWidget):
        super().__init__()

        self.frame = Container.frame = frame

        self.setContentsMargins(8, 4, 8, 4)
        self.setAlignment(Qt.AlignmentFlag.AlignTop |
                          Qt.AlignmentFlag.AlignVCenter)

        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        employee = Employee()

        hlayout.addLayout(vlayout)
        hlayout.setAlignment(Qt.AlignmentFlag.AlignVCenter
                             | Qt.AlignmentFlag.AlignTop)

        inside_frame = QFrame(self.frame)
        inside_frame.setFrameShape(QFrame.Shape.WinPanel)
        inside_frame.setFrameShadow(QFrame.Shadow.Raised)
        inside_frame.setLayout(hlayout)

        header = QLabel('Welcome to Employee Dashboard!')
        header.setAlignment(Qt.AlignmentFlag.AlignCenter |
                            Qt.AlignmentFlag.AlignBottom)
        header.setObjectName("header")

        self.addWidget(header)

        label = QLabel("Employee Summary")
        label.setObjectName("header2_underline")
        vlayout.addWidget(label)
        vlayout.addWidget(QLabel("Employees count: "
                                 + str(employee.count)))

        self.addWidget(inside_frame)
        self.addWidget(EmployeeFrame(self.frame))


class EmployeeFrame(QFrame):
    f: QWidget

    def __init__(self, f=QWidget):
        EmployeeFrame.f = f
        super().__init__()

        vlay = QVBoxLayout()

        table = TableDisplay()

        blayout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        blayout.setContentsMargins(0, 0, 0, 0)
        blayout.setAlignment(Qt.AlignmentFlag.AlignLeft |
                             Qt.AlignmentFlag.AlignBottom)

        header = QLabel("Employees Details",  self.f)
        header.setObjectName("header2_underline")

        blayout.addWidget(header)
        vlay.addLayout(blayout)

        self.setFrameShape(QFrame.Shape.WinPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

        vlay.addWidget(table)

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

        @staticmethod
        def cancel():
            reply = QMessageBox.warning(None, 'Message', "Are you sure about that?",
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                print("OMG! You are exiting")
                exit(0)
            else:
                print("Well Done!\nGood Job!")


class TableDisplay(QTableWidget):
    # frame: QWidget

    def __init__(self):
        super().__init__()

        employee = Employee()

        header_labels = ["emp_id", "Emp_name", "address", "email",
                         "dob", "gender", "phone_no", ""]

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,
                           QSizePolicy.Policy.Preferred)

        self.setRowCount(employee.count)
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(header_labels)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        data = employee.get_employee_detail()

        if data is not None:
            for row_index, row_data in enumerate(data):
                for column_index, column_data in enumerate(row_data):
                    if column_index == 0:
                        cell_widget = self.__CellWidget(self, column_data)
                        cell_widget.delete.setProperty("row", column_index)
                        self.setCellWidget(row_index, 7, cell_widget)

                    item = QTableWidgetItem(str(column_data))
                    self.setItem(row_index, column_index, item)

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        self.adjustSize()
        self.update()

    class __CellWidget(QWidget):
        emp_id: int
        update: QPushButton
        delete: QPushButton

        def __init__(self, table=QTableWidget, emp_id=int):
            self.employee = Employee()
            self.table = table
            super().__init__()

            self.emp_id = emp_id
            cell_layout = QHBoxLayout()
            self.update = QPushButton("Edit")
            self.update.setObjectName("update")
            self.update.clicked.connect(lambda: print(self.emp_id))

            self.delete = QPushButton("Delete")
            self.delete.setObjectName("delete")
            self.delete.clicked.connect(self.__delete)

            cell_layout.addWidget(self.update)
            cell_layout.addWidget(self.delete)
            cell_layout.setContentsMargins(2, 4, 2, 4)

            self.setLayout(cell_layout)

        def __delete(self):
            msg = QMessageBox()

            result = QMessageBox.critical(
                msg, "Delete", "Are you sure you want to", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if result == QMessageBox.StandardButton.Yes:
                if self.employee.delete(self.emp_id):
                    # Get the row index of the button that was clicked
                    button = self.sender()
                    row = button.property("row")

                    # Remove the row from the table
                    self.table.removeRow(row)
                    msg.information(
                        msg, "Delete", "data deleted", msg.StandardButton.Close)
                    self.table.update()
                    print("Deleted")

        def __edit(self):
            msg = QMessageBox()
            pass

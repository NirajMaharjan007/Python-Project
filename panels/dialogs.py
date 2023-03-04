from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from data.database import Employee
from datetime import datetime

import panels.layouts as lay


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


class AdminDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        self.setWindowTitle("Admin's Information")

        layout = QVBoxLayout()

        label = QLabel('Admin\'s details', self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter |
                           Qt.AlignmentFlag.AlignTop)
        label.setObjectName("header")

        layout.addWidget(label)

        self.setLayout(layout)
        self.setFixedSize(256, 128)
        self.adjustSize()


class EmployeeDialog(QDialog):
    __table: lay.TableDisplay

    @staticmethod
    def set_tableWidget(table=lay.TableDisplay):
        EmployeeDialog.__table = table

    def __init__(self):
        super().__init__()

        self.emp = Employee()

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        with open("./styles/styles.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        self.setWindowTitle("Add Employees")

        form = QFormLayout()
        hlayout = QHBoxLayout()
        radio_layout = QHBoxLayout()

        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        male_radio.toggled.connect(self.__set_gender)
        female_radio.toggled.connect(self.__set_gender)

        radio_layout.addWidget(QLabel("Select Gender:"))
        radio_layout.addWidget(male_radio)
        radio_layout.addWidget(female_radio)

        self.name = QLineEdit()
        self.name.setObjectName("form-control")

        self.address = QLineEdit()
        self.address.setObjectName("form-control")

        self.email = QLineEdit()
        self.email.setObjectName("form-control")

        self.dob = QLineEdit()
        self.dob.setObjectName("form-control")

        self.phone = QLineEdit()
        self.phone.setObjectName("form-control")

        save = QPushButton("Save")
        save.setObjectName("login")
        save.clicked.connect(self.__save)

        cancel = QPushButton("Cancel")
        cancel.setObjectName("cancel")
        cancel.clicked.connect(lambda: self.close())

        hlayout.addWidget(save)
        hlayout.addWidget(cancel)

        form.addRow("Employee's name", self.name)
        form.addRow("Employee's email", self.email)
        form.addRow("Employee's address", self.address)
        form.addRow("Employee's date of birth", self.dob)
        form.addRow("Employee's phone number", self.phone)
        form.addRow(radio_layout)
        form.addRow(hlayout)

        self.setLayout(form)
        self.setFixedSize(410, 235)
        self.adjustSize()

    def __set_gender(self):
        sender = self.sender()
        if sender.isChecked():
            self.gender = sender.text()

    def __save(self):
        try:
            message_box = QMessageBox()
            message_box.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

            name = self.name.text()
            address = self.address.text()
            email = self.email.text()
            dob = datetime.strptime(self.dob.text(), '%Y-%m-%d').date()
            gender = self.gender
            phone = int(self.phone.text())

            print(name, address, email, dob, gender, phone)

            if name == '' or address == '' or email == '':
                raise Exception("The Text field should not be blank")

            elif self.emp.set_employee(name, address, email, dob, gender, phone):
                emp_id = int(self.emp.get_empId())
                list = [emp_id, name, address, email,
                        dob, gender, phone]

                row_position = self.__table.rowCount()
                self.__table.insertRow(row_position)
                self.__table.setCellWidget(
                    row_position, 7, self.__table.get_widget(self.__table, emp_id))

                for column in range(len(list)):
                    item = QTableWidgetItem(str(list[column]))
                    self.__table.setItem(row_position, column, item)

                status = "Successfully added employee details\nRequried to re-login"
                message_box.information(message_box, 'Success', status,
                                        QMessageBox.StandardButton.Close)
            else:
                raise Exception("Failed to add employee details")

        except Exception as err:
            print(err)
            message_box.critical(message_box, 'Error',
                                 str(err), QMessageBox.StandardButton.Close)

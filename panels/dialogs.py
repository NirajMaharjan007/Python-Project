from random import randint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QFile
from data.database import Employee
from datetime import datetime

import panels.layouts as lay


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle("About us")
        self.setWindowIcon(QIcon("./resources/about-us-22-32.png"))
        with open("./styles/custom.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        inner_layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop |
                            Qt.AlignmentFlag.AlignVCenter)

        team = QLabel("Teams:")
        team.setAlignment(Qt.AlignmentFlag.AlignTop |
                          Qt.AlignmentFlag.AlignHCenter)
        team.setObjectName("header")

        inner_layout.addWidget(team)
        self.__info(inner_layout)

        layout.addLayout(inner_layout)
        self.setLayout(layout)

    def __info(self, layout: QBoxLayout):
        row = col = 0
        grid = QGridLayout()

        li = []
        name = ["Binita Lamichhane", "Jenisha Karki",
                "Niraj Maharjan", "Ruses Maharjan", "Samir Maharjan"]

        gender = ["Female", "Female", "Male", "Not Found", "Not Found"]

        ph = ["9808280005", "9840259835",
              "9813545029", "Not Found", "9813498649"]

        email = ["Lamichhanebinita23@gmail.com",
                 "jenishakarki8@gmail.com", "niraj.mhrjn770@gmail.com", "pandamaharjan@gmail.com",
                 "sameermaharjan982@gmail.com"]

        for i in range(5):
            li.append(self.__InfoWidget(name[i], gender[i], ph[i], email[i]))

            if col == 3:
                col = 0
                row += 1

            grid.addWidget(li[i], row, col)
            col += 1

        layout.addLayout(grid)

    class __InfoWidget(QFrame):
        def __init__(self, name, gender, phone, email):
            super().__init__()
            self.setFrameShape(QFrame.Shape.WinPanel)
            self.setFrameShadow(QFrame.Shadow.Raised)
            self.setContentsMargins(4, 2, 4, 2)
            self.setSizePolicy(
                QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

            main_layout = QVBoxLayout()
            main_layout.setContentsMargins(4, 0, 4, 0)

            header = QLabel("Team information")
            header.setAlignment(Qt.AlignmentFlag.AlignCenter |
                                Qt.AlignmentFlag.AlignTop)
            header.setObjectName("header2_underline")

            inner_layout = QFormLayout()

            name_label = QLabel("Name: ")
            name_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            name_label.setObjectName("bold-font")

            gender_label = QLabel("Gender: ")
            gender_label.setObjectName("bold-font")

            ph_label = QLabel("Ph no.: ")
            ph_label.setObjectName("bold-font")

            email_label = QLabel("Email: ")
            email_label.setObjectName("bold-font")

            inner_layout.addRow(name_label, QLabel(name))
            inner_layout.addRow(ph_label, QLabel(phone))
            inner_layout.addRow(email_label, QLabel(email))
            inner_layout.addRow(gender_label, QLabel(gender))

            main_layout.addWidget(header)
            main_layout.addLayout(inner_layout)

            self.setLayout(main_layout)


class AdminDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

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

    @ staticmethod
    def set_tableWidget(table=lay.TableDisplay):
        EmployeeDialog.__table = table

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./resources/icon.png"))

        self.emp = Employee()

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        with open("./styles/styles.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        self.setWindowTitle("Add Employees detail")

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

            emp_id = randint(1, 3000)
            name = self.name.text()
            address = self.address.text()
            email = self.email.text()
            dob = datetime.strptime(self.dob.text(), '%Y-%m-%d').date()
            gender = self.gender
            phone = int(self.phone.text())

            print(emp_id, name, address, email, dob, gender, phone)

            if name == '' or address == '' or email == '':
                raise Exception("The Text field should not be blank")

            elif self.emp.set_employee(emp_id, name, address, email, dob, gender, phone):
                list = [emp_id, name, address, email,
                        dob, gender, phone]
                row_position = self.__table.rowCount()
                widget = self.__table.get_widget(self.__table, emp_id)
                widget.delete.setProperty("row", row_position)
                self.__table.insertRow(row_position)
                self.__table.setCellWidget(
                    row_position, 7, widget)

                for column in range(len(list)):
                    item = QTableWidgetItem(str(list[column]))
                    self.__table.setItem(row_position, column, item)

                status = "Successfully added employee details\nHit Refresh to update table."
                message_box.information(message_box, 'Success', status,
                                        QMessageBox.StandardButton.Close)

            else:
                raise Exception("Failed to add employee details")

        except Exception as err:
            print(err)
            message_box.critical(message_box, 'Error',
                                 str(err), QMessageBox.StandardButton.Close)


class EditEmployeeDialog(QDialog):
    def __init__(self, emp_id):
        super().__init__()
        self.emp = Employee()
        self.emp_id = emp_id

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        with open("./styles/styles.css") as f:
            style = f.read()
            self.setStyleSheet(style)

        self.setWindowTitle("Update Employees detail")

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

        self.update_btn = QPushButton("Update")
        self.update_btn.setObjectName("login")
        self.update_btn.clicked.connect(self.__update)

        cancel = QPushButton("Cancel")
        cancel.setObjectName("cancel")
        cancel.clicked.connect(lambda: self.close())

        hlayout.addWidget(self.update_btn)
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

    def __update(self):
        message_box = QMessageBox()
        message_box.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        try:
            name = self.name.text()
            address = self.address.text()
            email = self.email.text()
            dob = datetime.strptime(self.dob.text(), '%Y-%m-%d').date()
            gender = self.gender
            phone = int(self.phone.text())

            if self.emp.update_info(self.emp_id, name, address, email, dob, gender, phone):
                status = "Successfully updated employee details\nRequired to Logout from session"
                message_box.information(message_box, 'Success', status,
                                        QMessageBox.StandardButton.Close)

            else:
                status = "Failed, updated employee details"
                message_box.critical(message_box, 'Failed', status,
                                     QMessageBox.StandardButton.Close)

        except Exception as e:
            print("Error =>", e)
            message_box.critical(message_box, 'Error',
                                 str(e), QMessageBox.StandardButton.Close)


class AddPerform(QDialog):
    def __init__(self, emp_id=int):
        super().__init__()
        self.emp = Employee()

        self.emp_id = emp_id
        self.emp_name = self.emp.get_emp_name(emp_id)

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle("Add Performer")

        with open("./styles/styles.css") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

        header = QLabel("Emp_Name:" + str(self.emp_name))
        with open("./styles/custom.css") as file:
            stylesheet = file.read()
            header.setStyleSheet(stylesheet)

        header.setObjectName("header2")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignTop)

        vlay = QVBoxLayout()
        vlay.setContentsMargins(8, 0, 8, 0)
        vlay.addWidget(header)
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignTop)

        form = QFormLayout()
        form.setAlignment(Qt.AlignmentFlag.AlignCenter |
                          Qt.AlignmentFlag.AlignTop)
        form.setContentsMargins(0, 0, 0, 0)

        self.res = QLineEdit()
        self.res.setObjectName("form-control")

        self.attitude = QLineEdit()
        self.attitude.setObjectName("form-control")

        self.project = QLineEdit()
        self.project.setObjectName("form-control")

        form.addRow("Set Result: ", self.res)
        form.addRow("Set Attitude: ", self.attitude)
        form.addRow("Set Finish Project: ", self.project)

        hlay = QHBoxLayout()
        hlay.setContentsMargins(2, 8, 2, 4)
        hlay.setAlignment(Qt.AlignmentFlag.AlignCenter |
                          Qt.AlignmentFlag.AlignBottom)

        add = QPushButton("Add")
        add.setFixedSize(75, 30)
        add.setObjectName("login")
        add.clicked.connect(self.__add_data)

        cancel = QPushButton("Cancel")
        cancel.setFixedSize(75, 30)
        cancel.setObjectName("cancel")
        cancel.clicked.connect(lambda: self.close())

        hlay.addWidget(add)
        hlay.addWidget(cancel)

        vlay.addLayout(form)
        vlay.addLayout(hlay)

        self.setLayout(vlay)
        self.setFixedSize(350, 200)

    def __add_data(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        res = self.res.text()
        attitude = self.attitude.text()
        project = self.project.text()

        data = self.emp.insert_performance(self.emp_id, res, attitude, project)

        if data:
            msg.information(
                msg, "Success", "Required to hit refresh", msg.StandardButton.Close)
            self.close()

        else:
            msg.information(
                msg, "Failed", "Failed to insert data", msg.StandardButton.Close)


class UpdatePerform(QDialog):
    def __init__(self, emp_id=int):
        super().__init__()
        self.emp = Employee()

        self.emp_name = self.emp.get_emp_name(emp_id)

        self.emp_id = emp_id

        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle("Update Performer Data")

        with open("./styles/styles.css") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

        header = QLabel("Emp_Name:" + str(self.emp_name))
        with open("./styles/custom.css") as file:
            stylesheet = file.read()
            header.setStyleSheet(stylesheet)

        header.setObjectName("header2")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignTop)

        vlay = QVBoxLayout()
        vlay.setContentsMargins(8, 0, 8, 0)
        vlay.addWidget(header)
        vlay.setAlignment(Qt.AlignmentFlag.AlignVCenter |
                          Qt.AlignmentFlag.AlignTop)

        form = QFormLayout()
        form.setAlignment(Qt.AlignmentFlag.AlignCenter |
                          Qt.AlignmentFlag.AlignTop)
        form.setContentsMargins(0, 0, 0, 0)

        self.res = QLineEdit()
        self.res.setObjectName("form-control")

        self.attitude = QLineEdit()
        self.attitude.setObjectName("form-control")

        self.project = QLineEdit()
        self.project.setObjectName("form-control")

        form.addRow("Set Result: ", self.res)
        form.addRow("Set Attitude: ", self.attitude)
        form.addRow("Set Finish Project: ", self.project)

        hlay = QHBoxLayout()
        hlay.setContentsMargins(2, 8, 2, 4)
        hlay.setAlignment(Qt.AlignmentFlag.AlignCenter |
                          Qt.AlignmentFlag.AlignBottom)

        add = QPushButton("Update")
        add.setFixedSize(75, 30)
        add.setObjectName("login")
        add.clicked.connect(self.__add_data)

        cancel = QPushButton("Cancel")
        cancel.setFixedSize(75, 30)
        cancel.setObjectName("cancel")
        cancel.clicked.connect(lambda: self.close())

        hlay.addWidget(add)
        hlay.addWidget(cancel)

        vlay.addLayout(form)
        vlay.addLayout(hlay)

        self.setLayout(vlay)
        self.setFixedSize(350, 200)

    def __add_data(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        res = self.res.text()
        attitude = self.attitude.text()
        project = self.project.text()

        data = self.emp.update_performance(self.emp_id, res, attitude, project)

        if data:
            msg.information(
                msg, "Success", "Data Update. \nRequired to hit refresh", msg.StandardButton.Close)

        else:
            msg.information(
                msg, "Failed", "Failed to Update data", msg.StandardButton.Close)

import panels.dialogs as dialog
from PyQt6.QtWidgets import *
from data.database import Employee


class TableDisplay(QTableWidget):
    table_performace: QTableWidget

    def __init__(self):
        super().__init__()

        employee = Employee()

        dialog.EmployeeDialog.set_tableWidget(self)

        header_labels = ["emp_id", "Emp_name", "address", "email",
                         "dob", "gender", "phone_no", ""]

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,
                           QSizePolicy.Policy.Expanding)

        self.setRowCount(employee.count)
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(header_labels)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.data = employee.get_employee_detail()

        if self.data is not None:
            for row_index, row_data in enumerate(self.data):
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

    def get_widget(self, table: QTableWidget, data):
        return self.__CellWidget(table, data)

    class __CellWidget(QWidget):
        emp_id: int
        update: QPushButton
        delete: QPushButton

        # def __init__(self, table=QTableWidget):

        def __init__(self, table=QTableWidget, emp_id=int):
            self.employee = Employee()
            self.emp_id = emp_id
            self.table = table

            super().__init__()

            cell_layout = QHBoxLayout()
            self.update = QPushButton("Edit")
            self.update.setObjectName("update")
            self.update.clicked.connect(self.__edit)

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
                    print("Deleted")

        def __edit(self):
            emp_dialog = dialog.EditEmployeeDialog(self.emp_id)
            emp_dialog.exec()


class PerformanceTable(QTableWidget):
    emp_id: int
    refresh: QPushButton

    def get_refresh_btn(self) -> QPushButton:
        self.refresh.setObjectName("refresh")
        self.refresh.setFixedSize(75, 30)
        self.refresh.clicked.connect(self.__update_table)
        return self.refresh

    def __init__(self):
        super().__init__()
        self.employee = Employee()

        PerformanceTable.refresh = QPushButton("Refresh")

        header_labels = ["emp_id", "Emp_name", "result", "attitude",
                         "project_completed", "present_days", "absent_days", ""]

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSizePolicy(QSizePolicy.Policy.Preferred,
                           QSizePolicy.Policy.Expanding)

        self.setRowCount(self.employee.count)
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(header_labels)

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        data = self.employee.get_performance()

        if data is not None:
            for row_index, row_data in enumerate(data):
                for column_index, column_data in enumerate(row_data):
                    if column_index == 0:
                        cell_widget = self.cell_widget = self.__ButtonWidget(
                            self, column_data)

                    if column_index >= 2:
                        if column_data == None:
                            cell_widget.set_add_btn()
                        else:
                            cell_widget.set_update_btn()

                        self.setCellWidget(row_index, 7, cell_widget)

                    item = QTableWidgetItem(str(column_data))
                    self.setItem(row_index, column_index, item)

        self.adjustSize()

    def __update_table(self):
        self.clearContents()
        self.setRowCount(0)
        self.update()

        data = Employee().get_performance()

        if data is not None:
            num_rows = len(data)
            self.setRowCount(num_rows)
            for row_index, row_data in enumerate(data):
                for column_index, column_data in enumerate(row_data):
                    if column_index == 0:
                        cell_widget = self.__ButtonWidget(self, column_data)

                    if column_index >= 2:
                        if column_data == None:
                            cell_widget.set_add_btn()
                        else:
                            cell_widget.set_update_btn()

                        self.setCellWidget(row_index, 7, cell_widget)

                    item = QTableWidgetItem(str(column_data))
                    self.setItem(row_index, column_index, item)

        print("update table")

    class __ButtonWidget(QWidget):
        emp_id: int
        table: QTableWidget
        update_btn: QPushButton
        add_btn: QPushButton

        def get_empId(self):
            return self.emp_id

        def __init__(self, table=QTableWidget, emp_id=int):
            super().__init__()
            self.table = table
            self.emp_id = emp_id

            self.hlay = QHBoxLayout()
            self.hlay.setContentsMargins(4, 2, 4, 2)

            self.add_btn = QPushButton("Add")
            self.add_btn.setObjectName("info")
            self.add_btn.clicked.connect(lambda: print(emp_id))

            self.update_btn = QPushButton("Update")
            self.update_btn.setObjectName("update")
            self.update_btn.clicked.connect(lambda: print(emp_id))

        def set_update_btn(self):
            self.hlay.addWidget(self.update_btn)

            self.setLayout(self.hlay)

        def set_add_btn(self):
            self.hlay.addWidget(self.add_btn)

            self.setLayout(self.hlay)

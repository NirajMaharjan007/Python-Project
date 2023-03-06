import panels.dialogs as dialog
from PyQt6.QtWidgets import *
from data.database import Employee


class TableDisplay(QTableWidget):

    def __init__(self):
        super().__init__()

        employee = Employee()

        dialog.EmployeeDialog.set_tableWidget(self)

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

    def __init__(self, emp_id=int):
        super().__init__()
        self.emp_id = emp_id
        employee = Employee()
        self.data = employee.get_performence()
        if self.data is not None:
            for row_index, row_data in enumerate(self.data):
                for column_index, column_data in enumerate(row_data):
                    item = QTableWidgetItem(str(column_data))
                    self.setItem(row_index, column_index, item)

        else:
            for row_index, row_data in enumerate(self.data):
                for column_index, column_data in enumerate(row_data):
                    item = QTableWidgetItem("None")
                    self.setItem(row_index, column_index, item)

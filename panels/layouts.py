from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from data.database import Employee


class Container(QVBoxLayout):
    frame: QWidget

    def __init__(self, frame=QWidget):
        super().__init__()

        self.frame = Container.frame = frame

        hlayout = QHBoxLayout()
        employee = Employee()

        inside_frame = QFrame(self.frame)
        inside_frame.setFrameShape(QFrame.Shape.WinPanel)
        inside_frame.setFrameShadow(QFrame.Shadow.Raised)
        inside_frame.setLayout(hlayout)

        header = QLabel('Welcome to Employee Dashboard!')
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                            Qt.AlignmentFlag.AlignTop)
        header.setObjectName("header")

        self.addWidget(header)

        hlayout.addWidget(
            QLabel("Employees count: " + str(employee.get_count())))

        self.addWidget(inside_frame)
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QDial, QLabel
from PySide2.QtCore import Signal
import sys

class CustomSignal(QWidget):
    pressure = Signal()

    def __init__(self):
        super(CustomSignal, self).__init__()

        main_layout = QVBoxLayout(self)

        self.dial = QDial()
        main_layout.addWidget(self.dial)

        self.allert_label = QLabel()
        main_layout.addWidget(self.allert_label)

        self.dial.sliderMoved.connect(self.check_value)

        self.pressure.connect(self.pressure_allert)

    def check_value(self, value):
        if value >= 50:
            self.pressure.emit()

    def pressure_allert(self):
        self.allert_label.setText("To much pressure!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CustomSignal()
    win.show()
    app.exec_()
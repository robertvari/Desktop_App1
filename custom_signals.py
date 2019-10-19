from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QDial, QLabel
import sys

class CustomSignal(QWidget):
    def __init__(self):
        super(CustomSignal, self).__init__()

        main_layout = QVBoxLayout(self)

        self.dial = QDial()
        main_layout.addWidget(self.dial)

        self.allert_label = QLabel()

    def pressure_allert(self):
        self.allert_label.setText("To much pressure!!!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CustomSignal()
    win.show()
    app.exec_()
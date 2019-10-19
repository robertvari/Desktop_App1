from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
import sys

class CSSWindow(QWidget):
    def __init__(self):
        super(CSSWindow, self).__init__()

        self.setWindowTitle("CSS Test")

        main_layout = QVBoxLayout(self)

        text_field = QLineEdit()
        main_layout.addWidget(text_field)

        button = QPushButton("Click")
        main_layout.addWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CSSWindow()
    win.show()
    app.exec_()
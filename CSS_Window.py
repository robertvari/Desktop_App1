from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, \
    QVBoxLayout, QTextEdit
import sys

class CSSWindow(QWidget):
    def __init__(self):
        super(CSSWindow, self).__init__()

        self.setWindowTitle("CSS Test")
        self.resize(400, 0)

        main_layout = QVBoxLayout(self)

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Name...")
        main_layout.addWidget(self.name_field)

        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Phone...")
        main_layout.addWidget(self.phone_field)

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email...")
        main_layout.addWidget(self.email_field)

        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Address...")
        main_layout.addWidget(self.address_field)

        self.message = QTextEdit()
        main_layout.addWidget(self.message)

        button = QPushButton("Save")
        main_layout.addWidget(button)

        self.apply_style()

    def apply_style(self):
        with open("style.css") as f:
            self.setStyleSheet(f.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CSSWindow()
    win.show()
    app.exec_()
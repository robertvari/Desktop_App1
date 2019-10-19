from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import sys, json

class ContactForm(QWidget):
    def __init__(self):
        super(ContactForm, self).__init__()
        self.setWindowTitle("My Contact Form")
        self.resize(400, 0)

        # main layout
        main_layout = QVBoxLayout(self)

        # line edits
        name_field = QLineEdit()
        name_field.setPlaceholderText("Name...")
        main_layout.addWidget(name_field)

        phone_field = QLineEdit()
        phone_field.setPlaceholderText("Phone...")
        main_layout.addWidget(phone_field)

        email_field = QLineEdit()
        email_field.setPlaceholderText("Email...")
        main_layout.addWidget(email_field)

        address_field = QLineEdit()
        address_field.setPlaceholderText("Address...")
        main_layout.addWidget(address_field)

        save_btn = QPushButton("Save")
        main_layout.addWidget(save_btn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ContactForm()
    win.show()
    app.exec_()
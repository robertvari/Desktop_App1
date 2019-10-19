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

        save_btn = QPushButton("Save")
        main_layout.addWidget(save_btn)

        # connect signals
        save_btn.clicked.connect(self.save_action)

    def check_fields(self):

        for k,v in self.user_data.items():
            if not len(v):
                print(f'{k} has no value!')
                return False

        return True

    def save_action(self):
        self.user_data = {
            "name": self.name_field.text(),
            "phone": self.phone_field.text(),
            "email": self.email_field.text(),
            "address": self.address_field.text(),
        }

        if self.check_fields():
            with open("contact_list.json", "a") as f:
                json.dump(self.user_data, f)

            self.name_field.clear()
            self.phone_field.clear()
            self.email_field.clear()
            self.address_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ContactForm()
    win.show()
    app.exec_()
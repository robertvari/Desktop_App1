from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import sys, json

class ContactForm(QWidget):
    def __init__(self):
        super(ContactForm, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ContactForm()
    win.show()
    app.exec_()
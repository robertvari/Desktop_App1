from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, \
    QPushButton, QVBoxLayout, QHBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("My Window")

        main_layout = QVBoxLayout(self)

        button = QPushButton("Click Me")
        main_layout.addWidget(button)

        button.clicked.connect(self.test_click)

    def test_click(self):
        print("Button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QPushButton
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # main layout has to have central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        button = QPushButton("Click")
        main_layout.addWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
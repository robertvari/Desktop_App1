from PySide2.QtWidgets import QWidget, QVBoxLayout, QApplication
import sys

from CSS_Window import CSSWindow

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        main_layout = QVBoxLayout(self)

        css_widget1 = CSSWindow()
        main_layout.addWidget(css_widget1)

        css_widget2 = CSSWindow()
        main_layout.addWidget(css_widget2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
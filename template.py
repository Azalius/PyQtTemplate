from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("example.ui", self)

        self.show()

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Template")

    window = MainWindow()
    app.exec_()

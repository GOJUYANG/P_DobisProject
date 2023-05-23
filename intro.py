import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect, QPushButton, QVBoxLayout

from_class = uic.loadUiType("./ui_src/intro.ui")[0]


class WindowClass(QDialog, from_class):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_1)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

    def btn_1(self):
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_2)
        self.stackedWidget.setCurrentIndex(1)

    def btn_2(self):
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_3)
        self.stackedWidget.setCurrentIndex(2)

    def btn_3(self):
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_4)
        self.stackedWidget.setCurrentIndex(3)

    def btn_4(self):
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_5)
        self.stackedWidget.setCurrentIndex(4)

    def btn_5(self):
        self.timer.start(1300)
        self.timer.timeout.connect(self.btn_6)
        self.stackedWidget.setCurrentIndex(0)

    def btn_6(self):
        # self.timer.start(1000)
        # self.timer.timeout.connect(self.btn_5)
        self.stackedWidget.setCurrentIndex(5)




    # def fade(self):
    #     for i in range(50):
    #         i = i / 100
    #         self.setWindowOpacity(1 - i)
    #         time.sleep(0.01)
    #     # self.close()
    #
    # def close(self):
    #     sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1500, 800)

        self.frame = QFrame(self)
        self.frame.resize(700, 700)

        # 라벨 생성 및 위치 조정
        self.label = QLabel(self.frame)
        self.label.setGeometry(50, 50, 35, 35)
        # self.label.setPixmap(QPixmap('./img_src/character.png'))
        self.label.setStyleSheet("background-color: red;")

    def keyPressEvent(self, event):
        # 방향키 누를 때마다 라벨 위치 조정
        if event.key() == Qt.Key_Left:
            x = self.label.x() - int(self.frame.width() / 20)
            if x < 0:
                x = 0
            self.label.move(x, self.label.y())
            print(self.label.x(), self.label.y())
        elif event.key() == Qt.Key_Right:
            x = self.label.x() + int(self.frame.width() / 20)
            if x > self.frame.width() - self.label.width():
                x = self.frame.width() - self.label.width()
            self.label.move(x, self.label.y())
            print(self.label.x(), self.label.y())
        elif event.key() == Qt.Key_Up:
            y = self.label.y() - int(self.frame.height() / 20)
            if y < 0:
                y = 0
            self.label.move(self.label.x(), y)
            print(self.label.x(), self.label.y())
        elif event.key() == Qt.Key_Down:
            y = self.label.y() + int(self.frame.height() / 20)
            if y > self.frame.height() - self.label.height():
                y = self.frame.height() - self.label.height()
            self.label.move(self.label.x(), y)
            print(self.label.x(), self.label.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWidget()
    main.show()
    sys.exit(app.exec())

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainFrame(QMainWindow):
    def __init__(self):
        pass

        # 상시고정
            # 메인화면
                # 필드

                # 던전

                # 전투

            # 아이템창
                # 포션

                # 운석

                # 텐트

            # 로그창
                # 알림

                # 경고

            # 클래스창
                # HP

                # MP

                # 공격

                # 장비


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    sys.exit(app.exec_())




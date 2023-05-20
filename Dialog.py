from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic.properties import QtCore


class CustomDialog(QDialog):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

        QBtn = QDialogButtonBox.StandardButton.Ok
        # QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(self.msg)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class ChoiceJopDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.msg = '아이템을 사용할 캐릭터를 선택해주세요!'
        self.job = ''

        self.list_job = ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white']

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(self.msg)
        self.layout.addWidget(message)
        for job in self.list_job:
            radio_job = QRadioButton(job)
            radio_job.clicked.connect(lambda x, y=radio_job.text(): self.return_job(y))
            self.layout.addWidget(radio_job)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def return_job(self, job):
        print(job)
        self.job = job

    def accept(self):
        if self.job == '':
            pass
        else:
            self.close()

from view.gard_name import Ui_Dialog


# 수호대 직업별 이름 부여
class GiveGardName(QDialog, Ui_Dialog):
    def __init__(self, gard):
        super().__init__()
        self.setupUi(self)
        self.gard_name = ''
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.list_gard = {'빛': 'light_gard', '달': 'moon_gard', '별': 'star_gard', '대지': 'earth_gard'}
        self.lb_gard_frame.setPixmap(QPixmap(f'img_src/name/{gard}_name.png'))
        self.lb_gard_frame.setScaledContents(True)
        self.lb_gard_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for k, v in self.list_gard.items():
            if v == gard:
                self.lb_gard_type.setText(f'{k}의 수호대')
                break
        self.movie = QMovie(f"./img_src/gard/{gard}.gif")
        self.lb_gard_img.setScaledContents(True)
        self.lb_gard_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_gard_img.setMovie(self.movie)
        self.movie.start()
        self.le_gard_name.setPlaceholderText("수호대 이름.")
        self.le_gard_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if gard == 'light_gard':
            self.le_gard_name.setStyleSheet(
                "border-style: solid;border-width: 3px;border-color: red;border-radius: 3px;text-align: center;")
            self.pb_save.setStyleSheet(
                "QPushButton{color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 11, 30, 255), stop:1 rgba(176, 43, 33, 255));border-radius: 20px;}")
        if gard == 'moon_gard':
            self.le_gard_name.setStyleSheet(
                "border-style: solid;border-width: 3px;border-color: blue;border-radius: 3px;text-align: center;")
            self.pb_save.setStyleSheet(
                "QPushButton{color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(15, 82, 186, 255), stop:1 rgba(15, 130, 180, 255));border-radius: 20px;}")
        if gard == 'star_gard':
            self.lb_gard_type.setStyleSheet("color: black;")
            self.le_gard_name.setStyleSheet(
                "color: black;border-style: solid;border-width: 3px;border-color: lightgrey;border-radius: 3px;text-align: center;")
            self.pb_save.setStyleSheet(
                "QPushButton{color: black;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(201, 219, 218, 255), stop:1 rgba(201, 240, 210, 255));border-radius: 20px;}")
        if gard == 'earth_gard':
            self.le_gard_name.setStyleSheet(
                "border-style: solid;border-width: 3px;border-color: green;border-radius: 3px;text-align: center;")
            self.pb_save.setStyleSheet(
                "QPushButton{color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(15, 157, 88, 255), stop:1 rgba(15, 180, 78, 255));border-radius: 20px;}")

        self.pb_save.clicked.connect(self.return_name)

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key.Key_Escape:
            pass

        if event.key() == 16777220:
            if len(self.le_gard_name.text()) > 0:
                self.pb_save.click()

    def return_name(self):
        self.gard_name = f'{self.lb_gard_type.text()} [{self.le_gard_name.text()}]'

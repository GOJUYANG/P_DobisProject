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
        self.job = job


from view.gard_name import Ui_Dialog


# 수호대 직업별 이름 부여
class GiveGardName(QDialog, Ui_Dialog):
    def __init__(self, gard):
        super().__init__()
        self.setupUi(self)
        self.gard_name = ''
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.list_gard = {'빛': 'light_gard', '달': 'moon_gard', '별': 'star_gard', '땅': 'earth_gard'}
        for k, v in self.list_gard.items():
            if v == gard:
                self.lb_gard_type.setText(f'{k}의 수호대')
                break
        self.movie = QMovie(f"./img_src/gard/{gard}.gif")
        self.lb_gard_img.setScaledContents(True)
        self.lb_gard_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_gard_img.setMovie(self.movie)
        self.movie.start()
        self.le_gard_name.setPlaceholderText("수호대에게 이름을 부여해주세요.")
        self.le_gard_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pb_save.clicked.connect(self.return_name)

    def return_name(self):
        self.gard_name = f'{self.lb_gard_type.text()} [{self.le_gard_name.text()}]'

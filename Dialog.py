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


class Choice_Jop_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.msg = '아이템을 사용할 캐릭터를 선택해주세요!'
        self.job = ''

        self.list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']

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

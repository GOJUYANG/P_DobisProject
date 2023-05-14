import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Equipment import Equipment

class MainClass(QMainWindow, Equipment):
    def __init__(self):
        super().__init__()
        # 수호대 리스트
        self.list_gard = ['light_gard', 'moon_gard', 'star_gard', 'earth_gard']
        # 직업 리스트
        self.list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']
        # 필드 리스트
        self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        # 수호대
        self.dict_gard = {'gard': '',
                          'location': {'region': '', 'x': 0, 'y': 0},
                          'warrior': {'survival': True,
                                      'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                      'equipment': [],
                                      'skill': {10: 'slice_chop'}},
                          'archer': {'survival': True,
                                     'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 300,
                                     'equipment': [],
                                     'skill': {10: 'target_shot',
                                               15: 'dual_shot',
                                               20: 'master_shot'}},
                          'swordman': {'survival': True,
                                       'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 250,
                                       'equipment': [],
                                       'skill': {10: 'slice_chop'}},
                          'wizard_red': {'survival': True,
                                         'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 150,
                                         'equipment': [],
                                         'skill': {1: ['heal_normal', 'fire_ball'],
                                                   15: ['heal_greater', 'fire_wall'],
                                                   20: 'thunder_breaker',
                                                   25: 'bilzzard',
                                                   30: 'heal_all'}},
                          'wizard_black': {'survival': True,
                                           'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                           'equipment': [],
                                           'skill': {1: 'fire_ball',
                                                     15: 'fire_wall',
                                                     20: 'thunder_breaker',
                                                     25: 'bilzzard'}},
                          'wizard_white': {'survival': True,
                                           'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 100,
                                           'equipment': [],
                                           'skill': {1: 'heal_normal',
                                                     15: 'heal_greater',
                                                     30: 'heal_all'}}}

        self.wear_equipment('swordman', 'horse_helmet', self.dict_gard)
        print(self.dict_gard)


    # 수호대 상태 갱신
    # @property
    # def dict_gard(self):
    #     return self.dict_gard
    # @dict_gard.setter
    # def dict_gard(self, dict_gard):
    #     self.dict_gard = dict_gard

    # 이동
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


    def update_gard_stat(self, gard):
        self.dict_gard = gard

    # 로그창 갱신
    def renew_log_view(self):
        list_widget = QListWidget()
        # Add an item to the list widget
        item = QListWidgetItem("")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")
        list_widget.addItem("아이템을 획득하였습니다.")

    # 아이템창 갱신
    def renew_item_view(self):
        pass

    # 장비창 띄우기
    def click_equip_button(self):
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
    main = MainClass()
    main.show()
    sys.exit(app.exec_())



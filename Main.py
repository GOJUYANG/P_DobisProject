import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Equipment import Equipment

class MainFrame(QMainWindow):
    def __init__(self):
        # 수호대 리스트
        self.list_gard = ['light_gard', 'moon_gard', 'star_gard', 'earth_gard']
        # 직업 리스트
        self.list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']
        # 필드 리스트
        self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        # 수호대
        self.dict_grad = {'gard': '',
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

        self.click_equip_button()


    def call_dict_grad(self):
        return self.dict_grad

    # 장비 버튼 클릭
    def click_equip_button(self):
        # 검사 장비 착용
        b = Equipment(job='swordman', equipment='horse_helmet')
        b.wear_equipment()
        print(b.dict_grad)
        b.take_off_equipment()
        print(b.dict_grad)


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

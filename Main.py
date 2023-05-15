import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from Equipment import EquipmentClass
from view.main_frame import Ui_MainWindow


class MainClass(QMainWindow, Ui_MainWindow, EquipmentClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.in_cnt = 0

        # 수호대 리스트
        self.list_gard = [{'빛': 'light_gard'}, {'달': 'moon_gard'}, {'별': 'star_gard'}, {'땅': 'earth_gard'}]

        # 필드 리스트
        self.dict_field = {'불': False, '물': False, '숲': False, '눈': False}

        # 아이템 리스트
        self.dict_item = {'부활포션': [0, 'img_src/item/부활포션.png'],
                          '텐트': [0, 'img_src/item/텐트.png'],
                          'ALL포션(상)': [0, 'img_src/item/올3.png'],
                          'ALL포션(중)': [0, 'img_src/item/올2.png'],
                          'ALL포션(하)': [0, 'img_src/item/올1.png'],
                          'HP포션(상)': [0, 'img_src/item/빨간3.png'],
                          'HP포션(중)': [0, 'img_src/item/빨간2.png'],
                          'HP포션(하)': [0, 'img_src/item/빨간1.png'],
                          'MP포션(상)': [0, 'img_src/item/파란3.png'],
                          'MP포션(중)': [0, 'img_src/item/파란2.png'],
                          'MP포션(하)': [0, 'img_src/item/파란1.png']}
        # 수호대
        self.dict_user_gard = {'gard': '',
                               'location': {'region': '', 'x': 0, 'y': 0},
                               'warrior': {'survival': True,
                                           'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                           'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                         'bronze_sword'],
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

        # 필드에 이미지 넣기
        self.forest_area.setPixmap(
            QPixmap('./img_src/forest_map.jpg').scaled(self.forest_area.width(), self.forest_area.height(),
                                                       Qt.KeepAspectRatio))
        self.forest_area.setScaledContents(True)
        self.fire_area.setPixmap(
            QPixmap('./img_src/fire_map.jpg').scaled(self.fire_area.width(), self.fire_area.height(),
                                                     Qt.KeepAspectRatio))
        self.fire_area.setScaledContents(True)
        self.snow_area.setPixmap(
            QPixmap('./img_src/snow_map.gif').scaled(self.snow_area.width(), self.snow_area.height(),
                                                     Qt.KeepAspectRatio))
        self.snow_area.setScaledContents(True)
        self.water_area.setPixmap(
            QPixmap('./img_src/water_map.jpg').scaled(self.water_area.width(), self.water_area.height(),
                                                      Qt.KeepAspectRatio))
        self.water_area.setScaledContents(True)

        # 시그널
        self.pb_equip_job_1.clicked.connect(lambda: self.click_equip_button('warrior'))
        self.pb_equip_job_2.clicked.connect(lambda: self.click_equip_button('archer'))
        self.pb_equip_job_3.clicked.connect(lambda: self.click_equip_button('swordman'))
        self.pb_equip_job_4.clicked.connect(lambda: self.click_equip_button('wizard_red'))
        self.pb_equip_job_5.clicked.connect(lambda: self.click_equip_button('wizard_black'))
        self.pb_equip_job_6.clicked.connect(lambda: self.click_equip_button('wizard_white'))

        # 수호대 랜덤지정
        self.random_assign_gard()

        # 수호대 필드 랜덤배치
        self.img_gard = QLabel(self.stack_field)
        self.x, self.y = self.random_assign_field()
        self.img_gard.move(self.x, self.y)
        self.alarm_where_field(self.x, self.y)
        # print(self.x * int(self.stack_field.width() / 20), self.y * int(self.stack_field.width() / 20))

        # 수호대 사이즈 조절
        self.img_gard.resize(int(self.stack_field.width() / 20), int(self.stack_field.height() / 20))
        # self.img_gard.setPixmap(QPixmap('./img_src/character.png'))
        # self.img_gard.setScaledContents(True)
        if self.dict_user_gard['gard'] == 'light_gard':
            color_ = 'white'
        elif self.dict_user_gard['gard'] == 'moon_gard':
            color_ = 'black'
        elif self.dict_user_gard['gard'] == 'star_gard':
            color_ = 'yellow'
        else:
            color_ = 'blue'
        self.img_gard.setStyleSheet(f"background-color: {color_};")

        # 장비 착용 및 해제
        self.wear_equip('swordman', 'horse_helmet', self.dict_user_gard)
        print(self.dict_user_gard)
        self.take_off_equip('swordman', 'horse_helmet', self.dict_user_gard)
        print(self.dict_user_gard)

        # 아이템창에 아이템 넣기
        self.renew_item_view()

    # 화면 크기 조절 이벤트
    def resizeEvent(self, event):
        print(self.stack_field.width(), self.stack_field.height())
        if self.img_gard.isVisible():
            self.img_gard.move(self.x, self.y)
            self.img_gard.resize(int(self.stack_field.width() / 20), int(self.stack_field.height() / 20))

    # 키 입력 이벤트
    def keyPressEvent(self, event):
        # 방향키 누를 때마다 라벨 위치 조정
        if event.key() == Qt.Key_Left:
            self.x = self.img_gard.x() - int(self.stack_field.width() / 20)
            if self.x < 0:
                self.x = 0
            self.img_gard.move(self.x, self.img_gard.y())
            print(self.img_gard.x(), self.img_gard.y())
        elif event.key() == Qt.Key_Right:
            self.x = self.img_gard.x() + int(self.stack_field.width() / 20)
            if self.x > self.stack_field.width() - self.img_gard.width():
                self.x = self.stack_field.width() - self.img_gard.width()
            self.img_gard.move(self.x, self.img_gard.y())
            print(self.img_gard.x(), self.img_gard.y())
        elif event.key() == Qt.Key_Up:
            self.y = self.img_gard.y() - int(self.stack_field.height() / 20)
            if self.y < 0:
                self.y = 0
            self.img_gard.move(self.img_gard.x(), self.y)
            print(self.img_gard.x(), self.img_gard.y())
        elif event.key() == Qt.Key_Down:
            self.y = self.img_gard.y() + int(self.stack_field.height() / 20)
            if self.y > self.stack_field.height() - self.img_gard.height():
                self.y = self.stack_field.height() - self.img_gard.height()
            self.img_gard.move(self.img_gard.x(), self.y)
            print(self.img_gard.x(), self.img_gard.y())

        self.alarm_where_field(self.x, self.y)

    # 수호대 랜덤배치
    def random_assign_gard(self):
        dict_one = random.choice(self.list_gard)
        print(dict_one)
        for k, v in dict_one.items():
            self.dict_user_gard['gard'] = v
            # 알림
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'당신은 {k}의 기운을 부여받으셨습니다.')
        self.list_gard.remove(dict_one)

    # 필드(집결지) 랜덤배치
    def random_assign_field(self):
        self.int_x = random.randint(1, 20) * int(self.stack_field.width() / 20)
        self.int_y = random.randint(1, 20) * int(self.stack_field.width() / 20)
        return self.int_x, self.int_y

    def alarm_where_field(self, int_x, int_y):
        # 알림
        if int_x < self.stack_field.width() / 2 and int_y < self.stack_field.height() / 2 and not self.dict_field['불']:
            self.dict_field['불'] = True
            self.dict_field['눈'] = False
            self.dict_field['숲'] = False
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'불의 지역에 입장하였습니다.')
        if int_x > self.stack_field.width() / 2 and int_y < self.stack_field.height() / 2 and not self.dict_field['눈']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = True
            self.dict_field['숲'] = False
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'눈의 지역에 입장하였습니다.')
        if int_x < self.stack_field.width() / 2 and int_y > self.stack_field.height() / 2 and not self.dict_field['숲']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = True
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'숲의 지역에 입장하였습니다.')
        if int_x > self.stack_field.width() / 2 and int_y > self.stack_field.height() / 2 and not self.dict_field['물']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = False
            self.dict_field['물'] = True
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'물의 지역에 입장하였습니다.')

    # 로그창 갱신
    def renew_log_view(self, q_icon, str_msg):
        # icon = QIcon('./img_src/alarm.png')
        icon_item = QListWidgetItem(q_icon, str_msg)
        icon_item.setFlags(icon_item.flags() & ~icon_item.flags())
        self.list_log.addItem(icon_item)
        self.list_log.scrollToItem(icon_item)

    # 아이템창 갱신
    def renew_item_view(self):
        self.table_item.setRowCount(len(self.dict_item))
        self.table_item.setColumnCount(1)
        self.table_item.horizontalHeader().setStretchLastSection(True)
        idx = 0
        for k, v in self.dict_item.items():
            item = QTableWidgetItem(f"{k} : {v[0]}개")
            item.setIcon(QIcon(f"{v[1]}"))
            self.table_item.setItem(idx, 0, item)
            idx += 1

    # 장비창 띄우기
    def click_equip_button(self, str_job):
        dlg = EquipmentClass()
        # 획득한 장비 중 직업별 착용 가능 장비 보여주기
        for item in dlg.dict_job_equip[str_job]:
            for k, v in dlg.dict_equipment.items():
                if k == item and v[1] > 0:
                    item = QListWidgetItem(f"{v[0]} : {v[1]}개")
                    dlg.list_unworn.addItem(item)

        # 클래스 별 착용 장비 보여주기
        for item in self.dict_user_gard[str_job]['equipment']:
            for k, v in dlg.dict_equipment.items():
                if k == item:
                    item = QListWidgetItem(f"{v[0]}")
                    dlg.list_wear.addItem(item)
        dlg.exec_()

        dlg.pb_wear.clicked.connect(self.wear_equip())



    # 타 수호대와의 조우
    def meet_other_guardian(self):
        # 우리 수호대 제외
        self.list_gard.remove(self.dict_grad_stat['gard'])
        # 리스트 셔플
        random.shuffle(self.list_gard)
        other_gard = self.list_gard.pop()
        return other_gard

    # 치트키
    def use_cheatkey(self):
        if self.str_cheatkey == 'easter_egg':
            pass


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

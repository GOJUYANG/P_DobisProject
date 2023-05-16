import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from view.main_frame import Ui_MainWindow
from Equipment import EquipmentClass
from Item import ItemClass
from Dungeon import mazeClass
from Field import FieldClass


class MainClass(QMainWindow, Ui_MainWindow, ItemClass, mazeClass, FieldClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 필드 전투 턴
        self.field_turn = 0

        # 던전 전투 턴
        self.maze_turn = 0

        # 수호대 리스트
        self.list_gard = [{'빛': 'light_gard'}, {'달': 'moon_gard'}, {'별': 'star_gard'}, {'땅': 'earth_gard'}]

        # 필드 리스트
        self.dict_field = {'불': False, '물': False, '숲': False, '눈': False}

        # 획득한 아이템 리스트 / 변수명 :  아이템명, 보유개수, 이미지소스
        self.dict_item = {'resurrection_potion': {'name': '부활포션', 'count': 0, 'image': 'img_src/item/부활포션.png'},
                          'tent': {'name': '텐트', 'count': 0, 'image': 'img_src/item/텐트.png'},
                          'all_potion_high': {'name': 'ALL포션(상)', 'count': 0, 'image': 'img_src/item/올3.png'},
                          'all_potion_middle': {'name': 'ALL포션(중)', 'count': 0, 'image': 'img_src/item/올2.png'},
                          'all_potion_low': {'name': 'ALL포션(하)', 'count': 0, 'image': 'img_src/item/올1.png'},
                          'hp_potion_high': {'name': 'HP포션(상)', 'count': 0, 'image': 'img_src/item/빨간3.png'},
                          'hp_potion_middle': {'name': 'HP포션(중)', 'count': 0, 'image': 'img_src/item/빨간2.png'},
                          'hp_potion_low': {'name': 'HP포션(하)', 'count': 0, 'image': 'img_src/item/빨간1.png'},
                          'mp_potion_high': {'name': 'MP포션(상)', 'count': 0, 'image': 'img_src/item/파란3.png'},
                          'mp_potion_middle': {'name': 'MP포션(중)', 'count': 0, 'image': 'img_src/item/파란2.png'},
                          'mp_potion_low': {'name': 'MP포션(하)', 'count': 0, 'image': 'img_src/item/파란1.png'}}

        # 획득한 장비 리스트 / 변수명 :  아이템명, 보유개수, 효과, 이미지
        self.dict_equipment = {
            'black_armor': {'name': '블랙 아머', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'black_cape': {'name': '블랙 망토', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'black_glove': {'name': '블랙 글로브', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'black_pants': {'name': '블랙 팬츠', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'blue_armor': {'name': '블루 아머', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'blue_cape': {'name': '블루 망토', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'blue_glove': {'name': '블루 글로브', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'blue_hood': {'name': '블루 후드', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'blue_pants': {'name': '블루 팬츠', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'bronze_armor': {'name': '브론즈 아머', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'bronze_bow': {'name': '브론즈 보우', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 10, 'image': ''},
            'bronze_pants': {'name': '브론즈 팬츠', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'bronze_shield': {'name': '브론즈 쉴드', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'bronze_staff': {'name': '브론즈 롱스태프', 'count': 0, 'max_hp': 0, 'max_mp': 3, 'power': 7, 'image': ''},
            'bronze_sword': {'name': '브론즈 소드', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 10, 'image': ''},
            'bronze_wand': {'name': '브론즈 숏스태프', 'count': 0, 'max_hp': 0, 'max_mp': 10, 'power': 0, 'image': ''},
            'chain_armor': {'name': '체인 아머', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'chain_pants': {'name': '체인 팬츠', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'chain_shield': {'name': '체인 쉴드', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'cow_armor': {'name': '소가죽 아머', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'cow_cape': {'name': '소가죽 망토', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'cow_glove': {'name': '소가죽 글로브', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'cow_helmet': {'name': '소가죽 헬멧', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'cow_pants': {'name': '소가죽 팬츠', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'croc_cape': {'name': '악어 망토', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'croc_glove': {'name': '악어 글로브', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'diamond_gem': {'name': '다이아 룬스태프', 'count': 0, 'max_hp': 0, 'max_mp': 9, 'power': 9, 'image': ''},
            'gold_armor': {'name': '골드 아머', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'gold_bow': {'name': '골드 보우', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 30, 'image': ''},
            'gold_helmet': {'name': '골드 헬멧', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'gold_pants': {'name': '골드 팬츠', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'gold_staff': {'name': '골드 롱스태프', 'count': 0, 'max_hp': 0, 'max_mp': 9, 'power': 21, 'image': ''},
            'gold_sword': {'name': '골드 소드', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 30, 'image': ''},
            'gold_wand': {'name': '골드 숏스태프', 'count': 0, 'max_hp': 0, 'max_mp': 30, 'power': 0, 'image': ''},
            'high_chain_glove': {'name': '튼튼한 체인 글로브', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'horse_armor': {'name': '말가죽 아머', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'horse_cape': {'name': '말가죽 망토', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'horse_glove': {'name': '말가죽 글로브', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'horse_helmet': {'name': '말가죽 헬멧', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'horse_pants': {'name': '말가죽 팬츠', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'iron_armor': {'name': '아이언 아머', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'iron_pants': {'name': '아이언 팬츠', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'iron_shield': {'name': '아이언 쉴드', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'leather_shield': {'name': '가죽 방패', 'count': 0, 'max_hp': 3, 'max_mp': 0, 'power': 0, 'image': ''},
            'low_chain_glove': {'name': '낡은 체인 글로브', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'middle_chain_glove': {'name': '체인 글로브', 'count': 0, 'max_hp': 7, 'max_mp': 0, 'power': 0, 'image': ''},
            'red_armor': {'name': '레드 아머', 'count': 0, 'max_hp': 1, 'max_mp': 0, 'power': 0, 'image': ''},
            'red_cape': {'name': '레드 망토', 'count': 0, 'max_hp': 1, 'max_mp': 0, 'power': 0, 'image': ''},
            'red_glove': {'name': '레드 글로브', 'count': 0, 'max_hp': 1, 'max_mp': 0, 'power': 0, 'image': ''},
            'red_hood': {'name': '레드 후드', 'count': 0, 'max_hp': 1, 'max_mp': 0, 'power': 0, 'image': ''},
            'red_pants': {'name': '레드 팬츠', 'count': 0, 'max_hp': 1, 'max_mp': 0, 'power': 0, 'image': ''},
            'ruby_gem': {'name': '루비 룬스태프', 'count': 0, 'max_hp': 0, 'max_mp': 7, 'power': 7, 'image': ''},
            'silver_armor': {'name': '실버 아머', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'silver_bow': {'name': '실버 보우', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 20, 'image': ''},
            'silver_helmet': {'name': '실버 헬멧', 'count': 0, 'max_hp': 5, 'max_mp': 0, 'power': 0, 'image': ''},
            'silver_pants': {'name': '실버 팬츠', 'count': 0, 'max_hp': 9, 'max_mp': 0, 'power': 0, 'image': ''},
            'silver_staff': {'name': '실버 롱스태프', 'count': 0, 'max_hp': 0, 'max_mp': 6, 'power': 14, 'image': ''},
            'silver_sword': {'name': '실버 소드', 'count': 0, 'max_hp': 0, 'max_mp': 0, 'power': 20, 'image': ''},
            'silver_wand': {'name': '실버 완드', 'count': 0, 'max_hp': 0, 'max_mp': 20, 'power': 0, 'image': ''},
            'stone_gem': {'name': '스톤 룬스태프', 'count': 0, 'max_hp': 0, 'max_mp': 5, 'power': 5, 'image': ''}}

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
        print(self.x, self.y)
        self.img_gard.move(self.x, self.y)
        self.alarm_where_field(self.x, self.y)

        # 수호대 사이즈 조절
        self.img_gard.resize(int(self.stack_field.width() / 20), int(self.stack_field.height() / 20))
        self.img_gard.setPixmap(QPixmap('./img_src/character.png'))
        self.img_gard.setScaledContents(True)
        if self.dict_user_gard['gard'] == 'light_gard':
            color_ = 'white'
        elif self.dict_user_gard['gard'] == 'moon_gard':
            color_ = 'black'
        elif self.dict_user_gard['gard'] == 'star_gard':
            color_ = 'yellow'
        else:
            color_ = 'blue'
        # self.img_gard.setStyleSheet(f"background-color: {color_};")

        # 아이템창에 아이템 넣기
        self.renew_item_view()

    # 화면 크기 조절 이벤트
    def resizeEvent(self, event):
        print(self.stack_field.width(), self.stack_field.height())
        if self.img_gard.isVisible():
            self.img_gard.resize(int(self.stack_field.width() / 20), int(self.stack_field.height() / 20))
            self.img_gard.move(self.x - int(self.img_gard.width() / 2), self.y - int(self.img_gard.height() / 2))

    # 키 입력 이벤트
    def keyPressEvent(self, event):
        # 필드
        if self.stackedWidget.currentWidget() == self.stack_field:
            # 방향키 누를 때마다 라벨 위치 조정
            if event.key() == Qt.Key_A:
                self.x = self.img_gard.x() - int(self.stack_field.width() / 20)
                if self.x < 0:
                    self.x = 0
                self.img_gard.move(self.x, self.img_gard.y())
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_D:
                self.x = self.img_gard.x() + int(self.stack_field.width() / 20)
                if self.x > self.stack_field.width() - self.img_gard.width():
                    self.x = self.stack_field.width() - self.img_gard.width()
                self.img_gard.move(self.x, self.img_gard.y())
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_W:
                self.y = self.img_gard.y() - int(self.stack_field.height() / 20)
                if self.y < 0:
                    self.y = 0
                self.img_gard.move(self.img_gard.x(), self.y)
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_S:
                self.y = self.img_gard.y() + int(self.stack_field.height() / 20)
                if self.y > self.stack_field.height() - self.img_gard.height():
                    self.y = self.stack_field.height() - self.img_gard.height()
                self.img_gard.move(self.img_gard.x(), self.y)
                print(self.img_gard.x(), self.img_gard.y())

            self.alarm_where_field(self.x, self.y)

            tuple_v = self.field_move_event(self.field_turn)

            if tuple_v is not None:
                if tuple_v[0] == '일반몬스터':
                    print(tuple_v[1])
                elif tuple_v[0] == '텐트':
                    print(tuple_v[1])
                elif tuple_v[0] == '아군수호대':
                    print(tuple_v[1])
                elif tuple_v[0] == '적군수호대':
                    print(tuple_v[1], tuple_v[2])
                elif tuple_v[0] == '아이템':
                    print(tuple_v[1])
            else:
                pass


        # 던전
        elif self.stackedWidget.currentWidget() == self.stack_maze:
            # 방향키 누를 때마다 라벨 위치 조정
            if event.key() == Qt.Key_A:
                self.x = self.img_gard.x() - int(self.stack_field.width() / 20)
                if self.x < 0:
                    self.x = 0
                self.img_gard.move(self.x, self.img_gard.y())
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_D:
                self.x = self.img_gard.x() + int(self.stack_field.width() / 20)
                if self.x > self.stack_field.width() - self.img_gard.width():
                    self.x = self.stack_field.width() - self.img_gard.width()
                self.img_gard.move(self.x, self.img_gard.y())
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_W:
                self.y = self.img_gard.y() - int(self.stack_field.height() / 20)
                if self.y < 0:
                    self.y = 0
                self.img_gard.move(self.img_gard.x(), self.y)
                print(self.img_gard.x(), self.img_gard.y())
            elif event.key() == Qt.Key_S:
                self.y = self.img_gard.y() + int(self.stack_field.height() / 20)
                if self.y > self.stack_field.height() - self.img_gard.height():
                    self.y = self.stack_field.height() - self.img_gard.height()
                self.img_gard.move(self.img_gard.x(), self.y)
                print(self.img_gard.x(), self.img_gard.y())

            self.alarm_where_field(self.x, self.y)

            tuple_v = self.maze_move_event()

            if tuple_v is not None:
                if tuple_v[0] == '일반몬스터':
                    print(tuple_v[1])
                elif tuple_v[0] == '아군수호대':
                    print(tuple_v[1])
                elif tuple_v[0] == '적군수호대':
                    print(tuple_v[1], tuple_v[2])
            else:
                pass

    # 수호대 랜덤배치
    def random_assign_gard(self):
        dict_one = random.choice(self.list_gard)
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
        if int_x + self.img_gard.width() > self.stack_field.width() / 2 and int_y < self.stack_field.height() / 2 and not \
                self.dict_field['눈']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = True
            self.dict_field['숲'] = False
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'눈의 지역에 입장하였습니다.')
        if int_x < self.stack_field.width() / 2 and int_y + self.img_gard.height() > self.stack_field.height() / 2 and not \
                self.dict_field['숲']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = True
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'숲의 지역에 입장하였습니다.')
        if int_x + self.img_gard.width() > self.stack_field.width() / 2 and int_y + self.img_gard.height() > self.stack_field.height() / 2 and not \
                self.dict_field['물']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = False
            self.dict_field['물'] = True
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'물의 지역에 입장하였습니다.')

    # 로그창 갱신
    def renew_log_view(self, q_icon, str_msg):
        # icon = QIcon('./img_src/alarm.png')
        icon_item = QListWidgetItem(q_icon, str_msg)
        self.list_log.addItem(icon_item)
        self.list_log.scrollToItem(icon_item)

    # 아이템창 갱신
    def renew_item_view(self):
        for k, v in self.dict_item.items():
            # if v['count'] > 0:
            item = QListWidgetItem(f"{v['name']} : {v['count']}개")
            item.setIcon(QIcon(f"{v['image']}"))
            self.list_item.addItem(item)

    # 장비창 띄우기
    def click_equip_button(self, str_job):
        dlg = EquipmentClass(str_job=str_job, dict_user_gard=self.dict_user_gard, dict_equipment=self.dict_equipment)
        dlg.exec_()

        # 갱신
        self.dict_user_gard = dlg.dict_user_gard
        self.dict_equipment = dlg.dict_equipment
        print(self.dict_user_gard)
        print(self.dict_equipment)

    # 타 수호대와의 조우
    def meet_other_guardian(self):
        # 우리 수호대 제외
        self.list_gard.remove(self.dict_gard_stat['gard'])
        # 리스트 셔플
        random.shuffle(self.list_gard)
        other_gard = self.list_gard.pop()
        return other_gard

    # 치트키
    def use_cheatkey(self):
        if self.str_cheatkey == 'easter_egg':
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainClass()
    main.show()
    sys.exit(app.exec_())

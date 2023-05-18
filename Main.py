import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.uic.properties import QtGui

from view.main_frame import Ui_MainWindow
from Equipment import EquipmentClass
from Item import ItemClass
from Dungeon import mazeClass
from Field import FieldClass
from Dialog import *


class MainClass(QMainWindow, Ui_MainWindow, ItemClass, mazeClass, FieldClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_maze_1 = QLabel(self.stack_maze_1)
        self.lb_maze_2 = QLabel(self.stack_maze_2)
        self.lb_maze_3 = QLabel(self.stack_maze_3)
        self.lb_maze_4 = QLabel(self.stack_maze_4)
        self.lb_maze_5 = QLabel(self.stack_maze_5)
        self.lb_maze_6 = QLabel(self.stack_maze_6)
        self.lb_maze_7 = QLabel(self.stack_maze_7)

        self.lb_boss_1 = QLabel(self.lb_maze_1)
        self.lb_boss_2 = QLabel(self.lb_maze_2)
        self.lb_boss_3 = QLabel(self.lb_maze_3)
        self.lb_boss_4 = QLabel(self.lb_maze_4)
        self.lb_boss_5 = QLabel(self.lb_maze_5)
        self.lb_boss_6 = QLabel(self.lb_maze_6)
        self.lb_boss_7 = QLabel(self.lb_maze_7)

        self.lb_field_gard = QLabel(self.stack_field)
        self.lb_maze_1_gard = QLabel(self.lb_maze_1)
        self.lb_maze_2_gard = QLabel(self.lb_maze_2)
        self.lb_maze_3_gard = QLabel(self.lb_maze_3)
        self.lb_maze_4_gard = QLabel(self.lb_maze_4)
        self.lb_maze_5_gard = QLabel(self.lb_maze_5)
        self.lb_maze_6_gard = QLabel(self.lb_maze_6)
        self.lb_maze_7_gard = QLabel(self.lb_maze_7)

        self.list_stack_maze = [self.stack_maze_1,
                                self.stack_maze_2,
                                self.stack_maze_3,
                                self.stack_maze_4,
                                self.stack_maze_5,
                                self.stack_maze_6,
                                self.stack_maze_7]

        self.list_lb_maze = [self.lb_maze_1,
                             self.lb_maze_2,
                             self.lb_maze_3,
                             self.lb_maze_4,
                             self.lb_maze_5,
                             self.lb_maze_6,
                             self.lb_maze_7]

        self.list_lb_boss = [self.lb_boss_1,
                             self.lb_boss_2,
                             self.lb_boss_3,
                             self.lb_boss_4,
                             self.lb_boss_5,
                             self.lb_boss_6,
                             self.lb_boss_7]

        # 지역별 수호대 리스트
        self.list_lb_gard = [self.lb_field_gard,
                             self.lb_maze_1_gard,
                             self.lb_maze_2_gard,
                             self.lb_maze_3_gard,
                             self.lb_maze_4_gard,
                             self.lb_maze_5_gard,
                             self.lb_maze_6_gard,
                             self.lb_maze_7_gard]


        # 캐릭터 방향
        self.character_dir = 'left'

        # 필드 지역
        self.field_area = ''

        # 필드 전투 턴
        self.field_turn = 0

        # 던전 전투 턴
        self.maze_turn = 0

        # 던전 층
        self.maze_floor = 1

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
        self.dict_equip = {
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
                                           'equipment': [],
                                           'skill': {10: 'slice_chop'}},
                               'archer': {'survival': True,
                                          'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 150, 'max_mp': 150, 'power': 300,
                                          'equipment': [],
                                          'skill': {10: 'target_shot',
                                                    15: 'dual_shot',
                                                    20: 'master_shot'}},
                               'swordman': {'survival': True,
                                            'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 150, 'max_mp': 150, 'power': 250,
                                            'equipment': [],
                                            'skill': {10: 'slice_chop'}},
                               'wizard_red': {'survival': True,
                                              'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 100, 'max_mp': 100, 'power': 150,
                                              'equipment': [],
                                              'skill': {1: ['heal_normal', 'fire_ball'],
                                                        15: ['heal_greater', 'fire_wall'],
                                                        20: 'thunder_breaker',
                                                        25: 'bilzzard',
                                                        30: 'heal_all'}},
                               'wizard_black': {'survival': True,
                                                'lv': 1, 'hp': 200, 'max_hp': 200, 'mp': 150, 'max_mp': 150,
                                                'power': 200,
                                                'equipment': [],
                                                'skill': {1: 'fire_ball',
                                                          15: 'fire_wall',
                                                          20: 'thunder_breaker',
                                                          25: 'bilzzard'}},
                               'wizard_white': {'survival': True,
                                                'lv': 1, 'hp': 200, 'max_hp': 200, 'mp': 150, 'max_mp': 150,
                                                'power': 100,
                                                'equipment': [],
                                                'skill': {1: 'heal_normal',
                                                          15: 'heal_greater',
                                                          30: 'heal_all'}}}

        # 필드에 이미지 넣기
        self.area_forest.setPixmap(
            QPixmap('./img_src/map/forest_map.jpg').scaled(self.area_forest.width(), self.area_forest.height(),
                                                           Qt.KeepAspectRatio))
        self.area_forest.setScaledContents(True)
        self.area_fire.setPixmap(
            QPixmap('./img_src/map/fire_map.jpg').scaled(self.area_fire.width(), self.area_fire.height(),
                                                         Qt.KeepAspectRatio))
        self.area_fire.setScaledContents(True)
        self.area_snow.setPixmap(
            QPixmap('./img_src/map/snow_map.gif').scaled(self.area_snow.width(), self.area_snow.height(),
                                                         Qt.KeepAspectRatio))
        self.area_snow.setScaledContents(True)
        self.area_water.setPixmap(
            QPixmap('./img_src/map/water_map.jpg').scaled(self.area_water.width(), self.area_water.height(),
                                                          Qt.KeepAspectRatio))
        self.area_water.setScaledContents(True)

        # 시그널
        self.pb_equip_warrior.clicked.connect(lambda: self.click_equip_button('warrior'))
        self.pb_equip_archer.clicked.connect(lambda: self.click_equip_button('archer'))
        self.pb_equip_swordman.clicked.connect(lambda: self.click_equip_button('swordman'))
        self.pb_equip_wizard_red.clicked.connect(lambda: self.click_equip_button('wizard_red'))
        self.pb_equip_wizard_black.clicked.connect(lambda: self.click_equip_button('wizard_black'))
        self.pb_equip_wizard_white.clicked.connect(lambda: self.click_equip_button('wizard_white'))

        self.pb_use_item.clicked.connect(self.click_use_item_button)

        self.action_field.triggered.connect(lambda: self.change_map(0))
        self.action_maze_floor_1.triggered.connect(lambda: self.change_map(1))
        self.action_maze_floor_2.triggered.connect(lambda: self.change_map(2))
        self.action_maze_floor_3.triggered.connect(lambda: self.change_map(3))
        self.action_maze_floor_4.triggered.connect(lambda: self.change_map(4))
        self.action_maze_floor_5.triggered.connect(lambda: self.change_map(5))
        self.action_maze_floor_6.triggered.connect(lambda: self.change_map(6))
        self.action_maze_floor_7.triggered.connect(lambda: self.change_map(7))
        self.action_maze_floor_8.triggered.connect(lambda: self.change_map(8))
        self.action_battle.triggered.connect(lambda: self.change_map(9))

        # 보스 타이머
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.MoveObject)
        self.timer.start()

        # 방향 타이머
        self.timer1 = QTimer(self)
        self.timer1.setInterval(5000)
        self.timer1.timeout.connect(self.GiveDirection)
        self.timer1.start()

        # 수호대 랜덤지정
        self.random_assign_gard()

        # 수호대 필드 랜덤배치
        self.change_map(0)

        # 아이템창에 아이템 넣기
        self.renew_item_view()

        # 수호대 상태 업데이트
        self.renew_gard_status()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.stackedWidget.setFocus()

    # 화면 크기 조절 이벤트
    def resizeEvent(self, event):
        # print(self.stackedWidget.width(), self.stackedWidget.height())
        if self.stackedWidget.currentWidget() == self.stack_field:
            if self.list_lb_gard[self.stackedWidget.currentIndex()].isVisible():
                self.list_lb_gard[self.stackedWidget.currentIndex()].resize(int(self.stackedWidget.width() / 20),
                                                                            int(self.stackedWidget.height() / 20))
                self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                    self.x - int(self.list_lb_gard[self.stackedWidget.currentIndex()].width() / 2),
                    self.y - int(self.list_lb_gard[self.stackedWidget.currentIndex()].height() / 2))
        elif self.stackedWidget.currentWidget() in self.list_stack_maze:
            if self.list_lb_gard[self.stackedWidget.currentIndex()].isVisible():
                self.list_lb_gard[self.stackedWidget.currentIndex()].resize(
                    int(self.stackedWidget.width() / self.maze_map_size),
                    int(self.stackedWidget.height() / self.maze_map_size))
                self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                    self.x - int(self.list_lb_gard[self.stackedWidget.currentIndex()].width() / 2),
                    self.y - int(self.list_lb_gard[self.stackedWidget.currentIndex()].height() / 2))
            if self.list_lb_boss[self.maze_floor - 1].isVisible():
                self.list_lb_boss[self.maze_floor - 1].resize(int(self.stackedWidget.width() / self.maze_map_size),
                                                              int(self.stackedWidget.height() / self.maze_map_size))
                self.list_lb_boss[self.maze_floor - 1].move(
                    self.x - int(self.list_lb_boss[self.maze_floor - 1].width() / 2),
                    self.y - int(self.list_lb_boss[self.maze_floor - 1].height() / 2))

    # 키를 누르지 않을때 이벤트
    def keyReleaseEvent(self, event):
        if self.character_dir == 'left':
            img_left_list = ["./img_src/character/motion/swing_l.gif",
                             "./img_src/character/motion/fight_l.gif",
                             "./img_src/character/motion/sword_l.gif"]
            img = random.choice(img_left_list)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
            self.movie = QMovie(img)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
            self.movie.start()
        if self.character_dir == 'right':
            img_right_list = ["./img_src/character/motion/swing_r.gif",
                              "./img_src/character/motion/fight_r.gif",
                              "./img_src/character/motion/sword_r.gif"]
            img = random.choice(img_right_list)
            self.movie = QMovie(img)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
            self.movie.start()

    # 키 입력 이벤트
    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S]:
            # 필드
            if self.stackedWidget.currentWidget() == self.stack_field:
                # 방향키 누를 때마다 라벨 위치 조정
                if event.key() == Qt.Key_A:
                    self.character_dir = 'left'
                    self.movie = QMovie(f"./img_src/character/c_left_move.gif")
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
                    self.movie.start()
                    self.x = self.list_lb_gard[self.stackedWidget.currentIndex()].x() - int(
                        self.stack_field.width() / 20)
                    if self.x < 0:
                        self.x = 0
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.list_lb_gard[
                        self.stackedWidget.currentIndex()].y())
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())
                elif event.key() == Qt.Key_D:
                    self.character_dir = 'right'
                    self.movie = QMovie(f"./img_src/character/c_right_move.gif")
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
                    self.movie.start()
                    self.x = self.list_lb_gard[self.stackedWidget.currentIndex()].x() + int(
                        self.stack_field.width() / 20)
                    if self.x > self.stack_field.width() - self.list_lb_gard[self.stackedWidget.currentIndex()].width():
                        self.x = self.stack_field.width() - self.list_lb_gard[self.stackedWidget.currentIndex()].width()
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.list_lb_gard[
                        self.stackedWidget.currentIndex()].y())
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())
                elif event.key() == Qt.Key_W:
                    self.y = self.list_lb_gard[self.stackedWidget.currentIndex()].y() - int(
                        self.stack_field.height() / 20)
                    if self.y < 0:
                        self.y = 0
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                        self.list_lb_gard[self.stackedWidget.currentIndex()].x(), self.y)
                    print(self.list_lb_gard[self.stackedWidget.currentIndex()].x(),
                          self.list_lb_gard[self.stackedWidget.currentIndex()].y())
                elif event.key() == Qt.Key_S:
                    self.y = self.list_lb_gard[self.stackedWidget.currentIndex()].y() + int(
                        self.stack_field.height() / 20)
                    if self.y > self.stack_field.height() - self.list_lb_gard[
                        self.stackedWidget.currentIndex()].height():
                        self.y = self.stack_field.height() - self.list_lb_gard[
                            self.stackedWidget.currentIndex()].height()
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                        self.list_lb_gard[self.stackedWidget.currentIndex()].x(), self.y)
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())

                self.alarm_where_field(self.x, self.y)

                tuple_v = self.field_move_event(self.dict_user_gard, self.field_turn)

                if tuple_v is not None:
                    if tuple_v[0] == '일반몬스터':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), f'{self.field_area} 몬스터를 만났습니다')
                    elif tuple_v[0] == '텐트':
                        self.dict_item['tent']['count'] += 1
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '텐트를 획득했습니다')
                    elif tuple_v[0] == '아군수호대':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '아군 수호대를 만났습니다.')
                        self.dict_item, self.dict_equip = self.get_item(tuple_v[1], self.dict_item, self.dict_equip)
                    elif tuple_v[0] == '적군수호대':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '적군 수호대를 만났습니다.')
                    elif tuple_v[0] == '아이템':
                        self.dict_item, self.dict_equip = self.get_item(tuple_v[1], self.dict_item, self.dict_equip)
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '아이템을 획득했습니다')
                    elif tuple_v == '이동':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '1칸 이동하였습니다.')
                    self.renew_item_view()
                else:
                    pass
            # 던전
            elif self.stackedWidget.currentWidget() in self.list_stack_maze:
                # 방향키 누를 때마다 라벨 위치 조정
                if event.key() == Qt.Key_A:
                    self.character_dir = 'left'
                    self.movie = QMovie(f"./img_src/character/c_left_move.gif")
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
                    self.movie.start()
                    self.x = self.list_lb_gard[self.stackedWidget.currentIndex()].x() - int(
                        self.list_stack_maze[self.maze_floor - 1].width() / self.maze_map_size)
                    if self.x < 0:
                        self.x = 0
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.list_lb_gard[
                        self.stackedWidget.currentIndex()].y())
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())
                elif event.key() == Qt.Key_D:
                    self.character_dir = 'right'
                    self.movie = QMovie(f"./img_src/character/c_right_move.gif")
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
                    self.movie.start()
                    self.x = self.list_lb_gard[self.stackedWidget.currentIndex()].x() + int(
                        self.list_stack_maze[self.maze_floor - 1].width() / self.maze_map_size)
                    if self.x > self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_gard[
                        self.stackedWidget.currentIndex()].width():
                        self.x = self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_gard[
                            self.stackedWidget.currentIndex()].width()
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.list_lb_gard[
                        self.stackedWidget.currentIndex()].y())
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())
                elif event.key() == Qt.Key_W:
                    self.y = self.list_lb_gard[self.stackedWidget.currentIndex()].y() - int(
                        self.list_stack_maze[self.maze_floor - 1].height() / self.maze_map_size)
                    if self.y < 0:
                        self.y = 0
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                        self.list_lb_gard[self.stackedWidget.currentIndex()].x(), self.y)
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())
                elif event.key() == Qt.Key_S:
                    self.y = self.list_lb_gard[self.stackedWidget.currentIndex()].y() + int(
                        self.list_stack_maze[self.maze_floor - 1].height() / self.maze_map_size)
                    if self.y > self.list_stack_maze[self.maze_floor - 1].height() - self.list_lb_gard[
                        self.stackedWidget.currentIndex()].height():
                        self.y = self.list_stack_maze[self.maze_floor - 1].height() - self.list_lb_gard[
                            self.stackedWidget.currentIndex()].height()
                    self.list_lb_gard[self.stackedWidget.currentIndex()].move(
                        self.list_lb_gard[self.stackedWidget.currentIndex()].x(), self.y)
                    # print(self.list_lb_gard[self.stackedWidget.currentIndex(].x(), self.list_lb_gard[self.stackedWidget.currentIndex(].y())

                tuple_v = self.maze_move_event(self.maze_floor, self.dict_user_gard, self.maze_turn)

                if tuple_v is not None:
                    if tuple_v[0] == '일반몬스터':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), f'던전 몬스터를 만났습니다')
                    elif tuple_v[0] == '아군수호대':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '아군 수호대를 만났습니다.')
                        self.dict_item, self.dict_equip = self.get_item(tuple_v[1], self.dict_item, self.dict_equip)
                    elif tuple_v[0] == '적군수호대':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '적군 수호대를 만났습니다.')
                    elif tuple_v == '이동':
                        self.renew_log_view(QIcon('./img_src/alarm.png'), '1칸 이동하였습니다.')
                    self.renew_item_view()
                else:
                    pass

    # 화면 전환
    def change_map(self, page):
        if page == 0:
            self.stackedWidget.setCurrentWidget(self.stack_field)
            self.movie = QMovie(f"./img_src/character/c_stand.gif")
            self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
            self.movie.start()
            self.list_lb_gard[self.stackedWidget.currentIndex()].resize(int(1230 / 20), int(660 / 20))
            self.x, self.y = self.random_assign_field()
            self.x *= self.list_lb_gard[self.stackedWidget.currentIndex()].width()
            self.y *= self.list_lb_gard[self.stackedWidget.currentIndex()].height()
            self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.y)
            self.alarm_where_field(self.x, self.y)

            # 수호대 사이즈 조절

        elif page == 9:
            self.stackedWidget.setCurrentWidget(self.stack_battle)
        else:
            self.maze_floor = page
            self.stackedWidget.setCurrentIndex(self.maze_floor)

            # 던전 이미지 바꾸기
            # self.list_lb_maze[self.maze_floor -1] = QLabel(self.list_stack_maze[self.maze_floor - 1])
            self.list_lb_maze[self.maze_floor - 1].setPixmap(
                QPixmap(f'./img_src/maze_map/maze_{self.maze_floor}.png').scaled(
                    self.list_stack_maze[self.maze_floor - 1].width(),
                    self.list_stack_maze[self.maze_floor - 1].height(),
                    Qt.KeepAspectRatio))
            self.list_lb_maze[self.maze_floor - 1].setScaledContents(True)
            self.list_lb_maze[self.maze_floor - 1].setSizePolicy(QSizePolicy.Policy.Expanding,
                                                                 QSizePolicy.Policy.Expanding)
            self.list_lb_maze[self.maze_floor - 1].setAlignment(Qt.AlignmentFlag.AlignCenter)

            layout = QVBoxLayout(self.list_stack_maze[self.maze_floor - 1])
            layout.addWidget(self.list_lb_maze[self.maze_floor - 1])

            # 보스몬스터 랜덤 배치
            self.maze_map_size, self.boss_x, self.boss_y = self.maze_boss_location(self.maze_floor)

            # 층별 던전보스 생성
            self.moveInt = 1
            self.direction_list = ['상', '하', '좌', '우', '좌상', '우상', '좌하', '우하']
            self.boss_dir = random.choice(self.direction_list)

            # 보스
            # self.list_lb_boss[self.maze_floor -1]  = QLabel(self.list_lb_maze[self.maze_floor -1])
            self.boss_dir = random.choice(self.direction_list)
            self.movie = self.changeImg(self.boss_dir)
            self.list_lb_boss[self.maze_floor - 1].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_lb_boss[self.maze_floor - 1].setMovie(self.movie)
            self.list_lb_boss[self.maze_floor - 1].setScaledContents(True)
            self.movie.start()
            self.list_lb_boss[self.maze_floor - 1].resize(int(self.stackedWidget.width() / self.maze_map_size),
                                                          int(self.stackedWidget.height() / self.maze_map_size))
            self.boss_x *= self.list_lb_boss[self.maze_floor - 1].width()
            self.boss_y *= self.list_lb_boss[self.maze_floor - 1].height()
            self.list_lb_boss[self.maze_floor - 1].move(self.boss_x, self.boss_y)
            self.adjustInt = self.list_lb_boss[self.maze_floor - 1].width()

            # 수호대 랜덤 배치
            # self.lb_gard = QLabel(self.list_lb_maze[self.maze_floor -1])
            self.movie = QMovie(f"./img_src/character/c_stand.gif")
            self.list_lb_gard[self.stackedWidget.currentIndex()].setScaledContents(True)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_lb_gard[self.stackedWidget.currentIndex()].setMovie(self.movie)
            self.movie.start()
            self.list_lb_gard[self.stackedWidget.currentIndex()].resize(
                int(self.stackedWidget.width() / self.maze_map_size),
                int(self.stackedWidget.height() / self.maze_map_size))
            self.x, self.y = self.random_assign_maze()
            self.x *= self.list_lb_gard[self.stackedWidget.currentIndex()].width()
            self.y *= self.list_lb_gard[self.stackedWidget.currentIndex()].height()
            self.list_lb_gard[self.stackedWidget.currentIndex()].move(self.x, self.y)

    # 방향값 주기
    def GiveDirection(self):
        if self.stackedWidget.currentWidget() in self.list_stack_maze:
            self.boss_dir = random.choice(self.direction_list)
            self.movie = self.changeImg(self.boss_dir)
            self.list_lb_boss[self.maze_floor - 1].setMovie(self.movie)
            self.movie.start()

    # 방향별 이미지
    def changeImg(self, str_dir):
        if self.stackedWidget.currentWidget() in self.list_stack_maze:
            gif_left_list = ["img_src/boss/1층/floor1_1_l.gif",
                             "img_src/boss/1층/floor1_2_l.gif",
                             "img_src/boss/1층/floor1_3_l.gif"]
            gif_l = random.choice(gif_left_list)
            gif_right_list = ["img_src/boss/1층/floor1_1_r.gif",
                              "img_src/boss/1층/floor1_2_r.gif",
                              "img_src/boss/1층/floor1_3_r.gif"]
            gif_r = random.choice(gif_right_list)
            if str_dir == '상':
                return QMovie(gif_l)
            elif str_dir == '하':
                return QMovie(gif_r)
            elif str_dir == '좌':
                return QMovie(gif_l)
            elif str_dir == '우':
                return QMovie(gif_r)
            elif str_dir == '좌상':
                return QMovie(gif_l)
            elif str_dir == '우상':
                return QMovie(gif_r)
            elif str_dir == '좌하':
                return QMovie(gif_l)
            elif str_dir == '우하':
                return QMovie(gif_r)

    # 보스 움직이기
    def MoveObject(self):
        if self.stackedWidget.currentWidget() in self.list_stack_maze:
            self.boss_x, self.boss_y = self.directionPos(self.boss_x, self.boss_y, self.boss_dir)
            self.list_lb_boss[self.maze_floor - 1].move(self.boss_x, self.boss_y)

    # 방향 값
    def directionPos(self, x, y, direction_):
        if self.stackedWidget.currentWidget() in self.list_stack_maze:
            if direction_ == '상':
                if y < 0:
                    y = 0
                elif y > 0:
                    y -= self.moveInt
            elif direction_ == '하':
                if y > self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt:
                    y = self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt
                else:
                    y += self.moveInt
            elif direction_ == '좌':
                if x < 0:
                    x = 0
                else:
                    x -= self.moveInt
            elif direction_ == '우':
                if x > self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_boss[
                    self.maze_floor - 1].width():
                    x = self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_boss[
                        self.maze_floor - 1].width()
                else:
                    x += self.moveInt
            elif direction_ == '좌상':
                if x < 0:
                    x = 0
                else:
                    x -= self.moveInt
                if y < 0:
                    y = 0
                else:
                    y -= self.moveInt
            elif direction_ == '우상':
                if x > self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_boss[
                    self.maze_floor - 1].width():
                    x = self.list_stack_maze[self.maze_floor - 1].width() - self.list_lb_boss[
                        self.maze_floor - 1].width()
                else:
                    x += self.moveInt
                if y < 0:
                    y = 0
                else:
                    y -= self.moveInt
            elif direction_ == '좌하':
                if x < 0:
                    x = 0
                else:
                    x -= self.moveInt
                if y > self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt:
                    y = self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt
                else:
                    y += self.moveInt
            elif direction_ == '우하':
                if x > self.list_stack_maze[self.maze_floor - 1].width() - self.adjustInt:
                    x = self.list_stack_maze[self.maze_floor - 1].width() - self.adjustInt
                else:
                    x += self.moveInt
                if y > self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt:
                    y = self.list_stack_maze[self.maze_floor - 1].height() - self.adjustInt
                else:
                    y += self.moveInt
            return x, y

    # 유저 스텟 갱신
    def renew_gard_status(self):
        self.lv_warrior.setText('Lv. ' + str(self.dict_user_gard['warrior']['lv']))
        self.hp_warrior.setValue(int(self.dict_user_gard['warrior']['hp']))
        self.hp_warrior.setMaximum(int(self.dict_user_gard['warrior']['max_hp']))
        self.mp_warrior.setValue(0)

        self.lv_archer.setText('Lv. ' + str(self.dict_user_gard['archer']['lv']))
        self.hp_archer.setValue(int(self.dict_user_gard['archer']['hp']))
        self.hp_archer.setMaximum(int(self.dict_user_gard['archer']['max_hp']))
        self.mp_archer.setValue(int(self.dict_user_gard['archer']['mp']))
        self.mp_archer.setMaximum(int(self.dict_user_gard['archer']['max_mp']))

        self.lv_swordman.setText('Lv. ' + str(self.dict_user_gard['swordman']['lv']))
        self.hp_swordman.setValue(int(self.dict_user_gard['swordman']['hp']))
        self.hp_swordman.setMaximum(int(self.dict_user_gard['swordman']['max_hp']))
        self.mp_swordman.setValue(int(self.dict_user_gard['swordman']['mp']))
        self.mp_swordman.setMaximum(int(self.dict_user_gard['swordman']['max_mp']))

        self.lv_wizard_red.setText('Lv. ' + str(self.dict_user_gard['wizard_red']['lv']))
        self.hp_wizard_red.setValue(int(self.dict_user_gard['wizard_red']['hp']))
        self.hp_wizard_red.setMaximum(int(self.dict_user_gard['wizard_red']['max_hp']))
        self.mp_wizard_red.setValue(int(self.dict_user_gard['wizard_red']['mp']))
        self.mp_wizard_red.setMaximum(int(self.dict_user_gard['wizard_red']['max_mp']))

        self.lv_wizard_black.setText('Lv. ' + str(self.dict_user_gard['wizard_black']['lv']))
        self.hp_wizard_black.setValue(int(self.dict_user_gard['wizard_black']['hp']))
        self.hp_wizard_black.setMaximum(int(self.dict_user_gard['wizard_black']['max_hp']))
        self.mp_wizard_black.setValue(int(self.dict_user_gard['wizard_black']['mp']))
        self.mp_wizard_black.setMaximum(int(self.dict_user_gard['wizard_black']['max_mp']))

        self.lv_wizard_white.setText('Lv. ' + str(self.dict_user_gard['wizard_white']['lv']))
        self.hp_wizard_white.setValue(int(self.dict_user_gard['wizard_white']['hp']))
        self.hp_wizard_white.setMaximum(int(self.dict_user_gard['wizard_white']['max_hp']))
        self.mp_wizard_white.setValue(int(self.dict_user_gard['wizard_white']['mp']))
        self.mp_wizard_white.setMaximum(int(self.dict_user_gard['wizard_white']['max_mp']))

    # 아이템 사용 버튼 클릭
    def click_use_item_button(self):
        if self.list_item.currentItem() is not None:
            item = self.list_item.currentItem().text().split(':')[0].strip()
            for k, v in self.dict_item.items():
                if v['name'] == item:
                    str_item = k
                    break

            choice_dlg = ChoiceJopDialog()
            if item not in ['부활포션', '텐트']:
                choice_dlg.exec_()
            str_job = choice_dlg.job

            self.dict_item, self.dict_user_gard, msg = self.use_item(str_job, str_item, self.dict_item,
                                                                     self.dict_user_gard)
            self.renew_log_view(QIcon('./img_src/alarm.png'), msg)
            self.renew_item_view()
            self.renew_gard_status()
        else:
            dlg = CustomDialog('사용할 아이템을 선택해주세요!')
            dlg.exec_()

    # 운석배치
    def location_meteor(self):
        rand_meteor_door_x = random.randint(1, 19) * int(self.stack_field.width() / 20)
        rand_meteor_door_y = random.randint(1, 19) * int(self.stack_field.width() / 20)

    # 던전입구 배치
    def location_maze_door(self):
        maze_door_x, maze_door_y, self.field_turn = self.random_maze_door(self.field_turn)
        maze_door_x *= int(self.stack_field.width() / 20)
        maze_door_y *= int(self.stack_field.width() / 20)

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
        int_x = random.randint(1, 19)
        int_y = random.randint(1, 19)
        return int_x, int_y

    # 던전 랜덤배치
    def random_assign_maze(self):
        int_x = random.randint(1, self.maze_map_size - 1)
        int_y = random.randint(1, self.maze_map_size - 1)
        return int_x, int_y

    def alarm_where_field(self, int_x, int_y):
        # 알림
        if int_x < self.stack_field.width() / 2 and int_y < self.stack_field.height() / 2 and not self.dict_field['불']:
            self.dict_field['불'] = True
            self.dict_field['눈'] = False
            self.dict_field['숲'] = False
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'불의 지역에 입장하였습니다.')
            self.field_area = '불의 지역'
        if int_x + self.list_lb_gard[
            self.stackedWidget.currentIndex()].width() > self.stack_field.width() / 2 and int_y < self.stack_field.height() / 2 and not \
                self.dict_field['눈']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = True
            self.dict_field['숲'] = False
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'눈의 지역에 입장하였습니다.')
            self.field_area = '눈의 지역'
        if int_x < self.stack_field.width() / 2 and int_y + self.list_lb_gard[
            self.stackedWidget.currentIndex()].height() > self.stack_field.height() / 2 and not \
                self.dict_field['숲']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = True
            self.dict_field['물'] = False
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'숲의 지역에 입장하였습니다.')
            self.field_area = '숲의 지역'
        if int_x + self.list_lb_gard[
            self.stackedWidget.currentIndex()].width() > self.stack_field.width() / 2 and int_y + self.list_lb_gard[
            self.stackedWidget.currentIndex()].height() > self.stack_field.height() / 2 and not \
                self.dict_field['물']:
            self.dict_field['불'] = False
            self.dict_field['눈'] = False
            self.dict_field['숲'] = False
            self.dict_field['물'] = True
            self.renew_log_view(QIcon('./img_src/alarm.png'), f'물의 지역에 입장하였습니다.')
            self.field_area = '물의 지역'

    # 로그창 갱신
    def renew_log_view(self, q_icon, str_msg):
        # icon = QIcon('./img_src/alarm.png')
        icon_item = QListWidgetItem(q_icon, str_msg)
        self.list_log.addItem(icon_item)
        self.list_log.scrollToItem(icon_item)

    # 아이템창 갱신
    def renew_item_view(self):
        self.list_item.clear()
        for k, v in self.dict_item.items():
            if v['count'] > 0:
                item = QListWidgetItem(f"{v['name']} : {v['count']}개")
                item.setIcon(QIcon(f"{v['image']}"))
                self.list_item.addItem(item)

    # 장비 버튼 클릭
    def click_equip_button(self, str_job):
        dlg = EquipmentClass(str_job=str_job, dict_user_gard=self.dict_user_gard, dict_equip=self.dict_equip)
        dlg.exec_()

        # 갱신

        self.dict_user_gard = dlg.dict_user_gard
        self.dict_equip = dlg.dict_equip

        # print(self.dict_user_gard)

        self.renew_gard_status()

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
    dlg_gard_name = GiveGardName(main.dict_user_gard['gard'])
    dlg_gard_name.exec_()
    main.lb_gard_name.setText(dlg_gard_name.gard_name)
    sys.exit(app.exec_())

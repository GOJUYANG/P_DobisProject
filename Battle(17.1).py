import os, sys
import random
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# 메인화면
main = resource_path('ui_src/this_is_boki_dialog.ui')
main_class = uic.loadUiType(main)[0]

class BattleClass(QDialog, main_class):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()

        ### 받아올 변수 ###
        # if 'bool_meet_gard' in kwargs:
        #     self.bool_meet_gard = kwargs['bool_meet_gard']
        # if 'bool_meet_monster' in kwargs:
        #     self.bool_meet_monster = kwargs['bool_meet_monster']
        # if 'bool_meet_maze_gard' in kwargs:
        #     self.bool_meet_maze_gard = kwargs['bool_meet_maze_gard']
        # if 'bool_meet_enemy_monster' in kwargs:
        #     self.bool_meet_enemy_monster = kwargs['bool_meet_enemy_monster']
        # if 'bool_meet_boss_monster' in kwargs:
        #     self.bool_meet_boss_monster = kwargs['bool_meet_boss_monster']
        # if 'dict_user_gard' in kwargs:
        #     self.dict_user_gard = kwargs['dict_user_gard']
        # if 'dict_field_monster' in kwargs:
        #     self.dict_field_monster = kwargs['dict_field_monster']
        # if 'dict_maze_monster' in kwargs:
        #     self.dict_maze_monster = kwargs['dict_maze_monster']
        # if 'int_floor' in kwargs:
        #     self.int_floor = kwargs['int_floor']
        # if 'dict_enemy_gard' in kwargs:
        #     self.dict_enemy_gard = kwargs['dict_enemy_gard']
        # if 'dict_boss_monster' in kwargs:
        #     self.dict_boss_monster = kwargs['dict_boss_monster']

        # -----5.24 추가 (백법사 map_find 변수)-----------------------------------------------------------------------------
        # if 'rand_maze_door_x' in kwargs:
        #     self.rand_maze_door_x = kwargs['rand_maze_door_x']
        # if 'rand_maze_door_y' in kwargs:
        #     self.rand_maze_door_y = kwargs['rand_maze_door_y']
        # if 'int_next_entrance_x' in kwargs:
        #     self.int_next_entrance_x = kwargs['int_next_entrance_x']
        # if 'int_next_entrance_y' in kwargs:
        #     self.int_next_entrance_y = kwargs['int_next_entrance_y']

# 받아올 변수들 임시 사용 #---------------------------------------------------------------------------------

        # 테스트용 임의설정 값 #
        user_gard = 'earth_gard'
        str_area = 'area_forest'
        self.bool_meet_monster = True
        self.bool_meet_gard = False
        self.bool_meet_enemy_monster = False
        self.bool_meet_maze_gard = False
        self.bool_meet_boss_monster = False
        self.int_floor = 1
        self.rand_maze_door_x = 200
        self.rand_maze_door_y = 200
        self.int_next_entrance_x = 100
        self.int_next_entrance_x = 100

        ## 유저 수호대 ##
        self.dict_user_gard = {'gard': user_gard,
                               'location': {'region': '', 'x': 0, 'y': 0},
                               'warrior': {'survival': True,
                                           'lv': 20, 'hp': 30, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                           'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                         'bronze_sword'],
                                           'skill': {10: 'slice_chop'}},
                               'archer': {'survival': True,
                                          'lv': 20, 'hp': 30, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 300,
                                          'equipment': [],
                                          'skill': {10: 'target_shot',
                                                    15: 'dual_shot',
                                                    20: 'master_shot'}},
                               'swordman': {'survival': True,
                                            'lv': 20, 'hp': 150, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 250,
                                            'equipment': [],
                                            'skill': {10: 'slice_chop'}},
                               'wizard_red': {'survival': True,
                                              'lv': 20, 'hp': 150, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 150,
                                              'equipment': [],
                                              'skill': {1: ['heal_normal', 'fire_ball'],
                                                        15: ['heal_greater', 'fire_wall'],
                                                        20: 'thunder_breaker',
                                                        25: 'bilzzard',
                                                        30: 'heal_all'}},
                               'wizard_black': {'survival': True,
                                                'lv': 20, 'hp': 200, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                                'equipment': [],
                                                'skill': {1: 'fire_ball',
                                                          15: 'fire_wall',
                                                          20: 'thunder_breaker',
                                                          25: 'bilzzard'}},
                               'wizard_white': {'survival': True,
                                                'lv': 35, 'hp': 200, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 100,
                                                'equipment': [],
                                                'skill': {1: 'heal_normal',
                                                          10: 'hp_up',
                                                          15: ['heal_greater', 'mp_up'],
                                                          30: ['heal_all', 'map_find']}}}

        # 필드 몬스터 ##
        monster_cnt = random.choice(range(1, 11))
        hp_monster = random.choices(range(200, 1001), k=monster_cnt)
        if str_area == 'area_fire':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['fire_attack', 0.05], 'skill': ['fire_ball', 0.10]}
        elif str_area == 'area_water':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['aqua_attack', 0.05], 'skill': ['aqua_ball', 0.10]}
        elif str_area == 'area_forest':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['air_attack', 0.05], 'skill': ['air_ball', 0.10]}
        else:
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['snow_attack', 0.05], 'skill': ['snow_ball', 0.10]}

        self.dict_field_monster = {'type': 'field_monster',
                                   'area': str_area,
                                   'info': dict_info}

        # 던전 몬스터 ##
        int_monster_count = random.randint(1, 10)
        self.dict_maze_monster = {'int_cnt': int_monster_count,
                                  'list_hp': random.sample(range(200, 1000), int_monster_count),
                                  'list_area_monster': random.choices(
                                      ['area_fire', 'area_water', 'area_forest', 'area_snow'],
                                      k=int_monster_count),
                                  'list_damage': random.choices([0.05, 0.1], k=int_monster_count)}

        ## [필드] 적 수호대 ##
        self.use_hp_up = False
        self.use_fire_wall = False
        self.use_thunder_breaker = False
        self.use_bilzzard = False

        list_enemy_lvs = random.choices(range(15, 21), k=6)
        int_hp_up = 1.2
        int_power_up = random.choice([1.1, 1.2, 1.3, 1.4, 1.5])

        if self.dict_user_gard['gard'] == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'earth_gard'])
        elif self.dict_user_gard['gard'] == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'earth_gard'])
        elif self.dict_user_gard['gard'] == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'earth_gard'])
        elif self.dict_user_gard['gard'] == 'earth_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

        self.dict_enemy_gard = {'type': 'field_enemy_gard',
                                'gard': str_enemy_gard,
                                'warrior': {'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300 * int_hp_up,
                                            'skill': {10: 'slice_chop'}, 'power': 200},
                                'archer': {'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                           'power': 300 * int_power_up,
                                           'skill': {10: 'target_shot',
                                                     15: 'dual_shot',
                                                     20: 'master_shot'}},
                                'swordman': {'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                             'power': 300 * int_power_up,
                                             'skill': {10: 'slice_chop'}},
                                'wizard_red': {'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up,
                                               'max_hp': 150 * int_hp_up,
                                               'mp': 100 * int_hp_up,
                                               'power': 300 * int_power_up,
                                               'skill': {1: ['heal_normal', 'fire_ball'],
                                                         15: ['heal_greater', 'fire_wall'],
                                                         20: 'thunder_breaker',
                                                         25: 'bilzzard',
                                                         30: 'heal_all'}},
                                'wizard_black': {'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up,
                                                 'max_hp': 200 * int_hp_up,
                                                 'power': 300 * int_power_up,
                                                 'skill': {1: 'fire_ball',
                                                           15: 'fire_wall',
                                                           20: 'thunder_breaker',
                                                           25: 'bilzzard'}},
                                'wizard_white': {'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up,
                                                 'max_hp': 200 * int_hp_up,
                                                 'power': 300 * int_power_up,
                                                 'skill': {1: 'heal_normal',
                                                           10: 'hp_up',
                                                           15: 'heal_greater',
                                                           30: 'heal_all'}}}

        ## [던전] 적 수호대 ##
        # if self.int_floor == 1:
        #     list_enemy_lvs = random.choices(range(20, 25), k=6)
        #     int_hp_up = 1.3
        #     power = random.randint(300, 400)
        # elif self.int_floor == 2:
        #     list_enemy_lvs = random.choices(range(25, 30), k=6)
        #     int_hp_up = 1.3
        #     power = random.randint(500, 1000)
        # elif self.int_floor == 3:
        #     list_enemy_lvs = random.choices(range(30, 35), k=6)
        #     int_hp_up = 1.3 * 1.4
        #     power = random.randint(1000, 2000)
        # elif self.int_floor == 4:
        #     list_enemy_lvs = random.choices(range(35, 40), k=6)
        #     int_hp_up = 1.3 * 1.4
        #     power = random.randint(2000, 3500)
        # elif self.int_floor == 5:
        #     list_enemy_lvs = random.choices(range(45, 50), k=6)
        #     int_hp_up = 1.3 * 1.4 * 1.5
        #     power = random.randint(3500, 5000)
        # elif self.int_floor >= 6:
        #     list_enemy_lvs = random.choices(range(50, 100), k=6)
        #     int_hp_up = 1.3 * 1.4 * 1.5 * 1.6
        #     power = random.randint(5000, 10000)

        # self.dict_enemy_gard = {'type': 'maze_enemy_gard',
        #                         'gard': str_enemy_gard,
        #                         'warrior': {'survival': True,
        #                                     'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300 * int_hp_up,
        #                                     'power': power,
        #                                     'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
        #                                                   'bronze_sword'],
        #                                     'skill': {10: 'slice_chop'}},
        #                         'archer': {'survival': True,
        #                                    'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
        #                                    'power': power,
        #                                    'equipment': [],
        #                                    'skill': {10: 'target_shot',
        #                                              15: 'dual_shot',
        #                                              20: 'master_shot'}},
        #                         'swordman': {'survival': True,
        #                                      'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
        #                                      'power': power,
        #                                      'equipment': [],
        #                                      'skill': {10: 'slice_chop'}},
        #                         'wizard_red': {'survival': True,
        #                                        'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up,
        #                                        'max_hp': 150 * int_hp_up,
        #                                        'power': power,
        #                                        'equipment': [],
        #                                        'skill': {1: ['heal_normal', 'fire_ball'],
        #                                                  15: ['heal_greater', 'fire_wall'],
        #                                                  20: 'thunder_breaker',
        #                                                  25: 'bilzzard',
        #                                                  30: 'heal_all'}},
        #                         'wizard_black': {'survival': True,
        #                                          'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up,
        #                                          'max_hp': 200 * int_hp_up,
        #                                          'power': power,
        #                                          'equipment': [],
        #                                          'skill': {1: 'fire_ball',
        #                                                    15: 'fire_wall',
        #                                                    20: 'thunder_breaker',
        #                                                    25: 'bilzzard'}},
        #                         'wizard_white': {'survival': True,
        #                                          'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up,
        #                                          'max_hp': 200 * int_hp_up,
        #                                          'power': power,
        #                                          'equipment': [],
        #                                          'skill': {1: 'heal_normal',
        #                                                    15: 'heal_greater',
        #                                                    30: 'heal_all'}}}

        # 보스 몬스터 ##
        int_cnt = random.randint(0, 6)
        list_hp = random.sample(range(200, 1000), k=int_cnt)
        list_area = random.choices(['area_fire', 'area_water', 'area_forest', 'area_snow'], k=int_cnt)

        if self.int_floor == 1:
            int_boss_hp = random.randint(25000, 35000)
            self.dict_boss_monster = {'floor': 1,
                                      'type': 'boss',
                                      'name': '이동려크',
                                      'hp': int_boss_hp,
                                      'attack': ['fan_attack', 0.05],
                                      'skill': ['hell_shouting', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 2:
            int_boss_hp = random.randint(45000, 55000)
            self.dict_boss_monster = {'floor': 2,
                                      'type': 'boss',
                                      'name': '조동혀니', 'hp': int_boss_hp, 'attack': ['silent_attack', 0.05],
                                      'skill': ['hell_feedback', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 3:
            int_boss_hp = random.randint(65000, 75000)
            self.dict_boss_monster = {'floor': 3,
                                      'type': 'boss',
                                      'name': '류홍거리', 'hp': int_boss_hp, 'attack': ['ignore_attack', 0.05],
                                      'skill': ['hell_ignore', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 4:
            int_boss_hp = random.randint(75000, 85000)
            self.dict_boss_monster = {'floor': 4,
                                      'type': 'boss',
                                      'name': '코로나악마공주', 'hp': int_boss_hp, 'attack': ['virus_attack', 0.05],
                                      'skill': ['hell_virus', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 5:
            int_boss_hp = random.randint(85000, 599999)
            self.dict_boss_monster = {'floor': 5,
                                      'type': 'boss',
                                      'name': '이땅복이', 'hp': int_boss_hp, 'attack': ['html_attack', 0.05],
                                      'skill': ['hell_task', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 6:
            int_boss_hp = random.randint(999999, 9999999)
            self.dict_boss_monster = {'floor': 6,
                                      'type': 'boss',
                                      'name': '환생의 복이', 'hp': int_boss_hp, 'attack': ['python_attack', 0.05],
                                      'skill': ['hell_coding', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 7:
            int_boss_hp = 9999999
            self.dict_boss_monster = {'floor': 7,
                                      'type': 'boss',
                                      'name': '로드오브보기', 'hp': int_boss_hp, 'attack': ['c_attack', 0.05],
                                      'skill': ['hell_boki', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}


### 전투클래스 내에서만 사용되는 변수 ###
        self.list_job = ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white']
        self.monster_li = []
        self.list_origin_power = []
        self.bool_war_result = False
        self.used_hp_up = None
        self.int_btn_clicked_cnt = 0  # 수호대의 캐릭터 중 survival:True 수와 비교하여 버튼 활성화/비활성화를 체크하기 위함.
        self.int_survival = 0  # 수호대 캐릭터 중 survival:True 숫자
        self.skill_effect_2 = 0
        self.int_war_cnt = 0
        self.mp_up_used = ''
        self.origin_mp = 0
        self.use_hp_up = False
        self.use_fire_wall = False
        self.use_thunder_breaker = False
        self.use_bilzzard = False

### qt object ###
        self.battle_dialog.verticalScrollBar().maximum()
        self.list_frame = self.btn_widget.findChildren(QFrame)
        self.list_enemy_btn = self.groupBox.findChildren(QPushButton)
        self.list_enemy_line = self.groupBox.findChildren(QLineEdit)
        self.list_job_lb = [self.warrior_lb, self.archer_lb, self.swordman_lb, self.red_wizard_lb, self.black_wizard_lb,
                            self.white_wizard_lb]
        self.list_attack_btn = [self.pb_atk_warrior, self.pb_atk_archer, self.pb_atk_swordman, self.pb_atk_wizard_red,
                                self.pb_atk_wizard_black, self.pb_atk_wizard_white]
        self.list_skill_btn = [self.pb_skill_job_warrior,
                               self.pb_skill_job_archer, self.pb_skill_job_swordman, self.pb_skill_job_wizard_red,
                               self.pb_skill_job_wizard_black, self.pb_skill_job_wizard_white]

        self.list_skill_to_enemy = [self.skill_btn_warrior_slice_chop,
                                    self.skill_btn_archer_target_shot, self.skill_btn_archer_dual_shot,
                                    self.skill_btn_archer_master_shot,
                                    self.skill_btn_swordman_slice_chop,
                                    self.skill_btn_wizard_red_fire_ball, self.skill_btn_wizard_red_fire_wall,
                                    self.skill_btn_wizard_red_thunder_breaker, self.skill_btn_wizard_red_bilzzard,
                                    self.skill_btn_wizard_black_fire_ball, self.skill_btn_wizard_black_fire_wall,
                                    self.skill_btn_wizard_black_thunder_breaker, self.skill_btn_wizard_black_bilzzard]

        self.list_skill_to_user_gard = [self.skill_btn_wizard_red_heal_normal, self.skill_btn_wizard_red_heal_greater,
                                        self.skill_btn_wizard_red_heal_all,
                                        self.skill_btn_wizard_white_heal_normal,
                                        self.skill_btn_wizard_white_heal_greater, self.skill_btn_wizard_white_heal_all,
                                        self.skill_btn_wizard_white_hp_up, self.skill_btn_wizard_white_mp_up,
                                        self.skill_btn_wizard_white_map_find]

 ### qt 연결 ###
        # 전투 시작 시 가장 먼저 호출될 함수들(배틀장소확인/장비버튼비활성화/몬스터생성)
        if self.bool_meet_monster or self.bool_meet_enemy_monster or self.bool_meet_boss_monster:
            # self.show_war_result()
            self.battle_location()
            self.equip_btn_disabled()
            self.monster_creat()
        elif self.bool_meet_gard or self.bool_meet_maze_gard:
            # self.show_war_result()
            self.battle_location()
            self.equip_btn_disabled()

# self.list_frame[i].findChildren(QPushButton)[i] -> i:0 공격 / 1:장비 / 2:스킬 / 3:도망
        for i in range(6):
            self.list_frame[i].findChildren(QPushButton)[0].clicked.connect(
                lambda x, y=i: self.atk_choice(x, y))
            self.list_frame[i].findChildren(QPushButton)[0].clicked.connect(
                lambda x, y=i: self.move_image_forward(x, y))
            self.list_frame[i].findChildren(QPushButton)[0].clicked.connect(
                lambda x, y=i: self.attack_btn_clicked(x, y))

            self.list_frame[i].findChildren(QPushButton)[2].clicked.connect(
                lambda x, y=i: self.skill_btn_clicked(x, y))
            self.list_frame[i].findChildren(QPushButton)[2].clicked.connect(
                lambda x, y=i: self.skill_widget_open(x, y))

        if self.bool_meet_monster:
            for btn in self.list_attack_btn:
                btn.clicked.connect(lambda: self.attack_connect(btn))

            self.list_skill_to_enemy[0].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[0]))
            self.list_skill_to_enemy[1].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[1]))
            self.list_skill_to_enemy[2].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[2]))
            self.list_skill_to_enemy[3].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[3]))
            self.list_skill_to_enemy[4].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[4]))
            self.list_skill_to_enemy[5].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[5]))
            self.list_skill_to_enemy[6].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[6]))
            self.list_skill_to_enemy[7].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[7]))
            self.list_skill_to_enemy[8].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[8]))
            self.list_skill_to_enemy[9].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[9]))
            self.list_skill_to_enemy[10].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[10]))
            self.list_skill_to_enemy[11].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[11]))

            self.list_skill_to_user_gard[0].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[1].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[2].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[3].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[4].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[5].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[6].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[6]))

            # mp_up (5.24 미구현 상태)
            # self.list_skill_to_user_gard[7].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[7]))

            self.list_skill_to_user_gard[8].clicked.connect(lambda x, y=i: self.wizard_skill_effect_3(x,y,'map_find', 'map', 70))

        elif self.bool_meet_enemy_monster:
            for btn in self.list_attack_btn:
                btn.clicked.connect(lambda: self.attack_connect(btn))

# -----5.24 변경 부분 (버튼 커넥트)---------------------------------------------------------------------------------------
            self.list_skill_to_enemy[0].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[0]))
            self.list_skill_to_enemy[1].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[1]))
            self.list_skill_to_enemy[2].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[2]))
            self.list_skill_to_enemy[3].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[3]))
            self.list_skill_to_enemy[4].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[4]))
            self.list_skill_to_enemy[5].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[5]))
            self.list_skill_to_enemy[6].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[6]))
            self.list_skill_to_enemy[7].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[7]))
            self.list_skill_to_enemy[8].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[8]))
            self.list_skill_to_enemy[9].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[9]))
            self.list_skill_to_enemy[10].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[10]))
            self.list_skill_to_enemy[11].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[11]))
            self.list_skill_to_enemy[12].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[12]))

            self.list_skill_to_user_gard[0].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[1].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[2].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[3].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[4].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[5].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[6].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[6]))

            # mp_up (5.24 미구현 상태)
            # self.list_skill_to_user_gard[7].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[7]))

            self.list_skill_to_user_gard[8].clicked.connect(lambda x, y=i: self.wizard_skill_effect_3(x,y,'map_find', 'map', 70))

        elif self.bool_meet_gard or self.bool_meet_maze_gard:
            for btn in self.list_attack_btn:
                btn.clicked.connect(lambda: self.attack_connect(btn))

            self.list_skill_to_enemy[0].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[0]))
            self.list_skill_to_enemy[1].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[1]))
            self.list_skill_to_enemy[2].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[2]))
            self.list_skill_to_enemy[3].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[3]))
            self.list_skill_to_enemy[4].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[4]))
            self.list_skill_to_enemy[5].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[5]))
            self.list_skill_to_enemy[6].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[6]))
            self.list_skill_to_enemy[7].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[7]))
            self.list_skill_to_enemy[8].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[8]))
            self.list_skill_to_enemy[9].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[9]))
            self.list_skill_to_enemy[10].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[10]))
            self.list_skill_to_enemy[11].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[11]))
            self.list_skill_to_enemy[12].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[12]))

            self.list_skill_to_user_gard[0].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[1].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[2].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[3].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[4].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[5].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[6].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[6]))

            # mp_up (5.24 미구현 상태)
            # self.list_skill_to_user_gard[7].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[7]))

            self.list_skill_to_user_gard[8].clicked.connect(lambda x, y=i: self.wizard_skill_effect_3(x,y,'map_find', 'map', 70))

        elif self.bool_meet_boss_monster:
            for btn in self.list_attack_btn:
                btn.clicked.connect(lambda: self.attack_connect(btn))

            self.list_skill_to_enemy[0].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[0]))
            self.list_skill_to_enemy[1].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[1]))
            self.list_skill_to_enemy[2].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[2]))
            self.list_skill_to_enemy[3].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[3]))
            self.list_skill_to_enemy[4].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[4]))
            self.list_skill_to_enemy[5].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[5]))
            self.list_skill_to_enemy[6].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[6]))
            self.list_skill_to_enemy[7].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[7]))
            self.list_skill_to_enemy[8].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[8]))
            self.list_skill_to_enemy[9].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[9]))
            self.list_skill_to_enemy[10].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[10]))
            self.list_skill_to_enemy[11].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[11]))
            self.list_skill_to_enemy[12].clicked.connect(lambda: self.skill_connect(self.list_skill_to_enemy[12]))

            self.list_skill_to_user_gard[0].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[1].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[2].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_red', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[3].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_normal', 'part', 30, 70, 30))
            self.list_skill_to_user_gard[4].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_greater', 'part', 60, 100, 50))
            self.list_skill_to_user_gard[5].clicked.connect(
                lambda: self.wizard_skill_effect('wizard_white', 'heal_all', 'all', 40, 80, 70))

            self.list_skill_to_user_gard[6].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[6]))

            # mp_up (5.24 미구현 상태)
            # self.list_skill_to_user_gard[7].clicked.connect(lambda x: self.skill_connect(self.list_skill_to_user_gard[7]))

            self.list_skill_to_user_gard[8].clicked.connect(lambda x, y=i: self.wizard_skill_effect_3(x,y,'map_find', 'map', 70))

    ### 함수 선언 ###
    # [공격]버튼 함수에 connect, 그 전에 몬스터 버튼은 disconnect이 되어있다.
    def attack_connect(self, btn):
        if self.bool_meet_monster:
            loop = self.dict_field_monster['info']['int_cnt']
        elif self.bool_meet_enemy_monster:
            loop = self.dict_maze_monster['int_cnt']
        elif self.bool_meet_gard or self.bool_meet_maze_gard:
            loop = 6
        elif self.bool_meet_boss_monster:
            loop = self.dict_boss_monster['list_field_monster'][0] + 1

        for i in range(loop):
            self.list_enemy_btn[i].disconnect()
        for i in range(loop):
            self.list_enemy_btn[i].clicked.connect(lambda x, y=i, z=self.list_enemy_btn[i]: self.monster_atk_choice(x, y, z))

    def skill_connect(self, btn):
        if self.bool_meet_monster:
            loop = self.dict_field_monster['info']['int_cnt']
        elif self.bool_meet_enemy_monster:
            loop = self.dict_maze_monster['int_cnt']
        elif self.bool_meet_gard or self.bool_meet_maze_gard:
            loop = 6
        elif self.bool_meet_boss_monster:
            loop = self.dict_boss_monster['list_field_monster'][0] + 1

        for i in range(loop):
            self.list_enemy_btn[i].disconnect()
        for i in range(loop):
            if btn == self.list_skill_to_enemy[0]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.warrior_skill_effect(x, y, self.skill_btn_warrior_slice_chop))
            elif btn == self.list_skill_to_enemy[1]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.archer_skill_effect_1(x, y, self.skill_btn_archer_target_shot))
            elif btn == self.list_skill_to_enemy[2]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.archer_skill_effect_2(x, y, self.skill_btn_archer_dual_shot))
            elif btn == self.list_skill_to_enemy[3]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.archer_skill_effect_3(x, y, self.skill_btn_archer_master_shot))
            elif btn == self.list_skill_to_enemy[4]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.swordman_skill_effect(x, y, self.skill_btn_swordman_slice_chop))
            elif btn == self.list_skill_to_enemy[5]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2('wizard_red', 'fire_ball', 'part', 30, 30))
            elif btn == self.list_skill_to_enemy[6]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2('wizard_red', 'fire_wall', 'all', 50, 50))
            elif btn == self.list_skill_to_enemy[7]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2('wizard_red', 'thunder_breaker', 'all', 60, 60, ))
            elif btn == self.list_skill_to_enemy[8]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2('wizard_red', 'bilzzard', 'all', 70, 70))
            elif btn == self.list_skill_to_enemy[9]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2(x, y,'wizard_black', 'fire_ball', 'part', 30, 30))
            elif btn == self.list_skill_to_enemy[10]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2(x, y,'wizard_black', 'fire_wall', 'all', 50, 50))
            elif btn == self.list_skill_to_enemy[11]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2(x, y,'wizard_black', 'thunder_breaker', 'all', 60, 60))
            elif btn == self.list_skill_to_enemy[12]:
                self.list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_2(x, y,'wizard_black', 'bilzzard', 'all', 70, 70))

#-----5.24 추가 부분 (백법사의 hp_up)-------------------------------------------------------------------------------------
        for i in range(5):
            if btn == self.list_skill_to_user_gard[6]:
                # 유저 수호대 공격버튼이 사용가능한 상태라면
                if self.list_attack_btn[i].isEnabled():
                    self.user_gard_frame.findChildren(QPushButton)[i].setEnabled(True)
                    # 백법사 버튼 비활성화
                    self.user_gard_frame.findChildren(QPushButton)[5].setDisabled(True)
                # 유저 수호대 공격버튼이 사용 불가상태라면
                elif not self.list_attack_btn[i].isEnabled():
                    self.user_gard_frame.findChildren(QPushButton)[i].setEnabled(False)
                    self.user_gard_frame.findChildren(QPushButton)[5].setEnabled(True)
                self.stackedWidget.setCurrentIndex(7)
                self.user_gard_frame.findChildren(QPushButton)[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_3(x,y,'hp_up', 'hp', 30))

            # mp_up
            elif btn == self.list_skill_to_user_gard[7]:
                survivor = []
                for k, v in self.dict_user_gard.items():
                    if k not in ['gard', 'location']:
                        if self.dict_user_gard[k]['survival']:
                            survivor.append(k)
                    if self.user_gard_frame.findChildren(QPushButton)[i].objectName() in survivor:
                        self.user_gard_frame.findChildren(QPushButton)[i].setEnabled(True)
                self.stackedWidget.setCurrentIndex(7)
                self.user_gard_frame.findChildren(QPushButton)[5].setDisabled(True)
                self.user_gard_frame.findChildren(QPushButton)[i].clicked.connect(
                    lambda x, y=i: self.wizard_skill_effect_3(x, y, 'mp_up', 'mp', 50))

# 전투결과(승패) 반환
    def show_war_result(self):
        user_died = 0
        enemy_died = 0
        if self.bool_meet_gard:
            for a in range(6):
                if self.dict_enemy_gard[self.list_job[a]]['hp'] <= 0:
                    enemy_died += 1
                if enemy_died == 6:
                    self.battle_dialog.append(f"수호대 {a + 1}명 처치")
                    self.bool_war_result = True
                    self.close()
            for b in self.list_job:
                if not self.dict_user_gard[b]['survival']:
                    user_died += 1
                if user_died == 6:
                    self.battle_dialog.append("전투 결과 : 수호대 전투 패배")
                    self.bool_war_result = False
                    self.close()
        elif self.bool_meet_monster:
            for c in range(self.dict_field_monster['info']['int_cnt']):
                if self.dict_field_monster['info']['hp'][c] <= 0:
                    enemy_died += 1
                if enemy_died == len(self.monster_li):
                    self.battle_dialog.append(f"전투 결과 : 몬스터 처치")
                    self.bool_war_result = True
                    self.close()
            for d in self.list_job:
                if not self.dict_user_gard[d]['survival']:
                    user_died += 1
                if user_died == 6:
                    self.battle_dialog.append("전투 결과 : 일반몬스터 전투 패배")
                    self.bool_war_result = False
                    self.close()
        elif self.bool_meet_maze_gard:
            for e in range(6):
                if self.dict_enemy_gard[self.list_job[e]]['hp'] <= 0:
                    enemy_died += 1
                if enemy_died == 6:
                    self.battle_dialog.append(f"수호대 {e + 1}명 처치")
                    self.bool_war_result = True
                    self.close()
            for f in self.list_job:
                if not self.dict_user_gard[f]['survival']:
                    user_died += 1
                if user_died == 6:
                    self.battle_dialog.append("전투 결과 : 수호대 전투 패배")
                    self.bool_war_result = False
                    self.close()
        elif self.bool_meet_enemy_monster:
            for g in range(self.dict_maze_monster['int_cnt']):
                if self.dict_maze_monster['list_hp'][g] <= 0:
                    enemy_died += 1
                if enemy_died == 6:
                    self.battle_dialog.append(f"{g + 1}번째 몬스터 처치")
                    self.bool_war_result = True
                    self.close()
            for h in self.list_job:
                if not self.dict_user_gard[h]['survival']:
                    user_died += 1
                if user_died == 6:
                    self.battle_dialog.append("전투 결과 : 일반몬스터 전투 패배")
                    self.bool_war_result = False
                    self.close()
        elif self.bool_meet_boss_monster:
            if self.dict_boss_monster['hp'] <= 0:
                self.battle_dialog.append(f"보스 몬스터를 처치했다!")
                self.bool_war_result = True
                self.close()
            for j in self.list_job:
                if not self.dict_user_gard[j]['survival']:
                    user_died += 1
                if user_died == 6:
                    self.battle_dialog.append("전투 결과 : 보스몬스터 전투 패배")
                    self.bool_war_result = False
                    self.close()

        return self.bool_war_result

# 전투 횟수 카운트
    def war_cnt(self):
        if self.bool_war_result:
            self.int_war_cnt += 1
        elif not self.bool_war_result:
            self.int_war_cnt += 1
        return self.int_war_cnt

# 전투횟수에 따른 EXP상승(n0레벨까지 n0판 당 +n레벨 상승) -> return
    def user_gard_lv_update(self):
        str_lv_update_msg1 = ''
        str_lv_update_msg2 = ''
        list_update_job1 = []
        list_update_job2 = []
        up1 = int
        for i in range(6):
            if self.int_war_cnt == 10:
                self.dict_user_gard[self.list_job[i]]['lv'] += 1
                list_update_job1.append(self.list_job[i])
                up1 = 1
            elif self.int_war_cnt == 20:
                self.dict_user_gard[self.list_job[i]]['lv'] += 2
                list_update_job1.append(self.list_job[i])
                up1 = 2
            elif self.int_war_cnt == 30:
                self.dict_user_gard[self.list_job[i]]['lv'] += 3
                list_update_job1.append(self.list_job[i])
                up1 = 3
            elif self.int_war_cnt == 40:
                self.dict_user_gard[self.list_job[i]]['lv'] += 4
                list_update_job1.append(self.list_job[i])
                up1 = 4
            elif self.int_war_cnt == 50:
                self.dict_user_gard[self.list_job[i]]['lv'] += 5
                list_update_job1.append(self.list_job[i])
                up1 = 5
            elif self.int_war_cnt == 60:
                self.dict_user_gard[self.list_job[i]]['lv'] += 6
                list_update_job1.append(self.list_job[i])
                up1 = 6
            elif self.int_war_cnt == 70:
                self.dict_user_gard[self.list_job[i]]['lv'] += 7
                list_update_job1.append(self.list_job[i])
                up1 = 7
            elif self.int_war_cnt == 80:
                self.dict_user_gard[self.list_job[i]]['lv'] += 8
                list_update_job1.append(self.list_job[i])
                up1 = 8
            elif self.int_war_cnt == 90:
                self.dict_user_gard[self.list_job[i]]['lv'] += 9
                list_update_job1.append(self.list_job[i])
                up1 = 9
            elif self.int_war_cnt == 100:
                self.dict_user_gard[self.list_job[i]]['lv'] += 10
                list_update_job1.append(self.list_job[i])
                up1 = 10

            # 보스몬스터 처치시 n층별 +n레벨
            if self.bool_boss_death == True:
                if self.int_floor == 1:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 1
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 2:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 2
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 3:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 3
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 4:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 4
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 5:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 5
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 6:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 6
                    list_update_job2.append(self.list_job[i])
                elif self.int_floor == 7:
                    self.dict_user_gard[self.list_job[i]]['lv'] += 7
                    list_update_job2.append(self.list_job[i])

        list_update_job1 = ','.join(list_update_job1)
        str_lv_update_msg1 = f"{list_update_job1}의 레벨 +{up1}상승"

        list_update_job2 = ','.join(list_update_job2)
        str_lv_update_msg2 = f"{list_update_job2}의 레벨 {self.int_floor}증가"

        return self.dict_user_gard, str_lv_update_msg1, str_lv_update_msg2

    # 10레벨당 전 공격력의 * 10% 상승 -> return
    def user_gard_power_update(self):
        str_power_update_msg = ''
        list_update_job3 = []
        for i in range(6):
            if self.dict_user_gard[self.list_job[i]]['lv'] % 10 == 0:
                self.dict_user_gard[self.list_job[i]]['power'] += self.dict_user_gard[self.list_job[i]]['power'] * 0.1
                list_update_job3.append(self.list_job[i])

            list_update_job3 = ','.join(list_update_job3)
            str_power_update_msg = f"{list_update_job3}의 공격력 10% 증가"

        return self.dict_user_gard, str_power_update_msg

    # 유저수호대 레벨에 따른 HP,MP 상승과 레벨 -> return
    def user_gard_hpmp_update(self):
        str_hpmp_update_msg = ''
        list_update_job4 = []
        up2 = ''
        for i in range(6):
            if self.dict_user_gard[self.list_job[i]]['lv'] <= 10:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.1
                if i == 0:
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.1
                    list_update_job4.append(self.list_job[i])
                up2 = '1.1'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 10:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.2
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.2
                    list_update_job4.append(self.list_job[i])
                up2 = '1.2'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 30:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.3
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.3
                    list_update_job4.append(self.list_job[i])
                up2 = '1.3'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 40:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]] * 1.4
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.4
                    list_update_job4.append(self.list_job[i])
                up2 = '1.4'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 50:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.5
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.5
                    list_update_job4.append(self.list_job[i])
                up2 = '1.5'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 60:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.6
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.6
                    list_update_job4.append(self.list_job[i])
                up2 = '1.6'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 70:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.7
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.7
                    list_update_job4.append(self.list_job[i])
                up2 = '1.7'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 80:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.8
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.8
                    list_update_job4.append(self.list_job[i])
                up2 = '1.8'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 90:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 1.9
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 1.9
                    list_update_job4.append(self.list_job[i])
                up2 = '1.9'
            elif self.dict_user_gard[self.list_job[i]]['lv'] <= 100:
                self.dict_user_gard[self.list_job[i]]['hp'] += self.dict_user_gard[self.list_job[i]]['hp'] * 2.0
                if self.list_job[i] == 'warrior':
                    self.dict_user_gard[self.list_job[i]]['mp'] = 0
                else:
                    self.dict_user_gard[self.list_job[i]]['mp'] += self.dict_user_gard[self.list_job[i]]['mp'] * 2.0
                    list_update_job4.append(self.list_job[i])
                up2 = '2.0'

        list_update_job4 = ','.join(list_update_job4)
        str_hpmp_update_msg = f"{self.list_job[0]}의 hp가 1.1 상승, {list_update_job4}의 hp, mp가 {up2} 상승"

        return self.dict_user_gard, str_hpmp_update_msg

    # 배틀 로케이션과 만난 적 확인
    def battle_location(self):
        if self.bool_meet_gard:
            self.battle_gard()
        elif self.bool_meet_monster:
            self.battle_monster()
        elif self.bool_meet_maze_gard:
            self.battle_gard()
        elif self.bool_meet_enemy_monster:
            self.battle_monster()
        elif self.bool_meet_boss_monster:
            self.battle_boss_monster()

    # -------------전투 공통 함수---------------------------------------------------------------------------------_----------#
    # 전투화면으로 전환시 각 캐릭터의 [공격]버튼에 따른 QDialog창 생성
    def atk_choice(self, x, index):

        self.atk_dialog = QDialog()
        self.atk_dialog.setWindowTitle("ATTACK")

        radio_button1 = QRadioButton(f"물리공격(현재 공격력: {self.dict_user_gard[self.list_job[index]]['power']})")
        OK_button = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(radio_button1)
        layout.addWidget(OK_button)
        self.atk_dialog.setLayout(layout)

        if radio_button1.isChecked:
            self.name = self.list_job[index]
            self.selected_option = self.dict_user_gard[self.list_job[index]]['power']

        OK_button.clicked.connect(self.atk_dialog_close)
        self.atk_dialog.exec_()

    # 각 캐릭터의 [공격]버튼에 따른 QDialog창 닫기
    def atk_dialog_close(self):
        self.atk_dialog.close()

    # 한번 누른 구성원의 [공격]버튼은 적의 턴이 끝날때 까지 비활성화.
    def attack_btn_clicked(self, x, index):
        survivor = []
        if not x:
            self.list_attack_btn[index].setEnabled(False)
            self.list_skill_btn[index].setEnabled(False)
            self.int_btn_clicked_cnt += 1
        for k, v in self.dict_user_gard.items():
            if k not in ['gard', 'location']:
                if self.dict_user_gard[k]['survival']:
                    survivor.append(k)
        print(f"len(survivor): {len(survivor)}")
        print(f"int_btn_clicked_cnt: {self.int_btn_clicked_cnt}")
        if self.int_btn_clicked_cnt == len(survivor):
            for i, job in enumerate(self.list_job):
                if self.dict_user_gard[job]['survival']:
                    self.list_attack_btn[i].setEnabled(True)
                    self.list_skill_btn[i].setEnabled(True)
                    self.int_btn_clicked_cnt = 0

    # 한번 누른 구성원의 [스킬]버튼은 적의 턴이 끝날때 까지 비활성화.
    def skill_btn_clicked(self, x, index):
        if not x:
            self.list_attack_btn[index].setEnabled(False)
            self.list_skill_btn[index].setEnabled(False)
            self.int_btn_clicked_cnt = index + 1
        for i, job in enumerate(self.list_job):
            if self.dict_user_gard[job]['survival']:
                self.int_survival += 1
                print(f'self.int_survival: {self.int_survival}')
        if self.int_btn_clicked_cnt == self.int_survival:
            for i, job in enumerate(self.list_job):
                if self.dict_user_gard[job]['survival']:
                    self.list_attack_btn[i].setEnabled(True)
                    self.list_skill_btn[i].setEnabled(True)
                    self.int_btn_clicked_cnt = 0

    # [스킬]버튼에 따른 직업별 스킬창으로 화면전환(gif)
    def skill_widget_open(self, x, index):
        self.list_skill_btn = []
        list_gif_lb = []
        if index == 3:
            self.movie = QMovie('../wizard_red/skill2.gif', QByteArray(), self)
            self.gif_3_1.setMovie(self.movie)
            self.movie.start()
        for i in range(6):
            list_gif_lb.append(getattr(self, f"gif_{i}"))
            self.list_skill_btn.append(getattr(self, f"pb_skill_job_{self.list_job[i]}"))
            self.movie = QMovie(f'../{self.list_job[i]}/skill.gif', QByteArray(), self)
            list_gif_lb[i].setMovie(self.movie)
            self.movie.start()

        if index == 3:
            self.stackedWidget.setCurrentIndex(4)
        elif index == 4:
            self.stackedWidget.setCurrentIndex(5)
        elif index == 5:
            self.stackedWidget.setCurrentIndex(6)
        else:
            self.stackedWidget.setCurrentIndex(index + 1)

        # 직업 레벨에 따른 버튼 활성화/비활성화
        job_skill_btn = self.sender()
        job_skill_choice = []
        for i, button in enumerate(self.list_skill_btn):  # 여기서 button = 각 직업의 [스킬]버튼
            dict_skill_list = self.dict_user_gard[self.list_job[i]]['skill']  # dict_skill_list는 각 직업의 skill 딕셔너리가 담긴다.
            if job_skill_btn == button:
                for lv, name in dict_skill_list.items():
                    if self.list_job[i] == 'wizard_red':
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_normal'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_greater'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_all'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_fire_ball'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_fire_wall'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_thunder_breaker'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_bilzzard'))
                    elif self.list_job[i] == 'wizard_white':
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_normal'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_greater'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_heal_all'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_hp_up'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_mp_up'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{self.list_job[i]}_map_find'))
                    else:
                        button_name = f"skill_btn_{self.list_job[i]}_{name}"
                        job_skill_choice.append(getattr(self, button_name))
                    for k in job_skill_choice:
                        if self.dict_user_gard[self.list_job[i]]['lv'] < lv:
                            if self.list_job[i] == 'archer':
                                index = 17
                                if k.objectName()[index:] == dict_skill_list[lv]:
                                    k.setDisabled(True)
                            elif self.list_job[i] == 'wizard_red':  # 15의 fire_ball heal_greater 안됌
                                index = 21
                                if k.objectName()[index:] == dict_skill_list[lv]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][0]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][1]:
                                    k.setDisabled(True)
                            elif self.list_job[i] == 'wizard_black' or self.list_job[i] == 'wizard_white':
                                index = 23
                                if k.objectName()[index:] == dict_skill_list[lv]:  # 15, 30의 4개 스킬 버튼 모두 활성화됨.
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][0]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][1]:
                                    k.setDisabled(True)
                            else:
                                k.setDisabled(True)

    # -------------스킬 구간----------------------------------------------------------------------------#
    # 전투 후 스킬사용에 따른 초기화
    def reset_user_gard(self):
        for i in range(6):
            self.dict_user_gard[self.list_job[i]]['power'] = self.list_origin_power[i]
        if not self.bool_war_result:
            self.dict_user_gard['warrior']['power'] = self.origin_power
            for i in range(6):
                self.dict_user_gard[self.list_job[i]]['power'] = self.list_origin_power[i]

    def warrior_skill_effect(self, x, index, btn):
        if btn.objectName() == 'skill_btn_warrior_slice_chop':
            origin_power = self.dict_user_gard['warrior']['power']
            print(origin_power)
            power_up = random.randint(2, 50)
            self.dict_user_gard['warrior']['power'] = self.dict_user_gard['warrior']['power'] * power_up
            damage = self.dict_user_gard['warrior']['power'] * power_up
            print(self.dict_user_gard['warrior']['power'])
            self.stackedWidget.setCurrentIndex(0)
            self.battle_dialog.append(
                f"warrior의 slice_chop사용! 공격력 {power_up}배 증가! [warrior] POWER: {self.dict_user_gard['warrior']['power']}")
            self.dict_user_gard['warrior']['power'] = origin_power

            if self.bool_meet_monster:
                self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][index] - damage}")
                if self.dict_field_monster['info']['hp'][index] <= 0:
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_enemy_monster:
                self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                if self.dict_maze_monster['list_hp'][index] <= 0:
                    self.dict_maze_monster['list_hp'][index] = 0
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_gard or self.bool_meet_maze_gard:
                self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                       'hp'] - damage
                self.list_enemy_line[index].setText(
                    f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                    self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_boss_monster:
                if index == 0:
                    self.hp_enemy_0.setText(
                        f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
                    self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                    if self.dict_boss_monster['hp'] <= 0:
                        self.dict_boss_monster['hp'] = 0
                        self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                        self.enemy_0.setDisabled(True)
                else:
                    self.list_enemy_line[index].setText(
                        f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
                    self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                        self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                    if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

            self.monster_turn()
            return self.dict_user_gard

    def archer_skill_effect_1(self, x, index, btn):
        if btn.objectName() == 'skill_btn_archer_target_shot':
            power_up = random.choice([1.2, 1.3, 1.4, 1.5])
            origin_power = self.dict_user_gard['archer']['power']
            damage = origin_power * power_up
            self.dict_user_gard['archer']['mp'] -= 30
            self.stackedWidget.setCurrentIndex(0)
            self.battle_dialog.append(f"[궁수]의 Target shot 사용! [궁수] 공격력 {power_up}배 증가!")
            self.battle_dialog.append(f"[궁수]의 MP가 30줄었습니다.")

            if self.bool_meet_monster:
                self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][index] - damage}")
                if self.dict_field_monster['info']['hp'][index] <= 0:
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_enemy_monster:
                self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                if self.dict_maze_monster['list_hp'][index] <= 0:
                    self.dict_maze_monster['list_hp'][index] = 0
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_gard or self.bool_meet_maze_gard:
                self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                       'hp'] - damage
                self.list_enemy_line[index].setText(
                    f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                    self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_boss_monster:
                if index == 0:
                    self.hp_enemy_0.setText(
                        f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
                    self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                    if self.dict_boss_monster['hp'] <= 0:
                        self.dict_boss_monster['hp'] = 0
                        self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                        self.enemy_0.setDisabled(True)
                else:
                    self.list_enemy_line[index].setText(
                        f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
                    self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                        self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                    if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP: 0 ")
                        self.list_enemy_btn[index].setDisabled(True)

        self.monster_turn()
        return self.dict_user_gard

    def archer_skill_effect_2(self, x, index, btn):
        if btn.objectName() == 'skill_btn_archer_dual_shot':
            if not x:
                self.skill_effect_2 += 1

            print(self.skill_effect_2)
            if self.skill_effect_2 % 2 == 0:
                msg = QMessageBox()
                skill_ban = msg.critical(self, "스킬 사용 제한", "해당 기술을 다음 턴에 사용가능합니다.", msg.Ok)
                if skill_ban == msg.Ok:  # 버튼의 이름을 넣으면 됩니다.
                    self.stackedWidget.setCurrentIndex(2)
            else:
                power_up = random.choice([1.4, 1.5, 1.6])
                origin_power = self.dict_user_gard['archer']['power']
                damage = origin_power * power_up
                self.dict_user_gard['archer']['mp'] -= 50
                self.stackedWidget.setCurrentIndex(0)
                self.battle_dialog.append(f"[궁수]의 Dual shot 사용! [궁수] 공격력 {power_up}배 증가!")
                self.battle_dialog.append(f"[궁수]의 MP가 50줄었습니다.")

                if self.bool_meet_monster:
                    self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][index]}")
                    if self.dict_field_monster['info']['hp'][index] <= 0:
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_enemy_monster:
                    self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index]}")
                    if self.dict_maze_monster['list_hp'][index] <= 0:
                        self.dict_maze_monster['list_hp'][index] = 0
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_gard or self.bool_meet_maze_gard:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                           'hp'] - damage
                    self.list_enemy_line[index].setText(
                        f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                    if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                        self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                        self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_boss_monster:
                    if index == 0:
                        self.hp_enemy_0.setText(
                            f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp']}")
                        self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                        if self.dict_boss_monster['hp'] <= 0:
                            self.dict_boss_monster['hp'] = 0
                            self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                            self.enemy_0.setDisabled(True)
                    else:
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1]}")
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                            self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                        if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                            self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                            self.list_enemy_line[index].setText(
                                f"던전몬스터 HP: 0")
                            self.list_enemy_btn[index].setDisabled(True)

        self.monster_turn()
        return self.dict_user_gard

    def archer_skill_effect_3(self, x, index, btn):
        if btn.objectName() == 'skill_btn_archer_master_shot':
            skill_effect_3 = 0
            if not x:
                skill_effect_3 += 1

            if skill_effect_3 % 2 == 0:
                msg = QMessageBox()
                skill_ban = msg.critical(self, "스킬 사용 제한", "해당 기술을 다음 턴에 사용가능합니다.", msg.Ok)
                if skill_ban == msg.Yes:  # 버튼의 이름을 넣으면 됩니다.
                    self.stackedWidget.setCurrentIndex(2)
            else:
                power_up = random.choice([1.5, 1.6, 1.7])
                origin_power = self.dict_user_gard['archer']['power']
                damage = origin_power * power_up
                self.dict_user_gard['archer']['mp'] -= 70
                self.stackedWidget.setCurrentIndex(0)
                self.battle_dialog.append(f"[궁수]의 Target shot으로 현 전투 중 모든 구성원의 공격력이 {power_up}배 증가! ")
                self.battle_dialog.append(f"[궁수]의 MP가 70줄었습니다.")

                if self.bool_meet_monster:
                    self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(
                        f"몬스터 HP:{self.dict_field_monster['info']['hp'][index] - damage}")
                    if self.dict_field_monster['info']['hp'][index] <= 0:
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_enemy_monster:
                    self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                    if self.dict_maze_monster['list_hp'][index] <= 0:
                        self.dict_maze_monster['list_hp'][index] = 0
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_gard or self.bool_meet_maze_gard:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                           'hp'] - damage
                    self.list_enemy_line[index].setText(
                        f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                    if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                        self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                        self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_boss_monster:
                    if index == 0:
                        self.hp_enemy_0.setText(
                            f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
                        self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                        if self.dict_boss_monster['hp'] <= 0:
                            self.dict_boss_monster['hp'] = 0
                            self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                            self.enemy_0.setDisabled(True)
                    else:
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                            self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                        if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                            self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                            self.list_enemy_line[index].setText(
                                f"던전몬스터 HP: 0")
                            self.list_enemy_btn[index].setDisabled(True)

        self.monster_turn()
        return self.dict_user_gard

    def swordman_skill_effect(self, x, index, btn):
        if btn.objectName() == 'skill_btn_swordman_slice_chop':
            origin_power = self.dict_user_gard['warrior']['power']
            power_up = random.randint(2, 50)
            damage = self.dict_user_gard['swordman']['power'] * power_up
            self.dict_user_gard['swordman']['mp'] -= 50
            self.stackedWidget.setCurrentIndex(0)
            self.battle_dialog.append(
                f"[검사]의 slice_chop사용! 공격력 {power_up}배 증가! [검사] POWER: {damage}만큼 올랐다! ")
            self.dict_user_gard['swordman']['power'] = origin_power
            self.battle_dialog.append(f"[검사]의 MP가 50줄었습니다.")

            if self.bool_meet_monster:
                self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][index] - damage}")
                if self.dict_field_monster['info']['hp'][index] <= 0:
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_enemy_monster:
                self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                if self.dict_maze_monster['list_hp'][index] <= 0:
                    self.dict_maze_monster['list_hp'][index] = 0
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_gard or self.bool_meet_maze_gard:
                self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                       'hp'] - damage
                self.list_enemy_line[index].setText(
                    f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                    self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_boss_monster:
                if index == 0:
                    self.hp_enemy_0.setText(
                        f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
                    self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                    if self.dict_boss_monster['hp'] <= 0:
                        self.dict_boss_monster['hp'] = 0
                        self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                        self.enemy_0.setDisabled(True)
                else:
                    self.list_enemy_line[index].setText(
                        f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
                    self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                        self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                    if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

        self.monster_turn()
        return self.dict_user_gard

    def wizard_skill_effect(self, str_job, str_skill_name, str_part_or_all, int_min, int_max, int_mp):
        # 힐량
        heal = random.randint(int_min, int_max)
        # 체력이 가장 낮은 구성원의 체력을 회복
        if str_part_or_all == 'part':
            list_hp = []
            for k, v in self.dict_user_gard.items():
                if k not in ['gard', 'location']:
                    list_hp.append(self.dict_user_gard[k]['hp'])
            min_hp = min(list_hp)
            for k, v in self.dict_user_gard.items():
                if k not in ['gard', 'location']:
                    if min_hp == self.dict_user_gard[k]['hp']:
                        low_hp_job = k
                        break
            self.dict_user_gard[low_hp_job]['hp'] += self.dict_user_gard[low_hp_job]['max_hp'] * (heal / 100)
            # 체력이 최대체력보다 크면 체력 = 최대체력
            if self.dict_user_gard[low_hp_job]['hp'] > self.dict_user_gard[low_hp_job]['max_hp']:
                self.dict_user_gard[low_hp_job]['hp'] = self.dict_user_gard[low_hp_job]['max_hp']
            self.battle_dialog.append(
                f"{str_job}의 {str_skill_name}사용으로 {low_hp_job}의 체력이 최대체력의 {heal}% 증가하여 {self.dict_user_gard[low_hp_job]['max_hp'] * (heal / 100)}만큼 올랐다! ")
            self.battle_dialog.append(f"{str_job}의 MP가 {int_mp}줄었습니다.")
            self.dict_user_gard[str_job]['mp'] -= int_mp
            self.stackedWidget.setCurrentIndex(0)

        # 모든 구성원의 체력을 회복
        else:
            for k, v in self.dict_user_gard.items():
                if k not in ['gard', 'location']:
                    k['hp'] += self.dict_user_gard[self.list_job]['max_hp'] * (heal / 100)
                    if k['hp'] > k['max_hp']:
                        k['hp'] = k['max_hp']
                    self.battle_dialog.append(
                        f"wizard_red의 {str_skill_name}사용으로 {k}의 체력이 최대체력의 {heal}% 증가하여 {k['max_hp'] * (heal / 100)}만큼 올랐다! ")
            self.battle_dialog.append(f"{str_job}의 MP가 {int_mp}줄었습니다.")
            self.dict_user_gard[str_job]['mp'] -= int_mp
            self.stackedWidget.setCurrentIndex(0)

        self.monster_turn()
        return self.dict_user_gard

    def wizard_skill_effect_2(self, x, index, str_job, str_skill_name, str_part_or_all, int_value, int_mp):
        # 타켓 공격
        if str_part_or_all == 'part':
            if str_skill_name == 'fire_ball':
                origin_power = self.dict_user_gard[str_job]['power']
                damage = self.dict_user_gard[str_job]['power'] * ((100 + int_value) / 100)
                # self.battle_dialog.append(
                #     f"wizard_red의 {str_skill_name}사용으로 {k}의 체력이 최대체력의 {heal}% 증가하여 {k['max_hp'] * (heal / 100)}만큼 올랐다! ")
                # self.battle_dialog.append(f"wizard_red의 MP가 {int_mp}줄었습니다.")
                self.dict_user_gard[str_job]['power'] = origin_power
                self.battle_dialog.append(f"{str_job}이 {self.monster_li[index]}에게 {damage}만큼 피해를 끼쳤다!")
                self.battle_dialog.append(f"{str_job}의 MP가 {int_mp}줄었습니다.")
                self.dict_user_gard[str_job]['mp'] -= int_mp
                self.stackedWidget.setCurrentIndex(0)

                if self.bool_meet_monster:
                    self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(
                        f"몬스터 HP:{self.dict_field_monster['info']['hp'][index]}")
                    if self.dict_field_monster['info']['hp'][index] <= 0:
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_enemy_monster:
                    self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index]}")
                    if self.dict_maze_monster['list_hp'][index] <= 0:
                        self.dict_maze_monster['list_hp'][index] = 0
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_gard or self.bool_meet_maze_gard:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                           'hp'] - damage
                    self.list_enemy_line[index].setText(
                        f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                    if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                        self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                        self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

                elif self.bool_meet_boss_monster:
                    if index == 0:
                        self.hp_enemy_0.setText(
                            f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp']}")
                        self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                        if self.dict_boss_monster['hp'] <= 0:
                            self.dict_boss_monster['hp'] = 0
                            self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                            self.enemy_0.setDisabled(True)
                    else:
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1]}")
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                            self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                        if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                            self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                            self.list_enemy_line[index].setText(
                                f"던전몬스터 HP: 0")
                            self.list_enemy_btn[index].setDisabled(True)

        # 광역 공격
        else:
            if str_skill_name == 'fire_wall':
                damage = self.dict_user_gard[str_job]['power'] * ((100 + int_value) / 100)
            elif str_skill_name == 'thunder_breaker':
                damage = self.dict_user_gard[str_job]['power'] * ((100 + int_value) / 100)
            elif str_skill_name == 'bilzzard':
                damage = self.dict_user_gard[str_job]['power'] * ((100 + int_value) / 100)
            # self.battle_dialog.append(
            #     f"wizard_red의 {str_skill_name}사용으로 {k}의 체력이 최대체력의 {heal}% 증가하여 {k['max_hp'] * (heal / 100)}만큼 올랐다! ")
            # self.battle_dialog.append(f"wizard_red의 MP가 {int_mp}줄었습니다.")
            self.battle_dialog.append(f"{str_job}이 모든 몬스터에게 {damage}만큼 피해를 입혔다!")
            self.battle_dialog.append(f"{str_job}의 MP가 {int_mp}줄었습니다.")
            self.dict_user_gard[str_job]['mp'] -= int_mp
            self.stackedWidget.setCurrentIndex(0)

            if self.bool_meet_monster:
                for i in range(self.dict_field_monster['info']['int_cnt']):
                    self.dict_field_monster['info']['hp'][i] = self.dict_field_monster['info']['hp'][i] - damage
                    self.list_enemy_line[i].setText(
                        f"몬스터 HP:{self.dict_field_monster['info']['hp'][i]}")
                    if self.dict_field_monster['info']['hp'][i] <= 0:
                        self.list_enemy_line[i].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[i].setDisabled(True)

            elif self.bool_meet_enemy_monster:
                for i in range(self.dict_maze_monster['int_cnt']):
                    self.dict_maze_monster['list_hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                    self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                    if self.dict_maze_monster['list_hp'][index] <= 0:
                        self.dict_maze_monster['list_hp'][index] = 0
                        self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_gard or self.bool_meet_maze_gard:
                self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]][
                                                                       'hp'] - damage
                self.list_enemy_line[index].setText(
                    f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
                if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                    self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                    self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_boss_monster:
                if index == 0:
                    self.hp_enemy_0.setText(
                        f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
                    self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                    if self.dict_boss_monster['hp'] <= 0:
                        self.dict_boss_monster['hp'] = 0
                        self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                        self.enemy_0.setDisabled(True)
                else:
                    self.list_enemy_line[index].setText(
                        f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
                    self.dict_boss_monster['list_field_monster'][1][index - 1] = \
                        self.dict_boss_monster['list_field_monster'][1][index - 1] - damage
                    if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                        self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                        self.list_enemy_line[index].setText(
                            f"던전몬스터 HP: 0")
                        self.list_enemy_btn[index].setDisabled(True)

        self.monster_turn()
        return self.dict_user_gard

    def wizard_skill_effect_3(self, x, index, str_skill_name, str_hp_or_mp_or_map, minus_mp):
        # 백법사가 공격력, mp를 올려줄 유저 수호대를 선택한다. (선택 대상에 본인은 제외한다.->코드 553번줄)
        # 선택할 수 있는 유저의 버튼은 턴 소모를 하지 않은 자들 뿐이다.
        # 선택된 유저 수호대의 공격력이 1턴 50~70% 상승되고 바로 적을 공격한다. = damage
        # 모든 직업이 턴을 소모했다면 백법사의 공격력이 상승하여 바로 적을 공격한다.

        if str_skill_name == 'hp_up':
            if str_hp_or_mp_or_map == 'hp':
                origin_power = self.dict_user_gard[self.list_job[index]]['power']
                power_up = random.choice([1.5,1.6,1.7])
                damage = origin_power * power_up

                self.battle_dialog.append(f"[백법사]의 {str_skill_name} 사용! {self.list_job[index]}의 공격력이 {power_up}배 상승!")
                self.battle_dialog.append(f"{self.list_job[index]}의 공격력 : {damage} (1턴 유지)")

                if self.bool_meet_monster:
                    for i in range(self.dict_field_monster['info']['int_cnt']):
                        if self.dict_field_monster['info']['hp'][i] > 0:
                            target_enemy = self.monster_li[i]
                            self.dict_field_monster['info']['hp'][i] -= damage
                            self.list_enemy_line[i].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][i]}")
                        if self.dict_field_monster['info']['hp'][i] <= 0:
                            self.list_enemy_line[i].setText(f"몬스터 HP: 0")
                            self.list_enemy_btn[i].setDisabled(True)

                elif self.bool_meet_enemy_monster:
                    for i in range(self.dict_maze_monster['int_cnt']):
                        if self.dict_maze_monster['list_hp'][i] > 0:
                            target_enemy = self.monster_li[i]
                            self.dict_maze_monster['list_hp'][i] -= damage
                            self.list_enemy_line[i].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][i]}")
                        if self.dict_maze_monster['list_hp'][i] <= 0:
                            self.dict_maze_monster['list_hp'][i] = 0
                            self.list_enemy_line[i].setText(f"몬스터 HP: 0")
                            self.list_enemy_btn[i].setDisabled(True)

                elif self.bool_meet_gard or self.bool_meet_maze_gard:
                    for i in range(6):
                        if self.dict_enemy_gard[self.list_job[i]] > 0:
                            target_enemy = self.dict_enemy_gard[self.list_job[i]]
                        self.dict_enemy_gard[self.list_job[i]]['hp'] = self.dict_enemy_gard[self.list_job[i]]['hp'] - damage
                        self.list_enemy_line[i].setText(
                        f"{self.list_job[i]} HP:{self.dict_enemy_gard[self.list_job[i]]['hp']}")
                        if self.dict_enemy_gard[self.list_job[i]]['hp'] <= 0:
                            self.dict_enemy_gard[self.list_job[i]]['hp'] = 0
                            self.list_enemy_line[i].setText(f"{self.list_job[i]} HP: 0")
                            self.list_enemy_btn[i].setDisabled(True)

                elif self.bool_meet_boss_monster:
                    target_enemy = self.dict_boss_monster['name']
                    self.dict_boss_monster['hp'] = self.dict_boss_monster['hp'] - damage
                    self.hp_enemy_0.setText(
                        f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp']}")
                    if self.dict_boss_monster['hp'] <= 0:
                        self.dict_boss_monster['hp'] = 0
                        self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: 0")
                        self.enemy_0.setDisabled(True)

                self.battle_dialog.append(f"{self.list_job[index]}의 {target_enemy}공격!")
                self.list_attack_btn[index].setDisabled(True)
                self.list_skill_btn[index].setDisabled(True)
                self.int_btn_clicked_cnt += 1
                self.stackedWidget.setCurrentIndex(0)
                self.battle_dialog.append(f"스킬 사용으로 [백법사]의 MP {minus_mp}소진")
                self.dict_user_gard['wizard_white']['mp'] -= minus_mp
                self.battle_dialog.append(f"[확인용] {self.list_job[index]}의 공격력 : {self.dict_user_gard[self.list_job[index]]['power']}")

        # 유저 수호대의 방어력을 1턴 50%상승시킨다.
        elif str_skill_name == 'mp_up':
            if str_hp_or_mp_or_map == 'mp':
                self.mp_up_used = ''
                self.mp_up_used = self.list_job[index]
                self.origin_mp = self.dict_user_gard[self.list_job[index]]['mp']
                self.battle_dialog.append(f"[백법사]의 {str_skill_name} 사용! {self.list_job[index]}의 방어력이 {1.5}배 상승!")
                self.dict_user_gard[self.list_job[index]]['mp'] = self.origin_mp * 1.5
                self.battle_dialog.append(f"{self.list_job[index]}의 mp : {self.origin_mp * 1.5} (1턴 유지)")
                self.battle_dialog.append(f"스킬 사용으로 [백법사]의 MP{minus_mp}소진")
                self.dict_user_gard['wizard_white']['mp'] -= minus_mp
                self.stackedWidget.setCurrentIndex(0)

        # 필드에서 현재 턴의 출입구 위치(던전입구 좌표값) 확인 가능
        elif str_skill_name == 'map_find':
            if str_hp_or_mp_or_map == 'map':
                if self.bool_meet_monster or self.bool_meet_gard:
                    x = self.rand_maze_door_x
                    y = self.rand_maze_door_y
                else:
                    x = self.int_next_entrance_x
                    y = self.int_next_entrance_y
                self.battle_dialog.append(f"[백법사]의 던전입구 좌표값을 얻었다!")
                self.battle_dialog.append(f"던전입구 좌표 -> x:{x} y:{y}")
                self.battle_dialog.append(f"스킬 사용으로 [백법사]의 MP{minus_mp}소진")
                self.dict_user_gard['wizard_white']['mp'] -= minus_mp
                self.stackedWidget.setCurrentIndex(0)

    # 유저 수호대의 스킬 사용 후 몬스터 턴
    def monster_turn(self):
        if self.bool_meet_monster or self.bool_meet_enemy_monster:
            QTimer.singleShot(2000, self.monster_atk)
        elif self.bool_meet_gard or self.bool_meet_maze_gard:
            QTimer.singleShot(2000, self.enemy_gard_atk)
        elif self.bool_meet_boss_monster:
            QTimer.singleShot(2000, self.boss_gard_atk)

    # -------------스킬 구간----------------------------------------------------------------------------#

    # 전투화면으로 전환시 각 캐릭터의 [장비]버튼 setDisabled처리
    def equip_btn_disabled(self):
        for i in range(6):
            list_job_btn = self.list_frame[i].findChildren(QPushButton)[1].setDisabled(True)

    # 위치가 바뀌면서 모션 수행
    def move_image_forward(self, x, index):
        self.index = index
        self.current_pos = self.list_job_lb[self.index].pos()
        print(self.current_pos)
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            self.list_job_lb[self.index].setPixmap(QPixmap(f'../{self.list_job[self.index]}/attack1.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y() - 200)
            QTimer.singleShot(500, self.move_image_forward2)
            # self.timer.stop()
        return self.index

    def move_image_forward2(self):
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.
            self.list_job_lb[self.index].setPixmap(QPixmap(f'../{self.list_job[self.index]}/attack2.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y() - 300)
            QTimer.singleShot(500, self.move_image_back)
            # self.timer.stop()
        return self.index

    def move_image_back(self):
        if self.current_pos.x() < 900:  # 원래 위치로 돌아가는 x 좌표
            self.list_job_lb[self.index].setPixmap(QPixmap(f'../{self.list_job[self.index]}/walk1.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y())
            self.timer.stop()

    # 각 캐릭터의 [도망]버튼 클릭시 battle_dialog에 메세지를 띄운다. 확률에 따른 도망 성공/실패 -> 반환값(필드/전투화면)으로넘기기
    def user_gard_run(self):
        num = random.choice(range(1, 101))
        sucess_rate = list(range(0, 31))
        sucess_rate_num = random.choice(sucess_rate)
        if sucess_rate_num < num:
            self.battle_dialog.append(f"{100 - sucess_rate_num}%확률로 도망에 실패했습니다.전투화면이 유지됩니다.")
            bool_run_mode = False
        elif sucess_rate_num >= num:
            if self.bool_meet_gard or self.bool_meet_monster:
                back_to_loc = '필드'
            elif self.bool_meet_maze_gard or self.bool_meet_enemy_monster or self.bool_meet_boss_monster:
                back_to_loc = '던전'
            self.battle_dialog.append(f"{sucess_rate_num}%확률로 도망에 성공했습니다. {back_to_loc}화면으로 돌아갑니다.")
            bool_run_mode = True
        return bool_run_mode

    # -------------수호대와의 전투-------------------------------------------------------------------------------------------#
    # [필드/던전]타수호대 조우 - 전투가능한 구성원의 [공격][스킬]버튼이 활성화
    def battle_gard(self):

        # 따로 함수로 빼서 호출할까...
        for i in range(6):
            if self.list_job[i] in self.dict_user_gard.keys():
                if self.dict_user_gard[self.list_job[i]]['survival'] == True:
                    self.int_survival = i + 1
                    self.list_attack_btn[i].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                if self.dict_user_gard[self.list_job[i]]['survival'] == False:
                    self.list_attack_btn[i].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setDisabled(True)

                if self.bool_meet_gard:
                    self.battle_dialog.setText(
                        f"{self.dict_enemy_gard['gard']}와의 전투 시작!")
                    for k in range(6):
                        self.list_enemy_line[k].setText(f"{self.list_job[k]} HP: {self.dict_enemy_gard[self.list_job[k]]['hp']}")
                        pixmap = QPixmap(f'../{self.list_job[k]}/reverse.png')
                        pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                        icon = QIcon()
                        icon.addPixmap(pixmap)
                        self.list_enemy_btn[k].setIcon(icon)
                        self.list_enemy_btn[k].setIconSize(QSize(100, 100))

                elif self.bool_meet_maze_gard:
                    self.battle_dialog.setText(f"{self.int_floor}층에서 벌어진 {self.dict_enemy_gard['gard']}와의 수호대와의 전투 시작!")
                    for j in range(6):
                        self.list_enemy_line[j].setText(
                            f"{self.list_job[j]} HP: {self.dict_enemy_gard[self.list_job[j]]['hp']}")
                        pixmap = QPixmap(f'../{self.list_job[j]}/reverse.png')
                        pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                        icon = QIcon()
                        icon.addPixmap(pixmap)
                        self.list_enemy_btn[j].setIcon(icon)
                        self.list_enemy_btn[j].setIconSize(QSize(100, 100))

    # 각 캐릭터의 [공격]버튼에 따른 누가/누구에게/nnn데미지 입었습니다. battle_dialog 메세지띄우기
    def gard_atk_choice(self, x, index):

        damage = self.selected_option
        self.battle_dialog.append(f"수호대{self.name}을/를 공격해 {damage}데미지를 입혔다.")
        if self.bool_meet_gard or self.bool_meet_maze_gard:
            self.dict_enemy_gard[self.list_job[index]]['hp'] = self.dict_enemy_gard[self.list_job[index]]['hp'] - damage
            self.list_enemy_line[index].setText(
                f"{self.list_job[index]} HP:{self.dict_enemy_gard[self.list_job[index]]['hp']}")
            if self.dict_enemy_gard[self.list_job[index]]['hp'] <= 0:
                self.dict_enemy_gard[self.list_job[index]]['hp'] = 0
                self.list_enemy_line[index].setText(f"{self.list_job[index]} HP: 0")
                self.list_enemy_btn[index].setDisabled(True)

        QTimer.singleShot(2000, self.enemy_gard_atk)

    # 타수호대의 유저 수호대 랜덤공격 : (일반공격/스킬/아이템사용)
    def enemy_gard_atk(self):
        list_job = ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white']
        # use
        # 일반/스킬/아이템 중 선택
        int_enemy_choice_act = random.randint(1, 3)
        # 필드에서 적수호대 만남
        if self.bool_meet_gard:
            # 필드에서 일반공격
            if int_enemy_choice_act == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(list_job)
                print('필드 일반공격 공격자', str_choice_enemy_gard)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                print('필드 일반공격 피해자', str_choice_user_gard)
                # 유저수호대 피해자 공격받아 hp감소(공격력 증가시키는 버프 사용 고려)
                if self.use_hp_up:  # 백법사 hp_up버프
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * (1 + random.randint(5, 7) / 10)
                    print(self.dict_user_gard[str_choice_user_gard]['hp'])
                    print(self.dict_enemy_gard[str_choice_enemy_gard]['power'])
                    print(1 + random.randint(5, 7) / 10)
                    print('백법사의 hp_up 버프마법 사용함')
                    self.use_hp_up = False
                elif self.use_fire_wall:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * 1.5
                    print('fire_wall버프 발동')
                    self.use_fire_wall = False
                elif self.use_thunder_breaker:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * 1.6
                    print('thunder_breaker 버프 발동')
                    self.use_thunder_breaker = False
                else:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                        'power']
                    print('bilzzard 버프발동')
                    self.use_bilzzard = False


            # 필드에서 스킬사용(궁수, 검사, 마법사들만 가능)-필드 적수호대 레벨 15~20
            elif int_enemy_choice_act == 2:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(
                    ['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                print('필드 스킬 공격자', str_choice_enemy_gard)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                print('필드 스킬 피해자', str_choice_user_gard)
                # 적수호대 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    # 적수호대 궁수 레벨이 20미만인 경우 사용 가능한 스킬
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([10, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'target_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                * (1 + random.randint(2, 5) / 10)
                            print("필드 아처 타겟샷 발동")
                        elif str_enemy_skill == 'dual_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                * (1 + random.randint(4, 6) / 10)
                            print('필드 궁수 20레벨 미만 사용한 스킬', str_enemy_skill)
                    else:  # 적수호대 궁수 레벨이 20인 경우 가능한 스킬
                        skill_num = random.choice([10, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'target_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                * (1 + random.randint(2, 5) / 10)
                            print("필드 레벨 20 경우 아처 타겟샷 발동")
                        elif str_enemy_skill == 'dual_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                * (1 + random.randint(4, 6) / 10)
                            print("필드 레벨 20 경우 아처 듀얼샷 발동")
                        else:
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                * (1 + random.randint(5, 7) / 10)
                            print('필드 궁수 20레벨 이상 사용한 스킬', str_enemy_skill)

                # 적수호대 검사 필드에서 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * random.randint(2, 50)
                    print('필드 검사 스킬 사용')
                # 적수호대 흑법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_black':
                    # 적수호대 흑법사 레벨 20 미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([1, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard][
                                    'power'] * 1.3
                            print("필드 20미만 흑법사 파이어볼 발사")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print('필드 흑법사 20레벨 미만 스킬 사용', str_enemy_skill)
                    # 적수호대 흑법사 레벨 20이상
                    else:
                        skill_num = random.choice([1, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard][
                                    'power'] * 1.3
                            print("적수호대 흑법사 레벨 20 이상 필드 파이어볼 발사")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("필드 흑법사 20레벨 이상 파이어 월 스킬사용", self.use_fire_wall)
                        else:
                            self.use_thunder_breaker = True
                            print('필드 흑법사 20레벨 이상 썬더 브레이커 사용', self.use_thunder_breaker)

                # 적수호대 백법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                      self.dict_enemy_gard[str_heal_enemy][
                                                                          'max_hp'] / 10
                        print("적수호대 백법사 필드 힐 노말 스킬 사용")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("적수호대 백법사 필드 에이치업 스킬사용", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                      self.dict_enemy_gard[str_heal_enemy][
                                                                          'max_hp'] / 10
                        print('필드 백법사 힐 그레이터 스킬사용', str_enemy_skill)
                # 적수호대 적법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    # 적법사 레벨 20미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([1, 15])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("적법사 필드 20미만 힐 노말 스킬사용")
                            else:  # fire_ball 사용
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard][
                                        'power'] * 1.3
                                print("적법사 필드 20미만 파이어 볼 스킬사용")
                        # 적법사 15레벨부터 사용 가능한 스킬
                        else:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("적법사 필드 힐그레이터 스킬 사용")
                            else:  # fire_wall 광역스킬 사용
                                self.use_fire_wall = True
                                print('필드 적법사 20레벨 미만 스킬 사용', self.use_fire_wall)
                    else:  # 필드 적법사 레벨 20 이상
                        skill_num = random.choice([1, 15, 20])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print('필드 적법사 힐노말 사용')
                            else:  # fire_ball 사용
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.3
                                print('필드 적법사 파이어월 사용')
                        # 적법사 15레벨부터 사용 가능한 스킬
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print('필드 적법사 20레벨 이상 스킬사용', str_enemy_skill)
                            else:  # fire_wall 광역스킬 사용
                                self.use_fire_wall = True
                                print('필드 적법사 20레벨 이상 파이어월 사용', self.use_fire_wall)

                        else:
                            self.use_thunder_breaker = True
                            print('필드 적법사 20레벨 이상 썬더브레이커 스킬사용', self.use_thunder_breaker)

            #  필드에서 아이템 사용
            else:
                # 적수호대 공격자(아이템 사용자) 선택
                str_choice_enemy_gard = random.choice(list_job)
                list_enemy_items = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                    'all_potion_high', 'all_potion_middle', 'all_potion_low']
                # 적수호대 사용할 아이템 선택
                str_enemy_use_item = random.choice(list_enemy_items)
                # HP포션 사용
                if str_enemy_use_item == 'hp_potion_high':
                    print("필드 HP(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.7
                elif str_enemy_use_item == 'hp_potion_middle':
                    print("필드 HP(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.5
                elif str_enemy_use_item == 'hp_potion_low':
                    print("필드 HP(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.3

                # MP포션 사용
                elif str_enemy_use_item == 'mp_potion_high':
                    print("필드 MP(상) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['mp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'mp_potion_middle':
                    print("필드 MP(중) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'mp_potion_low':
                    print("필드 MP(하) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

                # ALL포션 사용
                elif str_enemy_use_item == 'all_potion_high':
                    print("필드 ALL(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.7
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'all_potion_middle':
                    print("필드 ALL(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.5
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'all_potion_low':
                    print("필드 ALL(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.3
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

        # 던전에서 적군수호대 조우
        if self.bool_meet_maze_gard:
            # 일반공격
            if int_enemy_choice_act == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(list_job)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 유저수호대 피해자 공격받아 hp감소
                if self.use_hp_up:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * (
                                                                               1 + random.randint(5, 7) / 10)
                    print(self.dict_user_gard[str_choice_user_gard]['hp'])
                    print(self.dict_enemy_gard[str_choice_enemy_gard]['power'])
                    print(1 + random.randint(5, 7) / 10)
                    print('던전1층 백법사의 hp_up 버프마법 사용함')
                    self.use_hp_up = False
                elif self.use_fire_wall:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * 1.5
                    print("던전1층 파이어월 발동")
                    self.use_fire_wall = False
                elif self.use_thunder_breaker:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * 1.6
                    print("던전1층 썬더브레이커 발동")
                    self.use_thunder_breaker = False
                elif self.use_bilzzard:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * 1.7
                    print("던전1층 블리자드 발동")
                    self.use_bilzzard = False
                else:  # 버프없음
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                        'power']
                    print("던전1층 총공격")
            # 1층 : 적군 수호대 레벨 20~25
            elif int_enemy_choice_act == 2 and self.int_floor == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(
                    ['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 던전 1층에서 궁수 스킬사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(2, 5) / 10)
                        print("던전1층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(4, 6) / 10)
                        print("던전1층 아처 듀얼샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(5, 7) / 10)
                        print("던전1층 아처 마스터샷 발동")
                # 던전 1층에서 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * random.randint(2, 50)
                    print("던전1층 수아드맨 스킬 사용")
                # 던전 1층에서 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    # 흑법사 레벨 25미만인 경우
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 25:
                        skill_num = random.choice([1, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard][
                                    'power'] * 1.3
                            print("던전1층 흑법사 파이어볼 발동")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("던전1층 흑법사 파이어 월 발동", self.use_fire_wall)
                        else:
                            self.use_thunder_breaker = True
                            print("던전1층 흑법사 썬더 브레이커 스킬 발동", self.use_thunder_breaker)
                    # 흑법사 레벨 25이상이 경우
                    else:
                        skill_num = random.choice([1, 15, 20, 25])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard][
                                    'power'] * 1.3
                            print("던전1층 흑법사 레벨 25 이상 파이어볼 발동")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("던전1층 흑법사 레벨 25이상 파이어 월 발동", self.use_fire_wall)
                        elif str_enemy_skill == 'thunder_breaker':
                            self.use_thunder_breaker = True
                            print("던전1층 흑법사 레벨 25이상 썬더 브레이커 발동", self.use_thunder_breaker)
                        else:
                            self.use_bilzzard = True
                            print("던전1층 흑법사 레벨 25이상 블리자드 발동", self.use_bilzzard)
                # 던전1층 백법사 스킬사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    # 적수호대 힐 대상
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                          'max_hp'] * random.randint(
                            3, 7) / 10
                        print("던전1층 백법사 힐 노말 스킬 발동")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("던전1층 백법사 에이치업 스킬 발동", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                          'max_hp'] * random.randint(
                            6, 10) / 10
                        print("던전1층 백법사 힐그레이터 스킬 발동")
                # 던전1층 적법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    # 적법사 레벨 25미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 25:
                        skill_num = random.choice([1, 15, 20])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] \
                                                                              * random.randint(3, 7) / 10
                                print("던전1층 적법사 레벨 25미만 힐 노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard][
                                        'power'] * 1.3
                                print("던전1층 적법사 레벨 25미만 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] \
                                                                              * random.randint(6, 10) / 10
                                print("던전1층 적법사 레벨 25 미만 힐 그레이터 발동")
                            else:  # fire_wall인 경우
                                self.use_fire_wall = True
                                print("던전1층 적법사 레벨 25 미만 파이어 월 발동", self.use_fire_wall)
                        # skill_num == 20
                        else:
                            self.use_thunder_breaker = True
                            print("던전1층 적법사 레벨 25 미만 썬더 브레이커 발동", self.use_thunder_breaker)

                    else:  # 25레벨
                        skill_num = random.choice([1, 15, 20, 25])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] \
                                                                              * random.randint(3, 7) / 10
                                print("던전1층 적법사 레벨 25일때 힐노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard][
                                        'power'] * 1.3
                                print("던전1층 적법사 레벨 25일때 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] \
                                                                              * random.randint(6, 10) / 10
                                print("던전1층 적법사 레벨 25일때 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전1층 적법사 레벨 25일때 파이어 월 발동", self.use_fire_wall)
                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전1층 적법사 레벨 25일때 썬더 브레이커 발동", self.use_thunder_breaker)
                        else:  # 25인 경우
                            self.use_bilzzard = True
                            print("던전1층 적법사 레벨 25일때 블리자드 발동", self.use_bilzzard)

            # 2층 적수호대 : 26~30레벨
            elif int_enemy_choice_act == 2 and self.int_floor == 2:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(
                    ['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(2, 5) / 10)
                        print("던전2층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(4, 6) / 10)
                        print("던전2층 아처 듀얼 샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(5, 7) / 10)
                        print("던전2층 아처 마스터샷 발동")
                # 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * random.randint(2, 50)
                    print("던전2층 수아드맨 스킬 발동")
                # 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    skill_num = random.choice([1, 15, 20, 25])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'fire_ball':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] * 1.3
                        print("던전2층 흑법사 파이어볼 발동")
                    elif str_enemy_skill == 'fire_wall':
                        self.use_fire_wall = True
                        print("던전2층 흑법사 파이어 월 발동", self.use_fire_wall)
                    elif str_enemy_skill == 'thunder_breaker':
                        self.use_thunder_breaker = True
                        print("던전2층 흑법사 썬더 브레이커 발동", self.use_thunder_breaker)
                    else:
                        self.use_bilzzard = True
                        print("던전2층 흑법사 블리자드 발동", self.use_bilzzard)

                # 백법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_white':
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 30:
                        skill_num = random.choice([1, 10, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        str_heal_enemy = random.choice(
                            ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                          * random.randint(3, 7) / 10
                            print("던전2층 백법사 레벨 30미만 힐 노말 발동")
                        elif str_enemy_skill == 'hp_up':
                            self.use_hp_up = True
                            print("던전2층 백법사 레벨 30미만 에이치피 업 발동", self.use_hp_up)
                        elif str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                          * random.randint(6, 10) / 10
                            print("던전2층 백법사 레벨 30미만 힐 그레이터 발동")
                    else:
                        skill_num = random.choice([1, 10, 15, 30])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        str_heal_enemy = random.choice(
                            ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                          * random.randint(3, 7) / 10
                            print("던전2층 백법사 레벨 30일때 힐 노말 발동")
                        elif str_enemy_skill == 'hp_up':
                            self.use_hp_up = True
                            print("던전2층 백법사 레벨 30일때 에이치피 업 발동", self.use_hp_up)
                        elif str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                          self.dict_enemy_gard[str_heal_enemy][
                                                                              'max_hp'] / 10
                            print("던전2층 백법사 레벨 30일때 힐 그레이터 발동")
                        else:  # heal_all 사용
                            ratio = random.randint(4, 8) / 10
                            for i in list_job:
                                self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                            print("던전2층 백법사 레벨 30일때 힐 올 사용")

                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 30:
                        skill_num = random.choice([1, 15, 20, 25])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("던전2층 레벨 30미만 적법사 힐노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard][
                                        'power'] * 1.3
                                print("던전2층 레벨 30미만 적법사 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("던전2층 적법사 레벨 30미만 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전2층 적법사 레벨 30미만 파이어 볼 발동", self.use_fire_wall)

                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전2층 적법사 레벨 30미만 썬더브레이커 발동", self.use_thunder_breaker)

                        else:  # 25인 경우
                            self.use_bilzzard = True
                            print("던전2층 적법사 레벨 30미만 블리자드 발동", self.use_bilzzard)

                    else:  # 레벨 30일때
                        skill_num = random.choice([1, 15, 20, 25, 30])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("던전2층 레벨 30 이상 적법사 힐 노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                    self.dict_enemy_gard[str_choice_enemy_gard][
                                        'power'] * 1.3
                                print("던전2층 레벨 30이상 적법사 파이어볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print("던전2층 적법사 레벨 30이상 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전2층 적법사 레벨 30이상 파이어 월 발동", self.use_fire_wall)

                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전2층 적법사 레벨 30이상 썬더 브레이커 발동", self.use_thunder_breaker)

                        elif skill_num == 25:
                            self.use_bilzzard = True
                            print("던전2층 적법사 레벨 30이상 블리자드 발동", self.use_bilzzard)
                        else:  # 레벨 30
                            ratio = random.randint(4, 8) / 10
                            for i in list_job:
                                self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                            print("던전2층 적법사 레벨 30이상 힐올 발동")

            # 3층 이상(30이상)
            elif int_enemy_choice_act == 2 and self.int_floor >= 3:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(
                    ['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(2, 5) / 10)
                        print("던전3층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(4, 6) / 10)
                        print("던전3층 아처 듀얼샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] \
                                                                           * (1 + random.randint(5, 7) / 10)
                        print("던전3층 마스터샷 발동")
                # 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                           'power'] * random.randint(2, 50)
                    print("던전3층 검사 스킬 발동")
                # 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    skill_num = random.choice([1, 15, 20, 25])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'fire_ball':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                               'power'] * 1.3
                        print("던전3층 흑법사 파이어볼 발동")
                    elif str_enemy_skill == 'fire_wall':
                        self.use_fire_wall = True
                        print("던전3층 흑법사 파이어 월 발동", self.use_fire_wall)
                    elif str_enemy_skill == 'thunder_breaker':
                        self.use_thunder_breaker = True
                        print("던전3층 흑법사 썬더 브레이커 발동", self.use_thunder_breaker)
                    else:
                        self.use_bilzzard = True
                        print("던전3층 흑법사 블리자드 발동", self.use_bilzzard)

                # 백법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15, 30])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                      * random.randint(3, 7) / 10
                        print("던전3층 백법사 힐 노말 발동")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("던전3층 백법사 에이치피 업 발동", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                      * random.randint(6, 10) / 10
                        print("던전3층 백법사 힐 그레이터 발동")
                    else:  # heal_all 사용
                        ratio = random.randint(4, 8) / 10
                        for i in list_job:
                            self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                        print("던전3층 백법사 힐 올 발동")

                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(['warrior', 'archer', 'swordman', 'wizard_red',
                                                    'wizard_black', 'wizard_white'])
                    skill_num = random.choice([1, 15, 20, 25, 30])
                    if skill_num == 1:
                        str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                          * random.randint(3, 7) / 10
                            print("던전3층 적법사 힐 노말 발동")
                        else:
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard][
                                    'power'] * 1.3
                            print("던전3층 적법사 파이어 볼 발동")
                    elif skill_num == 15:
                        str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                        if str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                          self.dict_enemy_gard[str_heal_enemy][
                                                                              'max_hp'] / 10
                            print("던전3층 적법사 힐 그레이터 발동")
                        else:
                            self.use_fire_wall = True
                            print("던전3층 적법사 파이어 월 발동", self.use_fire_wall)
                    elif skill_num == 20:
                        self.use_thunder_breaker = True
                        print("던전3층 적법사 선더 브레이커 발동", self.use_thunder_breaker)
                    elif skill_num == 25:
                        self.use_bilzzard = True
                        print("던전3층 적법사 블리자드 발동", self.use_bilzzard)
                    else:  # 레벨 30
                        ratio = random.randint(4, 8) / 10
                        for i in list_job:
                            self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                        print("던전3층 적법사 힐 올 발동")

            # 아이템 사용
            else:
                # 적수호대 공격자(아이템 사용자) 선택
                str_choice_enemy_gard = random.choice(list_job)
                list_enemy_items = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                    'all_potion_high', 'all_potion_middle', 'all_potion_low']
                str_enemy_use_item = random.choice(list_enemy_items)
                if str_enemy_use_item == 'hp_potion_high':
                    print("던전 HP(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.7
                elif str_enemy_use_item == 'hp_potion_middle':
                    print("던전 HP(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.5
                elif str_enemy_use_item == 'hp_potion_low':
                    print("던전 HP(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.3

                # MP포션 사용
                elif str_enemy_use_item == 'mp_potion_high':
                    print("던전 MP(상) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['mp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.7
                elif str_enemy_use_item == 'mp_potion_middle':
                    print("던전 MP(중) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.5
                elif str_enemy_use_item == 'mp_potion_low':
                    print("던전 MP(하) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.3
                # ALL포션 사용
                elif str_enemy_use_item == 'all_potion_high':
                    print("던전 ALL(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.7
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.7

                elif str_enemy_use_item == 'all_potion_middle':
                    print("던전 ALL(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.5
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.5

                elif str_enemy_use_item == 'all_potion_low':
                    print("던전 ALL(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard][
                                                                             'max_hp'] * 0.3
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.3

    # -------------몬스터와의 전투-------------------------------------------------------------------------------------------#
    # [필드/던전]몬스터 조우 - 전투가능한 구성원의 [공격][스킬]버튼이 활성화
    def battle_monster(self):
        for i in range(6):
            if self.list_job[i] in self.dict_user_gard.keys():
                if self.dict_user_gard[self.list_job[i]]['survival']:
                    self.int_survival = i + 1
                    self.list_attack_btn[i].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                if not self.dict_user_gard[self.list_job[i]]['survival']:
                    self.list_attack_btn[i].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setDisabled(True)
                    self.list_job_lb[i].setPixmap(QPixmap(f'../{self.list_job[i]}/died.png'))

    def monster_creat(self):
        if self.bool_meet_monster:
            # self.monster_li.clear()  #디버깅1)수호대가 죽을 때마다 monster_li.clear()해줌으로써 몬스터의 이미지가 변경되고 있음.
            area = self.dict_field_monster['area'].split('_')
            self.battle_dialog.setText(f"{area[1]}지역에서 벌어진 전투 시작!")
            for k in range(self.dict_field_monster['info']['int_cnt']):
                self.list_enemy_line[k].setText(f"몬스터 HP: {str(self.dict_field_monster['info']['hp'][k])}")
                if self.dict_field_monster['area'] == 'area_fire':
                    if self.dict_field_monster['info']['hp'][k] <= 250:
                        self.monster_li.append('small_dragon[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 300:
                        self.monster_li.append('small_dragon[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 400:
                        self.monster_li.append('small_dragon[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 500:
                        self.monster_li.append('small_dragon[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 600:
                        self.monster_li.append('small_dragon[5]')
                    elif self.dict_field_monster['info']['hp'][k] <= 700:
                        self.monster_li.append('demon[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 800:
                        self.monster_li.append('demon[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 900:
                        self.monster_li.append('demon[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 950:
                        self.monster_li.append('demon[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 1000:
                        self.monster_li.append('demon[5]')
                elif self.dict_field_monster['area'] == 'area_water':
                    if self.dict_field_monster['info']['hp'][k] <= 250:
                        self.monster_li.append('dragon[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 300:
                        self.monster_li.append('dragon[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 400:
                        self.monster_li.append('dragon[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 500:
                        self.monster_li.append('dragon[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 600:
                        self.monster_li.append('dragon[5]')
                    elif self.dict_field_monster['info']['hp'][k] <= 700:
                        self.monster_li.append('jinn[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 800:
                        self.monster_li.append('jinn[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 900:
                        self.monster_li.append('jinn[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 950:
                        self.monster_li.append('jinn[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 1000:
                        self.monster_li.append('jinn[5]')
                elif self.dict_field_monster['area'] == 'area_forest':
                    if self.dict_field_monster['info']['hp'][k] <= 250:
                        self.monster_li.append('lizard[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 300:
                        self.monster_li.append('lizard[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 400:
                        self.monster_li.append('lizard[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 500:
                        self.monster_li.append('lizard[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 600:
                        self.monster_li.append('lizard[5]')
                    elif self.dict_field_monster['info']['hp'][k] <= 700:
                        self.monster_li.append('medusa[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 800:
                        self.monster_li.append('medusa[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 900:
                        self.monster_li.append('medusa[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 950:
                        self.monster_li.append('medusa[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 1000:
                        self.monster_li.append('medusa[5]')
                elif self.dict_field_monster['area'] == 'area_snow':
                    if self.dict_field_monster['info']['hp'][k] <= 250:
                        self.monster_li.append('snow[1]')
                    elif self.dict_field_monster['info']['hp'][k] <= 300:
                        self.monster_li.append('snow[2]')
                    elif self.dict_field_monster['info']['hp'][k] <= 400:
                        self.monster_li.append('snow[3]')
                    elif self.dict_field_monster['info']['hp'][k] <= 500:
                        self.monster_li.append('snow[4]')
                    elif self.dict_field_monster['info']['hp'][k] <= 600:
                        self.monster_li.append('snow[5]')
                    elif self.dict_field_monster['info']['hp'][k] <= 700:
                        self.monster_li.append('snow[6]')
                    elif self.dict_field_monster['info']['hp'][k] <= 800:
                        self.monster_li.append('snow[7]')
                    elif self.dict_field_monster['info']['hp'][k] <= 900:
                        self.monster_li.append('snow[8]')
                    elif self.dict_field_monster['info']['hp'][k] <= 950:
                        self.monster_li.append('snow[9]')
                    elif self.dict_field_monster['info']['hp'][k] <= 1000:
                        self.monster_li.append('snow[10]')

                self.battle_dialog.append(
                    f"HP: {str(self.dict_field_monster['info']['hp'][k])}의 {self.monster_li[k]}를 만났다!")
                pixmap = QPixmap(f'../data/{self.dict_field_monster["area"]}/{self.monster_li[k]}.png')
                pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                icon = QIcon()
                icon.addPixmap(pixmap)
                self.list_enemy_btn[k].setIcon(icon)
                self.list_enemy_btn[k].setIconSize(QSize(100, 100))

        elif self.bool_meet_enemy_monster:
            # self.monster_li.clear()
            self.battle_dialog.setText(f"{self.int_floor}층에서 벌어진 전투 시작!")
            for j in range(self.dict_maze_monster['int_cnt']):
                self.list_enemy_line[j].setText(f"몬스터 HP: {self.dict_maze_monster['list_hp'][j]}")
                if self.dict_maze_monster['list_hp'][j] <= 250:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('small_dragon[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('dragon[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('lizard[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[1]')
                elif self.dict_maze_monster['list_hp'][j] <= 300:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('small_dragon[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('dragon[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('lizard[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[2]')
                elif self.dict_maze_monster['list_hp'][j] <= 400:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('small_dragon[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('dragon[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('lizard[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[3]')
                elif self.dict_maze_monster['list_hp'][j] <= 500:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('small_dragon[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('dragon[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('lizard[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[4]')
                elif self.dict_maze_monster['list_hp'][j] <= 600:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('small_dragon[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('dragon[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('lizard[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[5]')
                elif self.dict_maze_monster['list_hp'][j] <= 700:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('demon[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('jinn[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('medusa[1]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[6]')
                elif self.dict_maze_monster['list_hp'][j] <= 800:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('demon[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('jinn[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('medusa[2]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[7]')
                elif self.dict_maze_monster['list_hp'][j] <= 900:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('demon[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('jinn[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('medusa[3]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[8]')
                elif self.dict_maze_monster['list_hp'][j] <= 950:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('demon[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('jinn[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('medusa[4]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[9]')
                elif self.dict_maze_monster['list_hp'][j] <= 1000:
                    if self.dict_maze_monster['list_area_monster'][j] == 'area_fire':
                        self.monster_li.append('demon[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_water':
                        self.monster_li.append('jinn[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_forest':
                        self.monster_li.append('medusa[5]')
                    elif self.dict_maze_monster['list_area_monster'][j] == 'area_snow':
                        self.monster_li.append('snow[10]')

                self.battle_dialog.append(f"HP: {self.dict_maze_monster['list_hp'][j]}의 {self.monster_li[j]}를 만났다!")
                pixmap = QPixmap(
                    f'../data/{self.dict_maze_monster["list_area_monster"][j]}/{self.monster_li[j]}.png')
                pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                icon = QIcon()
                icon.addPixmap(pixmap)
                self.list_enemy_btn[j].setIcon(icon)
                self.list_enemy_btn[j].setIconSize(QSize(100, 100))

    # 각 캐릭터의 [공격]버튼 수행
    def monster_atk_choice(self, x, index, btn):
        print(btn.objectName())
        if btn.objectName() in ['pb_atk_warrior', 'pb_atk_archer', 'pb_atk_swordman',
                                'pb_atk_wizard_red', 'pb_atk_wizard_black', 'pb_atk_wizard_white']:
            damage = self.selected_option
            print(f"공격데미지 : {damage}")

            # 오류#예상부분 : 죽은몬스터를 self.monster_li에서 제거하는 순간 index오류 발생할 가능성 농후
            self.battle_dialog.append(f"{self.name}이/가{self.monster_li[index]}을/를 공격해 {damage}데미지를 입혔다.")
            if self.bool_meet_monster:
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster['info']['hp'][index] - damage}")
                self.dict_field_monster['info']['hp'][index] = self.dict_field_monster['info']['hp'][index] - damage
                print(f"선택몬스터의 맞기전 hp:{self.dict_field_monster['info']['hp'][index]}")
                print(f"hp-데미지:{self.dict_field_monster['info']['hp'][index] - damage}")
                if self.dict_field_monster['info']['hp'][index] <= 0:
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            elif self.bool_meet_enemy_monster:
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index] - damage}")
                if self.dict_maze_monster['list_hp'][index] <= 0:
                    self.list_enemy_line[index].setText(f"몬스터 HP: 0")
                    self.list_enemy_btn[index].setDisabled(True)

            QTimer.singleShot(2000, self.monster_atk)

    # 몬스터의 유저 수호대 (랜덤)공격
    def monster_atk(self):

        list_target = []
        for k in self.list_job:
            if self.dict_user_gard[k]['survival']:
                list_target.append(k)
        int_monster_skill_c = random.randint(0, 1)
        int_monster_target_c = random.randint(0, len(list_target) - 1)
        int_skill_sucess = random.randint(0, 100)

        if int_monster_skill_c == 0:
            damage_key = 'attack'
        elif int_monster_skill_c == 1:
            damage_key = 'skill'

        # print(damage_key)
        damage_name = self.dict_field_monster['info'][damage_key][0]
        damage_num = self.dict_field_monster['info'][damage_key][1]

        # 필드에서 지역몬스터를 만났다.
        if self.bool_meet_monster:
            # 죽은 몬스터는 공격를 하지 못한다.
            atk_monster = random.randint(0, len(self.monster_li) - 1)
            for i in range(self.dict_field_monster['info']['int_cnt']):
                print(atk_monster)
                if self.dict_field_monster['info']['hp'][atk_monster] > 0:
                    print(self.monster_li[atk_monster])
                    self.atk_mon = self.monster_li[atk_monster]

            origin_hp = self.dict_user_gard[list_target[int_monster_target_c]]['hp']
            atk_monster_damage = abs(self.dict_field_monster['info']['hp'][atk_monster] * damage_num)

            if damage_key == 'attack':
                # 출력 메세지
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = origin_hp - atk_monster_damage
                if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                self.battle_msg = f"""{self.dict_field_monster['area']}의 {self.atk_mon}가 {damage_name}공격을 걸었다!
                {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""
                print(
                    f"{list_target[int_monster_target_c]} 현 hp : {origin_hp}")
                print(f"받은 데미지 : {atk_monster_damage}")

            elif damage_key == 'skill':
                if int_skill_sucess <= 30:
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = origin_hp - atk_monster_damage
                    if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                        self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                    self.battle_msg = f"""{self.dict_field_monster['area']}의 {self.atk_mon}가 {damage_name}공격을 걸었다!
{list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""
                    print(
                        f"{list_target[int_monster_target_c]} 현 hp : {origin_hp}")
                    print(f"-받은 데미지 : {atk_monster_damage}")
                else:
                    # 출력 메세지
                    self.battle_msg = "몬스터의 스킬이 먹히지 않았습니다. 아무일도 일어나지 않았습니다."

            # 최종 출력 메세지
            self.battle_dialog.append(self.battle_msg)

            # 공격을 받은 유저수호대의 hp가 0이 되었을 때
            if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                self.dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! {list_target[int_monster_target_c]}가 전투불능상태가 되었습니다.")
                QTimer.singleShot(1000, self.battle_monster)
                self.show_war_result()

        # 던전에서 지역몬스터를 만났다.
        elif self.bool_meet_enemy_monster:
            # 죽은 몬스터는 공격를 하지 못한다.
            atk_monster = random.randint(0, len(self.monster_li) - 1)
            for i in range(self.dict_maze_monster['int_cnt']):
                print(atk_monster)
                if self.dict_maze_monster['list_hp'][atk_monster] > 0:
                    print(self.monster_li[atk_monster])
                    self.atk_mon = self.monster_li[atk_monster]

            monster_damage = self.dict_maze_monster['list_damage'][atk_monster]
            str_damage_name = self.dict_maze_monster['list_area_monster'][atk_monster].split('_')
            if monster_damage == 0.05:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_maze_monster['list_hp'][atk_monster] * monster_damage
                str_damage_name = str_damage_name[1] + '_attack'
                if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                    # 출력 메세지
                self.battle_msg = f"""{self.dict_maze_monster['list_area_monster'][atk_monster]}의 {self.monster_li[atk_monster]}가 {str_damage_name}공격을 걸었다!
    그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""

            elif monster_damage == 0.1:
                if int_skill_sucess <= 30:
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_maze_monster['list_hp'][atk_monster] * monster_damage
                    str_damage_name = str_damage_name[1] + '_ball'
                    if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                        self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                    # 출력 메세지
                    self.battle_msg = f"""{self.dict_maze_monster['list_area_monster'][atk_monster]}의 {self.monster_li[atk_monster]}가 {str_damage_name}공격을 걸었다!
    그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""

                else:
                    # 출력 메세지
                    self.battle_msg = "몬스터의 스킬이 먹히지 않았습니다. 아무일도 일어나지 않았습니다."

            # 최종 출력 메세지
            self.battle_dialog.append(self.battle_msg)

            # 공격을 받은 유저수호대의 hp가 0이 되었을 때
            if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                self.dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! {list_target[int_monster_target_c]}가 전투불능상태가 되었습니다.")
                QTimer.singleShot(1000, self.battle_monster)

        self.show_war_result()

    # -------------보스몬스터와의 전투----------------------------------------------------------------------------------------#
    # 보스 몬스터 조우 - 전투 가능한 구성원의 [공격][스킬]버튼 활성화, 보스+일반몬스터 이미지 로드
    def battle_boss_monster(self):

        for i in range(6):
            if self.list_job[i] in self.dict_user_gard.keys():
                if self.dict_user_gard[self.list_job[i]]['survival'] == True:
                    self.int_survival = i + 1
                    self.list_attack_btn[i].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                if self.dict_user_gard[self.list_job[i]]['survival'] == False:
                    self.list_attack_btn[i].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                    self.list_frame[i].findChildren(QPushButton)[3].setDisabled(True)
                    self.list_job_lb[i].setPixmap(QPixmap(f'../{self.list_job[i]}/died.png'))

            if self.bool_meet_boss_monster:
                self.battle_dialog.setText(f"{self.int_floor}층에서 벌어진 {self.dict_boss_monster['name']}와의 전투 시작!")
                self.list_enemy_line[0].setText(f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp']}")
                for j in range(self.dict_boss_monster['list_field_monster'][0]):
                    self.list_enemy_line[j + 1].setText(
                        f"던전몬스터 HP: {self.dict_boss_monster['list_field_monster'][1][j]}")
                    if self.dict_boss_monster['list_field_monster'][1][j] <= 250:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('small_dragon[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('dragon[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('lizard[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[1]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 300:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('small_dragon[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('dragon[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('lizard[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[2]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 400:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('small_dragon[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('dragon[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('lizard[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[3]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 500:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('small_dragon[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('dragon[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('lizard[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[4]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 600:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('small_dragon[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('dragon[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('lizard[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[5]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 700:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('demon[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('jinn[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('medusa[1]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[6]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 800:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('demon[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('jinn[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('medusa[2]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[7]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 900:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('demon[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('jinn[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('medusa[3]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[8]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 950:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('demon[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('jinn[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('medusa[4]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[9]')
                    elif self.dict_boss_monster['list_field_monster'][1][j] <= 1000:
                        if self.dict_boss_monster['list_field_monster'][2][j] == 'area_fire':
                            self.monster_li.append('demon[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_water':
                            self.monster_li.append('jinn[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_forest':
                            self.monster_li.append('medusa[5]')
                        elif self.dict_boss_monster['list_field_monster'][2][j] == 'area_snow':
                            self.monster_li.append('snow[10]')
                    self.battle_dialog.append(
                        f"HP: {self.dict_boss_monster['list_field_monster'][1][j]}의 {self.monster_li[j]}를 만났다!")
                    pixmap = QPixmap(
                        f'../data/{self.dict_boss_monster["list_field_monster"][2][j]}/{self.monster_li[j]}.png')
                    pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                    icon = QIcon()
                    icon.addPixmap(pixmap)
                    self.list_enemy_btn[j + 1].setIcon(icon)
                    self.list_enemy_btn[j + 1].setIconSize(QSize(100, 100))

                for l in range(7):
                    if self.int_floor == l + 1:
                        self.movie = QMovie(f'../data/boss_monster/{l + 1}.gif', QByteArray(), self)
                        self.movie.frameChanged.connect(
                            lambda frame: self.enemy_0.setIcon(QIcon(self.movie.currentPixmap())))
                        if self.int_floor in [1, 5, 6, 7]:
                            self.enemy_0.setIconSize(QSize(180, 180))
                        else:
                            self.enemy_0.setIconSize(QSize(100, 100))
                        self.movie.start()

    # 각 직업의 [공격] + battle_dialog 메세지
    def boss_monster_atk_choice(self, x, index):

        if index == 0:
            atk_job, damage = self.name, self.selected_option
            self.battle_dialog.append(f"{atk_job}이/가 {self.dict_boss_monster['name']} 을/를 공격해 {damage}데미지를 입혔다.")
            self.hp_enemy_0.setText(f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp'] - damage}")
            if self.dict_boss_monster['hp'] <= 0:
                self.dict_boss_monster['hp'] = 0
                self.enemy_0.setText(f"{self.dict_boss_monster['name']} HP: {self.dict_boss_monster['hp']}")
                self.enemy_0.setDisabled(True)
        else:
            atk_job, damage = self.name, self.selected_option
            self.battle_dialog.append(f"{atk_job}이/가 {self.monster_li[index]} 을/를 공격해 {damage}데미지를 입혔다.")
            self.list_enemy_line[index].setText(
                f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1] - damage}")
            if self.dict_boss_monster['list_field_monster'][1][index - 1] <= 0:
                self.dict_boss_monster['list_field_monster'][1][index - 1] = 0
                self.list_enemy_line[index].setText(
                    f"던전몬스터 HP:{self.dict_boss_monster['list_field_monster'][1][index - 1]}")
                self.list_enemy_btn[index].setDisabled(True)

        QTimer.singleShot(2000, self.boss_monster_atk)

    # 보스몬스터/던전몬스터의 유저 수호대 (랜덤)공격
    def boss_monster_atk(self):

        list_target = []

        for i in self.list_job:
            if self.dict_user_gard[i]['survival'] == True:
                list_target.append(i)

        int_monster_skill_c = random.randint(0, 1)
        int_monster_target_c = random.randint(0, len(list_target) - 1)
        int_skill_suceess = random.randint(0, 100)
        atk_monster = random.randint(0, len(self.monster_li))

        # 보스몬스터 -> 유저수호대 공격
        if atk_monster == 0:
            if int_monster_skill_c == 0:
                damage = 'attack'
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_boss_monster['hp'] * 0.05
                self.battle_msg = f"""{self.dict_boss_monster['name']}가 {self.dict_boss_monster[damage][0]}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""
            elif int_monster_skill_c == 1:
                if int_skill_suceess <= 70:
                    # 광역효과 추가해야함
                    damage = 'skill'
                    for k in range(len(list_target) - 1):
                        self.dict_user_gard[list_target[k]]['hp'] -= self.dict_boss_monster['hp'] * 0.1
                    self.battle_msg = f"""{self.dict_boss_monster['name']}가 {self.dict_boss_monster[damage][1]}공격을 걸었다!
그 영향으로 수호대 모두의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!"""
                else:
                    self.battle_msg = "보스가 스킬을 쓰던 중 삐끗하여 아무일도 일어나지 않았습니다..보스가 민망해합니다."

            self.battle_dialog.append(self.battle_msg)

        # 던전몬스터 -> 유저수호대 공격
        else:
            for j in range(self.dict_boss_monster['list_field_monster'][0]):
                if int_monster_skill_c == 0:
                    monster_damage = 'attack'
                    area = self.dict_boss_monster['list_field_monster'][2][j][5:]
                    if area == 'water':
                        area = 'aqua'
                    elif area == 'forest':
                        area = 'air'
                    elif area == 'snow':
                        area = 'ice'
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= \
                        self.dict_boss_monster['list_field_monster'][1][j] * 0.05
                elif int_monster_skill_c == 1:
                    monster_damage = 'ball'
                    area = self.dict_boss_monster['list_field_monster'][2][j][5:]
                    if area == 'water':
                        area = 'aqua'
                    elif area == 'forest':
                        area = 'air'
                    self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= \
                        self.dict_boss_monster['list_field_monster'][1][j] * 0.1

            self.battle_dialog.append(
                f"""{self.dict_boss_monster['list_field_monster'][2][j]}의 {self.monster_li[j]}가 {area}{monster_damage}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!""")

        if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
            self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
            self.dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
            self.battle_dialog.append(f"앗! 우리의 {list_target[int_monster_target_c]}가 전투불능상태가 되었습니다.")
            QTimer.singleShot(1000, self.battle_monster)

        self.show_war_result()

    # -------------전투+아이템(사용/획득)-------------------------------------------------------------------------------------#
    # 필드에서 일반몬스터 만났을때 승리한 후 아이템 얻는 함수
    def field_battle_get_items(self, str_area):
        if self.bool_meet_monster and self.bool_war_result:
            int_mul = random.randint(1, 3)
            if self.dict_field_monster['area'] == 'area_fire':
                fire_cnt = self.dict_field_monster['area_fire']['int_cnt']
                list_fire_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                      'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                      'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                      'silver_helmet', 'bronze_armor', 'iron_shield', 'bronze_bow',
                                                      'red_glove', 'red_cape', 'bronze_pants'], k=fire_cnt * int_mul)
                return list_fire_drop_item
            elif self.dict_field_monster['area'] == 'area_water':
                water_cnt = self.dict_field_monster['area_water']['int_cnt']
                list_water_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                       'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                       'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                       'red_hood', 'bronze_shield', 'bronze_bow', 'red_glove',
                                                       'red_cape', 'red_pants'], k=water_cnt * int_mul)
                return list_water_drop_item
            elif self.dict_field_monster['area'] == 'area_forest':
                forest_cnt = self.dict_field_monster['area_forest']['int_cnt']
                list_forest_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                        'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                        'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                        'cow_helmet', 'cow_armor', 'leather_shield', 'stone_gem',
                                                        'bronze_wand', 'bronze_staff', 'cow_glove', 'cow_cape',
                                                        'cow_pants'], k=forest_cnt * int_mul)
                return list_forest_drop_item
            else:  # 'area_snow'인 경우
                snow_cnt = self.dict_field_monster['area_snow']['int_cnt']
                list_snow_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                      'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                      'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                      'silver_helmet', 'chain_armor', 'red_armor', 'chain_shield',
                                                      'bronze_sword', 'low_chain_glove', 'cow_cape', 'chain_pants'],
                                                     k=snow_cnt * int_mul)
                return list_snow_drop_item
        else:
            pass

    # 던전에서 일반몬스터 만났을때 승리한 후 아이템 얻는 함수
    def maze_battle_get_items(self, bool_meet_maze_monster):
        if (bool_meet_maze_monster == True) and (self.bool_war_result == True):
            int_mul = random.randint(1, 3)
            fire_cnt = self.dict_maze_monster['list_area_monster'].count('area_fire')
            list_fire_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                  'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                  'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                  'silver_helmet', 'bronze_armor', 'iron_shield', 'bronze_bow',
                                                  'red_glove', 'red_cape', 'bronze_pants'], k=fire_cnt * int_mul)
            water_cnt = self.dict_maze_monster['list_area_monster'].count('area_water')
            list_water_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                   'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                   'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                   'red_hood', 'bronze_shield', 'bronze_bow', 'red_glove',
                                                   'red_cape', 'red_pants'], k=water_cnt * int_mul)
            forest_cnt = self.dict_maze_monster['list_area_monster'].count('area_forest')
            list_forest_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                    'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                    'cow_helmet', 'cow_armor', 'leather_shield', 'stone_gem',
                                                    'bronze_wand', 'bronze_staff', 'cow_glove', 'cow_cape',
                                                    'cow_pants'], k=forest_cnt * int_mul)
            snow_cnt = self.dict_maze_monster['list_area_monster'].count('area_snow')
            list_snow_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                  'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                  'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                  'silver_helmet', 'chain_armor', 'red_armor', 'chain_shield',
                                                  'bronze_sword', 'low_chain_glove', 'cow_cape', 'chain_pants'],
                                                 k=snow_cnt * int_mul)
            list_maze_battle_get_item = []
            list_maze_battle_get_item.extend(list_fire_drop_item)
            list_maze_battle_get_item.extend(list_water_drop_item)
            list_maze_battle_get_item.extend(list_forest_drop_item)
            list_maze_battle_get_item.extend(list_snow_drop_item)
            return list_maze_battle_get_item
        else:
            pass

    # 타수호대 전투 승리한 후 아이템 얻는 함수
    def gard_battle_get_items(self):
        list_all_items = ['silver_helmet', 'cow_helmet', 'red_hood', 'bronze_armor',
                          'chain_armor', 'cow_armor', 'red_armor', 'bronze_shield',
                          'iron_shield', 'chain_shield', 'leather_shield', 'bronze_sword',
                          'stone_gem', 'bronze_wand', 'bronze_staff', 'bronze_bow',
                          'low_chain_glove', 'cow_glove', 'red_glove', 'cow_cape',
                          'red_cape', 'bronze_pants', 'chain_pants', 'cow_pants',
                          'red_pants', 'gold_helmet', 'horse_helmet', 'blue_hood',
                          'silver_armor', 'iron_armor', 'horse_armor', 'blue_armor',
                          'silver_sword', 'ruby_gem', 'silver_wand', 'silver_staff',
                          'silver_bow', 'middle_chain_glove', 'horse_glove', 'blue_glove',
                          'horse_cape', 'blue_cape', 'silver_pants', 'iron_pants',
                          'horse_pants', 'blue_pants', 'hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                          'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                          'all_potion_high', 'all_potion_middle', 'all_potion_low']
        if self.bool_war_result:
            list_gard_battle_get_item = random.choices(list_all_items, k=6)
            return list_gard_battle_get_item
        else:
            pass

    # 보스 전투 승리한 후 얻는 함수
    def boss_battle_get_items(self):
        if self.bool_war_result:
            list_boss_drop_item = []
            potions = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                      'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                      'all_potion_high', 'all_potion_middle', 'all_potion_low'], k=5)
            equipments = random.choices(['black_armor', 'black_cape', 'black_glove', 'black_pants', 'blue_armor',
                                         'blue_cape', 'blue_glove', 'blue_hood', 'blue_pants', 'bronze_armor',
                                         'bronze_bow', 'bronze_pants', 'bronze_shield', 'bronze_staff',
                                         'bronze_sword', 'bronze_wand', 'chain_armor', 'chain_pants',
                                         'chain_shield', 'cow_armor', 'cow_cape', 'cow_glove', 'cow_helmet',
                                         'cow_pants', 'croc_cape', 'croc_glove', 'diamond_gem', 'gold_armor',
                                         'gold_bow', 'gold_helmet', 'gold_pants', 'gold_staff', 'gold_sword',
                                         'gold_wand', 'high_chain_glove', 'horse_armor', 'horse_cape',
                                         'horse_glove', 'horse_helmet', 'horse_pants', 'iron_armor',
                                         'iron_pants', 'iron_shield', 'leather_shield', 'low_chain_glove',
                                         'middle_chain_glove', 'red_armor', 'red_cape', 'red_glove', 'red_hood',
                                         'red_pants', 'ruby_gem', 'silver_armor', 'silver_bow', 'silver_helmet',
                                         'silver_pants', 'silver_staff', 'silver_sword', 'silver_wand',
                                         'stone_gem'], k=5)

            list_boss_drop_item.extend(potions)
            list_boss_drop_item.extend(equipments)

            if self.int_floor == 1:
                ratio = random.randint(1, 10)
                if ratio == 1:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif self.int_floor == 2:
                ratio = random.randint(1, 10)
                if ratio <= 2:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif self.int_floor == 3:
                ratio = random.randint(1, 10)
                if ratio <= 3:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif self.int_floor == 4:
                list_boss_drop_item.extend(['revival_potion', 'clue_2'])
                return list_boss_drop_item
            elif self.int_floor == 5:
                list_boss_drop_item.extend(['revival_potion', 'clue_3'])
                return list_boss_drop_item
            elif self.int_floor == 6:
                list_boss_drop_item.extend(['revival_potion', 'clue_4'])
                return list_boss_drop_item
            elif self.int_floor == 7:
                list_boss_drop_item.extend(['revival_potion', 'clue_5'])
                return list_boss_drop_item
            else:
                print('층수 잘못 입력함')
                pass
        else:
            print('보스를 죽이지 못했습니다.')
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BattleClass()
    ex.show()
    app.exec_()

import os, sys
import random
import time

import keyboard
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# 메인화면
main = resource_path('../qt/This_is_boki.ui')
main_class = uic.loadUiType(main)[0]

class Main(QMainWindow, main_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()

        ### 임시 변수 ###
        int_btn_clicked_cnt = 0  # 수호대의 캐릭터 중 survival:True 수와 비교하여 버튼 활성화/비활성화를 체크하기 위함.
        int_survival = 0  # 수호대 캐릭터 중 survival:True 숫자

        list_area = ['area_fire', 'area_water', 'area_forest', 'area_snow']
        # self.current_loc = random.choice(self.list_area)         #from시연님(값 받아오기)
        list_maze_floor = [1, 2, 3, 4, 5, 6, 7, 8]
        current_loc = random.choice(list_maze_floor)  # from시연님(값 받아오기)

        num = random.choice(range(1, 11))
        dict_field_monster = {'area_fire': {'cnt': num,
                                            'hp': random.choices(range(200, 1001), k=num),
                                            'skill': ['fire_attack', 'fire_ball']},
                              'area_water': {'cnt': num,
                                             'hp': random.choices(range(200, 1001), k=num),
                                             'skill': ['aqua_attack', 'aqua_ball']},
                              'area_forest': {'cnt': num,
                                              'hp': random.choices(range(200, 1001), k=num),
                                              'skill': ['air_attack', 'air_ball']},
                              'area_snow': {'cnt': num,
                                            'hp': random.choices(range(200, 1001), k=num),
                                            'skill': ['ice_attack', 'snow_ball']}}

        # int_monster_count와 dict_maze_monster는 DungeonClass에서 상속받을 변수
        int_monster_count = random.randint(1, 10)
        dict_maze_monster = {'int_cnt': int_monster_count,
                             'list_hp': random.sample(range(200, 1000), int_monster_count),
                             'list_area_monster': random.choices(
                                 ['area_fire', 'area_water', 'area_forest', 'area_snow'],
                                 k=int_monster_count),
                             'list_damage': random.choices([0.05, 0.1], k=int_monster_count)}

        ## 필드 ##
        bool_meet_gard = False
        bool_meet_monster = False
        ## 던전 ##
        bool_meet_maze_gard = True
        bool_meet_enemy_monster = False
        bool_meet_boss_monster = False

        ### 변수 선언 ###
        dict_user_gard = {'gard': '',
                          'location': {'region': '', 'x': 0, 'y': 0},
                          'warrior': {'survival': True,
                                      'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                      'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                    'bronze_sword'],
                                      'skill': {10: 'slice_chop'}},
                          'archer': {'survival': True,
                                     'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 300,
                                     'equipment': [],
                                     'skill': {10: 'target_shot',
                                               15: 'dual_shot',
                                               20: 'master_shot'}},
                          'swordsman': {'survival': True,
                                        'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 250,
                                        'equipment': [],
                                        'skill': {10: 'slice_chop'}},
                          'wizard_red': {'survival': True,
                                         'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 150,
                                         'equipment': [],
                                         'skill': {1: ['heal_normal', 'fire_ball'],
                                                   15: ['heal_greater', 'fire_wall'],
                                                   20: 'thunder_breaker',
                                                   25: 'blizzard',
                                                   30: 'heal_all'}},
                          'wizard_black': {'survival': True,
                                           'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                           'equipment': [],
                                           'skill': {1: 'fire_ball',
                                                     15: 'fire_wall',
                                                     20: 'thunder_breaker',
                                                     25: 'blizzard'}},
                          'wizard_white': {'survival': True,
                                           'lv': 20, 'hp': 80, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 100,
                                           'equipment': [],
                                           'skill': {1: 'heal_normal',
                                                     10: 'hp_up',
                                                     15: ['heal_greater', 'mp_up'],
                                                     30: ['heal_all', 'map_find']}}}
        str_job = []
        str_job.extend(
            [sorted(dict_user_gard.keys())[4], 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white'])

        int_floor = current_loc
        if int_floor == 1:
            list_enemy_lvs = random.choices(range(20, 25), k=6)
            int_hp_up = 1.3
        elif int_floor == 2:
            list_enemy_lvs = random.choices(range(25, 30), k=6)
            int_hp_up = 1.3
        elif int_floor == 3:
            list_enemy_lvs = random.choices(range(30, 35), k=6)
            int_hp_up = 1.3 * 1.4
        elif int_floor == 4:
            list_enemy_lvs = random.choices(range(35, 40), k=6)
            int_hp_up = 1.3 * 1.4
        elif int_floor == 5:
            list_enemy_lvs = random.choices(range(45, 50), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5
        elif int_floor >= 6:
            list_enemy_lvs = random.choices(range(50, 100), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5 * 1.6

        list_enemy_lvs = [15, 17, 19, 20, 16, 18]
        str_enemy_gard = 'earth_gard'
        dict_enemy_gard = {'gard': str_enemy_gard,
                           'location': {'region': '', 'x': 0, 'y': 0},
                           'warrior': {'survival': True,
                                       'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                       'max_mp': 0, 'power': 200,
                                       'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                     'bronze_sword'],
                                       'skill': {10: 'slice_chop'}},
                           'archer': {'survival': True,
                                      'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                      'max_mp': 0, 'power': 300,
                                      'equipment': [],
                                      'skill': {10: 'target_shot',
                                                15: 'dual_shot',
                                                20: 'master_shot'}},
                           'swordsman': {'survival': True,
                                         'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                         'max_mp': 0, 'power': 250,
                                         'equipment': [],
                                         'skill': {10: 'slice_chop'}},
                           'wizard_red': {'survival': True,
                                          'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                          'max_mp': 0, 'power': 150,
                                          'equipment': [],
                                          'skill': {1: ['heal_normal', 'fire_ball'],
                                                    15: ['heal_greater', 'fire_wall'],
                                                    20: 'thunder_breaker',
                                                    25: 'bilzzard',
                                                    30: 'heal_all'}},
                           'wizard_black': {'survival': True,
                                            'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                            'max_mp': 0, 'power': 200,
                                            'equipment': [],
                                            'skill': {1: 'fire_ball',
                                                      15: 'fire_wall',
                                                      20: 'thunder_breaker',
                                                      25: 'bilzzard'}},
                           'wizard_white': {'survival': True,
                                            'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                            'max_mp': 0, 'power': 100,
                                            'equipment': [],
                                            'skill': {1: 'heal_normal',
                                                      15: 'heal_greater',
                                                      30: 'heal_all'}}}
        if dict_enemy_gard['gard'] == 'light_gard':
            str_enemy_gard = '빛'
        elif dict_enemy_gard['gard'] == 'moon_gard':
            str_enemy_gard = '달'
        elif dict_enemy_gard['gard'] == 'star_gard':
            str_enemy_gard = '별'
        elif dict_enemy_gard['gard'] == 'earth_gard':
            str_enemy_gard = '땅'

        list_job_name = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']
        monster_li = []
        list_enemy_btn = []
        list_enemy_line = []
        list_enemy_btn = self.groupBox.findChildren(QPushButton)
        list_enemy_line = self.groupBox.findChildren(QLineEdit)
        self.bool_war_result = False
        self.list_origin_power = []

        ### qt object -> list화하기 위한 findchildren 필요한 구간 ###
        list_frame = self.btn_widget.findChildren(QFrame)

        list_enemy_btn = [self.enemy_0, self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4,
                          self.enemy_5, self.enemy_6, self.enemy_7, self.enemy_8, self.enemy_9]

        list_enemy_line = [self.hp_enemy_0, self.hp_enemy_1, self.hp_enemy_2, self.hp_enemy_3, self.hp_enemy_4,
                           self.hp_enemy_5, self.hp_enemy_6, self.hp_enemy_7, self.hp_enemy_8, self.hp_enemy_9]

        list_job_lb = [self.warrior_lb, self.archer_lb, self.swordsman_lb,
                       self.red_wizard_lb, self.black_wizard_lb, self.white_wizard_lb]

        list_attack_btn = [self.pb_atk_warrior, self.pb_atk_archer, self.pb_atk_swordsman,
                           self.pb_atk_wizard_red, self.pb_atk_wizard_black, self.pb_atk_wizard_white]

        list_skill_btn = [self.pb_skill_job_warrior, self.pb_skill_job_archer, self.pb_skill_job_swordsman,
                          self.pb_skill_job_wizard_red, self.pb_skill_job_wizard_black, self.pb_skill_job_wizard_white]

        ### qt 연결 ###
        self.battle_dialog.verticalScrollBar().maximum()

        for i in range(6):
            list_attack_btn[i].clicked.connect(lambda x, y=i: self.atk_choice(x, y, dict_user_gard, list_job_name))
            list_attack_btn[i].clicked.connect(lambda x, y=i: self.move_image_forward(x, y, list_job_lb, list_job_name))
            list_attack_btn[i].clicked.connect(lambda x, y=i: self.attack_btn_clicked(x, y, dict_user_gard, str_job,
                                                                                      list_attack_btn,
                                                                                      int_btn_clicked_cnt,
                                                                                      int_survival))

            list_frame[i].findChildren(QPushButton)[2].clicked.connect(
                lambda x, y=i: self.skill_btn_clicked(x, y, dict_user_gard, str_job, list_skill_btn,
                                                      int_btn_clicked_cnt, int_survival))
            list_frame[i].findChildren(QPushButton)[2].clicked.connect(
                lambda x, y=i: self.skill_widget_open(x, y, str_job, dict_user_gard, bool_meet_gard,
                                                      bool_meet_maze_gard, list_skill_btn))

        if bool_meet_monster:
            for i in range(num):
                list_enemy_btn[i].clicked.connect(lambda x, y=i: self.monster_atk_choice(x, y))

        elif bool_meet_enemy_monster:
            for i in range(int_monster_count):
                list_enemy_btn[i].clicked.connect(lambda x, y=i: self.monster_atk_choice(x, y))

        elif bool_meet_maze_gard:
            for i in range(6):
                list_enemy_btn[i].clicked.connect(
                    lambda x, y=i: self.gard_atk_choice(x, y, dict_user_gard, list_job_name,
                                                        bool_meet_gard, bool_meet_maze_gard,
                                                        dict_enemy_gard, str_job, list_enemy_line, list_enemy_btn))

        self.war_start.clicked.connect(
            lambda: self.battle_location(list_frame, list_enemy_line, list_enemy_btn, list_attack_btn, dict_user_gard,
                                         dict_enemy_gard, str_job, int_survival, current_loc, str_enemy_gard, list_area,
                                         bool_meet_gard,
                                         bool_meet_monster, list_maze_floor, bool_meet_enemy_monster,
                                         bool_meet_maze_gard, bool_meet_boss_monster))

        self.war_start.clicked.connect(
            lambda: self.show_war_result(dict_user_gard, current_loc, list_area, bool_meet_gard, dict_enemy_gard,
                                         str_job, bool_meet_monster, num,
                                         dict_field_monster, list_maze_floor, bool_meet_maze_gard,
                                         bool_meet_enemy_monster,
                                         int_monster_count, dict_maze_monster, bool_meet_boss_monster))
        self.war_start.clicked.connect(lambda: self.equip_btn_disabled(list_frame))

        ### 전투 중 스킬사용(고주양:전사,궁수,검사)###
        self.skill_btn_warrior_slice_chop.clicked.connect(
            lambda: self.warrior_skill_effect(dict_user_gard, bool_meet_monster, bool_meet_enemy_monster,
                                              bool_meet_gard, bool_meet_maze_gard, bool_meet_boss_monster))

        self.skill_btn_archer_target_shot.clicked.connect(lambda: self.archer_skill_effect_1(dict_user_gard, str_job))
        self.skill_btn_archer_dual_shot.clicked.connect(
            lambda x: self.archer_skill_effect_2(x, dict_user_gard, str_job))
        self.skill_btn_archer_master_shot.clicked.connect(
            lambda x: self.archer_skill_effect_3(x, dict_user_gard, str_job))

        self.skill_btn_swordsman_slice_chop.clicked.connect(
            lambda: self.swordsman_skill_effect(dict_user_gard, bool_meet_monster, bool_meet_enemy_monster,
                                                bool_meet_gard, bool_meet_maze_gard, bool_meet_boss_monster))

        ### 전투 중 스킬사용(이시연:적법사/흑법사/백법사)###
        # self.skill_btn_wizard_red_heal_normal.clicked.connect
        # self.skill_btn_wizard_red_heal_normal.clicked.connect
        # self.skill_btn_wizard_red_heal_normal.clicked.connect
        # self.skill_btn_wizard_red_fire_ball.clicked.connect
        # self.skill_btn_wizard_red_fire_wall.clicked.connect
        # self.skill_btn_wizard_red_thunder_breaker.clicked.connect
        # self.skill_btn_wizard_red_blizzard.clicked.connect
        #
        # self.skill_btn_wizard_black_fire_ball.connect
        # self.skill_btn_wizard_black_fire_wall.connect
        # self.skill_btn_wizard_black_thunder_breaker.connect
        # self.skill_btn_wizard_black_blizzard.connect

        # self.skill_btn_wizard_white_heal_normal.connect
        # self.skill_btn_wizard_white_heal_greater.connect
        # self.skill_btn_wizard_white_heal_all.connect
        # self.skill_btn_wizard_white_hp_up.connect
        # self.skill_btn_wizard_white_mp_up.connect
        # self.skill_btn_wizard_white_map_find.connect

    ### 함수 선언 ###
    # 전투결과(승패) 반환
    def show_war_result(self, dict_user_gard, current_loc, list_area, bool_meet_gard, dict_enemy_gard, str_job,
                        bool_meet_monster, num,
                        dict_field_monster, list_maze_floor, bool_meet_maze_gard, bool_meet_enemy_monster,
                        int_monster_count, dict_maze_monster, bool_meet_boss_monster):
        user_died = 0
        enemy_died = 0
        if current_loc in list_area:
            if bool_meet_gard == True:
                for a in range(6):
                    if dict_enemy_gard[str_job[a]]['hp'] <= 0:
                        enemy_died += 1
                    if enemy_died == 6:
                        self.bool_war_result = True
                        self.battle_dialog.append(f"수호대 {a + 1}명 처치")
                for b in str_job:
                    if dict_user_gard[b]['survival'] == False:
                        user_died += 1
                    if user_died == 6:
                        self.bool_war_result = False
                        self.battle_dialog.append("수호대와의 전투에서 패배했습니다..")
        elif bool_meet_monster == True:
            for c in range(num):
                if dict_field_monster['hp'][c] <= 0:
                    enemy_died += 1
                if enemy_died == 6:
                    self.bool_war_result = True
                    self.battle_dialog.append(f"{c + 1}번째 몬스터 처치")
            for d in str_job:
                if dict_user_gard[d]['survival'] == False:
                    user_died += 1
                if user_died == 6:
                    self.bool_war_result = False
                    self.battle_dialog.append("일반몬스터와의 전투에서 패배했습니다..")
        if current_loc in list_maze_floor:
            if bool_meet_maze_gard == True:
                for e in range(6):
                    if dict_enemy_gard[str_job[e]]['hp'] <= 0:
                        enemy_died += 1
                    if enemy_died == 6:
                        self.bool_war_result = True
                        self.battle_dialog.append(f"수호대 {e + 1}명 처치")
                for f in str_job:
                    if dict_user_gard[f]['survival'] == False:
                        user_died += 1
                    if user_died == 6:
                        self.bool_war_result = False
                        self.battle_dialog.append("수호대와의 전투에서 패배했습니다..")
        elif bool_meet_enemy_monster == True:
            for g in range(int_monster_count):
                if dict_maze_monster['list_hp'][g] <= 0:
                    enemy_died += 1
                if enemy_died == 6:
                    self.bool_war_result = True
                    self.battle_dialog.append(f"{g + 1}번째 몬스터 처치")
            for h in str_job:
                if dict_user_gard[h]['survival'] == False:
                    user_died += 1
                if user_died == 6:
                    self.bool_war_result = False
                    self.battle_dialog.append("일반몬스터와의 전투에서 패배했습니다..")
        elif bool_meet_boss_monster == True:
            print("if - 조우한 보스의 hp가 0이라면 return self.war_result = True, bool_boss_death = True")
            print("elif - 유저 수호대의 모든 구성원의 hp가 0이라면 return self.war_result = False")

    # if not isinstance(self.bool_war_result, bool):
    #     raise "bool이 값할당 안됌!"

    # 전투 후 스킬사용에 따른 초기화를 해주는 함수
    def reset_user_gard(self, dict_user_gard, str_job):
        if self.bool_war_result:
            dict_user_gard['warrior']['power'] = self.origin_power
            for i in range(6):
                dict_user_gard[str_job[i]]['power'] = self.list_origin_power[i]
        elif not self.bool_war_result:
            dict_user_gard['warrior']['power'] = self.origin_power
            for i in range(6):
                dict_user_gard[str_job[i]]['power'] = self.list_origin_power[i]

    # 전투 횟수 카운트
    def war_cnt(self):
        int_war_cnt = int
        if self.bool_war_result == True:
            int_war_cnt += 1
        elif self.bool_war_result == False:
            int_war_cnt += 1
        return int_war_cnt

    # 전투횟수에 따른 EXP상승(n0레벨까지 n0판 당 +n레벨 상승) -> return
    def user_gard_lv_update(self, int_war_cnt, dict_user_gard, str_job, bool_boss_death, int_floor):
        str_lv_update_msg1 = ''
        str_lv_update_msg2 = ''
        list_update_job1 = []
        list_update_job2 = []
        up1 = int
        for i in range(6):
            if int_war_cnt == 10:
                dict_user_gard[str_job[i]]['lv'] += 1
                list_update_job1.append(str_job[i])
                up1 = 1
            elif int_war_cnt == 20:
                dict_user_gard[str_job[i]]['lv'] += 2
                list_update_job1.append(str_job[i])
                up1 = 2
            elif int_war_cnt == 30:
                dict_user_gard[str_job[i]]['lv'] += 3
                list_update_job1.append(str_job[i])
                up1 = 3
            elif int_war_cnt == 40:
                dict_user_gard[str_job[i]]['lv'] += 4
                list_update_job1.append(str_job[i])
                up1 = 4
            elif int_war_cnt == 50:
                dict_user_gard[str_job[i]]['lv'] += 5
                list_update_job1.append(str_job[i])
                up1 = 5
            elif int_war_cnt == 60:
                dict_user_gard[str_job[i]]['lv'] += 6
                list_update_job1.append(str_job[i])
                up1 = 6
            elif int_war_cnt == 70:
                dict_user_gard[str_job[i]]['lv'] += 7
                list_update_job1.append(str_job[i])
                up1 = 7
            elif int_war_cnt == 80:
                dict_user_gard[str_job[i]]['lv'] += 8
                list_update_job1.append(str_job[i])
                up1 = 8
            elif int_war_cnt == 90:
                dict_user_gard[str_job[i]]['lv'] += 9
                list_update_job1.append(str_job[i])
                up1 = 9
            elif int_war_cnt == 100:
                dict_user_gard[str_job[i]]['lv'] += 10
                list_update_job1.append(str_job[i])
                up1 = 10

            # 보스몬스터 처치시 n층별 +n레벨
            if bool_boss_death == True:
                if int_floor == 1:
                    dict_user_gard[str_job[i]]['lv'] += 1
                    list_update_job2.append(str_job[i])
                elif int_floor == 2:
                    dict_user_gard[str_job[i]]['lv'] += 2
                    list_update_job2.append(str_job[i])
                elif int_floor == 3:
                    dict_user_gard[str_job[i]]['lv'] += 3
                    list_update_job2.append(str_job[i])
                elif int_floor == 4:
                    dict_user_gard[str_job[i]]['lv'] += 4
                    list_update_job2.append(str_job[i])
                elif int_floor == 5:
                    dict_user_gard[str_job[i]]['lv'] += 5
                    list_update_job2.append(str_job[i])
                elif int_floor == 6:
                    dict_user_gard[str_job[i]]['lv'] += 6
                    list_update_job2.append(str_job[i])
                elif int_floor == 7:
                    dict_user_gard[str_job[i]]['lv'] += 7
                    list_update_job2.append(str_job[i])

        list_update_job1 = ','.join(list_update_job1)
        str_lv_update_msg1 = f"{list_update_job1}의 레벨 +{up1}상승"

        list_update_job2 = ','.join(list_update_job2)
        str_lv_update_msg2 = f"{list_update_job2}의 레벨 {int_floor}증가"

        return dict_user_gard, str_lv_update_msg1, str_lv_update_msg2

    # 10레벨당 전 공격력의 * 10% 상승 -> return
    def user_gard_power_update(self, dict_user_gard, str_job):
        str_power_update_msg = ''
        list_update_job3 = []
        for i in range(6):
            if dict_user_gard[str_job[i]]['lv'] % 10 == 0:
                dict_user_gard[str_job[i]]['power'] += dict_user_gard[str_job[i]]['power'] * 0.1
                list_update_job3.append(str_job[i])

            list_update_job3 = ','.join(list_update_job3)
            str_power_update_msg = f"{list_update_job3}의 공격력 10% 증가"

        return dict_user_gard, str_power_update_msg

    # 유저수호대 레벨에 따른 HP,MP 상승과 레벨 -> return
    def user_gard_hpmp_update(self, dict_user_gard, str_job):
        str_hpmp_update_msg = ''
        list_update_job4 = []
        up2 = ''
        for i in range(6):
            if dict_user_gard[str_job[i]]['lv'] <= 10:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.1
                if i == 0:
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.1
                    list_update_job4.append(str_job[i])
                up2 = '1.1'
            elif dict_user_gard[str_job[i]]['lv'] <= 10:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.2
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.2
                    list_update_job4.append(str_job[i])
                up2 = '1.2'
            elif dict_user_gard[str_job[i]]['lv'] <= 30:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.3
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.3
                    list_update_job4.append(str_job[i])
                up2 = '1.3'
            elif dict_user_gard[str_job[i]]['lv'] <= 40:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]] * 1.4
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.4
                    list_update_job4.append(str_job[i])
                up2 = '1.4'
            elif dict_user_gard[str_job[i]]['lv'] <= 50:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.5
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.5
                    list_update_job4.append(str_job[i])
                up2 = '1.5'
            elif dict_user_gard[str_job[i]]['lv'] <= 60:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.6
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.6
                    list_update_job4.append(str_job[i])
                up2 = '1.6'
            elif dict_user_gard[str_job[i]]['lv'] <= 70:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.7
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.7
                    list_update_job4.append(str_job[i])
                up2 = '1.7'
            elif dict_user_gard[str_job[i]]['lv'] <= 80:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.8
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.8
                    list_update_job4.append(str_job[i])
                up2 = '1.8'
            elif dict_user_gard[str_job[i]]['lv'] <= 90:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 1.9
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 1.9
                    list_update_job4.append(str_job[i])
                up2 = '1.9'
            elif dict_user_gard[str_job[i]]['lv'] <= 100:
                dict_user_gard[str_job[i]]['hp'] += dict_user_gard[str_job[i]]['hp'] * 2.0
                if str_job[i] == 'warrior':
                    dict_user_gard[str_job[i]]['mp'] = 0
                else:
                    dict_user_gard[str_job[i]]['mp'] += dict_user_gard[str_job[i]]['mp'] * 2.0
                    list_update_job4.append(str_job[i])
                up2 = '2.0'

        list_update_job4 = ','.join(list_update_job4)
        str_hpmp_update_msg = f"{str_job[0]}의 hp가 1.1 상승, {list_update_job4}의 hp, mp가 {up2} 상승"

        return dict_user_gard, str_hpmp_update_msg

    # 배틀 로케이션과 만난 적 확인 : 미구현된 부분은 주석처리함.
    def battle_location(self, list_frame, list_enemy_line, list_enemy_btn, list_attack_btn, dict_user_gard,
                        dict_enemy_gard, str_job, int_survival, current_loc,
                        str_enemy_gard, list_area, bool_meet_gard, bool_meet_monster, list_maze_floor,
                        bool_meet_enemy_monster, bool_meet_maze_gard, bool_meet_boss_monster):
        if current_loc in list_area:
            if bool_meet_gard == True:
                self.battle_gard()
            elif bool_meet_monster == True:
                self.battle_monster()
        if current_loc in list_maze_floor:
            if bool_meet_maze_gard == True:
                self.battle_gard(list_frame, list_enemy_line, list_enemy_btn, list_attack_btn, dict_user_gard,
                                 dict_enemy_gard, str_job, int_survival, current_loc,
                                 str_enemy_gard, bool_meet_gard, bool_meet_maze_gard)
            elif bool_meet_enemy_monster == True:
                self.battle_monster()
            elif bool_meet_boss_monster == True:
                self.battle_maze_boss()

    # -------------전투 공통 함수---------------------------------------------------------------------------------_----------#
    # 전투화면으로 전환시 각 캐릭터의 [공격]버튼에 따른 QDialog창 생성
    def atk_choice(self, x, index, dict_user_gard, list_job_name):

        self.atk_dialog = QDialog()
        self.atk_dialog.setWindowTitle("ATTACK")

        radio_button1 = QRadioButton(f"물리공격(현재 공격력: {dict_user_gard[list_job_name[index]]['power']})")
        OK_button = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(radio_button1)
        layout.addWidget(OK_button)
        self.atk_dialog.setLayout(layout)

        if radio_button1.isChecked:
            selected_option = dict_user_gard[list_job_name[index]]['power']

        OK_button.clicked.connect(self.atk_dialog_close)
        self.atk_dialog.exec_()

        return selected_option

    # 각 캐릭터의 [공격]버튼에 따른 QDialog창 닫기
    def atk_dialog_close(self):
        self.atk_dialog.close()

    # 한번 누른 구성원의 [공격]버튼은 적의 턴이 끝날때 까지 비활성화.
    def attack_btn_clicked(self, x, num, dict_user_gard, str_job,
                           list_attack_btn, int_btn_clicked_cnt, int_survival):
        if x == False:
            list_attack_btn[num].setEnabled(False)
            int_btn_clicked_cnt = num + 1
        for i, job in enumerate(str_job):
            if dict_user_gard[job]['survival'] == True:
                int_survival += 1
        if int_btn_clicked_cnt == int_survival:
            for i, job in enumerate(str_job):
                if dict_user_gard[job]['survival'] == True:
                    list_attack_btn[i].setEnabled(True)
                    int_btn_clicked_cnt = 0

    # [스킬]버튼에 따른 직업별 스킬창으로 화면전환(gif)
    def skill_widget_open(self, x, index, str_job, dict_user_gard, bool_meet_gard, bool_meet_maze_gard, list_skill_btn):
        list_skill_btn = []
        list_gif_lb = []
        if index == 3:
            self.movie = QMovie('../wizard_red/skill2.gif', QByteArray(), self)
            self.gif_3_1.setMovie(self.movie)
            self.movie.start()
        for i in range(6):
            list_gif_lb.append(getattr(self, f"gif_{i}"))
            list_skill_btn.append(getattr(self, f"pb_skill_job_{str_job[i]}"))
            self.movie = QMovie(f'../{str_job[i]}/skill.gif', QByteArray(), self)
            list_gif_lb[i].setMovie(self.movie)
            self.movie.start()

        if index == 3:
            self.stackedWidget.setCurrentIndex(4)
            self.skill_btn_wizard_red_heal_normal.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
            self.skill_btn_wizard_red_heal_greater.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        elif index == 4:
            self.stackedWidget.setCurrentIndex(5)
        elif index == 5:
            self.stackedWidget.setCurrentIndex(6)
            self.skill_btn_wizard_white_heal_normal.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
            self.skill_btn_wizard_white_heal_greater.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        else:
            self.stackedWidget.setCurrentIndex(index + 1)

        # 직업 레벨에 따른 버튼 활성화/비활성화
        job_skill_btn = self.sender()
        job_skill_choice = []
        for i, button in enumerate(list_skill_btn):  # 여기서 button = 각 직업의 [스킬]버튼
            dict_skill_list = dict_user_gard[str_job[i]]['skill']  # dict_skill_list는 각 직업의 skill 딕셔너리가 담긴다.
            if job_skill_btn == button:
                for lv, name in dict_skill_list.items():
                    if str_job[i] == 'wizard_red':
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_normal'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_greater'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_all'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_fire_ball'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_fire_wall'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_thunder_breaker'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_blizzard'))
                    elif str_job[i] == 'wizard_white':
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_normal'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_greater'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_heal_all'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_hp_up'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_mp_up'))
                        job_skill_choice.append(getattr(self, f'skill_btn_{str_job[i]}_map_find'))
                    else:
                        button_name = f"skill_btn_{str_job[i]}_{name}"
                        job_skill_choice.append(getattr(self, button_name))
                    for k in job_skill_choice:
                        if dict_user_gard[str_job[i]]['lv'] < lv:
                            if str_job[i] == 'archer':
                                index = 17
                                if k.objectName()[index:] == dict_skill_list[lv]:
                                    k.setDisabled(True)
                            elif str_job[i] == 'wizard_red':  # 15의 fire_ball heal_greater 안됌
                                index = 21
                                if k.objectName()[index:] == dict_skill_list[lv]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][0]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][1]:
                                    k.setDisabled(True)
                            elif str_job[i] == 'wizard_black' or str_job[i] == 'wizard_white':
                                index = 23
                                if k.objectName()[index:] == dict_skill_list[lv]:  # 15, 30의 4개 스킬 버튼 모두 활성화됨.
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][0]:
                                    k.setDisabled(True)
                                elif k.objectName()[index:] == dict_skill_list[lv][1]:
                                    k.setDisabled(True)
                            else:
                                k.setDisabled(True)

    # 한번 누른 구성원의 [스킬]버튼은 적의 턴이 끝날때 까지 비활성화.
    def skill_btn_clicked(self, x, num, dict_user_gard, str_job,
                          list_skill_btn, int_btn_clicked_cnt, int_survival):
        if x == False:
            list_skill_btn[num].setEnabled(False)
            int_btn_clicked_cnt = num + 1
            print(f'int_btn_clicked_cnt: {int_btn_clicked_cnt}')
        for i, job in enumerate(str_job):
            if dict_user_gard[job]['survival'] == True:
                int_survival += 1
        print(f'int_survival: {int_survival}')
        if int_btn_clicked_cnt == int_survival:
            for i, job in enumerate(str_job):
                if dict_user_gard[job]['survival'] == True:
                    list_skill_btn[i].setEnabled(True)
                    int_btn_clicked_cnt = 0

    def warrior_skill_effect(self, dict_user_gard, bool_meet_monster, bool_meet_enemy_monster,
                             bool_meet_gard, bool_meet_maze_gard, bool_meet_boss_monster):

        # 전투 중에는 유지하되, 전투가 끝났다 -> show_war_result()에서 power는 스킬사용 이전(origin_power)로 돌아간다.
        self.origin_power = dict_user_gard['warrior']['power']
        power_up = random.randint(2, 50)
        dict_user_gard['warrior']['power'] = dict_user_gard['warrior']['power'] * power_up
        self.stackedWidget.setCurrentIndex(0)
        self.battle_dialog.append(
            f"warrior의 slice_chop사용!으로 현 전투 중 공격력이 {power_up}배 증가하여 {dict_user_gard['warrior']['power']}만큼 올랐다! ")

        # 해당 스킬은 몬스터/수호대/보스를 만났을 때 적용된다.
        if bool_meet_monster or bool_meet_enemy_monster:
            QTimer.singleShot(2000, self.enemy_monster_atk)
        elif bool_meet_gard or bool_meet_maze_gard:
            QTimer.singleShot(2000, self.enemy_gard_atk)
        elif bool_meet_boss_monster:
            QTimer.singleShot(2000, self.boss_gard_atk)

    def archer_skill_effect_1(self, dict_user_gard, str_job):
        for i in range(6):
            self.list_origin_power.append(dict_user_gard[str_job[i]]['power'])

        power_up = random.choice([0.2, 0.3, 0.4, 0.5])
        for i in range(6):
            dict_user_gard[str_job[i]]['power'] * power_up

        dict_user_gard['archer']['mp'] -= 30
        self.stackedWidget.setCurrentIndex(0)
        self.battle_dialog.append(f"archer의 Target shot으로 현 전투 중 모든 구성원의 공격력이 {power_up}배 증가! ")
        self.battle_dialog.append(f"archer의 MP가 30줄었습니다.")

    def archer_skill_effect_2(self, x, dict_user_gard, str_job):
        skill_effect_2 = 0
        if x == False:
            skill_effect_2 += 1

        if skill_effect_2 % 2 == 0:
            msg = QMessageBox()
            skill_ban = msg.critical(self, "스킬 사용 제한", "해당 기술을 다음 턴에 사용가능합니다.", msg.Ok)
            if skill_ban == msg.Yes:  # 버튼의 이름을 넣으면 됩니다.
                self.stackedWidget.setCurrentIndex(2)
        else:
            for i in range(6):
                self.list_origin_power.append(dict_user_gard[str_job[i]]['power'])

            power_up = random.choice([0.4, 0.5, 0.6])
            for i in range(6):
                dict_user_gard[str_job[i]]['power'] * power_up
            dict_user_gard['archer']['mp'] -= 50
            self.stackedWidget.setCurrentIndex(0)
            self.battle_dialog.append(f"archer의 Target shot으로 현 전투 중 모든 구성원의 공격력이 {power_up}배 증가! ")
            self.battle_dialog.append(f"archer의 MP가 50줄었습니다.")

    def archer_skill_effect_3(self, x, dict_user_gard, str_job):
        skill_effect_3 = 0
        if x == False:
            skill_effect_3 += 1

        if skill_effect_3 % 2 == 0:
            msg = QMessageBox()
            skill_ban = msg.critical(self, "스킬 사용 제한", "해당 기술을 다음 턴에 사용가능합니다.", msg.Ok)
            if skill_ban == msg.Yes:  # 버튼의 이름을 넣으면 됩니다.
                self.stackedWidget.setCurrentIndex(2)
        else:
            for i in range(6):
                self.list_origin_power.append(dict_user_gard[str_job[i]]['power'])
            power_up = random.choice([0.5, 0.6, 0.7])
            for i in range(6):
                dict_user_gard[str_job[i]]['power'] * power_up
            dict_user_gard['archer']['mp'] -= 70
            self.stackedWidget.setCurrentIndex(0)
            self.battle_dialog.append(f"archer의 Target shot으로 현 전투 중 모든 구성원의 공격력이 {power_up}배 증가! ")
            self.battle_dialog.append(f"archer의 MP가 70줄었습니다.")

    def swordsman_skill_effect(self, dict_user_gard, bool_meet_monster, bool_meet_enemy_monster,
                               bool_meet_gard, bool_meet_maze_gard, bool_meet_boss_monster):

        # 전투 중에는 유지하되, 전투가 끝났다 -> show_war_result()에서 power는 스킬사용 이전(origin_power)로 돌아간다.
        origin_power = dict_user_gard['warrior']['power']
        power_up = random.randint(2, 50)
        dict_user_gard['swordsman']['power'] = dict_user_gard['swordsman']['power'] * power_up
        dict_user_gard['swordsman']['mp'] -= 50
        self.stackedWidget.setCurrentIndex(0)
        self.battle_dialog.append(
            f"swordsman의 slice_chop사용으로 현 전투 중 공격력이 {power_up}배 증가하여 {dict_user_gard['warrior']['power'] * power_up}만큼 올랐다! ")
        self.battle_dialog.append(f"swordsman의 MP가 50줄었습니다.")
        # 해당 스킬은 몬스터/수호대/보스를 만났을 때 적용된다.
        if bool_meet_monster or bool_meet_enemy_monster:
            QTimer.singleShot(2000, self.enemy_monster_atk)
        elif bool_meet_gard or bool_meet_maze_gard:
            QTimer.singleShot(2000, self.enemy_gard_atk)
        elif bool_meet_boss_monster:
            QTimer.singleShot(2000, self.boss_gard_atk)

        if self.bool_war_result:
            dict_user_gard['warrior']['power'] = origin_power
        elif self.bool_war_result == False:
            dict_user_gard['warrior']['power'] = origin_power

        return dict_user_gard

    # 전투화면으로 전환시 각 캐릭터의 [장비]버튼 setDisabled처리
    def equip_btn_disabled(self, list_frame):
        for i in range(6):
            list_job_btn = list_frame[i].findChildren(QPushButton)[1].setDisabled(True)

    # 2번 방식 : 위치가 바뀌면서 모션 수행
    def move_image_forward(self, x, lb_index, list_job_lb, list_job_name):
        current_pos = list_job_lb[lb_index].pos()
        print(current_pos)
        if current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            list_job_lb[lb_index].setPixmap(QPixmap(f'../{list_job_name[lb_index]}/attack1.png'))
            list_job_lb[lb_index].move(current_pos.x(), current_pos.y() - 200)
            QTimer.singleShot(1000, lambda: self.move_image_forward2(lb_index, list_job_lb, list_job_name))
        return lb_index

    def move_image_forward2(self, lb_index, list_job_lb, list_job_name):
        current_pos = list_job_lb[lb_index].pos()
        if current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            list_job_lb[lb_index].setPixmap(QPixmap(f'../{list_job_name[lb_index]}/attack2.png'))
            list_job_lb[lb_index].move(current_pos.x(), current_pos.y() - 100)
            QTimer.singleShot(1000, lambda: self.move_image_back(lb_index, list_job_lb, list_job_name))
            # self.timer.stop()
        return lb_index

    def move_image_back(self, lb_index, list_job_lb, list_job_name):
        x = 0
        current_pos = list_job_lb[lb_index].pos()
        if current_pos.x() < 900:  # 원래 위치로 돌아가는 x 좌표
            list_job_lb[lb_index].setPixmap(QPixmap(f'../{list_job_name[lb_index]}/walk1.png'))
            if lb_index == 0:
                x = -40
                y = 310
            elif lb_index == 1:
                x = 80
                y = 310
            elif lb_index == 2:
                x = 50
                y = 310
            elif lb_index == 3:
                x = 270
                y = 310
            elif lb_index == 4:
                x = 370
                y = 260
            elif lb_index == 5:
                x = 570
                y = 280
            list_job_lb[lb_index].move(x, y)
            self.timer.stop()

    # 각 캐릭터의 [도망]버튼 클릭시 battle_dialog에 메세지를 띄운다. 확률에 따른 도망 성공/실패 -> 반환값(필드/전투화면)으로넘기기
    def user_gard_run(self, current_loc, list_area, list_maze_floor):
        num = random.choice(range(1, 101))
        sucess_rate = list(range(0, 31))
        sucess_rate_num = random.choice(sucess_rate)
        if sucess_rate_num < num:
            self.battle_dialog.append(f"""{100 - sucess_rate_num}%확률로 도망에 실패했습니다.
        전투화면이 유지됩니다.""")
            bool_run_mode = False
        elif sucess_rate_num >= num:
            if current_loc in list_area:
                current_loc = '필드'
            elif current_loc in list_maze_floor:
                current_loc = '던전'
            self.battle_dialog.append(f"""{sucess_rate_num}%확률로 도망에 성공했습니다.
        {current_loc}화면으로 돌아갑니다.""")
            bool_run_mode = True
            return bool_run_mode

    # -------------수호대와의 전투-------------------------------------------------------------------------------------------#
    # [필드/던전]타수호대 조우 - 전투가능한 구성원의 [공격][스킬]버튼이 활성화
    def battle_gard(self, list_frame, list_enemy_line, list_enemy_btn, list_attack_btn, dict_user_gard,
                    dict_enemy_gard, str_job, int_survival, current_loc,
                    str_enemy_gard, bool_meet_gard, bool_meet_maze_gard):

        # 따로 함수로 빼서 호출할까...
        for i in range(6):
            if str_job[i] in dict_user_gard.keys():
                if dict_user_gard[str_job[i]]['survival'] == True:
                    int_survival = i + 1
                    list_attack_btn[i].setEnabled(True)
                    list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                    list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                if dict_user_gard[str_job[i]]['survival'] == False:
                    list_attack_btn[i].setDisabled(True)
                    list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                    list_frame[i].findChildren(QPushButton)[3].setDisabled(True)

                if bool_meet_gard:
                    area = current_loc.split('_')
                    self.battle_dialog.setText(f"{area[1]}지역에서 벌어진 {str_enemy_gard}의 수호대와의 전투 시작!")
                    for k in range(6):
                        list_enemy_line[k].setText(f"{str_job[k]} HP: {dict_user_gard[str_job[k]]['hp']:.f}")
                        pixmap = QPixmap(f'../{str_job[k]}/reverse.png')
                        pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                        icon = QIcon()
                        icon.addPixmap(pixmap)
                        list_enemy_btn[k].setIcon(icon)
                        list_enemy_btn[k].setIconSize(QSize(100, 100))

                elif bool_meet_maze_gard:
                    self.battle_dialog.setText(f"{current_loc}층에서 벌어진 {str_enemy_gard}의 수호대와의 전투 시작!")
                    for j in range(6):
                        list_enemy_line[j].setText(f"{str_job[j]} HP: {dict_enemy_gard[str_job[j]]['hp']}")
                        pixmap = QPixmap(f'../{str_job[j]}/reverse.png')
                        pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                        icon = QIcon()
                        icon.addPixmap(pixmap)
                        list_enemy_btn[j].setIcon(icon)
                        list_enemy_btn[j].setIconSize(QSize(100, 100))

    # 각 캐릭터의 [공격]버튼에 따른 누가/누구에게/nnn데미지 입었습니다. battle_dialog 메세지띄우기
    def gard_atk_choice(self, x, index, dict_user_gard, list_job_name,
                        bool_meet_gard, bool_meet_maze_gard,
                        dict_enemy_gard, str_job,
                        list_enemy_line, list_enemy_btn):
        damage = self.atk_choice(x, index, dict_user_gard, list_job_name)
        self.battle_dialog.append(f"수호대{str_job[index]}을/를 공격해 {damage}데미지를 입혔다.")
        if bool_meet_gard or bool_meet_maze_gard:
            dict_enemy_gard[str_job[index]]['hp'] = dict_enemy_gard[str_job[index]]['hp'] - damage
            list_enemy_line[index].setText(f"{str_job[index]} HP:{dict_enemy_gard[str_job[index]]['hp']}")
            if dict_enemy_gard[str_job[index]]['hp'] <= 0:
                dict_enemy_gard[str_job[index]]['hp'] = 0
                list_enemy_line[index].setText(f"{str_job[index]} HP: 0")
                list_enemy_btn[index].setDisabled(True)

        QTimer.singleShot(2000, self.enemy_gard_atk)

    # 타수호대의 유저 수호대 (랜덤)(일반공격/스킬/아이템사용)기능
    def enemy_gard_atk(self):
        print("3")

        # -------------몬스터와의 전투-------------------------------------------------------------------------------------------#
        # [필드/던전]몬스터 조우 - 전투가능한 구성원의 [공격][스킬]버튼이 활성화
        def battle_monster(self, str_job, dict_user_gard, int_survival, num, int_monster_count,
                           list_attack_btn, list_job_lb, list_frame, list_enemy_line, list_enemy_btn,
                           dict_field_monster, monster_li, dict_maze_monster,
                           bool_meet_monster, bool_meet_enemy_monster, current_loc):
            list_frame = self.findChildren(QFrame)[7:]
            for i in range(6):
                if str_job[i] in dict_user_gard.keys():
                    if dict_user_gard[str_job[i]]['survival'] == True:
                        int_survival = i + 1
                        list_attack_btn[i].setEnabled(True)
                        list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                        list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                    if dict_user_gard[str_job[i]]['survival'] == False:
                        list_attack_btn[i].setDisabled(True)
                        list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                        list_frame[i].findChildren(QPushButton)[3].setDisabled(True)
                        list_job_lb[i].setPixmap(QPixmap(f'../{str_job[i]}/died.png'))

            if bool_meet_monster:
                area = current_loc.split('_')
                self.battle_dialog.setText(f"{area[1]}지역에서 벌어진 전투 시작!")
                for k in range(num):
                    list_enemy_line[k].setText(f"몬스터 HP: {str(dict_field_monster[current_loc]['hp'][k])}")
                    if current_loc == 'area_fire':
                        if dict_field_monster[current_loc]['hp'][k] <= 250:
                            monster_li.append('small_dragon[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 300:
                            monster_li.append('small_dragon[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 400:
                            monster_li.append('small_dragon[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 500:
                            monster_li.append('small_dragon[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 600:
                            monster_li.append('small_dragon[5]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 700:
                            monster_li.append('demon[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 800:
                            monster_li.append('demon[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 900:
                            monster_li.append('demon[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 950:
                            monster_li.append('demon[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 1000:
                            monster_li.append('demon[5]')
                    elif current_loc == 'area_water':
                        if dict_field_monster[current_loc]['hp'][k] <= 250:
                            monster_li.append('dragon[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 300:
                            monster_li.append('dragon[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 400:
                            monster_li.append('dragon[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 500:
                            monster_li.append('dragon[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 600:
                            monster_li.append('dragon[5]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 700:
                            monster_li.append('jinn[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 800:
                            monster_li.append('jinn[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 900:
                            monster_li.append('jinn[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 950:
                            monster_li.append('jinn[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 1000:
                            monster_li.append('jinn[5]')
                    elif current_loc == 'area_forest':
                        if dict_field_monster[current_loc]['hp'][k] <= 250:
                            monster_li.append('lizard[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 300:
                            monster_li.append('lizard[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 400:
                            monster_li.append('lizard[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 500:
                            monster_li.append('lizard[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 600:
                            monster_li.append('lizard[5]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 700:
                            monster_li.append('medusa[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 800:
                            monster_li.append('medusa[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 900:
                            monster_li.append('medusa[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 950:
                            monster_li.append('medusa[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 1000:
                            monster_li.append('medusa[5]')
                    elif current_loc == 'area_snow':
                        if dict_field_monster[current_loc]['hp'][k] <= 250:
                            monster_li.append('snow[1]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 300:
                            monster_li.append('snow[2]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 400:
                            monster_li.append('snow[3]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 500:
                            monster_li.append('snow[4]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 600:
                            monster_li.append('snow[5]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 700:
                            monster_li.append('snow[6]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 800:
                            monster_li.append('snow[7]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 900:
                            monster_li.append('snow[8]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 950:
                            monster_li.append('snow[9]')
                        elif dict_field_monster[current_loc]['hp'][k] <= 1000:
                            monster_li.append('snow[10]')
                    self.battle_dialog.append(
                        f"HP: {str(dict_field_monster[current_loc]['hp'][k])}의 {monster_li[k]}를 만났다!")
                    pixmap = QPixmap(f'../data/{current_loc}/{monster_li[k]}.png')
                    pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                    icon = QIcon()
                    icon.addPixmap(pixmap)
                    list_enemy_btn[k].setIcon(icon)
                    list_enemy_btn[k].setIconSize(QSize(100, 100))

            elif bool_meet_enemy_monster:
                self.battle_dialog.setText(f"{current_loc}층에서 벌어진 전투 시작!")
                for j in range(int_monster_count):
                    list_enemy_line[j].setText(f"몬스터 HP: {dict_maze_monster['list_hp'][j]}")
                    if dict_maze_monster['list_hp'][j] <= 250:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('small_dragon[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('dragon[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('lizard[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[1]')
                    elif dict_maze_monster['list_hp'][j] <= 300:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('small_dragon[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('dragon[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('lizard[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[2]')
                    elif dict_maze_monster['list_hp'][j] <= 400:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('small_dragon[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('dragon[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('lizard[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[3]')
                    elif dict_maze_monster['list_hp'][j] <= 500:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('small_dragon[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('dragon[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('lizard[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[4]')
                    elif dict_maze_monster['list_hp'][j] <= 600:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('small_dragon[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('dragon[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('lizard[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[5]')
                    elif dict_maze_monster['list_hp'][j] <= 700:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('demon[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('jinn[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('medusa[1]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[6]')
                    elif dict_maze_monster['list_hp'][j] <= 800:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('demon[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('jinn[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('medusa[2]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[7]')
                    elif dict_maze_monster['list_hp'][j] <= 900:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('demon[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('jinn[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('medusa[3]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[8]')
                    elif dict_maze_monster['list_hp'][j] <= 950:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('demon[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('jinn[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('medusa[4]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[9]')
                    elif dict_maze_monster['list_hp'][j] <= 1000:
                        if dict_maze_monster['list_area_monster'][j] == 'area_fire':
                            monster_li.append('demon[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_water':
                            monster_li.append('jinn[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_forest':
                            monster_li.append('medusa[5]')
                        elif dict_maze_monster['list_area_monster'][j] == 'area_snow':
                            monster_li.append('snow[10]')
                    self.battle_dialog.append(f"HP: {dict_maze_monster['list_hp'][j]}의 {monster_li[j]}를 만났다!")
                    pixmap = QPixmap(f'../data/{dict_maze_monster["list_area_monster"][j]}/{monster_li[j]}.png')
                    pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                    icon = QIcon()
                    icon.addPixmap(pixmap)
                    list_enemy_btn[j].setIcon(icon)
                    list_enemy_btn[j].setIconSize(QSize(100, 100))

    # 각 캐릭터의 [공격]버튼에 따른 누가/누구에게/nnn데미지 입었습니다. battle_dialog 메세지띄우기
    def monster_atk_choice(self, x, index, atk_job, selected_option,
                           monster_li, bool_meet_monster, bool_meet_enemy_monster,
                           dict_field_monster, dict_maze_monster, current_loc,
                           list_enemy_line, list_enemy_btn):
        name, damage = atk_job, selected_option
        self.battle_dialog.append(f"{name}이/가{monster_li[index]}을/를 공격해 {damage}데미지를 입혔다.")
        if bool_meet_monster == True:
            dict_field_monster[current_loc]['hp'][index] = dict_field_monster[current_loc]['hp'][index] - damage
            list_enemy_line[index].setText(f"몬스터 HP:{dict_field_monster[current_loc]['hp'][index]}")
            if dict_field_monster[current_loc]['hp'][index] <= 0:
                dict_field_monster[current_loc]['hp'][index] = 0
                list_enemy_line[index].setText(f"몬스터 HP:{dict_field_monster[current_loc]['hp'][index]}")
                list_enemy_btn[index].setDisabled(True)

        elif bool_meet_enemy_monster == True:
            dict_maze_monster['list_hp'][index] = dict_maze_monster['list_hp'][index] - damage
            list_enemy_line[index].setText(f"몬스터 HP:{dict_maze_monster['list_hp'][index]}")
            if dict_maze_monster['list_hp'][index] <= 0:
                dict_maze_monster['list_hp'][index] = 0
                list_enemy_line[index].setText(f"몬스터 HP:{dict_maze_monster['list_hp'][index]}")
                list_enemy_btn[index].setDisabled(True)

        QTimer.singleShot(2000, self.monster_atk)

    # 몬스터의 유저 수호대 (랜덤)공격 기능
    def monster_atk(self, str_job, dict_user_gard, monster_li,
                    dict_field_monster, dict_maze_monster, current_loc,
                    bool_meet_monster, bool_meet_enemy_monster):
        list_target = []
        for k in str_job:
            if dict_user_gard[k]['survival'] == True:
                list_target.append(k)
        int_monster_skill_c = random.randint(0, 1)
        int_monster_target_c = random.randint(0, len(list_target) - 1)
        atk_monster = random.randint(0, len(monster_li) - 1)
        if bool_meet_monster == True:
            # atk_monster = random.randint(0, len(self.dict_field_monster[self.current_loc]['hp']) - 1)
            monster_damage = dict_field_monster[current_loc]['skill'][int_monster_skill_c]
            if monster_damage[6] == 'a':
                dict_user_gard[list_target[int_monster_target_c]]['hp'] -= dict_field_monster[current_loc]['hp'][
                                                                               atk_monster] * 0.05
            elif monster_damage[6] == 'b':
                dict_user_gard[list_target[int_monster_target_c]]['hp'] -= dict_field_monster[current_loc]['hp'][
                                                                               atk_monster] * 0.1
                self.battle_dialog.append(f"""{current_loc}의 {monster_li[atk_monster]}가 {monster_damage}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!""")
            if dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! 우리의 {list_target[int_monster_target_c]}가 전투불능상태가 되었습니다.")
                QTimer.singleShot(1000, self.battle_monster)
            self.show_war_result()

        elif bool_meet_enemy_monster:
            monster_damage = dict_maze_monster['list_damage'][atk_monster]
            str_damage_name = dict_maze_monster['list_area_monster'][atk_monster].split('_')
            if monster_damage == 0.05:
                dict_user_gard[list_target[int_monster_target_c]]['hp'] -= dict_maze_monster['list_hp'][atk_monster] * \
                                                                           dict_maze_monster['list_damage'][atk_monster]
                str_damage_name = str_damage_name[1] + '_attack'
            elif monster_damage == 0.1:
                dict_user_gard[list_target[int_monster_target_c]]['hp'] -= dict_maze_monster['list_hp'][atk_monster] * \
                                                                           dict_maze_monster['list_damage'][atk_monster]
                str_damage_name = str_damage_name[1] + '_ball'
                self.battle_dialog.append(
                    f"""{dict_maze_monster['list_area_monster'][atk_monster]}의 {monster_li[atk_monster]}가 {str_damage_name}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!""")
            if dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! 우리의 {list_target[int_monster_target_c]}가 전투불능상태가 되었습니다.")
                QTimer.singleShot(1000, self.battle_monster)
            self.show_war_result()

    # -------------보스몬스터와의 전투----------------------------------------------------------------------------------------#

    # -------------전투+아이템(사용/획득)-------------------------------------------------------------------------------------#
    # 필드에서 일반몬스터 만났을때 승리한 후 아이템 얻는 함수
    def field_battle_get_items(self, str_area, bool_meet_monster, dict_field_monster):
        if bool_meet_monster and self.bool_war_result:
            int_mul = random.randint(1, 3)
            if str_area == 'area_fire':
                fire_cnt = dict_field_monster['area_fire']['int_cnt']
                list_fire_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                      'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                      'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                      'silver_helmet', 'bronze_armor', 'iron_shield', 'bronze_bow',
                                                      'red_glove', 'red_cape', 'bronze_pants'], k=fire_cnt * int_mul)
                return list_fire_drop_item
            elif str_area == 'area_water':
                water_cnt = dict_field_monster['area_water']['int_cnt']
                list_water_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                       'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                       'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                       'red_hood', 'bronze_shield', 'bronze_bow', 'red_glove',
                                                       'red_cape', 'red_pants'], k=water_cnt * int_mul)
                return list_water_drop_item
            elif str_area == 'area_forest':
                forest_cnt = dict_field_monster['area_forest']['int_cnt']
                list_forest_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                        'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                        'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                        'cow_helmet', 'cow_armor', 'leather_shield', 'stone_gem',
                                                        'bronze_wand', 'bronze_staff', 'cow_glove', 'cow_cape',
                                                        'cow_pants'], k=forest_cnt * int_mul)
                return list_forest_drop_item
            else:  # 'area_snow'인 경우
                snow_cnt = dict_field_monster['area_snow']['int_cnt']
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
    def maze_battle_get_items(self, bool_meet_maze_monster, dict_maze_monster):
        if (bool_meet_maze_monster == True) and (self.bool_war_result == True):
            int_mul = random.randint(1, 3)
            fire_cnt = dict_maze_monster['list_area_monster'].count('area_fire')
            list_fire_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                  'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                  'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                  'silver_helmet', 'bronze_armor', 'iron_shield', 'bronze_bow',
                                                  'red_glove', 'red_cape', 'bronze_pants'], k=fire_cnt * int_mul)
            water_cnt = dict_maze_monster['list_area_monster'].count('area_water')
            list_water_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                   'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                   'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                   'red_hood', 'bronze_shield', 'bronze_bow', 'red_glove',
                                                   'red_cape', 'red_pants'], k=water_cnt * int_mul)
            forest_cnt = dict_maze_monster['list_area_monster'].count('area_forest')
            list_forest_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                    'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                    'cow_helmet', 'cow_armor', 'leather_shield', 'stone_gem',
                                                    'bronze_wand', 'bronze_staff', 'cow_glove', 'cow_cape',
                                                    'cow_pants'], k=forest_cnt * int_mul)
            snow_cnt = dict_maze_monster['list_area_monster'].count('area_snow')
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
    def boss_battle_get_items(self, int_floor):
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
            if int_floor == 1:
                ratio = random.randint(1, 10)
                if ratio == 1:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif int_floor == 2:
                ratio = random.randint(1, 10)
                if ratio <= 2:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif int_floor == 3:
                ratio = random.randint(1, 10)
                if ratio <= 3:
                    list_boss_drop_item.extend(['revival_potion', 'clue_1'])
                else:
                    list_boss_drop_item.append('revival_potion')
                return list_boss_drop_item
            elif int_floor == 4:
                list_boss_drop_item.extend(['revival_potion', 'clue_2'])
                return list_boss_drop_item
            elif int_floor == 5:
                list_boss_drop_item.extend(['revival_potion', 'clue_3'])
                return list_boss_drop_item
            elif int_floor == 6:
                list_boss_drop_item.extend(['revival_potion', 'clue_4'])
                return list_boss_drop_item
            elif int_floor == 7:
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
    ex = Main()
    ex.show()
    app.exec_()
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
main = resource_path('../qt/boki_test.ui')
main_class = uic.loadUiType(main)[0]

second = resource_path('../qt/attack.ui')
second_class = uic.loadUiType(second)[0]

class MY(QMainWindow, main_class, second_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()

    ### 임시 변수 ###
        # self.lb_warrior1.hide()
        # self.lb_warrior2.hide()
        self.int_btn_clicked_cnt = 0 #수호대의 캐릭터 중 survival:True 수와 비교하여 버튼 활성화/비활성화를 체크하기 위함.
        self.int_survival = 0 #수호대 캐릭터 중 survival:True 숫자
        self.int_war_cnt = 0 #전투횟수

        self.list_area = ['area_fire', 'area_water', 'area_forest', 'area_snow']
        self.list_maze_floor = [1,2,3,4,5,6,7,8]
        # self.current_loc = random.choice(self.list_area)         #from시연님(값 받아오기)
        self.current_loc = random.choice(self.list_maze_floor)     #from시연님(값 받아오기)

        ## 필드 ##
        self.bool_meet_gard= False
        self.bool_meet_monster= False

        self.num = random.choice(range(1,11))
        self.dict_field_monster = {'area_fire': {'cnt': self.num,
                                                 'hp':random.choices(range(200,1001),k=self.num),
                                                 'skill': ['fire_attack', 'fire_ball']},
                                   'area_water': {'cnt': self.num,
                                                 'hp': random.choices(range(200, 1001), k=self.num),
                                                 'skill': ['aqua_attack', 'aqua_ball']},
                                   'area_forest': {'cnt': self.num,
                                                 'hp': random.choices(range(200, 1001), k=self.num),
                                                 'skill': ['air_attack', 'air_ball']},
                                   'area_snow': {'cnt': self.num,
                                                 'hp': random.choices(range(200, 1001), k=self.num),
                                                 'skill': ['ice_attack', 'snow_ball']}}

        ## 던전 ##
        self.bool_meet_maze_gard= False
        self.bool_meet_enemy_monster= True
        self.bool_meet_boss_monster= False

        # int_monster_count와 dict_maze_monster는 DungeonClass에서 상속받을 변수
        self.int_monster_count = random.randint(1, 10)
        self.dict_maze_monster = {'int_cnt': self.int_monster_count,
                                  'list_hp': random.sample(range(200, 1000), self.int_monster_count),
                                  'list_area_monster': random.choices(['area_fire', 'area_water', 'area_forest', 'area_snow'], k=self.int_monster_count),
                                  'list_damage': random.choices([0.05, 0.1], k=self.int_monster_count)}

    ### 변수 선언 ###
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
                               'swordsman': {'survival': True,
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
                               'wizard_white': {'survival': False,
                                                'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 100,
                                                'equipment': [],
                                                'skill': {1: 'heal_normal',
                                                          15: 'heal_greater',
                                                          30: 'heal_all'}}}
        self.str_job = []
        self.str_job.extend([sorted(self.dict_user_gard.keys())[4],'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white'])

        self.list_job_name = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']
        self.monster_li = []
        self.list_enemy_btn = []
        self.list_enemy_line = []
        self.list_enemy_btn = self.groupBox.findChildren(QPushButton)
        self.list_enemy_line = self.groupBox.findChildren(QLineEdit)

        ### qt object -> list화하기 위한 findchildren 필요한 구간 ###
        list_frame = self.findChildren(QFrame)[7:]

        list_enemy_btn = [self.enemy_0, self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4,
                          self.enemy_5, self.enemy_6, self.enemy_7, self.enemy_8, self.enemy_9]
        self.list_enemy_line = [self.hp_enemy_0,self.hp_enemy_1,self.hp_enemy_2,self.hp_enemy_3,self.hp_enemy_4,
                                self.hp_enemy_5,self.hp_enemy_6,self.hp_enemy_7,self.hp_enemy_8,self.hp_enemy_9]

        self.list_job_lb = [self.warrior_lb,self.archer_lb,self.swordsman_lb,
                            self.red_wizard_lb,self.black_wizard_lb,self.white_wizard_lb]
        self.list_attack_btn = [self.pb_atk_warrior,self.pb_atk_archer,self.pb_atk_swordsman,
                                self.pb_atk_wizard_red,self.pb_atk_wizard_black,self.pb_atk_wizard_white]

    ### qt 연결 ###
        for i in range(len(self.list_attack_btn)):
            self.list_attack_btn[i].clicked.connect(lambda x, y=i: self.atk_choice(x, y))
            self.list_attack_btn[i].clicked.connect(lambda x, y=i: self.move_image_forward(x, y))
            self.list_attack_btn[i].clicked.connect(lambda x, y=i: self.attack_btn_clicked(x, y))

        for i in range(6):
            # list_frame[i].findChildren(QPushButton)[2].clicked.connect(lambda x, y=i: self.skill_choice(x, y))
            list_frame[i].findChildren(QPushButton)[3].clicked.connect(self.user_gard_run)

        if self.bool_meet_monster == True:
            for i in range(self.num):
                list_enemy_btn[i].clicked.connect(lambda x, y=i: self.monster_choice(x, y))
        elif self.bool_meet_enemy_monster == True:
            for i in range(self.int_monster_count):
                list_enemy_btn[i].clicked.connect(lambda x, y=i: self.monster_choice(x, y))

        self.war_start.clicked.connect(self.battle_location)
        self.war_start.clicked.connect(self.equip_btn_disabled)

    ### 함수 선언 ###

    #전투결과(승패) 반환
    def show_war_result(self):
        died = 0
        if self.current_loc in self.list_area:
            if self.bool_meet_gard == True:
                print("if - 조우한 수호대의 모든 구성원이 hp가 0이라면 return self.war_result = True")
                print("elif - 유저 수호대의 모든 구성원의 hp가 0이라면 return self.war_result = False")
            elif self.bool_meet_monster == True:
                for c in range(self.num):
                    if self.dict_field_monster['hp'][c] == 0:
                        war_result = True
                        self.battle_dialog.append("일반몬스터와의 전투에서 승리했습니다!")
                    for d in self.str_job:
                        if self.dict_user_gard[d]['survival'] == False:
                            died += 1
                        if died == self.int_survival:
                            war_result = False
                            self.battle_dialog.append("일반몬스터와의 전투에서 패배했습니다..")
        if self.current_loc in self.list_maze_floor:
            if self.bool_meet_maze_gard == True:
                print("if - 조우한 수호대의 모든 구성원이 hp가 0이라면 return self.war_result = True")
                print("elif - 유저 수호대의 모든 구성원의 hp가 0이라면 return self.war_result = False")
            elif self.bool_meet_enemy_monster == True:
                for g in range(self.int_monster_count):
                    if self.dict_maze_monster['list_hp'][g] == 0:
                        war_result = True
                        self.battle_dialog.append("일반몬스터와의 전투에서 승리했습니다!")
                for h in self.str_job:
                    if self.dict_user_gard[h]['survival'] == False:
                        died += 1
                    if died == self.int_survival:
                        war_result = False
                        self.battle_dialog.append("일반몬스터와의 전투에서 패배했습니다..")
            elif self.bool_meet_boss_monster == True:
                print("if - 조우한 보스의 hp가 0이라면 return self.war_result = True, bool_boss_death = True")
                print("elif - 유저 수호대의 모든 구성원의 hp가 0이라면 return self.war_result = False")
        return war_result

    # 전투 횟수 카운트
    def war_cnt(self):
        war_result = self.war_win_or_lose
        if war_result == True:
            self.int_war_cnt += 1
        elif war_result == False:
            self.int_war_cnt += 1
        return self.int_war_cnt

    # 배틀 로케이션과 만난 적 확인 : 미구현된 부분은 주석처리함.
    def battle_location(self):
        if self.current_loc in self.list_area:
            if self.bool_meet_gard == True:
                self.battle_area_gard()
            elif self.bool_meet_monster == True:
                self.battle_monster()
        if self.current_loc in self.list_maze_floor:
            if self.bool_meet_maze_gard == True:
                self.battle_maze_gard()
            elif self.bool_meet_enemy_monster == True:
                self.battle_monster()
            elif self.bool_meet_boss_monster == True:
                self.battle_maze_boss()

    # [필드/던전]몬스터 조우 - 전투가능한 구성원의 [공격][스킬]버튼이 활성화
    def battle_monster(self):
        list_frame = self.findChildren(QFrame)[7:]
        for i in range(6):
            if self.str_job[i] in self.dict_user_gard.keys():
                if self.dict_user_gard[self.str_job[i]]['survival'] == True:
                    self.int_survival = i + 1
                    self.list_attack_btn[i].setEnabled(True)
                    list_frame[i].findChildren(QPushButton)[2].setEnabled(True)
                    list_frame[i].findChildren(QPushButton)[3].setEnabled(True)
                if self.dict_user_gard[self.str_job[i]]['survival'] == False:
                    self.list_attack_btn[i].setDisabled(True)
                    list_frame[i].findChildren(QPushButton)[2].setDisabled(True)
                    list_frame[i].findChildren(QPushButton)[3].setDisabled(True)

        if self.bool_meet_monster == True:
            area = self.current_loc.split('_')
            self.battle_dialog.setText(f"{area[0]}지역에서 벌어진 전투 시작!")
            for k in range(self.num):
                self.list_enemy_line[k].setText(f"몬스터 HP: {str(self.dict_field_monster[self.current_loc]['hp'][k])}")
                if self.current_loc == 'area_fire':
                    if self.dict_field_monster[self.current_loc]['hp'][k] <= 250:
                        self.monster_li.append('small_dragon[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 300:
                        self.monster_li.append('small_dragon[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 400:
                        self.monster_li.append('small_dragon[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 500:
                        self.monster_li.append('small_dragon[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 600:
                        self.monster_li.append('small_dragon[5]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 700:
                        self.monster_li.append('demon[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 800:
                        self.monster_li.append('demon[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 900:
                        self.monster_li.append('demon[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 950:
                        self.monster_li.append('demon[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 1000:
                        self.monster_li.append('demon[5]')
                elif self.current_loc == 'area_water':
                    if self.dict_field_monster[self.current_loc]['hp'][k] <= 250:
                        self.monster_li.append('dragon[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 300:
                        self.monster_li.append('dragon[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 400:
                        self.monster_li.append('dragon[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 500:
                        self.monster_li.append('dragon[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 600:
                        self.monster_li.append('dragon[5]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 700:
                        self.monster_li.append('jinn[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 800:
                        self.monster_li.append('jinn[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 900:
                        self.monster_li.append('jinn[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 950:
                        self.monster_li.append('jinn[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 1000:
                        self.monster_li.append('jinn[5]')
                elif self.current_loc == 'area_forest':
                    if self.dict_field_monster[self.current_loc]['hp'][k] <= 250:
                        self.monster_li.append('lizard[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 300:
                        self.monster_li.append('lizard[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 400:
                        self.monster_li.append('lizard[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 500:
                        self.monster_li.append('lizard[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 600:
                        self.monster_li.append('lizard[5]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 700:
                        self.monster_li.append('medusa[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 800:
                        self.monster_li.append('medusa[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 900:
                        self.monster_li.append('medusa[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 950:
                        self.monster_li.append('medusa[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 1000:
                        self.monster_li.append('medusa[5]')
                elif self.current_loc == 'area_snow':
                    if self.dict_field_monster[self.current_loc]['hp'][k] <= 250:
                        self.monster_li.append('snow[1]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 300:
                        self.monster_li.append('snow[2]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 400:
                        self.monster_li.append('snow[3]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 500:
                        self.monster_li.append('snow[4]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 600:
                        self.monster_li.append('snow[5]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 700:
                        self.monster_li.append('snow[6]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 800:
                        self.monster_li.append('snow[7]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 900:
                        self.monster_li.append('snow[8]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 950:
                        self.monster_li.append('snow[9]')
                    elif self.dict_field_monster[self.current_loc]['hp'][k] <= 1000:
                        self.monster_li.append('snow[10]')
                self.battle_dialog.append(
                    f"HP: {str(self.dict_field_monster[self.current_loc]['hp'][k])}의 {self.monster_li[k]}를 만났다!")
                pixmap = QPixmap(f'../data/{self.current_loc}/{self.monster_li[k]}.png')
                pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                icon = QIcon()
                icon.addPixmap(pixmap)
                self.list_enemy_btn[k].setIcon(icon)
                self.list_enemy_btn[k].setIconSize(QSize(100, 100))

        elif self.bool_meet_enemy_monster == True:
            self.battle_dialog.setText(f"{self.current_loc}층에서 벌어진 전투 시작!")
            for k in range(self.int_monster_count):
                self.list_enemy_line[k].setText(f"몬스터 HP: {self.dict_maze_monster['list_hp'][k]}")
                if self.dict_maze_monster['list_hp'][k] <= 250:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('small_dragon[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('dragon[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('lizard[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[1]')
                elif self.dict_maze_monster['list_hp'][k] <= 300:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('small_dragon[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('dragon[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('lizard[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[2]')
                elif self.dict_maze_monster['list_hp'][k] <= 400:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('small_dragon[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('dragon[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('lizard[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[3]')
                elif self.dict_maze_monster['list_hp'][k] <= 500:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('small_dragon[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('dragon[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('lizard[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[4]')
                elif self.dict_maze_monster['list_hp'][k] <= 600:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('small_dragon[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('dragon[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('lizard[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[5]')
                elif self.dict_maze_monster['list_hp'][k] <= 700:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('demon[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('jinn[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('medusa[1]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[6]')
                elif self.dict_maze_monster['list_hp'][k] <= 800:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('demon[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('jinn[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('medusa[2]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[7]')
                elif self.dict_maze_monster['list_hp'][k] <= 900:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('demon[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('jinn[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('medusa[3]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[8]')
                elif self.dict_maze_monster['list_hp'][k] <= 950:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('demon[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('jinn[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('medusa[4]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[9]')
                elif self.dict_maze_monster['list_hp'][k] <= 1000:
                    if self.dict_maze_monster['list_area_monster'][k] == 'area_fire':
                        self.monster_li.append('demon[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_water':
                        self.monster_li.append('jinn[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_forest':
                        self.monster_li.append('medusa[5]')
                    elif self.dict_maze_monster['list_area_monster'][k] == 'area_snow':
                        self.monster_li.append('snow[10]')
                self.battle_dialog.append(f"HP: {self.dict_maze_monster['list_hp'][k]}의 {self.monster_li[k]}를 만났다!")
                pixmap = QPixmap(f'../data/{self.dict_maze_monster["list_area_monster"][k]}/{self.monster_li[k]}.png')
                pixmap.scaled(QSize(200, 200), Qt.IgnoreAspectRatio)
                icon = QIcon()
                icon.addPixmap(pixmap)
                self.list_enemy_btn[k].setIcon(icon)
                self.list_enemy_btn[k].setIconSize(QSize(100, 100))

    # 한번 누른 구성원의 버튼은 몬스터의 턴이 끝날때 까지 비활성화된다. -> 몬스터의 턴 값 재정의
    def attack_btn_clicked(self, x, num):
        self.list_attack_btn[num].setEnabled(False)
        self.int_btn_clicked_cnt += 1
        if self.int_btn_clicked_cnt == self.int_survival:
            for i, job in enumerate(self.str_job):
                if self.dict_user_gard[job]['survival'] == True:
                    self.list_attack_btn[i].setEnabled(True)
                    self.int_btn_clicked_cnt = 0

    #전투화면으로 전환시 각 캐릭터의 [장비]버튼 setDisabled처리
    def equip_btn_disabled(self):
        list_frame = self.findChildren(QFrame)[7:]
        for i in range(6):
            list_job_btn = list_frame[i].findChildren(QPushButton)[1].setDisabled(True)

    # 전투화면으로 전환시 각 캐릭터의 [공격]버튼에 따른 QDialog창 생성
    def atk_choice(self,x,index):
        self.atk_job = self.sender().objectName()[7:]

        self.atk_dialog = QDialog()
        self.atk_dialog.setWindowTitle("ATTACK")

        radio_button1 = QRadioButton(f"물리공격(현재 공격력: {self.dict_user_gard[self.list_job_name[index]]['power']})")
        OK_button = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(radio_button1)
        layout.addWidget(OK_button)
        self.atk_dialog.setLayout(layout)

        if radio_button1.isChecked:
            self.selected_option = self.dict_user_gard[self.list_job_name[index]]['power']

        OK_button.clicked.connect(self.atk_dialog_close)
        self.atk_dialog.exec_()

        return self.atk_job, self.selected_option

    # 각 캐릭터의 [공격]버튼에 따른 QDialog창 닫기
    def atk_dialog_close(self):
        self.atk_dialog.close()

    # 각 캐릭터의 [공격]버튼에 따른 누가/누구에게/nnn데미지 입었습니다. battle_dialog 메세지띄우기
    def monster_choice(self, x, index):
        name, damage = self.atk_job, self.selected_option
        self.battle_dialog.append(f"{name}이/가{self.monster_li[index]}을/를 공격해 {damage}데미지를 입혔다.")
        if self.bool_meet_monster == True:
            self.dict_field_monster[self.current_loc]['hp'][index] = self.dict_field_monster[self.current_loc]['hp'][index] - damage
            self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster[self.current_loc]['hp'][index]}")
            if self.dict_field_monster[self.current_loc]['hp'][index] <= 0:
                self.dict_field_monster[self.current_loc]['hp'][index] = 0
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster[self.current_loc]['hp'][index]}")
                self.list_enemy_btn[index].setDisabled(True)

        elif self.bool_meet_enemy_monster == True:
            self.dict_maze_monster['list_hp'][index] = self.dict_maze_monster['list_hp'][index] - damage
            self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index]}")
            if self.dict_maze_monster['list_hp'][index] <= 0:
                self.dict_maze_monster['list_hp'][index] = 0
                self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_maze_monster['list_hp'][index]}")
                self.list_enemy_btn[index].setDisabled(True)
        QTimer.singleShot(2000, self.monster_atk)

    def monster_atk(self):
        list_target = []
        for k in self.str_job:
            if self.dict_user_gard[k]['survival'] == True:
                list_target.append(k)
        int_monster_skill_c = random.randint(0, 1)
        int_monster_target_c = random.randint(0, len(list_target) - 1)
        atk_monster = random.randint(0, len(self.monster_li) - 1)
        if self.bool_meet_monster == True:
            # atk_monster = random.randint(0, len(self.dict_field_monster[self.current_loc]['hp']) - 1)
            monster_damage = self.dict_field_monster[self.current_loc]['skill'][int_monster_skill_c]
            if monster_damage[6] == 'a':
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_field_monster[self.current_loc]['hp'][atk_monster] * 0.05
            elif monster_damage[6] == 'b':
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_field_monster[self.current_loc]['hp'][atk_monster] * 0.1
            self.battle_dialog.append(f"""{self.current_loc}의 {self.monster_li[atk_monster]}가 {monster_damage}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!""")
            if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                self.dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! 우리의 {self.dict_user_gard[list_target[int_monster_target_c]]}가 전투불능상태가 되었습니다.")
            self.show_war_result()
            self.battle_monster() #디버깅 필요 점심이후

        elif self.bool_meet_enemy_monster == True:
            monster_damage = self.dict_maze_monster['list_damage'][atk_monster]
            str_damage_name = self.dict_maze_monster['list_area_monster'][atk_monster].split('_')
            if monster_damage == 0.05:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_maze_monster['list_hp'][atk_monster] * self.dict_maze_monster['list_damage'][atk_monster]
                str_damage_name = str_damage_name[1] + '_attack'
            elif monster_damage == 0.1:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] -= self.dict_maze_monster['list_hp'][atk_monster] * self.dict_maze_monster['list_damage'][atk_monster]
                str_damage_name = str_damage_name[1] + '_ball'
            self.battle_dialog.append(f"""{self.dict_maze_monster['list_area_monster'][atk_monster]}의 {self.monster_li[atk_monster]}가 {str_damage_name}공격을 걸었다!
그 영향으로 {list_target[int_monster_target_c]}의 hp가 {self.dict_user_gard[list_target[int_monster_target_c]]['hp']:.1f}로 떨어졌다!""")
            if self.dict_user_gard[list_target[int_monster_target_c]]['hp'] <= 0:
                self.dict_user_gard[list_target[int_monster_target_c]]['hp'] = 0
                self.dict_user_gard[list_target[int_monster_target_c]]['survival'] = False
                self.battle_dialog.append(f"앗! 우리의 {self.dict_user_gard[list_target[int_monster_target_c]]}가 전투불능상태가 되었습니다.")
            self.show_war_result()
            self.battle_monster()

    # 각 캐릭터의 [공격]버튼에 따른 이미지 모션 주는 함수 2가지
    #1번 방식 : 캐릭터는 그자리 그대로, 모션만 주기
    # def move_image_forward(self):
        # QTimer.singleShot(800,self.lb_warrior0.hide)
        # QTimer.singleShot(800,self.lb_warrior1.show)
        # QTimer.singleShot(1600,self.lb_warrior1.hide)
        # QTimer.singleShot(1600,self.lb_warrior2.show)
        # QTimer.singleShot(2400,self.lb_warrior2.hide)
        # QTimer.singleShot(2400, self.lb_warrior0.show)

    #2번 방식 : 위치가 바뀌면서 모션 수행
    def move_image_forward(self,x,index):
        self.index = index
        self.current_pos = self.list_job_lb[index].pos()
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            self.list_job_lb[index].setPixmap(QPixmap(f'../data/{self.list_job_name[index]}/attack1.png'))
            self.list_job_lb[index].move(self.current_pos.x(), self.current_pos.y()-200)
            QTimer.singleShot(1000, self.move_image_forward2)
        return self.index

    def move_image_forward2(self):
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            self.list_job_lb[self.index].setPixmap(QPixmap(f'../data/{self.list_job_name[self.index]}/attack2.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y()-300)
            QTimer.singleShot(1000, self.move_image_back)
            self.timer.stop()
        return self.index

    def move_image_back(self):
        if self.current_pos.x() < 900:  # 원래 위치로 돌아가는 x 좌표
            self.list_job_lb[self.index].setPixmap(QPixmap(f'../data/{self.list_job_name[self.index]}/walk1.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y())
            self.timer.stop()

    # 전투화면으로 전환시 각 캐릭터의 [스킬]버튼에 따른 QDialog창 생성
    # [스킬]버튼을 누르면 각 직업에 맞는, 해당 직업의 레벨에 따른 스킬이름을 가진 라디오 버튼이 등장한다.
    # 라디오버튼을 누르면 캐릭터는 그에 맞는 mp소모 + 스킬효과가 battle_dialog와 mp창의 변화를 주어야한다.
    # 유저 구성원 1명을 고르는 경우 한번 더 Qdialog 생성해야할듯....
    # def skill_choice(self, x, job):
        # int_lv = self.dict_user_gard[self.str_job[job]]['lv']
        # self.skill_job = self.sender().objectName()[7:]
        #
        # self.skill_dialog = QDialog()
        # self.skill_dialog.setWindowTitle("SKILL")
        # layout = QVBoxLayout()
        #
        # # for i in range(len(self.dict_user_gard[self.str_job[job]]['skill'])):
        # #     radio_button = QRadioButton()
        # #     radio_button.setText(f"{self.dict_user_gard[self.str_job[job]]['skill'][int_lv]}")
        # #     layout.addWidget(radio_button)
        #
        # OK_button = QPushButton("OK")
        # layout.addWidget(OK_button)
        # self.skill_dialog.setLayout(layout)
        #
        # radio_btn_sender = self.sender()
    #     self.skill_dialog.exec_()
    #
    # # 각 캐릭터의 [스킬]버튼에 따른 QDialog창 닫기
    # def skill_dialog_close(self):
    #     self.skill_dialog.close()

    # 각 캐릭터의 [도망]버튼 클릭시 battle_dialog에 메세지를 띄운다. 확률에 따른 도망 성공/실패 -> 반환값(필드/전투화면)으로넘기기
    def user_gard_run(self):
        num = random.choice(range(1, 101))
        sucess_rate = list(range(0, 31))
        sucess_rate_num = random.choice(sucess_rate)
        if sucess_rate_num < num:
            self.battle_dialog.append(f"""{100 - sucess_rate_num}%확률로 도망에 실패했습니다.
전투화면이 유지됩니다.""")
            self.bool_run_mode = False
        elif sucess_rate_num >= num:
            self.battle_dialog.append(f"""{sucess_rate_num}%확률로 도망에 성공했습니다.
{self.current_loc}화면으로 돌아갑니다.""")
            self.bool_run_mode = True
            return self.bool_run_mode


    # bool_meet_maze_monster, bool_meet_monster
    # 필드에서 일반몬스터 만났을때 승리한 후 아이템 얻는 함수
    def field_battle_get_items(self, str_area, bool_meet_monster, bool_war_result, dict_field_monster):
        if bool_meet_monster and bool_war_result:
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
            else:   # 'area_snow'인 경우
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
    def maze_battle_get_items(self, bool_meet_maze_monster, bool_war_result, dict_maze_monster):
        if (bool_meet_maze_monster == True) and (bool_war_result == True):
            int_mul = random.randint(1, 3)
            fire_cnt = dict_maze_monster['list_area_monster'].count('area_fire')
            list_fire_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                  'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                  'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                  'silver_helmet', 'bronze_armor', 'iron_shield', 'bronze_bow',
                                                  'red_glove', 'red_cape', 'bronze_pants'], k=fire_cnt*int_mul)
            water_cnt = dict_maze_monster['list_area_monster'].count('area_water')
            list_water_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                   'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                   'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                   'red_hood', 'bronze_shield', 'bronze_bow', 'red_glove',
                                                   'red_cape', 'red_pants'], k=water_cnt*int_mul)
            forest_cnt = dict_maze_monster['list_area_monster'].count('area_forest')
            list_forest_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                    'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                    'cow_helmet', 'cow_armor', 'leather_shield', 'stone_gem',
                                                    'bronze_wand', 'bronze_staff', 'cow_glove', 'cow_cape',
                                                    'cow_pants'], k=forest_cnt*int_mul)
            snow_cnt = dict_maze_monster['list_area_monster'].count('area_snow')
            list_snow_drop_item = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                  'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                  'all_potion_high', 'all_potion_middle', 'all_potion_low',
                                                  'silver_helmet', 'chain_armor', 'red_armor', 'chain_shield',
                                                  'bronze_sword', 'low_chain_glove', 'cow_cape', 'chain_pants'], k=snow_cnt*int_mul)
            list_maze_battle_get_item = []
            list_maze_battle_get_item.extend(list_fire_drop_item)
            list_maze_battle_get_item.extend(list_water_drop_item)
            list_maze_battle_get_item.extend(list_forest_drop_item)
            list_maze_battle_get_item.extend(list_snow_drop_item)
            return list_maze_battle_get_item
        else:
            pass

    # 타수호대 전투 승리한 후 아이템 얻는 함수
    def gard_battle_get_items(self, bool_war_result):
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
        if bool_war_result:
            list_gard_battle_get_item = random.choices(list_all_items, k=6)
            return list_gard_battle_get_item
        else:
            pass

    # 보스 전투 승리한 후 얻는 함수
    def boss_battle_get_items(self, bool_war_result, int_floor):
        if bool_war_result:
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
    ex = MY()
    ex.show()
    app.exec_()
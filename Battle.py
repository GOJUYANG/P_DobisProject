from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

#전투화면은 QMainWindow의 stackedWidget에 해당한다.

#self.dict_ 의 key값은 def__init__(self, **kwargs)에서 찾을 값들이다. 함께 딕셔너리의 value값들은 기본값이 존재하지 않는다면 ''처리 해둔다.
#해당 딕셔너리에 key값들로 모여들 것들은 공통적으로 함께 묶여있어야할 값들이다. (ex, gard -> location -> warrior,archer,,,,,->lv,hp,max_hp,equipment,skill)

class Battle():
    def __init__(self, **kwargs):
        if 'gard' in kwargs:                              #수호대
            self.gard = kwargs['gard']

        if 'user_gard' in kwargs:                         #유저수호대{'gard':'', 'warrior':{'lv':,'HP',...'},}  +공격력
            self.user_gard = kwargs['user_gard']

        if 'location' in kwargs:                          #유저수호대 위치(필드/던전) {location: {field: ['fire', 'water', 'forest', 'snow']
            self.location = kwargs['location']            #                         ,dungeon: [1,2,3,4,5,6,7,8]}}

        if 'x' in kwargs:                                 #유저수호대 좌표값x
            self.x = kwargs['x']
        if 'y' in kwargs:                                 #유저수호대 좌표값x
            self.y = kwargs['y']

        if 'field_monster' in kwargs:
            self.field_monster = kwargs['field_monster']  #필드몬스터 {'fire_field_monster' : {'HP':'', 'cnt': , 'demage':['fire_ball', 'fire_wall']},
                                                          #           'water_field_monster' : {'HP':'', 'cnt': , 'demage':['aqua_ball', 'aqua_wall']},
                                                          #           'forest_field_monster' : {'HP':'', 'cnt': , 'demage':['air_ball', 'air_wall']},
                                                          #           'snow_field_monster' : {'HP':'', 'cnt': , 'demage':['ice_ball', 'snow_wall']}}

        if 'boss_monster' in kwargs:                      #보스몬스터{'이동려크': {'HP': '','demage':['fan_attack', 'hell_shouting'],'clue':0.1},
            self.boss_monster = kwargs['boss_monster']    #          '조동혀니' : {'HP': '','demage' = ['silent_attack', 'hell_feedback'],'clue':0.2},
                                                          #          '류홍거리' : {'HP': '','demage' = ['silent_attack', 'hell_feedback'],'clue':0.3},
                                                          #          '코로나악마공주' : {},'이땅복이' : {},'환생의 복이' : {},'로드오브보기' : {} }

        # if 'dungeon_monster' in kwargs:
        #     self.dungeon_monster = kwargs['dungeon_monster'] #던전몬스터는 필드몬스터에서 0~6 랜덤숫자 중 랜덤차출한다. +속성따라오기

        if 'mode' in kwargs:                              #전투모드{'war_possible_all':True, 'war_possible_part':True, 'war_impossible_part'=True}
            self.war_mode = kwargs['war_mode']
        if 'run_mode' in kwargs:                          #도망모드{'rate':30,'cnt': 5,'x': '','y':''}
            self.run_mode = kwargs['run_mode']

        if 'war_cnt' in kwargs:                           #전투횟수{10:1, 20:2, 30:3, 40:4, 50:5, 60:6, 70:7, 80:8, 90:9, 100:10}
            self.war_cnt = kwargs['war_cnt']

        if 'turn' in kwargs:                              #전투 턴{'enemy_turn':True, 'team_trun':True}
            self.turn = kwargs['turn']

        if 'item' in kwargs:                              #아이템 (포션사용)
            self.item = kwargs['item']
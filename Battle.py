from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

#self.dict_ 의 key값은 def__init__(self, **kwargs)에서 찾을 값들이다. 함께 딕셔너리의 value값들은 기본값이 존재하지 않는다면 ''처리 해둔다.
#해당 딕셔너리에 key값들로 모여들 것들은 공통적으로 함께 묶여있어야할 값들이다. (ex, gard -> location -> warrior,archer,,,,,->lv,hp,max_hp,equipment,skill)

### 클래스 화면 ###
#전투화면은 QMainWindow의 stackedWidget에 해당한다.

### 클래스 함수 ###
# 도망
# 받을 값 : 화면전환 후 위치할 필드/던전 좌표

# 턴제 방식
# 생성 값 : self.enemy_turn = True, self.team_turn = True

# 전투가능/불능 상태 판단
# 받을 값 : dict_user_gard_lv(job : lv)
# 넘겨줄 값 : dict_user_gard_state{'warrior':True,'archer':True,'swordsman':True,'wizard_W':True,'wizard_R':True,'wizard_B':True}

# 필드 일반 몬스터 조우
# 받을 값(1): str_area
# 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]
# 받을 값(3): dict_maze_monster[int_cnt, int_hp, list_area_monster, list_damage(일반공격, 스킬)]
# 넘겨줄 값 : int_war_cnt, bool_run_mode

# 필드 수호대 조우
# 받을 값(1): str_area
# 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]
# 받을 값(3): enemy_gard[name, lv, hp, mp, skill, power]
# 넘겨줄 값 : int_war_cnt, bool_run_mode

# 던전 일반몬스터 조우
# 받을 값(1): int_floor
# 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]
# 받을 값(3): dict_maze_monster[int_cnt, list_hp, list_area_monster, list_damage(일반공격, 스킬)]
# 넘겨줄 값 : int_war_cnt, bool_run_mode

# 던전 수호대 조우
# 받을 값(1): int_floor
# 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]
# 받을 값(3): enemy_gard[name, lv, hp, mp, skill, power]
# 넘겨줄 값: int_war_cnt, bool_run_mode

# 던전 보스몬스터 조우
# 받을 값(1): int_floor
# 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]
# 받을 값(3): dict_boss_monster[name, hp, attack, skill,list_field_monster:[int_cnt, list_hp, list_area]] ->area에 따른 기술사용은 BattleClass차원에서 처리?
# 넘겨줄 값 : int_war_cnt,bool_run_mode

# 승리/패배
# 필드 일반몬스터 상대
# 넘겨줄 값 : dict_result_field = {'win' : [lv, mp, hp, exp, skill, power, list_item(포션,지역별 장비)], 'lose' : ??}
# 필드 수호대 상대
# 넘겨줄 값 : dict_result_field = {'win' : [lv, mp, hp, exp, skill, power, list_item(포션,지역별 장비)], 'lose' : ??}
# 던전 일반몬스터 상대
# 넘겨줄 값 : dict_result_maze = {'win' : [lv, mp, hp, exp, skill, power, list_item(포션,지역별 장비)], 'lose' : ??}
# 던전 수호대 상대
# 넘겨줄 값 : dict_result_maze = {'win' : [lv, mp, hp, exp, skill, power, list_item(포션,장비)], 'lose' : ??}
# 던전 보스몬스터 상대
# 넘겨줄 값 : dict_result = {'win' : [lv, mp, hp, exp, skill, power, list_item(부활포션,단서,장비)], 'lose' : ??}

# 치트키 (n턴 동안 무적)

# 만렙달성 (레벨만 초기화 되고 self.job의 mp,hp,demage,skill,equipment는 그대로 전승)

class BattelClass():
    def __init__(self, **kwargs):
        if 'dict_user_gard' in kwargs:
            self.dict_user_gard = kwargs['dict_user_gard']


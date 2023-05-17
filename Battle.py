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
        self.current_loc = 'fire_area' #test용 (from 시연님 받아올값)
        self.int_btn_clicked_cnt = 0 #수호대의 캐릭터 중 survival:True 수와 비교하여 버튼 활성화/비활성화를 체크하기 위함.
        self.int_survival = 0 #수호대 캐릭터 중 survival:True 숫자
        self.int_war_cnt = 0 #전투횟수

        self.list_area = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        self.list_maze_floor = [1,2,3,4,5,6,7,8]
        self.num = random.choice(range(1,11))
        self.dict_field_monster = {'fire_area': {'survival': True,
                                                 'cnt': self.num,
                                                 'hp':random.choices(range(200,1001),k=self.num),
                                                 'skill': ['fire_attack', 'fire_ball']}}
        self.bool_meet_gard= False
        self.bool_meet_monster= True
        self.bool_meet_maze_gard= False
        self.bool_meet_enemy_monster= False
        self.bool_meet_boss_monster= False

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
        self.str_job.extend([sorted(self.dict_user_gard.keys())[4],
                             'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white'])

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

        self.war_start.clicked.connect(self.battle_location)
        self.war_start.clicked.connect(self.equip_btn_disabled)

        for i in range(self.num):
            list_enemy_btn[i].clicked.connect(lambda x, y=i: self.monster_choice(x, y))

    ### 함수 선언 ###

    #전투결과(승패) 반환
    # def war_result(self):
    #승리한다면 아이템 획득/bool_boss_death
    #패배한다면 각 캐릭터 전투가능상태 확인

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
                # self.battle_area_gard()
            elif self.bool_meet_monster == True:
                self.battle_monster()
        if self.current_loc in self.list_maze_floor:
            if self.bool_meet_maze_gard == True:
                # self.battle_maze_gard()
            elif self.bool_meet_enemy_monster == True:
                self.battle_monster()
            elif self.bool_meet_boss_monster == True:
                # self.battle_maze_boss()

    # 전투가능한 구성원의 [공격][스킬]버튼이 활성화
    def battle_monster(self):
        list_frame = self.findChildren(QFrame)[7:]
        area = self.current_loc.split('_')
        self.battle_dialog.setText(f"{area[0]}지역에서 벌어진 전투 시작!")

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

        for k in range(self.num):
            self.list_enemy_line[k].setText(f"몬스터 HP: {str(self.dict_field_monster['fire_area']['hp'][k])}")
            if self.dict_field_monster['fire_area']['hp'][k] < 400:
                self.monster_li.append('small_dragon')
            elif self.dict_field_monster['fire_area']['hp'][k] < 600:
                self.monster_li.append('lizard')
            elif self.dict_field_monster['fire_area']['hp'][k] < 800:
                self.monster_li.append('medusa')
            elif self.dict_field_monster['fire_area']['hp'][k] < 1000:
                self.monster_li.append('jinn')
            self.battle_dialog.append(
                f"HP: {str(self.dict_field_monster['fire_area']['hp'][k])}의 {self.monster_li[k]}를 만났다!")
            pixmap = QPixmap(f'../data/PNG/{self.monster_li[k]}.png')
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
        self.dict_field_monster[self.current_loc]['hp'][index] = self.dict_field_monster['fire_area']['hp'][index] - damage
        self.list_enemy_line[index].setText(f"몬스터 HP:{self.dict_field_monster[self.current_loc]['hp'][index]}")
        QTimer.singleShot(2000, self.monster_atk)
        if self.dict_field_monster[self.current_loc]['hp'][index] <= 0:
            self.list_enemy_btn[index].setDisabled(True)

    def monster_atk(self):
        atk_monster = random.randint(0, len(self.dict_field_monster[self.current_loc]['hp']) - 1)
        list_target = []
        for k in self.str_job:
            if self.dict_user_gard[k]['survival'] == True:
                list_target.append(k)
        int_monster_attack = random.randint(0, 1)
        int_monster_target = random.randint(0, len(list_target)-1)
        monster_damage = self.dict_field_monster[self.current_loc]['skill'][int_monster_attack]
        if monster_damage[6] == 'a':
            self.dict_user_gard[list_target[int_monster_target]]['hp'] -= self.dict_field_monster[self.current_loc]['hp'][atk_monster] * 0.05
        elif monster_damage[6] == 'b':
            self.dict_user_gard[list_target[int_monster_target]]['hp'] -= self.dict_field_monster[self.current_loc]['hp'][atk_monster] * 0.1
        self.battle_dialog.append(f"""{self.current_loc}의 {self.monster_li[atk_monster]}가 {monster_damage}공격을 걸었다!
그 영향으로 {list_target[random.randint(0, len(list_target))]}의 hp가 {self.dict_user_gard[list_target[int_monster_target]]['hp']:.1f}로 떨어졌다!""")

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MY()
    ex.show()
    app.exec_()
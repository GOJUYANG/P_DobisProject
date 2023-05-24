import os, sys
import random
import time

import keyboard
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.uic.properties import QtGui

#
# def resource_path(relative_path):
#     base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)
#
#
# # 메인화면
# main = resource_path('img_src/qt/this_is_boki_dialog.ui')
# main_class = uic.loadUiType(main)[0]


from view.this_is_boki_dialog import Ui_Dialog


class BattleClass(QDialog, Ui_Dialog):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()

        if 'bool_meet_gard' in kwargs:
            self.bool_meet_gard = kwargs['bool_meet_gard']
        if 'bool_meet_monster' in kwargs:
            self.bool_meet_monster = kwargs['bool_meet_monster']
        if 'bool_meet_maze_gard' in kwargs:
            self.bool_meet_maze_gard = kwargs['bool_meet_maze_gard']
        if 'bool_meet_enemy_monster' in kwargs:
            self.bool_meet_enemy_monster = kwargs['bool_meet_enemy_monster']
        if 'bool_meet_boss_monster' in kwargs:
            self.bool_meet_boss_monster = kwargs['bool_meet_boss_monster']
        if 'dict_user_gard' in kwargs:
            self.dict_user_gard = kwargs['dict_user_gard']
        if 'dict_field_monster' in kwargs:
            self.dict_field_monster = kwargs['dict_field_monster']
        if 'dict_maze_monster' in kwargs:
            self.dict_maze_monster = kwargs['dict_maze_monster']
        if 'int_floor' in kwargs:
            self.int_floor = kwargs['int_floor']
        if 'dict_enemy_gard' in kwargs:
            self.dict_enemy_gard = kwargs['dict_enemy_gard']
        if 'dict_boss_monster' in kwargs:
            self.dict_boss_monster = kwargs['dict_boss_monster']

        self.list_job = ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white']

        # 유저 수호대 ##
        self.dict_user_gard = {'gard': 'light_gard',
                               'location': {'region': '', 'x': 0, 'y': 0},
                               'warrior': {'survival': True,
                                           'lv': 20, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                           'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                         'bronze_sword'],
                                           'skill': {10: 'slice_chop'}},
                               'archer': {'survival': True,
                                          'lv': 20, 'hp': 150, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 300,
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
                                                'lv': 20, 'hp': 200, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 100,
                                                'equipment': [],
                                                'skill': {1: 'heal_normal',
                                                          10: 'hp_up',
                                                          15: ['heal_greater', 'mp_up'],
                                                          30: ['heal_all', 'map_find']}}}

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
        self.list_job_skill = [self.skill_btn_warrior_slice_chop,  # 0
                               self.skill_btn_archer_target_shot, self.skill_btn_archer_dual_shot,
                               self.skill_btn_archer_master_shot,
                               # 1~3
                               self.skill_btn_swordman_slice_chop,  # 4
                               self.skill_btn_wizard_red_heal_normal, self.skill_btn_wizard_red_heal_greater,
                               self.skill_btn_wizard_red_heal_all,
                               # 5~11
                               self.skill_btn_wizard_red_fire_ball, self.skill_btn_wizard_red_fire_wall,
                               self.skill_btn_wizard_red_thunder_breaker, self.skill_btn_wizard_red_bilzzard,
                               self.skill_btn_wizard_black_fire_ball, self.skill_btn_wizard_black_fire_wall,
                               self.skill_btn_wizard_black_thunder_breaker, self.skill_btn_wizard_black_bilzzard,
                               # 12~15
                               self.skill_btn_wizard_white_heal_normal, self.skill_btn_wizard_white_heal_greater,
                               self.skill_btn_wizard_white_heal_all,
                               # 16~21
                               self.skill_btn_wizard_white_hp_up, self.skill_btn_wizard_white_mp_up,
                               self.skill_btn_wizard_white_map_find]

        # 공격, 스킬 버튼 시그널
        for i in range(6):
            self.list_frame[i].findChildren(QPushButton)[0].clicked.connect(
                lambda x, y=i, z=self.list_frame[i].findChildren(QPushButton)[0]: self.atk_choice(x, y, z))
            self.list_frame[i].findChildren(QPushButton)[2].clicked.connect(
                lambda x, y=i, z=self.list_frame[i].findChildren(QPushButton)[2]: self.atk_choice(x, y, z))

        self.btn_goback.clicked.connect(self.goback)

        # 몬스터 클릭
        for btn in self.list_enemy_btn:
            btn.clicked.connect(lambda x, y=btn: self.clicked_monster(y))

    def goback(self):
        self.list_attack_btn[self.stackedWidget.currentIndex() - 1].setEnabled(True)
        self.list_skill_btn[self.stackedWidget.currentIndex() - 1].setEnabled(True)
        self.int_btn_clicked_cnt = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(0)

    def clicked_monster(self, button):
        for btn in self.list_enemy_btn:
            try:
                if btn != button:
                    btn.setChecked(False)
            except:
                pass

    def clicked_monster_clear(self):
        for btn in self.list_enemy_btn:
            btn.setChecked(False)

    def atk_choice(self, x, index, button):

        isMonsterClicked = False
        for btn in self.list_enemy_btn:
            if btn.isChecked():
                isMonsterClicked = True
                break

        if not isMonsterClicked:
            msg = QMessageBox()
            msg.critical(self, "몬스터 선택", "공격할 몬스터를 선택해주세요!", msg.Ok)

        else:
            if button.text() == '공격':
                self.atk_dialog = QDialog(self)
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
                self.attack_btn_clicked(x, index)
                self.move_image_forward(x, index)

            elif button.text() == '스킬':
                self.attack_btn_clicked(x, index)
                self.skill_widget_open(x, index)

        self.clicked_monster_clear()

    def atk_dialog_close(self):
        self.atk_dialog.close()

    # 위치가 바뀌면서 모션 수행
    def move_image_forward(self, x, index):
        self.index = index
        self.current_pos = self.list_job_lb[self.index].pos()
        print(self.current_pos)
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.)
            self.list_job_lb[self.index].setPixmap(QPixmap(f'img_src/{self.list_job[self.index]}/attack1.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y() - 200)
            QTimer.singleShot(300, self.move_image_forward2)
            # self.timer.stop()
        return self.index

    def move_image_forward2(self):
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error 발생시 화면크기에 맞춰 좌표 숫자 조정필요.
            self.list_job_lb[self.index].setPixmap(QPixmap(f'img_src/{self.list_job[self.index]}/attack2.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y() - 300)
            QTimer.singleShot(300, self.move_image_back)
            # self.timer.stop()
        return self.index

    def move_image_back(self):
        if self.current_pos.x() < 900:  # 원래 위치로 돌아가는 x 좌표
            self.list_job_lb[self.index].setPixmap(QPixmap(f'img_src/{self.list_job[self.index]}/walk1.png'))
            self.list_job_lb[self.index].move(self.current_pos.x(), self.current_pos.y())
            self.timer.stop()

    # 한번 누른 구성원의 [공격]버튼은 적의 턴이 끝날때 까지 비활성화.
    def attack_btn_clicked(self, x, index):
        if not x:
            self.list_attack_btn[index].setEnabled(False)
            self.list_skill_btn[index].setEnabled(False)
            self.int_btn_clicked_cnt = index + 1
        for i, job in enumerate(self.list_job):
            if self.dict_user_gard[job]['survival']:
                self.int_survival = i
        if self.int_btn_clicked_cnt == self.int_survival + 1:
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
            self.movie = QMovie('img_src/wizard_red/skill2.gif', QByteArray(), self)
            self.gif_3_1.setMovie(self.movie)
            self.movie.start()
        for i in range(6):
            list_gif_lb.append(getattr(self, f"gif_{i}"))
            self.list_skill_btn.append(getattr(self, f"pb_skill_job_{self.list_job[i]}"))
            self.movie = QMovie(f'img_src/{self.list_job[i]}/skill.gif', QByteArray(), self)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BattleClass()
    ex.show()
    app.exec_()

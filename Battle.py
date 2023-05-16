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
        self.current_loc = 'fire_area'
        self.int_btn_clicked_cnt = 0
        self.int_survive = 0

        ### 변수 선언 ###
        self.list_area = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        self.list_maze_floor = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh', 'eighth']

        self.list_attack_btn = [self.warrior_attack, self.archer_attack, self.swordsman_attack,
                                self.wizard_r_attack, self.wizard_w_attack, self.wizard_b_attack]

        self.dict_job = {'warrior': {'survive': True}, 'archer': {'survive': False}, 'swordsman': {'survive': True},
                         'wizard_w': {'survive': True}, 'wizard_b': {'survive': True}, 'wizard_r': {'survive': True}}
        self.str_job = sorted(self.dict_job.keys())

        self.num = random.choice(range(1, 11))
        self.dict_field_monster = {'fire_area': {'survival': True,
                                                 'cnt': self.num,
                                                 'hp': random.choices(range(200, 1001), k=self.num),
                                                 'skill': {'fire_attack', 'fire_ball'}}}
        self.monster_li = []
        self.list_enemy_btn = []
        self.list_enemy_line = []
        self.list_enemy_btn = self.groupBox.findChildren(QPushButton)
        self.list_enemy_line = self.groupBox.findChildren(QLineEdit)

        self.list_job = [self.lb_warrior, self.lb_archer, self.lb_swordsman, self.lb_wizard_r, self.lb_wizard_w,
                         self.lb_wizard_b]
        self.list_job_name = ['lb_warrior', 'lb_archer', 'lb_swordsman', 'lb_wizard_r', 'lb_wizard_w', 'lb_wizard_b']
        list_job_attack_btn = [self.warrior_attack, self.archer_attack, self.swordsman_attack,
                               self.wizard_r_attack, self.wizard_w_attack, self.wizard_b_attack]

        ### qt 연결 ###
        for i in range(len(list_job_attack_btn)):
            list_job_attack_btn[i].clicked.connect(lambda x, y=i: self.move_image_forward(x, y))
            self.pushButton.clicked.connect(lambda x, y=i: self.battle_turn(x, y))
            self.list_attack_btn[i].clicked.connect(lambda x, y=i: self.attack_btn_clicked(x, y))

        self.run_btn_0.clicked.connect(self.user_gard_run)

        for i in range(0, 9):
            self.enemy_0.clicked.connect(self.monster_attack)

    ### 함수 선언 ###

    # 1번 방식 : 캐릭터는 그자리 그대로, 모션만 주기
    # def move_image_forward(self):
    # QTimer.singleShot(800,self.lb_warrior0.hide)
    # QTimer.singleShot(800,self.lb_warrior1.show)
    # QTimer.singleShot(1600,self.lb_warrior1.hide)
    # QTimer.singleShot(1600,self.lb_warrior2.show)
    # QTimer.singleShot(2400,self.lb_warrior2.hide)
    # QTimer.singleShot(2400, self.lb_warrior0.show)

    # 2번 방식 : 위치가 바뀌면서 모션 수행
    def move_image_forward(self, x, index):
        self.index = index
        self.current_pos = self.list_job[index].pos()
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error가 난다면 숫자조정필요.)
            print(self.current_pos.x())
            print(self.current_pos.y())
            self.list_job[index].setPixmap(QPixmap(f'../data/{self.list_job_name[index]}/attack1.png'))
            self.list_job[index].move(self.current_pos.x(), self.current_pos.y() - 200)
            QTimer.singleShot(1000, self.move_image_forward2)
        return self.index

    def move_image_forward2(self):
        # index = self.move_image_forward(self.x, self.index)
        if self.current_pos.x() < 1000:  # 이동할 최종 위치 (x 좌표 :error가 난다면 숫자조정필요.)
            self.list_job[self.index].setPixmap(QPixmap(f'../data/{self.list_job_name[self.index]}/attack2.png'))
            self.list_job[self.index].move(self.current_pos.x(), self.current_pos.y() - 300)
            QTimer.singleShot(1000, self.move_image_back)
            self.timer.stop()
        return self.index

    def move_image_back(self):
        # index = self.move_image_forward2()
        if self.current_pos.x() < 900:  # 원래 위치로 돌아가는 x 좌표
            self.list_job[self.index].setPixmap(QPixmap(f'../data/{self.list_job_name[self.index]}/walk1.png'))
            self.list_job[self.index].move(self.current_pos.x(), self.current_pos.y())
            self.timer.stop()

    def monster_attack(self):
        self.battle_dialog.append("두번째 몬스터가 전사에게 **데미지를 먹었습니다.")

    # 전투가능한 구성원의 버튼이 활성화된다.
    def battle_turn(self, x, num):
        if self.current_loc in self.list_area:
            area = self.current_loc.split('_')
            self.battle_dialog.setText(f"{area[0]}지역에서 벌어진 전투 시작!")
        elif self.current_loc in self.list_maze_floor:
            self.battle_dialog.setText(f"{self.current_loc}층에서 벌어진 전투 시작!")

        for i in range(num):
            if self.str_job[i] in self.dict_job:
                if self.dict_job[self.str_job[i]]['survive'] == True:
                    self.list_attack_btn[num].setEnabled(True)
                    self.int_survive = i + 1
                if self.dict_job[self.str_job[i]]['survive'] == False:
                    self.list_attack_btn[num].setDisabled(True)

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

    # def enemy_btn_clicked(self):

    # 한번 누른 구성원의 버튼은 몬스터의 턴이 끝날때 까지 비활성화된다. -> 몬스터의 턴 값 재정의
    def attack_btn_clicked(self, x, num):
        self.list_attack_btn[num].setEnabled(x)
        self.int_btn_clicked_cnt += 1
        if self.int_btn_clicked_cnt == self.int_survive:
            for i, str_job in enumerate(self.dict_job):
                if self.dict_job[str_job]['survive'] == True:
                    self.list_attack_btn[i].setDisabled(x)
                    self.int_btn_clicked_cnt = 0

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

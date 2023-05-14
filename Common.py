from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

from Dialog import CustomDialog as cd


class Common():
    def __init__(self, **kwargs):
        # 방향
        if 'direction' in kwargs:
            self.directon = kwargs['direction']
        # 열
        if 'x' in kwargs:
            self.x = kwargs['x']
        # 행
        if 'y' in kwargs:
            self.y = kwargs['y']
        # 수호대 구성원 클래스
        if 'job' in kwargs:
            self.job = kwargs['job']
        # 아이템(소모품)
        if 'item' in kwargs:
            self.item = kwargs['item']
        # 수호대가 위치한 지역
        if 'region' in kwargs:
            self.region = kwargs['region']
        # 치트키
        if 'cheatkey' in kwargs:
            self.cheatkey = kwargs['cheatkey']
        # 수호대
        if 'dict_gard' in kwargs:
            self.dict_grad_stat = kwargs['dict_gard']
        # 직업리스트
        if 'list_job' in kwargs:
            self.list_job = kwargs['list_job']
        # 수호대 리스트
        if 'list_gard' in kwargs:
            self.list_gard = kwargs['list_gard']
        # 필드 리스트
        if 'list_field' in kwargs:
            self.list_field = kwargs['list_field']

    # 수호대 랜덤배치
    def random_assign_gard(self, dict_gard):
        dict_gard['gard'] = random.choice(self.list_gard)

    # 필드(집결지) 랜덤배치
    def random_assign_field(self):
        self.region = random.choice(self.list_field)
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.dict_grad_stat['location'] = {'region': self.region, 'x': self.x, 'y': self.y}

    # 이동
    def move_by_direction(self):
        if self.directon.upper() == 'U':
            self.y -= 1
        elif self.directon.upper() == 'D':
            self.y += 1
        elif self.directon.upper() == 'L':
            self.x -= 1
        elif self.directon.upper() == 'R':
            self.x += 1
        elif self.directon.upper() == 'LU':
            self.x -= 1
            self.y += 1
        elif self.directon.upper() == 'RU':
            self.x += 1
            self.y += 1
        elif self.directon.upper() == 'LD':
            self.x -= 1
            self.y += 1
        elif self.directon.upper() == 'RD':
            self.x += 1
            self.y += 1

        # self.dict_grad_stat['location'] = {'region': self.region, 'x': self.x, 'y': self.y}
        return self.dict_grad_stat['location']

    # 체력회복
    def use_hp_potion(self):
        if self.item == 'HP_potion_high':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.7
        elif self.item == 'HP_potion_middle':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.5
        elif self.item == 'HP_potion_low':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.3
        return self.dict_grad_stat[self.job]['HP']

    # 마나회복
    def use_mp_potion(self):
        if self.item == 'MP_potion_high':
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.7
        elif self.item == 'MP_potion_middle':
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.5
        elif self.item == 'MP_potion_low':
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.3
        return self.dict_grad_stat[self.job]['MP']

    # 체력,마나회복
    def use_all_potion(self):
        if self.item == 'All_potion_high':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.7
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.7
        elif self.item == 'All_potion_middle':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.5
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.5
        elif self.item == 'All_potion_low':
            self.dict_grad_stat[self.job]['HP'] += self.dict_grad_stat[self.job]['Max_HP'] * 0.3
            self.dict_grad_stat[self.job]['MP'] += self.dict_grad_stat[self.job]['Max_MP'] * 0.3
        return self.dict_grad_stat[self.job]['HP'], self.dict_grad_stat[self.job]['MP']

    # 전투불능 상태인 클래스 중 사용자가 선택한 클래스에 부활포션 사용
    def revival_guardian(self):
        if not self.dict_grad_stat[self.job]['survival']:
            self.dict_grad_stat[self.job]['survival'] = True

    # 텐트 사용: 전투불능인 구성원 모두가 되살아나고 구성원 전부 체력 100% 회복
    def use_tent(self):
        for job in self.list_job:
            self.dict_grad_stat[job]['survival'] = True
            self.dict_grad_stat[job]['hp'] = self.dict_grad_stat[job]['max_hp']

    # 타 수호대와의 조우
    def meet_other_guardian(self):
        # 우리 수호대 제외
        self.list_gard.remove(self.dict_grad_stat['gard'])
        # 리스트 셔플
        random.shuffle(self.list_gard)
        other_gard = self.list_gard.pop()
        return other_gard

    # 치트키
    def use_cheatkey(self):
        if self.cheatkey == 'easter_egg':
            pass

# # 위치값 확인
# Common(direction='u', x=1, y=1).move_by_direction()
#
# # 랜덤배치 확인
# a = Common(region='')
# # 수호대 랜덤배치
# a.random_assign_gard()
# # 필드 랜덤배치
# a.random_assign_field()
#
# for k, v in a.dict_grad_stat.items():
#     print(f'{k}:{v}')
# # print(a.dict_grad_stat)

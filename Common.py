from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

from Dialog import CustomDialog as cd

class Common():
    def __init__(self, **kwargs):
        if 'direction' in kwargs:
            self.directon = kwargs['direction']
        if 'job' in kwargs:
            self.job = kwargs['job']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
        if 'item' in kwargs:
            self.item = kwargs['item']
        if 'guardian' in kwargs:
            self.guardian = kwargs['guardian']

        self.guardian_list = ['light', 'moon', 'star', 'land']

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

        return self.x, self.y

    # 체력회복
    def use_hp_potion(self):
        if self.item == 'HP_potion_high':
            self.job['HP'] += self.job['Max_HP'] * 0.7
        elif self.item == 'HP_potion_middle':
            self.job['HP'] += self.job['Max_HP'] * 0.5
        elif self.item == 'HP_potion_low':
            self.job['HP'] += self.job['Max_HP'] * 0.3
        return self.job['HP']

    # 마나회복
    def use_mp_potion(self):
        if self.item == 'MP_potion_high':
            self.job['MP'] += self.job['Max_MP'] * 0.7
        elif self.item == 'MP_potion_middle':
            self.job['MP'] += self.job['Max_MP'] * 0.5
        elif self.item == 'MP_potion_low':
            self.job['MP'] += self.job['Max_MP'] * 0.3
        return self.job['MP']

    # 체력,마나회복
    def use_all_potion(self):
        if self.item == 'All_potion_high':
            self.job['HP'] += self.job['Max_HP'] * 0.7
            self.job['MP'] += self.job['Max_MP'] * 0.7
        elif self.item == 'All_potion_middle':
            self.job['HP'] += self.job['Max_HP'] * 0.5
            self.job['MP'] += self.job['Max_MP'] * 0.5
        elif self.item == 'All_potion_low':
            self.job['HP'] += self.job['Max_HP'] * 0.3
            self.job['MP'] += self.job['Max_MP'] * 0.3
        return self.job['HP'], self.job['MP']

    # 부활포션 사용
    def revival_guardian(self):
        for k, v in self.guardian.items():
            if not v['survival']:
                v['survival'] = True

    # 텐트 사용
    def use_tent(self):
        for k, v in self.guardian.items():
            v['HP'] = v['Max_HP']

    # 타 수호대와의 조우
    def meet_other_guardian(self):
        # 우리 수호대 제외
        self.guardian_list.remove(self.guardian['name'])
        # 리스트 셔플
        random.shuffle(self.guardian_list)
        guardian = self.guardian_list.pop()
        return guardian

    # 아이템 드랍
    def


x, y = Common(direction='u', x=1, y=1).MoveByDirection()
print(x, y)

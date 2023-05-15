from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

from Dialog import CustomDialog as cd


class CommonClass():
    def __init__(self, **kwargs):
        # 방향
        if 'direction' in kwargs:
            self.str_directon = kwargs['direction']
        # 열
        if 'int_x' in kwargs:
            self.int_x = kwargs['int_x']
        # 행
        if 'int_y' in kwargs:
            self.int_y = kwargs['int_y']
        # 수호대 구성원 클래스
        if 'str_job' in kwargs:
            self.str_job = kwargs['str_job']
        # 아이템(소모품)
        if 'str_item' in kwargs:
            self.str_item = kwargs['str_item']
        # 수호대가 위치한 지역
        if 'str_region' in kwargs:
            self.str_region = kwargs['str_region']
        # 치트키
        if 'str_cheatkey' in kwargs:
            self.str_cheatkey = kwargs['str_cheatkey']
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

        # 수호대 리스트
        self.list_gard = ['light_gard', 'moon_gard', 'star_gard', 'earth_gard']

        # 필드 리스트
        self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']

    # 수호대 랜덤배치
    def random_assign_gard(self, dict_gard):
        dict_gard['gard'] = random.choice(self.list_gard)

    # 필드(집결지) 랜덤배치
    def random_assign_field(self):
        self.str_region = random.choice(self.list_field)
        self.int_x = random.randint(1, 20)
        self.int_y = random.randint(1, 20)
        return self.int_x, self.int_y


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
        if self.str_cheatkey == 'easter_egg':
            pass



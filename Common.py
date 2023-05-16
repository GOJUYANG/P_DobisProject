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
        if 'dict_user_grad' in kwargs:
            self.dict_grad_stat = kwargs['dict_user_grad']
        # 직업리스트
        if 'list_job' in kwargs:
            self.list_job = kwargs['list_job']
        # 수호대 리스트
        if 'list_gard' in kwargs:
            self.list_gard = kwargs['list_gard']
        # 필드 리스트
        if 'list_field' in kwargs:
            self.list_field = kwargs['list_field']







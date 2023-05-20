import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from view.equipment import Ui_Equipment
from Dialog import *


class EquipmentClass(QDialog, Ui_Equipment):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        if 'str_job' in kwargs:
            self.str_job = kwargs['str_job']

        if 'str_equipment' in kwargs:
            self.str_equipment = kwargs['str_equipment']

        if 'dict_user_gard' in kwargs:
            self.dict_user_gard = kwargs['dict_user_gard']

        if 'dict_equip' in kwargs:
            self.dict_equip = kwargs['dict_equip']

        # 직업별 착용가능 장비리스트
        self.dict_job_equip = {
            'warrior': ['silver_helmet', 'gold_helmet',
                        'bronze_armor', 'silver_armor', 'gold_armor',
                        'bronze_shield', 'iron_shield', 'chain_shield', 'leather_shield',
                        'bronze_sword', 'silver_sword', 'gold_sword',
                        'low_chain_glove', 'middle_chain_glove', 'high_chain_glove',
                        'cow_cape', 'horse_cape', 'croc_cape', 'red_cape', 'blue_cape', 'black_cape',
                        'bronze_pants', 'silver_pants', 'gold_pants'],
            'archer': ['cow_helmet', 'horse_helmet',
                       'cow_armor', 'horse_armor',
                       'bronze_bow', 'silver_bow', 'gold_bow',
                       'cow_glove', 'horse_glove', 'croc_glove',
                       'cow_cape', 'horse_cape', 'croc_cape', 'red_cape', 'blue_cape', 'black_cape',
                       'cow_pants', 'horse_pants'],
            'swordman': ['cow_helmet', 'horse_helmet',
                          'chain_armor', 'iron_armor',
                          'bronze_sword', 'silver_sword', 'gold_sword',
                          'cow_glove', 'horse_glove', 'croc_glove',
                          'cow_cape', 'horse_cape', 'croc_cape',
                          'chain_pants', 'iron_pants'],
            'wizard_red': ['cow_helmet', 'horse_helmet',
                           'cow_armor', 'horse_armor',
                           'chain_shield',
                           'stone_gem', 'ruby_gem', 'diamond_gem',
                           'cow_glove', 'horse_glove', 'croc_glove',
                           'cow_cape', 'horse_cape', 'croc_cape', 'red_cape', 'blue_cape', 'black_cape',
                           'cow_pants', 'horse_pants'],
            'wizard_black': ['red_hood', 'blue_hood',
                             'red_armor', 'blue_armor', 'black_armor',
                             'leather_shield',
                             'bronze_staff', 'silver_staff', 'gold_staff',
                             'red_glove', 'blue_glove', 'black_glove',
                             'cow_cape', 'horse_cape', 'croc_cape', 'red_cape', 'blue_cape', 'black_cape',
                             'red_pants', 'blue_pants', 'black_pants', ],
            'wizard_white': ['red_hood', 'blue_hood',
                             'red_armor', 'blue_armor', 'black_armor',
                             'leather_shield',
                             'bronze_wand', 'silver_wand', 'gold_wand',
                             'red_glove', 'blue_glove', 'black_glove',
                             'cow_cape', 'horse_cape', 'croc_cape', 'red_cape', 'blue_cape', 'black_cape',
                             'red_pants', 'blue_pants', 'black_pants', ]}

        # 장비창 갱신
        self.show_wear_equip()
        self.show_can_wear_equip()

        # 시그널
        self.pb_wear.clicked.connect(self.wear_equip)
        self.pb_unworn.clicked.connect(self.urworn_equip)

    # 클래스 별 착용한 장비 보여주기
    def show_wear_equip(self):
        for item in self.dict_user_gard[self.str_job]['equipment']:
            for k, v in self.dict_equip.items():
                if k == item:
                    item = QListWidgetItem(f"{v['name']}")
                    item.setIcon(QIcon(f"{v['image']}"))
                    self.list_wear.addItem(item)

    # 획득한 장비 중 직업별 착용 가능 장비 보여주기
    def show_can_wear_equip(self):
        for item in self.dict_job_equip[self.str_job]:
            for k, v in self.dict_equip.items():
                if k == item and v['count'] > 0:
                    item = QListWidgetItem(f"{v['name']} : {v['count']}개")
                    item.setIcon(QIcon(f"{v['image']}"))
                    self.list_unworn.addItem(item)

    # 장비 착용
    def wear_equip(self):
        isDouble = False
        if self.list_unworn.currentItem() is not None:
            item = self.list_unworn.currentItem().text().split(':')[0].strip()

            if self.list_wear.count() > 0:
                # 중복 확인
                for index in range(self.list_wear.count()):
                    if item == self.list_wear.item(index).text():
                        isDouble = True
                        break
            else:
                pass

            if not isDouble:
                # 착용해제 리스트에서 장비 빼기
                for k, v in self.dict_equip.items():
                    if v['name'] == item:
                        self.dict_user_gard[self.str_job]['equipment'].append(k)
                        print((100 + v['max_hp']) / 100)
                        self.dict_user_gard[self.str_job]['max_hp'] *= (100 + v['max_hp']) / 100
                        self.dict_user_gard[self.str_job]['max_mp'] *= (100 + v['max_mp']) / 100
                        self.dict_user_gard[self.str_job]['power'] *= (100 + v['power']) / 100
                        self.dict_equip[k]['count'] -= 1
                        break
                self.renew_equip_view()
            else:
                dlg = CustomDialog('같은 장비를 중복착용 할 수 없습니다!')
                dlg.exec_()
        else:
            pass

    # 장비 해제
    def urworn_equip(self):
        if self.list_wear.currentItem() is not None:
            item = self.list_wear.currentItem().text()

            # 착용 리스트에서 장비 빼기
            for k, v in self.dict_equip.items():
                if v['name'] == item:
                    self.dict_user_gard[self.str_job]['equipment'].remove(k)
                    self.dict_user_gard[self.str_job]['hp'] /= (100 + v['max_hp']) / 100
                    self.dict_user_gard[self.str_job]['max_hp'] /= (100 + v['max_hp']) / 100
                    self.dict_user_gard[self.str_job]['mp'] /= (100 + v['max_mp']) / 100
                    self.dict_user_gard[self.str_job]['max_mp'] /= (100 + v['max_mp']) / 100
                    self.dict_user_gard[self.str_job]['power'] /= (100 + v['power']) / 100
                    self.dict_equip[k]['count'] += 1
                    break

            self.renew_equip_view()
        else:
            pass

    # 장비창 갱신
    def renew_equip_view(self):
        self.list_wear.clear()
        self.list_unworn.clear()
        self.show_wear_equip()
        self.show_can_wear_equip()

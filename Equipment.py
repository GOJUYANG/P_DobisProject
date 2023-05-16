import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from view.equipment import Ui_Equipment


class EquipmentClass(QDialog, Ui_Equipment):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 획득한 장비 리스트
        self.dict_equipment = {
            'black_armor': ['블랙 아머', 0],
            'black_cape': ['블랙 망토', 0],
            'black_glove': ['블랙 글로브', 0],
            'black_pants': ['블랙 팬츠', 0],
            'blue_armor': ['블루 아머', 0],
            'blue_cape': ['블루 망토', 0],
            'blue_glove': ['블루 글로브', 0],
            'blue_hood': ['블루 후드', 0],
            'blue_pants': ['블루 팬츠', 0],
            'bronze_armor': ['브론즈 아머', 0],
            'bronze_bow': ['브론즈 보우', 0],
            'bronze_pants': ['브론즈 팬츠', 0],
            'bronze_shield': ['브론즈 쉴드', 0],
            'bronze_staff': ['브론즈 롱스태프', 0],
            'bronze_sword': ['브론즈 소드', 0],
            'bronze_wand': ['브론즈 숏스태프', 0],
            'chain_armor': ['체인 아머', 0],
            'chain_pants': ['체인 팬츠', 0],
            'chain_shield': ['체인 쉴드', 0],
            'cow_armor': ['소가죽 아머', 0],
            'cow_cape': ['소가죽 망토', 0],
            'cow_glove': ['소가죽 글로브', 0],
            'cow_helmet': ['소가죽 헬멧', 0],
            'cow_pants': ['소가죽 팬츠', 0],
            'croc_cape': ['악어 망토', 0],
            'croc_glove': ['악어 글로브', 0],
            'diamond_gem': ['다이아 룬스태프', 0],
            'gold_armor': ['골드 아머', 0],
            'gold_bow': ['골드 보우', 0],
            'gold_helmet': ['골드 헬멧', 0],
            'gold_pants': ['골드 팬츠', 0],
            'gold_staff': ['골드 롱스태프', 0],
            'gold_sword': ['골드 소드', 0],
            'gold_wand': ['골드 숏스태프', 0],
            'high_chain_glove': ['튼튼한 체인 글로브', 0],
            'horse_armor': ['말가죽 아머', 0],
            'horse_cape': ['말가죽 망토', 0],
            'horse_glove': ['말가죽 글로브', 0],
            'horse_helmet': ['말가죽 헬멧', 0],
            'horse_pants': ['말가죽 팬츠', 0],
            'iron_armor': ['아이언 아머', 0],
            'iron_pants': ['아이언 팬츠', 0],
            'iron_shield': ['아이언 쉴드', 0],
            'leather_shield': ['가죽 방패', 0],
            'low_chain_glove': ['낡은 체인 글로브', 0],
            'middle_chain_glove': ['체인 글로브', 0],
            'red_armor': ['레드 아머', 0],
            'red_cape': ['레드 망토', 0],
            'red_glove': ['레드 글로브', 0],
            'red_hood': ['레드 후드', 0],
            'red_pants': ['레드 팬츠', 0],
            'ruby_gem': ['루비 룬스태프', 0],
            'silver_armor': ['실버 아머', 0],
            'silver_bow': ['실버 보우', 0],
            'silver_helmet': ['실버 헬멧', 0],
            'silver_pants': ['실버 팬츠', 0],
            'silver_staff': ['실버 롱스태프', 0],
            'silver_sword': ['실버 소드', 0],
            'silver_wand': ['실버 완드', 0],
            'stone_gem': ['스톤 룬스태프', 0]}

        #
        # 직업별 착용 장비리스트
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

        for k, v in self.dict_equipment.items():
            v[1] = 1

    # 장비 획득
    def get_equip(self, list_equip):
        for equip in list_equip:
            for k, v in self.dict_equipment.items():
                if k == equip:
                    v[1] += 1

    # 장비 착용
    def wear_equip(self, str_job, str_equipment, dict_user_grad):
        # 직업에 맞는 장비인지 확인
        if str_equipment in self.dict_job_equip[str_job]:
            is_correct = True
        else:
            is_correct = False
        # 맞으면 장비 착용
        if is_correct:
            dict_user_grad[str_job]['equipment'].append(str_equipment)

    # 장비 해제
    def take_off_equip(self, str_job, str_equipment, dict_user_grad):
        dict_user_grad[str_job]['equipment'].remove(str_equipment)

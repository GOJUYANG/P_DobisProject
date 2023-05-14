from Common import Common as c
from Main import MainFrame as mf


class Equipment():
    def __init__(self, **kwargs):
        if 'job' in kwargs:
            self.job = kwargs['job']
        if 'equipment' in kwargs:
            self.equipment = kwargs['equipment']

        # 직업별 착용 장비리스트
        self.job_equip_list = {
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

    # 장비 착용
    def wear_equipment(self):
        # 직업에 맞는 장비인지 확인
        is_correct = self.isEquipCorrect()

        # 맞으면 장비 착용
        if is_correct:
            self.a[self.job]['equipment'].append(self.equipment)
            print(self.a[self.job])

    def isEquipCorrect(self):
        if self.equipment in self.job_equip_list[self.job]:
            return True
        else:
            return False

    # 장비 해제
    def take_off_equipment(self):
        self.a.dict_grad_stat[self.job]['equipment'].remove(self.equipment)
        print(self.a.dict_grad_stat[self.job])
        # 해제한 장비 반환
        return self.equipment






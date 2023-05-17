from PyQt5.QtGui import QIcon

class ItemClass():
    def __init__(self):
        pass

    # 아이템 획득
    def get_item(self, list_item, dict_item, dict_equip):
        # 소모품
        for item in list_item:
            for k, v in dict_item.items():
                if k == item:
                    v['count'] += 1
        # 장비
        for equip in list_item:
            for k, v in dict_equip.items():
                if k == equip:
                    v['count'] += 1
        return dict_item, dict_equip

    # 아이템 사용
    def use_item(self, str_job, str_item, dict_item, dict_user_gard):
        # 직업 리스트
        list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']

        if str_item == 'revival_potion':
            for job in list_job:
                dict_user_gard[job]['survival'] = True
                msg  = '부활포션을 사용하였습니다.'
        elif str_item == 'tent':
            for job in list_job:
                dict_user_gard[job]['hp'] = dict_user_gard[job]['max_hp']
                msg  = '텐트를 사용하였습니다.'
        elif str_item == 'hp_potion_high':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.7
            msg  = 'HP포션(상)을 사용하였습니다.'
        elif str_item == 'hp_potion_middle':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.5
            msg  = 'HP포션(중)을 사용하였습니다.'
        elif str_item == 'hp_potion_low':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.3
            msg  = 'HP포션(하)을 사용하였습니다.'
        elif str_item == 'mp_potion_high':
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.7
            msg  = 'MP포션(상)을 사용하였습니다.'
        elif str_item == 'mp_potion_middle':
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.5
            msg  = 'MP포션(중)을 사용하였습니다.'
        elif str_item == 'mp_potion_low':
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.3
            msg  = 'MP포션(하)을 사용하였습니다.'
        elif str_item == 'all_potion_high':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.7
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.7
            msg  = 'ALL포션(상)을 사용하였습니다.'
        elif str_item == 'all_potion_middle':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.5
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.5
            msg  = 'ALL포션(중)을 사용하였습니다.'
        elif str_item == 'all_potion_low':
            dict_user_gard[str_job]['hp'] += dict_user_gard[str_job]['max_hp'] * 0.3
            dict_user_gard[str_job]['mp'] += dict_user_gard[str_job]['max_mp'] * 0.3
            msg  = 'ALL포션(하)을 사용하였습니다.'
        else:
            pass

        if str_job != '':
            if dict_user_gard[str_job]['hp'] > dict_user_gard[str_job]['max_hp']:
                dict_user_gard[str_job]['hp'] = dict_user_gard[str_job]['max_hp']
            if dict_user_gard[str_job]['mp'] > dict_user_gard[str_job]['max_mp']:
                dict_user_gard[str_job]['mp'] = dict_user_gard[str_job]['max_mp']

        dict_item[str_item]['count'] -= 1

        return dict_item, dict_user_gard, msg

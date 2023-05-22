import random


class FieldClass():
    def __init__(self):
        pass

        # 지역 몬스터 리스트

    def field_meet_monster(self, str_area):
        monster_cnt, hp_monster = self.field_monster_population()

        if str_area == 'area_fire':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['fire_attack', 0.05], 'skill': ['fire_ball', 0.10]}
        elif str_area == 'area_water':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['aqua_attack', 0.05], 'skill': ['aqua_ball', 0.10]}
        elif str_area == 'area_water':
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['air_attack', 0.05], 'skill': ['air_ball', 0.10]}
        else:
            dict_info = {'int_cnt': monster_cnt, 'hp': hp_monster,
                         'attack': ['snow_attack', 0.05], 'skill': ['snow_ball', 0.10]}

        dict_field_monster = {'type': 'field_monster',
                              'area': str_area,
                              'info': dict_info}

        return dict_field_monster

    def return_list_move_drop(self):
        list_move_drop = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low', 'mp_potion_high',
                          'mp_potion_middle', 'mp_potion_low', 'all_potion_high', 'all_potion_middle',
                          'all_potion_low']
        return list_move_drop

    # 획득한 장비 리스트
    def return_move_meet_equipment(self):
        move_meet_equipment = ['black_armor', 'black_cape', 'black_glove', 'black_pants', 'blue_armor',
                               'blue_cape',
                               'blue_glove', 'blue_hood', 'blue_pants', 'bronze_armor', 'bronze_bow',
                               'bronze_pants',
                               'bronze_shield', 'bronze_staff', 'bronze_sword', 'bronze_wand', 'chain_armor',
                               'chain_pants', 'chain_shield', 'cow_armor', 'cow_cape', 'cow_glove', 'cow_helmet',
                               'cow_pants', 'croc_cape', 'croc_glove', 'diamond_gem', 'gold_armor', 'gold_bow',
                               'gold_helmet', 'gold_pants', 'gold_staff', 'gold_sword', 'gold_wand',
                               'high_chain_glove',
                               'horse_armor', 'horse_cape', 'horse_glove', 'horse_helmet', 'horse_pants',
                               'iron_armor',
                               'iron_pants', 'iron_shield', 'leather_shield', 'low_chain_glove',
                               'middle_chain_glove',
                               'red_armor', 'red_cape', 'red_glove', 'red_hood', 'red_pants', 'ruby_gem',
                               'silver_armor',
                               'silver_bow', 'silver_helmet', 'silver_pants', 'silver_staff', 'silver_sword',
                               'silver_wand', 'stone_gem']
        return move_meet_equipment

    def field_monster_population(self):  # 1~10 마리 뽑기
        rand_monster_population_ = random.randint(1, 10)
        monster_population_hp = random.sample(range(200, 1000), k=rand_monster_population_)
        return rand_monster_population_, monster_population_hp

    def field_hp_monster(self):  # 몬스터 랜덤 체력
        rand_hp_monster = random.randint(200, 1000)
        print(f"일반 몬스터의 체력 {rand_hp_monster}")
        return rand_hp_monster

    def field_move_random_drop(self, list_move_drop):  # 필드 이동 중 랜덤 드랍
        list_ = []
        list_drop = random.choice(list_move_drop)
        list_.append(list_drop)
        return list_

    def field_meet_ally_gard(self, list_move_drop, move_meet_equipment):  # 아군 수호대 조우
        rand_num = random.randint(1, 3)
        list_drop_ = []
        drop_item = random.choices(list_move_drop, k=rand_num)
        list_eq_drop = random.choices(move_meet_equipment, k=rand_num)

        list_drop_ += drop_item
        list_drop_ += list_eq_drop
        return list_drop_

    def field_meet_enemy_gard(self, dict_user_gard, str_area):
        int_hp_up = 1.2
        int_power_up = random.choice([1.1, 1.2, 1.3, 1.4, 1.5])
        list_enemy_lvs = random.choices(range(15, 21), k=6)

        if dict_user_gard['gard'] == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'earth_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

        dict_enemy_gard = {'gard': str_enemy_gard,
                           'area': str_area,
                           'warrior': {'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300 * int_hp_up,
                                       'skill': {10: 'slice_chop'}, 'power': 200},
                           'archer': {'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                      'power': 300 * int_power_up,
                                      'skill': {10: 'target_shot',
                                                15: 'dual_shot',
                                                20: 'master_shot'}},
                           'swordman': {'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                        'power': 300 * int_power_up,
                                        'skill': {10: 'slice_chop'}},
                           'wizard_red': {'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                          'mp': 100 * int_hp_up,
                                          'power': 300 * int_power_up,
                                          'skill': {1: ['heal_normal', 'fire_ball'],
                                                    15: ['heal_greater', 'fire_wall'],
                                                    20: 'thunder_breaker',
                                                    25: 'bilzzard',
                                                    30: 'heal_all'}},
                           'wizard_black': {'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                            'power': 300 * int_power_up,
                                            'skill': {1: 'fire_ball',
                                                      15: 'fire_wall',
                                                      20: 'thunder_breaker',
                                                      25: 'bilzzard'}},
                           'wizard_white': {'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                            'power': 300 * int_power_up,
                                            'skill': {1: 'heal_normal',
                                                      10: 'hp_up',
                                                      15: 'heal_greater',
                                                      30: 'heal_all'}}}

        return dict_enemy_gard


    def field_move_event(self, dict_user_gard, int_turn, str_area):  # 이동 중 이벤트 발생
        ratio = random.randint(1, 100)
        if 0 < ratio <= 28:
            return None
        elif 28 < ratio <= 38:
            int_turn += 1
            bool_meet_gard = True
            return '적군수호대', self.field_meet_enemy_gard(dict_user_gard, str_area), bool_meet_gard, int_turn
        elif 38 < ratio <= 58:
            return '아이템', self.field_move_random_drop(self.return_list_move_drop())
        elif 58 < ratio <= 88:
            bool_meet_monster = True
            int_turn += 1
            return '일반몬스터', bool_meet_monster, int_turn
        elif 88 < ratio <= 98:
            return '아군수호대', self.field_meet_ally_gard(self.return_list_move_drop(), self.return_move_meet_equipment())
        elif 98 < ratio <= 100:
            return '텐트', ['tent']

    # def back_position(self): # 도망 , 전투 후 전투전 위치로
    # 몬스터 출현 했을때 좌표 저장했을때의 위치로 돌아가기

    # def fire_monster_match(self):
    #     print(self.dict_field_monster['area_fire'])

    # def water_monster_match(self):
    #     self.dict_field_monster['area_water']
    #     print(self.dict_field_monster['area_water'])
    #
    # def forest_monster_match(self):
    #     self.dict_field_monster['area_forest']
    #     print(self.dict_field_monster['area_forest'])
    #
    # def snow_monster_match(self):
    #     self.dict_field_monster['area_snow']
    #     print(self.dict_field_monster['area_snow'])

    # def random_set_maze_door(self): # 랜덤한 위치에 던전 입구 생성
    #     # if self.int_turn <= 10: # 10 턴 마다 던전입구 재생성
    #     rand_maze_door_x = random.randint(0, 20)
    #     rand_maze_door_y = random.randint(0, 20)
    #     print(f"랜덤 던전 좌표 X {rand_maze_door_x} Y {rand_maze_door_y}")

    # a = FieldClass()
    # f = a.field_move_event()
    # print(f)
    # a.field_monster_population()
    # a.field_hp_monster()
    # a.field_move_random_drop()
    # a.field_meet_ally_gard
    # a.field_monster_population()
    # a.random_set_maze_door()
    #

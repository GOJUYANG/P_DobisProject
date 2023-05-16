import random


class Field:
    def __init__(self):
        self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        # self.monster_population()
        # self.hp_monster()
        monster_cnt, hp_monster_ = self.monster_population()
        self.dict_user_gard = dict()

        # 지역 몬스터 리스트
        self.dict_field_monster = {'fire_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                 'attack': ['fire_attack', 0.05], 'skill': ['fire_ball', 0.10]},
                                   'water_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                  'attack': ['aqua_attack', 0.05], 'skill': ['aqua_ball', 0.10]},
                                   'forest_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                   'attack': ['air_attack', 0.05], 'skill': ['air_ball', 0.10]},
                                   'snow_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                 'attack': ['snow_attack', 0.05], 'skill': ['snow_ball', 0.10]}}
        # 이동 중 아이템 드랍 리스트
        self.list_move_drop = ['HP_potion_high', 'HP_potion_middle', 'HP_potion_low', 'MP_potion_high',
                               'MP_potion_middle', 'MP_potion_low', 'All_potion_high', 'All_potion_middle',
                               'All_potion_low']




        # 턴수 11번째에 던전입구 재생성
        self.trun = 0

    def monster_population(self):  # 1~10 마리 뽑기
        rand_monster_population_ = random.randint(1, 10)
        monster_population_hp = random.sample(range(200, 1000), k=rand_monster_population_)
        return rand_monster_population_, monster_population_hp

    def hp_monster(self):  # 몬스터 랜덤 체력
        rand_hp_monster = random.randint(200, 1000)
        print(f"일반 몬스터의 체력 {rand_hp_monster}")
        return rand_hp_monster

    def field_move_random_drop(self):  # 필드 이동 중 랜덤 드랍
        list_drop = random.choice(self.list_move_drop)
        print(f"이동중 포션 획득 {list_drop} 획득")
        return list_drop

    def meet_ally_gard(self):  # 아군 수호대 조우
        list_drop_ = random.choice(self.list_move_drop)
        print(f"아군 수호대 조우 {list_drop_} 획득")
        return list_drop_

    # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
    def random_maze_door(self):  # 랜덤한 위치에 던전 입구 생성
        rand_maze_door = random.randint(1, 20)
        rand_maze_door_ = random.randint(1, 20)
        print(f"랜덤 던전 좌표 X {rand_maze_door} Y {rand_maze_door_}")

        return rand_maze_door, rand_maze_door_

    def meet_enemy_gard(self, str_my_gard):
        self.int_hp_up = 1.2
        self.list_enemy_lvs = [15, 16, 17, 18, 19, 20]
        self.list_enemy_lvs_ = random.choice(self.list_enemy_lvs)

        if str_my_gard == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'forest_gard'])
        elif str_my_gard == 'forest_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

        self.dict_user_gard = {'gard': str_my_gard,
                               'warrior': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 200,
                                           'skill': {10: 'slice_chop'}},
                               'archer': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 300,
                                          'skill': {10: 'target_shot',
                                                    15: 'dual_shot',
                                                    20: 'master_shot'}},
                               'swordman': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 250,
                                            'skill': {10: 'slice_chop'}},
                               'wizard_red': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 150,
                                              'skill': {1: ['heal_normal', 'fire_ball'],
                                                        15: ['heal_greater', 'fire_wall'],
                                                        20: 'thunder_breaker',
                                                        25: 'bilzzard',
                                                        30: 'heal_all'}},
                               'wizard_black': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 200,
                                                'skill': {1: 'fire_ball',
                                                          15: 'fire_wall',
                                                          20: 'thunder_breaker',
                                                          25: 'bilzzard'}},
                               'wizard_white': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 100,
                                                'skill': {1: 'heal_normal',
                                                          15: 'heal_greater',
                                                          30: 'heal_all'}}}

        self.dict_enemy_gard = {'gard': str_enemy_gard,
                                'warrior': {'lv': self.list_enemy_lvs_, 'hp': 300 * self.int_hp_up, 'mp': 0,
                                            'skill': {10: 'slice_chop'}, 'power': 200},
                                'archer': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                           'power': 300,
                                           'skill': {10: 'target_shot',
                                                     15: 'dual_shot',
                                                     20: 'master_shot'}},
                                'swordman': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                             'power': 250,
                                             'skill': {10: 'slice_chop'}},
                                'wizard_red': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 100 * self.int_hp_up,
                                               'power': 150,
                                               'skill': {1: ['heal_normal', 'fire_ball'],
                                                         15: ['heal_greater', 'fire_wall'],
                                                         20: 'thunder_breaker',
                                                         25: 'bilzzard',
                                                         30: 'heal_all'}},
                                'wizard_black': {'lv': self.list_enemy_lvs_, 'hp': 200 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                                 'power': 200,
                                                 'skill': {1: 'fire_ball',
                                                           15: 'fire_wall',
                                                           20: 'thunder_breaker',
                                                           25: 'bilzzard'}},
                                'wizard_white': {'lv': self.list_enemy_lvs_, 'hp': 200 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                                 'power': 100,
                                                 'skill': {1: 'heal_normal',
                                                           15: 'heal_greater',
                                                           30: 'heal_all'}}}

        return self.dict_enemy_gard, self.dict_user_gard

    def move_event(self):  # 이동 중 이벤트 발생
        ratio = random.randint(1, 100)
        if ratio <= 10:
            print('Tent 획득')
            # self.field_drop()

        elif 10 < ratio <= 20:
            print('아군수호대 조우')
            self.meet_ally_gard()

        elif 20 < ratio <= 30:
            print('적군수호대 조우')
            self.trun += 1
            self.meet_enemy_gard()
            self.bool_meet_gard = True

        elif 30 < ratio <= 50:
            print('아이템 드랍')
            self.field_move_random_drop()

        elif 50 < ratio <= 80:
            print('몬스터 출현')
            self.bool_meet_monster = True
            self.trun += 1
            # 전투전 좌표 저장
        elif 80 < ratio <= 100:
            print('이동')

    # def back_position(self): # 도망 , 전투 후 전투전 위치로
    # 몬스터 출현 했을때 좌표 저장했을때의 위치로 돌아가기

    # def fire_monster_match(self):
    #     print(self.dict_field_monster['fire_area'])

    # def water_monster_match(self):
    #     self.dict_field_monster['water_area']
    #     print(self.dict_field_monster['water_area'])
    #
    # def forest_monster_match(self):
    #     self.dict_field_monster['forest_area']
    #     print(self.dict_field_monster['forest_area'])
    #
    # def snow_monster_match(self):
    #     self.dict_field_monster['snow_area']
    #     print(self.dict_field_monster['snow_area'])


# def random_maze_door(self): # 랜덤한 위치에 던전 입구 생성
#     # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
#     rand_maze_door = random.randint(0, 20)
#     rand_maze_door_ = random.randint(0, 20)
#     print(f"랜덤 던전 좌표 X {rand_maze_door} Y {rand_maze_door_}")


a = Field()
a.move_event()
a.monster_population()
a.hp_monster()
a.field_move_random_drop()
a.meet_ally_gard
a.monster_population()
a.random_maze_door()




# import random
#
#
# class Feild():
#     def __init__(self, **kwargs):
#         # if 'field' in kwargs:
#         #     self.field = kwargs['field']
#         # if 'gard' in kwargs:
#         #     self.gard = kwargs['gard']
#         # if 'monster' in kwargs:
#         #     self.moster = kwargs['monster']
#         # if 'item' in kwargs:
#         #     self.item = kwargs['item']
#         # if 'maze' in kwargs:
#         #     self.tower = kwargs['maze']
#
#         self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']
#         self.list_gard = ['light_gard', 'moon_gard', 'star_gard', 'forest_gard']
#         self.list_monster = ['fire_field_moster', 'water_field_moster', 'forest_field_moster', 'snow_field_moster']
#         self.list_item = ['meteorite', 'tent', 'HP_potion_high', 'HP_potion_middle', 'HP_potion_low', 'MP_potion_high',
#                           'MP_potion_middle', 'MP_potion_low', 'All_potion_high', 'All_potion_middle', 'All_potion_low',
#                           'survival']
#         self.list_move_drop = ['HP_potion_high', 'HP_potion_middle', 'HP_potion_low', 'MP_potion_high',
#                                'MP_potion_middle',
#                                'MP_potion_low', 'All_potion_high', 'All_potion_middle', 'All_potion_low']
#         self.list_maze = ['maze_way', 'random_maze_way']
#         self.meteorite = ['meteorite_item']
#         use_hp = 0
#         # self.turn = 0
#         # hp_monster_ = self.hp_monster()
#         monster_cnt, hp_monster_ = self.monster_population()
#         self.dict_field_monster = {'fire_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
#                                                  'attack': ['fire_attack', 0.05], 'skill': ['fire_ball', 0.10]},
#                                    'water_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
#                                                   'attack': ['aqua_attack', 0.05], 'skill': ['aqua_ball', 0.10]},
#                                    'forest_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
#                                                    'attack': ['air_attack', 0.05], 'skill': ['air_ball', 0.10]},
#                                    'snow_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
#                                                  'attack': ['snow_attack', 0.05], 'skill': ['snow_ball', 0.10]},
#                                    # 직업 리스트
#                                    self.list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black',
#                                                     'wizard_white']
#
#         # 수호대
#         self.dict_gard = {'gard': '',
#                           'location': {'region': '', 'x': 0, 'y': 0},
#                           'warrior': {'survival': True,
#                                       'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
#                                       'equipment': [],
#                                       'skill': {10: 'slice_chop'}},
#                           'archer': {'survival': True,
#                                      'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 150, 'max_mp': 150, 'power': 300,
#                                      'equipment': [],
#                                      'skill': {10: 'target_shot',
#                                                15: 'dual_shot',
#                                                20: 'master_shot'}},
#                           'swordman': {'survival': True,
#                                        'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 150, 'max_mp': 150, 'power': 250,
#                                        'equipment': [],
#                                        'skill': {10: 'slice_chop'}},
#                           'wizard_red': {'survival': True,
#                                          'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 100, 'max_mp': 100, 'power': 150,
#                                          'equipment': [],
#                                          'skill': {1: ['heal_normal', 'fire_ball'],
#                                                    15: ['heal_greater', 'fire_wall'],
#                                                    20: 'thunder_breaker',
#                                                    25: 'bilzzard',
#                                                    30: 'heal_all'}},
#                           'wizard_black': {'survival': True,
#                                            'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 150, 'max_mp': 150, 'power': 200,
#                                            'equipment': [],
#                                            'skill': {1: 'fire_ball',
#                                                      15: 'fire_wall',
#                                                      20: 'thunder_breaker',
#                                                      25: 'bilzzard'}},
#                           'wizard_white': {'survival': True,
#                                            'lv': 1, 'hp': 300, 'max_hp': 300, 'mp': 150, 'max_mp': 150, 'power': 100,
#                                            'equipment': [],
#                                            'skill': {1: 'heal_normal',
#                                                      15: 'heal_greater',
#                                                      30: 'heal_all'}}}
#
#         print('')
#
#     def random_field(self):  # 랜덤 필드 1
#         rand_field_way = random.choice(self.list_field)
#         print(f"나의 용병단 {rand_field_way}의 위치에 생성")
#
#     def random_field_(self):  # 랜덤 필드 2
#         rand_field_way_ = random.randint(0, 20)
#         rand_field_wa_ = random.randint(0, 20)
#         print(f"플레이어는 X {rand_field_way_} Y {rand_field_wa_}에 생성 되었습니다")
#
#     def random_user_gard(self):  # 랜덤 유저 속성 수호대
#         rand_user_gard = random.choice(self.list_gard)
#         print(f"나의 수호대 {rand_user_gard}로 생성")
#
#     def random_maze_door(self):  # 랜덤한 위치에 던전 입구 생성
#         # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
#         rand_maze_door = random.randint(0, 20)
#         rand_maze_door_ = random.randint(0, 20)
#         print(f"랜덤 던전 좌표 X {rand_maze_door} Y {rand_maze_door_}")
#
#     def random_meteorite_position(self):  # 랜덤한 위치에 운석 생성
#         rand_met_position = random.randint(0, 20)
#         rand_met_position_ = random.randint(0, 20)
#         print(f"랜덤 운석 좌표 X {rand_met_position}, Y {rand_met_position_}")
#         # self.inven.append(self.meteorite)
#
#     def field_area(self):  # 지역
#         print('\n')
#         for i in range(10):
#             print("'불'" * 10, '"눈"' * 10, end="\n")
#
#         for i in range(10):
#             print("'숲'" * 10, '"물"' * 10, end="\n")
#
#     def feild_move_random_drop(self):  # 필드 이동 중 랜덤 드랍
#         list_drop = random.choice(self.list_move_drop)
#         print(f"이동 중 {list_drop} 획득했다.")
#
#     def hp_monster(self):  # 몬스터 랜덤 체력
#         rand_hp_monster = random.randint(200, 1000)
#         print(f"일반 몬스터의 체력 {rand_hp_monster}")
#         return rand_hp_monster
#
#     def monster_population(self):  # 1~10 마리 뽑기
#         rand_monster_population_ = random.randint(1, 10)
#         print(f"몬스터 {rand_monster_population_}마리 출현")
#         monster_population_hp = random.sample(range(200, 1000), k=rand_monster_population_)
#         return rand_monster_population_, monster_population_hp
#
#     def monster_population_(self):  # 1칸씩 지정하면 1칸씩 뽑기
#         rand_monster_population = random.randint(0, 1)
#         print(rand_monster_population)
#
#     # def fire_mob(self): # 지역 고유 몬스터를 출현 시키기 위한 함수 어렵따
#     #     if x10 in self.x
#
#     # def monster_(self): # 몬스터의 특성 어렵따
#     def monster_fire(self):
#         print(self.dict_field_monster['fire_area'])
#         print("불 몬스터")
#
#     def monseter_water(self):
#         print(self.dict_field_monster['water_area'])
#         print("물 몬스터")
#
#     def monster_forest(self):
#         print(self.dict_field_monster['forest_area'])
#         print("숲 몬스터")
#
#     def monster_snow(self):
#         print(self.dict_field_monster['snow_area'])
#         print("눈 몬스터")
#
#     # def skil_dam(self):
#
#     def monster_dam(self):
#
#
# a = Feild()
# a.random_field()
# b = Feild()
# b.random_user_gard()
# c = Feild()
# c.random_maze_door()
# d = Feild()
# d.random_meteorite_position()
# e = Feild()
# e.field_area()
# f = Feild()
# f.feild_move_random_drop()
# g = Feild()
# g.hp_monster()
# h = Feild()
# h.monster_population()
# j = Feild()
# j.random_field_()
# k = Feild()
# k.monster_fire()
# l = Feild()
# l.monseter_water()
# m = Feild()
# m.monster_forest()
# n = Feild()
# n.monster_snow()
#
# # 시작 버튼 클릭 시 필드에서 4개지역 [불, 물, 숲, 눈] 중 랜덤한 위치에 수호대가 생성된다.0
# # 플레이어의 특정 수호대를 제외한 나머지 특정 타 수호대를 생성한다.
# # 각 지역 이동 중 지역의 고유 몬스터를 일정 확률로 몬스터가 출몰한다.
# # 던전 입구는 필드 내 랜덤한 위치에 생성된다. 0
# # 이동 중 랜덤한 위치에 운석이 존재하며 획득한다. 0
# # 이동 중 일정 확률로 아이템 획득이 가능하다. (부활포션, 장비아이템 제외) 0
# # 이동 중 일정 확률로 타 수호대와 조우 한다.
# # 11번째 전투까지 던전 입구 못찾을시 랜덤한 위치에 재생성
# # 각 지역 필드 몬스터 설정 어렵다.
# # 각 지역 설정 0
# # 전투시 마리 수 랜덤 0
# # 전투에 전해 줄 딕셔너리 몬스터 설정 어렵다.
# # 지역에 있을때 지역 고유 몬스터 출몰 시키기. 어렵다.
# # list_area_monster, list_damage(일반공격, 스킬) 에 넣을 방법 생각하기
#
# # 좌표 설정하는게 어렵다!
#
# # cho_ = random.choices([1,2,3,4,5],k=3)
#
#
# # 필드 일반 몬스터 조우
# # 받을 값(1): str_area
# # 받을 값(2): dict_user_gard[name, lv, hp, mp, list_item[potion,meteorite], skill, power]

# 우리 수호대
self.dict_user_gard = {'gard': '',
                       'warrior': {'survival': True,
                                   'image': '',
                                   'lv': 30, 'hp': 300, 'max_hp': 300, 'mp': 0, 'max_mp': 0, 'power': 200,
                                   'equipment': [],
                                   'skill': {10: 'slice_chop'}},
                       'archer': {'survival': True,
                                  'image': '',
                                  'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 150, 'max_mp': 150, 'power': 300,
                                  'equipment': [],
                                  'skill': {10: 'target_shot',
                                            15: 'dual_shot',
                                            20: 'master_shot'}},
                       'swordman': {'survival': True,
                                    'image': '',
                                    'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 150, 'max_mp': 150, 'power': 250,
                                    'equipment': [],
                                    'skill': {10: 'slice_chop'}},
                       'wizard_red': {'survival': True,
                                      'image': '',
                                      'lv': 1, 'hp': 150, 'max_hp': 150, 'mp': 100, 'max_mp': 100, 'power': 150,
                                      'equipment': [],
                                      'skill': {1: ['heal_normal', 'fire_ball'],
                                                15: ['heal_greater', 'fire_wall'],
                                                20: 'thunder_breaker',
                                                25: 'bilzzard',
                                                30: 'heal_all'}},
                       'wizard_black': {'survival': True,
                                        'image': '',
                                        'lv': 1, 'hp': 200, 'max_hp': 200, 'mp': 150, 'max_mp': 150,
                                        'power': 200,
                                        'equipment': [],
                                        'skill': {1: 'fire_ball',
                                                  15: 'fire_wall',
                                                  20: 'thunder_breaker',
                                                  25: 'bilzzard'}},
                       'wizard_white': {'survival': True,
                                        'image': '',
                                        'lv': 1, 'hp': 200, 'max_hp': 200, 'mp': 150, 'max_mp': 150,
                                        'power': 100,
                                        'equipment': [],
                                        'skill': {1: 'heal_normal',
                                                  15: 'heal_greater',
                                                  30: 'heal_all'}}}

# 필드 적수호대
int_hp_up = 1.2
int_power_up = random.choice([1.1, 1.2, 1.3, 1.4, 1.5])
list_enemy_lvs = [15, 16, 17, 18, 19, 20]
list_enemy_lvs_ = random.choice(list_enemy_lvs)

if dict_user_gard['gard'] == 'light_gard':
    str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'moon_gard':
    str_enemy_gard = random.choice(['light_gard', 'star_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'star_gard':
    str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'earth_gard':
    str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

dict_enemy_gard = {'type': 'maze_enemy_gard',
                   'gard': str_enemy_gard,

                   'warrior': {'lv': list_enemy_lvs_, 'hp': 300 * int_hp_up, 'max_hp': 300 * int_hp_up,
                               'skill': {10: 'slice_chop'}, 'power': 200},
                   'archer': {'lv': list_enemy_lvs_, 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                              'power': 300 * int_power_up,
                              'skill': {10: 'target_shot',
                                        15: 'dual_shot',
                                        20: 'master_shot'}},
                   'swordman': {'lv': list_enemy_lvs_, 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                'power': 300 * int_power_up,
                                'skill': {10: 'slice_chop'}},
                   'wizard_red': {'lv': list_enemy_lvs_, 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                  'mp': 100 * int_hp_up,
                                  'power': 300 * int_power_up,
                                  'skill': {1: ['heal_normal', 'fire_ball'],
                                            15: ['heal_greater', 'fire_wall'],
                                            20: 'thunder_breaker',
                                            25: 'bilzzard',
                                            30: 'heal_all'}},
                   'wizard_black': {'lv': list_enemy_lvs_, 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                    'power': 300 * int_power_up,
                                    'skill': {1: 'fire_ball',
                                              15: 'fire_wall',
                                              20: 'thunder_breaker',
                                              25: 'bilzzard'}},
                   'wizard_white': {'lv': list_enemy_lvs_, 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                    'power': 300 * int_power_up,
                                    'skill': {1: 'heal_normal',
                                              15: 'heal_greater',
                                              30: 'heal_all'}}}

# 던전 적수호대
if int_floor == 1:
    list_enemy_lvs = random.choices(range(20, 25), k=6)
    int_hp_up = 1.3
    power = random.randint(300, 400)
elif int_floor == 2:
    list_enemy_lvs = random.choices(range(25, 30), k=6)
    int_hp_up = 1.3
    power = random.randint(500, 1000)
elif int_floor == 3:
    list_enemy_lvs = random.choices(range(30, 35), k=6)
    int_hp_up = 1.3 * 1.4
    power = random.randint(1000, 2000)
elif int_floor == 4:
    list_enemy_lvs = random.choices(range(35, 40), k=6)
    int_hp_up = 1.3 * 1.4
    power = random.randint(2000, 3500)
elif int_floor == 5:
    list_enemy_lvs = random.choices(range(45, 50), k=6)
    int_hp_up = 1.3 * 1.4 * 1.5
    power = random.randint(3500, 5000)
elif int_floor >= 6:
    list_enemy_lvs = random.choices(range(50, 100), k=6)
    int_hp_up = 1.3 * 1.4 * 1.5 * 1.6
    power = random.randint(5000, 10000)

if dict_user_gard['gard'] == 'light_gard':
    str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'moon_gard':
    str_enemy_gard = random.choice(['light_gard', 'star_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'star_gard':
    str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'earth_gard'])
elif dict_user_gard['gard'] == 'earth_gard':
    str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

dict_enemy_gard = {'type': 'maze_enemy_gard',
                   'gard': str_enemy_gard,
                   'warrior': {'survival': True,
                               'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300 * int_hp_up,
                               'power': power,
                               'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                             'bronze_sword'],
                               'skill': {10: 'slice_chop'}},
                   'archer': {'survival': True,
                              'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                              'power': power,
                              'equipment': [],
                              'skill': {10: 'target_shot',
                                        15: 'dual_shot',
                                        20: 'master_shot'}},
                   'swordman': {'survival': True,
                                'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                'power': power,
                                'equipment': [],
                                'skill': {10: 'slice_chop'}},
                   'wizard_red': {'survival': True,
                                  'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up, 'max_hp': 150 * int_hp_up,
                                  'power': power,
                                  'equipment': [],
                                  'skill': {1: ['heal_normal', 'fire_ball'],
                                            15: ['heal_greater', 'fire_wall'],
                                            20: 'thunder_breaker',
                                            25: 'bilzzard',
                                            30: 'heal_all'}},
                   'wizard_black': {'survival': True,
                                    'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                    'power': power,
                                    'equipment': [],
                                    'skill': {1: 'fire_ball',
                                              15: 'fire_wall',
                                              20: 'thunder_breaker',
                                              25: 'bilzzard'}},
                   'wizard_white': {'survival': True,
                                    'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up, 'max_hp': 200 * int_hp_up,
                                    'power': power,
                                    'equipment': [],
                                    'skill': {1: 'heal_normal',
                                              15: 'heal_greater',
                                              30: 'heal_all'}}}

# 필드몬스터
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

# 던전몬스터 구성
dict_maze_monster = {'int_cnt': int_monster_count,
                     'list_hp': random.sample(range(200, 1000), int_monster_count),
                     'list_area_monster': random.choices(
                         ['area_fire', 'area_water', 'area_forest', 'area_snow'], k=int_monster_count),
                     'list_damage': random.choices([0.05, 0.1], k=int_monster_count)}

# 보스
if int_floor == 1:
    int_boss_hp = random.randint(25000, 35000)
    dict_boss_monster = {'floor': 1,
                         'type': 'boss',
                         'name': '이동려크',
                         'hp': int_boss_hp,
                         'attack': ['fan_attack', 0.05],
                         'skill': ['hell_shouting', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 2:
    int_boss_hp = random.randint(45000, 55000)
    dict_boss_monster = {'floor': 2,
                         'type': 'boss',
                         'name': '조동혀니', 'hp': int_boss_hp, 'attack': ['silent_attack', 0.05],
                         'skill': ['hell_feedback', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 3:
    int_boss_hp = random.randint(65000, 75000)
    dict_boss_monster = {'floor': 3,
                         'type': 'boss',
                         'name': '류홍거리', 'hp': int_boss_hp, 'attack': ['ignore_attack', 0.05],
                         'skill': ['hell_ignore', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 4:
    int_boss_hp = random.randint(75000, 85000)
    dict_boss_monster = {'floor': 4,
                         'type': 'boss',
                         'name': '코로나악마공주', 'hp': int_boss_hp, 'attack': ['virus_attack', 0.05],
                         'skill': ['hell_virus', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 5:
    int_boss_hp = random.randint(85000, 599999)
    dict_boss_monster = {'floor': 5,
                         'type': 'boss',
                         'name': '이땅복이', 'hp': int_boss_hp, 'attack': ['html_attack', 0.05],
                         'skill': ['hell_task', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 6:
    int_boss_hp = random.randint(999999, 9999999)
    dict_boss_monster = {'floor': 6,
                         'type': 'boss',
                         'name': '환생의 복이', 'hp': int_boss_hp, 'attack': ['python_attack', 0.05],
                         'skill': ['hell_coding', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}
elif int_floor == 7:
    int_boss_hp = 9999999
    dict_boss_monster = {'floor': 7,
                         'type': 'boss',
                         'name': '로드오브보기', 'hp': int_boss_hp, 'attack': ['c_attack', 0.05],
                         'skill': ['hell_boki', 0.1],
                         'list_field_monster': [int_cnt, list_hp, list_area]}

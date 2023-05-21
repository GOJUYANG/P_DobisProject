# #던전 입장
# 던전 크기 랜덤 생성, 각 층의 던전 크기 저장

# 텔레포트
# 층마다 5개의 텔레포트 주어짐
# 텔레포트와 전투시 옵션인 도망은 별개
# (전투중 사용하며 발동 확률이 존재하는 도망과 달리 텔레포트는 던전 내에서 후퇴용으로 무조건 사용 가능)
# (텐트사용, 텐트 및 포션줍기, 보스몬스터피하기 등 던전에서 필드로 후퇴할 때 사용, 어감만 도망일뿐 전투중 도망과 다름)
# 던전에서 텔레포트 사용하면 필드로 나옴
# 필드로 텔레포트 한 후 던전으로 재입장하려면 다시 랜덤으로 생성된 입구 찾아야함
# 던전을 나와서 재입장할때 입장했던(클리어한) 던전의 최상층의 랜덤 좌표로 이동
#
# #던전 내 이동
# 던전 내 이동시 20%이동, 20% 포션 획득, 30% 일반몬스터 만남, 15% 아군타수호대 만남, 15%적군수호대 만남
# 전투를 안하는 동안 포션사용 및 장비 교체 가능
# 아군수호대 만날 경우 아군 수호대를 만났다는 메시지 보여줌
# 포션 습득 시 메시지 알리며 포션 개수 업데이트
# 일반몬스터 혹은 타수호대 만나면 전투 시작

# 아군 수호대 조우시 아이템 휙득
# 부활포션 및 텐트 이외의 아이템과 장비 중 하나가 나옴
#
# #적군수호대와 조우 시 전투 세팅
# 던전 내 이동시 15% 확률로 만남
# 던젼 1층에서 만날시 타 수호대 레벨 평균20~25렙
# 던젼 2층에서 만날시 타 수호대 레벨 평균25~30렙
# 던젼 3층에서 만날시 타 수호대 레벨 평균30~35렙
# 던젼 4층에서 만날시 타 수호대 레벨 평균35~40렙
# 던젼 5층에서 만날시 타 수호대 레벨 평균45~50렙
# 던젼 6층 이상 만날시 타 수호대 레벨 평균은 50~100렙

#
# #일반몬스터 조우 시 전투 세팅
# 던전 내 이동시 30% 확률로 만남
# 각 지역별 필드몬스터가 랜덤하게 등장 - 일반몬스터는 텐트 및 부활포션 제외한 9개의 포션아이템&장비 드랍
# 일반 몬스터 1~10마리/최소 HP 200~1000

# #보스 모스터 위치 및 종류 지정 - 보스몬스터는 부활포션 드랍
# 보스의 부하 일반몬스터는 0~6마리
# 처치하면 모든 장비와 포션이 일정확률로 드랍한다.
# 던젼 1층 보스 : 이동려크 최소 HP25000~35000 랜덤 등장
# 던젼 2층 보스 : 조동혀니 최소 HP45000~55000 랜덤 등장
# 던젼 3층 보스 : 류홍거리  최소 HP65000~75000 랜덤 등장
# 던젼 4층 보스 : 코로나악마공주 HP75000~85000 랜덤 등장
# 던젼 5층 보스 : 이땅복이  HP85000~599999 랜덤 등장
# 던젼 6층 보스 : 환생의 복이 HP 999999~9999999 랜덤 등장
# 던젼 7층 보스 : 로드오브보기 HP 9999999 이상 랜덤 등장
# 보스 위치 도달하면 보스전 시작
# 보스전 이기면 다음층 올라가는 입구 열림

# #윗층 이동
# 위로 올라가는 계단 입구 랜덤 생성 및 위치 표시
# (타수호대, 일반 보스와의)전투 7번까지는 다음층 계단 유지
# 8번째 전투부터 다음층 계단 위치 변경
# 보스 죽이기 전에는 접근해도 들어갈 수 없음

#
# #전투불능 상태
# 던전에서 전투 중 전투불능 상태(전원 hp가 0)인 경우 전투가 강제종료되어 던전으로 돌아옴(주양)
# 던전에서 부활포션 유무 판단, 있으면 사용하고 없으면 필드로 내보냄(경고: 부활포션이 없습니다! 필드로 이동합니다)
# (진영 필드에서 랜덤배치 및 전투배제모드, 텐트 유무 판단 후 텐트조차 없으면 게임오버)
#
# #최종장
# 7층에서 최종보스 죽인후 8층 이동
# 8층 4*4 크기의 던전에서 복이 위치 표시
# 복이 좌표에 다가가 구출, 게임엔딩

import random


class mazeClass:
    def __init__(self):
        pass

    def return_list_widths(self):
        list_widths = random.choices([15, 16, 17, 18], k=7)
        list_widths.append(4)
        return list_widths

    def return_int_floor(self):
        int_floor = 1
        return int_floor

    def return_dict_teleport_stock(self):
        dict_teleport_stock = {'first': 5, 'second': 5, 'third': 5, 'fourth': 5, 'fifth': 5, 'sixth': 5, 'seventh': 5}
        return dict_teleport_stock

    def maze_move_event(self, int_floor, dict_user_gard, int_turn):
        ratio = random.randint(1, 100)
        if ratio <= 30:
            bool_meet_maze_monster = True
            int_turn += 1
            return '일반몬스터', self.maze_meet_monster(int_floor, dict_user_gard), bool_meet_maze_monster, int_turn
        elif ratio <= 45:

            return '아군수호대', self.maze_meet_ally_gard()
        elif ratio <= 60:
            bool_meet_enemy_gard = True
            int_turn += 1
            return '적군수호대', self.maze_meet_enemy_gard(int_floor, dict_user_gard), bool_meet_enemy_gard, int_turn
        else:
            return '이동'

    # 일반몬스터 만남(1~10마리)
    def maze_meet_monster(self, int_floor, dict_user_gard):
        int_floor = int_floor
        int_monster_count = random.randint(1, 10)
        # 일반몬스터 구성
        dict_maze_monster = {'int_cnt': int_monster_count,
                             'list_hp': random.sample(range(200, 1000), int_monster_count),
                             'list_area_monster': random.choices(
                                 ['area_fire', 'area_water', 'area_forest', 'area_snow'], k=int_monster_count),
                             'list_damage': random.choices([0.05, 0.1], k=int_monster_count)}
        # 시연님 상속받기

        return int_floor, dict_maze_monster, dict_user_gard

    # 아군 수호대 만남-9종류의 포션과 장비 중 나눔받음
    def maze_meet_ally_gard(self):
        list_ally_drop = []
        drop_cnt = random.randint(1, 3)
        list_ally_drop_potion = random.choices(['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                                'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                                'all_potion_high', 'all_potion_middle', 'all_potion_low'], k=drop_cnt)
        list_ally_drop_equip = random.choices(['black_armor', 'black_cape', 'black_glove', 'black_pants', 'blue_armor',
                                               'blue_cape', 'blue_glove', 'blue_hood', 'blue_pants', 'bronze_armor',
                                               'bronze_bow', 'bronze_pants', 'bronze_shield', 'bronze_staff',
                                               'bronze_sword', 'bronze_wand', 'chain_armor', 'chain_pants',
                                               'chain_shield', 'cow_armor', 'cow_cape', 'cow_glove', 'cow_helmet',
                                               'cow_pants', 'croc_cape', 'croc_glove', 'diamond_gem', 'gold_armor',
                                               'gold_bow', 'gold_helmet', 'gold_pants', 'gold_staff', 'gold_sword',
                                               'gold_wand', 'high_chain_glove', 'horse_armor', 'horse_cape',
                                               'horse_glove', 'horse_helmet', 'horse_pants', 'iron_armor',
                                               'iron_pants', 'iron_shield', 'leather_shield', 'low_chain_glove',
                                               'middle_chain_glove', 'red_armor', 'red_cape', 'red_glove', 'red_hood',
                                               'red_pants', 'ruby_gem', 'silver_armor', 'silver_bow', 'silver_helmet',
                                               'silver_pants', 'silver_staff', 'silver_sword', 'silver_wand',
                                               'stone_gem'], k=drop_cnt)
        for i in list_ally_drop_potion:
            list_ally_drop.append(i)
        for j in list_ally_drop_equip:
            list_ally_drop.append(j)
        return list_ally_drop

    # 적군수호대 만남
    def maze_meet_enemy_gard(self, int_floor, dict_user_gard):
        # 전투시작
        if int_floor == 1:
            list_enemy_lvs = random.choices(range(20, 25), k=6)
            int_hp_up = 1.3
        elif int_floor == 2:
            list_enemy_lvs = random.choices(range(25, 30), k=6)
            int_hp_up = 1.3
        elif int_floor == 3:
            list_enemy_lvs = random.choices(range(30, 35), k=6)
            int_hp_up = 1.3 * 1.4
        elif int_floor == 4:
            list_enemy_lvs = random.choices(range(35, 40), k=6)
            int_hp_up = 1.3 * 1.4
        elif int_floor == 5:
            list_enemy_lvs = random.choices(range(45, 50), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5
        elif int_floor >= 6:
            list_enemy_lvs = random.choices(range(50, 100), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5 * 1.6

        if dict_user_gard['gard'] == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'earth_gard'])
        elif dict_user_gard['gard'] == 'earth_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

        dict_enemy_gard = {'gard': str_enemy_gard,
                           'location': {'region': '', 'x': 0, 'y': 0},
                           'warrior': {'survival': True,
                                       'lv': list_enemy_lvs[0], 'hp': 300 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                       'max_mp': 0, 'power': 200,
                                       'equipment': ['silver_helmet', 'bronze_armor', 'bronze_shield',
                                                     'bronze_sword'],
                                       'skill': {10: 'slice_chop'}},
                           'archer': {'survival': True,
                                      'lv': list_enemy_lvs[1], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                      'max_mp': 0, 'power': 300,
                                      'equipment': [],
                                      'skill': {10: 'target_shot',
                                                15: 'dual_shot',
                                                20: 'master_shot'}},
                           'swordman': {'survival': True,
                                        'lv': list_enemy_lvs[2], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                        'max_mp': 0, 'power': 250,
                                        'equipment': [],
                                        'skill': {10: 'slice_chop'}},
                           'wizard_red': {'survival': True,
                                          'lv': list_enemy_lvs[3], 'hp': 150 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                          'max_mp': 0, 'power': 150,
                                          'equipment': [],
                                          'skill': {1: ['heal_normal', 'fire_ball'],
                                                    15: ['heal_greater', 'fire_wall'],
                                                    20: 'thunder_breaker',
                                                    25: 'bilzzard',
                                                    30: 'heal_all'}},
                           'wizard_black': {'survival': True,
                                            'lv': list_enemy_lvs[4], 'hp': 200 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                            'max_mp': 0, 'power': 200,
                                            'equipment': [],
                                            'skill': {1: 'fire_ball',
                                                      15: 'fire_wall',
                                                      20: 'thunder_breaker',
                                                      25: 'bilzzard'}},
                           'wizard_white': {'survival': True,
                                            'lv': list_enemy_lvs[5], 'hp': 200 * int_hp_up, 'max_hp': 300, 'mp': 0,
                                            'max_mp': 0, 'power': 100,
                                            'equipment': [],
                                            'skill': {1: 'heal_normal',
                                                      15: 'heal_greater',
                                                      30: 'heal_all'}}}
        return int_floor, dict_enemy_gard, dict_user_gard

    # 던전 보스 위치
    def maze_boss_location(self, int_floor):
        map_size = random.randint(15, 18)
        boss_x = random.randint(1, map_size - 1)
        boss_y = random.randint(1, map_size - 1)
        print(map_size, boss_x, boss_y)
        return map_size, boss_x, boss_y

    # 던전 각 층 내 보스와 부하들 종류
    # 던전 보스 위치와 내 수호대의 위치가 동일한 경우 보스전 시작
    def maze_boss_match(self, int_floor):
        # 부하 몬스터들(0~6마리) 속성
        int_cnt = random.randint(0, 6)
        list_hp = random.sample(range(200, 1000), k=int_cnt)
        list_area = random.choices(['area_fire', 'area_water', 'area_forest', 'area_snow'], k=int_cnt)

        if int_floor == 1:
            int_boss_hp = random.randint(25000, 35000)
            dict_boss_monster = {'name': '이동려크', 'hp': int_boss_hp, 'attack': ['fan_attack', 0.05],
                                 'skill': ['hell_shouting', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 2:
            int_boss_hp = random.randint(45000, 55000)
            dict_boss_monster = {'name': '조동혀니', 'hp': int_boss_hp, 'attack': ['silent_attack', 0.05],
                                 'skill': ['hell_feedback', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 3:
            int_boss_hp = random.randint(65000, 75000)
            dict_boss_monster = {'name': '류홍거리', 'hp': int_boss_hp, 'attack': ['ignore_attack', 0.05],
                                 'skill': ['hell_ignore', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 4:
            int_boss_hp = random.randint(75000, 85000)
            dict_boss_monster = {'name': '코로나악마공주', 'hp': int_boss_hp, 'attack': ['virus_attack', 0.05],
                                 'skill': ['hell_virus', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 5:
            int_boss_hp = random.randint(85000, 599999)
            dict_boss_monster = {'name': '이땅복이', 'hp': int_boss_hp, 'attack': ['html_attack', 0.05],
                                 'skill': ['hell_task', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 6:
            int_boss_hp = random.randint(999999, 9999999)
            dict_boss_monster = {'name': '환생의 복이', 'hp': int_boss_hp, 'attack': ['python_attack', 0.05],
                                 'skill': ['hell_coding', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        elif int_floor == 7:
            int_boss_hp = 9999999
            dict_boss_monster = {'name': '로드오브보기', 'hp': int_boss_hp, 'attack': ['c_attack', 0.05],
                                 'skill': ['hell_boki', 0.1],
                                 'list_field_monster': [int_cnt, list_hp, list_area]}
        print(int_floor, dict_boss_monster)
        return int_floor, dict_boss_monster

    # 텔레포트 사용
    def maze_use_teleport(self, int_floor, dict_teleport_stock):
        if int_floor == 1:
            dict_teleport_stock['first'] -= 1
        elif int_floor == 2:
            dict_teleport_stock['second'] -= 1
        elif int_floor == 3:
            dict_teleport_stock['third'] -= 1
        elif int_floor == 4:
            dict_teleport_stock['fourth'] -= 1
        elif int_floor == 5:
            dict_teleport_stock['fifth'] -= 1
        elif int_floor == 6:
            dict_teleport_stock['sixth'] -= 1
        elif int_floor == 7:
            dict_teleport_stock['seventh'] -= 1
        print(dict_teleport_stock)
        return dict_teleport_stock

    # 필드로 텔레포트 사용시 필드 이동 위치
    def maze_teleport_location(self):
        tele_x = random.randint(1, 20)
        tele_y = random.randint(1, 20)
        print('텔레포트를 사용해 필드({},{})로 이동'.format(tele_y, tele_x))
        return tele_y, tele_x

    # 텔레포트 사용 후 재입장시 이동위치
    def maze_reentry_maze(self, int_floor):
        maze_reentry_maze_x = random.randint(1, self.list_widths[int_floor - 1])
        maze_reentry_maze_y = random.randint(1, self.list_widths[int_floor - 1])
        print('{}층 {},{}로 재입장'.format(int_floor, maze_reentry_maze_y, maze_reentry_maze_x))
        self.maze_use_teleport(int_floor)
        return maze_reentry_maze_y, maze_reentry_maze_x

    # 다음층으로 가는 계단 좌표
    def maze_next_maze_entrance(self, int_floor):
        int_floor = int_floor
        int_next_entrance_x = random.randint(1, self.return_list_widths()[int_floor - 1])
        int_next_entrance_y = random.randint(1, self.return_list_widths()[int_floor - 1])
        print("{}층에서 다음층으로 가는 계단 좌표 {},{}".format(int_floor, int_next_entrance_y, int_next_entrance_x))
        return int_next_entrance_y, int_next_entrance_x

    # 7번째 전투까지는 다음 던전으로 가는 입구 유지, 8번째부터 계단 랜덤 재배치
    def maze_change_entrance_location(self, int_floor, int_turn):
        if int_turn > 7:
            self.maze_next_maze_entrance(int_floor)
        else:
            print('계단 입구 유지')

    # 보스 처치 유무 확인
    # 보스 죽인후 다음층 이동
    def maze_next_maze(self, int_floor, bool_death_boss):
        if bool_death_boss:
            int_floor += 1
            self.int_turn = 0
            int_current_x = random.randint(1, self.return_list_widths[int_floor - 1])
            int_current_y = random.randint(1, self.return_list_widths[int_floor - 1])
            print("{}층 {},{}로 진입".format(int_floor, int_current_y, int_current_x))
            return int_floor, int_current_y, int_current_x
        else:
            str_disable_next = "아직 보스를 죽이지 않아 다음층으로 이동할 수 없습니다."
            print(str_disable_next, '현재층:', int_floor)
            return str_disable_next

    # 8층 복이 위치(구출하고 게임엔딩)
    def maze_boki_location(self, int_floor):
        if int_floor == 8:
            int_boki_x = random.randint(1, 4)
            int_boki_y = random.randint(1, 4)
            print("{}층 {},{} 복이 구출".format(int_floor, int_boki_y, int_boki_x))
            return int_boki_y, int_boki_x
        else:
            print('8층 아님')

# class_b = mazeClass()
# print('>>>던전 맵 내 이동시 이벤트')
# class_b.maze_move_event(class_b.int_floor, 'moon_gard')
# print()
# print('>>>보스몬스터 위치')
# class_b.maze_boss_location(class_b.int_floor)
# print()
# print('>>>보스몬스터 위치에 도달한 경우 전투 시작')
# class_b.maze_boss_match(class_b.int_floor)
# print()
# print('>>>다음층 계단 입구 위치')
# class_b.maze_next_maze_entrance(class_b.int_floor)
# print()
# print('>>>다음층 입구 도달시 보스처치 유무에 따른 결과')
# class_b.maze_next_maze(class_b.int_floor, bool_death_boss=True)
# class_b.maze_next_maze(class_b.int_floor, bool_death_boss=False)
# class_b.maze_change_entrance_location(class_b.int_floor, int_turn=7)
# class_b.maze_change_entrance_location(class_b.int_floor, int_turn=8)
# print(class_b.int_floor, '층')
# print()
# print('>>>텔레포트 사용')
# class_b.maze_use_teleport(class_b.int_floor, class_b.return_dict_teleport_stock())
# class_b.maze_teleport_location()
# class_b.maze_reentry_maze()
# print(class_b.int_floor)
# print()
# print('>>>이상복 구출')
# class_b.maze_boki_location()
# class_b.int_floor = 8
# class_b.maze_boki_location()
#

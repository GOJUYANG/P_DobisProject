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


class DungeonClass:
    def __init__(self):
        # 던전입장 후 현재 층 : int_floor = 1
        self.dict_teleport_stock = {'first': 5, 'second': 5, 'third': 5, 'fourth': 5, 'fifth': 5, 'sixth': 5, 'seventh': 5}
        self.list_widths = random.choices([15, 16, 17, 18], k=7)
        self.list_widths.append(4)
        print(self.list_widths)

        self.first_width = self.list_widths[0]
        self.second_width = self.list_widths[1]
        self.third_width = self.list_widths[2]
        self.fourth_width = self.list_widths[3]
        self.fifth_width = self.list_widths[4]
        self.sixth_width = self.list_widths[5]
        self.seventh_width = self.list_widths[6]
        self.eighth_width = self.list_widths[7]

        self.int_floor = 1
        self.dict_gard = dict()
        self.int_turn = 0

    def move_event(self, int_floor, str_my_gard):
        self.int_floor = int_floor
        ratio = random.randint(1, 100)
        if ratio <= 30:
            print('일반몬스터')
            self.bool_meet_monster = True
            self.meet_monster(self.int_floor, str_my_gard)
            self.int_turn += 1
        elif ratio <= 45:
            print('아군수호대 조우')
            self.meet_ally_gard()
        elif ratio <= 60:
            print('적군수호대 조우')
            self.bool_meet_enemy_gard = True
            self.meet_enemy_gard(self.int_floor, str_my_gard)
            self.int_turn += 1
        else:
            print('그냥이동')

    # 일반몬스터 만남(1~10마리)
    def meet_monster(self, int_floor, str_my_gard):
        self.int_floor = int_floor
        int_monster_count = random.randint(1, 10)
        # 일반몬스터 구성
        self.dict_maze_monster = {'int_cnt': int_monster_count,
                                  'list_hp': random.sample(range(200, 1000), int_monster_count),
                                  'list_area_monster': random.choices(['area_fire', 'area_water', 'area_forest', 'area_snow'], k=int_monster_count),
                                  'list_damage': random.choices([0.05, 0.1], k=int_monster_count)
                                  }
        #시연님 상속받기-어떻게?
        self.dict_gard = {'gard': str_my_gard,
                          'warrior': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                      'skill':{10:'slice_chop'}, 'power': 200},
                          'archer': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                     'skill': {10: 'target_shot',
                                               15: 'dual_shot',
                                               20: 'master_shot'}, 'power': 300},
                          'swordman': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                       'skill': {10: 'slice_chop'}, 'power': 250},
                          'wizard_red': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                         'skill': {1: ['heal_normal', 'fire_ball'],
                                                   15: ['heal_greater', 'fire_wall'],
                                                   20: 'thunder_breaker',
                                                   25: 'bilzzard',
                                                   30: 'heal_all'}, 'power': 150},
                          'wizard_black': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                           'skill': {1: 'fire_ball',
                                                     15: 'fire_wall',
                                                     20: 'thunder_breaker',
                                                     25: 'bilzzard'}, 'power': 200},
                          'wizard_white': {'lv': 1, 'hp': 300, 'mp': 0, 'list_item': {'portion', 'meteorite'},
                                           'skill': {1: 'heal_normal',
                                                     15: 'heal_greater',
                                                     30: 'heal_all'}, 'power': 100}}
        print(self.int_floor, '층', '일반몬 구성:', self.dict_maze_monster, '내 수호대 구성:', self.dict_gard)
        return self.int_floor, self.dict_maze_monster, self.dict_gard

    # 아군 수호대 만남-9종류의 포션 중 하나 나눔받음
    def meet_ally_gard(self):
        #9개의 포션, 장비들 중 하나 드랍
        print('아군수호대를 만났다')
        ally_drop_item = random.choice(['HP_potion_high', 'HP_potion_middle', 'HP_potion_low',
                                        'MP_potion_high', 'MP_potion_middle', 'MP_potion_low',
                                        'All_potion_high', 'All_potion_middle', 'All_potion_low'])
        # 차후 GUI 연결하고 개수 1개 늘어나도록
        if ally_drop_item == 'HP_potion_high':
            ally_drop_potion = 'HP대'
        elif ally_drop_item == 'HP_potion_middle':
            ally_drop_potion = 'HP중'
        elif ally_drop_item == 'HP_potion_low':
            ally_drop_potion = 'HP소'
        elif ally_drop_item == 'MP_potion_high':
            ally_drop_potion = 'MP대'
        elif ally_drop_item == 'MP_potion_middle':
            ally_drop_potion = 'MP중'
        elif ally_drop_item == 'MP_potion_low':
            ally_drop_potion = 'MP소'
        elif ally_drop_item == 'All_potion_high':
            ally_drop_potion = 'ALL대'
        elif ally_drop_item == 'All_potion_middle':
            ally_drop_potion = 'ALL중'
        else:
            ally_drop_potion = 'ALL소'
        print('아군수호대로부터 {}를 나눔받았다.'.format(ally_drop_item))
        print('아군수호대로부터 {}를 나눔받았다.'.format(ally_drop_potion))
        return ally_drop_item

    # 적군수호대 만남
    def meet_enemy_gard(self, int_floor, str_my_gard):
        # 전투시작
        self.int_floor = int_floor
        if self.int_floor == 1:
            list_enemy_lvs = random.choices(range(20, 25), k=6)
            int_hp_up = 1.3
        elif self.int_floor == 2:
            list_enemy_lvs = random.choices(range(25, 30), k=6)
            int_hp_up = 1.3
        elif self.int_floor == 3:
            list_enemy_lvs = random.choices(range(30, 35), k=6)
            int_hp_up = 1.3 * 1.4
        elif self.int_floor == 4:
            list_enemy_lvs = random.choices(range(35, 40), k=6)
            int_hp_up = 1.3 * 1.4
        elif self.int_floor == 5:
            list_enemy_lvs = random.choices(range(45, 50), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5
        elif self.int_floor >= 6:
            list_enemy_lvs = random.choices(range(50, 100), k=6)
            int_hp_up = 1.3 * 1.4 * 1.5 * 1.6

        if str_my_gard == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'forest_gard'])
        elif str_my_gard == 'forest_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])


        # 나의 수호대, 시연님 상속
        self.dict_gard = {'gard': str_my_gard,
                          'location': {'region': '', 'x': 0, 'y': 0},
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
                                'warrior': {'lv': list_enemy_lvs[0], 'hp': 300*int_hp_up, 'mp': 0,
                                            'skill': {10: 'slice_chop'}, 'power': 200},
                                'archer': {'lv': list_enemy_lvs[1], 'hp': 150*int_hp_up, 'mp': 150*int_hp_up, 'power': 300,
                                           'skill': {10: 'target_shot',
                                                     15: 'dual_shot',
                                                     20: 'master_shot'}},
                                'swordman': {'lv': list_enemy_lvs[2], 'hp': 150*int_hp_up, 'mp': 150*int_hp_up, 'power': 250,
                                             'skill': {10: 'slice_chop'}},
                                'wizard_red': {'lv': list_enemy_lvs[3], 'hp': 150*int_hp_up, 'mp': 100*int_hp_up, 'power': 150,
                                               'skill': {1: ['heal_normal', 'fire_ball'],
                                                         15: ['heal_greater', 'fire_wall'],
                                                         20: 'thunder_breaker',
                                                         25: 'bilzzard',
                                                         30: 'heal_all'}},
                                'wizard_black': {'lv': list_enemy_lvs[4], 'hp': 200*int_hp_up, 'mp': 150*int_hp_up, 'power': 200,
                                                 'skill': {1: 'fire_ball',
                                                           15: 'fire_wall',
                                                           20: 'thunder_breaker',
                                                           25: 'bilzzard'}},
                                'wizard_white': {'lv': list_enemy_lvs[5], 'hp': 200*int_hp_up, 'mp': 150*int_hp_up, 'power': 100,
                                                 'skill': {1: 'heal_normal',
                                                           15: 'heal_greater',
                                                           30: 'heal_all'}}}
        print(self.int_floor,'층', '적수호대:', self.dict_enemy_gard, '나의 수호대:', self.dict_gard)
        return self.int_floor, self.dict_enemy_gard, self.dict_gard

    # 던전 보스 위치
    def boss_location(self, int_floor):
        # if self.current_floor == 1:
        #     self.boss_x = random.randint(0, self.first_width-1)
        #     self.boss_y = random.randint(0, self.first_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 2:
        #     self.boss_x = random.randint(0, self.second_width-1)
        #     self.boss_y = random.randint(0, self.second_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 3:
        #     self.boss_x = random.randint(0, self.third_width-1)
        #     self.boss_y = random.randint(0, self.third_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 4:
        #     self.boss_x = random.randint(0, self.fourth_width-1)
        #     self.boss_y = random.randint(0, self.fourth_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 5:
        #     self.boss_x = random.randint(0, self.fifth_width-1)
        #     self.boss_y = random.randint(0, self.fifth_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 6:
        #     self.boss_x = random.randint(0, self.sixth_width-1)
        #     self.boss_y = random.randint(0, self.sixth_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        # elif self.current_floor == 7:
        #     self.boss_x = random.randint(0, self.seventh_width-1)
        #     self.boss_y = random.randint(0, self.seventh_width-1)
        #     print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        self.int_floor = int_floor
        boss_x = random.randint(1, self.list_widths[self.int_floor-1])
        boss_y = random.randint(1, self.list_widths[self.int_floor-1])
        print("{}층 ({},{}) 보스몬스터".format(self.int_floor, boss_y, boss_x))
        return boss_y, boss_x

    # 던전 각 층 내 보스와 부하들 종류
    # 던전 보스 위치와 내 수호대의 위치가 동일한 경우 보스전 시작
    def boss_match(self, int_floor):
        self.int_floor = int_floor
        # 부하 몬스터들(0~6마리) 속성
        int_cnt = random.randint(0, 6)
        list_hp = random.sample(range(200, 1000), k=int_cnt)
        list_area = random.choices(['fire_area', 'water_area', 'forest_area', 'snow_area'], k=int_cnt)

        if self.int_floor == 1:
            self.int_boss_hp = random.randint(25000, 35000)
            self.dict_boss_monster = {'name': '이동려크', 'hp': self.int_boss_hp, 'attack': ['fan_attack', 0.05],
                                      'skill': ['hell_shouting', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 2:
            self.int_boss_hp = random.randint(45000, 55000)
            self.dict_boss_monster = {'name': '조동혀니', 'hp': self.int_boss_hp, 'attack': ['silent_attack', 0.05],
                                      'skill': ['hell_feedback', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 3:
            self.int_boss_hp = random.randint(65000, 75000)
            self.dict_boss_monster = {'name': '류홍거리', 'hp': self.int_boss_hp, 'attack': ['ignore_attack', 0.05],
                                      'skill': ['hell_ignore', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 4:
            self.int_boss_hp = random.randint(75000, 85000)
            self.dict_boss_monster = {'name': '코로나악마공주', 'hp': self.int_boss_hp, 'attack': ['virus_attack', 0.05],
                                      'skill': ['hell_virus', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 5:
            self.int_boss_hp = random.randint(85000, 599999)
            self.dict_boss_monster = {'name': '이땅복이', 'hp': self.int_boss_hp, 'attack': ['html_attack', 0.05],
                                      'skill': ['hell_task', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 6:
            int_boss_hp = random.randint(999999, 9999999)
            self.dict_boss_monster = {'name': '환생의 복이', 'hp': int_boss_hp, 'attack': ['python_attack', 0.05],
                                      'skill': ['hell_coding', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        elif self.int_floor == 7:
            self.int_boss_hp = 9999999
            self.dict_boss_monster = {'name': '로드오브보기', 'hp': self.int_boss_hp, 'attack': ['c_attack', 0.05],
                                      'skill': ['hell_boki', 0.1],
                                      'list_field_monster': [int_cnt, list_hp, list_area]}
        print(self.int_floor, self.dict_boss_monster)
        return self.int_floor, self.dict_boss_monster

    # 텔레포트 사용
    def use_teleport(self, int_floor):
        # self.dict_teleport_stock = dict_teleport_stock
        self.int_floor = int_floor
        if self.int_floor == 1:
            self.dict_teleport_stock['first'] -= 1
        elif self.int_floor == 2:
            self.dict_teleport_stock['second'] -= 1
        elif self.int_floor == 3:
            self.dict_teleport_stock['third'] -= 1
        elif self.int_floor == 4:
            self.dict_teleport_stock['fourth'] -= 1
        elif self.int_floor == 5:
            self.dict_teleport_stock['fifth'] -= 1
        elif self.int_floor == 6:
            self.dict_teleport_stock['sixth'] -= 1
        elif self.int_floor == 7:
            self.dict_teleport_stock['seventh'] -= 1
        print(self.dict_teleport_stock)
        return self.dict_teleport_stock

    # 필드로 텔레포트 사용시 필드 이동 위치
    def teleport_location(self):
        self.tele_x = random.randint(0, 19)
        self.tele_y = random.randint(0, 19)
        print('텔레포트를 사용해 필드({},{})로 이동'.format(self.tele_y, self.tele_x))
        return self.tele_y, self.tele_x

    # 텔레포트 사용 후 재입장시 이동위치
    def reentry_maze(self):
        # self.int_floor = int_floor
        self.reentry_maze_x = random.randint(1, self.list_widths[self.int_floor-1])
        self.reentry_maze_y = random.randint(1, self.list_widths[self.int_floor-1])
        print('{}층 {},{}로 재입장'.format(self.int_floor, self.reentry_maze_y, self.reentry_maze_x))
        self.use_teleport(self.int_floor)
        return self.reentry_maze_y, self.reentry_maze_x

    # 다음층으로 가는 계단 좌표
    def next_maze_entrance(self, int_floor):
        self.int_floor = int_floor
        self.int_next_entrance_x = random.randint(1, self.list_widths[self.int_floor-1])
        self.int_next_entrance_y = random.randint(1, self.list_widths[self.int_floor-1])
        print("{}층에서 다음층으로 가는 계단 좌표 {},{}".format(self.int_floor, self.int_next_entrance_y, self.int_next_entrance_x))
        return self.int_next_entrance_y, self.int_next_entrance_x

    # 7번째 전투까지는 다음 던전으로 가는 입구 유지, 8번째부터 계단 랜덤 재배치
    def change_entrance_location(self, int_floor, int_turn):
        if int_turn > 7:
            self.next_maze_entrance(int_floor)
        else:
            print('계단 입구 유지')


    # 보스 처치 유무 확인
    # 보스 죽인후 다음층 이동
    def next_maze(self, int_floor, bool_death_boss):
        if bool_death_boss:
            self.int_floor = int_floor
            self.int_floor += 1
            self.int_turn = 0
            self.int_current_x = random.randint(1, self.list_widths[self.int_floor-1])
            self.int_current_y = random.randint(1, self.list_widths[self.int_floor-1])
            print("{}층 {},{}로 진입".format(self.int_floor, self.int_current_y, self.int_current_x))
            return self.int_floor, self.int_current_y, self.int_current_x
        else:
            str_disable_next = "아직 보스를 죽이지 않아 다음층으로 이동할 수 없습니다."
            print(str_disable_next, '현재층:', self.int_floor)
            return str_disable_next

    # 도망 선택해 작동한 경우(전투에서 던전으로 빠져나옴)
    # 도망 성공 시 전투에서 던전으로 화면만 전환되고 이동하지 않으므로 이 함수는 필요없을듯 함
    # def escape_location(self, int_floor):
    #     self.int_floor = int_floor
    #     self.int_escape_x = random.randint(1, self.list_widths[self.int_floor-1])
    #     self.int_escape_y = random.randint(1, self.list_widths[self.int_floor-1])
    #     print('현재 {}층 {},{}로 도망'.format(self.int_floor, self.int_escape_y, self.int_escape_x))
    #     return self.int_floor, self.int_escape_y, self.int_escape_x

    #8층 복이 위치(구출하고 게임엔딩)
    def boki_location(self):
        if self.int_floor == 8:
            int_boki_x = random.randint(1, 4)
            int_boki_y = random.randint(1, 4)
            print("{}층 {},{} 복이 구출".format(self.int_floor, int_boki_y, int_boki_x))
            return int_boki_y, int_boki_x
        else:
            print('8층 아님')


# # DungeonClass().meet_monster(1)
# class_a = DungeonClass()
# # 8층 복이 구출
# class_a.boki_location(8)
# # 전투 중 도망 성공해 던전으로 나옴
# class_a.escape_location(6)
# # 다음층 이동(보스 죽인 경우 다음층 이동, 보스 못해치웠으면 이동 불가)
# class_a.next_maze(4, True)
# class_a.next_maze(4, False)
# # 텔레포트 사용
# class_a.use_teleport(4)
# class_a.use_teleport(5)
# class_a.teleport_location()
# # 다시 던전 안으로 재입장
# class_a.reentry_maze()
# # 보스위치
# print('던전 각 층 보스위치')
# class_a.boss_location(1)
# class_a.boss_location(2)
# class_a.boss_location(3)
# class_a.boss_location(4)
# class_a.boss_location(5)
# class_a.boss_location(6)
# class_a.boss_location(7)
# print()
# # 보스전
# class_a.boss_match(1)
# class_a.boss_match(2)
# class_a.boss_match(3)
# class_a.boss_match(4)
# class_a.boss_match(5)
# class_a.boss_match(6)
# class_a.boss_match(7)
# print()
# # 던전 일반몬스터 만남
# class_a.meet_monster(1, 'star_gard')
# print()
# # 아군 수호대 만남
# class_a.meet_ally_gard()
# print()
# # 적군 수호대 만남
# class_a.meet_enemy_gard(3, 'moon_gard')
# print()
# # 클래스, 메소드 호출 시 인자 없어도 괄호 붙이기
# # print(DungeonClass().dict_teleport_stock)
# # DungeonClass().meet_monster(2)
# class_a.move_event(1, 'light_gard')
# class_a.next_maze_entrance(6)
# class_a.change_entrance_location(6, 10)

class_b = DungeonClass()
print('>>>던전 맵 내 이동시 이벤트')
class_b.move_event(class_b.int_floor, 'moon_gard')
print()
print('>>>보스몬스터 위치')
class_b.boss_location(class_b.int_floor)
print()
print('>>>보스몬스터 위치에 도달한 경우 전투 시작')
class_b.boss_match(class_b.int_floor)
print()
print('>>>다음층 계단 입구 위치')
class_b.next_maze_entrance(class_b.int_floor)
print()
print('>>>다음층 입구 도달시 보스처치 유무에 따른 결과')
class_b.next_maze(class_b.int_floor, bool_death_boss=True)
class_b.next_maze(class_b.int_floor, bool_death_boss=False)
class_b.change_entrance_location(class_b.int_floor, int_turn=7)
class_b.change_entrance_location(class_b.int_floor, int_turn=8)
print(class_b.int_floor, '층')
print()
print('>>>텔레포트 사용')
class_b.use_teleport(class_b.int_floor)
class_b.teleport_location()
class_b.reentry_maze()
print(class_b.int_floor)
print()
print('>>>이상복 구출')
class_b.boki_location()
class_b.int_floor = 8
class_b.boki_location()







import random

class Common():
    def __init__(self, **kwargs):
        if 'field' in kwargs:
            self.field = kwargs['field']
        if 'gard' in kwargs:
            self.gard = kwargs['gard']
        if 'monster' in kwargs:
            self.moster = kwargs['monster']
        if 'item' in kwargs:
            self.item = kwargs['item']
        if 'maze' in kwargs:
            self.tower = kwargs['maze']

        self.field_list = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        self.gard_list = ['light_gard', 'moon_gard', 'star_gard', 'forest_gard']
        self.monster_list = ['fire_field_moster', 'water_field_moster', 'forest_field_moster', 'snow_field_moster']
        self.item_list = ['meteorite', 'tent', 'HP_potion_high', 'HP_potion_middle', 'HP_potion_low', 'MP_potion_high',
                          'MP_potion_middle', 'MP_potion_low', 'All_potion_high', 'All_potion_middle', 'All_potion_low',
                          'survival']
        self.move_drop_list = ['HP_potion_high', 'HP_potion_middle', 'HP_potion_low', 'MP_potion_high', 'MP_potion_middle',
                               'MP_potion_low', 'All_potion_high', 'All_potion_middle', 'All_potion_low']
        self.maze_list = ['maze_way', 'random_maze_way']
        self.meteorite = ['meteorite_item']
        self.user_state_list = ['job', 'lv', 'hp', 'mp', 'exp', 'skil', 'power']
        # self.turn = 0

    def random_field(self): # 랜덤 필드
        rand_field_way = random.choice(self.field_list)
        print(f"나의 용병단 {rand_field_way}의 위치에 생성")

    def random_user_gard(self): # 랜덤 유저 속성 수호대
        rand_user_gard = random.choice(self.gard_list)
        print(f"나의 수호대 {rand_user_gard}로 생성")

    def random_maze_start(self): # 랜덤한 위치에 던전 입구 생성
        # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
        rand_maze_start = random.randint(0, 20)
        rand_maze_start_ = random.randint(0, 20)
        print(f"랜덤 던전 좌표 X {rand_maze_start} Y {rand_maze_start_}")

    def random_meteorite_way(self): # 랜덤한 위치에 운석 생성
        rand_met_way = random.randint(0, 20)
        rand_met_way_ = random.randint(0, 20)
        print(f"랜덤 운석 좌표 X {rand_met_way}, Y {rand_met_way_}")
        # self.inven.append(self.meteorite)

    def field_area(self): # 지역
        print('\n')
        for i in range(10):
            print("'불'"*10,'"눈"'*10, end="\n")

        for i in range(10):
            print("'숲'"*10,'"물"'*10, end="\n")

    def feild_move_random_drop(self): # 필드 이동 중 랜덤 드랍
        drop_list = random.choice(self.move_drop_list)
        print(drop_list)


a = Common()
a.random_field()
b = Common()
b.random_user_gard()
c = Common()
c.random_maze_start()
d = Common()
d.random_meteorite_way()
e = Common()
e.field_area()
f = Common()
f.feild_move_random_drop()

# 시작 버튼 클릭 시 필드에서 4개지역 [불, 물, 숲, 눈] 중 랜덤한 위치에 수호대가 생성된다.0
# 플레이어의 특정 수호대를 제외한 나머지 특정 타 수호대를 생성한다.
# 방향키를 지정하여 맵을 이동한다 # 공통
# 각 지역 이동 중 지역의 고유 몬스터를 일정 확률로 몬스터가 출몰한다.
# 던전 입구는 필드 내 랜덤한 위치에 생성된다. 0
# 이동 중 랜덤한 위치에 운석이 존재하며 획득한다. 0
# 이동 중 일정 확률로 아이템 획득이 가능하다. (부활포션, 장비아이템 제외) 0
# 이동 중 일정 확률로 타 수호대와 조우 한다.
# 11번째 전투까지 던전 입구 못찾을시 랜덤한 위치에 재생성 !
# 각 지역 필드 몬스터 설정
# 각 지역 설정 0


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

# import random
# #층별 면적 결정
# class DungeonArea():
#     def __init__(self):
#         self.widths = random.choices([15, 16, 17, 18], k=7)
#         self.widths.append(4)
#         print(self.widths)
#         self.first_width = self.widths[0]
#         self.second_width = self.widths[1]
#         self.third_width = self.widths[2]
#         self.fourth_width = self.widths[3]
#         self.fifth_width = self.widths[4]
#         self.sixth_width = self.widths[5]
#         self.seventh_width = self.widths[6]
#         self.eighth_width = self.widths[7]
#
#     # 던전 보스 위치
#     def boss_location(self, current_floor):
#         self.current_floor = current_floor
#         if self.current_floor == 1:
#             self.boss_x = random.randint(0, self.first_width-1)
#             self.boss_y = random.randint(0, self.first_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 2:
#             self.boss_x = random.randint(0, self.second_width-1)
#             self.boss_y = random.randint(0, self.second_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 3:
#             self.boss_x = random.randint(0, self.third_width-1)
#             self.boss_y = random.randint(0, self.third_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 4:
#             self.boss_x = random.randint(0, self.fourth_width-1)
#             self.boss_y = random.randint(0, self.fourth_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 5:
#             self.boss_x = random.randint(0, self.fifth_width-1)
#             self.boss_y = random.randint(0, self.fifth_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 6:
#             self.boss_x = random.randint(0, self.sixth_width-1)
#             self.boss_y = random.randint(0, self.sixth_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#         elif self.current_floor == 7:
#             self.boss_x = random.randint(0, self.seventh_width-1)
#             self.boss_y = random.randint(0, self.seventh_width-1)
#             print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
#
#     # 보스 hp
#     def boss_match(self, floor):
#         self.floor = floor
#         self.boss_hp = 0
#         if self.floor == 1:
#             self.boss_hp = random.randint(25000, 35000)
#         elif self.floor == 2:
#             self.boss_hp = random.randint(45000, 55000)
#         elif self.floor == 3:
#             self.boss_hp = random.randint(65000, 75000)
#         elif self.floor == 4:
#             self.boss_hp = random.randint(75000, 85000)
#         elif self.floor == 5:
#             self.boss_hp = random.randint(85000, 599999)
#         elif self.floor == 6:
#             self.boss_hp = random.randint(999999, 9999999)
#         elif self.floor == 7:
#             self.boss_hp = 9999999
#         elif self.floor == 8:
#             print('용사 복이 구출')
#
#     # 텔레포트 사용
#     def teleport_use(self, current_floor):
#         self.teleport_stock = {'first': 5, 'second': 5, 'third': 5, 'fourth': 5, 'fifth': 5, 'sixth': 5, 'seventh': 5}
#         self.current_floor = current_floor
#         if current_floor == 1:
#             self.teleport_stock['first'] -= 1
#         elif current_floor == 2:
#             self.teleport_stock['second'] -= 1
#         elif current_floor == 3:
#             self.teleport_stock['third'] -= 1
#         elif current_floor == 4:
#             self.teleport_stock['fourth'] -= 1
#         elif current_floor == 5:
#             self.teleport_stock['fifth'] -= 1
#         elif current_floor == 6:
#             self.teleport_stock['sixth'] -= 1
#         elif current_floor == 7:
#             self.teleport_stock['seventh'] -= 1
#
#     # 텔레포트 이동 위치
#     def teleport_location(self):
#         self.tele_x = random.randint(19)
#         self.tele_y = random.randint(19)
#         print('텔레포트를 사용해 필드({},{})로 이동'.format(self.tele_y, self.tele_x))

import random
#호할란아ㅣ닞ㄷㄹ
#층별 면적 결정
class DungeonArea():
    def __init__(self, **kwargs):
        if 'current_floor' in kwargs:
            self.current_floor = kwargs['current_floor']

        # self.teleport_stock = {'first': 5, 'second': 5, 'third': 5, 'fourth': 5, 'fifth': 5, 'sixth': 5, 'seventh': 5}
        self.teleport_stock = {1: 5, 2: 5, 3: 5, 4: 5, 6: 5, 7: 5}
        self.widths = random.choices([15, 16, 17, 18], k=7)
        self.widths.append(4)
        self.widths = tuple(self.widths)
        print(self.widths)

        self.first_width = self.widths[0]
        self.second_width = self.widths[1]
        self.third_width = self.widths[2]
        self.fourth_width = self.widths[3]
        self.fifth_width = self.widths[4]
        self.sixth_width = self.widths[5]
        self.seventh_width = self.widths[6]
        self.eighth_width = self.widths[7]

        # 클리어한 층(보스몬스터를 해치운 층)
        self.cleared_floors = []
        for i in range(1, self.current_floor):
            self.cleared_floors.append(i)
        # print(self.cleared_floors)


    # 던전 보스 위치
    def boss_location(self):
        if self.current_floor == 1:
            self.boss_x = random.randint(0, self.first_width-1)
            self.boss_y = random.randint(0, self.first_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 2:
            self.boss_x = random.randint(0, self.second_width-1)
            self.boss_y = random.randint(0, self.second_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 3:
            self.boss_x = random.randint(0, self.third_width-1)
            self.boss_y = random.randint(0, self.third_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 4:
            self.boss_x = random.randint(0, self.fourth_width-1)
            self.boss_y = random.randint(0, self.fourth_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 5:
            self.boss_x = random.randint(0, self.fifth_width-1)
            self.boss_y = random.randint(0, self.fifth_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 6:
            self.boss_x = random.randint(0, self.sixth_width-1)
            self.boss_y = random.randint(0, self.sixth_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))
        elif self.current_floor == 7:
            self.boss_x = random.randint(0, self.seventh_width-1)
            self.boss_y = random.randint(0, self.seventh_width-1)
            print("{}층({},{})에 보스".format(self.current_floor, self.boss_y, self.boss_x))

    # 보스 hp
    def boss_match(self):
        self.boss_hp = 0
        if self.current_floor == 1:
            self.boss_hp = random.randint(25000, 35000)
        elif self.current_floor == 2:
            self.boss_hp = random.randint(45000, 55000)
        elif self.current_floor == 3:
            self.boss_hp = random.randint(65000, 75000)
        elif self.current_floor == 4:
            self.boss_hp = random.randint(75000, 85000)
        elif self.current_floor == 5:
            self.boss_hp = random.randint(85000, 599999)
        elif self.current_floor == 6:
            self.boss_hp = random.randint(999999, 9999999)
        elif self.current_floor == 7:
            self.boss_hp = 9999999
        elif self.current_floor == 8:
            print('용사 복이 구출')

    # 텔레포트 사용
    def teleport_use(self):
        if self.current_floor == 1:
            self.teleport_stock[1] -= 1
            print(self.teleport_stock[1])
        elif self.current_floor == 2:
            self.teleport_stock[2] -= 1
            print(teleport_stock[2])
        elif self.current_floor == 3:
            self.teleport_stock[3] -= 1
        elif self.current_floor == 4:
            self.teleport_stock[4] -= 1
        elif self.current_floor == 5:
            self.teleport_stock[5] -= 1
        elif self.current_floor == 6:
            self.teleport_stock[6] -= 1
        elif self.current_floor == 7:
            self.teleport_stock[7] -= 1

    # 텔레포트 사용시 필드 이동 위치
    def teleport_location(self):
        self.tele_x = random.randint(0, 19)
        self.tele_y = random.randint(1, 19)
        print('텔레포트를 사용해 필드({},{})로 이동'.format(self.tele_y, self.tele_x))

    # 텔레포트 사용 후 재입장시 이동위치
    def come_back(self):
        self.come_back_x = random.randint(0, self.widths[self.current_floor-1])
        self.come_back_y = random.randint(0, self.widths[self.current_floor-1])
        print('{}층 {},{}로 재입장'.format(self.current_floor, self.come_back_y, self.come_back_x))

    # 다음층 이동
    def next_dungeon(self):
        if self.current_floor == 1:
            self.current_floor += 1
            self.current_x = random.randint(0, self.widths[1]-1)
            self.current_y = random.randint(0, self.widths[1]-1)
            print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
            # print(self.current_y)

DungeonArea(current_floor=1).next_dungeon()
DungeonArea(current_floor=1).teleport_use()
DungeonArea(current_floor=1).teleport_location()
DungeonArea(current_floor=1).come_back()
print(DungeonArea(current_floor=3).cleared_floors)


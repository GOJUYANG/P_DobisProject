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
#층별 면적 결정
class DungeonClass():
    def __init__(self, **kwargs):
        #던전입장 후 현재 층 : current_floor = 1
        if 'current_floor' in kwargs:
            self.int_current_floor = kwargs['current_floor']

        self.dict_teleport_stock = {1: 5, 2: 5, 3: 5, 4: 5, 6: 5, 7: 5}
        self.list_widths = random.choices([15, 16, 17, 18], k=7)
        self.list_widths.append(4)
        self.tuple_widths = tuple(self.list_widths)
        print(self.tuple_widths)

        self.first_width = self.tuple_widths[0]
        self.second_width = self.tuple_widths[1]
        self.third_width = self.tuple_widths[2]
        self.fourth_width = self.tuple_widths[3]
        self.fifth_width = self.tuple_widths[4]
        self.sixth_width = self.tuple_widths[5]
        self.seventh_width = self.tuple_widths[6]
        self.eighth_width = self.tuple_widths[7]

    #일반몬스터 만남(1~10마리)
    def meet_monster(self):
        self.int_monster_count = random.randint(1, 10)

    #아군 수호대 만남
    def meet_army(self):
        #9개의 포션, 장비들 중 하나 드랍
        pass

    #적군수호대 만남
    def meet_enemy(self):
        #전투시작


    # 던전 보스 위치
    def boss_location(self):
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
        self.boss_x = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        self.boss_y = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        print("{}층 ({},{}) 보스몬스터".format(self.int_current_floor, self.boss_y, self.boss_x))

    # 보스 hp
    def boss_match(self):
        self.int_boss_hp = 0
        if self.int_current_floor == 1:
            self.int_boss_hp = random.randint(25000, 35000)
        elif self.int_current_floor == 2:
            self.int_boss_hp = random.randint(45000, 55000)
        elif self.int_current_floor == 3:
            self.int_boss_hp = random.randint(65000, 75000)
        elif self.int_current_floor == 4:
            self.int_boss_hp = random.randint(75000, 85000)
        elif self.int_current_floor == 5:
            self.int_boss_hp = random.randint(85000, 599999)
        elif self.int_current_floor == 6:
            self.int_boss_hp = random.randint(999999, 9999999)
        elif self.int_current_floor == 7:
            self.int_boss_hp = 9999999
        elif self.int_current_floor == 8:
            print('용사 복이 구출')

    # 텔레포트 사용
    def teleport_use(self):
        if self.int_current_floor == 1:
            self.dict_teleport_stock[1] -= 1
            print(self.dict_teleport_stock[1])
        elif self.int_current_floor == 2:
            self.dict_teleport_stock[2] -= 1
            print(self.dict_teleport_stock[2])
        elif self.int_current_floor == 3:
            self.dict_teleport_stock[3] -= 1
        elif self.int_current_floor == 4:
            self.dict_teleport_stock[4] -= 1
        elif self.int_current_floor == 5:
            self.dict_teleport_stock[5] -= 1
        elif self.int_current_floor == 6:
            self.dict_teleport_stock[6] -= 1
        elif self.int_current_floor == 7:
            self.dict_teleport_stock[7] -= 1

    # 텔레포트 사용시 필드 이동 위치
    def teleport_location(self):
        self.tele_x = random.randint(0, 19)
        self.tele_y = random.randint(0, 19)
        print('텔레포트를 사용해 필드({},{})로 이동'.format(self.tele_y, self.tele_x))

    # 텔레포트 사용 후 재입장시 이동위치
    def come_back(self):
        self.come_back_x = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        self.come_back_y = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        print('{}층 {},{}로 재입장'.format(self.int_current_floor, self.come_back_y, self.come_back_x))

    # 보스 죽인후 다음층 이동
    def next_dungeon(self):
        # if self.current_floor == 1:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.second_width-1) #self.widths[self.current_floor]-1
        #     self.current_y = random.randint(0, self.second_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        #     # print(self.current_y)
        # elif self.current_floor == 2:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.third_width-1)
        #     self.current_y = random.randint(0, self.third_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        # elif self.current_floor == 3:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.fourth_width-1)
        #     self.current_y = random.randint(0, self.fourth_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        # elif self.current_floor == 4:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.fifth_width-1)
        #     self.current_y = random.randint(0, self.fifth_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        # elif self.current_floor == 5:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.sixth_width-1)
        #     self.current_y = random.randint(0, self.sixth_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        # elif self.current_floor == 6:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.seventh_width-1)
        #     self.current_y = random.randint(0, self.seventh_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        # elif self.current_floor == 7:
        #     self.current_floor += 1
        #     self.current_x = random.randint(0, self.eighth_width-1)
        #     self.current_y = random.randint(0, self.eighth_width-1)
        #     print("{}층 {},{}에 입장".format(self.current_floor, self.current_y, self.current_x))
        self.int_current_floor += 1
        self.current_x = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        self.current_y = random.randint(0, self.tuple_widths[self.int_current_floor-1]-1)
        print("{}층 {},{}로 진입".format(self.int_current_floor, self.current_y, self.current_x))

    def boki_location(self):
        if self.int_current_floor == 8:
            self.int_boki_x = random.randint(0, 3)
            self.int_boki_y = random.randint(0, 3)
            print("{}층 {},{} 복이 구출".format(self.int_current_floor, self.int_boki_y, self.int_boki_x))


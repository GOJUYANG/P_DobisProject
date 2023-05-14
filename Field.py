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
# 방향키를 지정하여 맵을 이동한다
# 각 지역 이동 중 지역의 고유 몬스터를 일정 확률로 몬스터가 출몰한다.
# 던전 입구는 필드 내 랜덤한 위치에 생성된다. 0
# 이동 중 랜덤한 위치에 운석이 존재하며 획득한다. 0
# 이동 중 일정 확률로 아이템 획득이 가능하다. (부활포션, 장비아이템 제외)
# 이동 중 일정 확률로 타 수호대와 조우 한다.
# 11번째 전투까지 던전 입구 못찾을시 랜덤한 위치에 재생성
# 각 지역 필드 몬스터 설정
# 각 지역 설정 0




#
# 필드
# Field()
# 게임시작 버튼이 눌리면 불,물,숲,눈 의 지역 중 랜덤으로 수호대가 생성된다.
#
# 불, 물, 숲,  눈 지역
# fire_Area
# water_Area
# forest_Area
# snow_Area
# 4개의 지역 이동중 텐트 드롭 10%, 타 수호대 만날 20%, 성공적 이동 20%, 성공적이동20%+포션획득20%,
# 몬스터 만날 20% 이며 특정지역의 자리에 운석이 숨겨져 있음
#
# 던전입구
# tower_random_way
# 던전 입구는 클래스 전체 레벨이 30이 달성되면 랜덤으로 던전 입구가 생성된다.
#
# 필드몬스터
# area_fire
# area_water
# area_forest
# area_snow
#
#
# 각 지역마다 지역의 몬스터가 존재하며 이동시 30% 확률로 몬스터가 출몰한다.
#
# 운석 (게임 시작시 필드 랜덤한 위치에 생성, 발견시 아이템 획득)
# field_random_meteorite
#
# 필드 수호대
# light_gard
# moon_gard
# star_gard
# earth_gard
#
# 필드내 수호대 조우(20% 확률)
# random_gard
#
# 아이템 흭득 (이동중 일정한 확률로 설정한 확률 포션 드랍 20%)
# field_item_drop
#
# 텐트 사용 (모든 수호대의 체력이 100% 상승/ 팀원 부활)
# Tent
#
#
#
# 처음 수호대를 생성 하면 (불, 물, 숲, 눈) 지역의 수호대에 랜덤으로 생성되며 수호대의 종류는 (빛, 달, 별, 대지)의
# 수호대가 존재 한다. 4개의 지역을 수호대가 이동키를 이용하여 이동을 하게 되며 이동중
# (텐트 드롭 10%, 몬스터 출몰 30%, 타수호대 출몰 20%, 패스 20%,포션+패스 확률 20%)
# 상황이 발생할 수 있고 텐트 드롭 및 텐트사용을 하게 되면 전투불능 상태와 일반 경우에는 HP/MP가 100%채워지며
# 몬스터나 타 수호대 출몰시 각 지역의 고유 몬스터 와 타 수호대 와 턴제전투를 치루게 되며 전투상태에서는 1 공격 2 스킬 3 아이템 4 도망 을 선택할 수
# 있으며 공격 선택시 몬스터를 일반 공격을 하고 스킬을 선택 하면 클래스의 고유스킬을 발동 할 수 있다 . 아이템을 선택시
# 전투 중 물약 섭취가 가능하며 도망을 선택할 시 1~30%의 확률로 도망을 갈 수 있다. 도망 실패시 현재 나의 턴은 끝이나고
# 몬스터와 타 수호대의 턴으로 돌아간다 . 도망에 성공 하였을 시 전투는 종료되며 전투 전의 위치로 복귀하고
# 이동중 20% 의 확률로 포션을 획득 할 수 있으며 포션은 부활포션과 텐트를 제외한 포션을 랜덤으로 획득 할 수 있다.
# 필드에서 타 수호대와 조우시 타 수호대의 평균 레벨대는 15~20레벨 이다 [ ? ]
# 필드 몬스터 가 출몰시 1~10마리 랜덤 [ ? ] 으로 등장하며 각 지역별로 몬스터의 기본공격과 스킬공격이 있으며
# 기본 공격은 클래스의 HP 5% 가 차감되며 스킬 발동시 클래스의 HP 10%가 차감되며 필드 몬스터의 체력은 200~1000 사이 랜덤으로 출몰 한다
# 전투가 승리할 시 경험치(턴) 과 아이템이 드롭되며 포션은 부활 포션을 제외한 나머지 포션들이 랜덤으로 드랍되며
# 장비,무기 아이템은 각 지역 몬스터가 뱉는 아이템의 종류가 다르니 속성값 파일을 참고한다.
# 전투 중 전원 사망으로 전투불가능 상태일 경우 전투는 종료되고 필드로 이동하며 텐트,부활포션을 사용하여 부활을 시킬 수 있으며
# 텐트, 부활포션 을 소지하지 않고 있으면 패배엔딩이 된다.
# 필드 내에는 던전으로 가는 입구는 4지역 중 1지역에 랜덤한 위치에 존재하며 레벨 30이 [ ? ] 입장 조건이며
# 10번째 전투안에 던전을 입장하지 못하면 11번째 전투가 끝나는 동시에 던전 입구는 랜덤하게 재배치가 된다.
# 필드 내에 운석이 랜덤한 위치에 존재 하며 운석을 찾음과 동시 운석을 소지 할 수 있으며 운석은 던전 보스의 체력을 일정비율
# 차감 시킬 수 있으며 필드에서 운석을 찾지 못하더라도 던전 1, 2, 3  층 보스를 처치 할 시 일정 확률로 좌표를 얻을 수 있다.
#
#
# 1단 오늘 카페에서 본 코드를 잘 파헤쳐보자. tqtqtqtqtqtqtqtqtqtqtq



# import random
#
# class Common():
#     def __init__(self, **kwargs):
#         if 'field' in kwargs:
#             self.field = kwargs['field']
#         if 'gard' in kwargs:
#             self.gard = kwargs['gard']
#         if 'monster' in kwargs:
#             self.moster = kwargs['monster']
#         if 'meteorite' in kwargs:
#             self.meteorite = kwargs['meteorite']
#         if 'item' in kwargs:
#             self.item = kwargs['item']
#         if 'tower' in kwargs:
#             self.tower = kwargs['tower']
#         if 'user' in kwargs:
#             self.user = kwargs['user']
#
#         self.field_list = ['fire_area', 'water_area', 'forest_area', 'snow_area']
#         self.gard_list = ['light_gard', 'moon_gard', 'star_gard', 'forest_gard']
#         self.monster_list = ['fire_field_moster', 'water_field_moster', 'forest_field_moster', 'snow_field_moster']
#         self.item_list = ['meteorite', 'tent']
#         self.tower_list = ['tower_way', 'tower_start'] # 혹시나 해서!
#         self.meteorite_l = ['meteorite_way', 'meteorite_item']
#         self.user_state_list = ['lv', 'hp', 'mp', 'exp', 'skil', 'power']
#
#     def random_field(self):
#         rand_field_way = random.choice(self.field_list)
#         print(rand_field_way)
#
#     def random_user_gard(self):
#         rand_user_gard = random.choice(self.gard_list)
#         print(rand_user_gard)
#
#
# a = Common()
# a.random_field()
# b = Common()
# b.random_user_gard()
#
# # 시작 버튼 클릭 시 필드에서 4개지역 [ 불 물 숲 눈 ] 중 랜덤한 위치에 수호대가 생성된다.
# # 플레이어의 특정 수호대를 제외한 나머지 특정 타 수호대를 생성한다.
# # 방향키를 지정하여 맵을 이동한다
# # 각 지역 이동 중 지역의 고유 몬스터를 일정 확률로 몬스터가 출몰한다.
# # 던전 입구는 필드 내 랜덤한 위치에 생성된다.
# # 이동 중 랜덤한 위치에 운석이 존재하며 획득한다.
# # 이동 중 일정 확률로 아이템 획득이 가능하다. (부활포션, 장비아이템 제외)
# # 이동 중 일정 확률로 타 수호대와 조우 한다.
# # 11번째 전투까지 던전 입구 못찾을시 랜덤한 위치에 재생성
# # 각 지역 필드 몬스터 설정
# #
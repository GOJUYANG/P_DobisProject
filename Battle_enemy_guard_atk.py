import random

class My():
    def __init__(self, bool_meet_gard, bool_meet_maze_gard, int_floor, dict_enemy_gard):
        self.bool_meet_gard = bool_meet_gard
        self.bool_meet_maze_gard = bool_meet_maze_gard
        self.int_floor = int_floor
        self.dict_enemy_gard = dict_enemy_gard

        self.dict_user_gard = {'gard': '',
                  'location': {'region': '', 'x': 0, 'y': 0},
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
                                             10: 'hp_up',
                                             15: 'heal_greater',
                                             30: 'heal_all'}}}

        self.int_hp_up = 1.2
        self.dict_enemy_gard = {'gard': 'moon_gard',
                                'warrior': {'lv': 15, 'hp': 300 * self.int_hp_up, 'max_hp': 300 * self.int_hp_up, 'mp': 0,
                                            'skill': {10: 'slice_chop'}, 'power': 200},
                                'archer': {'lv': 16, 'hp': 150 * self.int_hp_up, 'max_hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                           'power': 300,
                                           'skill': {10: 'target_shot',
                                                     15: 'dual_shot',
                                                     20: 'master_shot'}},
                                'swordman': {'lv': 17, 'hp': 150 * self.int_hp_up, 'max_hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                             'power': 250,
                                             'skill': {10: 'slice_chop'}},
                                'wizard_red': {'lv': 18, 'hp': 150 * self.int_hp_up, 'max_hp': 150 * self.int_hp_up,
                                               'mp': 100 * self.int_hp_up,
                                               'power': 150,
                                               'skill': {1: ['heal_normal', 'fire_ball'],
                                                         15: ['heal_greater', 'fire_wall'],
                                                         20: 'thunder_breaker',
                                                         25: 'bilzzard',
                                                         30: 'heal_all'}},
                                'wizard_black': {'lv': 19, 'hp': 200 * self.int_hp_up, 'max_hp': 200 * self.int_hp_up,
                                                 'mp': 150 * self.int_hp_up,
                                                 'power': 200,
                                                 'skill': {1: 'fire_ball',
                                                           15: 'fire_wall',
                                                           20: 'thunder_breaker',
                                                           25: 'bilzzard'}},
                                'wizard_white': {'lv': 20, 'hp': 200 * self.int_hp_up, 'max_hp': 200 * self.int_hp_up,
                                                 'mp': 150 * self.int_hp_up,
                                                 'power': 100,
                                                 'skill': {1: 'heal_normal',
                                                           10: 'hp_up',
                                                           15: 'heal_greater',
                                                           30: 'heal_all'}}}
        
        self.use_hp_up = False
        self.use_fire_wall = False
        self.use_thunder_breaker = False
        self.use_bilzzard = False


    def enemy_gard_atk(self):
        list_job = ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white']
        # use
        # 일반/스킬/아이템 중 선택
        int_enemy_choice_act = random.randint(1, 3)
        # 필드에서 적수호대 만남
        if self.bool_meet_gard:
            # 필드에서 일반공격
            if int_enemy_choice_act == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(list_job)
                print('필드 일반공격 공격자', str_choice_enemy_gard)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                print('필드 일반공격 피해자', str_choice_user_gard)
                # 유저수호대 피해자 공격받아 hp감소(공격력 증가시키는 버프 사용 고려)
                if self.use_hp_up:  # 백법사 hp_up버프
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * (
                            1 + random.randint(5, 7) / 10)
                    print(self.dict_user_gard[str_choice_user_gard]['hp'])
                    print(self.dict_enemy_gard[str_choice_enemy_gard]['power'])
                    print(1 + random.randint(5, 7) / 10)
                    print('백법사의 hp_up 버프마법 사용함')
                    self.use_hp_up = False
                elif self.use_fire_wall:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.5
                    print('fire_wall버프 발동')
                    self.use_fire_wall = False
                elif self.use_thunder_breaker:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.6
                    print('thunder_breaker 버프 발동')
                    self.use_thunder_breaker = False
                else:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power']
                    print('bilzzard 버프발동')
                    self.use_bilzzard = False


            # 필드에서 스킬사용(궁수, 검사, 마법사들만 가능)-필드 적수호대 레벨 15~20
            elif int_enemy_choice_act == 2:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                print('필드 스킬 공격자', str_choice_enemy_gard)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                print('필드 스킬 피해자', str_choice_user_gard)
                # 적수호대 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    # 적수호대 궁수 레벨이 20미만인 경우 사용 가능한 스킬
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([10, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'target_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                          * (1 + random.randint(2, 5) / 10)
                            print("필드 아처 타겟샷 발동")
                        elif str_enemy_skill == 'dual_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                          * (1 + random.randint(4, 6) / 10)
                            print('필드 궁수 20레벨 미만 사용한 스킬', str_enemy_skill)
                    else:  # 적수호대 궁수 레벨이 20인 경우 가능한 스킬
                        skill_num = random.choice([10, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'target_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                          * (1 + random.randint(2, 5) / 10)
                            print("필드 레벨 20 경우 아처 타겟샷 발동")
                        elif str_enemy_skill == 'dual_shot':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                          * (1 + random.randint(4, 6) / 10)
                            print("필드 레벨 20 경우 아처 듀얼샷 발동")
                        else:
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                          * (1 + random.randint(5, 7) / 10)
                            print('필드 궁수 20레벨 이상 사용한 스킬', str_enemy_skill)

                # 적수호대 검사 필드에서 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                      'power'] * random.randint(2, 50)
                    print('필드 검사 스킬 사용')
                # 적수호대 흑법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_black':
                    # 적수호대 흑법사 레벨 20 미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([1, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                              'power'] * 1.3
                            print("필드 20미만 흑법사 파이어볼 발사")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print('필드 흑법사 20레벨 미만 스킬 사용', str_enemy_skill)
                    # 적수호대 흑법사 레벨 20이상
                    else:
                        skill_num = random.choice([1, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                              'power'] * 1.3
                            print("적수호대 흑법사 레벨 20 이상 필드 파이어볼 발사")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("필드 흑법사 20레벨 이상 파이어 월 스킬사용", self.use_fire_wall)
                        else:
                            self.use_thunder_breaker = True
                            print('필드 흑법사 20레벨 이상 썬더 브레이커 사용', self.use_thunder_breaker)

                # 적수호대 백법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * self.dict_enemy_gard[str_heal_enemy][
                            'max_hp'] / 10
                        print("적수호대 백법사 필드 힐 노말 스킬 사용")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("적수호대 백법사 필드 에이치업 스킬사용", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * self.dict_enemy_gard[str_heal_enemy][
                            'max_hp'] / 10
                        print('필드 백법사 힐 그레이터 스킬사용', str_enemy_skill)
                # 적수호대 적법사 필드에서 스킬사용
                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    # 적법사 레벨 20미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 20:
                        skill_num = random.choice([1, 15])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                         self.dict_enemy_gard[str_heal_enemy][
                                                                             'max_hp'] / 10
                                print("적법사 필드 20미만 힐 노말 스킬사용")
                            else:  # fire_ball 사용
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                                  'power'] * 1.3
                                print("적법사 필드 20미만 파이어 볼 스킬사용")
                        # 적법사 15레벨부터 사용 가능한 스킬
                        else:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                         self.dict_enemy_gard[str_heal_enemy][
                                                                             'max_hp'] / 10
                                print("적법사 필드 힐그레이터 스킬 사용")
                            else:  # fire_wall 광역스킬 사용
                                self.use_fire_wall = True
                                print('필드 적법사 20레벨 미만 스킬 사용', self.use_fire_wall)
                    else:   #필드 적법사 레벨 20 이상
                        skill_num = random.choice([1, 15, 20])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print('필드 적법사 힐노말 사용')
                            else:  # fire_ball 사용
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= \
                                self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.3
                                print('필드 적법사 파이어월 사용')
                        # 적법사 15레벨부터 사용 가능한 스킬
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                              self.dict_enemy_gard[str_heal_enemy][
                                                                                  'max_hp'] / 10
                                print('필드 적법사 20레벨 이상 스킬사용', str_enemy_skill)
                            else:  # fire_wall 광역스킬 사용
                                self.use_fire_wall = True
                                print('필드 적법사 20레벨 이상 파이어월 사용', self.use_fire_wall)

                        else:
                            self.use_thunder_breaker = True
                            print('필드 적법사 20레벨 이상 썬더브레이커 스킬사용', self.use_thunder_breaker)

            #  필드에서 아이템 사용
            else:
                # 적수호대 공격자(아이템 사용자) 선택
                str_choice_enemy_gard = random.choice(list_job)
                list_enemy_items = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                    'all_potion_high', 'all_potion_middle', 'all_potion_low']
                # 적수호대 사용할 아이템 선택
                str_enemy_use_item = random.choice(list_enemy_items)
                # HP포션 사용
                if str_enemy_use_item == 'hp_potion_high':
                    print("필드 HP(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'hp_potion_middle':
                    print("필드 HP(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'hp_potion_low':
                    print("필드 HP(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

                # MP포션 사용
                elif str_enemy_use_item == 'mp_potion_high':
                    print("필드 MP(상) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['mp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'mp_potion_middle':
                    print("필드 MP(중) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'mp_potion_low':
                    print("필드 MP(하) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

                # ALL포션 사용
                elif str_enemy_use_item == 'all_potion_high':
                    print("필드 ALL(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'all_potion_middle':
                    print("필드 ALL(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'all_potion_low':
                    print("필드 ALL(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

        # 던전에서 적군수호대 조우
        if self.bool_meet_maze_gard:
            # 일반공격
            if int_enemy_choice_act == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(list_job)
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 유저수호대 피해자 공격받아 hp감소
                if self.use_hp_up:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * (
                            1 + random.randint(5, 7) / 10)
                    print(self.dict_user_gard[str_choice_user_gard]['hp'])
                    print(self.dict_enemy_gard[str_choice_enemy_gard]['power'])
                    print(1 + random.randint(5, 7) / 10)
                    print('던전1층 백법사의 hp_up 버프마법 사용함')
                    self.use_hp_up = False
                elif self.use_fire_wall:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.5
                    print("던전1층 파이어월 발동")
                    self.use_fire_wall = False
                elif self.use_thunder_breaker:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.6
                    print("던전1층 썬더브레이커 발동")
                    self.use_thunder_breaker = False
                elif self.use_bilzzard:
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.7
                    print("던전1층 블리자드 발동")
                    self.use_bilzzard = False
                else:  # 버프없음
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power']
                    print("던전1층 총공격")
            # 1층 : 적군 수호대 레벨 20~25
            elif int_enemy_choice_act == 2 and self.int_floor == 1:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 던전 1층에서 궁수 스킬사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(2, 5) / 10)
                        print("던전1층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(4, 6) / 10)
                        print("던전1층 아처 듀얼샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(5, 7) / 10)
                        print("던전1층 아처 마스터샷 발동")
                # 던전 1층에서 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                      'power'] * random.randint(2, 50)
                    print("던전1층 수아드맨 스킬 사용")
                # 던전 1층에서 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    # 흑법사 레벨 25미만인 경우
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 25:
                        skill_num = random.choice([1, 15, 20])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                              'power'] * 1.3
                            print("던전1층 흑법사 파이어볼 발동")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("던전1층 흑법사 파이어 월 발동", self.use_fire_wall)
                        else:
                            self.use_thunder_breaker = True
                            print("던전1층 흑법사 썬더 브레이커 스킬 발동", self.use_thunder_breaker)
                    # 흑법사 레벨 25이상이 경우
                    else:
                        skill_num = random.choice([1, 15, 20, 25])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        if str_enemy_skill == 'fire_ball':
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                              'power'] * 1.3
                            print("던전1층 흑법사 레벨 25 이상 파이어볼 발동")
                        elif str_enemy_skill == 'fire_wall':
                            self.use_fire_wall = True
                            print("던전1층 흑법사 레벨 25이상 파이어 월 발동", self.use_fire_wall)
                        elif str_enemy_skill == 'thunder_breaker':
                            self.use_thunder_breaker = True
                            print("던전1층 흑법사 레벨 25이상 썬더 브레이커 발동", self.use_thunder_breaker)
                        else:
                            self.use_bilzzard = True
                            print("던전1층 흑법사 레벨 25이상 블리자드 발동", self.use_bilzzard)
                # 던전1층 백법사 스킬사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    # 적수호대 힐 대상
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * random.randint(
                            3, 7) / 10
                        print("던전1층 백법사 힐 노말 스킬 발동")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("던전1층 백법사 에이치업 스킬 발동", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * random.randint(
                            6, 10) / 10
                        print("던전1층 백법사 힐그레이터 스킬 발동")
                # 던전1층 적법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    # 적법사 레벨 25미만
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 25:
                        skill_num = random.choice([1, 15, 20])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                         * random.randint(3, 7) / 10
                                print("던전1층 적법사 레벨 25미만 힐 노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                                  'power'] * 1.3
                                print("던전1층 적법사 레벨 25미만 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                         * random.randint(6, 10) / 10
                                print("던전1층 적법사 레벨 25 미만 힐 그레이터 발동")
                            else:  # fire_wall인 경우
                                self.use_fire_wall = True
                                print("던전1층 적법사 레벨 25 미만 파이어 월 발동", self.use_fire_wall)
                        # skill_num == 20
                        else:
                            self.use_thunder_breaker = True
                            print("던전1층 적법사 레벨 25 미만 썬더 브레이커 발동", self.use_thunder_breaker)

                    else:  # 25레벨
                        skill_num = random.choice([1, 15, 20, 25])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                         * random.randint(3, 7) / 10
                                print("던전1층 적법사 레벨 25일때 힐노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                                  'power'] * 1.3
                                print("던전1층 적법사 레벨 25일때 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                         * random.randint(6, 10) / 10
                                print("던전1층 적법사 레벨 25일때 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전1층 적법사 레벨 25일때 파이어 월 발동", self.use_fire_wall)
                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전1층 적법사 레벨 25일때 썬더 브레이커 발동", self.use_thunder_breaker)
                        else:  # 25인 경우
                            self.use_bilzzard = True
                            print("던전1층 적법사 레벨 25일때 블리자드 발동", self.use_bilzzard)

            # 2층 적수호대 : 26~30레벨
            elif int_enemy_choice_act == 2 and self.int_floor == 2:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(2, 5) / 10)
                        print("던전2층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(4, 6) / 10)
                        print("던전2층 아처 듀얼 샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(5, 7) / 10)
                        print("던전2층 아처 마스터샷 발동")
                # 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                      'power'] * random.randint(2, 50)
                    print("던전2층 수아드맨 스킬 발동")
                # 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    skill_num = random.choice([1, 15, 20, 25])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'fire_ball':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.3
                        print("던전2층 흑법사 파이어볼 발동")
                    elif str_enemy_skill == 'fire_wall':
                        self.use_fire_wall = True
                        print("던전2층 흑법사 파이어 월 발동", self.use_fire_wall)
                    elif str_enemy_skill == 'thunder_breaker':
                        self.use_thunder_breaker = True
                        print("던전2층 흑법사 썬더 브레이커 발동", self.use_thunder_breaker)
                    else:
                        self.use_bilzzard = True
                        print("던전2층 흑법사 블리자드 발동", self.use_bilzzard)

                # 백법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_white':
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 30:
                        skill_num = random.choice([1, 10, 15])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        str_heal_enemy = random.choice(
                            ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                     * random.randint(3, 7) / 10
                            print("던전2층 백법사 레벨 30미만 힐 노말 발동")
                        elif str_enemy_skill == 'hp_up':
                            self.use_hp_up = True
                            print("던전2층 백법사 레벨 30미만 에이치피 업 발동", self.use_hp_up)
                        elif str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                     * random.randint(6, 10) / 10
                            print("던전2층 백법사 레벨 30미만 힐 그레이터 발동")
                    else:
                        skill_num = random.choice([1, 10, 15, 30])
                        str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                        str_heal_enemy = random.choice(
                            ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                     * random.randint(3, 7) / 10
                            print("던전2층 백법사 레벨 30일때 힐 노말 발동")
                        elif str_enemy_skill == 'hp_up':
                            self.use_hp_up = True
                            print("던전2층 백법사 레벨 30일때 에이치피 업 발동", self.use_hp_up)
                        elif str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                     self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                            print("던전2층 백법사 레벨 30일때 힐 그레이터 발동")
                        else:  # heal_all 사용
                            ratio = random.randint(4, 8) / 10
                            for i in list_job:
                                self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                            print("던전2층 백법사 레벨 30일때 힐 올 사용")

                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if self.dict_enemy_gard[str_choice_enemy_gard]['lv'] < 30:
                        skill_num = random.choice([1, 15, 20, 25])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                         self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                                print("던전2층 레벨 30미만 적법사 힐노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                                  'power'] * 1.3
                                print("던전2층 레벨 30미만 적법사 파이어 볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                         self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                                print("던전2층 적법사 레벨 30미만 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전2층 적법사 레벨 30미만 파이어 볼 발동", self.use_fire_wall)

                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전2층 적법사 레벨 30미만 썬더브레이커 발동", self.use_thunder_breaker)

                        else:  # 25인 경우
                            self.use_bilzzard = True
                            print("던전2층 적법사 레벨 30미만 블리자드 발동", self.use_bilzzard)

                    else:  # 레벨 30일때
                        skill_num = random.choice([1, 15, 20, 25, 30])
                        if skill_num == 1:
                            str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                            if str_enemy_skill == 'heal_normal':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(3, 7) * \
                                                                         self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                                print("던전2층 레벨 30 이상 적법사 힐 노말 발동")
                            else:
                                self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                                  'power'] * 1.3
                                print("던전2층 레벨 30이상 적법사 파이어볼 발동")
                        elif skill_num == 15:
                            str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                            if str_enemy_skill == 'heal_greater':
                                self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                         self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                                print("던전2층 적법사 레벨 30이상 힐 그레이터 발동")
                            else:
                                self.use_fire_wall = True
                                print("던전2층 적법사 레벨 30이상 파이어 월 발동", self.use_fire_wall)

                        elif skill_num == 20:
                            self.use_thunder_breaker = True
                            print("던전2층 적법사 레벨 30이상 썬더 브레이커 발동", self.use_thunder_breaker)

                        elif skill_num == 25:
                            self.use_bilzzard = True
                            print("던전2층 적법사 레벨 30이상 블리자드 발동", self.use_bilzzard)
                        else:  # 레벨 30
                            ratio = random.randint(4, 8) / 10
                            for i in list_job:
                                self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                            print("던전2층 적법사 레벨 30이상 힐올 발동")

            # 3층 이상(30이상)
            elif int_enemy_choice_act == 2 and self.int_floor >= 3:
                # 적수호대 공격자 선택
                str_choice_enemy_gard = random.choice(['archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                # 유저수호대 피해자 선택
                str_choice_user_gard = random.choice(list_job)
                # 궁수 스킬 사용
                if str_choice_enemy_gard == 'archer':
                    skill_num = random.choice([10, 15, 20])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'target_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(2, 5) / 10)
                        print("던전3층 아처 타겟샷 발동")
                    elif str_enemy_skill == 'dual_shot':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(4, 6) / 10)
                        print("던전3층 아처 듀얼샷 발동")
                    else:
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] \
                                                                      * (1 + random.randint(5, 7) / 10)
                        print("던전3층 마스터샷 발동")
                # 검사 스킬 사용
                elif str_choice_enemy_gard == 'swordman':
                    self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                      'power'] * random.randint(2, 50)
                    print("던전3층 검사 스킬 발동")
                # 흑법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_black':
                    skill_num = random.choice([1, 15, 20, 25])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    if str_enemy_skill == 'fire_ball':
                        self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard]['power'] * 1.3
                        print("던전3층 흑법사 파이어볼 발동")
                    elif str_enemy_skill == 'fire_wall':
                        self.use_fire_wall = True
                        print("던전3층 흑법사 파이어 월 발동", self.use_fire_wall)
                    elif str_enemy_skill == 'thunder_breaker':
                        self.use_thunder_breaker = True
                        print("던전3층 흑법사 썬더 브레이커 발동", self.use_thunder_breaker)
                    else:
                        self.use_bilzzard = True
                        print("던전3층 흑법사 블리자드 발동", self.use_bilzzard)

                # 백법사 스킬 사용
                elif str_choice_enemy_gard == 'wizard_white':
                    skill_num = random.choice([1, 10, 15, 30])
                    str_enemy_skill = self.dict_enemy_gard[str_choice_enemy_gard]['skill'][skill_num]
                    str_heal_enemy = random.choice(
                        ['warrior', 'archer', 'swordman', 'wizard_red', 'wizard_black', 'wizard_white'])
                    if str_enemy_skill == 'heal_normal':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                 * random.randint(3, 7) / 10
                        print("던전3층 백법사 힐 노말 발동")
                    elif str_enemy_skill == 'hp_up':
                        self.use_hp_up = True
                        print("던전3층 백법사 에이치피 업 발동", self.use_hp_up)
                    elif str_enemy_skill == 'heal_greater':
                        self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                 * random.randint(6, 10) / 10
                        print("던전3층 백법사 힐 그레이터 발동")
                    else:  # heal_all 사용
                        ratio = random.randint(4, 8) / 10
                        for i in list_job:
                            self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                        print("던전3층 백법사 힐 올 발동")

                elif str_choice_enemy_gard == 'wizard_red':
                    str_heal_enemy = random.choice(['warrior', 'archer', 'swordman', 'wizard_red',
                                                    'wizard_black', 'wizard_white'])
                    skill_num = random.choice([1, 15, 20, 25, 30])
                    if skill_num == 1:
                        str_enemy_skill = random.choice(['heal_normal', 'fire_ball'])
                        if str_enemy_skill == 'heal_normal':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] \
                                                                     * random.randint(3, 7) / 10
                            print("던전3층 적법사 힐 노말 발동")
                        else:
                            self.dict_user_gard[str_choice_user_gard]['hp'] -= self.dict_enemy_gard[str_choice_enemy_gard][
                                                                              'power'] * 1.3
                            print("던전3층 적법사 파이어 볼 발동")
                    elif skill_num == 15:
                        str_enemy_skill = random.choice(['heal_greater', 'fire_wall'])
                        if str_enemy_skill == 'heal_greater':
                            self.dict_enemy_gard[str_heal_enemy]['hp'] += random.randint(6, 10) * \
                                                                     self.dict_enemy_gard[str_heal_enemy]['max_hp'] / 10
                            print("던전3층 적법사 힐 그레이터 발동")
                        else:
                            self.use_fire_wall = True
                            print("던전3층 적법사 파이어 월 발동", self.use_fire_wall)
                    elif skill_num == 20:
                        self.use_thunder_breaker = True
                        print("던전3층 적법사 선더 브레이커 발동", self.use_thunder_breaker)
                    elif skill_num == 25:
                        self.use_bilzzard = True
                        print("던전3층 적법사 블리자드 발동", self.use_bilzzard)
                    else:  # 레벨 30
                        ratio = random.randint(4, 8) / 10
                        for i in list_job:
                            self.dict_enemy_gard[i]['hp'] += self.dict_enemy_gard[i]['max_hp'] * ratio
                        print("던전3층 적법사 힐 올 발동")

            # 아이템 사용
            else:
                # 적수호대 공격자(아이템 사용자) 선택
                str_choice_enemy_gard = random.choice(list_job)
                list_enemy_items = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low',
                                    'mp_potion_high', 'mp_potion_middle', 'mp_potion_low',
                                    'all_potion_high', 'all_potion_middle', 'all_potion_low']
                str_enemy_use_item = random.choice(list_enemy_items)
                if str_enemy_use_item == 'hp_potion_high':
                    print("던전 HP(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                elif str_enemy_use_item == 'hp_potion_middle':
                    print("던전 HP(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                elif str_enemy_use_item == 'hp_potion_low':
                    print("던전 HP(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3

                # MP포션 사용
                elif str_enemy_use_item == 'mp_potion_high':
                    print("던전 MP(상) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['mp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.7
                elif str_enemy_use_item == 'mp_potion_middle':
                    print("던전 MP(중) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.5
                elif str_enemy_use_item == 'mp_potion_low':
                    print("던전 MP(하) 포션 사용")
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.3
                # ALL포션 사용
                elif str_enemy_use_item == 'all_potion_high':
                    print("던전 ALL(상) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.7
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.7

                elif str_enemy_use_item == 'all_potion_middle':
                    print("던전 ALL(중) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.5
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.5

                elif str_enemy_use_item == 'all_potion_low':
                    print("던전 ALL(하) 포션 사용")
                    self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_choice_enemy_gard]['max_hp'] * 0.3
                    # self.dict_enemy_gard[str_choice_enemy_gard]['hp'] += self.dict_enemy_gard[str_heal_enemy]['max_hp'] * 0.3


a = My(False, True, 1, {})
for i in range(1, 1000):
    a.enemy_gard_atk()




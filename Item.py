class ItemClass():
    def __init__(self):
        # 직업 리스트
        self.list_job = ['warrior', 'archer', 'swordsman', 'wizard_red', 'wizard_black', 'wizard_white']

    # 체력회복
    def use_hp_potion(self, str_job, str_item, dict_grad):
        if str_item == 'HP_potion_high':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.7
        elif str_item == 'HP_potion_middle':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.5
        elif str_item == 'HP_potion_low':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.3
        return dict_grad[str_job]['HP']

    # 마나회복
    def use_mp_potion(self, str_job, str_item, dict_grad):
        if str_item == 'MP_potion_high':
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.7
        elif str_item == 'MP_potion_middle':
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.5
        elif str_item == 'MP_potion_low':
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.3
        return dict_grad[str_job]['MP']

    # 체력,마나회복
    def use_all_potion(self, str_job, str_item, dict_grad):
        if str_item == 'All_potion_high':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.7
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.7
        elif str_item == 'All_potion_middle':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.5
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.5
        elif str_item == 'All_potion_low':
            dict_grad[str_job]['HP'] += dict_grad[str_job]['Max_HP'] * 0.3
            dict_grad[str_job]['MP'] += dict_grad[str_job]['Max_MP'] * 0.3
        return dict_grad[str_job]['HP'], dict_grad[str_job]['MP']

    # 전투불능 상태인 클래스 모두 부활
    def use_resurrection_potion(self, dict_grad):
        for job in self.list_job:
            dict_grad[job]['survival'] = True

    # 텐트 사용: 구성원 전부 체력 100% 회복
    def use_tent(self, str_job, dict_grad):
        for job in self.list_job:
            dict_grad[job]['hp'] = dict_grad[str_job]['max_hp']

    # 아이템 획득
    def get_item(self):
        pass

    # 아이템창 갱신
    def renew_item_view(self):
        pass

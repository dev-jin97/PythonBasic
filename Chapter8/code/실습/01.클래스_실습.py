
"""
영철은 스타트 게임스 회사에 개발자로 취직을 하게 되었다.
지난주 회의 결과로 신작 MMORPG 게임의 아이템 구성안을 만들었다.

아이템 공통: 이름, 가격, 무게, 판매하기, 버리기
장비 아이템: 착용 효과, 착용하기
소모품 아이템: 사용 효과, 사용하기
(단, 버리기는 버릴 수 있는 아이템만 가능하다.)
"""


# 부모 클래스
class Item:
    def __init__(self, name, price, weight, is_dropable):
        self.name = str(name)
        self.price = int(price)
        self.weghit = float(weight)
        self.is_dropable = bool(is_dropable)

    # 아이템 판매
    def sale(self):
        print(f"아이템 <{self.name}>을 ${self.price}에 판매하셨습니다.")

    # 아이템 버리기
    def discard(self):
        if self.is_dropable is True:
            print(f"아이템 <{self.name}>을 버리셨습니다.")
        else:
            print(f"아이템 <{self.name}>을 버리지 못합니다.")
    def info(self):
        main_panel = "[Item Information]\n" \
                     f"<{self.name}>\n" \
                     f"{self.weghit}kg\n" \
                     f"{self.price} $\n" \
                     f"Drop : {'가능' if self.is_dropable is True else '불가능'}"
        print(main_panel)


# 자식 클래스
class WearableItem(Item):
    def __init__(self, name, price, weight, is_dropable, effect):
        super().__init__(name, price, weight, is_dropable)
        self.effect = effect

    def wear(self):
        print(f"{self.name}을 착용하셨습니다! 착용효과 -> {self.effect}")


# 자식 클래스
class UsableItem(Item):
    def __init__(self, name, price, weight, is_dropable, effect):
        super().__init__(name, price, weight, is_dropable)
        self.effect = effect

    def use(self):
        print(f"{self.name}을 사용하셨습니다! 사용효과 -> {self.effect}")


# 인스턴스 생성
sword = WearableItem("이가닌자의 검", 30000, 3.5, True, "체력 5000 증가, 마력 5000 증가")
sword.wear()
print()
sword.sale()
print()
sword.discard()

print()
portion = UsableItem("신비한 투명 물약", 150000, 0.1, False, "3분간 은신 상태")
portion.discard()
portion.use()

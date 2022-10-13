# 클래스를 사용하는 이유
# 리그오브레전드를 사용해보자.

# 클래스를 사용하지 않았을 때
champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신 것을 환영합니다.")
champion2_name = "리신"
champion2_health = 800
champion2_attack = 90

print(f"{champion2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")


basic_attack(champion1_name, champion1_attack)

basic_attack(champion2_name, champion2_attack)

# 클래스 사용
print("==============클래스를 사용했을 때==============")


class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")

    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")


ezreal  = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)

ezreal.basic_attack()
leesin.basic_attack()
"""
클래스를 추가하지 않았을 경우 변수를 할당하고 함수에 데이터를 넣는 작업이 끊임없이 반복되지만
클래스는 속도면 코드 길이면에서 더욱 경량화된다.
"""
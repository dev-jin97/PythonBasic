class Monster:
    def say(self):
        print("나는 몬스터다.")


# 클래스 사용
goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다

a = 10
b = "문자열객체"
c = True

# 각 자료형 클래스 타입
print(type(a))
print(type(b))
print(type(c))

# 문자열 객체 함수
print(b.__dir__())
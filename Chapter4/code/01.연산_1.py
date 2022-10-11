# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 5
y = 2

print(x + y) 
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱

# - 문자열 연산
# 인스타 그램 해시태그
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3 
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" * 5 # 문자열의 곱하기 연산
print(message)

# -복합할당연산자
level = 10 # (레벨 1 증가)
level += 1 # 코드 구문을 줄여줄 수 있음. level = level + 1

health = 2000 # (체력 300 감소)
health -= 300 # health = health - 300

attack = 300 # (공격력 1.5배 증가)
attack *= 1.5

speed = 420 # (이동속동 50% 감소)
speed /= 2

print(level, health, attack, speed)
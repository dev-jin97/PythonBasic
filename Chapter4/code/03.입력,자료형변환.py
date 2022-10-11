# 입력

# 자료형 변환

x = input("첫번째 숫자를 입력하세요 >>> ")
y = input("두번째 숫자를 입력하세요 >>> ")

add = int(x) + int(y) # 자료형 변환을 안했을 시 2040, int형 변환시 60
str_add = x + y # 자료형 변환을 안했을 시 2040, int형 변환시 60

print(add, str_add)
# 입력

# 자료형 변환

x = input("첫번째 숫자를 입력하세요 >>> ")
y = input("두번째 숫자를 입력하세요 >>> ")

add = int(x) + int(y) # 자료형 변환을 안했을 시 2040, int형 변환시 60
str_add = x + y # 자료형 변환을 안했을 시 2040, int형 변환시 60

print(add, str_add)

# 사용자로부터 태어난 연도를 입력받으면, 현재 나이를 출력하기

'''
표준입력 
태어난 연도를 입력하세요 >>> 1994 

표준출력
현재나이는 28세입니다.
'''
import datetime

dt_now = datetime.datetime.now()

current_year = dt_now.year

age_calculator = input("태어난 연도를 입력하세요 >>> ")

current_age = current_year - int(age_calculator)

print("현재 나이는 만{}세입니다.".format(current_age))
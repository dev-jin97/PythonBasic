
"""
현동이는 강의를 8시간 동안 들으니, 배가 너무 고파 저녁을 먹기로 하였다. 현동이가 현재 가진
금액을 통해 최대로 먹을 수 있는 음식을 출력해 주는 프로그램을 작성해 보자.

조건) 20000원 이상 : 치킨, 10000원 이상: 떡복이, 2000원 이상: 편의점 김밥
"""

my_money = int(input("현재 가진 금액을 입력 >>> "))

if my_money >= 20000:
    print("오늘 저녁은...치킨!")
elif my_money >= 10000:
    print("오늘 저녁은...떡볶이!")
elif my_money >= 2000:
    print("오늘 저녁은...편의점 김밥!")
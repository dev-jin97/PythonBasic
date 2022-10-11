
"""
턱걸이 평균 측정 프로그램을 만들어보자. 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다.
그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다. 리스트에 저장된 데이터의
평균을 구해 출력한다.
"""

health_list = list()

for i in range(7):
    health_list.append(int(input("{}일차 턱걸이 횟수 >>> ".format(str(i + 1)))))


total = 0
for j in health_list:
    total += j

avg_score = total / 7

print(int(avg_score))

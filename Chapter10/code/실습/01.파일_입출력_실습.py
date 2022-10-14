import os
import csv
"""
보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을 작성해보자.
mystock.csv 로부터 종목, 매입가, 수량, 목표가 정보를 가져온다.

수익금 = (목표가 - 매입가) * 수량
수익률 = (목표가 / 매입가) * 100
"""

# mystock.csv Write
data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER", 380000, 5, 400000]
]

if not os.path.isfile("mystock.csv"):
    with open("mystock.csv", 'w', encoding='utf-8-sig', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for d in data:
            csv_writer.writerow(d)


file = open("mystock.csv", 'r', encoding='utf-8-sig')
reader = csv.reader(file)
next(reader)
for line in reader:
    line_3 = int(line[3])
    line_2 = int(line[2])
    line_1 = int(line[1])

    option1 = (line_3 - line_1) * line_2
    option2 = (line_3 / line_1 -1) * 100

    print(f"{line[0]} {option1} {option2:.2f}%")
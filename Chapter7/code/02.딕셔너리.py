# 딕셔너리
# : 사전형태의 자료형

# 딕셔너리 만들기
stock_a = {"samsung": 82000, "Lg" : 150000}

stock_b = {
        "samsung": [82000, 81500, 83000, 82000],
        "Lg": (150000, 140000, 160000, 170000)
}

stock_c = {
    "samsung": {
        "current_value": 82000,
        "qty": 5,
        "price": 81000
    }
}

#  딕셔너리 접근
print(stock_a["samsung"]) # 키에 해당하는 값이 출력
print(stock_c["samsung"]["price"]) # 딕셔너리 안에 딕셔너리도 컨트롤 가능

# 딕셔너리 할당
stock_a["samsung"] = 90000
print(stock_a)

# 딕셔너리 삭제
del stock_a["Lg"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "samsung": 82000,
    "sk": 123000,
    "Naver": 370000,
    "Kakao": 133000
}
# items()   : 키와 데이터 쌍

for item in stock_d.items():
    print(item, end=" ")
print()
# keys() : 키
for key in stock_d.keys():

    print(key, end=" ")
print()
# values() : 데이터
for value in stock_d.values():
    print(value, end=" ")

# 01. 조건문 개념

# 조건문
# : 조건에 따라 실행할 명령이 달라지는 것

origin_pass = "1234"
input_path = input("패스워드를 입력하세요 >>> ")

if input_path == origin_pass:
    # 조건 A 참

    print("로그인 성공!")
    print("반갑습니다.")
elif input_path == "":
    # 조건 A 거짓, 조건 B 참

    print("아무것도 입력하지 않았습니다.")
else:
    # 비교연산의 결과가 False일 경우
    # 조건 A 거짓, 조건 B 거짓

    print("로그인 실패! 다시 시도해주세요!")

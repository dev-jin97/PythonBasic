
"""
패스트 게임즈에 인턴으로 근무하게 된 종현. 사수에게 과제로 게임 메뉴 만들기를 받았다.
과제내용은 다음과 같았다.

숫자 1 : "게임을 시작합니다."
숫자 2 : "실시간 랭킹"
숫자 3 : "게임을 종료합니다."
"""

while True:
    main_panel = "[메뉴를 입력하세요.]\n" \
                 "1. 게임시작 2. 랭킹보기. 3.게임종료"
    x = int(input(f"{main_panel} >>> "))

    if x == 1:
        print("-> 게임을 시작합니다.")
    elif x == 2:
        print("-> 실시간 랭킹")
    elif x == 3:
        print("-> 프로그램을 종료합니다.")
        break
    else:
        print("-> 다시 입력해 주세요.")



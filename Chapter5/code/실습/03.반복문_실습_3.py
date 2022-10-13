
"""
성민은 한국대학교에 Lily라는 이름의 교환학생과 친해지게 되었다. 영어를 잘하지 못했던 성민은, Lily에게
한국어를 가르쳐 주기 위해 한국어 연습 프로그램을 만들게 되었다.

연습할 한국어가 담긴 리스트를 만든다.
리스트에서 순서대로 단어를 가져와 화면에 출력한다.
프로그램 사용자는 단어를 그대로 입력하고
맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료
"""

korean_list = ["사랑해", "귀엽다", "고마워", "행복해"]
print(len(korean_list))
i = 0
while True:

    main_panel = "[Let's Learning Korean!]\n" \
                 f"{korean_list[i]}\n"
    text_ipt = input(f"{main_panel}>>>")

    if text_ipt == korean_list[i]:
        i += 1
        if i == len(korean_list):
            print("과제 완료!!!")
            break
    else:
        print("틀렸습니다. 처음부터 다시 시도해보세요!!")
        break



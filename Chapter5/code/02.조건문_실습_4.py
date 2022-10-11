
"""
프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다.
세 과목의 평균점수가 80점 이상이면 합격인 프로그램이 오류가 생겼다.
80점 이상일 경우 불합격이 표시되도록 하고 0<=N<=100 범위를 벗어나면 "잘못 입력하셨습니다." 표기!
"""

korean = int(input("국어 >>> "))
math = int(input("수학 >>> "))
english = int(input("영어 >>> "))

if (100 >= korean >= 0) and (100 >= math >= 0) and (100 >= english >= 0):
    avg_score = (korean + math + english)/3
    if avg_score >= 80:
        print("불합격!")
    else:
        print("합격!")
else:
    print("잘못 입력하셨습니다.")
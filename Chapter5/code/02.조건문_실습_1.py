
"""
회사를 그만두게 된 유진이는 유튜브를 시작하게 되었다. 그리고, 유튜브를 통해 수익창출을 하려고 한다.
프로그램 사용자로부터 현재 구독자 수를 입력 받으면, 수익 창출이 가능한지 불가능한지 알려주는 프로그램을 작성해보자.
(단, 수익창출은 구독자가 1000명 이상일 경우 가능하다.)
"""

subscribe_total = 1000

current_my_subscribe = int(input("현재 구독자 수를 입력하세요 >>> "))

if current_my_subscribe >= subscribe_total:
    print("수익창출이 가능합니다!")
else:
    print("수익창출이 불가능합니다!")

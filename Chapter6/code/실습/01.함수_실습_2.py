
"""
로또에 당첨 되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추출 프로그램을 파이썬으로 작성하려고 한다.
다음 조건에 따라 김로또의 프로그램을 완성해보자.

1. 로또 번호 6개를 생성하자.
2. 로또 번호는 1~45까지의 랜덤 번호
3. 6개 숫자 모두 달라야 한다.
"""
import random


def get_random_number():
    number = random.randint(1, 45)

    return number


lotto_list = list()

i = 0
while i < 6:
    random_num = get_random_number()
    if random_num not in lotto_list:
        lotto_list.append(random_num)
        lotto_list.sort()
        i += 1


for item in lotto_list:
    print(f"{item}", end=" ")
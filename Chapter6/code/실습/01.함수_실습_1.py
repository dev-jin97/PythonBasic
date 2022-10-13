
"""
세 개의 정수를 인자로 받아, 합계와 평균을 출력해주는 함수이다. 함수를 호출한 결과로 표준출력이 나오도록 함수를 정의해보자.
"""

def printSumAvg(x, y, z):
    sum = x + y + z
    avg = int(sum / 3)

    print(f"합게 : {sum} 평균 : {avg}")


printSumAvg(10, 20, 30)
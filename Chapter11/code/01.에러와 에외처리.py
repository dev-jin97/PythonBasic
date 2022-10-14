# 원화를 입력, 환율 입력 --> 달러값

won = input("원화 금액을 입력하세요 >>> ")
doller = input("환율을 입력하세요 >>> ")
try : # 예외가 발생할 수 있는 코드
    print(int(won) / int(doller))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print(f"예외발생 : {e}")
except ZeroDivisionError as e:
    print(f"예외발생 : {e}")
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("항상 실행되는 코드")

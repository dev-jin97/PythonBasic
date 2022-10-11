# 1. 비교연산
print("비교연산 -----")
print(2 > 3) # False
print(15 < 30) # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("팙팙" == "팙팙") # True
print("팙팙" != "팙팙") # False

# 2. 논리연산
print("논리연산 -----")
print(4 < 6 and 10 >= 10) # True and True  = True
print('포기' != "포기" or "나는" == "나는") # False or True = True
print(not 6==6) # not True = False

# 3. 멤버십 연산
print("멤버십 연산문제 -----")
print("a" in "abc") # 포함되어 있다면 True
print("d" not in "abc") # 포함되어 있지 않다면 True
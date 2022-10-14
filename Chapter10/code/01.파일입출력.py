# 1. 파일 쓰기
file = open("data.txt", "w", encoding='utf-8-sig')
file.write("1. 슬기로운 파이썬 코딩!")
file.close()

# 2. 파일 추가
file = open("data.txt", "a", encoding='utf-8-sig')
file.write("\n2. 다시 한 번 화이팅!")
file.close()

# 3. 파일 읽기
file = open("data.txt", "r", encoding='utf-8-sig')

# 3.1 파일 전체 읽기
total_data = file.read()
print(total_data)
file.close()

# 3.2 파일 한줄 읽기
file = open("data.txt", "r", encoding='utf-8-sig')
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()
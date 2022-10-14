# 1. 파이썬 객체를 pickle로 저장하기
import pickle

data = {
    "add1": "data1",
    "add2": "data2"
}

file = open("data.pickle", "wb")
pickle.dump(data, file)
file.close()

# 2. pickle 파일 파이썬으로 가져오기
file = open("data.pickle", "rb")
data = pickle.load(file)
print(data)

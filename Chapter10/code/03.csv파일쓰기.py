import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 7],
    ["형돈", 6, 10]
]

file = open("student.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()
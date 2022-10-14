import csv

file = open("student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)

for line in reader:
    print(line)
file.close()
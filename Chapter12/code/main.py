"""
post.csv file path
"""
import csv
import os.path
import time
from post import Post

file_path = "data/post.csv"

# Post instance List
post_list = list()

if os.path.isfile(file_path):
    #
    print("=============Post Content Loading.....=============")
    time.sleep(0.5)
    f = open(file_path, 'r', encoding='utf-8-sig')
    reader = csv.reader(f)
    for data in reader:
        # Make a Post Instance
        post = Post(int(data[0]), data[1], data[2], data[3])
        post_list.append(post)

else:
    # Make a File
    f = open(file_path, 'w', encoding='utf-8-sig', newline='')
    f.close()
print(post_list[0].get_title())
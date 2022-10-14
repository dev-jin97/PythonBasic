"""
post.csv file path
"""
import csv
import os.path
import time
from post import Post


def clear_console():
    for i in range(30):
        print()


def sentence_view(sentence, timesl=0.1):
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)


file_path = "data/post.csv"

# Post instance List
post_list = list()

if os.path.isfile(file_path):
    #
    clear_console()
    print("=============Post Content Loading.....=============")
    time.sleep(1)

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

clear_console()
"""
Make a Main Panel
"""


main_trigger = True

main_panel = "_________________________________________________________________\n" \
             "                      Welcome to My BLOG!😁                    \n" \
             "                       Hyeon jin's Blog👨🏻‍                       \n" \
             "-----------------------------------------------------------------\n" \
             "--====-| 1. Write Post | 2. Post List | 3. Program Exit |-====--\n" \

end_panel = "_________________________________________________________________\n" \
            "                        Thank you! Bye😭                         \n" \
            "-----------------------------------------------------------------\n" \

if __name__ == '__main__':

    while True:
        print(main_panel)
        input_btn = input(">>>> ")

        if input_btn == "3":

            clear_console()
            print(end_panel)

            break

        if input_btn == "2":

            break

        if input_btn == "1":
            clear_console()

            while True:
                sentence_view("원하는 글을 작성해보세요!\n")

                title = input("제목 : ")
                contents = input("내용 : ")
                if title == "":
                    print("제목이 비어있습니다.")
                elif contents == "":
                    print("내용이 비어있습니다.")
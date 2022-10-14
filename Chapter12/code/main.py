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


def write_post():
    """
    게시글 쓰기 함수
    """
    print("게시글 쓰기 ----")
    title = input("제목 : ")
    content = input("내용 : ")

    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("게시글 작성완료!")
    clear_console()


def list_post():
    """
    게시글 목록
    """
    id_list = list()

    while True:
        for post in post_list:
            print(f"No({post.get_id()}). {post.get_title()} || {post.get_view_count()}회 조회 수")
            id_list.append(post.get_id())

        print("Q) 글 번호를 선택해주세요(메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            id = int(input(">>> "))
        except ValueError:
            print("숫자를 입력해주세요!")
        else:
            if id in id_list:
                clear_console()
                detail_post(id)
            elif id == -1:
                clear_console()
                break
            else:
                print("없는 글 번호입니다.")


def detail_post(id):
    """
    글 상세 페이지
    """
    print("게시글 상세 내용 ----")

    for post in post_list:
        if post.get_id() == id:
            # 조회수 1증가
            post.add_view_count()
            print(f"번호 : {post.get_id()}")
            print(f"제목 : {post.get_title()}")
            print(f"본문 : {post.get_content()}")
            print(f"조회수 : {post.get_view_count()}")
            target_post = post

    while True:
        print("수정 : 1 삭제: 2")
        try:
            choice = int(input(">>> "))

            if choice == 1:
                update_post(target_post)
                break
            elif choice ==2:
                delete_post(target_post)
                break
            elif choice == -1:
                clear_console()
                break
            else:
                print("잘못 입력하셨습니다.")
        except ValueError:
            print("숫자를 입력해 주세요!")


def update_post(target_post):
    """게시글 수정"""
    print("게시글 수정------")
    title = input('제목 ㅣ ')
    content = input("본문 | ")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("# 게시글이 수정되었습니다!")
    time.sleep(1)
    clear_console()


def delete_post(target_post):
    post_list.remove(target_post)
    print("# 게시글이 삭제되었습니다.")
    time.sleep(1)
    clear_console()


def save():
    """게시글 저장"""
    file = open(file_path, 'w', encoding='utf-8', newline='')

    writer = csv.writer(file)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    file.close()

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
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
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
        try:
            choice = int(input(">>>> "))
        except ValueError:
            print("숫자를 입력해주세요!")
        else:

            if choice == 1:
                clear_console()

                write_post()

            elif choice == 2:
                clear_console()

                list_post()
            elif choice == 3:
                clear_console()
                save()

                print(end_panel)
                break
            else:
                print("다시 입력해주세요!")
                time.sleep(1)
                clear_console()



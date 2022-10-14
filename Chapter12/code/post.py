class Post:
    """
    todo [게시물 클래스]
    post_id = 글 번호
    post_title = 글 제목
    post_content = 글 내용
    post_view_count = 조회수
    """
    def __init__(self, post_id, post_title, post_content, post_view_count):
        self.id = post_id
        self.title = post_title
        self.content = post_content
        self.view_count = post_view_count

    def set_post(self, post_id, post_title, post_content, post_view_count):
        self.id = post_id
        self.title = post_title
        self.content = post_content
        self.view_count = post_view_count

    def add_view_count(self):
        self.view_count += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return  self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count


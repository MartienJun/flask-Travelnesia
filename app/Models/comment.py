# Class ini digunakan untuk menyimpan data Comment dari database travelnesia
class Comment:
    # Constructor ini digunakan untuk inisialiasi data dari class Comment
    def __init__(self, comment_id, post_id, username, content, vote):
        self.comment_id = comment_id
        self.post_id = post_id
        self.username = username
        self.content = content
        self.vote = vote

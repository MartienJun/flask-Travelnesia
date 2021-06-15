# Class ini digunakan untuk menyimpan data Post dari database travelnesia
class Post:
    # Constructor ini digunakan untuk inisialiasi data dari class Post
    def __init__(self, post_id, title, username, location, location_rating, transport, vote, budget, content):
        self.post_id = post_id
        self.title = title
        self.username = username
        self.location = location
        self.location_rating = location_rating
        self.transport = transport
        self.vote = vote
        self.budget = budget
        self.content = content

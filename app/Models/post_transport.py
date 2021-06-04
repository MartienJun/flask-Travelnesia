# Class ini digunakan untuk menyimpan data Post_transport dari database travelnesia
class Post_transport:
    # Constructor ini digunakan untuk inisialiasi data dari class Post_transport
    def __init__(self, id, post_id, transport_id):
        self.id = id
        self.post_id = post_id
        self.transport_id = transport_id

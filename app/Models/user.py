# Class ini digunakan untuk menyimpan data User dari database travelnesia
class User:
    # Constructor ini digunakan untuk inisialiasi data dari class User
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password

from flask_login import UserMixin
# Class ini digunakan untuk menyimpan data User dari database travelnesia
class User(UserMixin):
    # Constructor ini digunakan untuk inisialiasi data dari class User
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password
    
    def get_id(self):
           return (self.username)

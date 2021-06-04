# Class ini digunakan untuk menyimpan data Profile dari database travelnesia
class Profile:
    # Constructor ini digunakan untuk inisialiasi data dari class Profile
    def __init__(self, username, name, email, telp, profile_pict):
        self.username = username
        self.name = name
        self.email = email
        self.telp = telp
        self.profile_pict = profile_pict

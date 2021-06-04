from app.my_database import MyDatabase
from app.Models.profile import Profile


# Sebuah Controller untuk mengakses Tabel profile pada database travelnesia
class ProfileController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel profile dalam database travelnesia
    @staticmethod
    def insert(profile):
        MyDatabase.execute_and_commit(
            "INSERT into profile VALUES(%s, %s, %s, %s, %s)",
            [ profile.username, profile.name, profile.email, profile.telp, profile.profile_pict ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel profile dalam database travelnesia
    @staticmethod
    def update(profile):
        MyDatabase.execute_and_commit(
            "UPDATE profile SET name=%s, email=%s, telp=%s, profile_pict=%s WHERE username=%s",
            [ profile.name, profile.email, profile.telp, profile.profile_pict, profile.username]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel profile dalam database travelnesia berdasarkan username
    @staticmethod
    def delete(username):
        MyDatabase.execute_and_commit(
            "DELETE FROM profile where username=%s",
            [ username ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel profile dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM profile")

        # Setiap hasil data profile dari database travelnesia disimpan ke dalam model profile
        list_profile = []
        for profile in hasil:
            list_profile += [ Profile(*profile) ]

        return list_profile

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel profile dalam database travelnesia berdasarkan username
    @staticmethod
    def get_by_id(username):
        hasil = MyDatabase.query(
            "SELECT * FROM profile where username=%s",
            [ username ]
        )

        m = None
        # Jika username tersebut berhasil ditemukan
        if hasil:
            profile = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Profile(*profile)

        return m

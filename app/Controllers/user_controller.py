from app.my_database import MyDatabase
from app.Models.user import User


# Sebuah Controller untuk mengakses Tabel user pada database travelnesia
class UserController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel user dalam database travelnesia
    @staticmethod
    def insert(user):
        MyDatabase.execute_and_commit(
            "INSERT into user VALUES(%s, %s, %s)",
            [ user.username, user.role, user.password ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel user dalam database travelnesia
    @staticmethod
    def update(user):
        MyDatabase.execute_and_commit(
            "UPDATE user SET role=%s, password=%s WHERE username=%s",
            [ user.role, user.password, user.username]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel user dalam database travelnesia berdasarkan username
    @staticmethod
    def delete(username):
        MyDatabase.execute_and_commit(
            "DELETE FROM user where username=%s",
            [ username ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel user dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM user")

        # Setiap hasil data user dari database travelnesia disimpan ke dalam model user
        list_user = []
        for user in hasil:
            list_user += [ User(*user) ]

        return list_user

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel user dalam database travelnesia berdasarkan username
    @staticmethod
    def get_by_id(username):
        hasil = MyDatabase.query(
            "SELECT * FROM user where username=%s",
            [ username ]
        )

        m = None
        # Jika username tersebut berhasil ditemukan
        if hasil:
            user = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = User(*user)

        return m

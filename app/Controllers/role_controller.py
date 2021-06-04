from app.my_database import MyDatabase
from app.Models.role import Role


# Sebuah Controller untuk mengakses Tabel role pada database travelnesia
class RoleController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel role dalam database travelnesia
    @staticmethod
    def insert(role):
        MyDatabase.execute_and_commit(
            "INSERT into role VALUES(%s, %s)",
            [ role.role_id, role.role_name ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel role dalam database travelnesia
    @staticmethod
    def update(role):
        MyDatabase.execute_and_commit(
            "UPDATE role SET role_name=%s WHERE role_id=%s",
            [ role.role_name, role.role_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel role dalam database travelnesia berdasarkan role_id
    @staticmethod
    def delete(role_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM role where role_id=%s",
            [ role_id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel role dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM role")

        # Setiap hasil data role dari database travelnesia disimpan ke dalam model role
        list_role = []
        for role in hasil:
            list_role += [ Role(*role) ]

        return list_role

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel role dalam database travelnesia berdasarkan role_id
    @staticmethod
    def get_by_id(role_id):
        hasil = MyDatabase.query(
            "SELECT * FROM role where role_id=%s",
            [ role_id ]
        )

        m = None
        # Jika role_id tersebut berhasil ditemukan
        if hasil:
            role = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Role(*role)

        return m

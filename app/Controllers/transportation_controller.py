from app.my_database import MyDatabase
from app.Models.transportation import Transportation


# Sebuah Controller untuk mengakses Tabel transportation pada database travelnesia
class TransportationController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel transportation dalam database travelnesia
    @staticmethod
    def insert(transportation):
        MyDatabase.execute_and_commit(
            "INSERT into transportation VALUES(%s, %s, %s)",
            [ transportation.transport_id, transportation.transport, transportation.type ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel transportation dalam database travelnesia
    @staticmethod
    def update(transportation):
        MyDatabase.execute_and_commit(
            "UPDATE transportation SET transport=%s, type=%s WHERE transport_id=%s",
            [ transportation.transport, transportation.type, transportation.transport_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel transportation dalam database travelnesia berdasarkan transport_id
    @staticmethod
    def delete(transport_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM transportation where transport_id=%s",
            [ transport_id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel transportation dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM transportation")

        # Setiap hasil data transportation dari database travelnesia disimpan ke dalam model transportation
        list_transportation = []
        for transportation in hasil:
            list_transportation += [ Transportation(*transportation) ]

        return list_transportation

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel transportation dalam database travelnesia berdasarkan transport_id
    @staticmethod
    def get_by_id(transport_id):
        hasil = MyDatabase.query(
            "SELECT * FROM transportation where transport_id=%s",
            [ transport_id ]
        )

        m = None
        # Jika transport_id tersebut berhasil ditemukan
        if hasil:
            transportation = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Transportation(*transportation)

        return m

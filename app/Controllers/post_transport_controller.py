from app.my_database import MyDatabase
from app.Models.post_transport import Post_transport


# Sebuah Controller untuk mengakses Tabel post_transport pada database travelnesia
class Post_transportController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel post_transport dalam database travelnesia
    @staticmethod
    def insert(post_transport):
        MyDatabase.execute_and_commit(
            "INSERT into post_transport VALUES(%s, %s, %s)",
            [ post_transport.id, post_transport.post_id, post_transport.transport_id ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel post_transport dalam database travelnesia
    @staticmethod
    def update(post_transport):
        MyDatabase.execute_and_commit(
            "UPDATE post_transport SET post_id=%s, transport_id=%s WHERE id=%s",
            [ post_transport.post_id, post_transport.transport_id, post_transport.id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel post_transport dalam database travelnesia berdasarkan id
    @staticmethod
    def delete(id):
        MyDatabase.execute_and_commit(
            "DELETE FROM post_transport where id=%s",
            [ id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel post_transport dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM post_transport")

        # Setiap hasil data post_transport dari database travelnesia disimpan ke dalam model post_transport
        list_post_transport = []
        for post_transport in hasil:
            list_post_transport += [ Post_transport(*post_transport) ]

        return list_post_transport

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel post_transport dalam database travelnesia berdasarkan id
    @staticmethod
    def get_by_id(id):
        hasil = MyDatabase.query(
            "SELECT * FROM post_transport where id=%s",
            [ id ]
        )

        m = None
        # Jika id tersebut berhasil ditemukan
        if hasil:
            post_transport = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Post_transport(*post_transport)

        return m

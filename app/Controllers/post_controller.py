from app.my_database import MyDatabase
from app.Models.post import Post


# Sebuah Controller untuk mengakses Tabel post pada database travelnesia
class PostController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel post dalam database travelnesia
    @staticmethod
    def insert(post):
        MyDatabase.execute_and_commit(
            "INSERT into post VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
            [ post.post_id, post.title, post.username, post.location, post.location_rating, post.vote, post.budget, post.content ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel post dalam database travelnesia
    @staticmethod
    def update(post):
        MyDatabase.execute_and_commit(
            "UPDATE post SET title=%s, username=%s, location=%s, location_rating=%s, vote=%s, budget=%s, content=%s WHERE post_id=%s",
            [ post.title, post.username, post.location, post.location_rating, post.vote, post.budget, post.content, post.post_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel post dalam database travelnesia berdasarkan post_id
    @staticmethod
    def delete(post_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM post where post_id=%s",
            [ post_id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel post dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM post")

        # Setiap hasil data post dari database travelnesia disimpan ke dalam model post
        list_post = []
        for post in hasil:
            list_post += [ Post(*post) ]

        return list_post

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel post dalam database travelnesia berdasarkan post_id
    @staticmethod
    def get_by_id(post_id):
        hasil = MyDatabase.query(
            "SELECT * FROM post where post_id=%s",
            [ post_id ]
        )

        m = None
        # Jika post_id tersebut berhasil ditemukan
        if hasil:
            post = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Post(*post)

        return m

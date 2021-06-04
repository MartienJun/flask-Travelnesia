from app.my_database import MyDatabase
from app.Models.comment import Comment


# Sebuah Controller untuk mengakses Tabel comment pada database travelnesia
class CommentController:
    # Fungsi insert digunakan untuk memasukan data ke Tabel comment dalam database travelnesia
    @staticmethod
    def insert(comment):
        MyDatabase.execute_and_commit(
            "INSERT into comment VALUES(%s, %s, %s, %s, %s)",
            [ comment.comment_id, comment.post_id, comment.username, comment.content, comment.vote ]
        )

    # Fungsi update digunakan untuk men-update data ke Tabel comment dalam database travelnesia
    @staticmethod
    def update(comment):
        MyDatabase.execute_and_commit(
            "UPDATE comment SET post_id=%s, username=%s, content=%s, vote=%s WHERE comment_id=%s",
            [ comment.post_id, comment.username, comment.content, comment.vote, comment.comment_id]
        )

    # Fungsi delete digunakan untuk menghapus data dari Tabel comment dalam database travelnesia berdasarkan comment_id
    @staticmethod
    def delete(comment_id):
        MyDatabase.execute_and_commit(
            "DELETE FROM comment where comment_id=%s",
            [ comment_id ]
        )

    # Fungsi get_all digunakan untuk menerima semua data dari Tabel comment dalam database travelnesia
    @staticmethod
    def get_all():
        hasil = MyDatabase.query("SELECT * FROM comment")

        # Setiap hasil data comment dari database travelnesia disimpan ke dalam model comment
        list_comment = []
        for comment in hasil:
            list_comment += [ Comment(*comment) ]

        return list_comment

    # Fungsi get_by_id digunakan untuk menerima data dari Tabel comment dalam database travelnesia berdasarkan comment_id
    @staticmethod
    def get_by_id(comment_id):
        hasil = MyDatabase.query(
            "SELECT * FROM comment where comment_id=%s",
            [ comment_id ]
        )

        m = None
        # Jika comment_id tersebut berhasil ditemukan
        if hasil:
            comment = hasil[0]
            # Hasil data yang didapat dari database disimpan dalam model
            m = Comment(*comment)

        return m

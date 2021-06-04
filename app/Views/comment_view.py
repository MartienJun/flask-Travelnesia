from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.comment_controller import CommentController
from app.Models.comment import Comment
from app.Controllers.post_controller import PostController
from app.Controllers.user_controller import UserController


# Insialisasi Blueprint dengan url_prefix comment
blueprint = Blueprint("comment", __name__, url_prefix="/admin/comment")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("Views/comment/view.html", list_comment=CommentController.get_all(), list_post=PostController.get_all(), list_user=UserController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("Views/comment/insert.html", list_post=PostController.get_all(), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    comment_id = request.form['comment_id']
    post_id = request.form['post_id']
    username = request.form['username']
    content = request.form['content']
    vote = request.form['vote']

    # Cek apakah comment_id sudah ada dalam database
    if CommentController.get_by_id(comment_id) is not None:
        # jika iya, tampilkan error message
        return render_template('Views/comment/insert.html', message="comment_id sudah pernah terdaftar!", list_post=PostController.get_all(), list_user=UserController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    comment = Comment(comment_id, post_id, username, content, vote)
    CommentController.insert(comment)

    # Redirect ke halaman view
    return redirect(url_for('comment.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("Views/comment/update.html", comment=CommentController.get_by_id(id), list_post=PostController.get_all(), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    comment_id = request.form['comment_id']
    post_id = request.form['post_id']
    username = request.form['username']
    content = request.form['content']
    vote = request.form['vote']

    # Update data tersebut ke dalam database melalui model
    comment = Comment(comment_id, post_id, username, content, vote)
    CommentController.update(comment)

    # Redirect kembali ke view
    return redirect(url_for('comment.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    CommentController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('comment.view'))

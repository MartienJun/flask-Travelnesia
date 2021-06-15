from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.comment import Comment
from app.Controllers.comment_controller import CommentController
from app.Controllers.post_controller import PostController
from app.Controllers.user_controller import UserController


# Insialisasi Blueprint dengan url_prefix comment
blueprint = Blueprint("comment", __name__, url_prefix="/admin/comment")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
@login_required
def view():
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("Views/comment/view.html", list_comment=CommentController.get_all(), list_post=PostController.get_all(), list_user=UserController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert/<id>', methods=['GET', 'POST'])
@login_required
def insert(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))

    # Jika metodenya adalah post, dapatkan data dari post
    comment_id = None
    post_id = id
    username = request.form['username'] 
    content = request.form['content']
    vote = None

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    comment = Comment(comment_id, post_id, username, content, vote)
    CommentController.insert(comment)

    # Redirect ke halaman view
    return redirect(url_for('post.detail', id=id))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
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
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))

    # Hapus data tersebut dari database
    CommentController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('post.detail', id=id))

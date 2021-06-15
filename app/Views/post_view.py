from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.post import Post
from app.Controllers.post_controller import PostController
from app.Controllers.transportation_controller import TransportationController
from app.Controllers.user_controller import UserController
from app.Controllers.comment_controller import CommentController



# Insialisasi Blueprint dengan url_prefix post
blueprint = Blueprint("post", __name__, url_prefix="/admin/post")


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
    return render_template("admin/post/view_post.html", list_post=PostController.get_all(), list_user=UserController.get_all(), list_transport=TransportationController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
@login_required
def insert():
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/post/insert.html", list_user=UserController.get_all(), list_transport=TransportationController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    post_id = None
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    transport = request.form['transport']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    post = Post(post_id, title, username, location, location_rating, transport, vote, budget, content)
    PostController.insert(post)

    # Redirect ke halaman view
    return redirect(url_for('post.view'))


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
        return render_template("admin/post/update.html", post=PostController.get_by_id(id), list_user=UserController.get_all(), list_transport=TransportationController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    post_id = request.form['post_id']
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    transport = request.form['transport']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    # Update data tersebut ke dalam database melalui model
    post = Post(post_id, title, username, location, location_rating, transport, vote, budget, content)
    PostController.update(post)

    # Redirect kembali ke view
    return redirect(url_for('post.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))

    # Hapus data tersebut dari database
    PostController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('post.view'))


# Routing untuk halaman post detail
@blueprint.route('/detail/<id>', methods=['POST', 'GET'])
@login_required
def detail(id):
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))

    return render_template(
        "admin/post/post.html",
        post=PostController.get_by_id(id),
        list_transport=TransportationController.get_all(),
        list_comment=CommentController.get_all()
    )
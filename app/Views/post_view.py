from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.post_controller import PostController
from app.Models.post import Post
from app.Controllers.user_controller import UserController


# Insialisasi Blueprint dengan url_prefix post
blueprint = Blueprint("post", __name__, url_prefix="/admin/post")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/post/view_post.html", list_post=PostController.get_all(), list_user=UserController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("Views/post/insert.html", list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    post_id = request.form['post_id']
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    # Cek apakah post_id sudah ada dalam database
    if PostController.get_by_id(post_id) is not None:
        # jika iya, tampilkan error message
        return render_template('Views/post/insert.html', message="post_id sudah pernah terdaftar!", list_user=UserController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    post = Post(post_id, title, username, location, location_rating, vote, budget, content)
    PostController.insert(post)

    # Redirect ke halaman view
    return redirect(url_for('post.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("Views/post/update.html", post=PostController.get_by_id(id), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    post_id = request.form['post_id']
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    # Update data tersebut ke dalam database melalui model
    post = Post(post_id, title, username, location, location_rating, vote, budget, content)
    PostController.update(post)

    # Redirect kembali ke view
    return redirect(url_for('post.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    PostController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('post.view'))
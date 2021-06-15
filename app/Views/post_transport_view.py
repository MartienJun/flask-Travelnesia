from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.post_transport import Post_transport
from app.Controllers.post_controller import PostController
from app.Controllers.post_transport_controller import Post_transportController
from app.Controllers.transportation_controller import TransportationController


# Insialisasi Blueprint dengan url_prefix post_transport
blueprint = Blueprint("post_transport", __name__, url_prefix="/admin/post_transport")


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
    return render_template("admin/post_transport/view.html", list_post_transport=Post_transportController.get_all(), list_post=PostController.get_all(), list_transportation=TransportationController.get_all())


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
        return render_template("admin/post_transport/insert.html", list_post=PostController.get_all(), list_transportation=TransportationController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    id = request.form['id']
    post_id = request.form['post_id']
    transport_id = request.form['transport_id']

    # Cek apakah id sudah ada dalam database
    if Post_transportController.get_by_id(id) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/post_transport/insert.html', message="id sudah pernah terdaftar!", list_post=PostController.get_all(), list_transportation=TransportationController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    post_transport = Post_transport(id, post_id, transport_id)
    Post_transportController.insert(post_transport)

    # Redirect ke halaman view
    return redirect(url_for('post_transport.view'))


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
        return render_template("admin/post_transport/update.html", post_transport=Post_transportController.get_by_id(id), list_post=PostController.get_all(), list_transportation=TransportationController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    id = request.form['id']
    post_id = request.form['post_id']
    transport_id = request.form['transport_id']

    # Update data tersebut ke dalam database melalui model
    post_transport = Post_transport(id, post_id, transport_id)
    Post_transportController.update(post_transport)

    # Redirect kembali ke view
    return redirect(url_for('post_transport.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
@login_required
def delete(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))

    # Hapus data tersebut dari database
    Post_transportController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('post_transport.view'))

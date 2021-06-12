from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.user_controller import UserController
from app.Models.user import User
from app.Controllers.role_controller import RoleController
from app.Models.profile import Profile
from app.Controllers.profile_controller import ProfileController


# Insialisasi Blueprint dengan url_prefix user
blueprint = Blueprint("user", __name__, url_prefix="/admin/user")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/user/view.html", list_user=UserController.get_all(), list_role=RoleController.get_all(), list_profile=ProfileController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/user/insert.html", list_role=RoleController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    role = request.form['role']
    password = request.form['password']
    profile_pict = request.files['profile_pict']

    # Cek apakah username sudah ada dalam database
    if UserController.get_by_id(username) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/user/insert.html', message="username sudah pernah terdaftar!", list_role=RoleController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    user = User(username, role, password)
    profile = Profile(username, name, email, telp, profile_pict.filename)
    UserController.insert(user)
    ProfileController.insert(profile)

    # Redirect ke halaman view
    return redirect(url_for('user.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("admin/user/update.html", user=UserController.get_by_id(id), list_role=RoleController.get_all(), list_profile=ProfileController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    role = request.form['role']
    password = request.form['password']
    profile_pict = request.files['profile_pict']

    # Update data tersebut ke dalam database melalui model
    user = User(username, role, password)
    profile = Profile(username, name, email, telp, profile_pict.filename)
    UserController.insert(user)
    ProfileController.insert(profile)

    # Redirect kembali ke view
    return redirect(url_for('user.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    UserController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('user.view'))
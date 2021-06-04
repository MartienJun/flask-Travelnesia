from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.profile_controller import ProfileController
from app.Models.profile import Profile
from app.Controllers.user_controller import UserController


# Insialisasi Blueprint dengan url_prefix profile
blueprint = Blueprint("profile", __name__, url_prefix="/admin/profile")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("Views/profile/view.html", list_profile=ProfileController.get_all(), list_user=UserController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("Views/profile/insert.html", list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    profile_pict = request.form['profile_pict']

    # Cek apakah username sudah ada dalam database
    if ProfileController.get_by_id(username) is not None:
        # jika iya, tampilkan error message
        return render_template('Views/profile/insert.html', message="username sudah pernah terdaftar!", list_user=UserController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    profile = Profile(username, name, email, telp, profile_pict)
    ProfileController.insert(profile)

    # Redirect ke halaman view
    return redirect(url_for('profile.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("Views/profile/update.html", profile=ProfileController.get_by_id(id), list_user=UserController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    profile_pict = request.form['profile_pict']

    # Update data tersebut ke dalam database melalui model
    profile = Profile(username, name, email, telp, profile_pict)
    ProfileController.update(profile)

    # Redirect kembali ke view
    return redirect(url_for('profile.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    ProfileController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('profile.view'))

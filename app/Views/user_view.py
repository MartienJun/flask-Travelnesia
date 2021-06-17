import os
import app
from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.user import User
from app.Models.profile import Profile
from app.Controllers.user_controller import UserController
from app.Controllers.role_controller import RoleController
from app.Controllers.profile_controller import ProfileController


# Insialisasi Blueprint dengan url_prefix user
blueprint = Blueprint("user", __name__, url_prefix="/admin/user")


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
    return render_template("admin/user/view.html", list_user=UserController.get_all(), list_role=RoleController.get_all(), list_profile=ProfileController.get_all())


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
        return render_template("admin/user/insert.html", list_role=RoleController.get_all())

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    role = request.form['role']
    password = request.form['password']
    profile_pict = request.files['profile_pict']
    p_pict = profile_pict.filename

    # Cek apakah username sudah ada dalam database
    if UserController.get_by_id(username) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/user/insert.html', message="username sudah pernah terdaftar!", list_role=RoleController.get_all())

    # Jika profile picture tidak diisi
    if p_pict == "":
        p_pict = "default_profile.png"
    
    # Jika ekstensi file sesuai
    if app.allowed_image(p_pict) is True:
        # Save kedalam folder
        profile_pict.save(os.path.join(app.file_path, p_pict))
    else:
        return render_template('admin/user/insert.html', message="Ekstensi file tidak sesuai! Hanya bisa menampung file JPG, JPEG, dan PNG", list_role=RoleController.get_all())

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    user = User(username, role, password)
    profile = Profile(username, name, email, telp, p_pict)
    UserController.insert(user)
    ProfileController.insert(profile)


    # Redirect ke halaman view
    return redirect(url_for('user.view'))


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
        return render_template("admin/user/update.html", user=UserController.get_by_id(id), list_role=RoleController.get_all(), profile=ProfileController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    role = request.form['role']
    password = request.form['password']
    profile_pict = request.files['profile_pict']
    p_pict = profile_pict.filename

    # Jika profile picture tidak diisi
    if p_pict == "":
        p_pict = ProfileController.get_by_id(id).profile_pict

    # Jika ekstensi file sesuai
    if app.allowed_image(p_pict) is True:
        # Jika nama file != file default profile pict
        if p_pict != 'default_profile.png':
            # Hapus file
            os.remove(os.path.join(app.file_path, ProfileController.get_by_id(id).profile_pict))

        profile_pict.save(os.path.join(app.file_path, p_pict))
    else:
        return render_template('admin/user/insert.html', message="Ekstensi file tidak sesuai! Hanya bisa menampung file JPG, JPEG, dan PNG", list_role=RoleController.get_all())
    
    # Update data tersebut ke dalam database melalui model
    user = User(username, role, password)
    profile = Profile(username, name, email, telp, p_pict)
    UserController.update(user)
    ProfileController.update(profile)

    # Redirect kembali ke view
    return redirect(url_for('user.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Hapus data tersebut dari database
    
    # Jika nama file != file default profile pict
    if ProfileController.get_by_id(id).profile_pict != 'default_profile.png':
        # Hapus file
        os.remove(os.path.join(app.file_path, ProfileController.get_by_id(id).profile_pict))

    UserController.delete(id)



    # Redirect kembali ke View
    return redirect(url_for('user.view'))
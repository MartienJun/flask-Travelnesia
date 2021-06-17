import os
import app
from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.user import User
from app.Models.profile import Profile
from app.Controllers.profile_controller import ProfileController
from app.Controllers.role_controller import RoleController
from app.Controllers.user_controller import UserController


# Insialisasi Blueprint dengan url_prefix profile
blueprint = Blueprint("profile", __name__, url_prefix="/admin/profile")


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
    return render_template("admin/profile/view.html", profile=ProfileController.get_by_id(current_user.username), list_role=RoleController.get_all(), user=UserController.get_by_id(current_user.username))


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
        return render_template("admin/profile/update.html", profile=ProfileController.get_by_id(id), list_role=RoleController.get_all(), user=UserController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    telp = request.form['telp']
    role = request.form['role']
    password = request.form['password']
    profile_pict = request.files['profile_pict']

    # Jika profile picture tidak diisi
    if profile_pict.filename == "":
        if ProfileController.get_by_id(id).profile_pict != "default_profile.png":
                # Hapus file
                os.remove(os.path.join(app.file_path, ProfileController.get_by_id(id).profile_pict))
                
        profile_pict.filename = "default_profile.png"
    else:
        if app.allowed_image(profile_pict.filename) is True:
            # Jika nama file != file default profile pict
            if ProfileController.get_by_id(id).profile_pict != "default_profile.png":
                # Hapus file
                os.remove(os.path.join(app.file_path, ProfileController.get_by_id(id).profile_pict))
            
            profile_pict.save(os.path.join(app.file_path, profile_pict.filename))
        else:
            return render_template('admin/user/insert.html', message="Ekstensi file tidak sesuai! Hanya bisa menampung file JPG, JPEG, dan PNG", list_role=RoleController.get_all())
    
    # Update data tersebut ke dalam database melalui model
    user = User(username, role, password)
    profile = Profile(username, name, email, telp, profile_pict.filename)
    UserController.update(user)
    ProfileController.update(profile)

    # Redirect kembali ke view
    return redirect(url_for('profile.view'))
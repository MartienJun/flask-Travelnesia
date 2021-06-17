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


blueprint = Blueprint("user_profile", __name__, url_prefix="/user/profile")


@blueprint.route('/')
@blueprint.route('/view')
@login_required
def view():
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    return render_template(
        "user/profile/view.html",
        profile=ProfileController.get_by_id(current_user.username)
    )


@blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    if request.method == 'GET':
        return render_template(
            "user/profile/update.html",
            profile=ProfileController.get_by_id(id)
        )

    username = ProfileController.get_by_id(id).username
    name = request.form['name']
    email = ProfileController.get_by_id(id).email
    telp = request.form['telp']
    role = 'usr'
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
    
    
    user = User(
        username,
        role,
        password
    )
    profile = Profile(
        username,
        name,
        email,
        telp,
        profile_pict.filename
    )
    UserController.update(user)
    ProfileController.update(profile)

    return redirect(url_for('user_profile.view'))
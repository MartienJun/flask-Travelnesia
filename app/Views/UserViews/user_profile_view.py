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
    p_pict = profile_pict.filename

    if p_pict == "":
        p_pict = ProfileController.get_by_id(id).profile_pict
    
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
        p_pict
    )
    UserController.update(user)
    ProfileController.update(profile)

    return redirect(url_for('user_profile.view'))
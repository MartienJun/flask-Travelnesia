from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.Models.user import User
from app.Models.profile import Profile
from app.Controllers.user_controller import UserController
from app.Controllers.role_controller import RoleController
from app.Controllers.profile_controller import ProfileController


# Insialisasi Blueprint dengan url_prefix auth
blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = UserController.get_by_id(username)

        if not user or not password or password != user.password:
            flash('Wrong credentials')
        else:
            # Remember user
            login_user(user, remember=True)

            if current_user.role == 'adm':
                return redirect(url_for('post.view'))
            else:
                print(current_user)
                return "Hello user"

    return render_template('auth/sign-in.html')


@blueprint.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('index'))
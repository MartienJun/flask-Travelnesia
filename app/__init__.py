from os.path import join, dirname, realpath
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_login.utils import login_user
from app.Views import auth, role_view, user_view, profile_view, transportation_view, post_view, comment_view
from app.Views.UserViews import user_post_view, user_comment_view, user_profile_view
from app.Controllers.user_controller import UserController
from app.my_database import MyDatabase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'travelnesia'

# Set database
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'travelnesia'
MyDatabase.mysql.init_app(app)



# Set direcotry upload
app.config['UPLOAD_FILE'] = join(dirname(realpath(__file__)), 'static/img') #os.path.realpath('.') + '/static/uploads'
file_path = app.config['UPLOAD_FILE']
app.config['ALLOWED_IMAGE_EXTENSION'] = ['JPEG', 'JPG', 'PNG']
file_ext = app.config['ALLOWED_IMAGE_EXTENSION']
app.config['MAX_IMAGE_SIZE'] = 2 * 1024 * 1024
file_size = app.config['MAX_IMAGE_SIZE']

# Set blueprint admin
app.register_blueprint(auth.blueprint)
app.register_blueprint(role_view.blueprint)
app.register_blueprint(user_view.blueprint)
app.register_blueprint(profile_view.blueprint)
app.register_blueprint(transportation_view.blueprint)
app.register_blueprint(post_view.blueprint)
app.register_blueprint(comment_view.blueprint)


# Set blueprint user
app.register_blueprint(user_post_view.blueprint)
app.register_blueprint(user_comment_view.blueprint)
app.register_blueprint(user_profile_view.blueprint)


 #Login manager settings
login_manager = LoginManager()
login_manager.login_view = 'auth.signin'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return UserController.get_by_id(id)


@app.route('/')
def index():
    if current_user.is_authenticated is True:
        if current_user.role == 'adm':
            return redirect(url_for('post.view'))
        
        return redirect(url_for('user_post.view'))

    return render_template("index.html")


def allowed_image(filename):
    if not '.' in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in file_ext:
        return True
    else:
        return False



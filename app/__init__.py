from flask import Flask, render_template
from flask_login import LoginManager
from app.Views import auth, role_view, user_view, profile_view, transportation_view, post_view, comment_view
from app.Views.UserViews import user_post_view, user_comment_view
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


 #Login manager settings
login_manager = LoginManager()
login_manager.login_view = 'auth.signin'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return UserController.get_by_id(id)


@app.route('/')
def index():
    return render_template("index.html")
from flask import Flask, Blueprint, session, render_template, redirect, url_for
from flask_login import LoginManager
from app.Views import auth, dashboard, role_view, user_view, profile_view, transportation_view, post_transport_view, post_view, comment_view
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


# Set blueprint
app.register_blueprint(auth.blueprint)
app.register_blueprint(dashboard.blueprint)
app.register_blueprint(role_view.blueprint)
app.register_blueprint(user_view.blueprint)
app.register_blueprint(profile_view.blueprint)
app.register_blueprint(transportation_view.blueprint)
app.register_blueprint(post_transport_view.blueprint)
app.register_blueprint(post_view.blueprint)
app.register_blueprint(comment_view.blueprint)


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
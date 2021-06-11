from app.Views.dashboard import dashboard
from flask import Flask, Blueprint, session
from app.Views import dashboard, role_view, user_view, profile_view, transportation_view, post_transport_view, post_view, comment_view
from app.my_database import MyDatabase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'travelnesia'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'travelnesia'
MyDatabase.mysql.init_app(app)


# Admin Views
app.register_blueprint(dashboard.blueprint)
app.register_blueprint(role_view.blueprint)
app.register_blueprint(user_view.blueprint)
app.register_blueprint(profile_view.blueprint)
app.register_blueprint(transportation_view.blueprint)
app.register_blueprint(post_transport_view.blueprint)
app.register_blueprint(post_view.blueprint)
app.register_blueprint(comment_view.blueprint)

@app.route('/')
def index():
    session['admin'] = 'admin'
    return "Ini index"
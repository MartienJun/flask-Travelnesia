from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.post import Post
from app.Controllers.post_controller import PostController
from app.Controllers.transportation_controller import TransportationController
from app.Controllers.user_controller import UserController
from app.Controllers.comment_controller import CommentController


blueprint = Blueprint("user_post", __name__, url_prefix="/user/post")


@blueprint.route('/')
@blueprint.route('/view')
@login_required
def view():
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    return render_template(
        "user/post/view_post.html",
        list_post=PostController.get_all(),
        list_transport=TransportationController.get_all()
    )


@blueprint.route('/insert', methods=['GET', 'POST'])
@login_required
def insert():
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    if request.method == 'GET':
        return render_template(
            "user/post/insert.html",
            list_user=UserController.get_all(),
            list_transport=TransportationController.get_all()
        )

    post_id = None
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    transport = request.form['transport']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    post = Post(
        post_id,
        title,
        username,
        location,
        location_rating,
        transport,
        vote,
        budget,
        content
    )
    PostController.insert(post)

    return redirect(url_for('user_post.view'))


@blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    if request.method == 'GET':
        return render_template(
            "admin/post/update.html",
            post=PostController.get_by_id(id),
            list_user=UserController.get_all(),
            list_transport=TransportationController.get_all()
        )

    post_id = request.form['post_id']
    title = request.form['title']
    username = request.form['username']
    location = request.form['location']
    location_rating = request.form['location_rating']
    transport = request.form['transport']
    vote = request.form['vote']
    budget = request.form['budget']
    content = request.form['content']

    post = Post(
        post_id,
        title,
        username,
        location,
        location_rating,
        transport,
        vote,
        budget,
        content
    )
    PostController.update(post)

    return redirect(url_for('user_post.view'))


@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    PostController.delete(id)

    return redirect(url_for('user_post.view'))


# Routing untuk halaman post detail
@blueprint.route('/detail/<id>', methods=['POST', 'GET'])
@login_required
def detail(id):
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    return render_template(
        "user/post/post.html",
        post=PostController.get_by_id(id),
        list_transport=TransportationController.get_all(),
        list_comment=CommentController.get_all()
    )
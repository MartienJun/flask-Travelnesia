from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.comment import Comment
from app.Controllers.comment_controller import CommentController
from app.Controllers.post_controller import PostController
from app.Controllers.user_controller import UserController


blueprint = Blueprint("user_comment", __name__, url_prefix="/user/comment")


@blueprint.route('/')
@blueprint.route('/view')
@login_required
def view():
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    return render_template(
        "user/comment/view.html",
        list_comment=CommentController.get_all(),
        list_post=PostController.get_all(),
        list_user=UserController.get_all()
    )


@blueprint.route('/insert/<id>', methods=['GET', 'POST'])
@login_required
def insert(id): #id in this case post id
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    comment_id = None
    post_id = id
    username = current_user.username
    content = request.form['content']
    vote = 0

    comment = Comment(
        comment_id,
        post_id,
        username,
        content,
        vote
    )
    CommentController.insert(comment)

    return redirect(url_for('user_post.detail', id=id))


@blueprint.route('/delete/<id>', methods=['POST', 'GET'])
@login_required
def delete(id): # id in this case is comment id
    if current_user.role != 'usr':
        flash("You must sign in to use this feature")
        return redirect(url_for('auth.signin'))

    post_id = CommentController.get_by_id(id).post_id

    CommentController.delete(id)

    return redirect(url_for('user_post.detail', id=post_id))

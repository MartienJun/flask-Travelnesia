from flask import Blueprint, render_template, request, redirect, url_for, session


# Insialisasi Blueprint dengan url_prefix user
blueprint = Blueprint("dashboard", __name__, url_prefix="/admin")


@blueprint.route('/')
def dashboard():
    if session.get('admin') is None:
        return redirect(url_for('home'))
    
    return redirect(url_for('post.view'))
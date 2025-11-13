from flask import Blueprint, render_template, request

home_bp = Blueprint('Home', __name__)

@home_bp.route('/')
def home_page():
    username = request.cookies.get('nome')
    return render_template('home.html', username=username)
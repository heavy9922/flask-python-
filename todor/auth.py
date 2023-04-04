from flask import (Blueprint, render_template,
                   request, url_for, flash, redirect)
from . import models

from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users(username, generate_password_hash(password))

        error = None

        user_name = Users.query.filter_by(username=username).first()

        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'{user_name} already exists'

        flash(error)
        
    return render_template('auth/register.html')


@bp.route('/login')
def login():
    return render_template('auth/login.html')

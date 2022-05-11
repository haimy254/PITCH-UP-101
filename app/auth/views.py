form flask import render_template,url_for,redirect
from . import auth
from ..models import User
from .forms import Registration
from .. import db

@auth.route('/login')
def login():
    return render_template(authentic/login.html)

@auth.route('/register', method=["GET","POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,pass_s=form.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('authentic/signup.html')

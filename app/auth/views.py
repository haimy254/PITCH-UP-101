# from turtle import title
# from app import main
from flask import render_template,url_for,redirect,flash, request
from flask_login import login_user, logout_user, login_required, login_form
from . import auth
from ..models import Login, User, LoginForm
from .forms import Registration
from .. import db


@auth.route('/login',method=["GET","POST"])
def login():
    def register():
        login_form = LoginForm()
        if login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()
            if user is not None and user.verify_hash(login_form.password.data):
                login_user(user,login_form.remember.data)
                return redirect(request.args.get('next')or url_for('main.index'))
            flash('Invalid username or Password')
            title = "pitch login"
        # return redirect(url_for('auth.login'))
    # return render_template('authentic/signup.html')
    return render_template('authentic/login.html', login_form=login_form ,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("/authentic.index.html"))

@auth.route('/register', method=["GET","POST"])
def signUp():
    form = Registration()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,pass_s=form.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('authentic/signup.html', registration_form=form)
 
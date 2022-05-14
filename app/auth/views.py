
from flask import render_template,url_for,redirect,flash, request
from flask_login import login_user, logout_user, login_required,current_user
from . import auth
from ..models import  User, Pitch
from .forms import PitchForm, RegistrationForm, LoginForm
from .. import db


@auth.route('/login',methods=["GET","POST"])
def login():
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_hash(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))
        flash('Invalid username or Password')
            
    title = "pitch login"
       
    return render_template('auth/login.html', login_form=login_form ,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register', methods=["GET","POST"])
def signUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,pass_s=form.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/signUp.html', registration_form=form)

@auth.route('/pitch', methods=["GET","POST"])
def pitch():
    form = PitchForm()
    if form.submit():
        description=form.description.data
        category= form.category.data
        # title =form.title.data
        pitch = Pitch (description=description,category=category,author_id=current_user.id)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('auth.pitch'))
    return render_template('auth/pitch.html', pitch_form=form)
 
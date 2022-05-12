from ..models import User
from flask import render_template,abort
from app import main

@main.route('/user/<uname>')
def profile(uname):
    user = user.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
         
    return render_template("profile/profile.html", user = user)
    


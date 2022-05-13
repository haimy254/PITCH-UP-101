
from ..models import User
from flask import render_template,abort, url_for
from . import main
# from .forms import UpdateProfile
from .. import db
from flask_login import login_required


@main.route('/')
def index():
    title= 'welcome'
         
    return render_template("index.html", title = title)



    


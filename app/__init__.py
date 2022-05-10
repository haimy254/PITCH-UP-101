from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app= Flask (__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()


    # Initializing flask extensions
bootstrap.init_app(app)
db.init_app(app)
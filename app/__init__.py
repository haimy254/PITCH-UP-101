from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy()

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    
   


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
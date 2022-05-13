import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://code_world:haimy@localhost/pitchone'
    
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://code_world:code00@localhost/users'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
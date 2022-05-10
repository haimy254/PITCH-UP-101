import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/pitch_up_101'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
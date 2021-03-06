from app import create_app, db
from flask_script import Manager,Server
from app.models import Pitch, User
from flask_migrate import Migrate, MigrateCommand
# from .. import db

app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
# @manager.command
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
    
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User,Pitch=Pitch)


if __name__ == '__main__':
    manager.run()
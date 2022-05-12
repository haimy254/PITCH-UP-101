# import email
from . import db
from wekzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.uqer_loader
def load_user(user_id):
        return User.query.get(int(user_id))
class User(db.model):
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key=True)
    username= db.column(db.string(300))
    email = db.column(db.string(300),unique=True, index=True)
    role_id = db.column(db.Integer,db.foreignkey('roles.id'))
    pass_s =db.Column(db.string(300))
    pitch = db.column(db.string(600))
    comments = db.column(db.string(600))
    likes = db.column(db.integer(1))
    dislike = db.column(db.integer(1))
    
    
    def __repr__(self):
        return f'User{self.username}'
    @property
    def password(self):
      raise AttributeError('this is restriced')
  
    @password.setter
    def password(self,password):
        self.pass_s = generate_password_hash(password)
        
    def verify_hash(self,password):
        return check_password_hash(self.pass_s, password)
  

class Role (db.model):
    __tablename__ ='roles'
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.string(300))
    user = db.relationship('User',backref='role', lazy="dynamic")
    
    def __repr__(self):
       return f'Role{self.title}'
   
class User(UserMixin,db.model):
    __tablename__= 'users'
    
    id = db.colmn(db.integer, primary_key = True)
    username= db.column(db.string(300))
    email = db.column(db.string(300),unique=True, index=True)
    role_id = db.column(db.Integer,db.foreignkey('roles.id'))
    password_s = db.colmn(db.string(300))
    
class Pitch(db.model):
    __tablename__ = 'pitches'
    
    id = db.colmn(db.integer, primary_key = True)
    username= db.column(db.string(300))
    email = db.column(db.string(300),unique=True, index=True)
    pitch = db.column(db.string(600))
    
    def __repr__(self):
       return f'Pitch{self.title}'
   
class Comment(db.model):
    __tablename__ = 'comments'
    
    id = db.colmn(db.integer, primary_key = True)
    username= db.column(db.string(300))
    pitch = db.column(db.string(600))
    comments = db.column(db.string(600))
    likes = db.column(db.integer(1))
    dislike = db.column(db.integer(1))
    
    def __repr__(self):
       return f'Comment{self.title}'

         
        
       
from unicodedata import category
from wsgiref import validate
from xmlrpc.client import DateTime
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, TextAreaField,SubmitField,PasswordField, BooleanField,ValidationError
from ..models import Upvote, User
from wtforms.validators import Required,Email,EqualTo


class RegistrationForm(FlaskForm):
    email = StringField("Your Email Address",validators=[Required(),Email()])
    username = StringField("Enter your username",validators = [Required()])
    password = PasswordField("Password",validators = [Required()])
    EqualTo("password_confirm",message = "Passwords must match")
    password_confirm = PasswordField("Confirm Passwords",validators = [Required()])
    submit = SubmitField("Sign Up")   
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError("There is an account with that email")  
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is taken")
        

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')     
    
class PitchForm(FlaskForm):
    
    description = StringField('Enter Your Pitch')
    category = StringField ('Enter Your Catergory')
    posted = DateTime('Day And Time Posted')
    author = StringField("Enter your username",validators = [Required()])
    comment =  StringField('Comment On The Post')
    upvote = Integer('Vote likes',default=1)
    downvote = Integer('Vote likes',default=1)
    
    
   
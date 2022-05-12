from wsgiref import validate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,PasswordField, BooleanField
from ..models import User
from wtforms import ValidartionError,InputRequired,Email,EqualTo


class Registration(FlaskForm):
    email = StringField('email address',validators =[InputRequired(),Email()])
    username = StringField('username',validators =[InputRequired(),Email()])
    password = StringField('password',validators =[InputRequired, EqualTo('password_confirm', message='password ')])
    password_confirm= PasswordField('confirm')
    submit = SubmitField('Register')
    
    def validate_username(self,data_field):
        if  User.query.filter_by(email=data_field.data).first():
            raise ValidartionError(' is already in use try another one')
        
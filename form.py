__author__ = 'trust'

from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(Form):
    newusername = TextField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(Form):
    firstname = TextField('Firstname', validators=[DataRequired()])
    surname = TextField('Surname', validators=[DataRequired()])
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from models import Users

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    apikey = StringField('apikey', validators=[DataRequired()])

class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message
        def __call__(self, form, field):
            email = form['email'].data
            password = field.data
            users = Users.query.filter_by(email=email).first()
            if users.password != password:
                raise ValueError('Wrong password')
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])